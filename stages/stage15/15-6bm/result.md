# Stage15-6bm — physical toric congruence-neighbourhood adapter

Base: Stage15-6bl.

Stage15-2b identifies the physical shared-edge incidence space with a chamber of the dense torus of the split toric surface `Bl_4(P1 x P1)`, and proves that the exact Stage15 cutoff `R` is an anticanonical height.

The two primitive Pythagorean parameter ratios `m/n` and `r/s` are the two rational torus coordinates before the finite chamber/canonical postfilters. At every odd core prime, Stage15-6aa gives `p∤mnrs`; hence these ratios are units and the 6bl congruences are well-defined finite-place conditions.

For fixed squarefree `q` and fixed S/O orientation, the conditions

\[
m/n\equiv\lambda\pmod q,\qquad r/s\equiv\mu\pmod q
\]

therefore define a nonempty clopen finite adelic neighbourhood on the dense torus. Primewise it has codimension two in the two independent torus coordinates and expected local mass `q^{-2+o(1)}`. Positivity/canonical ordering/exactly-two remain archimedean or monotone postfilters and do not enlarge the count.

This stage is only an adapter. It does not assert uniform equidistribution for polynomially growing `q`.

```text
STAGE15_6_SUBSTAGE=6bm
STAGE15_6BM_AUDIT_VERDICT=PASS
STAGE15_6BM_PHYSICAL_SPACE=SPLIT_TORIC_DENSE_ORBIT_CHAMBER
STAGE15_6BM_HEIGHT=EXACT_ANTICANONICAL_R
STAGE15_6BM_CHANNEL_CONDITION=FINITE_ADELIC_CLOPEN_NEIGHBOURHOOD
STAGE15_6BM_FIXED_q_LOCAL_DENSITY=q^(-2+o(1))
STAGE15_6BM_PHYSICAL_POSTFILTERS_RETAINED=true
STAGE15_6BM_POLYNOMIAL_q_UNIFORMITY_PROVED=false
STAGE15_6BM_EXIT=EFFECTIVE_TORIC_EQUIDISTRIBUTION_AUDIT_READY
```