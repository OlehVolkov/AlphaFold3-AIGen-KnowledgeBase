---
cssclasses: [note]
tags: [audit, quality, confidence, references]
---

# Knowledge Base Audit (AlphaFold3 Vault)

Date: 2026-03-18
Scope: `UA/`, `EN/`, root governance/navigation pages, `AGENTS.md`, `UA/AGENTS.md`, `BRAIN.md`, `AUDIT.md`, wiki-link integrity, DOI/source coverage, and mirror consistency spot-checks.

## 1. Method

Audit was performed using local vault checks:
- markdown file inventory and root-file presence,
- numbered note parity check across `UA/` and the `EN/` note tree,
- absolute wiki-link target validation,
- DOI-block presence scan (`DOI: [...]`),
- lightweight formatting scan for trailing whitespace / repeated blank blocks in repository markdown,
- targeted UA↔EN section-parity spot-checks for recently changed mirrored notes.

Notes:
- This audit cycle was local-only; no external web verification was performed.
- Confidence levels below are based on source presence, mirror consistency, and prior curation state inside the vault.

## 2. Structural Integrity Results

- Markdown files:
  - `UA`: 48
  - `EN`: 45
  - `root`: 6
  - `total`: 104
- Numbered note parity (`1.x.x` to `4.x.x`) between `UA/` and the `EN/` note tree: **no mismatches**.
- Critical entry and governance pages present:
  - `Home.md`
  - `UA/Головна.md`
  - `UA/Індекс.md`
  - `EN/Index.md`
  - `UA/Література та пріоритети.md`
  - `EN/Literature and Priorities.md`
  - `README.md`
  - `UA/README.md`
  - `AGENTS.md`
  - `UA/AGENTS.md`
  - `BRAIN.md`
  - `AUDIT.md`
  - `NOTICE.md`
  - `UA/NOTICE.md`

Status: **PASS**

## 3. Link and Mirror Integrity

- Absolute wiki-link target check: **0 missing targets**.
- Filtered repository-format scan (excluding plugin vendor docs): **0 trailing-whitespace / repeated-blank-block issues**.
- Spot-checked mirrored section counts for recently edited note pairs:
  - `Featurization`: `13 / 13` top-level `##` sections in UA/EN
  - `A3M`: `10 / 10`
  - `MSA`: `7 / 7`
- `Related Notes` section naming normalized in EN mirrors where lowercase `notes` was still present.

Status: **PASS**

## 4. DOI and Source Coverage

- Markdown files with at least one DOI block: `53 / 104` (`51.0%`).
- Residual files without DOI blocks include many non-scientific pages (navigation, notice, audit, gallery), but **38 content notes** still lack DOI-backed source blocks.

Highest-priority content gaps:
- AF3 overview / resource notes without DOI blocks:
  - `Context and Motivation`
  - `Key Terms`
  - `Comparison with Predecessors`
- AF3 architecture notes without DOI blocks:
  - `Pairformer`
  - `Diffusion Module`
  - `Model Training`
- AF3 results and limitations notes:
  - `Accuracy Across Complex Types`
  - `Confidence Scores`
  - `Model Limitations`
- Resource notes:
  - `Working with FASTA Files`
  - `Working with mmCIF Files`
- Dataset overview page:
  - `Datasets Overview`
- Dataset pages:
  - `PDB`
  - `UniProt`
  - `AlphaFoldDB`
  - `CASP`
- Concept pages still lacking DOI in at least one mirror:
  - `Protein Folding`
  - `Diffusion Models`
  - `Geometric Deep Learning`

Status: **PASS with medium residual risk**

## 5. Corrections Applied During This Audit Cycle

- Refreshed `AGENTS.md`, `UA/AGENTS.md`, and `BRAIN.md` to reflect the current repository state:
  - `EN/` remains the canonical English note branch,
  - `UA/README.md` is now documented inside the `UA/` structure,
  - `README.md` / `UA/README.md` are treated as aligned repository-usage guides.
- Normalized remaining governance-history references in `NOTICE.md` / `UA/NOTICE.md` where duplicated `AGENTS.md` / `NOTICE.md` names were ambiguous.
- Re-ran the local audit after the latest structure and formatting updates.

## 6. Confidence Level Matrix

Scale:
- `High` = strong source presence and stable UA↔EN representation.
- `Medium-High` = technically consistent, but source coverage is incomplete in part of the topic cluster.
- `Medium` = useful and coherent, but still under-sourced or overview-heavy.

| Domain | Confidence | Rationale |
|---|---|---|
| AF3 core architecture and Featurization | High | Core architecture/feature-building material is mirrored, structurally aligned, and anchored by primary AF3 sources in the central notes. |
| MSA / A3M / sequence-alignment practice | Medium-High | Practical guidance is now richer and mirrored well, but some adjacent resource notes still lack DOI blocks. |
| Diffusion and ML foundations | Medium-High | Topic coverage is broad and coherent, though `Diffusion Models` and `Geometric Deep Learning` still need stronger DOI coverage in the audited set. |
| Model comparisons (AF2, AF3, RoseTTAFold, ESMFold, DiffDock) | High | Core model pages and overview pages are mirrored and generally source-backed. |
| Dataset overviews and operational reference pages | Medium | Structurally complete, but the dataset cluster is still under-cited relative to the rest of the vault. |

## 7. Recommended Next Actions

1. Raise DOI coverage first in the 38 remaining content notes without source blocks, starting with `Pairformer`, `Diffusion Module`, `Model Training`, `PDB`, `UniProt`, `AlphaFoldDB`, and `CASP`.
2. Add a lightweight local lint step for:
   - missing DOI blocks in numbered notes,
   - `## Related Notes` capitalization consistency,
   - missing mirrored `## Related Notes / ## Пов'язані нотатки` sections.
3. Re-run `AUDIT.md` after the next major EN↔UA synchronization, DOI-enrichment pass, or mass terminology rename.
