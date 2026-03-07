# Diffusion Module

[[EN/🏠 Home]] > [[EN/01_AlphaFold3/Architecture/AF3 Architecture Overview]] > Diffusion Module
🇺🇦 [[01_AlphaFold3/Архітектура/Дифузійний модуль|Українська]]

---

## How It Works

The Diffusion Module replaces the **Structure Module** from AF2 and directly generates **raw 3D atom coordinates**.

### Standard diffusion approach:
1. Model is trained to receive "noised" atom coordinates
2. It learns to predict the true (clean) coordinates
3. At inference: random noise → iterative denoising → final structure

## Multi-scale Nature

The diffusion process teaches the network to understand structure at multiple scales:
- **Low noise** → emphasis on local stereochemistry (bond geometry)
- **High noise** → emphasis on the global arrangement of the system

## Advantages over AF2 Structure Module

| Aspect | AF2 Structure Module | AF3 Diffusion Module |
|---|---|---|
| Parametrization | Backbone frames + torsion angles | Raw atom coordinates |
| Chemical flexibility | Protein-specific | Any chemical component |
| Stereochemical penalties | Required complex penalties | Not needed (learned implicitly) |
| Model type | Deterministic | **Generative (distribution of answers)** |

## Key Property: Generativity

Because the module is **generative**, for each output:
- Local structure is sharply defined (e.g., bond geometry)
- Even when the network is **uncertain** about position — local stereochemistry remains correct

## Hallucination Problem

Generative models are prone to **hallucinations** — inventing plausible-looking structure in disordered regions.

**Solution:** Cross-distillation — enriching training data with structures from AlphaFold-Multimer v.2.3, where disordered regions appear as extended loops.

---

## Related Notes
- [[EN/01_AlphaFold3/Architecture/AF3 Architecture Overview]]
- [[EN/01_AlphaFold3/Architecture/Diffusion Models — Theory and Applications]]
- [[EN/01_AlphaFold3/Limitations/Model Limitations]]

## Tags
`#diffusion` `#generative-model` `#architecture` `#atom-coordinates`
