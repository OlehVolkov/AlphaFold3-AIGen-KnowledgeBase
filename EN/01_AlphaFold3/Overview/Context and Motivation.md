# Context and Motivation

[[EN/🏠 Home]] > Overview
🇺🇦 [[01_AlphaFold3/Огляд/Контекст і мотивація|Українська]]

---

## The Problem

Before AF3, existing structure prediction methods were **highly specialized**: each tool worked only with a specific type of molecular interaction (protein–protein, protein–DNA, ligand docking, etc.). Building a general model that covers the entire biomolecular space remained an open challenge.

## Background

- **AlphaFold 2 (2021)** — a revolution in protein structure prediction
- Simple input modifications to AF2 enabled surprisingly accurate protein interaction predictions
- AlphaFold-Multimer v.2.3 extended AF2 to multi-chain complexes
- However, no single method could simultaneously handle **proteins + ligands + nucleic acids + ions + modifications**

## Goal of AF3

Build a single deep learning model that:
1. Predicts structures of complexes from **nearly all molecular types in the Protein Data Bank**
2. Outperforms specialized methods in each interaction class
3. Does not require separate models for different task types

## Significance

> Accurate models of biological complexes are critical for understanding cellular functions and for the rational design of therapeutics.

---

## Related Notes
- [[EN/01_AlphaFold3/Architecture/AF3 Architecture Overview]]
- [[EN/01_AlphaFold3/Results/Accuracy Across Complex Types]]

## Tags
`#motivation` `#alphafold2` `#overview`
