# AGENTS.md — Universal Instructions for AI Agents

> Rules for building and maintaining a bilingual STEM knowledge base in Obsidian.

---

## 1. Vault Structure

```text
AlphaFold3/
├── .git/
├── .gitignore
├── .brain/
│   └── .index/
├── .obsidian/
├── .smart-env/
├── PDF/
├── AGENTS.md
├── Home.md
├── AUDIT.md
├── BRAIN.md
├── EN/
│   ├── 1. AlphaFold3/
│   ├── 2. Concepts/
│   ├── 3. Models/
│   ├── 4. Datasets/
│   ├── Index.md
│   ├── Literature and Priorities.md
│   └── Summary.md              ← optional technical implementation summary/blueprint
├── NOTICE.md
├── README.md
└── UA/
    ├── AGENTS.md
    ├── NOTICE.md
    ├── Головна.md
    ├── Індекс.md
    ├── Література та пріоритети.md
    ├── 1. AlphaFold3/
    ├── 2. Концепції/
    ├── 3. Моделі/
    └── 4. Датасети/
```

### 1.1 Rules

- `UA/` is Ukrainian-only, while `EN/` is English-only.
- Hierarchical numbering: `1.`, `1.1.`, `1.1.1.`, and so on.
- Use absolute links from vault root only.
- Substantial UA notes must have EN mirrors.
- `Home.md` is the main English entry point; `EN/Summary*.md` files are allowed for technical digests/implementation notes.

### 1.2 EN ↔ UA Synchronization (required)

- Any content change in `UA/` or in an `EN/` note must be mirrored in the corresponding note in the other language within the same PR/commit.
- "Synchronization" means not only file existence but parity of:
  - core `##` sections,
  - formulas, tables, and Mermaid diagrams,
  - practical code blocks,
  - `## Related Notes / ## Пов'язані нотатки` section.
- Differences are allowed only in language localization and phrasing style; technical content must remain equivalent.
- Before finishing, the agent must verify that neither UA nor EN is a shortened version of the same topic.

### 1.3 Terminology and naming

- Inside `UA/`, English STEM terms may remain in titles and file/folder names when the Ukrainian analogue is non-standard, awkward, or weaker than the domain-standard term.
- Typical examples: `Featurization`, `recycling`, `Pairformer`, `Template Embedder`.
- If a natural Ukrainian analogue exists, use a paired first mention:
  - `English term` (Ukrainian equivalent), or
  - Ukrainian equivalent (`English term`).
- Once a term choice is made, keep it consistent across the file name, title, breadcrumb, `Related Notes`, and wiki-links.

### 1.4 Secrets and personal data

- Before creating, updating, indexing, or committing files, the agent must check whether any of the following would be exposed:
  - secrets (`API keys`, tokens, passwords, private keys, session cookies, credentials, `.env` values),
  - personal data (`PII`) or other sensitive local user data.
- Such data must not be intentionally copied into:
  - `UA/` notes / `EN/` notes,
  - `NOTICE.md`, `UA/NOTICE.md`, `AUDIT.md`, `EN/Summary*.md`, `BRAIN.md`, `AGENTS.md`, `UA/AGENTS.md`,
  - `/.brain/.index`, `/.brain`, `PDF/`, or other versioned files.
- If the source material contains secrets or personal data, the agent must:
  - avoid copying them verbatim into the repository,
  - redact or mask them when possible,
  - explicitly warn the user about the risk if safe continuation would otherwise be unclear.

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

### 2.5 New Content Sections (required)

- When adding a new content section or a new conceptual note, do not stop at a short definition.
- By default, gather **expanded** material in the style of a deeper overview unless the user explicitly asks for a short version.
- Minimum expected structure of a new section:
  - `why it is possible / why it matters`;
  - main approaches or architecture variants;
  - key properties;
  - limitations;
  - examples of related methods, models, or practical applications.
- For technical topics, also prefer adding formulas, Mermaid diagrams, comparison tables, practical code blocks, or short case studies where appropriate.
- If a topic already has a short note, do not leave it in a "collapsed" form after expansion: the updated UA/EN versions should both remain sufficiently complete.

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
- Do not add non-system files to vault root.
- Do not commit secrets, `PII`, or other sensitive local data.
- Allowed root files/directories: `.git/`, `.gitignore`, `.brain/`, `.obsidian/`, `.smart-env/`, `PDF/`, `Home.md`, `README.md`, `AGENTS.md`, `BRAIN.md`, `NOTICE.md`, `AUDIT.md`, `EN/`, `UA/`.

---

## 7. NOTICE files

- Maintain formatting-change logs in `UA/NOTICE.md` (UA) and `NOTICE.md` (EN).
- Update these files after each mass rename, move, or formatting refactor.
- If a mass EN↔UA synchronization was performed, record it as a dedicated entry in both NOTICE files.

---

## 8. AUDIT file

- Create/update `AUDIT.md` only on explicit user request.
- A standard audit includes:
  - structural integrity checks (key pages and UA↔EN parity),
  - wiki-link integrity checks,
  - DOI/source checks,
  - a `Confidence Level` matrix for core domains.
- After an audit, log notable format/consistency changes in `UA/NOTICE.md` and `NOTICE.md` (if changes were applied).
- Even when no audit is executed, the agent should occasionally provide a lightweight reminder to refresh `AUDIT.md` (especially after major synchronization or mass edits).

---

## 9. CSS and scaling

- Active snippets: `homepage`, `math-note`, `diagram-scale`, `content-width`.
- Theme: **GitHub Theme** — has its own `max-width` for `img`; snippets use explicit `!important` to override.
- `diagram-scale.css` — governs uniform scaling of Mermaid diagrams and images:
  - Mermaid SVG → `width: 100%` via `.mermaid svg`
  - Images → `width: 100%` via `img` (no `:not([class])`) + `.markdown-preview-section img`
  - `img[width]` exception: images with an explicit width attribute are not stretched (icons, badges)
  - `.note` scope added to all key rules for compatibility with `cssclasses: [note]`
- `content-width.css` — adaptive text container width:
  - wider than default readable width but not full-width,
  - `clamp(860px, 86vw, 1180px)` on desktop/tablet,
  - dedicated alignment for Reading + Editing (CM6).
- If illustrations disappear after CSS changes: check Excalidraw plugin settings first, then CSS.

---

## 10. Python sections in notes (1.2.6)

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

## 11. Agent Communication

- Reply in Ukrainian by default unless user asks for English.
- Never use Russian.
- Code examples, code comments, and identifiers in English.
- Keep an English technical term when it is more natural than the Ukrainian alternative.
- If a good Ukrainian equivalent exists, use a paired first mention: `English term` (Ukrainian equivalent) or Ukrainian equivalent (`English term`).
- Default programming language is Python if unspecified.
