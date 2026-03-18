# AlphaFold3 Knowledge Base

Bilingual Obsidian vault for AlphaFold 3 and related STEM topics.

## Repository Purpose

This repository is an Obsidian knowledge base with:

- a stable bilingual note tree where `UA/` stores Ukrainian notes and `EN/` stores English notes
- vault governance and editing rules in `AGENTS.md`, `UA/AGENTS.md`, and `BRAIN.md`
- local research helpers in `/.brain`
- generated indexing data in `/.brain/.index`
- local PDF storage in `/PDF`

The existing bilingual layout is the source of truth: `UA/` is the Ukrainian branch, while `EN/` is the English branch.

## Root Layout

- `Home.md`: main English landing page
- `UA/Головна.md`: main Ukrainian landing page
- `EN/`: English notes
- `UA/`: Ukrainian notes
- `AGENTS.md`: English repository rules
- `UA/AGENTS.md`: Ukrainian mirror of repository rules
- `BRAIN.md`: research-agent and retrieval workflow rules
- `AUDIT.md`: audit snapshot and quality summary
- `NOTICE.md`, `UA/NOTICE.md`: change log for structural and formatting refactors
- `/.brain`: local BRAIN logic, scripts, prompts, utilities
- `/.brain/.index`: generated index data, caches, manifests, embeddings
- `/PDF`: local PDF storage

## Knowledge Base Structure

- `EN/1. AlphaFold3`: overview, architecture, results, limitations, resources, illustrations
- `EN/2. Concepts`: biology, machine learning, structural bioinformatics
- `EN/3. Models`: AlphaFold2, AlphaFold3, RoseTTAFold, ESMFold, DiffDock
- `EN/4. Datasets`: PDB, UniProt, AlphaFoldDB, CASP

## Editing Rules

Before editing:

1. Read `AGENTS.md` or `UA/AGENTS.md`.
2. Read `BRAIN.md` if the task involves retrieval, indexing, automation, or research workflows.
3. Preserve the existing bilingual layout: `UA/` for Ukrainian and `EN/` for English.
4. Keep absolute wiki-links from vault root.
5. Keep language separation strict:
   - `UA/` only Ukrainian
   - `EN/` only English
6. Mirror substantive UA/EN content changes in both languages.
7. Update `NOTICE.md` and `UA/NOTICE.md` after mass renames, moves, or structural refactors.

## Local Research Directories

- `/.brain`: place reusable local tooling here
- `/.brain/.index`: place generated indexing data here
- `/PDF`: place local PDFs here

Rules:

- `/PDF` is local storage for source files
- PDF payload files in `/PDF` must not be committed
- generated index data should stay in `/.brain/.index`, not in the note tree
- do not expose secrets, `.env` values, credentials, or `PII` in notes, indexes, or governance files

## Required Obsidian Plugins

Community plugins required by this vault (`.obsidian/community-plugins.json`):

- `obsidian-git`
- `dataview`
- `obsidian-excalidraw-plugin`
- `editing-toolbar`
- `obsidian-linter`
- `obsidian-advanced-slides`
- `smart-connections`
- `jupymd`
- `homepage`
- `mermaid-tools`

## Recommended Plugin Settings

For Excalidraw embeds in Reading view:

- `renderImageInMarkdownReadingMode: true`
- `mdSVGwidth: 1200`
- `mdSVGmaxHeight: 1600`

These values are already set in `.obsidian/plugins/obsidian-excalidraw-plugin/data.json`.

## CSS Snippets

Enabled snippets (`.obsidian/appearance.json`):

- `homepage`
- `math-note`
- `diagram-scale`
- `content-width`

## Open the Vault

1. Clone this repository.
2. Open the folder as an Obsidian vault.
3. Enable Community Plugins when prompted.
4. Open `Home.md` or `UA/Головна.md`.
