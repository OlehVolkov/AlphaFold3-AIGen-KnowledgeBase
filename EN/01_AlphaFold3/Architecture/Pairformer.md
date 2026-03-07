# Pairformer

[[EN/🏠 Home]] > [[EN/01_AlphaFold3/Architecture/AF3 Architecture Overview]] > Pairformer
🇺🇦 [[01_AlphaFold3/Архітектура/Pairformer|Українська]]

---

## What is the Pairformer?

**Pairformer** is the new central processing block of AF3, replacing the **Evoformer** from AF2.

## Architecture

The Pairformer operates on two representations:
- **Pair representation:** shape `(n, n, c)`, where `c = 128`
- **Single representation:** shape `(n, c)`, where `c = 384`

`n` — number of tokens (polymer residues and atoms)

### Sub-blocks inside each of the 48 Pairformer blocks:
1. Triangle Update (outgoing edges)
2. Triangle Update (incoming edges)
3. Triangle Self-Attention (around starting node)
4. Triangle Self-Attention (around ending node)
5. Transition
6. Single Attention with pair bias
7. Transition (for single representation)

## Key Differences from Evoformer

- **MSA representation is not retained** — all information flows through the pair representation
- MSA processing is reduced to **inexpensive pair-weighted averaging**
- Number of MSA blocks reduced from ~48 to **4**
- Number of Pairformer blocks: **48** (same as AF2 Evoformer)

## Why This Design?

Simplifying MSA processing allows:
- More efficient modelling of diverse chemical entities
- Reduced computational cost
- Demonstrates that **lack of cross-entity evolutionary information** is not a major barrier

---

## Related Notes
- [[EN/01_AlphaFold3/Architecture/AF3 Architecture Overview]]
- [[EN/01_AlphaFold3/Architecture/Diffusion Module]]

## Tags
`#pairformer` `#architecture` `#transformer` `#evoformer`
