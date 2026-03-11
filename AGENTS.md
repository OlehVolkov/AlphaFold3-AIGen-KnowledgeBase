# AGENTS.md — Універсальні інструкції для AI-агентів

> Правила побудови й підтримки двомовної STEM-бази знань в Obsidian.

---

## 1. Структура vault

```text
AlphaFold3/
├── .git/
├── .gitignore
├── .obsidian/
├── .smart-env/
├── Home.md
├── AGENTS.md
├── NOTICE.md
├── README.md
├── Summary.md
├── UA/
│   ├── Головна.md
│   ├── Індекс.md
│   ├── Література та пріоритети.md
│   ├── 1. AlphaFold3/
│   │   ├── 1.1. Огляд/
│   │   │   └── 1.1.1. Контекст і мотивація.md
│   │   ├── 1.2. Архітектура/
│   │   │   ├── 1.2.1. Загальна архітектура AF3.md
│   │   │   ├── 1.2.2. Pairformer.md
│   │   │   ├── 1.2.3. Дифузійний модуль.md
│   │   │   ├── 1.2.4. Дифузійні моделі — теорія та застосування.md
│   │   │   ├── 1.2.5. Навчання моделі.md
│   │   │   └── 1.2.6. Феатуризація.md
│   │   ├── 1.3. Результати/
│   │   │   ├── 1.3.1. Точність по типах комплексів.md
│   │   │   └── 1.3.2. Ступінь впевненості.md
│   │   ├── 1.4. Обмеження/
│   │   │   └── 1.4.1. Обмеження моделі.md
│   │   ├── 1.5. Ресурси/
│   │   │   ├── 1.5.1. Ключові терміни.md
│   │   │   ├── 1.5.2. Порівняння з попередниками.md
│   │   │   ├── 1.5.3. Робота з FASTA файлами.md
│   │   │   └── 1.5.4. Робота з mmCIF файлами.md
│   │   └── 1.6. Ілюстрації/
│   │       ├── 1.6.1. Галерея ілюстрацій.md
│   │       ├── af3-diffusion-pipeline.excalidraw
│   │       ├── diffusion-bio-landscape.excalidraw
│   │       └── diffusion-forward-reverse.excalidraw
│   ├── 2. Концепції/
│   │   ├── 2.1. Біологія/
│   │   │   ├── 2.1.1. Згортання білків.md
│   │   │   ├── 2.1.2. Білок-білок взаємодії.md
│   │   │   ├── 2.1.3. Ліганди та малі молекули.md
│   │   │   └── 2.1.4. Нуклеїнові кислоти.md
│   │   ├── 2.2. Машинне-Навчання/
│   │   │   ├── 2.2.1. Трансформери.md
│   │   │   ├── 2.2.2. Дифузійні моделі.md
│   │   │   ├── 2.2.3. Білкові мовні моделі.md
│   │   │   └── 2.2.4. Геометричне глибоке навчання.md
│   │   └── 2.3. Структурна-Біоінформатика/
│   │       ├── 2.3.1. RMSD.md
│   │       ├── 2.3.2. lDDT.md
│   │       ├── 2.3.3. DockQ.md
│   │       └── 2.3.4. MSA.md
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
└── EN/
    ├── AGENTS.md
    ├── NOTICE.md
    ├── Index.md
    ├── Literature and Priorities.md
    ├── 1. AlphaFold3/
    │   ├── 1.1. Overview/
    │   │   └── 1.1.1. Context and Motivation.md
    │   ├── 1.2. Architecture/
    │   │   ├── 1.2.1. AF3 Architecture Overview.md
    │   │   ├── 1.2.2. Pairformer.md
    │   │   ├── 1.2.3. Diffusion Module.md
    │   │   ├── 1.2.4. Diffusion Models — Theory and Applications.md
    │   │   ├── 1.2.5. Model Training.md
    │   │   └── 1.2.6. Featurization.md
    │   ├── 1.3. Results/
    │   │   ├── 1.3.1. Accuracy Across Complex Types.md
    │   │   └── 1.3.2. Confidence Scores.md
    │   ├── 1.4. Limitations/
    │   │   └── 1.4.1. Model Limitations.md
    │   ├── 1.5. Resources/
    │   │   ├── 1.5.1. Key Terms.md
    │   │   ├── 1.5.2. Comparison with Predecessors.md
    │   │   ├── 1.5.3. Working with FASTA Files.md
    │   │   └── 1.5.4. Working with mmCIF Files.md
    │   └── 1.6. Illustrations/
    │       ├── 1.6.1. Illustration Gallery.md
    │       ├── af3-diffusion-pipeline.excalidraw
    │       ├── diffusion-bio-landscape.excalidraw
    │       └── diffusion-forward-reverse.excalidraw
    ├── 2. Concepts/
    │   ├── 2.1. Biology/
    │   │   ├── 2.1.1. Protein Folding.md
    │   │   ├── 2.1.2. Protein-Protein Interactions.md
    │   │   ├── 2.1.3. Ligands and Small Molecules.md
    │   │   └── 2.1.4. Nucleic Acids.md
    │   ├── 2.2. Machine-Learning/
    │   │   ├── 2.2.1. Transformers.md
    │   │   ├── 2.2.2. Diffusion Models.md
    │   │   ├── 2.2.3. Protein Language Models.md
    │   │   └── 2.2.4. Geometric Deep Learning.md
    │   └── 2.3. Structural-Bioinformatics/
    │       ├── 2.3.1. RMSD.md
    │       ├── 2.3.2. lDDT.md
    │       ├── 2.3.3. DockQ.md
    │       └── 2.3.4. MSA.md
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


### 1.1 Правила

- `UA/` — лише українська, `EN/` — лише англійська.
- Ієрархічна нумерація: `1.`, `1.1.`, `1.1.1.` і далі.
- Посилання лише абсолютні від кореня vault.
- Суттєві UA-нотатки мають EN-дзеркало.
- `Home.md` — головна точка входу; root-файли `Summary*.md` дозволені як технічні дайджести/implementation-нотатки.

### 1.2 Синхронізація EN ↔ UA (обов'язково)

- Будь-яка зміна змісту в `UA/` або `EN/` має дзеркально оновлювати відповідник в іншій мові в межах цього ж PR/коміту.
- Під "синхронізацією" мається на увазі не тільки наявність файлу, а й паритет по:
  - ключових розділах `##`,
  - формулах, таблицях, Mermaid-діаграмах,
  - практичних блоках коду,
  - секції `## Пов'язані нотатки / ## Related Notes`.
- Допускається різниця лише в мовній локалізації та стилі формулювань; технічний зміст має бути еквівалентним.
- Перед завершенням змін агент повинен перевірити, що обидві версії (UA/EN) не мають "скороченого" варіанту однієї теми.

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
- Дозволені root-файли/папки: `.git/`, `.gitignore`, `.obsidian/`, `.smart-env/`, `Home.md`, `Summary*.md`, `README.md`, `AGENTS.md`, `NOTICE.md`, `UA/`, `EN/`.


## 7. NOTICE-файли

- Вести журнал форматних змін у `NOTICE.md` (UA) та `EN/NOTICE.md` (EN).
- Оновлювати ці файли після кожного масового перейменування, переносу або форматного рефакторингу.
- Якщо виконувалась масова синхронізація EN↔UA, зафіксувати це окремим пунктом у двох NOTICE-файлах.

---

## 8. CSS та масштабування

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

## 9. Python-секції в нотатках (1.2.6)

Нотатка `1.2.6. Феатуризація` / `1.2.6. Featurization` містить розділи 10 і 11 з Python-кодом.

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

## 10. Комунікація агента

- За замовчуванням відповідати українською.
- Російську не використовувати.
- Код, коментарі в коді та ідентифікатори — англійською.
- Технічні терміни: `English term` — український відповідник.
- Якщо мову програмування не вказано, використовувати Python.
