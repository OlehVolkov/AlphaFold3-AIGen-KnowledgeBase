#!/usr/bin/env python3
"""
Reusable audit generator for bilingual Obsidian-style knowledge bases.

Purpose:
- generate a repository-specific `AUDIT.md` report;
- check structural integrity, EN↔UA parity, DOI coverage, wiki-links, and optional `/.brains` runtime health;
- serve as an adaptation template for similar repositories with a different folder layout or note taxonomy.

When adapting this script for another repository, review first:
- `SPECIAL_PAGE_PAIRS`
- `ENTRY_PAGES`
- `SECTION_LABELS`
- `QUERY_PROBES`
- any repository-specific parity or source heuristics below.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SPECIAL_PAGE_PAIRS = (
    ("Home.md", "UA/Головна.md"),
    ("EN/Index.md", "UA/Індекс.md"),
    ("EN/Literature and Priorities.md", "UA/Література та пріоритети.md"),
    ("README.md", "UA/README.md"),
    ("AGENTS.md", "UA/AGENTS.md"),
    ("NOTICE.md", "UA/NOTICE.md"),
)

ENTRY_PAGES = (
    "Home.md",
    "EN/Index.md",
    "UA/Індекс.md",
    "EN/Literature and Priorities.md",
    "UA/Література та пріоритети.md",
    "EN/Summary.md",
    "README.md",
    "UA/README.md",
    "AGENTS.md",
    "UA/AGENTS.md",
    "NOTICE.md",
    "UA/NOTICE.md",
    "AUDIT.md",
    ".brains/BRAIN.md",
)

EXCLUDE_FROM_DOI_CHECK = {
    "Home.md",
    "AGENTS.md",
    "README.md",
    "NOTICE.md",
    "AUDIT.md",
    "Index.md",
    "Literature and Priorities.md",
    "Summary.md",
    "Головна.md",
    "Індекс.md",
    "Література та пріоритети.md",
}

SECTION_LABELS = {
    "1": "1. AlphaFold3",
    "2": "2. Concepts",
    "3": "3. Models",
    "4": "4. Datasets",
}

BRAINS_TIMEOUT_SECONDS = 30

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
DOI_RE = re.compile(r"^>\s*DOI:\s*.+$", re.M)
NUMERIC_PREFIX_RE = re.compile(r"^((\d+)(?:\.\d+)*)\.")
FENCED_BLOCK_RE = re.compile(r"```.*?```", re.S)
MERMAID_BLOCK_RE = re.compile(r"```mermaid\b.*?```", re.S)
TABLE_SEPARATOR_RE = re.compile(r"^\|(?:\s*:?-{3,}:?\s*\|)+\s*$", re.M)
RELATED_EN_RE = re.compile(r"^##\s+Related Notes\s*$", re.M)
RELATED_UA_RE = re.compile(r"^##\s+Пов[’']язані нотатки\s*$", re.M)
SOURCES_EN_RE = re.compile(r"^##\s+Sources\s*$", re.M)
SOURCES_UA_RE = re.compile(r"^##\s+Джерела\s*$", re.M)
MIRROR_UA_RE = re.compile(r"^🇺🇦\s+\[\[UA/", re.M)
MIRROR_EN_RE = re.compile(r"^🇬🇧\s+\[\[EN/", re.M)


@dataclass(frozen=True)
class ProbeSpec:
    query: str
    preferred_paths: tuple[str, ...]
    note: str


QUERY_PROBES = (
    ProbeSpec(
        query="pairformer",
        preferred_paths=(
            "EN/1. AlphaFold3/1.2. Architecture/1.2.2. Pairformer.md",
            "UA/1. AlphaFold3/1.2. Архітектура/1.2.2. Pairformer.md",
        ),
        note="Canonical Pairformer notes should rank first.",
    ),
    ProbeSpec(
        query="foldseek",
        preferred_paths=(
            "EN/1. AlphaFold3/1.5. Resources/1.5.7. Foldseek and Structure Search.md",
            "UA/1. AlphaFold3/1.5. Ресурси/1.5.7. Foldseek і пошук структур.md",
        ),
        note="The dedicated Foldseek note should be the primary hit.",
    ),
    ProbeSpec(
        query="confidence",
        preferred_paths=(
            "EN/1. AlphaFold3/1.3. Results/1.3.2. Confidence Scores.md",
            "UA/1. AlphaFold3/1.3. Результати/1.3.2. Ступінь впевненості.md",
        ),
        note="Generic confidence queries may also surface FAQ or pLDDT context, but the dedicated confidence note is preferred.",
    ),
)


@dataclass
class PageMetrics:
    path: str
    h2_count: int
    has_related: bool
    has_sources_heading: bool
    mermaid_blocks: int
    code_blocks: int
    table_count: int
    math_block_count: int
    has_mirror_line: bool


@dataclass
class PairCheck:
    left: str
    right: str
    left_metrics: PageMetrics
    right_metrics: PageMetrics


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def tracked_md_files(root: Path) -> list[Path]:
    files: list[Path] = []
    excluded_dirs = {
        ".git",
        ".index",
        ".venv",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
    }
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in excluded_dirs]
        base = Path(dirpath)
        for filename in filenames:
            if filename.endswith(".md"):
                files.append(base / filename)
    return sorted(files)


def tracked_repo_files(root: Path) -> list[Path]:
    files: list[Path] = []
    excluded_dirs = {
        ".git",
        ".index",
        ".venv",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
    }
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [name for name in dirnames if name not in excluded_dirs]
        base = Path(dirpath)
        for filename in filenames:
            files.append(base / filename)
    return sorted(files)


def branch_md_files(root: Path, branch: str) -> list[Path]:
    return sorted((root / branch).rglob("*.md"))


def numbered_content_files(root: Path, branch: str) -> list[Path]:
    return sorted(path for path in branch_md_files(root, branch) if NUMERIC_PREFIX_RE.match(path.name))


def audit_link_scan_files(root: Path) -> list[Path]:
    files = numbered_content_files(root, "EN") + numbered_content_files(root, "UA")
    for page in (
        "Home.md",
        "UA/Головна.md",
        "EN/Index.md",
        "UA/Індекс.md",
        "EN/Literature and Priorities.md",
        "UA/Література та пріоритети.md",
        "EN/Summary.md",
    ):
        path = root / page
        if path.exists():
            files.append(path)
    return sorted(set(files))


def strip_fenced_blocks(text: str) -> str:
    return FENCED_BLOCK_RE.sub("", text)


def find_broken_links(files: list[Path], root: Path) -> list[tuple[str, str]]:
    targets = {rel(path, root) for path in tracked_repo_files(root)}
    broken: list[tuple[str, str]] = []
    for path in files:
        text = strip_fenced_blocks(read_text(path))
        for target in LINK_RE.findall(text):
            cleaned = target.strip().replace("\\", "/")
            if not cleaned or cleaned.startswith("http"):
                continue
            if cleaned in targets or f"{cleaned}.md" in targets:
                continue
            broken.append((rel(path, root), cleaned))
    return sorted(set(broken))


def numbered_note_map(root: Path, branch: str) -> dict[str, list[Path]]:
    mapping: dict[str, list[Path]] = defaultdict(list)
    for path in numbered_content_files(root, branch):
        match = NUMERIC_PREFIX_RE.match(path.name)
        if match:
            mapping[match.group(1)].append(path)
    return dict(mapping)


def analyze_page(path: Path, root: Path, branch: str) -> PageMetrics:
    text = read_text(path)
    mermaid_blocks = len(MERMAID_BLOCK_RE.findall(text))
    fenced_blocks = len(FENCED_BLOCK_RE.findall(text))
    code_blocks = max(fenced_blocks - mermaid_blocks, 0)
    has_related = bool(RELATED_EN_RE.search(text) if branch == "EN" else RELATED_UA_RE.search(text))
    has_sources_heading = bool(SOURCES_EN_RE.search(text) if branch == "EN" else SOURCES_UA_RE.search(text))
    has_mirror_line = bool(MIRROR_UA_RE.search(text) if branch == "EN" else MIRROR_EN_RE.search(text))
    return PageMetrics(
        path=rel(path, root),
        h2_count=len(H2_RE.findall(text)),
        has_related=has_related,
        has_sources_heading=has_sources_heading,
        mermaid_blocks=mermaid_blocks,
        code_blocks=code_blocks,
        table_count=len(TABLE_SEPARATOR_RE.findall(text)),
        math_block_count=text.count("$$") // 2,
        has_mirror_line=has_mirror_line,
    )


def build_pair_checks(root: Path) -> tuple[list[PairCheck], list[dict[str, object]]]:
    checks: list[PairCheck] = []
    issues: list[dict[str, object]] = []

    en_map = numbered_note_map(root, "EN")
    ua_map = numbered_note_map(root, "UA")
    all_numeric_ids = sorted(set(en_map) | set(ua_map), key=lambda value: [int(part) for part in value.split(".")])

    for numeric_id in all_numeric_ids:
        en_paths = en_map.get(numeric_id, [])
        ua_paths = ua_map.get(numeric_id, [])
        if len(en_paths) != 1 or len(ua_paths) != 1:
            issues.append(
                {
                    "pair": numeric_id,
                    "issue": "numbered_pair_problem",
                    "en_count": len(en_paths),
                    "ua_count": len(ua_paths),
                }
            )
            continue
        left_metrics = analyze_page(en_paths[0], root, "EN")
        right_metrics = analyze_page(ua_paths[0], root, "UA")
        checks.append(PairCheck(left=left_metrics.path, right=right_metrics.path, left_metrics=left_metrics, right_metrics=right_metrics))

    for left_rel, right_rel in SPECIAL_PAGE_PAIRS:
        left_path = root / left_rel
        right_path = root / right_rel
        if not left_path.exists() or not right_path.exists():
            issues.append(
                {
                    "pair": f"{left_rel} <-> {right_rel}",
                    "issue": "special_pair_missing",
                    "left_exists": left_path.exists(),
                    "right_exists": right_path.exists(),
                }
            )
            continue
        left_branch = "EN" if left_rel.startswith("EN/") or left_rel in {"Home.md", "README.md", "AGENTS.md", "NOTICE.md"} else "UA"
        right_branch = "UA"
        left_metrics = analyze_page(left_path, root, left_branch)
        right_metrics = analyze_page(right_path, root, right_branch)
        checks.append(PairCheck(left=left_metrics.path, right=right_metrics.path, left_metrics=left_metrics, right_metrics=right_metrics))

    for check in checks:
        if check.left_metrics.h2_count != check.right_metrics.h2_count:
            issues.append(
                {
                    "pair": f"{check.left} <-> {check.right}",
                    "issue": "h2_count_mismatch",
                    "left_h2": check.left_metrics.h2_count,
                    "right_h2": check.right_metrics.h2_count,
                }
            )
        if check.left_metrics.has_related != check.right_metrics.has_related:
            issues.append(
                {
                    "pair": f"{check.left} <-> {check.right}",
                    "issue": "related_notes_mismatch",
                }
            )
        if check.left_metrics.has_sources_heading != check.right_metrics.has_sources_heading:
            issues.append(
                {
                    "pair": f"{check.left} <-> {check.right}",
                    "issue": "sources_heading_mismatch",
                }
            )
        if check.left_metrics.mermaid_blocks != check.right_metrics.mermaid_blocks:
            issues.append(
                {
                    "pair": f"{check.left} <-> {check.right}",
                    "issue": "mermaid_count_mismatch",
                    "left_mermaid": check.left_metrics.mermaid_blocks,
                    "right_mermaid": check.right_metrics.mermaid_blocks,
                }
            )
        if check.left_metrics.code_blocks != check.right_metrics.code_blocks:
            issues.append(
                {
                    "pair": f"{check.left} <-> {check.right}",
                    "issue": "code_block_mismatch",
                    "left_code": check.left_metrics.code_blocks,
                    "right_code": check.right_metrics.code_blocks,
                }
            )
        if check.left_metrics.table_count != check.right_metrics.table_count:
            issues.append(
                {
                    "pair": f"{check.left} <-> {check.right}",
                    "issue": "table_count_mismatch",
                    "left_tables": check.left_metrics.table_count,
                    "right_tables": check.right_metrics.table_count,
                }
            )
        if check.left_metrics.math_block_count != check.right_metrics.math_block_count:
            issues.append(
                {
                    "pair": f"{check.left} <-> {check.right}",
                    "issue": "math_block_mismatch",
                    "left_math": check.left_metrics.math_block_count,
                    "right_math": check.right_metrics.math_block_count,
                }
            )
        if NUMERIC_PREFIX_RE.match(Path(check.left).name) and check.left.startswith("EN/") and not check.left_metrics.has_mirror_line:
            issues.append({"pair": check.left, "issue": "missing_ua_mirror_line"})
        if NUMERIC_PREFIX_RE.match(Path(check.right).name) and check.right.startswith("UA/") and not check.right_metrics.has_mirror_line:
            issues.append({"pair": check.right, "issue": "missing_en_mirror_line"})

    return checks, issues


def notes_without_doi(root: Path, files: list[Path]) -> list[str]:
    result: list[str] = []
    for path in files:
        if path.name in EXCLUDE_FROM_DOI_CHECK:
            continue
        if not DOI_RE.search(read_text(path)):
            result.append(rel(path, root))
    return sorted(result)


def count_doi_lines(root: Path) -> int:
    total = 0
    for branch in ("EN", "UA"):
        for path in branch_md_files(root, branch):
            total += len(DOI_RE.findall(read_text(path)))
    return total


def root_markdown_count(root: Path) -> int:
    return len(list(root.glob("*.md")))


def run_brains_cmd(root: Path, args: list[str]) -> tuple[bool, str, bool]:
    brains_args = subprocess.list2cmdline(["uv", "run", "python", "-m", "brains", *args])
    cmd = f'cd /d %CD%\\.brains && set "UV_PROJECT_ENVIRONMENT=.venv" && {brains_args}'
    try:
        completed = subprocess.run(
            ["cmd.exe", "/c", cmd],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=BRAINS_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        partial = ((exc.stdout or "") + (exc.stderr or "")).strip()
        return False, f"Timed out after {BRAINS_TIMEOUT_SECONDS}s\n{partial}".strip(), True
    output = ((completed.stdout or "") + (completed.stderr or "")).strip()
    return completed.returncode == 0, output, False


def extract_json_tail(text: str) -> dict[str, object] | None:
    end = text.rfind("}")
    start = text.find("{")
    if start == -1 or end == -1 or end < start:
        return None
    try:
        return json.loads(text[start : end + 1])
    except json.JSONDecodeError:
        return None


def check_indexes(root: Path) -> dict[str, dict[str, object]]:
    results: dict[str, dict[str, object]] = {}
    for target in ("vault", "pdf"):
        ok, output, timed_out = run_brains_cmd(root, ["check-index", "--target", target])
        results[target] = {
            "ok": ok,
            "timed_out": timed_out,
            "raw_output": output,
            "parsed": extract_json_tail(output),
        }
    return results


def query_probes(root: Path) -> dict[str, dict[str, object]]:
    results: dict[str, dict[str, object]] = {}
    for probe in QUERY_PROBES:
        ok, output, timed_out = run_brains_cmd(root, ["search-vault", probe.query, "--k", "3", "--json-output"])
        results[probe.query] = {
            "ok": ok,
            "timed_out": timed_out,
            "raw_output": output,
            "parsed": extract_json_tail(output),
        }
    return results


def top_hit_path(payload: dict[str, object]) -> str | None:
    parsed = payload.get("parsed")
    if not isinstance(parsed, dict):
        return None
    results = parsed.get("results")
    if not isinstance(results, list) or not results:
        return None
    top = results[0]
    if not isinstance(top, dict):
        return None
    value = top.get("source_path")
    return value if isinstance(value, str) else None


def top_hit_section(payload: dict[str, object]) -> str | None:
    parsed = payload.get("parsed")
    if not isinstance(parsed, dict):
        return None
    results = parsed.get("results")
    if not isinstance(results, list) or not results:
        return None
    top = results[0]
    if not isinstance(top, dict):
        return None
    value = top.get("section_path") or top.get("section")
    return value if isinstance(value, str) else None


def preferred_probe_hit(probe: ProbeSpec, payload: dict[str, object]) -> bool:
    top_path = top_hit_path(payload)
    if not top_path:
        return False
    return any(top_path == candidate for candidate in probe.preferred_paths)


def top_level_key(path_str: str) -> str:
    filename_match = NUMERIC_PREFIX_RE.match(Path(path_str).name)
    if filename_match:
        return filename_match.group(2)
    path = Path(path_str)
    for part in path.parts:
        match = NUMERIC_PREFIX_RE.match(part)
        if match:
            return match.group(2)
    return "?"


def confidence_label(score: int) -> str:
    return {
        0: "Low",
        1: "Medium",
        2: "Medium-High",
        3: "High",
    }[max(0, min(score, 3))]


def confidence_rows(
    root: Path,
    pair_checks: list[PairCheck],
    pair_issues: list[dict[str, object]],
    doi_missing: list[str],
    broken_links: list[tuple[str, str]],
    index_results: dict[str, dict[str, object]],
    probes: dict[str, dict[str, object]],
    include_runtime: bool,
) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []

    for key, label in SECTION_LABELS.items():
        pair_count = sum(1 for check in pair_checks if check.left.startswith(f"EN/{key}.") or check.left.startswith(f"EN/{key} "))
        missing_count = sum(1 for path in doi_missing if path.startswith(f"EN/{key}.") or path.startswith(f"UA/{key}."))
        section_issue_count = sum(
            1
            for issue in pair_issues
            if isinstance(issue.get("pair"), str)
            and (issue["pair"].startswith(key + ".") or f"/{key}." in issue["pair"])
        )
        coverage_ratio = 1.0
        total_branch_notes = max(pair_count * 2, 1)
        coverage_ratio -= missing_count / total_branch_notes

        score = 0
        if coverage_ratio >= 0.85:
            score += 2
        elif coverage_ratio >= 0.65:
            score += 1
        if section_issue_count == 0:
            score += 1
        score = min(score, 3)

        rows.append(
            (
                label,
                confidence_label(score),
                f"{pair_count} mirrored pairs, {missing_count} branch-level notes without DOI, {section_issue_count} parity issue(s).",
            )
        )

    missing_entry_pages = [page for page in ENTRY_PAGES if not (root / page).exists()]
    governance_score = 3
    if broken_links:
        governance_score -= 1
    if missing_entry_pages:
        governance_score -= 1
    rows.append(
        (
            "Governance and navigation",
            confidence_label(governance_score),
            f"{len(ENTRY_PAGES) - len(missing_entry_pages)}/{len(ENTRY_PAGES)} key pages present, {len(broken_links)} broken wiki-links in the audit scan.",
        )
    )

    if include_runtime:
        probe_exact_hits = sum(1 for probe in QUERY_PROBES if preferred_probe_hit(probe, probes.get(probe.query, {})))
        indexes_ok = sum(
            1
            for payload in index_results.values()
            if isinstance(payload.get("parsed"), dict) and payload["parsed"].get("status") == "ok"
        )
        retrieval_score = 0
        if indexes_ok == 2:
            retrieval_score += 2
        elif indexes_ok == 1:
            retrieval_score += 1
        if probe_exact_hits >= 2:
            retrieval_score += 1
        rows.append(
            (
                "`/.brains` retrieval layer",
                confidence_label(retrieval_score),
                f"{indexes_ok}/2 indexes healthy, {probe_exact_hits}/{len(QUERY_PROBES)} preferred probe hits ranked first.",
            )
        )
    else:
        rows.append(
            (
                "`/.brains` retrieval layer",
                "Not checked",
                "Runtime probes were skipped via `--skip-runtime`.",
            )
        )
    return rows


def status_line(ok: bool, risk: str | None = None) -> str:
    if not ok and risk:
        return f"**FAIL** ({risk})"
    if not ok:
        return "**FAIL**"
    if risk:
        return f"**PASS with {risk} residual risk**"
    return "**PASS**"


def build_audit_markdown(root: Path, include_runtime: bool = True) -> str:
    en_files = branch_md_files(root, "EN")
    ua_files = branch_md_files(root, "UA")
    numbered_en = numbered_content_files(root, "EN")
    numbered_ua = numbered_content_files(root, "UA")
    pair_checks, pair_issues = build_pair_checks(root)
    broken_links = find_broken_links(audit_link_scan_files(root), root)
    doi_missing = notes_without_doi(root, numbered_en + numbered_ua)
    doi_count = count_doi_lines(root)
    missing_entry_pages = [page for page in ENTRY_PAGES if not (root / page).exists()]

    if include_runtime:
        index_results = check_indexes(root)
        probes = query_probes(root)
    else:
        index_results = {
            target: {"ok": False, "timed_out": False, "raw_output": "skipped", "parsed": None}
            for target in ("vault", "pdf")
        }
        probes = {
            probe.query: {"ok": False, "timed_out": False, "raw_output": "skipped", "parsed": None}
            for probe in QUERY_PROBES
        }

    mirror_missing_en = sum(1 for check in pair_checks if check.left.startswith("EN/") and not check.left_metrics.has_mirror_line)
    mirror_missing_ua = sum(1 for check in pair_checks if check.right.startswith("UA/") and not check.right_metrics.has_mirror_line)
    h2_mismatches = [issue for issue in pair_issues if issue["issue"] == "h2_count_mismatch"]
    asset_mismatches = [
        issue
        for issue in pair_issues
        if issue["issue"] in {"mermaid_count_mismatch", "code_block_mismatch", "table_count_mismatch", "math_block_mismatch"}
    ]

    notes_with_doi = len(numbered_en) + len(numbered_ua) - len(doi_missing)
    total_numbered = len(numbered_en) + len(numbered_ua)
    doi_ratio = (notes_with_doi / total_numbered * 100) if total_numbered else 0.0

    rows = confidence_rows(root, pair_checks, pair_issues, doi_missing, broken_links, index_results, probes, include_runtime)

    lines: list[str] = []
    lines.append("---")
    lines.append("cssclasses: [note]")
    lines.append("tags: [audit, quality, confidence, references]")
    lines.append("---")
    lines.append("")
    lines.append("# Knowledge Base Audit (AlphaFold3 Vault)")
    lines.append("")
    lines.append(f"Date: {date.today().isoformat()}")
    lines.append(
        "Scope: `UA/`, `EN/`, root governance/navigation pages, `/.brains/BRAIN.md`, wiki-link integrity, DOI/source coverage, mirror-consistency checks, and optional `/.brains` runtime health."
    )
    lines.append("")
    lines.append("## 1. Method")
    lines.append("")
    lines.append("Audit was generated by the local automation script in `/.scripts/generate_audit.py`.")
    lines.append("- structure checks use the live repository tree;")
    lines.append("- EN↔UA parity is checked by numbered note IDs plus mirrored governance/navigation pairs;")
    lines.append("- parity heuristics compare `##` sections, mirror breadcrumb lines, `Related Notes`, `Sources`, Mermaid blocks, fenced code blocks, tables, and display-math blocks;")
    lines.append("- DOI coverage is measured from `> DOI:` blocks in numbered content notes only;")
    if include_runtime:
        lines.append("- runtime checks call `brains check-index` for `vault` and `pdf`, then run `search-vault` probes over project-specific terms.")
    else:
        lines.append("- runtime `/.brains` checks were skipped via `--skip-runtime`.")
    lines.append("")
    lines.append("## 2. Structural Integrity Results")
    lines.append("")
    lines.append(f"- Markdown files: `EN={len(en_files)}`, `UA={len(ua_files)}`, `root={root_markdown_count(root)}`.")
    lines.append(f"- Numbered content notes: `EN={len(numbered_en)}`, `UA={len(numbered_ua)}`.")
    lines.append(f"- Mirrored pairs checked automatically: `{len(pair_checks)}`.")
    lines.append(f"- Pair issues detected: `{len(pair_issues)}`.")
    lines.append("- Critical pages present:")
    for page in ENTRY_PAGES:
        marker = "ok" if (root / page).exists() else "missing"
        lines.append(f"  - `{page}`: `{marker}`")
    lines.append("")
    lines.append(f"Status: {status_line(ok=not missing_entry_pages and not any(issue['issue'] == 'numbered_pair_problem' for issue in pair_issues), risk='low' if pair_issues else None)}")
    lines.append("")
    lines.append("## 3. Link and Mirror Integrity")
    lines.append("")
    lines.append(f"- Broken wiki-links in the audit scan: `{len(broken_links)}`.")
    lines.append(f"- EN notes missing the `🇺🇦` mirror line: `{mirror_missing_en}`.")
    lines.append(f"- UA notes missing the `🇬🇧` mirror line: `{mirror_missing_ua}`.")
    lines.append(f"- Pairs with top-level `##` count mismatch: `{len(h2_mismatches)}`.")
    lines.append(f"- Pairs with Mermaid / code / table / math parity mismatches: `{len(asset_mismatches)}`.")
    if broken_links:
        lines.append("- Sample broken links:")
        for path, target in broken_links[:10]:
            lines.append(f"  - `{path}` -> `{target}`")
    if h2_mismatches:
        lines.append("- Sample `##` parity mismatches:")
        for issue in h2_mismatches[:10]:
            lines.append(f"  - `{issue['pair']}`: `{issue['left_h2']}` vs `{issue['right_h2']}`")
    if asset_mismatches:
        lines.append("- Sample asset parity mismatches:")
        for issue in asset_mismatches[:10]:
            lines.append(f"  - `{issue['pair']}`: `{issue['issue']}`")
    lines.append("")
    lines.append(f"Status: {status_line(ok=not broken_links and mirror_missing_en == 0 and mirror_missing_ua == 0 and not h2_mismatches, risk='low' if asset_mismatches else 'medium' if broken_links or h2_mismatches else None)}")
    lines.append("")
    lines.append("## 4. DOI and Source Coverage")
    lines.append("")
    lines.append(f"- Numbered content notes audited: `{total_numbered}`.")
    lines.append(f"- Notes with at least one DOI block: `{notes_with_doi} / {total_numbered}` (`{doi_ratio:.1f}%`).")
    lines.append(f"- Numbered notes still lacking DOI-backed sources: `{len(doi_missing)}`.")
    if doi_missing:
        grouped: dict[str, list[str]] = defaultdict(list)
        for path in doi_missing:
            grouped[top_level_key(path)].append(path)
        lines.append("- Missing DOI coverage by top-level section:")
        for key in sorted(grouped, key=lambda value: int(value) if value.isdigit() else 99):
            label = SECTION_LABELS.get(key, key)
            lines.append(f"  - `{label}`: `{len(grouped[key])}`")
        lines.append("- Sample missing DOI notes:")
        for path in doi_missing[:12]:
            lines.append(f"  - `{path}`")
    lines.append("")
    lines.append(f"Status: {status_line(ok=len(doi_missing) == 0, risk='medium' if doi_missing else None)}")
    lines.append("")
    lines.append("## 5. `/.brains` Index Health")
    lines.append("")
    for target in ("vault", "pdf"):
        payload = index_results[target]
        parsed = payload.get("parsed")
        lines.append(f"### {target.capitalize()} Index")
        lines.append("")
        if isinstance(parsed, dict):
            lines.append(f"- `status`: `{parsed.get('status', 'unknown')}`")
            lines.append(f"- `row_count`: `{parsed.get('row_count', 'unknown')}`")
            lines.append(f"- `index_root`: `{parsed.get('index_root', 'unknown')}`")
            lines.append(f"- `pointer_used`: `{parsed.get('pointer_used', 'unknown')}`")
        elif payload.get("timed_out"):
            lines.append(f"- timed out after `{BRAINS_TIMEOUT_SECONDS}` seconds")
        elif include_runtime:
            lines.append("- command did not produce parseable JSON")
        else:
            lines.append("- skipped by `--skip-runtime`")
        lines.append("")
    lines.append("## 6. Retrieval Quality Probes")
    lines.append("")
    for probe in QUERY_PROBES:
        payload = probes[probe.query]
        lines.append(f"### Query: `{probe.query}`")
        lines.append("")
        if isinstance(payload.get("parsed"), dict):
            lines.append(f"- top result: `{top_hit_path(payload) or 'unknown'}`")
            lines.append(f"- top section: `{top_hit_section(payload) or 'unknown'}`")
            lines.append(f"- preferred top hit: `{'yes' if preferred_probe_hit(probe, payload) else 'no'}`")
        elif payload.get("timed_out"):
            lines.append(f"- timed out after `{BRAINS_TIMEOUT_SECONDS}` seconds")
        elif include_runtime:
            lines.append("- command did not produce parseable JSON")
        else:
            lines.append("- skipped by `--skip-runtime`")
        lines.append(f"- assessment: {probe.note}")
        lines.append("")
    lines.append("## 7. Corrections Applied During This Audit Cycle")
    lines.append("")
    lines.append("- This automation script reflects the current AlphaFold3 vault structure, not the previous project-specific quantum-computing template.")
    lines.append("- The generated audit now treats `/.brains/BRAIN.md` as canonical runtime instructions instead of the deleted root `BRAIN.md`.")
    lines.append("- No direct note edits are implied by this generated report; updating `AUDIT.md` remains an explicit user action.")
    lines.append("")
    lines.append("## 8. Confidence Level Matrix")
    lines.append("")
    lines.append("| Domain | Confidence | Rationale |")
    lines.append("|---|---|---|")
    for domain, confidence, rationale in rows:
        lines.append(f"| {domain} | {confidence} | {rationale} |")
    lines.append("")
    lines.append("## 9. Recommended Next Actions")
    lines.append("")
    if broken_links:
        lines.append(f"1. Fix the `{len(broken_links)}` broken wiki-links detected by the current scan.")
    else:
        lines.append("1. Keep the static wiki-link scan in regular maintenance so future broken links do not accumulate silently.")
    if pair_issues:
        lines.append(f"2. Resolve the `{len(pair_issues)}` EN↔UA parity issues, starting with numbered note mismatches and `##` section mismatches.")
    else:
        lines.append("2. Preserve EN↔UA parity by rerunning this audit after any large bilingual update or note move.")
    if doi_missing:
        lines.append(f"3. Raise DOI coverage in the `{len(doi_missing)}` numbered notes that still lack `> DOI:` blocks, starting with the largest affected section.")
    else:
        lines.append("3. Preserve DOI hygiene in new numbered notes and keep the current coverage from regressing.")
    if include_runtime:
        probe_misses = sum(1 for probe in QUERY_PROBES if not preferred_probe_hit(probe, probes.get(probe.query, {})))
        lines.append(f"4. Review retrieval ranking for the `{probe_misses}` probe(s) where the preferred note is not ranked first.")
    else:
        lines.append("4. Re-run this script without `--skip-runtime` when you want live `/.brains` health and retrieval checks.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an AlphaFold3-specific AUDIT.md report.")
    parser.add_argument(
        "--skip-runtime",
        action="store_true",
        help="Skip `/.brains` index health and retrieval probes.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional output path. Defaults to <REPO_ROOT>/AUDIT.md.",
    )
    args = parser.parse_args()

    root = repo_root()
    output_path = args.output or (root / "AUDIT.md")
    audit = build_audit_markdown(root, include_runtime=not args.skip_runtime)
    output_path.write_text(audit + "\n", encoding="utf-8")
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
