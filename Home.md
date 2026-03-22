---
cssclasses:
  - homepage
tags:
  - homepage
---

# 🧬 AlphaFold 3

Google DeepMind · *Nature* 2024 · [[UA/Головна|🇺🇦 Українська →]]

> [!quote] Source
> Abramson et al., *Nature* Vol 630, 13 June 2024 · [DOI: 10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w)

## 🗂️ Indexes

- [[EN/Index|Concepts Index]]
- [[EN/3. Models/3.0. Models Overview|Models Index]]
- [[EN/4. Datasets/4.0. Datasets Overview|Datasets Index]]
- [[EN/Summary|Technical Summary]]

## 📚 Literature

- [[EN/Literature and Priorities|Prioritized literature list]]

---

## 🏗️ 01 · AlphaFold 3

> [!info] Overview & Architecture
>
> 📌 <span class="link-blue">[[EN/1. AlphaFold3/1.1. Overview/1.1.1. Context and Motivation|Context and Motivation]]</span>
>
> 🏛️ <span class="link-purple">[[EN/1. AlphaFold3/1.2. Architecture/1.2.1. AF3 Architecture Overview|Architecture Overview]]</span>
>
> ⚙️ <span class="link-purple">[[EN/1. AlphaFold3/1.2. Architecture/1.2.2. Pairformer|Pairformer]]</span>
>
> 🌀 <span class="link-purple">[[EN/1. AlphaFold3/1.2. Architecture/1.2.3. Diffusion Module|Diffusion Module]]</span>
>
> 📐 <span class="link-purple">[[EN/1. AlphaFold3/1.2. Architecture/1.2.4. Diffusion Models — Theory and Applications|Diffusion Models — Theory]]</span>
>
> 🎓 <span class="link-purple">[[EN/1. AlphaFold3/1.2. Architecture/1.2.5. Model Training|Model Training]]</span>

> [!success] Results
>
> 📊 <span class="link-green">[[EN/1. AlphaFold3/1.3. Results/1.3.1. Accuracy Across Complex Types|Accuracy Across Complex Types]]</span>
>
> 🎯 <span class="link-green">[[EN/1. AlphaFold3/1.3. Results/1.3.2. Confidence Scores|Confidence Scores]]</span>

> [!warning] Limitations
>
> ⚠️ <span class="link-orange">[[EN/1. AlphaFold3/1.4. Limitations/1.4.1. Model Limitations|Model Limitations]]</span>

> [!abstract] Resources
>
> 🔑 <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.1. Key Terms|Key Terms]]</span>
>
> 🔄 <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.2. Comparison with Predecessors|Comparison with Predecessors]]</span>
>
> 🧬 <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.3. Working with FASTA Files|Working with FASTA Files]]</span>
>
> 🗂️ <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.4. Working with mmCIF Files|Working with mmCIF Files]]</span>
>
> ⚗️ <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.5. Working with SMILES Files|Working with SMILES Files]]</span>
>
> 🧵 <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.6. Working with A3M Files|Working with A3M Files]]</span>
>
> 🔎 <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.7. Foldseek and Structure Search|Foldseek and Structure Search]]</span>
>
> ❓ <span class="link-teal">[[EN/1. AlphaFold3/1.5. Resources/1.5.8. AlphaFold DB FAQ|AlphaFold DB FAQ]]</span>
>
> 🖼️ <span class="link-teal">[[EN/1. AlphaFold3/1.6. Illustrations/1.6.1. Illustration Gallery|Illustration Gallery]]</span>

---

## 🧠 02 · Concepts

> [!tip] 🧬 Biology
>
> <span class="link-blue">[[EN/2. Concepts/2.1. Biology/2.1.1. Protein Folding|Protein Folding]]</span> · <span class="link-blue">[[EN/2. Concepts/2.1. Biology/2.1.2. Protein-Protein Interactions|Protein–Protein Interactions]]</span> · <span class="link-blue">[[EN/2. Concepts/2.1. Biology/2.1.3. Ligands and Small Molecules|Ligands]]</span> · <span class="link-blue">[[EN/2. Concepts/2.1. Biology/2.1.4. Nucleic Acids|Nucleic Acids]]</span>

> [!tip] 🤖 Machine Learning
>
> <span class="link-purple">[[EN/2. Concepts/2.2. Machine-Learning/2.2.1. Transformers|Transformers]]</span> · <span class="link-purple">[[EN/2. Concepts/2.2. Machine-Learning/2.2.2. Diffusion Models|Diffusion Models]]</span> · <span class="link-purple">[[EN/2. Concepts/2.2. Machine-Learning/2.2.3. Protein Language Models|Protein Language Models]]</span> · <span class="link-purple">[[EN/2. Concepts/2.2. Machine-Learning/2.2.4. Geometric Deep Learning|Geometric DL]]</span>

> [!tip] 📐 Structural Bioinformatics
>
> <span class="link-teal">[[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.1. RMSD|RMSD]]</span> · <span class="link-teal">[[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.2. lDDT|lDDT]]</span> · <span class="link-teal">[[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.3. DockQ|DockQ]]</span> · <span class="link-teal">[[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.4. MSA|MSA]]</span>

---

## 🤖 03 · Models

📖 [[EN/3. Models/3.0. Models Overview|Extended models overview →]]

> [!example] Comparative models
>
> [[EN/3. Models/3.1. AlphaFold2|AlphaFold2]] · [[EN/3. Models/3.2. AlphaFold3|AlphaFold3]] · [[EN/3. Models/3.3. RoseTTAFold|RoseTTAFold]] · [[EN/3. Models/3.4. ESMFold|ESMFold]] · [[EN/3. Models/3.5. DiffDock|DiffDock]]

> [!example] Open and specialized extensions
>
> [[EN/3. Models/3.6. OpenFold|OpenFold]] · [[EN/3. Models/3.7. Boltz-1|Boltz-1]] · [[EN/3. Models/3.8. Chai-1|Chai-1]] · [[EN/3. Models/3.9. RoseTTAFoldNA|RoseTTAFoldNA]]

---

## 🗂️ 04 · Datasets

📖 [[EN/4. Datasets/4.0. Datasets Overview|Extended datasets overview →]]

> [!example] Core data sources
>
> [[EN/4. Datasets/4.1. PDB|PDB]] · [[EN/4. Datasets/4.2. UniProt|UniProt]] · [[EN/4. Datasets/4.3. AlphaFoldDB|AlphaFoldDB]] · [[EN/4. Datasets/4.4. CASP|CASP]]

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
  AND file.name != "1.0. Home"
SORT file.folder ASC, file.name ASC
```
