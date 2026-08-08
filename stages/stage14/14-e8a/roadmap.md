# Stage14-e8a — accumulating curves / square-root source

## Scope

This is an e8-side branch that is intentionally independent of Stage14-e9.  It does **not** edit `stages/stage14/e-supplement-roadmap.md` and does not change the e9 gcd/lcm-local-statistics contract.

Stage14-e8a asks a narrower geometric question left open by Stage14-e8:

> Can the finite `R_EB(B) ~ sqrt(B)` signal be explained by one or a few accumulating rational curves on the Euler-brick K3 surface?

The frozen Euler-brick surface is

\[
U^2=E^2+X^2,\qquad
V^2=E^2+Y^2,\qquad
Z^2=X^2+Y^2
\]

in `P^5`, with physical Euclidean height uniformly comparable to projective max height.

## Work plan

1. **Literature collision audit first.**  Recheck Saunderson, Spohn's derived cuboid, Himane's generator, and McKinnon's accumulating-curve/K3 point-count framework.
2. **Classical curve height laws.**  Compute the physical-height degree of the Saunderson family and of its derived-cuboid image.
3. **Degree gate.**  Translate a rational curve of projective degree `d` into the bounded-height exponent `2/d`; isolate the degree required for a `sqrt(B)` contribution.
4. **Low-degree geometry.**  Prove that no projective line can meet the physical torus of the three-quadric model, and inspect the simplest degree-four candidates via split lifts of `(1,1)` curves on the toric base.
5. **Finite census collision.**  Recompute all primitive Euler bricks through `B=10^6`, classify the exact Saunderson and derived-Saunderson members, and test small-height `(1,1)` split relations without promoting a finite coefficient search to a theorem.
6. **Boundary.**  Do not claim that all degree-four rational curves have been classified unless a complete Neron-Severi/lattice argument is supplied.

## Promotion rules

```text
SQRT_SOURCE_FROM_SAUNDERSON=false unless degree/height calculation permits it
SQRT_SOURCE_FROM_DERIVED_SAUNDERSON=false unless degree/height calculation permits it
DEGREE4_CURVE_CLASSIFICATION_COMPLETE=false unless proved globally
FINITE_MOBIUS_SCAN_IS_THEOREM=false
E9_FILES_TOUCHED=false
```

## Target output

A successful e8a should leave one of two conclusions:

- an explicit degree-four rational curve/multisection that can genuinely generate a `B^(1/2)` layer; or
- a rigorous exclusion of the classical low-degree candidates plus a sharply stated degree-four search target for later lattice/Kummer work.
