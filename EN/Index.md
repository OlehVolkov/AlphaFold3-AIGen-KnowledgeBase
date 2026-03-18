---
cssclasses: [index-note]
tags: [index, concepts]
---

# 🧠 2. Concepts

[[Home]] | 🇺🇦 [[UA/Індекс]]

Reference map of core biology, machine learning, and structural bioinformatics concepts used in AlphaFold 3.

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
