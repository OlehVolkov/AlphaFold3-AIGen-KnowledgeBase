# AGENTS.md — Універсальні інструкції для AI-агентів

> Правила побудови й підтримки двомовної STEM-бази знань в Obsidian.

---

## 1. Структура vault

```text
AlphaFold3/
├── .git/
├── .gitignore
├── .brains/
│   ├── BRAIN.md
│   └── .index/
├── .obsidian/
├── .smart-env/
├── PDF/
├── AGENTS.md
├── Home.md
├── AUDIT.md
├── EN/
│   ├── 1. AlphaFold3/
│   ├── 2. Concepts/
│   ├── 3. Models/
│   ├── 4. Datasets/
│   ├── Index.md
│   ├── Literature and Priorities.md
│   └── Summary.md
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

### 1.1 Правила

- `UA/` — лише українська, `EN/` — лише англійська.
- Ієрархічна нумерація: `1.`, `1.1.`, `1.1.1.` і далі.
- Посилання лише абсолютні від кореня vault.
- Суттєві UA-нотатки мають EN-дзеркало.
- `Home.md` — головна англомовна точка входу; `EN/Summary*.md` дозволені як технічні дайджести/implementation-нотатки.
- `README.md` і `UA/README.md` описують використання репозиторію та мають лишатися синхронними на рівні політик.
- Для retrieval, indexing, automation і research-agent workflow канонічним файлом інструкцій є `/.brains/BRAIN.md`; не слід знову створювати `BRAIN.md` у корені.

### 1.2 Синхронізація EN ↔ UA (обов'язково)

- Будь-яка зміна змісту в `UA/` або в нотатці з `EN/` має дзеркально оновлювати відповідник в іншій мові в межах цього ж PR/коміту.
- Під "синхронізацією" мається на увазі не тільки наявність файлу, а й паритет по:
  - ключових розділах `##`,
  - формулах, таблицях, Mermaid-діаграмах,
  - практичних блоках коду,
  - секції `## Пов'язані нотатки / ## Related Notes`.
- Допускається різниця лише в мовній локалізації та стилі формулювань; технічний зміст має бути еквівалентним.
- Перед завершенням змін агент повинен перевірити, що обидві версії (UA/EN) не мають "скороченого" варіанту однієї теми.

### 1.3 Термінологія і назви

- У `UA/` дозволено лишати англійські STEM-терміни в заголовках, назвах файлів і папок, якщо український відповідник неусталений, звучить неприродно або поступається domain standard.
- Типові приклади таких термінів: `Featurization`, `recycling`, `Pairformer`, `Template Embedder`.
- Якщо природний український відповідник існує, при першій змістовій згадці використовувати парну форму:
  - `English term` (український відповідник), або
  - український відповідник (`English term`).
- Після вибору терміна використовувати його послідовно в назві файла, заголовку, breadcrumb, `Related Notes` і wiki-links.

### 1.4 Секрети та персональні дані

- Перед створенням, оновленням, індексацією або комітом файлів агент повинен перевіряти, чи не компрометуються:
  - секрети (`API keys`, токени, паролі, приватні ключі, session cookies, credentials, `.env` значення),
  - персональні дані (`PII`) або чутливі локальні дані користувача.
- Заборонено навмисно виносити такі дані в:
  - нотатки `UA/` / нотатки `EN/`,
  - `NOTICE.md`, `UA/NOTICE.md`, `AUDIT.md`, `EN/Summary*.md`, `/.brains/BRAIN.md`, `AGENTS.md`, `UA/AGENTS.md`,
  - `/.brains/.index`, `/.brains`, `PDF/` або інші versioned файли.
- Якщо вхідні матеріали містять секрети або персональні дані, агент повинен:
  - не копіювати їх дослівно в репозиторій,
  - за можливості редагувати або маскувати їх,
  - явно попередити користувача про ризик, якщо без цього не можна коректно продовжити.

### 1.4.1 Доступ Codex у чаті

- Коли цей репозиторій використовується з `Codex` у чаті, пріоритетно надавати режим Full Access замість restricted sandbox.
- Це особливо важливо для задач, пов'язаних із `/.brains`, indexing, retrieval, `Ollama`, `LanceDB`, health-check або runtime-перевіркою.
- Запуски в restricted sandbox можуть давати хибні негативні результати, зокрема `LanceDB` hangs/timeouts або failed index checks, навіть коли активний fallback-індекс валідний.
- Якщо задача залежить від перевірки реальної локальної runtime-поведінки, очікуваний default це Full Access.

### 1.5 Python tooling

- `uv` є основним інструментом для Python-оточень, керування залежностями й запуску скриптів.
- Приклади встановлення `uv`:
  - macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Приклади встановлення Python через `uv`:
  - встановити найновіший доступний Python: `uv python install`
  - встановити Python 3.12 для цього репозиторію: `uv python install 3.12`
- Пріоритетні команди:
  - `uv venv` замість `python -m venv`,
  - `uv add` замість прямого `pip install`,
  - `uv run` для запуску Python entry points і скриптів.
- Конвенції launcher-ів:
  - `uvx` використовувати для одноразового запуску зовнішніх Python CLI tools, які не треба встановлювати в проєктне середовище.
  - `uvx` доречний тоді, коли потрібен Python tool тимчасово й без додавання в `/.brains/.venv`.
  - `npx` є Node/npm-аналогом для одноразового запуску JavaScript CLI tools.
  - Для non-Python tools на кшталт `markdownlint-cli` використовувати `npx`, а не `uvx`.
- Не вводити паралельні Python-workflows (`requirements.txt` + довільний `pip install`, ручне керування virtualenv, змішані package managers), якщо цього явно не вимагає сам репозиторій або запит користувача.
- Якщо Python-автоматизація додається в `/.brains`, `uv`-workflow має бути явно відображений у локальній документації та прикладах команд.
- Якщо для задачі потрібен reusable helper script, його слід зберігати в `/.scripts`, а не залишати як тимчасовий одноразовий артефакт.
- Якщо скрипт специфічний саме для workflow `/.brains`, його слід тримати в `/.brains/scripts`, а не в кореневому `/.scripts`.
- Скрипти, додані в `/.scripts` або `/.brains/scripts`, повинні містити короткий header comment або docstring, який пояснює:
  - що саме робить скрипт,
  - які repository-specific constants або structural assumptions треба перевірити насамперед при адаптації під інший репозиторій.
- Такі helper scripts варто писати з розрахунком на повторне використання або адаптацію іншими агентами в подібних репозиторіях, особливо коли відрізняються структура папок, таксономія нотаток або governance-сторінки.
- Для `/.brains` вважати `pytest`, `ruff` і `mypy` стандартним verification-toolbox після Python-змін.
- Не проганяти повний `pytest tests -q` за замовчуванням після кожної дрібної зміни.
- За замовчуванням:
  - запускати `ruff` і `mypy` окремо,
  - запускати лише targeted pytest-файли або конкретні тести, пов'язані зі зміненим кодом,
  - повний pytest-suite запускати лише для широких refactor-ів, cross-cutting changes або за явним запитом.
- Для `/.brains` канонічною командою type-check вважати `uv run mypy brains`.
- Mypy-конфіг у репозиторії має залишатися виконуваним у стандартному локальному середовищі; не підміняти це ad hoc command-line flags у прикладах або звичній перевірці, якщо не змінюється сама конфігурація.
- У цьому репозиторії для `mypy` слід зберігати `follow_imports = "skip"` як default policy, доки окрема зміна не доведе, що повний import traversal і стабільний, і реально корисніший.
- Причина: важкі optional dependency trees на кшталт `docling`, `sentence-transformers`, `transformers` і `torch` можуть робити full import traversal непропорційно повільним або провокувати internal mypy failures у Windows workflow з `/.brains/.venv`.
- Якщо `mypy` виглядає як такий, що завис, спершу перевіряти, чи проблема не в важкому third-party import traversal, а не одразу припускати локальну typing-помилку.
- Для перевикористовуваної mypy-діагностики в `/.brains` пріоритетно використовувати helper script `/.brains/scripts/diagnose_mypy_hang.py`, а не разові shell-експерименти.
- Не прибирати mypy safeguards для import-skipping цих важких third-party пакетів, доки оновлена конфігурація не буде підтверджена реальним успішним запуском `uv run mypy brains` у цьому репозиторії.
- У Ruff-конфігу для `/.brains` тримати `known-first-party = ["brain"]`; не залишати шаблонні placeholders на кшталт `your_package`.
- Для `/.brains` repository-specific operational defaults, які можуть відрізнятися між репозиторіями або структурою vault, слід зберігати в `/.brains/config/brains.toml`, а не як Python hardcode.
- Зокрема:
  - exclusions для governance-сторінок у graph retrieval тримати в `[graph].governance_files`,
  - явні mirror/special page pairs тримати в `[graph].special_page_pairs`,
  - default queries для `check-index` тримати в `[health].pdf_probe_query` і `[health].vault_probe_query`.
- `/.brains`-specific helper scripts не повинні містити власний inline `DEFAULT_CONFIG`, якщо ці значення вже задаються через TOML; такі скрипти мають читати `config/brains.toml` і, за наявності, `config/local.toml`.
- Для `/.brains` helper scripts, які входять у звичайний локальний workflow, слід віддавати пріоритет переносимим Python wrappers замість shell-only wrappers, якщо це практично можливо.
- Для workflow завантаження та реіндексації літературних PDF канонічним helper entrypoint вважати `/.brains/scripts/fetch_literature_pdfs.py`.
- Для `/.brains` canonical environment це Windows virtual environment у `/.brains/.venv`.
- Навіть якщо агент працює з `WSL`, `/.brains/.venv` треба створювати, перестворювати і синхронізувати через Windows `cmd.exe` з `uv`, а не через Linux-layout `venv`.
- Не тримати паралельні canonical environments на кшталт `/.brains/.venvx`; для локальної роботи з `brain` має використовуватися один проєктний env `/.brains/.venv`.
- У `cmd.exe` викликати `uv` напряму через `PATH`; не використовувати absolute path до `uv.exe`.
- Якщо для цього репозиторію з `WSL` потрібен Docker, його теж слід викликати через Windows `cmd.exe`.
- Для цього workflow пріоритетно використовувати `cmd.exe /c "docker ..."` замість прямого виклику Docker із Linux shell.
- Не можна жорстко прошивати локальний шлях репозиторію в командах, документації, скриптах чи прикладах.
- Пріоритетно використовувати переносимі шаблони на кшталт `%CD%`, відносні шляхи від поточного каталогу або явні placeholders типу `<REPO_ROOT>` замість machine-specific absolute paths.

Приклади:

```bash
cmd.exe /c "cd /d %CD%\.brains && uv python install 3.12"
```

```bash
cmd.exe /c "cd /d %CD%\.brains && uv venv .venv --python 3.12"
```

```bash
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv sync --all-groups"
```

```bash
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run python -m brain"
```

```bash
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run pytest tests/test_cli.py -q"
```

```bash
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run ruff check brain tests"
```

```bash
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run mypy brains"
```

```bash
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run pytest tests -q"
```

### 1.5.1 Переносимість шляхів

- Переносимість шляхів для operational examples та automation snippets вважати must-have вимогою.

### 1.6 WSL і Ollama

- Якщо локальна робота з моделями використовує Windows-екземпляр `Ollama` з `WSL`, пріоритетно використовувати mirrored networking на `Windows 11 22H2+`.
- Глобальну конфігурацію WSL тримати в `%UserProfile%\\.wslconfig`:

```ini
[wsl2]
networkingMode=mirrored
dnsTunneling=true
autoProxy=true
firewall=true
```

- Після зміни `.wslconfig` перезапускати `WSL` командою:

```powershell
wsl --shutdown
```

- У mirrored mode перевіряти доступ до Windows-екземпляра `Ollama` з `WSL` через:

```bash
curl http://127.0.0.1:11434/api/tags
```

- Якщо mirrored mode недоступний або вимкнений, запускати Windows `Ollama` зі змінною `OLLAMA_HOST=0.0.0.0:11434` у користувацьких змінних середовища Windows і звертатися до неї з `WSL` через IP Windows-хоста:

```bash
WIN_HOST=$(ip route show | awk '/default/ {print $3}')
curl "http://$WIN_HOST:11434/api/tags"
```

- Ніколи не копіювати секрети, токени, credentials, приватні prompts або персональні дані в `Ollama` prompts, shell history, note-файли чи versioned configuration files.

### 1.7 WSL і LanceDB

- Якщо `/.brains` запускається всередині `WSL`, а сам репозиторій лежить на `/mnt/c/...`, `LanceDB` може падати на стандартному шляху `/.brains/.index/...` з `I/O` або `metadata`-помилками під час створення чи перезапису таблиць.
- Канонічний default при цьому все одно лишається `/.brains/.index/...`.
- Коли стається саме цей збій `WSL + /mnt/c + LanceDB`, використовувати fallback index root у Linux-native файловій системі:

```bash
cd .brains
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run python -m brain index --index-root /tmp/alphafold3-pdf-index"
```

- У fallback-режимі PDF-індекс зберігається тут:
  - `/tmp/alphafold3-pdf-index/manifest.json`
  - `/tmp/alphafold3-pdf-index/lancedb`
- Також треба записувати pointer на активний fallback-шлях у:
  - `/.brains/.index/pdf_search/active_index.json`
- Таку саму pointer-схему треба використовувати і для fallback markdown-індексу vault через:
  - `/.brains/.index/vault_search/active_index.json`
- Треба явно фіксувати, що використовується fallback-шлях, щоб наступні запуски не припускали, ніби активний індекс лежить у `/.brains/.index/pdf_search`.
- У restricted sandbox-середовищах `LanceDB` може також зависати на `connect()` або `open_table()`, навіть коли fallback-індекс у `/tmp/...` валідний.
- Перш ніж вважати індекс пошкодженим, перевіряти його поза sandbox через:

```bash
cd .brains
cmd.exe /c "cd /d %CD%\.brains && set \"UV_PROJECT_ENVIRONMENT=.venv\" && uv run python -m brain check-index --target vault"
```

- `brain check-index` має читати `active_index.json`, якщо він є, і перевіряти саме активний fallback-індекс, а не лише canonical-шлях `/.brains/.index/...`.

---

## 2. Формат нотаток

### 2.1 Frontmatter (обов'язково)

```yaml
---
cssclasses: [note]                 # homepage, index-note, math-note, note
tags: [topic_name, domain_name]    # snake_case
---
```

### 2.2 Breadcrumb

```markdown
# Назва

[[UA/Головна]] > [[UA/Індекс|Концепції]] > Розділ
🇬🇧 [[Home|Home]]
```

### 2.3 Wiki-links

```markdown
✅ [[UA/1. AlphaFold3/1.2. Архітектура/1.2.2. Pairformer|Pairformer]]
✅ [[EN/1. AlphaFold3/1.2. Architecture/1.2.2. Pairformer|Pairformer]]
❌ `Pairformer`
❌ `Архітектура/Pairformer`
```

### 2.4 Wiki-links у таблицях

- Усередині markdown-таблиць: лише `[[path]]` — без alias.
- `[[path|alias]]` ламає парсинг таблиці через символ `|`.

### 2.5 Нові змістові секції (обов'язково)

- Під час додавання нової змістової секції або нової концептуальної нотатки не обмежуватися коротким визначенням.
- За замовчуванням збирати **розширений** матеріал у стилі поглибленого overview, якщо користувач явно не просив коротку версію.
- Мінімальний очікуваний склад нової секції:
  - `чому це можливо / навіщо це потрібно`;
  - основні підходи або варіанти архітектури;
  - ключові властивості;
  - обмеження;
  - приклади споріднених методів, моделей або практичних застосувань.
- Якщо тема технічна, бажано також додавати формули, Mermaid-діаграми, порівняльні таблиці, practical code blocks або короткі case studies там, де це доречно.
- Якщо тема вже має коротку нотатку, при розширенні не залишати її у "згорнутому" вигляді: нова UA/EN-версія має бути достатньо повною в обох мовах.

---

## 3. Візуалізація

- ASCII-діаграми не використовувати, лише Mermaid.
- `\n` у вузлах Mermaid замінюємо на `<br/>`.
- `quadrantChart`: прибирати мітки `quadrant-1..4`, залишати осі + точки.
- Для математичних нотаток: `cssclasses: [math-note]`.

### 3.1 Уніфікація Mermaid (flowchart)

- Для `flowchart` використовувати стандартизовані класи вузлів:
  - `input`
  - `trunk`
  - `diffusion`
  - `confidence`
  - `output`
  - `neutral`
- У кожному `flowchart`-блоці задавати `classDef` для всіх 6 класів із єдиною палітрою.
- Не використовувати локальні/довільні назви класів (`root`, `emb`, `model`, `clean`, `gen` тощо).
- Виняток: `timeline`, `mindmap`, `xychart-beta`, `quadrantChart` можуть бути без `classDef`, якщо це не погіршує читабельність.

### 3.2 Читабельність і компактність діаграм

- Діаграми мають бути візуально компактними й зручними для читання в Obsidian; не оптимізувати їх лише під технічну повноту.
- Для коротких pipeline-діаграм, порівнянь і summary metric/component diagrams зазвичай віддавати перевагу `flowchart LR`, якщо це зменшує висоту.
- `flowchart TD` використовувати тоді, коли процес справді ієрархічний або коли горизонтальна схема стає надто широкою.
- Підписи вузлів мають бути короткими:
  - краще `Query seq`, ніж довгий приклад послідовності,
  - краще `DB search`, ніж повний опис баз,
  - деталі краще винести під діаграму в bullets або таблицю.
- Не починати Mermaid labels із ordered-list-подібних префіксів на кшталт `1.`, `2.`, `7.` або значень типу `76.4% ...`, якщо можна використати звичайний label або форму `Metric: value`.
- Не робити oversized diagrams:
  - якщо вузлів або тексту занадто багато, розбивати на дві менші діаграми,
  - не зводити все в один великий `flowchart`, якщо пара тематично вузьких схем читається краще.
- Для простих metric/component diagrams зазвичай тримати 4-6 вузлів і 1-2 короткі рядки на вузол.
- Якщо діаграма виходить занадто високою, спочатку:
  - скорочувати labels,
  - пробувати `TD` -> `LR`,
  - переносити деталі під діаграму в bullets або таблицю.

---

## 4. Джерела

Для технічних/наукових тверджень обов'язково додавати джерела:

```markdown
> Author et al. (Year). *Title*. Venue.
> DOI: [10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)
```

---

## 5. Obsidian UI Hacks

- HTML може огортати wiki-link: `<span>[[Note]]</span>`.
- HTML усередині `[[...]]` заборонено.
- Для навігації пріоритетно callouts.

---

## 6. Заборони

- Не використовувати відносні шляхи.
- Не змішувати мови в межах мовної папки.
- Не додавати несистемні файли в корінь vault.
- Не комітити секрети, `PII` або інші чутливі локальні дані.
- Дозволені root-файли/папки: `.git/`, `.gitignore`, `.brains/`, `.obsidian/`, `.smart-env/`, `PDF/`, `Home.md`, `README.md`, `AGENTS.md`, `NOTICE.md`, `AUDIT.md`, `EN/`, `UA/`.

## 7. NOTICE-файли

- Вести журнал форматних змін у `UA/NOTICE.md` (UA) та `NOTICE.md` (EN).
- Оновлювати ці файли після кожного масового перейменування, переносу або форматного рефакторингу.
- Якщо виконувалась масова синхронізація EN↔UA, зафіксувати це окремим пунктом у двох NOTICE-файлах.

---

## 8. AUDIT-файл

- `AUDIT.md` створювати/оновлювати лише за явним запитом користувача.
- Стандартний аудит включає:
  - структурну цілісність (наявність ключових сторінок, паритет UA↔EN),
  - перевірку wiki-links,
  - перевірку DOI/джерел,
  - матрицю `Confidence Level` по ключових доменах.
- Після аудиту коротко фіксувати важливі зміни у `UA/NOTICE.md` і `NOTICE.md` (за наявності змін).
- Навіть без запуску аудиту, агент має час від часу ненав'язливо нагадувати про доцільність оновлення `AUDIT.md` (особливо після великих синхронізацій або масових правок).

---

## 9. CSS та масштабування

- Активні сніпети: `homepage`, `math-note`, `diagram-scale`, `content-width`.
- Тема: **GitHub Theme** — має власні `max-width` для `img`, тому сніпети пишуться з явним `!important`.
- `diagram-scale.css` — відповідає за рівне масштабування Mermaid та зображень:
  - Mermaid SVG → `width: 100%` через `.mermaid svg`
  - Зображення → `width: 100%` через `img` (без `:not([class])`) + `.markdown-preview-section img`
  - `img[width]` — виняток: зображення з явно заданою шириною не розтягуються (іконки, badges)
  - `.note` scope додано до всіх ключових правил для сумісності з `cssclasses: [note]`
- `content-width.css` — адаптивна ширина текстового контейнера:
  - текст ширший за default readable width, але не full-width,
  - `clamp(860px, 86vw, 1180px)` для desktop/tablet,
  - окреме вирівнювання для Reading + Editing (CM6).
- Якщо після змін ілюстрації зникли: перевірити Excalidraw plugin → потім CSS.

---

## 10. Python-секції в нотатках (1.2.6)

Нотатка `1.2.6. Featurization` містить розділи 10 і 11 з Python-кодом.

| Розділ | Зміст |
|---|---|
| 10.1 | Встановлення залежностей (`numpy`, `rdkit`, `gemmi`, `biopython`) |
| 10.2 | Токенізація білка → one-hot `(L, 22)` |
| 10.3 | Токенізація ліганду зі SMILES → атоми + bond graph |
| 10.4 | Парсинг A3M + кодування MSA |
| 10.5 | Cβ дистограма шаблону `(L, L, 39)` |
| 10.6 | Відносне позиційне кодування `(L, L, 65)` |
| 10.7 | `build_feature_dict()` — повний словник ознак |
| 11.0 | Таблиця: що можливо лише з FASTA + mmCIF |
| 11.1 | `parse_fasta()` |
| 11.2 | `sequence_from_mmcif()` + крос-перевірка |
| 11.3 | `extract_ligand_features_from_mmcif()` |
| 11.4 | `backbone_unit_vectors()` + `plddt_from_mmcif()` |
| 11.5 | `featurize_from_fasta_and_mmcif()` — повний пайплайн |
| 11.6 | Таблиця відсутніх ознак у no_msa режимі |
| 11.7 | Бази даних + інструменти для повного MSA режиму |

---

## 11. Комунікація агента

- За замовчуванням відповідати українською.
- Російську не використовувати.
- Код, коментарі в коді та ідентифікатори — англійською.
- Якщо англійський технічний термін природніший за український, лишати його англійською.
- Якщо є добрий український аналог, при першій згадці давати парну форму: `English term` (український відповідник) або український відповідник (`English term`).
- Якщо мову програмування не вказано, використовувати Python.
