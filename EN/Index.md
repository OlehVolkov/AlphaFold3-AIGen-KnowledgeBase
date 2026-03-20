---
cssclasses: [index-note]
tags: [index, concepts]
---

# 🧠 2. Concepts

[[Home]] | 🇺🇦 [[UA/Індекс]]

Reference map of core biology, machine learning, and structural bioinformatics concepts used in AlphaFold 3.

## Cross-Domain Navigation

| Area | Entry point | Why it matters |
|---|---|---|
| AlphaFold 3 core | [[EN/1. AlphaFold3/1.2. Architecture/1.2.1. AF3 Architecture Overview]] | Main architecture, training, confidence, and limitations |
| Models | [[EN/3. Models/3.0. Models Overview]] | Compare `AF2`, `AF3`, `RoseTTAFold`, `ESMFold`, `DiffDock`, `OpenFold`, `Boltz-1`, `Chai-1`, `RoseTTAFoldNA` |
| Datasets | [[EN/4. Datasets/4.0. Datasets Overview]] | Understand training data, sequence resources, and evaluation benchmarks |
| Literature | [[EN/Literature and Priorities]] | Current reading list and coverage gaps |
| Technical digest | [[EN/Summary]] | Compact engineering and implementation-oriented recap |

## Biology

| Topic | Core idea | AF3 link |
|---|---|---|
| [[EN/2. Concepts/2.1. Biology/2.1.1. Protein Folding]] | Energy landscape and native state | Coordinate generation |
| [[EN/2. Concepts/2.1. Biology/2.1.2. Protein-Protein Interactions]] | Interface geometry and binding | DockQ / ipTM |
| [[EN/2. Concepts/2.1. Biology/2.1.3. Ligands and Small Molecules]] | Binding pocket and affinity | PoseBusters |
| [[EN/2. Concepts/2.1. Biology/2.1.4. Nucleic Acids]] | DNA/RNA structure and sequence | Protein–nucleic complexes |

## Machine Learning

| Topic | Core idea | AF3 link |
|---|---|---|
| [[EN/2. Concepts/2.2. Machine-Learning/2.2.1. Transformers]] | Attention and contextual token mixing | Pairformer trunk |
| [[EN/2. Concepts/2.2. Machine-Learning/2.2.2. Diffusion Models]] | Denoising from noise to data | Diffusion module |
| [[EN/2. Concepts/2.2. Machine-Learning/2.2.3. Protein Language Models]] | Sequence embeddings | Input representations |
| [[EN/2. Concepts/2.2. Machine-Learning/2.2.4. Geometric Deep Learning]] | Equivariance and geometry | 3D-aware updates |
| [[EN/2. Concepts/2.2. Machine-Learning/2.2.5. ResNet]] | Residual blocks, skip paths, bottlenecks | Residual updates are a general optimization pattern for deep trunks |
| [[EN/2. Concepts/2.2. Machine-Learning/2.2.6. U-Net]] | Encoder-decoder, skip fusion, dense prediction | U-Net is a core template for segmentation and many diffusion denoisers |

## Structural Bioinformatics

| Topic | Core metric | Typical use |
|---|---|---|
| [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.1. RMSD]] | Global coordinate deviation | Pose comparison |
| [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.2. lDDT]] | Local distance consistency | Confidence |
| [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.3. DockQ]] | Interface quality | Complex evaluation |
| [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.4. MSA]] | Evolutionary alignment depth | Sequence signal |

## From Concepts To Practice

| Practical topic | Most relevant concept layer | Main notes |
|---|---|---|
| General multimolecular prediction | Transformers + diffusion + nucleic acids | [[EN/3. Models/3.2. AlphaFold3]], [[EN/2. Concepts/2.2. Machine-Learning/2.2.1. Transformers]], [[EN/2. Concepts/2.2. Machine-Learning/2.2.2. Diffusion Models]] |
| Open `AF2` engineering | Transformers + MSA | [[EN/3. Models/3.6. OpenFold]], [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.4. MSA]] |
| Open `AF3`-like local workflows | Protein LMs + diffusion + complex evaluation | [[EN/3. Models/3.7. Boltz-1]], [[EN/3. Models/3.8. Chai-1]], [[EN/2. Concepts/2.2. Machine-Learning/2.2.3. Protein Language Models]], [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.3. DockQ]] |
| Protein–DNA / protein–RNA complexes | Nucleic acids + interface metrics | [[EN/3. Models/3.9. RoseTTAFoldNA]], [[EN/2. Concepts/2.1. Biology/2.1.4. Nucleic Acids]], [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.2. lDDT]] |
| Structure search after prediction | Structural bioinformatics metrics | [[EN/1. AlphaFold3/1.5. Resources/1.5.7. Foldseek and Structure Search]], [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.1. RMSD]], [[EN/2. Concepts/2.3. Structural-Bioinformatics/2.3.2. lDDT]] |
