# Stage14-tH17 canonical downstream pointer

Current revision: `r2.md`.

Merged tH17 `result.md` remains the valid broad ambient-state TT*/operator applicability audit requested by t61. After merged t62, downstream stages must use the narrower R2 matched-block formulation first.

Importable R2 facts:

```text
MATCHED_RECTANGLE_PROJECTION_ISOMETRY_PROVED=true
PHYSICAL_MASS_VECTOR_RAYLEIGH_IS_EXACT_TARGET=true
PROJECTED_TTSTAR_GRAM_IDENTITY_PROVED=true
MATCHED_GRAM_EXACT_H2_MINUS_DIAGONAL_FORMULA_PROVED=true
MATCHED_RECTANGLE_PROJECTED_DUAL_LARGE_SIEVE_IMPLIES_PHYSICAL_TARGET=true
```

Do not import either missing theorem as proved:

```text
PHYSICAL_MASS_VECTOR_KUMMER_RAYLEIGH_BOUND_PROVED=false
MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_PROVED=false
```

Current minimal obstruction:

```text
PhysicalMassVectorKummerRayleighBound
```

Stronger sufficient theorem:

```text
MatchedRectangleProjectedKummerDualLargeSieve
```

Next: Stage14-t63 should attack the exact matched projected Kummer Gram after diagonal / same-row / same-column / principal-transverse / nonprincipal-transverse separation, before any entrywise absolute Schur majorant.
