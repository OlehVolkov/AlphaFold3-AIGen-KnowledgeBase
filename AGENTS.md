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
    ├── README.md
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
- `README.md` and `UA/README.md` describe repository usage and should stay aligned at the policy level.

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

### 1.4.1 Codex Chat Access

- When this repository is used with Codex in chat, prefer Full Access mode over a restricted sandbox.
- This is especially important for tasks involving `/.brain`, indexing, retrieval, `Ollama`, `LanceDB`, health-checks, or runtime verification.
- Restricted sandbox runs may produce false negatives such as `LanceDB` hangs/timeouts or failed index checks even when the active fallback index is valid.
- If the task depends on confirming real local runtime behavior, the expected default is Full Access.

### 1.5 Python tooling

- Use `uv` as the primary tool for Python environments, dependency management, and script execution.
- `uv` installation examples:
  - macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Python installation examples with `uv`:
  - install the latest available Python: `uv python install`
  - install Python 3.12 for this repository: `uv python install 3.12`
- Prefer:
  - `uv venv` instead of `python -m venv`,
  - `uv add` instead of direct `pip install`,
  - `uv run` for Python entry points and scripts.
- Launcher conventions:
  - `uvx` is for one-off external Python CLI tools that should not be installed into the project environment.
  - Prefer `uvx` when you need a Python tool temporarily and do not want to add it to `/.brain/.venv`.
  - `npx` is the Node/npm analogue for one-off JavaScript CLI tools.
  - Use `npx` for non-Python tools such as `markdownlint-cli`; do not route npm tools through `uvx`.
- Avoid introducing parallel Python workflow conventions (`requirements.txt` + ad hoc `pip install`, manual virtualenv handling, mixed package managers) unless the repository or the user explicitly requires them.
- When adding Python automation under `/.brain`, keep the `uv` workflow explicit in local documentation and commands.
- For `/.brain`, the canonical environment is the Windows virtual environment at `/.brain/.venv`.
- Even when the agent is working from `WSL`, create, recreate, and sync `/.brain/.venv` through Windows `cmd.exe` with `uv`, not through a Linux `venv` layout.
- Do not keep parallel canonical environments such as `/.brain/.venvx`; `/.brain/.venv` is the single project environment for local `brain` work.
- When Docker is needed from `WSL` for this repository, invoke it through Windows `cmd.exe` as well.
- Prefer `cmd.exe /c "docker ..."` over calling Docker directly from the Linux shell in this repository workflow.
- Must not hardcode the local repository path in commands, docs, scripts, or examples.
- Prefer portable command patterns such as `%CD%`, relative paths from the current working directory, or explicit placeholders like `<REPO_ROOT>` instead of machine-specific absolute paths.

Examples:

```bash
cmd.exe /c "cd /d %CD%\.brain && uv python install 3.12"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && uv venv .venv --python 3.12"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv sync --all-groups"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run python -m brain"
```

- For local automation under `/.brain`, preserve the modular package layout:
  - `brain/config/`
  - `brain/shared/`
  - `brain/sources/pdf/`
  - `brain/sources/pdf/backends/`
  - `brain/sources/vault/`
  - `brain/research/`
  - `brain/mcp/tools/`
  - `brain/commands/`
- Prefer extending those packages over adding flat compatibility wrappers or oversized mixed-responsibility files.
- When maintaining `/.brain`, verify direct Python dependencies against actual imports/usages after refactors.
- Remove unused direct dependencies from `/.brain/pyproject.toml`, refresh `/.brain/uv.lock`, and rerun `/.brain` tests when cleanup is safe.
- For `/.brain`, treat `pytest`, `ruff`, and `mypy` as standard verification steps after Python changes.
- In `/.brain` Ruff configuration, keep `known-first-party = ["brain"]`; do not leave template placeholders such as `your_package`.

Verification examples:

```bash
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run pytest tests -q"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run ruff check brain tests"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run mypy brain"
```

### 1.5.1 BRAIN environment workflow

- Treat `/.brain/.venv` as the canonical local interpreter for `brain`.
- When invoking `brain` commands, ensure the underlying project environment is the Windows `/.venv`.
- If the agent is currently in `WSL`, prefer invoking Windows `uv` / Python through `cmd.exe /c "cd /d %CD%\.brain && ..."` for environment creation, dependency sync, and direct interpreter checks.
- In `cmd.exe`, call `uv` directly from `PATH`; do not use an absolute filesystem path to `uv.exe`.
- Apply the same rule to Docker commands needed for local tooling or services: invoke them through `cmd.exe`.
- Treat path portability as a must-have for all operational examples and automation snippets.

### 1.5.2 BRAIN-first workflow

- When `/.brain` provides retrieval or tool support for the current task, use it first instead of manually browsing the vault.
- Treat `/.brain` as the default operational layer for:
  - vault search,
  - PDF search,
  - note reads before edits,
  - experiment planning,
  - index health checks.
- Preferred execution order for knowledge-work tasks:
  1. `search-vault` or `search_pdfs` to gather grounded context.
  2. `read_note` for the specific notes that will be updated or compared.
  3. direct file edits only after retrieval confirms the target paths and context.
  4. `run_experiment` or `think` when the task needs multi-step synthesis instead of a single lookup.
- Prefer direct module or CLI usage over transport overhead when working locally in this repository:
  - `cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run python -m brain ..."`
  - local Python imports from `brain/...`
- Treat the `MCP` surface as the canonical tool contract for note and retrieval operations even when the same logic is invoked directly through Python.
- Do not bypass `/.brain` for convenience when the task depends on grounded retrieval, active index pointers, or repository-specific search logic.

### 1.6 WSL and Ollama

- If local model work uses Windows-hosted `Ollama` from `WSL`, prefer mirrored networking on `Windows 11 22H2+`.
- Keep the global WSL config in `%UserProfile%\\.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
dnsTunneling=true
autoProxy=true
firewall=true
```

- After editing `.wslconfig`, restart WSL with:

```powershell
wsl --shutdown
```

- In mirrored mode, verify Windows-side `Ollama` from `WSL` via:

```bash
curl http://127.0.0.1:11434/api/tags
```

- If mirrored mode is unavailable or disabled, run Windows `Ollama` with `OLLAMA_HOST=0.0.0.0:11434` in the Windows user environment variables and access it from `WSL` through the Windows host IP:

```bash
WIN_HOST=$(ip route show | awk '/default/ {print $3}')
curl "http://$WIN_HOST:11434/api/tags"
```

- Never copy secrets, tokens, credentials, private prompts, or personal data into `Ollama` prompts, shell history, note files, or versioned configuration files.

### 1.7 WSL and LanceDB

- If `/.brain` runs inside `WSL` while the repository lives on `/mnt/c/...`, `LanceDB` may fail on the default `/.brain/.index/...` path with I/O or metadata errors during table creation/overwrite.
- The canonical default still remains `/.brain/.index/...`.
- When that specific `WSL + /mnt/c + LanceDB` failure happens, use a Linux-native fallback index root:

```bash
cd .brain
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run python -m brain index --index-root /tmp/alphafold3-pdf-index"
```

- In this fallback mode, store the PDF index at:
  - `/tmp/alphafold3-pdf-index/manifest.json`
  - `/tmp/alphafold3-pdf-index/lancedb`
- Also write the active fallback pointer into:
  - `/.brain/.index/pdf_search/active_index.json`
- Use the same pointer pattern for a fallback vault index via:
  - `/.brain/.index/vault_search/active_index.json`
- Record clearly when the fallback path is being used so future runs do not assume that the active index is under `/.brain/.index/pdf_search`.
- Under restricted sandbox environments, `LanceDB` may also hang during `connect()` or `open_table()` even when the fallback index in `/tmp/...` is valid.
- Before concluding that an index is corrupted, verify it outside the sandbox with:

```bash
cd .brain
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run python -m brain check-index --target vault"
```

- `brain check-index` must read `active_index.json` when present and validate the currently active fallback index, not only the canonical `/.brain/.index/...` path.

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

### 3.2 Diagram readability and compactness

- Diagrams must be visually compact and easy to scan in Obsidian; do not optimize only for raw technical completeness.
- Prefer `flowchart LR` for short pipelines, comparisons, and metric/component summaries when it reduces vertical height.
- Prefer `flowchart TD` only when the process is inherently hierarchical or when left-to-right layout becomes too wide.
- Keep node labels short:
  - prefer `Query seq` over long examples,
  - prefer `DB search` over full database descriptions,
  - move detailed explanations below the diagram instead of inside nodes.
- Do not start Mermaid node labels with ordered-list-like prefixes such as `1.`, `2.`, `7.` or values like `76.4% ...` when a plain label or `Metric: value` form is possible.
- Avoid oversized diagrams:
  - if a diagram has too many nodes or long labels, split it into two smaller diagrams,
  - do not force one large "everything at once" flowchart when a pair of focused diagrams is clearer.
- For simple metric/component diagrams, prefer 4-6 nodes and 1-2 short lines per node.
- When a diagram becomes visually tall, first try:
  - shortening labels,
  - switching `TD` to `LR`,
  - moving details into bullets or a table below the diagram.

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
