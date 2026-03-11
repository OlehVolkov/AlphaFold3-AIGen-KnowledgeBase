---
cssclasses: [note]
tags: [audit, quality, confidence, references]
---

# Knowledge Base Audit (AlphaFold3 Vault)

Date: 2026-03-11  
Scope: `UA/`, `EN/`, root navigation pages, bibliography consistency, DOI/reference quality.

## 1. Method

Audit was performed using:
- structural checks (file/folder presence and numbering parity),
- wiki-link integrity checks,
- bibliography/DOI pattern checks,
- UA↔EN mirror consistency review for core scientific notes,
- cross-check against external primary sources (DOI links).

## 2. Structural Integrity Results

- Markdown files:
  - `UA`: 41
  - `EN`: 42
  - `root`: 5
- Numbered note parity (`1.x.x` to `4.x.x`) between `UA/` and `EN/`: **no mismatches**.
- Critical entry/index pages present:
  - `Home.md`
  - `UA/Головна.md`
  - `UA/Індекс.md`
  - `EN/Index.md`
  - `UA/Література та пріоритети.md`
  - `EN/Literature and Priorities.md`

Status: **PASS**

## 3. Link and Citation Integrity

- Wiki-link target check: **0 missing targets** (for vault content links).
- DOI coverage in `UA/` + `EN/` markdown files:
  - files with DOI mentions: `36 / 83` (~43.4%)
- Malformed known DOI typo fixed during audit:
  - `10.48550/arXiv.2109.22paym` → `10.1101/2021.10.04.463034` (AlphaFold-Multimer preprint DOI).

Status: **PASS with minor residual risk**  
Residual risk: not every conceptual file has an explicit DOI block yet.

## 4. Knowledge Consistency Corrections Applied

During this audit cycle, the following were corrected/unified:
- Bibliography expanded in UA/EN prioritized literature pages with additional high-citation core papers.
- DOI blocks added/synchronized in EN mirrors for:
  - `RMSD`,
  - `lDDT`,
  - `DockQ`,
  - `Protein-Protein Interactions`.
- PPI symmetry flowcharts aligned to the standardized Mermaid class scheme.

## 5. Confidence Level Matrix

Scale:
- `High` = strong agreement with primary sources and consistent UA/EN representation.
- `Medium` = generally correct, but incomplete citation depth or narrower coverage.
- `Low` = weakly sourced or potentially outdated/underspecified.

| Domain | Confidence | Rationale | Key External Sources |
|---|---|---|---|
| AF3 core claims (architecture/results) | High | Backed by Nature AF3 + AF2 primary papers; mirrored across UA/EN | `10.1038/s41586-024-07487-w`, `10.1038/s41586-021-03819-2` |
| Diffusion/transformer fundamentals | High | Canonical foundational papers are present and consistently referenced | `10.48550/arXiv.2006.11239`, `10.48550/arXiv.2011.13456`, `10.48550/arXiv.1706.03762` |
| Structural metrics (RMSD, lDDT, DockQ) | High | Core metric references now present in UA and EN | `10.1107/S0567739476001873`, `10.1093/bioinformatics/btt473`, `10.1371/journal.pone.0161879` |
| MSA and evolutionary signal | Medium-High | Core sources present; some practical sections rely on summary-level descriptions | `10.1016/0022-2836(70)90057-4`, `10.1016/S0022-2836(05)80360-2`, `10.1038/nbt.3988` |
| Competing model comparisons (RoseTTAFold/ESMFold/DiffDock) | Medium-High | Good source coverage, but benchmark narratives may evolve with new releases | `10.1126/science.abj8754`, `10.1126/science.ade2574`, `10.48550/arXiv.2210.01776` |
| Operational/practice guidance (pipelines, tooling) | Medium | Technically coherent, but implementation choices are context-dependent and may drift | `10.1038/s41592-022-01488-1`, `10.1038/s41586-021-03828-1` |

## 6. External Sources Used for Confidence Anchoring

Primary scientific sources (DOI links):
- AlphaFold 3: https://doi.org/10.1038/s41586-024-07487-w
- AlphaFold 2: https://doi.org/10.1038/s41586-021-03819-2
- AF2 human proteome: https://doi.org/10.1038/s41586-021-03828-1
- AlphaFold-Multimer: https://doi.org/10.1101/2021.10.04.463034
- DDPM: https://doi.org/10.48550/arXiv.2006.11239
- Score-SDE: https://doi.org/10.48550/arXiv.2011.13456
- Attention Is All You Need: https://doi.org/10.48550/arXiv.1706.03762
- DockQ: https://doi.org/10.1371/journal.pone.0161879
- Kabsch alignment: https://doi.org/10.1107/S0567739476001873
- lDDT: https://doi.org/10.1093/bioinformatics/btt473
- TM-score: https://doi.org/10.1002/prot.20264
- MMseqs2: https://doi.org/10.1038/nbt.3988
- ColabFold: https://doi.org/10.1038/s41592-022-01488-1
- RoseTTAFold: https://doi.org/10.1126/science.abj8754
- ESMFold: https://doi.org/10.1126/science.ade2574

## 7. Recommended Next Actions

1. Raise DOI coverage from ~43% to >60% for conceptual notes by adding 1–2 canonical sources per file.
2. Add a lightweight `references lint` check (regex + whitelist) to catch malformed DOI strings automatically.
3. Introduce per-note `confidence` frontmatter (e.g., `confidence: high|medium|low`) for transparent evidence grading.

