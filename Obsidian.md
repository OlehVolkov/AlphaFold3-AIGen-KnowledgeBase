# Obsidian UI Hacks для Wiki-Links

> Інструкції для AI-агентів щодо генерації Obsidian-сумісних UI-елементів з внутрішніми посиланнями.

---

## Головне правило

**HTML огортає wiki-links — не навпаки.**

| ❌ Неправильно | ✅ Правильно |
|----------------|--------------|
| `[[<div>note</div>]]` | `<div>[[note]]</div>` |
| `[[<button>note</button>]]` | `<div class="btn">[[note]]</div>` |
| `[[<span>note</span>]]` | `<span class="color">[[note]]</span>` |

---

## 1. Кнопки (Button-style Links)

Огорнути wiki-link у HTML-контейнер.

```html
<div class="obsidian-button">
  [[AlphaFold]]
</div>
```

**CSS-сніпет (опціонально):**

```css
.obsidian-button a {
  display: inline-block;
  padding: 6px 12px;
  background: #6c8cff;
  color: white;
  border-radius: 6px;
  text-decoration: none;
}
```

---

## 2. Кольорові посилання

```html
<span class="link-green">[[Protein Folding]]</span>
<span class="link-red">[[Model Limitations]]</span>
```

**CSS-сніпет:**

```css
.link-green a { color: #3cb371; font-weight: 600; }
.link-red   a { color: #ff5c5c; }
```

---

## 3. Callout-картки з посиланнями

Використовувати Obsidian callouts для навігаційних блоків.

**Простий список:**

```markdown
> [!tip] Protein Models
> - [[AlphaFold]]
> - [[ESM-3]]
> - [[Protein Design]]
```

**Картка з відступами:**

```markdown
> [!info] Research Tools
>
> [[AlphaFold]]
>
> [[Protein Language Models]]
>
> [[ESM-3]]
```

---

## 4. Навігаційні панелі

```markdown
> [!abstract] Навігація
>
> [[AlphaFold]]
> [[ESM-3]]
> [[Protein Structure Prediction]]
```

---

## 5. Дозволений синтаксис wiki-links

```markdown
[[note]]            ← пряме посилання
[[note|alias]]      ← з псевдонімом
[[note#heading]]    ← до заголовку
[[note^block]]      ← до блоку
```

> [!danger] Заборонено
> Ніколи не генерувати HTML всередині `[[ ]]`.

---

## 6. Правила безпечного рендерингу

1. HTML **огортає** wiki-links
2. Wiki-links **ніколи** не огортають HTML
3. Markdown — пріоритет над HTML
4. Callouts — для UI-карток і навігації
5. CSS-класи — опціонально, через сніпети

---

## 7. Приклад коректного UI-блоку

```markdown
> [!info] Protein AI Models
>
> <span class="link-green">[[AlphaFold]]</span>
>
> <span class="link-green">[[ESM-3]]</span>
```

> ✅ Гарантує сумісність з Obsidian Markdown renderer.
