# NOTICE — Журнал виправлень форматування

Останнє оновлення: 2026-03-11
Платформа: Obsidian vault
Сумісність Obsidian (мінімум): 1.12.0
Примітка: `app.json` у vault порожній (`{}`), тому точна версія застосунку не зафіксована в репозиторії.

Цей файл фіксує, які саме форматні проблеми вже виправлялися у vault, щоб не повторювати помилки.

## 1. Wiki-links у таблицях

- Проблема: посилання виду `[[path|label]]` ламали markdown-таблиці через символ `|`.
- Рішення: у таблицях використовуємо тільки `[[path]]` (без alias).
- Застосовано до:
  - `UA/Індекс.md`
  - `EN/Index.md`
  - `UA/3. Моделі/3.0. Огляд моделей.md`
  - `EN/3. Models/3.0. Models Overview.md`
  - `UA/4. Датасети/4.0. Огляд датасетів.md`
  - `EN/4. Datasets/4.0. Datasets Overview.md`

## 2. Mermaid форматування

- Проблема: `\n` у підписах вузлів інколи не рендерився коректно.
- Рішення: замінено на `<br/>` у Mermaid-блоках.
- Проблема: `quadrantChart` може падати на рядках `quadrant-1 ...`, `quadrant-2 ...`.
- Рішення: прибрати `quadrant-1..4` підписи, залишити осі + точки.

## 3. Абсолютні посилання

- Правило: використовуємо абсолютні шляхи від кореня vault.
- Виправлено масово після змін структури папок і файлів.

## 4. Головні сторінки та навігація

- Англійська home-сторінка винесена в корінь:
  - `Home.md`
- Українська home-сторінка переміщена в:
  - `UA/Головна.md`
- Міжмовні переходи оновлені:
  - `Home.md` ↔ `UA/Головна.md`

## 5. Індекси і література на верхньому рівні мовних папок

- UA:
  - `UA/Індекс.md`
  - `UA/Література та пріоритети.md`
- EN:
  - `EN/Index.md`
  - `EN/Literature and Priorities.md`

## 6. Перевірка після змін

Після масових перейменувань/переносів завжди:

1. Перевірити всі `[[...]]` посилання на існування цільових `.md`.
2. Окремо перевірити індексні сторінки (`Concepts`, `Models`, `Datasets`).
3. Перезавантажити Obsidian (за потреби), якщо видно кешовані артефакти рендеру.
4. Для `.excalidraw` перевірити налаштування плагіна:
   - `renderImageInMarkdownReadingMode: true`
   - рекомендовано: `mdSVGwidth: 1200`, `mdSVGmaxHeight: 1600`

## 7. Антипатерни (не робити)

- Не використовувати `[[path|label]]` всередині markdown-таблиць.
- Не використовувати відносні посилання.
- Не вставляти HTML усередині `[[...]]`.
- Не робити агресивний CSS-скейлінг для Excalidraw без перевірки Reading view (може зламати рендер).

## 8. Масштабування діаграм та ілюстрацій (оновлено 2026-03-11)

Виявлено три одночасні причини невідповідності масштабів між Mermaid та зображеннями:

**Причина 1 — мертвий `.note` scope.**
Усі нотатки мають `cssclasses: [note]`, але в `diagram-scale.css` не було жодного `.note`-scoped правила. Snippet застосовувався лише через глобальні `.markdown-preview-view` селектори, які GitHub Theme перебивав власними правилами вищої специфічності.
- Рішення: додано `.note .markdown-preview-view` scope до всіх ключових правил.

**Причина 2 — GitHub Theme обмежує `img`.**
Тема має власний `max-width` для `.markdown-preview-section img`, який відрізнявся від ширини Mermaid контейнера.
- Рішення: додано явний `img` selector + `.markdown-preview-section img` з `!important`.

**Причина 3 — `img:not([class])` пропускав зображення з класами.**
GitHub Theme додає власні класи на `<img>` теги — такі зображення взагалі не потрапляли під правила snippet.
- Рішення: `img:not([class])` → `img` (без фільтру по класу).

**Новий виняток:** `img[width]` — зображення з явно заданою шириною (іконки, badges) не розтягуються.
**Нова змінна:** `--content-max-width: 100%` для централізованого контролю.

- Використовуємо `.obsidian/snippets/diagram-scale.css`.
- Ціль: Mermaid SVG та `<img>` рендеряться з однаковою шириною — 100% текстового контейнера.
- Якщо після змін ілюстрації зникли: спершу перевірити Excalidraw plugin settings, потім CSS.

## 9. Підтримка файла

- Цей файл потрібно оновлювати після кожного масового рефакторингу структури або форматування.
- Англійська версія: `EN/NOTICE.md`.

## 10. Obsidian Mermaid render fix (2026-03-11)

Виявлено, що частина діаграм рендерилась гірше в Obsidian, ніж у VS Code/GitHub, через надто агресивні локальні стилі та вузький content mode.

- `.obsidian/app.json`:
  - `readableLineLength: true` → `false` (щоб широкі Mermaid-діаграми не стискались контейнером читабельної ширини).
- `.obsidian/snippets/diagram-scale.css`:
  - прибрано примусовий `font-size: ... !important` для `.mermaid svg` (він ламав авто-лейаут підписів у деяких типах Mermaid),
  - `overflow-x: hidden` → `overflow-x: auto` для `.mermaid` контейнера (щоб уникати обрізання),
  - знято `max-height` обмеження для Excalidraw/internal embed (`svg/img/canvas`), щоб уникнути вертикального "стискання" діаграм.

## 11. Масова синхронізація EN↔UA (2026-03-11)

Виконано вирівнювання неповних EN-нотаток до рівня UA-дзеркал (структура розділів, таблиці, формули, практичні приклади).

- Оновлено EN Concepts (розділи `2.1`, `2.2`, `2.3` для основних тем):
  - `2.1.1 Protein Folding`
  - `2.1.2 Protein-Protein Interactions`
  - `2.1.3 Ligands and Small Molecules`
  - `2.1.4 Nucleic Acids`
  - `2.2.1 Transformers`
  - `2.2.2 Diffusion Models`
  - `2.2.3 Protein Language Models`
  - `2.2.4 Geometric Deep Learning`
  - `2.3.1 RMSD`
  - `2.3.2 lDDT`
  - `2.3.3 DockQ`
- Суттєво розширено:
  - `EN/1. AlphaFold3/1.5. Resources/1.5.4. Working with mmCIF Files.md`
    (metadata extraction, NumPy coordinates, interface analysis, AF3 output parsing, PDB download, write/modify workflow).
- Перевірено wiki-links у змінених EN-файлах: битих посилань не виявлено.

## 12. Уніфікація Mermaid-стилів (2026-03-11)

Узгоджено єдиний стиль Mermaid-діаграм у нових/оновлених EN та UA нотатках (Concepts + mmCIF resource):

- Стандартизовані класи вузлів:
  - `input`
  - `trunk`
  - `diffusion`
  - `confidence`
  - `output`
  - `neutral`
- Для flowchart-блоків додано єдині `classDef` з палітрою з `AGENTS.md`.
- Замінено локальні/старі назви класів (`root`, `sm`, `emb`, `clean`, `gen`, `model`, тощо) на уніфіковані.
- Мета: передбачуваний вигляд діаграм у Obsidian Reading view та однакова семантика кольорів між EN/UA.

## 13. Оновлення AGENTS/NOTICE (2026-03-11)

- `AGENTS.md` та `EN/AGENTS.md` синхронізовано з актуальними правилами Mermaid.
- Додано обов'язковий стандарт для `flowchart`: `input`, `trunk`, `diffusion`, `confidence`, `output`, `neutral`.
- Додано явну вимогу: у кожному `flowchart` задавати `classDef` для всіх 6 класів.
- Зафіксовано винятки для non-flowchart типів (`timeline`, `mindmap`, `xychart-beta`, `quadrantChart`).
