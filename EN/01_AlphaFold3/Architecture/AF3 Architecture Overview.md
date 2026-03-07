# AF3 Architecture Overview

[[EN/🏠 Home]] > Architecture
🇺🇦 [[01_AlphaFold3/Архітектура/Загальна архітектура AF3|Українська]]

---

## High-Level Schema

AF3 inherits the general structure of AF2 but with major changes in every component:

```
Input (sequences, ligands, covalent bonds)
  ↓
Input Embedder (3 blocks)
  ↓ ← Template Module (2 blocks)
  ↓ ← MSA Module (4 blocks)  ← reduced vs AF2
  ↓
Pairformer (48 blocks)  ← replaces Evoformer
  ↓
Diffusion Module (3 + 24 + 3 blocks)  ← replaces Structure Module
  ↓
Confidence Module (4 blocks)
  ↓
Output: 3D atom coordinates
```

## Key Differences from AF2

| Component | AF2 | AF3 |
|---|---|---|
| Main processing block | Evoformer | **Pairformer** |
| Structure generation | Structure Module (torsion angles) | **Diffusion Module** (raw coordinates) |
| MSA processing | Central role | Greatly simplified (4 blocks) |
| Chemical generality | Proteins / complexes only | All molecular types |
| Residue parametrization | Frames + torsion angles | Raw atom coordinates |

## Recycling

The model uses **iterative recycling** — outputs from one pass are fed as inputs to the next, improving accuracy.

---

## Related Notes
- [[EN/01_AlphaFold3/Architecture/Pairformer]]
- [[EN/01_AlphaFold3/Architecture/Diffusion Module]]
- [[EN/01_AlphaFold3/Architecture/Model Training]]

## Tags
`#architecture` `#neural-network` `#transformer`
