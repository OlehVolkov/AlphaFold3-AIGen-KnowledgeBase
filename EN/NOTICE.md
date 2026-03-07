# NOTICE — Formatting Fix Log

Last updated: 2026-03-07 (updated)
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

## 8. Diagram and illustration scaling

- Use `.obsidian/snippets/diagram-scale.css`.
- Goal: Mermaid and Excalidraw should match text container width (`100%`) with readable text.
- If illustrations disappear after styling: check Excalidraw plugin settings first, then CSS.

## 9. File maintenance

- Keep this file updated after every major formatting or structure refactor.
- Ukrainian counterpart: `NOTICE.md`.
