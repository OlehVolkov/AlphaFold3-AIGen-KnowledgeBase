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
│   ├── 1. AlphaFold3/
│   │   ├── 1.1. Огляд/
│   │   ├── 1.2. Архітектура/
│   │   ├── 1.3. Результати/
│   │   ├── 1.4. Обмеження/
│   │   ├── 1.5. Ресурси/
│   │   └── 1.6. Ілюстрації/
│   └── 2. Концепції/
│       ├── …
│       ├── 2.1. Біологія/
│       ├── 2.2. Машинне-Навчання/
│       └── 2.3. Структурна-Біоінформатика/
│   ├── Індекс.md
│   └── Література та пріоритети.md
└── EN/
    ├── AGENTS.md
    ├── NOTICE.md
    ├── Index.md
    ├── Literature and Priorities.md
    ├── 2. Concepts/
    │   ├── …
    │   ├── 2.1. Biology/
    │   ├── 2.2. Machine-Learning/
    │   └── 2.3. Structural-Bioinformatics/
    └── 1. AlphaFold3/
        ├── 1.1. Overview/
        ├── 1.2. Architecture/
        ├── 1.3. Results/
        ├── 1.4. Limitations/
        └── 1.5. Resources/
```

### 1.1 Rules

- `UA/` is Ukrainian-only, `EN/` is English-only.
- Hierarchical numbering: `1.`, `1.1.`, `1.1.1.`, and so on.
- Use absolute links from vault root only.
- Substantial UA notes must have EN mirrors.

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

---

## 3. Visualization

- Do not use ASCII diagrams; use Mermaid.
- For math-heavy notes use `cssclasses: [math-note]`.

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

## 7. NOTICE files

- Maintain formatting-change logs in `NOTICE.md` (UA) and `EN/NOTICE.md` (EN).
- Update these files after each mass rename, move, or formatting refactor.

---

## 8. Agent Communication

- Reply in Ukrainian by default unless user asks for English.
- Never use Russian.
- Code examples, code comments, and identifiers in English.
- Technical terms format: `English term` — Ukrainian equivalent.
- Default programming language is Python if unspecified.
