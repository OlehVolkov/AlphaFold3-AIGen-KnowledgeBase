# AlphaFold3 Knowledge Base

Bilingual Obsidian vault for AlphaFold 3 and related STEM topics.

## Repository Purpose

This repository is an Obsidian knowledge base with:

- a stable bilingual note tree where `UA/` stores Ukrainian notes and `EN/` stores English notes
- vault governance and editing rules in `AGENTS.md`, `UA/AGENTS.md`, and `BRAIN.md`
- local research helpers in `/.brain`
- generated indexing data in `/.brain/.index`
- local PDF storage in `/PDF`
- `uv` as the primary Python tool for local automation

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
- `/.brain/brain/`: modular Python package for settings, PDF indexing, vault indexing, research loops, and CLI commands
- `/.brain` CLI stays on `Typer`, with `Rich` for output and `Loguru` for logging

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

## Codex Access

When using Codex in chat for this repository, prefer Full Access mode instead of a restricted sandbox.

Reason:

- local indexing and health-check flows may depend on direct filesystem access, `/tmp` fallback indexes, and real local `Ollama` / `LanceDB` runtime behavior
- restricted sandbox runs can produce false negatives such as `LanceDB` timeouts or failed index health-checks even when the actual index is valid

If a Codex task involves indexing, retrieval, `/.brain`, `Ollama`, `LanceDB`, or runtime verification, the expected default is Full Access.

## Local Research Directories

- `/.brain`: place reusable local tooling here
- `/.brain/.index`: place generated indexing data here
- `/PDF`: place local PDFs here

Rules:

- `/PDF` is local storage for source files
- PDF payload files in `/PDF` must not be committed
- generated index data should stay in `/.brain/.index`, not in the note tree
- do not expose secrets, `.env` values, credentials, or `PII` in notes, indexes, or governance files
- use `uv` as the primary tool for Python virtual environments, dependencies, and script execution

## Local Python Tooling

Installation:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
uv python install 3.12
```

- Prefer `uv venv` for environments.
- Prefer `uv add` for dependencies.
- Prefer `uv run` for Python scripts and entry points.
- `uvx` is for one-off external Python CLI tools that should not be installed into the project environment.
- `npx` is for one-off Node/npm CLI tools.
- For this repository, run `markdownlint-cli` through `npx`; it is not a Python tool and should not be routed through `uvx`.
- Avoid mixing `uv` with ad hoc `pip install` / manual `venv` workflows unless a task explicitly requires that compatibility path.
- For `/.brain`, use the Windows project environment at `/.brain/.venv` as the single canonical environment.
- Even from `WSL`, create and sync `/.brain/.venv` through `cmd.exe` and `uv`.
- In `cmd.exe`, call `uv` directly from `PATH`; do not use a full filesystem path to `uv.exe`.
- For this repository, invoke Docker through Windows `cmd.exe` as well when working from `WSL`.
- In `/.brain` Ruff configuration, use `known-first-party = ["brain"]` for import sorting; do not keep template placeholders such as `your_package`.
- Keep `/.brain` code modular; prefer extending the existing package layout instead of adding flat compatibility files.
- For `/.brain`, periodically audit direct dependencies against actual imports and remove stale packages when they are no longer used.
- For `/.brain`, use `pytest`, `ruff`, and `mypy` as the verification toolbox.
- By default, run `ruff` and `mypy` plus targeted pytest files related to the changed code.
- Run the full `pytest tests -q` suite only for broad refactors, cross-cutting changes, or when you explicitly want the whole suite.
- Use `cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run python -m brain think \"your query\""` for the local multi-role research loop with memory and reflection.

Examples:

```bash
cmd.exe /c "cd /d %CD%\.brain && uv python install 3.12"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && uv venv .venv --python 3.12"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv sync --all-groups"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run python -m brain"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run pytest tests/test_cli.py -q"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run ruff check brain tests"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run mypy brain"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run pytest tests -q"
```

```bash
uvx ruff check .
```

```bash
npx --yes markdownlint-cli@0.39.0 '**/*.md' --ignore node_modules --ignore .git --ignore .obsidian --config markdownlint.jsonc
```

## WSL and Ollama

If `Ollama` runs on Windows and you want to use it from `WSL`, prefer mirrored networking on `Windows 11 22H2+`.

Create `%UserProfile%\\.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
dnsTunneling=true
autoProxy=true
firewall=true
```

Then restart WSL:

```powershell
wsl --shutdown
```

After that, `WSL` can usually reach the Windows-side `Ollama` API via:

```bash
curl http://127.0.0.1:11434/api/tags
```

If mirrored mode is unavailable or disabled, restart the Windows `Ollama` app with `OLLAMA_HOST=0.0.0.0:11434` set in the Windows user environment variables, then query it from `WSL` through the Windows host IP:

```bash
WIN_HOST=$(ip route show | awk '/default/ {print $3}')
curl "http://$WIN_HOST:11434/api/tags"
```

Typical `WSL` usage examples:

```bash
ollama run llama3.2
```

```bash
curl http://127.0.0.1:11434/api/generate \
  -d '{
    "model": "llama3.2",
    "prompt": "Explain AlphaFold 3 in two sentences.",
    "stream": false
  }'
```

Do not store tokens, credentials, or other secrets in `Ollama` prompts, shell history, note files, or versioned config files.

## WSL and LanceDB

When `/.brain` runs under `WSL` against a repository located on `/mnt/c/...`, `LanceDB` may fail with low-level I/O or metadata errors while creating or overwriting tables inside `/.brain/.index/...`.

Default behavior remains:

- generated index data lives in `/.brain/.index`

If PDF indexing fails in this `WSL + /mnt/c + LanceDB` scenario, use a Linux-native fallback path instead of the Windows-mounted repository filesystem:

```bash
cd .brain
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run python -m brain index --index-root /tmp/alphafold3-pdf-index"
```

In that fallback mode, the index is stored at:

- `/tmp/alphafold3-pdf-index/manifest.json`
- `/tmp/alphafold3-pdf-index/lancedb`

Additionally, the canonical index directory keeps a local pointer file with the active fallback location:

- `/.brain/.index/pdf_search/active_index.json`

This fallback is temporary/local to the current machine and should be used only when `LanceDB` fails on the default `/.brain/.index/...` path under `WSL`.

Apply the same pattern to the vault markdown index when `index-vault` is built in a fallback location: keep the pointer file at `/.brain/.index/vault_search/active_index.json`.

Important runtime note:

- under restricted sandbox environments, `LanceDB` can also hang during `connect()` or `open_table()` even when the fallback index under `/tmp/...` is valid
- when you need to verify whether an index is actually readable, run the health-check outside the sandbox:

```bash
cd .brain
cmd.exe /c "cd /d %CD%\.brain && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run python -m brain check-index --target vault"
```

- the command reads `active_index.json` automatically and checks the active fallback index when a pointer is present
- if the command reports `status: timeout`, retry it outside the sandbox before assuming the index is corrupted

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
