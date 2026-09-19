# MB104 P6I — factor-line ambient Picard restriction interface wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-INTERFACE WALL / P6H RETAINED / NO CREDIT**

## Target

P6H proves for every hypothetical genus-one carrier on the hostile P6 ray that the two quotient maps

```text
psi_1,psi_2:E -> C8/G ~= P1
```

have the same degree-`56l` fiber line:

```text
M_1 := psi_1^*O(1) ~= M_2 := psi_2^*O(1).
```

The desired P6I move was to identify surface divisor classes `F_1,F_2` whose restrictions to the normalization are `M_1,M_2`, so that P6H becomes an exact ambient Picard restriction condition.

## Retained-source inspection

The inspection is deliberately bounded to the current retained MB104 source inventory and the immutable archive head

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11.
```

### Beauville product-cover adapter

`BEAUVILLE-PRODUCT-COVER-SOURCE-NOTE.md` source-locks

```text
P=C8 x C8 -> X -> B
```

and the diagonal finite group actions. It does not identify a divisor class on the smooth cuboid resolution whose restriction to a downstairs carrier is `psi_i^*O(1)`.

### Historical e=2 external-product Picard reduction

`GENUS1-SPAN5-BALANCED16-000707-E2-EXTERNAL-PRODUCT-PICARD-REDUCTION.md` concerns the product divisor line bundle `O_P(Zbar)` in the support-specific e=2 route. Its factor classes `A,B` arise only after the candidate extra condition

```text
Phi_Z=0
```

removes the correspondence component. They are line bundles on `C8`, of degree `28l`, not ambient divisor classes on the cuboid resolution restricting to the current degree-`56l` pencils.

That candidate e=2 conclusion is not imported into P6.

### Historical half-hyperplane factorization

`GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION.md` depends on the support-specific residual double cover, exact Picard64 parity, and a candidate ambient-H1 linearization. Its half-hyperplane class is not an adapter for the full-deck e=4 factor maps.

### Historical absent-type half-branch class

`GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md` treats the old `(7,7,0)` support and the absent-type residual two-torsion class. The hostile P6 support has all three types `(6,2,6)`, so there is no absent-type class to identify with `M_1-M_2`.

### Stoll--Testa genus-five fibrations

`STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md` source-locks the surface genus-five fibrations used elsewhere in MB104. Nothing in the inspected retained adapters identifies either current quotient map `psi_i:E->C8/G` with one of those surface fibrations, or identifies `M_i` with the restriction of a class `F_Q` satisfying a Stoll--Testa half-hyperplane relation.

Matching target genus or modular provenance is not an adapter.

## Disposition

No exact retained identification

```text
M_i ~= nu^*O_S(F_i)
```

with source-locked ambient divisor classes `F_i` was found in the bounded retained inventory inspected above.

Therefore P6H cannot presently be pushed into the surface Picard lattice without guessing the factor-pencil classes. P6I is parked at this interface.

This is **not** a repository-wide nonexistence claim. A new source-locked adapter identifying the ambient factor pencils would reopen P6I immediately.

## Why numerical Picard alone is insufficient

Even if a degree-zero surface class `F_1-F_2` were guessed,

```text
nu^*O_S(F_1-F_2) ~= O_E
```

is a statement in `Pic^0(E)`, not merely an intersection-number statement. Nonzero surface numerical classes may restrict trivially to a singular carrier normalization, especially in the presence of the unsupported exceptional null curves. No Lefschetz/injectivity shortcut is retained for this exact big-nef singular curve.

## Next route

The common-cover information can be used without descending `M_i` to the cuboid surface: work directly on

```text
P=C8 x C8.
```

Because the connected product image is stabilized by diagonal full `G`, its Jacobian correspondence commutes with `G`. The next shallow gate is therefore

```text
MB104-P6J-FULL-G-PRODUCT-CORRESPONDENCE-CENTRALIZER.
```

First target: source-lock the exact `G`-character decomposition of `H^0(C8,K)` and determine whether the integral algebraic centralizer is restrictive enough for a degree-`56l` common etale correspondence. Do **not** import the historical candidate e=2 conclusion `Phi_Z=0`.

## Source locks

Historical archive exact head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `BEAUVILLE-PRODUCT-COVER-SOURCE-NOTE.md` blob `974c6cfecb6e4141615583841a0c90146ad2b4a6`;
- `GENUS1-SPAN5-BALANCED16-000707-E2-EXTERNAL-PRODUCT-PICARD-REDUCTION.md` blob `dc2def9e4d0148aa3146a034a2ce0ef331206a29`;
- `GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION.md` blob `ba7ea7a7e21f0e4ca5d8b96c3dac1dbafbbddff6`;
- `GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md` blob `e22de5a6f4be163268e699cde03d37e1e564d43b`;
- `STOLL-TESTA-G2-ISOTRIVIAL-FIBRATION-SOURCE-NOTE.md` blob `b71225ac859eef5afefeebd019a97c403ed27655`.

Current P6H certificate blob:

```text
5c9b3eafed5e55d0a360870722cea7ea81758745
```

## Firewalls

```text
ambient_factor_classes_identified=false
P6H_common_line_retained=true
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
