# Model Training

[[EN/🏠 Home]] > [[EN/01_AlphaFold3/Architecture/AF3 Architecture Overview]] > Training
🇺🇦 [[01_AlphaFold3/Архітектура/Навчання моделі|Українська]]

---

## Three Training Stages

| Stage | Crop size (tokens) | Diffusion samples |
|---|---|---|
| Initial training | 384 | 256 × 48 = **12,288** |
| Fine-tune 1 | 640 | 256 × 32 = **8,192** |
| Fine-tune 2 | 768 | 256 × 32 = **8,192** |

**Data cutoff:** only PDB structures released before **30 September 2021** (for PoseBusters — before 30 September 2019).

## Training Dynamics

- **Local structures** (intra-chain metrics) are learned quickly — reach 97% of maximum within the first ~20,000 steps
- **Global arrangement** (interface metrics) is learned slower — protein–protein interface LDDT passes 97% only after ~60,000 steps

## Confidence Module

The confidence module predicts prediction errors:

- **pLDDT** — modified local distance difference test (per-atom level)
- **PAE (Predicted Aligned Error)** — pairwise error matrix
- **PDE (Predicted Distance Error)** — error in the predicted distance matrix

### Challenge of training confidence for diffusion:
AF2 trained confidence by regressing the error of the Structure Module output. For diffusion this doesn't work (only a single diffusion step is trained, not full structure generation).

**Solution:** A diffusion "mini-rollout" procedure — during training, a full structure is generated (with larger step size), and used to train the confidence head.

## Cross-distillation (countering hallucinations)

Training data is enriched with structures from **AlphaFold-Multimer v.2.3**, where disordered regions appear as extended loops. This "teaches" AF3 to mimic this behaviour.

---

## Related Notes
- [[EN/01_AlphaFold3/Architecture/Diffusion Module]]
- [[EN/01_AlphaFold3/Results/Confidence Scores]]

## Tags
`#training` `#fine-tuning` `#confidence` `#plddt` `#pae`
