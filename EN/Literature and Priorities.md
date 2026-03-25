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
| --- | --- | --- | --- |
| 1 | Abramson et al. (2024), *Accurate structure prediction of biomolecular interactions with AlphaFold 3* | Primary AF3 paper | `[1.2 Architecture]` `[1.3 Results]` `[1.4 Limitations]` |
| | DOI: [10.1038/s41586-024-07487-w](https://doi.org/10.1038/s41586-024-07487-w) | | |
| 2 | Jumper et al. (2021), *Highly accurate protein structure prediction with AlphaFold* | AF2 baseline for architectural comparison | `[1.2 Architecture]` `[1.5 Resources]` |
| | DOI: [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2) | | |

## B. Generative Models and ML

| Rank | Source | Importance | Critical sections |
| --- | --- | --- | --- |
| 3 | Ho et al. (2020), *Denoising Diffusion Probabilistic Models* | Core `DDPM` theory | `[1.2.4 Diffusion Models]` `[2.2.2 Diffusion Models]` |
| | DOI: [10.48550/arXiv.2006.11239](https://doi.org/10.48550/arXiv.2006.11239) | | |
| 4 | Song et al. (2021), *Score-Based Generative Modeling through SDEs* | Continuous-time score formulation | `[1.2.4 Diffusion Models]` `[2.2.2 Diffusion Models]` |
| | DOI: [10.48550/arXiv.2011.13456](https://doi.org/10.48550/arXiv.2011.13456) | | |
| 5 | Vaswani et al. (2017), *Attention Is All You Need* | Transformer foundation | `[1.2.2 Pairformer]` `[2.2.1 Transformers]` |
| | DOI: [10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762) | | |
| 6 | Watson et al. (2023), *De novo design of protein structure and function with RFdiffusion* | Practical diffusion in protein design | `[1.2.4 Diffusion Models]` `[1.5 Resources]` |
| | DOI: [10.1038/s41586-023-06415-8](https://doi.org/10.1038/s41586-023-06415-8) | | |
| 7 | Corso et al. (2022), *DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking* | Diffusion for molecular docking | `[1.3 Results]` `[2.1.3 Ligands]` |
| | DOI: [10.48550/arXiv.2210.01776](https://doi.org/10.48550/arXiv.2210.01776) | | |

## C. Structural Quality Metrics

| Rank | Source | Importance | Critical sections |
| --- | --- | --- | --- |
| 8 | Basu & Wallner (2016), *DockQ: A Quality Measure for Protein-Protein Docking Models* | Core interface metric `DockQ` | `[1.3 Results]` `[2.3.3 DockQ]` |
| | DOI: [10.1371/journal.pone.0161879](https://doi.org/10.1371/journal.pone.0161879) | | |
| 9 | Kabsch (1976), *A solution for the best rotation to relate two sets of vectors* | Mathematical basis for `RMSD` superposition | `[2.3.1 RMSD]` `[1.3 Results]` |
| | DOI: [10.1107/S0567739476001873](https://doi.org/10.1107/S0567739476001873) | | |

## D. Biological Foundations

| Rank | Source | Importance | Critical sections |
| --- | --- | --- | --- |
| 10 | Anfinsen (1973), *Principles that govern the folding of protein chains* | Foundational folding hypothesis | `[2.1.1 Protein Folding]` |
| | DOI: [10.1126/science.181.4096.223](https://doi.org/10.1126/science.181.4096.223) | | |
| 11 | Dill & MacCallum (2012), *The Protein-Folding Problem, 50 Years On* | Modern folding framework | `[2.1.1 Protein Folding]` |
| | DOI: [10.1126/science.1219021](https://doi.org/10.1126/science.1219021) | | |

## E. Alignment and Evolutionary Signal

| Rank | Source | Importance | Critical sections |
| --- | --- | --- | --- |
| 12 | Needleman & Wunsch (1970), *A general method applicable to the search for similarities in the amino acid sequence of two proteins* | Alignment algorithm foundation | `[2.3.4 MSA]` |
| | DOI: [10.1016/0022-2836(70)90057-4](https://doi.org/10.1016/0022-2836(70)90057-4) | | |
| 13 | Altschul et al. (1990), *Basic local alignment search tool* | Practical homology search standard | `[2.3.4 MSA]` `[1.5.3 FASTA]` |
| | DOI: [10.1016/S0022-2836(05)80360-2](https://doi.org/10.1016/S0022-2836(05)80360-2) | | |

## F. Additional Highly Cited Papers (recommended for core reading)

| Rank | Source | Importance | Critical sections |
| --- | --- | --- | --- |
| 14 | Tunyasuvunakool et al. (2021), *Highly accurate protein structure prediction for the human proteome* | AF2 scaling at proteome level | `[1.5 Resources]` `[4.3 AlphaFoldDB]` |
| | DOI: [10.1038/s41586-021-03828-1](https://doi.org/10.1038/s41586-021-03828-1) | | |
| 15 | Evans et al. (2021), *Protein complex prediction with AlphaFold-Multimer* | Key transition from monomer to complex prediction | `[1.3 Results]` `[2.1.2 Protein-Protein Interactions]` |
| | DOI: [10.1101/2021.10.04.463034](https://doi.org/10.1101/2021.10.04.463034) | | |
| 16 | Mariani et al. (2013), *lDDT: a local superposition-free score for comparing protein structures and models* | Foundational `lDDT/pLDDT` reference | `[2.3.2 lDDT]` `[1.3 Results]` |
| | DOI: [10.1093/bioinformatics/btt473](https://doi.org/10.1093/bioinformatics/btt473) | | |
| 17 | Zhang & Skolnick (2004), *Scoring function for automated assessment of protein structure template quality* | Canonical source for `TM-score` | `[2.3.1 RMSD]` `[1.3 Results]` |
| | DOI: [10.1002/prot.20264](https://doi.org/10.1002/prot.20264) | | |
| 18 | Steinegger & Söding (2017), *MMseqs2 enables sensitive protein sequence searching for the analysis of massive data sets* | High-throughput standard for large-scale sequence search | `[2.3.4 MSA]` `[1.5.3 FASTA]` |
| | DOI: [10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) | | |
| 19 | Mirdita et al. (2022), *ColabFold: making protein folding accessible to all* | Practical engineering standard for AF2/AF-Multimer workflows | `[1.5 Resources]` `[2.3.4 MSA]` |
| | DOI: [10.1038/s41592-022-01488-1](https://doi.org/10.1038/s41592-022-01488-1) | | |
| 20 | Baek et al. (2021), *Accurate prediction of protein structures and interactions using a three-track neural network* | Competitive `RoseTTAFold` architecture for benchmarking | `[3.3 RoseTTAFold]` `[1.5.2 Comparison]` |
| | DOI: [10.1126/science.abj8754](https://doi.org/10.1126/science.abj8754) | | |
| 21 | Lin et al. (2023), *Evolutionary-scale prediction of atomic-level protein structure with a language model* | Landmark `ESMFold` / pLM paradigm reference | `[3.4 ESMFold]` `[2.2.3 Protein Language Models]` |
| | DOI: [10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574) | | |

## G. Open Ecosystem and Coverage Gaps (recommended next)

| Rank | Source | Importance | Critical sections |
| --- | --- | --- | --- |
| 22 | Ahdritz et al. (2024), *OpenFold: retraining AlphaFold2 yields new insights into its learning mechanisms and capacity for generalization* | Best open training reference for `AF2`-class systems | `[3.6 OpenFold]` `[EN/Summary]` |
| | DOI: [10.1038/s41592-024-02272-z](https://doi.org/10.1038/s41592-024-02272-z) | | |
| 23 | Wohlwend et al. (2024), *Boltz-1: Democratizing Biomolecular Interaction Modeling* | Open `AF3`-adjacent biomolecular interaction model | `[3.7 Boltz-1]` `[1.5.2 Comparison]` |
| | DOI: [10.1101/2024.11.19.624167](https://doi.org/10.1101/2024.11.19.624167) | | |
| 24 | Chai Discovery (2024), *Chai-1: Decoding the molecular interactions of life* | Practical open multi-modal complex modeling stack | `[3.8 Chai-1]` `[1.5.2 Comparison]` |
| | DOI: [10.1101/2024.10.10.615955](https://doi.org/10.1101/2024.10.10.615955) | | |
| 25 | Baek et al. (2024), *Accurate prediction of protein–nucleic acid complexes using RoseTTAFoldNA* | Best direct coverage gap for `protein–DNA/RNA` complexes | `[3.9 RoseTTAFoldNA]` `[2.1.4 Nucleic Acids]` |
| | DOI: [10.1038/s41592-023-02086-5](https://doi.org/10.1038/s41592-023-02086-5) | | |
| 26 | van Kempen et al. (2024), *Fast and accurate protein structure search with Foldseek* | Key practical tool for searching predicted and experimental structures | `[1.5.7 Foldseek and Structure Search]` `[4.1 PDB]` |
| | DOI: [10.1038/s41587-023-01773-0](https://doi.org/10.1038/s41587-023-01773-0) | | |
| 27 | Cheng et al. (2023), *Accurate proteome-wide missense variant effect prediction with AlphaMissense* | Strong downstream use-case bridging structure and variant interpretation | `[3.2 AlphaFold3]` `[1.5.2 Comparison]` |
| | DOI: [10.1126/science.adg7492](https://doi.org/10.1126/science.adg7492) | | |
| 28 | Shen et al. (2024), *Accurate RNA 3D structure prediction using a language model-based deep learning approach* | Strong RNA-focused complement to AF3 and RoseTTAFoldNA | `[2.1.4 Nucleic Acids]` `[1.5.2 Comparison]` |
| | DOI: [10.1038/s41592-024-02487-0](https://doi.org/10.1038/s41592-024-02487-0) | | |

## H. Official Repositories and Portals

| Resource | Why it matters |
| --- | --- |
| [OpenFold GitHub](https://github.com/aqlaboratory/openfold) | Trainable PyTorch reproduction of `AlphaFold2`; useful for engineering and retraining |
| [Boltz GitHub](https://github.com/jwohlwend/boltz) | Official open repository for `Boltz` biomolecular interaction models |
| [Chai-1 GitHub](https://github.com/chaidiscovery/chai-lab) | Official open implementation and technical report for `Chai-1` |
| [Foldseek GitHub](https://github.com/steineggerlab/foldseek) | Practical CLI for large-scale structure search, clustering, and multimer search |
| [AlphaFold / AlphaFold Server](https://deepmind.google/science/alphafold/) | Official DeepMind landing page for `AFDB`, `AlphaFold 3`, and `AlphaFold Server` |
| [RCSB Computed Structure Models](https://www.rcsb.org/docs/general-help/computed-structure-models-and-rcsborg) | Official access point for computed models integrated alongside experimental PDB structures |
| [PDBx/mmCIF Dictionary Resources](https://mmcif.wwpdb.org/) | Official format and dictionary reference for structural data interchange |

## Related Notes

- [[EN/1. AlphaFold3/1.5. Resources/1.5.1. Key Terms|Key Terms]]
- [[EN/1. AlphaFold3/1.5. Resources/1.5.2. Comparison with Predecessors|Comparison with Predecessors]]
- [[EN/1. AlphaFold3/1.5. Resources/1.5.7. Foldseek and Structure Search|Foldseek and Structure Search]]
- [[EN/3. Models/3.6. OpenFold|OpenFold]]
- [[EN/3. Models/3.7. Boltz-1|Boltz-1]]
- [[EN/3. Models/3.8. Chai-1|Chai-1]]
- [[EN/3. Models/3.9. RoseTTAFoldNA|RoseTTAFoldNA]]
- [[EN/Index|Concepts Index]]
