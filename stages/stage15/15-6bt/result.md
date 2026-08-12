# Stage15-6bt — Selberg/large-sieve theorem-species audit

Base: merged PR #854. Audit verdict: BLOCK.

Browning–Loughran develop a general sieve for rational points, but their quantitative Selberg-sieve theorem with explicit power-saving control is specialized to smooth quadric hypersurfaces of dimension at least 3. The Stage15 shared-edge counting space is instead the split toric surface `Bl_4(P1 x P1)` of dimension 2 and Picard rank 6.

Thus the general almost-Fano equidistribution framework only supplies qualitative/little-o sieving, while the explicit quadric Selberg theorem cannot be imported.

```text
STAGE15_6_SUBSTAGE=6bt
STAGE15_6BT_AUDIT_VERDICT=BLOCK
STAGE15_6BT_GENERAL_LARGE_SIEVE_SPECIES_MATCH=true
STAGE15_6BT_QUANTITATIVE_SELBERG_THEOREM_APPLICABLE=false
STAGE15_6BT_REASON=STAGE15_IS_TORIC_SURFACE_DIM2_NOT_QUADRIC_DIMGE3
STAGE15_6BT_EXIT=UNIVERSAL_TORSOR_ELEMENTARY_LATTICE_AUDIT_READY
```
