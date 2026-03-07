---
cssclasses: [note]
tags: [alphafold3, literature, references, ranking]
---

# Literature and Priorities

[[Home|Home]] > Resources
🇺🇦 [[UA/Література та пріоритети|Українська]]

Prioritized reading list for AF3. Rank `1` means highest importance.

## A. AlphaFold Core

| Rank | Source | Importance | Critical sections |
|---|---|---|---|
| 1 | Abramson et al. (2024), *Accurate structure prediction of biomolecular interactions with AlphaFold 3* | Primary AF3 paper | `[1.2 Architecture]` `[1.3 Results]` `[1.4 Limitations]` |
|   | DOI: [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) |  |  |
| 2 | Jumper et al. (2021), *Highly accurate protein structure prediction with AlphaFold* | AF2 baseline for architectural comparison | `[1.2 Architecture]` `[1.5 Resources]` |
|   | DOI: [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) |  |  |

## B. Generative Models and ML

| Rank | Source | Importance | Critical sections |
|---|---|---|---|
| 3 | Ho et al. (2020), *Denoising Diffusion Probabilistic Models* | Core `DDPM` theory | `[1.2.4 Diffusion Models]` `[2.2.2 Diffusion Models]` |
|   | DOI: [10.48550/arXiv.2006.11239](https://doi.org/10.48550/arXiv.2006.11239) |  |  |
| 4 | Song et al. (2021), *Score-Based Generative Modeling through SDEs* | Continuous-time score formulation | `[1.2.4 Diffusion Models]` `[2.2.2 Diffusion Models]` |
|   | DOI: [10.48550/arXiv.2011.13456](https://doi.org/10.48550/arXiv.2011.13456) |  |  |
| 5 | Vaswani et al. (2017), *Attention Is All You Need* | Transformer foundation | `[1.2.2 Pairformer]` `[2.2.1 Transformers]` |
|   | DOI: [10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762) |  |  |
| 6 | Watson et al. (2023), *De novo design of protein structure and function with RFdiffusion* | Practical diffusion in protein design | `[1.2.4 Diffusion Models]` `[1.5 Resources]` |
|   | DOI: [10.1038/s41586-023-06415-8](https://doi.org/10.1038/s41586-023-06415-8) |  |  |
| 7 | Corso et al. (2022), *DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking* | Diffusion for molecular docking | `[1.3 Results]` `[2.1.3 Ligands]` |
|   | DOI: [10.48550/arXiv.2210.01776](https://doi.org/10.48550/arXiv.2210.01776) |  |  |

## C. Structural Quality Metrics

| Rank | Source | Importance | Critical sections |
|---|---|---|---|
| 8 | Basu & Wallner (2016), *DockQ: A Quality Measure for Protein-Protein Docking Models* | Core interface metric `DockQ` | `[1.3 Results]` `[2.3.3 DockQ]` |
|   | DOI: [10.1371/journal.pone.0161879](https://doi.org/10.1371/journal.pone.0161879) |  |  |
| 9 | Kabsch (1976), *A solution for the best rotation to relate two sets of vectors* | Mathematical basis for `RMSD` superposition | `[2.3.1 RMSD]` `[1.3 Results]` |
|   | DOI: [10.1107/S0567739476001873](https://doi.org/10.1107/S0567739476001873) |  |  |

## D. Biological Foundations

| Rank | Source | Importance | Critical sections |
|---|---|---|---|
| 10 | Anfinsen (1973), *Principles that govern the folding of protein chains* | Foundational folding hypothesis | `[2.1.1 Protein Folding]` |
|   | DOI: [10.1126/science.181.4096.223](https://doi.org/10.1126/science.181.4096.223) |  |  |
| 11 | Dill & MacCallum (2012), *The Protein-Folding Problem, 50 Years On* | Modern folding framework | `[2.1.1 Protein Folding]` |
|   | DOI: [10.1126/science.1219021](https://doi.org/10.1126/science.1219021) |  |  |

## E. Alignment and Evolutionary Signal

| Rank | Source | Importance | Critical sections |
|---|---|---|---|
| 12 | Needleman & Wunsch (1970), *A general method applicable to the search for similarities in the amino acid sequence of two proteins* | Alignment algorithm foundation | `[2.3.4 MSA]` |
|   | DOI: [10.1016/0022-2836(70)90057-4](https://doi.org/10.1016/0022-2836(70)90057-4) |  |  |
| 13 | Altschul et al. (1990), *Basic local alignment search tool* | Practical homology search standard | `[2.3.4 MSA]` `[1.5.3 FASTA]` |
|   | DOI: [10.1016/S0022-2836(05)80360-2](https://doi.org/10.1016/S0022-2836(05)80360-2) |  |  |

## Related Notes

- [[EN/1. AlphaFold3/1.5. Resources/1.5.1. Key Terms|Key Terms]]
- [[EN/1. AlphaFold3/1.5. Resources/1.5.2. Comparison with Predecessors|Comparison with Predecessors]]
- [[EN/Index|Concepts Index]]
