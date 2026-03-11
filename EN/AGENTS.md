# AGENTS.md — Universal Instructions for AI Agents

> Rules for building and maintaining a bilingual STEM knowledge base in Obsidian.

---

## 1. Vault Structure

```text
AlphaFold3/
├── Home.md
├── AGENTS.md
├── NOTICE.md
├── UA/
│   ├── Головна.md
│   ├── Індекс.md
│   ├── Література та пріоритети.md
│   ├── 1. AlphaFold3/
│   │   ├── 1.1. Огляд/
│   │   ├── 1.2. Архітектура/
│   │   │   ├── 1.2.1. Загальна архітектура AF3.md
│   │   │   ├── 1.2.2. Pairformer.md
│   │   │   ├── 1.2.3. Diffusion Module.md
│   │   │   ├── 1.2.4. Diffusion Models — Theory and Applications.md
│   │   │   ├── 1.2.5. Model Training.md
│   │   │   └── 1.2.6. Феатуризація.md
│   │   ├── 1.3. Результати/
│   │   ├── 1.4. Обмеження/
│   │   ├── 1.5. Ресурси/
│   │   └── 1.6. Ілюстрації/
│   ├── 2. Концепції/
│   │   ├── 2.1. Біологія/
│   │   ├── 2.2. Машинне-Навчання/
│   │   └── 2.3. Структурна-Біоінформатика/
│   ├── 3. Моделі/
│   │   ├── 3.0. Огляд моделей.md
│   │   ├── 3.1. AlphaFold2.md
│   │   ├── 3.2. AlphaFold3.md
│   │   ├── 3.3. RoseTTAFold.md
│   │   ├── 3.4. ESMFold.md
│   │   └── 3.5. DiffDock.md
│   └── 4. Датасети/
│       ├── 4.0. Огляд датасетів.md
│       ├── 4.1. PDB.md
│       ├── 4.2. UniProt.md
│       ├── 4.3. AlphaFoldDB.md
│       └── 4.4. CASP.md
```
```text
└── EN/
    ├── AGENTS.md
    ├── NOTICE.md
    ├── Index.md
    ├── Literature and Priorities.md
    ├── 1. AlphaFold3/
    │   ├── 1.1. Overview/
    │   ├── 1.2. Architecture/
    │   │   ├── 1.2.1. AF3 Architecture Overview.md
    │   │   ├── 1.2.2. Pairformer.md
    │   │   ├── 1.2.3. Diffusion Module.md
    │   │   ├── 1.2.4. Diffusion Models — Theory and Applications.md
    │   │   ├── 1.2.5. Model Training.md
    │   │   └── 1.2.6. Featurization.md
    │   ├── 1.3. Results/
    │   ├── 1.4. Limitations/
    │   ├── 1.5. Resources/
    │   └── 1.6. Illustrations/
    ├── 2. Concepts/
    │   ├── 2.1. Biology/
    │   ├── 2.2. Machine-Learning/
    │   └── 2.3. Structural-Bioinformatics/
    ├── 3. Models/
    │   ├── 3.0. Models Overview.md
    │   ├── 3.1. AlphaFold2.md
    │   ├── 3.2. AlphaFold3.md
    │   ├── 3.3. RoseTTAFold.md
    │   ├── 3.4. ESMFold.md
    │   └── 3.5. DiffDock.md
    └── 4. Datasets/
        ├── 4.0. Datasets Overview.md
        ├── 4.1. PDB.md
        ├── 4.2. UniProt.md
        ├── 4.3. AlphaFoldDB.md
        └── 4.4. CASP.md
```

### 1.1 Rules

- `UA/` is Ukrainian-only, `EN/` is English-only.
- Hierarchical numbering: `1.`, `1.1.`, `1.1.1.`, and so on.
- Use absolute links from vault root only.
- Substantial UA notes must have EN mirrors.

### 1.2 EN ↔ UA Synchronization (required)

- Any content change in `UA/` or `EN/` must be mirrored in the corresponding note in the other language within the same PR/commit.
- "Synchronization" means not only file existence but parity of:
  - core `##` sections,
  - formulas, tables, and Mermaid diagrams,
  - practical code blocks,
  - `## Related Notes / ## Пов'язані нотатки` section.
- Differences are allowed only in language localization and phrasing style; technical content must remain equivalent.
- Before finishing, the agent must verify that neither UA nor EN is a shortened version of the same topic.

---

## 2. Note Format

### 2.1 Frontmatter (required)

```yaml
---
cssclasses: [note]                 # homepage, index-note, math-note, note
tags: [topic_name, domain_name]    # snake_case
---
```

### 2.2 Breadcrumb

```markdown
# Title

[[Home|Home]] > [[EN/1. AlphaFold3/1.2. Architecture/1.2.1. AF3 Architecture Overview|Architecture]] > Topic
🇺🇦 [[UA/1. AlphaFold3/1.2. Архітектура/1.2.2. Pairformer|Українська]]
```

### 2.3 Wiki-links

```markdown
✅ [[UA/1. AlphaFold3/1.2. Архітектура/1.2.2. Pairformer|Pairformer]]
✅ [[EN/1. AlphaFold3/1.2. Architecture/1.2.2. Pairformer|Pairformer]]
❌ `Pairformer`
❌ `Architecture/Pairformer`
```

### 2.4 Wiki-links inside tables

- Inside markdown tables: use only `[[path]]` — no alias.
- `[[path|alias]]` breaks table parsing due to the `|` character.

---

## 3. Visualization

- Do not use ASCII diagrams; use Mermaid only.
- Replace `\n` in Mermaid node labels with `<br/>`.
- `quadrantChart`: remove `quadrant-1..4` labels, keep axes + data points only.
- For math-heavy notes use `cssclasses: [math-note]`.

### 3.1 Mermaid unification (flowchart)

- For `flowchart`, use standardized node classes:
  - `input`
  - `trunk`
  - `diffusion`
  - `confidence`
  - `output`
  - `neutral`
- In each `flowchart` block, define `classDef` for all 6 classes using the shared palette.
- Do not use local/custom class names (`root`, `emb`, `model`, `clean`, `gen`, etc.).
- Exception: `timeline`, `mindmap`, `xychart-beta`, `quadrantChart` may omit `classDef` when readability is not reduced.

---

## 4. Sources

All scientific/technical claims require sources:

```markdown
> Author et al. (Year). *Title*. Venue.
> DOI: [10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)
```

---

## 5. Obsidian UI Hacks

- HTML may wrap wiki-links: `<span>[[Note]]</span>`.
- HTML inside `[[...]]` is forbidden.
- Prefer callouts for navigation blocks.

---

## 6. Prohibitions

- No relative links.
- No mixed languages inside one language folder.
- No non-system files in vault root.

---

## 7. NOTICE files

- Maintain formatting-change logs in `NOTICE.md` (UA) and `EN/NOTICE.md` (EN).
- Update these files after each mass rename, move, or formatting refactor.
- If a mass EN↔UA synchronization was performed, record it as a dedicated entry in both NOTICE files.

---

## 8. CSS and scaling

- Active snippets: `homepage`, `math-note`, `diagram-scale`.
- Theme: **GitHub Theme** — has its own `max-width` for `img`; snippets use explicit `!important` to override.
- `diagram-scale.css` — governs uniform scaling of Mermaid diagrams and images:
  - Mermaid SVG → `width: 100%` via `.mermaid svg`
  - Images → `width: 100%` via `img` (no `:not([class])`) + `.markdown-preview-section img`
  - `img[width]` exception: images with an explicit width attribute are not stretched (icons, badges)
  - `.note` scope added to all key rules for compatibility with `cssclasses: [note]`
- If illustrations disappear after CSS changes: check Excalidraw plugin settings first, then CSS.

---

## 9. Python sections in notes (1.2.6)

Note `1.2.6. Featurization` contains sections 10 and 11 with Python code.

| Section | Content |
|---|---|
| 10.1 | Dependencies (`numpy`, `rdkit`, `gemmi`, `biopython`) |
| 10.2 | Protein tokenization → one-hot `(L, 22)` |
| 10.3 | Ligand tokenization from SMILES → atoms + bond graph |
| 10.4 | A3M parsing + MSA encoding |
| 10.5 | Cβ distogram `(L, L, 39)` |
| 10.6 | Relative position encoding `(L, L, 65)` |
| 10.7 | `build_feature_dict()` — full feature dictionary |
| 11.0 | Table: what is possible with FASTA + mmCIF only |
| 11.1 | `parse_fasta()` |
| 11.2 | `sequence_from_mmcif()` + cross-check |
| 11.3 | `extract_ligand_features_from_mmcif()` |
| 11.4 | `backbone_unit_vectors()` + `plddt_from_mmcif()` |
| 11.5 | `featurize_from_fasta_and_mmcif()` — full pipeline |
| 11.6 | Table of features absent in no_msa mode |
| 11.7 | Databases + tools required for full MSA mode |

---

## 10. Agent Communication

- Reply in Ukrainian by default unless user asks for English.
- Never use Russian.
- Code examples, code comments, and identifiers in English.
- Technical terms format: `English term` — Ukrainian equivalent.
- Default programming language is Python if unspecified.
