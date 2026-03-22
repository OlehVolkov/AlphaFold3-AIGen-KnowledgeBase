---
cssclasses: [note]
tags: [audit, quality, confidence, references]
---

# Knowledge Base Audit (AlphaFold3 Vault)

Date: 2026-03-19
Scope: `UA/`, `EN/`, root governance/navigation pages, `AGENTS.md`, `UA/AGENTS.md`, `BRAIN.md`, `AUDIT.md`, wiki-link integrity, DOI/source coverage, and mirror-consistency spot-checks.

## 1. Method

Audit was performed using local repository checks:

- markdown file inventory and root-file presence,
- numbered-note parity check across `UA/` and the `EN/` note tree,
- filtered absolute wiki-link target validation,
- DOI/source-block presence scan,
- lightweight formatting scan for trailing whitespace and repeated blank blocks,
- targeted UA↔EN section-parity spot-checks for recently added and recently updated mirrored notes.

Notes:

- This audit cycle was local-only; no external web verification was performed.
- Wiki-link validation was filtered to exclude pseudo-link examples inside governance documentation such as `[[path]]`, `[[Note]]`, and `[[...]]`.
- Confidence levels below are based on source presence, mirror consistency, navigation integrity, and prior curation state inside the vault.

## 2. Structural Integrity Results

- Markdown files:
  - `UA`: 53
  - `EN`: 50
  - `root`: 6
  - `total`: 109
- Numbered note parity (`1.x.x` to `4.x.x`) between `UA/` and the `EN/` note tree:
  - `EN`: 47
  - `UA`: 47
  - mismatches: **0**
- Critical entry and governance pages present:
  - `Home.md`
  - `UA/Головна.md`
  - `EN/Index.md`
  - `UA/Індекс.md`
  - `EN/Literature and Priorities.md`
  - `UA/Література та пріоритети.md`
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

- Filtered absolute wiki-link target check over notes and navigation pages: **0 missing targets**.
- Lightweight formatting scan over `EN/`, `UA/`, and `Home.md`: **0 trailing-whitespace / repeated-blank-block issues**.
- Mirror breadcrumb check for numbered notes:
  - EN notes missing the `🇺🇦` mirror line: `0`
  - UA notes missing the `🇬🇧` mirror line: `0`
- Spot-checked mirrored section counts for recently expanded content:
  - `OpenFold`: `7 / 7` top-level `##` sections in UA/EN
  - `Boltz-1`: `7 / 7`
  - `Chai-1`: `7 / 7`
  - `RoseTTAFoldNA`: `7 / 7`
  - `Foldseek and Structure Search`: `5 / 5`
  - `Models Overview`: `7 / 7`
  - `Literature and Priorities`: `9 / 9`
  - `Home`: `8 / 8`
- Residual navigation discrepancy:
  - `UA/Індекс.md` currently has one extra top-level section, `## 🔗 Концепти → AF3`, that is not mirrored in `EN/Index.md`.

Status: **PASS with low residual risk**

## 4. DOI and Source Coverage

- Numbered content notes audited: `94`
- Content notes with at least one DOI block or DOI link: `57 / 94` (`60.6%`)
- Numbered content notes still lacking DOI-backed sources: `37`

Highest-priority content gaps:

- Dataset cluster:
  - `4.0. Datasets Overview`
  - `PDB`
  - `UniProt`
  - `AlphaFoldDB`
  - `CASP`
- AF3 overview / architecture / results notes:
  - `Context and Motivation`
  - `Pairformer`
  - `Diffusion Module`
  - `Model Training`
  - `Accuracy Across Complex Types`
  - `Confidence Scores`
  - `Model Limitations`
- AF3 resource notes:
  - `Key Terms`
  - `Comparison with Predecessors`
  - `Working with FASTA Files`
  - `Working with mmCIF Files`
  - `Illustration Gallery`
- Concepts still under-sourced in at least one mirror:
  - `Protein Folding`
  - `Diffusion Models`
  - `Geometric Deep Learning`

Status: **PASS with medium residual risk**

## 5. Corrections Applied During This Audit Cycle

- Refreshed `AUDIT.md` to match the current repository state after the latest note expansion, navigation updates, and `/.brains` structure changes.
- No direct content-note edits were applied as part of this audit refresh.

## 6. Confidence Level Matrix

Scale:

- `High` = strong source presence, good mirror parity, and stable navigation/integrity.
- `Medium-High` = technically consistent and useful, but with partial source gaps in the topic cluster.
- `Medium` = structurally coherent, but still under-sourced or overview-heavy.

| Domain | Confidence | Rationale |
|---|---|---|
| AF3 architecture and Featurization | Medium-High | Core architectural notes are mirrored and structurally coherent, but several architecture subnotes (`Pairformer`, `Diffusion Module`, `Model Training`) still lack DOI-backed source blocks. |
| MSA / A3M / input-resource practice | Medium-High | Practical notes are rich and mirrored well, but some adjacent operational resource notes such as `Working with FASTA Files` and `Working with mmCIF Files` remain under-cited. |
| Diffusion and ML foundations | Medium-High | Coverage is broad and technically useful, but `Diffusion Models` and `Geometric Deep Learning` still need stronger DOI coverage in both branches. |
| Model ecosystem (`AF2`, `AF3`, `RoseTTAFold`, `ESMFold`, `DiffDock`, `OpenFold`, `Boltz-1`, `Chai-1`, `RoseTTAFoldNA`) | High | The model cluster is mirrored, recently expanded, and section-parity spot-checks are clean across the new notes. |
| Dataset cluster and operational references | Medium | The dataset tree is structurally complete and navigable, but DOI/source coverage is still the weakest part of the numbered note set. |
| Governance, navigation, and repository rules | High | Root governance files are present, link integrity passes after filtering documentation examples, and most key navigation pages are aligned, with one remaining `EN/Index` vs `UA/Індекс` section mismatch. |

## 7. Recommended Next Actions

1. Raise DOI coverage in the 37 remaining numbered content notes without DOI-backed sources, starting with the dataset cluster and the AF3 architecture/result notes.
2. Synchronize `EN/Index.md` with `UA/Індекс.md` by either adding the missing `Concepts → AF3` block to EN or removing the mismatch intentionally in both branches.
3. Add a lightweight local lint step for:
   - missing DOI blocks in numbered notes,
   - missing mirror breadcrumb lines,
   - `EN/Index` ↔ `UA/Індекс` section-parity checks,
   - filtered broken wiki-link checks over `EN/`, `UA/`, and `Home.md`.
4. Re-run `AUDIT.md` after the next DOI-enrichment pass, navigation synchronization, or mass EN↔UA content update.
