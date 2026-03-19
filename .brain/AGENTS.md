# .brain AGENTS.md

Local instructions for agents working inside `/.brain`.

## Scope

- `/.brain` is the home for local research tooling, helper scripts, prompts, manifests, and small automation utilities.
- `/.brain/.index` stores generated artifacts only: indexes, caches, manifests, embeddings, and similar derived data.
- The Obsidian knowledge base itself stays in `UA/`, `EN/`, and root governance files.
- Prefer the current modular package layout in `/.brain/brain`; do not collapse logic back into a few oversized files.

## Ecosystem Overview

- Scientific PDF indexing is usually best designed as four layers:
  - parsing,
  - chunking and embeddings,
  - vector / full-text storage,
  - retrieval / reranking / RAG orchestration.
- Useful package families by layer:
  - parsing: `PyMuPDF`, `pdfplumber`, `Grobid`, `marker-pdf`, `Docling`
  - chunking / indexing: `LangChain`, `LlamaIndex`
  - embeddings: `sentence-transformers`, scientific models such as `SPECTER2` and `SciBERT`, or local `Ollama` embeddings
  - storage: `ChromaDB`, `FAISS`, `Qdrant`, `LanceDB`
  - retrieval / RAG: `Haystack`, `RAGatouille`, `rank_bm25`, `paper-qa`
- The current local default in `/.brain` is:
  - `PyMuPDF` for default PDF parsing
  - `pdfplumber` as a table-aware fallback
  - `LangChain` for chunking
  - `LanceDB` for vector + FTS + hybrid retrieval
  - `Ollama` for local embeddings and optional reranking
  - `brain/vault/` modules for markdown indexing over `UA/`, `EN/`, and root knowledge files
- This is the preferred default for the vault unless the task clearly needs:
  - better scientific-paper structure extraction (`Grobid`, `Docling`),
  - stronger scientific embedding models (`SPECTER2`, `SciBERT`),
  - or a different storage backend for scale / deployment constraints.

## Project Rules

- Use `uv` as the primary tool for Python environments, dependency management, and execution.
- Install `uv` with the official installer when needed:
  - macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Install Python with `uv` when a managed interpreter is needed:
  - `uv python install`
  - `uv python install 3.12`
- Use the local virtual environment at `/.brain/.venv`.
- Use `BaseSettings`-driven `pydantic` config under `/.brain/config` and `/.brain/.env`.
- Keep the CLI on `Typer`; use `Rich` for user-facing output and `Loguru` for runtime logging.
- Virtual environments are local-only artifacts and must never be committed.
- Prefer running Python through `uv`:
  - `UV_CACHE_DIR=/tmp/uv-cache /home/oleh/.local/bin/uv run ...`
- Prefer `uv add` over direct `pip install`.
- Prefer `uv venv` over manual `python -m venv`.
- Keep code changes in `/.brain` small, local, and automation-focused.
- Before adding or keeping a Python dependency, verify that it is actually needed by the current codebase.
- Prefer checking this explicitly via import search / usage search instead of assuming a package is still needed after refactors.
- If a direct dependency is no longer used, remove it from `pyproject.toml`, refresh `uv.lock`, and rerun tests.
- Prefer adding code to the existing package slices:
  - `brain/settings/`
  - `brain/common/`
  - `brain/pdf/`
  - `brain/pdf/backends/`
  - `brain/research/`
  - `brain/vault/`
  - `brain/commands/`
- Do not reintroduce compatibility facades such as flat re-export modules when the canonical package API is already clear.
- Do not write generated index data into notes or governance files.
- Do not commit secrets, credentials, `.env` values, or `PII`.
- Do not commit machine-specific overrides in `/.brain/config/local.toml`.
- Do not commit `/.brain/.env`.

Examples:

```bash
UV_CACHE_DIR=/tmp/uv-cache /home/oleh/.local/bin/uv venv .brain/.venv
```

```bash
UV_CACHE_DIR=/tmp/uv-cache /home/oleh/.local/bin/uv python install 3.12
```

```bash
UV_CACHE_DIR=/tmp/uv-cache /home/oleh/.local/bin/uv add --project .brain typer
```

```bash
UV_CACHE_DIR=/tmp/uv-cache /home/oleh/.local/bin/uv add --project .brain pydantic
```

```bash
UV_CACHE_DIR=/tmp/uv-cache /home/oleh/.local/bin/uv run --project .brain python -m brain
```

## File Layout

- `pyproject.toml` defines the local `brain` project.
- Run the CLI via `uv run --project .brain python -m brain ...`.
- `config/brain.toml` holds committed defaults.
- `config/local.toml` is an optional ignored local override file.
- `/.brain/.env` is an optional ignored dotenv override file.
- `brain/cli.py` is a thin Typer facade that registers commands from `brain/commands/`.
- `brain/settings/` is the canonical `BaseSettings` configuration loader and path resolver package.
- `brain/commands/` holds Typer command registration code.
- `brain/common/` holds shared utilities used by both PDF and vault indexing/search, including `Rich`/`Loguru` runtime helpers.
- Environment overrides should use nested names such as `BRAIN_OLLAMA__EMBED_MODEL`.
- `brain/pdf/` contains parser routing, indexing, retrieval, and reranking logic.
- `brain/pdf/backends/` contains isolated parser backends (`PyMuPDF`, `pdfplumber`, optional `Grobid`, optional `marker`).
- `brain/research/` contains the multi-role research loop, memory handling, reflection steps, and report formatting.
- `brain/vault/` contains markdown file discovery, section splitting, indexing, retrieval, and reranking logic.
- Keep files readable: prefer extracting cohesive submodules before a file becomes long or mixed-responsibility.
- `README.md` explains how to use the local project.
- `.venv/` is local-only and must never be committed.
- `.index/` is for generated data, not hand-authored documentation.

## Working Style

- Default to Python 3.12 via the local `uv` setup.
- Prefer deterministic scripts over ad hoc shell pipelines when logic will be reused.
- Keep outputs reproducible and scoped to repository needs.
- If a script updates vault content, make the target paths explicit and reviewable.
- Keep the modular structure stable; extend existing packages instead of adding new flat top-level helper files.
- Keep dependency hygiene strict: avoid stale direct dependencies and periodically audit `pyproject.toml` against actual imports.
- PDF search artifacts must stay under `/.brain/.index/pdf_search`.
- Vault markdown search artifacts must stay under `/.brain/.index/vault_search`.
- Research memory/session artifacts must stay under `/.brain/.index/research`.
- Under `WSL`, when the repository is mounted from `/mnt/c/...`, `LanceDB` may fail on the default `/.brain/.index/...` path.
- In that failure mode, keep the canonical default unchanged but rebuild the PDF index into `/tmp/alphafold3-pdf-index` and explicitly note that the active fallback artifacts are:
  - `/tmp/alphafold3-pdf-index/manifest.json`
  - `/tmp/alphafold3-pdf-index/lancedb`
- Also store the active fallback pointer in `/.brain/.index/pdf_search/active_index.json`.
- Apply the same rule to vault indexing when `index-vault` uses a fallback path:
  - fallback artifacts may live outside `/.brain/.index/vault_search`
  - store the active pointer in `/.brain/.index/vault_search/active_index.json`
- Under restricted sandbox environments, `LanceDB` may also hang during `connect()` or `open_table()` even when the fallback index under `/tmp/...` is valid.
- Use `brain check-index` to validate the active PDF or vault index, and make sure the command follows `active_index.json` when present.
- If `brain check-index` reports `status: timeout`, rerun it outside the sandbox before treating the index as corrupted.
