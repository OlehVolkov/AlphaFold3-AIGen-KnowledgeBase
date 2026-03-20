# База знань AlphaFold3

Двомовний Obsidian vault про AlphaFold 3 і пов'язані STEM-теми.

## Призначення репозиторію

Цей репозиторій є Obsidian-базою знань з:

- стабільним двомовним деревом нотаток, де `UA/` містить українські матеріали, а `EN/` містить англомовні;
- правилами керування vault і редагування в `AGENTS.md`, `UA/AGENTS.md` і `BRAIN.md`;
- локальними research-інструментами в `/.brain`;
- згенерованими індексними даними в `/.brain/.index`;
- локальним сховищем PDF у `/PDF`.
- `uv` як основним Python-інструментом для локальної автоматизації.

Чинна двомовна структура є source of truth: `UA/` це українська гілка, а `EN/` це англомовна гілка.

## Root-структура

- `Home.md`: головна англомовна сторінка
- `UA/Головна.md`: головна українська сторінка
- `EN/`: англомовні нотатки
- `UA/`: українські нотатки
- `AGENTS.md`: англомовні правила репозиторію
- `UA/AGENTS.md`: українське дзеркало правил репозиторію
- `BRAIN.md`: правила research-agent workflow і retrieval-поведінки
- `AUDIT.md`: знімок аудиту й короткий quality summary
- `NOTICE.md`, `UA/NOTICE.md`: журнал структурних і форматних змін
- `/.brain`: локальна BRAIN-логіка, скрипти, prompts, utilities
- `/.brain/.index`: згенеровані index-дані, кеші, manifests, embeddings
- `/PDF`: локальне сховище PDF

## Структура бази знань

- `EN/1. AlphaFold3`: огляд, архітектура, результати, обмеження, ресурси, ілюстрації
- `EN/2. Concepts`: біологія, машинне навчання, структурна біоінформатика
- `EN/3. Models`: AlphaFold2, AlphaFold3, RoseTTAFold, ESMFold, DiffDock
- `EN/4. Datasets`: PDB, UniProt, AlphaFoldDB, CASP

## Правила редагування

Перед редагуванням:

1. Прочитати `AGENTS.md` або `UA/AGENTS.md`.
2. Прочитати `BRAIN.md`, якщо задача стосується retrieval, indexing, automation або research-workflows.
3. Зберігати чинну двомовну структуру: `UA/` для української, `EN/` для англійської.
4. Використовувати лише absolute wiki-links від кореня vault.
5. Строго розділяти мови:
   - `UA/` лише українською
   - `EN/` лише англійською
6. Дзеркалити суттєві зміни змісту між UA/EN.
7. Оновлювати `NOTICE.md` і `UA/NOTICE.md` після масових перейменувань, переносів або структурних рефакторингів.

## Доступ для Codex

Коли `Codex` використовується в чаті для цього репозиторію, пріоритетно надавати режим Full Access, а не restricted sandbox.

Причина:

- локальні indexing і health-check сценарії можуть залежати від прямого доступу до файлової системи, fallback-індексів у `/tmp` і реальної runtime-поведінки `Ollama` / `LanceDB`
- запуски в restricted sandbox можуть давати хибні негативні результати, наприклад `LanceDB timeout` або failed index health-check, навіть коли реальний індекс валідний

Якщо задача `Codex` стосується indexing, retrieval, `/.brain`, `Ollama`, `LanceDB` або runtime-перевірок, очікуваний default це Full Access.

## Локальні research-каталоги

- `/.brain`: місце для reusable local tooling
- `/.brain/.index`: місце для generated indexing data
- `/PDF`: місце для локальних PDF

Правила:

- `/PDF` це локальне сховище source files
- PDF payload files у `/PDF` не повинні комітитися
- generated index data мають лишатися в `/.brain/.index`, а не в дереві нотаток
- не можна виносити секрети, `.env` значення, credentials або `PII` у нотатки, індекси чи governance-файли
- для Python-оточень, залежностей і запуску скриптів пріоритетно використовувати `uv`

## Локальний Python tooling

Встановлення:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
uv python install 3.12
```

- Для оточень пріоритетно використовувати `uv venv`.
- Для залежностей пріоритетно використовувати `uv add`.
- Для запуску Python-скриптів і entry points пріоритетно використовувати `uv run`.
- Не змішувати `uv` з довільними `pip install` / ручними `venv`-workflow, якщо задача явно не вимагає такого сумісного режиму.
- Для `/.brain` використовувати Windows project environment у `/.brain/.venv` як єдиний canonical env.
- Навіть із `WSL` створювати та синхронізувати `/.brain/.venv` через `cmd.exe` і `uv`.
- У `cmd.exe` викликати `uv` напряму через `PATH`; не використовувати повний файловий шлях до `uv.exe`.
- Для цього репозиторію при роботі з `WSL` Docker теж слід викликати через Windows `cmd.exe`.
- Для `/.brain` перед завершенням локальних Python-змін запускати і тести, і `flake8`.

Приклади:

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

```bash
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run pytest tests -q"
```

```bash
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run flake8 brain tests"
```

## WSL і Ollama

Якщо `Ollama` запущена у Windows, а використовувати її треба з `WSL`, пріоритетно вмикати mirrored networking на `Windows 11 22H2+`.

Створи `%UserProfile%\\.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
dnsTunneling=true
autoProxy=true
firewall=true
```

Потім перезапусти `WSL`:

```powershell
wsl --shutdown
```

Після цього `WSL` зазвичай може звертатися до Windows-екземпляра `Ollama` через:

```bash
curl http://127.0.0.1:11434/api/tags
```

Якщо mirrored mode недоступний або вимкнений, потрібно перезапустити Windows-застосунок `Ollama` зі змінною `OLLAMA_HOST=0.0.0.0:11434` у користувацьких змінних середовища Windows, а потім звертатися до нього з `WSL` через IP Windows-хоста:

```bash
WIN_HOST=$(ip route show | awk '/default/ {print $3}')
curl "http://$WIN_HOST:11434/api/tags"
```

Типові приклади використання з `WSL`:

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

Не зберігати токени, credentials чи інші секрети в prompts для `Ollama`, shell history, note-файлах або versioned config files.

## WSL і LanceDB

Коли `/.brain` запускається в `WSL` для репозиторію, що лежить на `/mnt/c/...`, `LanceDB` може падати з низькорівневими `I/O` або `metadata`-помилками під час створення чи перезапису таблиць усередині `/.brain/.index/...`.

Базове правило лишається таким:

- generated index data зберігаються в `/.brain/.index`

Якщо індексація PDF падає саме в цьому сценарії `WSL + /mnt/c + LanceDB`, треба використовувати fallback-шлях у Linux-native файловій системі замість Windows-mounted каталогу репозиторію:

```bash
cd .brain
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run python -m brain index --index-root /tmp/alphafold3-pdf-index"
```

У fallback-режимі індекс зберігається тут:

- `/tmp/alphafold3-pdf-index/manifest.json`
- `/tmp/alphafold3-pdf-index/lancedb`

Додатково canonical-каталог індексу зберігає локальний pointer-файл з активним fallback-шляхом:

- `/.brain/.index/pdf_search/active_index.json`

Цей fallback є тимчасовим/локальним для поточної машини і має використовуватись лише тоді, коли `LanceDB` падає на стандартному шляху `/.brain/.index/...` під `WSL`.

Та сама схема застосовується і до markdown-індексу vault, якщо `index-vault` будується у fallback-шляху: pointer-файл треба тримати в `/.brain/.index/vault_search/active_index.json`.

Важлива runtime-нотатка:

- у restricted sandbox-середовищах `LanceDB` може також зависати на `connect()` або `open_table()`, навіть якщо fallback-індекс у `/tmp/...` реально валідний
- коли треба перевірити, чи індекс справді читається, запускати health-check поза sandbox:

```bash
cd .brain
cmd.exe /c "cd /d %CD%\.brain && set UV_PROJECT_ENVIRONMENT=.venv && uv run python -m brain check-index --target vault"
```

- команда автоматично читає `active_index.json` і перевіряє активний fallback-індекс, якщо pointer присутній
- якщо команда повертає `status: timeout`, спочатку повторити її поза sandbox, а вже потім вважати індекс пошкодженим

## Обов'язкові Obsidian plugins

Community plugins, потрібні для цього vault (`.obsidian/community-plugins.json`):

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

## Рекомендовані plugin settings

Для Excalidraw embeds у Reading view:

- `renderImageInMarkdownReadingMode: true`
- `mdSVGwidth: 1200`
- `mdSVGmaxHeight: 1600`

Ці значення вже задані в `.obsidian/plugins/obsidian-excalidraw-plugin/data.json`.

## CSS snippets

Увімкнені snippets (`.obsidian/appearance.json`):

- `homepage`
- `math-note`
- `diagram-scale`
- `content-width`

## Відкриття vault

1. Клонувати репозиторій.
2. Відкрити папку як Obsidian vault.
3. Увімкнути Community Plugins, коли Obsidian запропонує це зробити.
4. Відкрити `Home.md` або `UA/Головна.md`.
