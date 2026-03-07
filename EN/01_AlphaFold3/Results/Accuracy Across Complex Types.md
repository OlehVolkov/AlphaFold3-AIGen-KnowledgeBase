# Accuracy Across Complex Types

[[EN/🏠 Home]] > Results
🇺🇦 [[01_AlphaFold3/Результати/Точність по типах комплексів|Українська]]

---

## Protein–Ligand (PoseBusters)

**Metric:** % structures with pocket-aligned RMSD < 2 Å  
**Dataset:** 428 structures (PoseBusters V1, August 2023)

| Method | Result |
|---|---|
| **AF3 (2019 cutoff)** | **76.4%** |
| RoseTTAFold All-Atom | 42.0% |
| AutoDock Vina | ~52% |

- p = 2.27×10⁻¹³ (AF3 vs Vina)
- AF3 does not use pocket information (true blind docking)
- Chirality violation rate: ~4.4% (known issue)

## Protein–Nucleic Acids

**Metric:** Interface LDDT (iLDDT)

| Type | AF3 | RoseTTAFold2NA |
|---|---|---|
| Protein–RNA | **39.4** | 19.0 |
| Protein–dsDNA | **64.8** | 28.3 |

Evaluated on structures < 1000 residues (RF2NA limitation).

## RNA (CASP15)

AF3 outperforms RoseTTAFold2NA and AIchemy_RNA (best AI method at CASP15), but **does not reach** the level of AIchemy_RNA2 (which uses human expert input).

## Covalent Modifications

**Metric:** % predictions with pocket RMSD < 2 Å

| Type | AF3 |
|---|---|
| Bonded ligands | 78.5% |
| Glycosylation (high quality) | 72.1% |
| Modified residues | 59.9% |
| Modified DNA | 68.6% |

## Protein–Protein

**Metric:** % DockQ > 0.23

| Type | AF3 | AF-Multimer 2.3 |
|---|---|---|
| All protein–protein | **76.6%** | 67.5% |
| Antibody–antigen | **62.9%** | 29.6% |
| Monomers (LDDT) | **86.9** | 85.5 |

### Antibodies — special case
Antibody prediction quality **keeps improving** with more model seeds — even up to 1000! (p = 2×10⁻⁵). This is not observed for other molecule types.

---

## Related Notes
- [[EN/01_AlphaFold3/Results/Confidence Scores]]
- [[EN/01_AlphaFold3/Resources/Comparison with Predecessors]]

## Tags
`#results` `#benchmark` `#posebusters` `#casp15` `#accuracy`
