---
cssclasses:
  - homepage
tags:
  - homepage
---

# 🧬 AlphaFold 3

<div class="home-meta">
Google DeepMind · <em>Nature</em> 2024 · <span class="link-ua">[[🏠 Головна|🇺🇦 Українська →]]</span>
</div>

> [!quote] Source
> Abramson et al., *Nature* Vol 630, 13 June 2024 · [DOI: 10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w)

---

## 🏗️ 01 · AlphaFold 3

> [!info] Overview & Architecture
>
> 📌 <span class="link-blue">[[EN/01_AlphaFold3/Overview/Context and Motivation|Context and Motivation]]</span>
>
> 🏛️ <span class="link-purple">[[EN/01_AlphaFold3/Architecture/AF3 Architecture Overview|Architecture Overview]]</span>
>
> ⚙️ <span class="link-purple">[[EN/01_AlphaFold3/Architecture/Pairformer|Pairformer]]</span>
>
> 🌀 <span class="link-purple">[[EN/01_AlphaFold3/Architecture/Diffusion Module|Diffusion Module]]</span>
>
> 📐 <span class="link-purple">[[EN/01_AlphaFold3/Architecture/Diffusion Models — Theory and Applications|Diffusion Models — Theory]]</span>
>
> 🎓 <span class="link-purple">[[EN/01_AlphaFold3/Architecture/Model Training|Model Training]]</span>

> [!success] Results
>
> 📊 <span class="link-green">[[EN/01_AlphaFold3/Results/Accuracy Across Complex Types|Accuracy Across Complex Types]]</span>
>
> 🎯 <span class="link-green">[[EN/01_AlphaFold3/Results/Confidence Scores|Confidence Scores]]</span>

> [!warning] Limitations
>
> ⚠️ <span class="link-orange">[[EN/01_AlphaFold3/Limitations/Model Limitations|Model Limitations]]</span>

> [!abstract] Resources
>
> 🔑 <span class="link-teal">[[EN/01_AlphaFold3/Resources/Key Terms|Key Terms]]</span>
>
> 🔄 <span class="link-teal">[[EN/01_AlphaFold3/Resources/Comparison with Predecessors|Comparison with Predecessors]]</span>
>
> 🧬 <span class="link-teal">[[EN/01_AlphaFold3/Resources/Working with FASTA Files|Working with FASTA Files]]</span>
>
> 🗂️ <span class="link-teal">[[EN/01_AlphaFold3/Resources/Working with mmCIF Files|Working with mmCIF Files]]</span>

---

## 🧠 02 · Concepts

<div class="home-index-btn">[[UA/02_Концепції/Індекс|📖 Full Concepts Index →]]</div>

> [!tip] 🧬 Biology
>
> <span class="link-blue">[[UA/02_Концепції/Біологія/Згортання білків|Protein Folding]]</span> · <span class="link-blue">[[UA/02_Концепції/Біологія/Білок-білок взаємодії|Protein–Protein Interactions]]</span> · <span class="link-blue">[[UA/02_Концепції/Біологія/Ліганди та малі молекули|Ligands]]</span> · <span class="link-blue">[[UA/02_Концепції/Біологія/Нуклеїнові кислоти|Nucleic Acids]]</span>

> [!tip] 🤖 Machine Learning
>
> <span class="link-purple">[[UA/02_Концепції/Машинне-Навчання/Трансформери|Transformers]]</span> · <span class="link-purple">[[UA/02_Концепції/Машинне-Навчання/Дифузійні моделі|Diffusion Models]]</span> · <span class="link-purple">[[UA/02_Концепції/Машинне-Навчання/Білкові мовні моделі|Protein Language Models]]</span> · <span class="link-purple">[[UA/02_Концепції/Машинне-Навчання/Геометричне глибоке навчання|Geometric DL]]</span>

> [!tip] 📐 Structural Bioinformatics
>
> <span class="link-teal">[[UA/02_Концепції/Структурна-Біоінформатика/RMSD|RMSD]]</span> · <span class="link-teal">[[UA/02_Концепції/Структурна-Біоінформатика/lDDT|lDDT]]</span> · <span class="link-teal">[[UA/02_Концепції/Структурна-Біоінформатика/DockQ|DockQ]]</span> · <span class="link-teal">[[UA/02_Концепції/Структурна-Біоінформатика/MSA|MSA]]</span>

---

## 📈 Key Numbers

| Complex type | Metric | AF3 | Competitor |
|---|---|---|---|
| Protein–ligand | PoseBusters | **76.4%** | Vina 52% |
| Protein–RNA | iLDDT | **39.4** | RF2NA 19.0 |
| Protein–dsDNA | iLDDT | **64.8** | RF2NA 28.3 |
| Antibody–antigen | DockQ > 0.23 | **62.9%** | AF-M 29.6% |
| Protein–protein | DockQ > 0.23 | **76.6%** | AF-M 67.5% |

---

## 🗺️ All Notes

```dataview
TABLE WITHOUT ID
  file.link AS Note,
  file.folder AS Folder,
  length(file.inlinks) AS "← In",
  length(file.outlinks) AS "→ Out"
FROM "EN"
WHERE !contains(file.path, ".obsidian")
  AND file.name != "Home"
SORT file.folder ASC, file.name ASC
```
