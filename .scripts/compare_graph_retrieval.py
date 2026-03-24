#!/usr/bin/env python3
"""
Reusable retrieval benchmark for comparing graph-augmented vault search against
the non-graph baseline in repositories that keep local search tooling under
`/.brains`.

Purpose:
- run the same representative query set against `hybrid` and `hybrid-graph`;
- compare retrieval quality using simple, inspectable metrics;
- surface whether graph expansion improves multi-note coverage or mostly adds noise.

Adapt first when reusing in another repository:
- replace `DEFAULT_CASES` with queries and relevant note aliases that fit the new vault;
- review `GOVERNANCE_FILES` if the repo has different root/governance pages;
- adjust `k`, `fetch_k`, and `graph_max_hops` if the retrieval policy differs;
- if the Python project is not under `/.brains`, update `project_root()` and `sys.path` wiring.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


REPO_ROOT = project_root()
BRAINS_PROJECT = REPO_ROOT / ".brains"
if str(BRAINS_PROJECT) not in sys.path:
    sys.path.insert(0, str(BRAINS_PROJECT))

from brains.sources.vault.search import search_vault_knowledge  # noqa: E402


GOVERNANCE_FILES = {
    "AGENTS.md",
    "README.md",
    "NOTICE.md",
    "AUDIT.md",
    "Home.md",
    "Index.md",
    "Індекс.md",
    "Головна.md",
    "Literature and Priorities.md",
    "Література та пріоритети.md",
}


@dataclass(frozen=True)
class BenchmarkCase:
    name: str
    category: str
    query: str
    expected_topics: tuple[tuple[str, ...], ...]
    notes: str = ""


@dataclass
class QueryRun:
    case_name: str
    category: str
    mode: str
    elapsed_seconds: float
    hit_at_1: int
    hit_at_3: int
    mrr: float
    topic_recall: float
    relevant_results: int
    governance_results: int
    graph_rows: int
    matched_topics: list[dict[str, Any]]
    result_paths: list[str]
    result_titles: list[str]


DEFAULT_CASES: tuple[BenchmarkCase, ...] = (
    BenchmarkCase(
        name="direct_pairformer",
        category="direct",
        query="pairformer",
        expected_topics=(("pairformer",),),
    ),
    BenchmarkCase(
        name="direct_diffusion_module",
        category="direct",
        query="diffusion module",
        expected_topics=(("diffusion module", "дифузійний модуль"),),
    ),
    BenchmarkCase(
        name="direct_featurization",
        category="direct",
        query="featurization",
        expected_topics=(("featurization",),),
    ),
    BenchmarkCase(
        name="direct_confidence_scores",
        category="direct",
        query="confidence scores",
        expected_topics=(("confidence scores", "ступінь впевненості"),),
    ),
    BenchmarkCase(
        name="direct_foldseek",
        category="direct",
        query="foldseek structure search",
        expected_topics=(("foldseek and structure search", "foldseek і пошук структур", "foldseek"),),
    ),
    BenchmarkCase(
        name="direct_msa",
        category="direct",
        query="multiple sequence alignment msa",
        expected_topics=(("msa", "multiple sequence alignment"),),
    ),
    BenchmarkCase(
        name="relation_pairformer_diffusion",
        category="relation",
        query="how is pairformer related to diffusion module",
        expected_topics=(
            ("pairformer",),
            ("diffusion module", "дифузійний модуль"),
        ),
    ),
    BenchmarkCase(
        name="relation_featurization_pairformer",
        category="relation",
        query="how does featurization connect to pairformer",
        expected_topics=(
            ("featurization",),
            ("pairformer",),
        ),
    ),
    BenchmarkCase(
        name="relation_confidence_diffusion",
        category="relation",
        query="how are confidence scores related to diffusion module",
        expected_topics=(
            ("confidence scores", "ступінь впевненості"),
            ("diffusion module", "дифузійний модуль"),
        ),
    ),
    BenchmarkCase(
        name="relation_msa_featurization",
        category="relation",
        query="how does msa connect to featurization",
        expected_topics=(
            ("msa", "multiple sequence alignment"),
            ("featurization",),
        ),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare hybrid vs hybrid-graph vault retrieval.")
    parser.add_argument(
        "--k",
        type=int,
        default=5,
        help="Final number of hits to compare.",
    )
    parser.add_argument(
        "--fetch-k",
        type=int,
        default=20,
        help="Number of candidates fetched before ranking.",
    )
    parser.add_argument(
        "--graph-max-hops",
        type=int,
        default=1,
        help="Graph expansion depth for hybrid-graph.",
    )
    parser.add_argument(
        "--json-output",
        action="store_true",
        help="Emit the full benchmark payload as JSON.",
    )
    return parser.parse_args()


def normalize(text: str) -> str:
    return text.casefold()


def topic_match_rank(topic_aliases: tuple[str, ...], results: list[dict[str, Any]]) -> tuple[int | None, list[str]]:
    aliases = [normalize(alias) for alias in topic_aliases]
    for row in results:
        haystack = " ".join(
            [
                str(row.get("title", "")),
                str(row.get("source_path", "")),
                str(row.get("section_path", "")),
            ]
        )
        haystack_norm = normalize(haystack)
        if any(alias in haystack_norm for alias in aliases):
            return int(row.get("rank", 0)) or None, list(topic_aliases)
    return None, list(topic_aliases)


def relevant_row_count(case: BenchmarkCase, results: list[dict[str, Any]]) -> int:
    count = 0
    normalized_topics = [[normalize(alias) for alias in group] for group in case.expected_topics]
    for row in results:
        haystack = normalize(
            " ".join(
                [
                    str(row.get("title", "")),
                    str(row.get("source_path", "")),
                    str(row.get("section_path", "")),
                ]
            )
        )
        if any(any(alias in haystack for alias in group) for group in normalized_topics):
            count += 1
    return count


def run_case(case: BenchmarkCase, *, mode: str, k: int, fetch_k: int, graph_max_hops: int) -> QueryRun:
    started = time.perf_counter()
    payload = search_vault_knowledge(
        query=case.query,
        mode=mode,
        k=k,
        fetch_k=fetch_k,
        graph_max_hops=graph_max_hops,
    )
    elapsed = time.perf_counter() - started
    results = list(payload.get("results", []))

    matched_topics: list[dict[str, Any]] = []
    topic_ranks: list[int] = []
    for topic_aliases in case.expected_topics:
        rank, aliases = topic_match_rank(topic_aliases, results)
        matched_topics.append(
            {
                "aliases": aliases,
                "rank": rank,
            }
        )
        if rank is not None:
            topic_ranks.append(rank)

    first_relevant_rank = min(topic_ranks) if topic_ranks else None
    governance_results = sum(1 for row in results if Path(str(row.get("source_path", ""))).name in GOVERNANCE_FILES)
    graph_rows = sum(
        1
        for row in results
        if str(row.get("parser", "")) == "graph" or bool(row.get("graph_evidence"))
    )

    return QueryRun(
        case_name=case.name,
        category=case.category,
        mode=mode,
        elapsed_seconds=round(elapsed, 3),
        hit_at_1=int(first_relevant_rank == 1),
        hit_at_3=int(first_relevant_rank is not None and first_relevant_rank <= 3),
        mrr=round((1.0 / first_relevant_rank) if first_relevant_rank else 0.0, 4),
        topic_recall=round(len(topic_ranks) / len(case.expected_topics), 4),
        relevant_results=relevant_row_count(case, results),
        governance_results=governance_results,
        graph_rows=graph_rows,
        matched_topics=matched_topics,
        result_paths=[str(row.get("source_path", "")) for row in results],
        result_titles=[str(row.get("title", "")) for row in results],
    )


def aggregate(runs: list[QueryRun]) -> dict[str, dict[str, float]]:
    grouped: dict[str, list[QueryRun]] = {}
    for run in runs:
        grouped.setdefault(run.mode, []).append(run)
        grouped.setdefault(f"{run.mode}:{run.category}", []).append(run)

    summary: dict[str, dict[str, float]] = {}
    for key, items in grouped.items():
        summary[key] = {
            "query_count": float(len(items)),
            "avg_hit_at_1": round(mean(run.hit_at_1 for run in items), 4),
            "avg_hit_at_3": round(mean(run.hit_at_3 for run in items), 4),
            "avg_mrr": round(mean(run.mrr for run in items), 4),
            "avg_topic_recall": round(mean(run.topic_recall for run in items), 4),
            "avg_relevant_results": round(mean(run.relevant_results for run in items), 4),
            "avg_governance_results": round(mean(run.governance_results for run in items), 4),
            "avg_graph_rows": round(mean(run.graph_rows for run in items), 4),
            "avg_elapsed_seconds": round(mean(run.elapsed_seconds for run in items), 4),
        }
    return summary


def text_report(runs: list[QueryRun], summary: dict[str, dict[str, float]]) -> str:
    lines: list[str] = []
    lines.append("Aggregate metrics:")
    for key in (
        "hybrid",
        "hybrid-graph",
        "hybrid:direct",
        "hybrid-graph:direct",
        "hybrid:relation",
        "hybrid-graph:relation",
    ):
        metrics = summary.get(key)
        if not metrics:
            continue
        lines.append(
            "- "
            f"{key}: hit@1={metrics['avg_hit_at_1']:.2f}, "
            f"hit@3={metrics['avg_hit_at_3']:.2f}, "
            f"mrr={metrics['avg_mrr']:.2f}, "
            f"topic_recall={metrics['avg_topic_recall']:.2f}, "
            f"relevant@{5}={metrics['avg_relevant_results']:.2f}, "
            f"governance@{5}={metrics['avg_governance_results']:.2f}, "
            f"graph_rows@{5}={metrics['avg_graph_rows']:.2f}, "
            f"latency={metrics['avg_elapsed_seconds']:.2f}s"
        )

    lines.append("")
    lines.append("Per-query comparison:")
    by_case: dict[str, dict[str, QueryRun]] = {}
    for run in runs:
        by_case.setdefault(run.case_name, {})[run.mode] = run

    for case in DEFAULT_CASES:
        hybrid = by_case[case.name]["hybrid"]
        graph = by_case[case.name]["hybrid-graph"]
        lines.append(f"- {case.name} [{case.category}]")
        lines.append(
            "  "
            f"hybrid: mrr={hybrid.mrr:.2f}, topic_recall={hybrid.topic_recall:.2f}, "
            f"relevant={hybrid.relevant_results}, governance={hybrid.governance_results}, "
            f"latency={hybrid.elapsed_seconds:.2f}s"
        )
        lines.append(
            "  "
            f"hybrid-graph: mrr={graph.mrr:.2f}, topic_recall={graph.topic_recall:.2f}, "
            f"relevant={graph.relevant_results}, governance={graph.governance_results}, "
            f"graph_rows={graph.graph_rows}, latency={graph.elapsed_seconds:.2f}s"
        )
        lines.append(
            "  "
            f"hybrid top paths: {', '.join(hybrid.result_paths[:3])}"
        )
        lines.append(
            "  "
            f"hybrid-graph top paths: {', '.join(graph.result_paths[:3])}"
        )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    runs: list[QueryRun] = []
    for case in DEFAULT_CASES:
        runs.append(
            run_case(
                case,
                mode="hybrid",
                k=args.k,
                fetch_k=args.fetch_k,
                graph_max_hops=args.graph_max_hops,
            )
        )
        runs.append(
            run_case(
                case,
                mode="hybrid-graph",
                k=args.k,
                fetch_k=args.fetch_k,
                graph_max_hops=args.graph_max_hops,
            )
        )

    summary = aggregate(runs)
    payload = {
        "cases": [asdict(case) for case in DEFAULT_CASES],
        "runs": [asdict(run) for run in runs],
        "summary": summary,
    }

    if args.json_output:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(text_report(runs, summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
