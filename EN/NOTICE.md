# NOTICE — Formatting Fix Log

Last updated: 2026-03-18
Platform: Obsidian vault
Obsidian compatibility (minimum): 1.12.0
Note: `app.json` in this vault is empty (`{}`), so the exact app version is not pinned in-repo.

This file records formatting issues that were already fixed, to avoid regressions.

## 1. Wiki-links inside markdown tables

- Problem: links like `[[path|label]]` broke table parsing because `|` is a table delimiter.
- Resolution: inside tables, use only `[[path]]` (no alias).
- Applied to:
  - `UA/Індекс.md`
  - `EN/Index.md`
  - `UA/3. Моделі/3.0. Огляд моделей.md`
  - `EN/3. Models/3.0. Models Overview.md`
  - `UA/4. Датасети/4.0. Огляд датасетів.md`
  - `EN/4. Datasets/4.0. Datasets Overview.md`

## 2. Mermaid formatting

- Problem: `\n` in node labels was not rendered reliably.
- Resolution: replaced with `<br/>` inside Mermaid blocks.
- Problem: `quadrantChart` may fail on lines like `quadrant-1 ...`, `quadrant-2 ...`.
- Resolution: remove `quadrant-1..4` labels and keep only axes + data points.

## 3. Absolute wiki-links

- Rule: use absolute paths from vault root.
- Applied in bulk after file/folder restructuring.

## 4. Home pages and navigation

- English home is at vault root:
  - `Home.md`
- Ukrainian home moved to:
  - `UA/Головна.md`
- Cross-language navigation updated:
  - `Home.md` ↔ `UA/Головна.md`

## 5. Index and literature notes at language-root level

- UA:
  - `UA/Індекс.md`
  - `UA/Література та пріоритети.md`
- EN:
  - `EN/Index.md`
  - `EN/Literature and Priorities.md`

## 6. Post-change validation checklist

After mass rename/move/refactor:

1. Verify every `[[...]]` target `.md` exists.
2. Re-check index pages (`Concepts`, `Models`, `Datasets`) first.
3. Reload Obsidian if render cache artifacts appear.
4. For `.excalidraw`, verify plugin settings:
   - `renderImageInMarkdownReadingMode: true`
   - recommended: `mdSVGwidth: 1200`, `mdSVGmaxHeight: 1600`

## 7. Anti-patterns (do not use)

- Do not use `[[path|label]]` inside markdown tables.
- Do not use relative links.
- Do not put HTML inside `[[...]]`.
- Do not apply aggressive Excalidraw CSS scaling without validating Reading view (it may break rendering).

## 8. Diagram and image scaling fix (2026-03-11)

Three simultaneous root causes were found for the scale mismatch between Mermaid and images:

**Cause 1 — dead `.note` scope.**
All notes have `cssclasses: [note]`, but `diagram-scale.css` had no `.note`-scoped rules. The snippet only applied via global `.markdown-preview-view` selectors, which GitHub Theme overrode with higher-specificity rules.
- Fix: added `.note .markdown-preview-view` scope to all key rules.

**Cause 2 — GitHub Theme constrains `img`.**
The theme applies its own `max-width` to `.markdown-preview-section img`, which differed from the Mermaid container width.
- Fix: added explicit `img` selector + `.markdown-preview-section img` with `!important`.

**Cause 3 — `img:not([class])` missed images with classes.**
GitHub Theme adds its own classes to `<img>` tags — those images were entirely outside the snippet's scope.
- Fix: changed `img:not([class])` → `img` (no class filter).

**New exception:** `img[width]` — images with an explicit width attribute (icons, badges) are not stretched.
**New variable:** `--content-max-width: 100%` for centralised control.

- Snippet: `.obsidian/snippets/diagram-scale.css`.
- Goal: Mermaid SVG and `<img>` render at the same width — 100% of the text container.
- If illustrations disappear after CSS changes: check Excalidraw plugin settings first, then CSS.

## 9. File maintenance

- Keep this file updated after every major formatting or structure refactor.
- Ukrainian counterpart: `NOTICE.md`.

## 10. Obsidian Mermaid render fix (2026-03-11)

Some diagrams rendered worse in Obsidian than in VS Code/GitHub due to overly aggressive local CSS and narrow readable-width mode.

- `.obsidian/app.json`:
  - `readableLineLength: true` → `false` (so wide Mermaid diagrams are not squeezed by the readable-width container).
- `.obsidian/snippets/diagram-scale.css`:
  - removed forced `font-size: ... !important` on `.mermaid svg` (it could break label auto-layout for some Mermaid types),
  - changed Mermaid container `overflow-x: hidden` → `overflow-x: auto` (to avoid clipping),
  - removed `max-height` constraints for Excalidraw/internal embeds (`svg/img/canvas`) to avoid vertical compression.

## 11. Mass EN↔UA synchronization (2026-03-11)

Performed content parity sync where EN notes were shorter than UA mirrors (sections, tables, formulas, and practical examples).

- Updated EN Concepts core notes (`2.1`, `2.2`, `2.3`):
  - `2.1.1 Protein Folding`
  - `2.1.2 Protein-Protein Interactions`
  - `2.1.3 Ligands and Small Molecules`
  - `2.1.4 Nucleic Acids`
  - `2.2.1 Transformers`
  - `2.2.2 Diffusion Models`
  - `2.2.3 Protein Language Models`
  - `2.2.4 Geometric Deep Learning`
  - `2.3.1 RMSD`
  - `2.3.2 lDDT`
  - `2.3.3 DockQ`
- Substantially expanded:
  - `EN/1. AlphaFold3/1.5. Resources/1.5.4. Working with mmCIF Files.md`
    (metadata extraction, NumPy coordinates, interface analysis, AF3 output parsing, PDB download, write/modify workflow).
- Validated wiki-links in changed EN files: no broken targets detected.

## 12. Mermaid style unification (2026-03-11)

Applied a single Mermaid styling standard across newly added/updated EN and UA notes (Concepts + mmCIF resource):

- Standard node classes:
  - `input`
  - `trunk`
  - `diffusion`
  - `confidence`
  - `output`
  - `neutral`
- Added unified `classDef` palette (from `AGENTS.md`) to flowchart blocks.
- Replaced local/legacy class names (`root`, `sm`, `emb`, `clean`, `gen`, `model`, etc.) with the unified set.
- Goal: consistent semantics and visual rendering in Obsidian Reading view across EN/UA.

## 13. AGENTS/NOTICE update (2026-03-11)

- Synchronized `AGENTS.md` and `EN/AGENTS.md` with the current Mermaid rules.
- Added mandatory `flowchart` class standard: `input`, `trunk`, `diffusion`, `confidence`, `output`, `neutral`.
- Added explicit requirement: every `flowchart` must define `classDef` for all 6 classes.
- Documented exceptions for non-flowchart types (`timeline`, `mindmap`, `xychart-beta`, `quadrantChart`).

## 14. Adaptive page text width (2026-03-11)

- Added new snippet: `.obsidian/snippets/content-width.css`.
- Goal: make text **wider than default readable width** but **not full-width**.
- Implementation:
  - adaptive width via `clamp(860px, 86vw, 1180px)`,
  - centered content container,
  - same logic for Reading view and Editing view (CM6),
  - mobile profile via `@media (max-width: 900px)`.
- Snippet enabled in `.obsidian/appearance.json` as `content-width`.

## 15. Structure audit and instruction sync (2026-03-11)

- Re-checked vault structure against `AGENTS.md` / `EN/AGENTS.md`.
- Verified critical entry/index pages:
  - `Home.md`, `UA/Головна.md`, `UA/Індекс.md`, `EN/Index.md`.
- Verified parity of numbered note IDs between `UA/` and `EN/` (`1.x.x`–`4.x.x`): no mismatches found.
- Updated AGENTS instructions:
  - added system root entries `.git/`, `.gitignore`, `.obsidian/`, `.smart-env/`,
  - synchronized `README.md` presence in the structure example,
  - clarified allowed root files/directories list.

## 16. Bibliography unification and knowledge correction (2026-03-11)

- Reviewed and synchronized the core literature lists:
  - `UA/Література та пріоритети.md`
  - `EN/Literature and Priorities.md`
- Added an extra high-citation block (AF-Multimer, lDDT, TM-score, MMseqs2, ColabFold, RoseTTAFold, ESMFold, AF2 human proteome paper).
- Fixed an incorrect DOI in the UA PPI note:
  - `10.48550/arXiv.2109.22paym` → `10.1101/2021.10.04.463034`.
- Added missing DOI/source blocks to EN mirrors:
  - `EN/.../2.3.1. RMSD.md`,
  - `EN/.../2.3.2. lDDT.md`,
  - `EN/.../2.3.3. DockQ.md`,
  - `EN/.../2.1.2. Protein-Protein Interactions.md`.
- Applied standardized Mermaid node classes (`input/trunk/diffusion/confidence/output/neutral`) to PPI symmetry flowcharts in UA/EN.

## 17. AUDIT.md rule in AGENTS (2026-03-11)

- Updated `AGENTS.md` and `EN/AGENTS.md` with a dedicated `AUDIT.md` section.
- Recorded rule: run/create `AUDIT.md` **only on explicit user request**.
- Added operational requirement: the agent should **occasionally provide a lightweight reminder** to refresh the audit after major synchronization or mass edits.
- Added `AUDIT.md` to the allowed root-file list in agent rules.

## 18. New A3M resource note and UA↔EN synchronization (2026-03-18)

- Added a new paired resource note:
  - `UA/1. AlphaFold3/1.5. Ресурси/1.5.6. Робота з A3M файлами.md`
  - `EN/1. AlphaFold3/1.5. Resources/1.5.6. Working with A3M Files.md`
- Synchronized content across UA and EN:
  - `A3M` syntax,
  - difference between `A3M`, `FASTA`, and `Stockholm`,
  - practical Python parsing,
  - common CLI operations (`reformat.pl`, `hhfilter`, `hhmake`),
  - role of `A3M` in `AF3` featurization.
- Corrected an inaccurate `A3M` description in the `MSA` notes:
  - lowercase in `A3M` means **insertions**, not deletions;
  - `-` means a gap in an aligned column;
  - `.` may act as a placeholder in insert-only columns.
- Updated navigation in `Home.md` / `UA/Головна.md` and related links in resource notes.

## 19. UA `Featurization` file rename and link synchronization (2026-03-18)

- Renamed the UA file:
  - `UA/1. AlphaFold3/1.2. Архітектура/1.2.6. Феатуризація.md`
  - `UA/1. AlphaFold3/1.2. Архітектура/1.2.6. Featurization.md`
- Synchronized supporting references and wiki-links after the rename:
  - `AGENTS.md`
  - `EN/AGENTS.md`
  - `NOTICE.md`
  - `EN/NOTICE.md`
  - related UA/EN notes that link to `1.2.6`.
- No folder rename was required because no directory names used the old term.

## 20. Instruction refresh and vault audit (2026-03-18)

- Updated `AGENTS.md` and `EN/AGENTS.md`:
  - aligned the example vault tree with the actual structure (`AUDIT.md`, `1.5.5`, `1.5.6`, `2.2.5`, `2.2.6`),
  - added an explicit terminology rule for English STEM terms inside `UA/` titles and file names.
- Normalized the `## Related Notes` heading in two EN notes:
  - `EN/1. AlphaFold3/1.2. Architecture/1.2.6. Featurization.md`
  - `EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.4. MSA.md`
- Refreshed `AUDIT.md`:
  - confirmed numbered UA↔EN note parity,
  - checked absolute wiki-links (`0` missing targets),
  - recorded current DOI coverage and remaining citation gaps.
