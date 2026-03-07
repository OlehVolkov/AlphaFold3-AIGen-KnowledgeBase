# Comparison with Predecessors

[[EN/🏠 Home]] > Resources
🇺🇦 [[01_AlphaFold3/Ресурси/Порівняння з попередниками|Українська]]

---

## AlphaFold Evolution

```
AlphaFold (AF1, 2018)
    ↓ revolution in protein structure prediction
AlphaFold 2 (AF2, 2021) — Nature, Jumper et al.
    ↓ + complexes
AlphaFold-Multimer v2.3 (AF-M 2.3)
    ↓ + all molecule types + diffusion
AlphaFold 3 (AF3, 2024) ← we are here
```

## Architecture Comparison

| Aspect | AF2 | AF3 |
|---|---|---|
| Core block | Evoformer | Pairformer |
| Structure module | Frame-based (torsions) | Diffusion (coordinates) |
| Molecule types | Proteins (+ complexes) | All PDB types |
| MSA processing | Deep | Simplified |
| Generative | No | Yes |

## Competing Methods (at time of publication)

| Method | Strengths | Weaknesses |
|---|---|---|
| **AutoDock Vina** | Classical ligand docking | Requires protein structure; far worse than AF3 |
| **RoseTTAFold All-Atom** | General biomolecules | Lower accuracy than AF3 in most categories |
| **RoseTTAFold2NA (RF2NA)** | Protein–nucleic acids | Only <1000 residues; worse than AF3 |
| **AIchemy_RNA2** | RNA (with human input) | Requires expert; not automated |
| **AF-Multimer v2.3** | Protein complexes | Proteins only; worse than AF3 for protein–protein |

## Where AF3 Did Not Win

- **AIchemy_RNA2** (with human expert input) on CASP15 RNA targets — AF3 is behind the best human-assisted submission

---

## Related Notes
- [[EN/01_AlphaFold3/Overview/Context and Motivation]]
- [[EN/01_AlphaFold3/Results/Accuracy Across Complex Types]]

## Tags
`#comparison` `#alphafold2` `#rosettafold` `#autodock` `#evolution`
