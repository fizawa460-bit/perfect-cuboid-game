# Stage29-02f — geometric boundary Gersten receiver

## Why this remains after the proper-surface odd-prime kill

The odd-primary Frobenius witness concerns classes on the smooth proper compactification `S`.  The physical open is

```text
U=S\D
```

with 72 geometric boundary components.  A class in `Br(U)` need not extend across `D`, so it may carry nonzero residues on boundary curves even when `Br(S)` has no odd-primary nonconstant class.

For the smooth compactification, purity/Gersten gives the residue complex beginning

```text
Br(S_Qbar)
 -> Br(U_Qbar)
 -> direct_sum_{D_j} H^1(Qbar(D_j),Q/Z)
 -> direct_sum_{x in D^(2)} Q/Z.
```

The last map records residue compatibility at codimension-two intersection points.  It is therefore incorrect to set the open geometric Brauer correction to zero merely because every boundary component is a rational curve.

## Exact boundary input already available

```text
24 side conics (Q-defined)
48 exceptional curves
72 total geometric components
```

All components are explicit in the Testa--Stoll verification model, and pairwise incidence can be read from the same curve/node incidence data used to construct the Picard intersection matrix.

The remaining geometric receiver is therefore finite/combinatorial plus one-variable residue arithmetic:

```text
R29-BR0G=BoundaryGerstenResidueAndIntersectionComplexFor72Components
```

Required output:

1. enumerate all codimension-two intersections among the 72 components on `S_Qbar`;
2. normalize each rational boundary component and record the intersection-point divisor;
3. compute the kernel of the second-residue compatibility map prime-by-prime;
4. quotient by residues of global proper Brauer classes;
5. descend the surviving geometric boundary classes under `Gal(Qbar/Q)`;
6. keep algebraic and transcendental/open-boundary contributions separated.

## Odd-prime narrowing

From `odd-primary-proper-brauer.md`, an odd-primary class on `U` cannot be sourced from a nonconstant class on proper `S`.  Therefore, for odd `ell`, every surviving class must be visible in the boundary-residue complex.

This gives a useful stop rule:

```text
if R29-BR0G has zero odd-primary kernel after Galois descent,
then the entire physical-open nonconstant Brauer group is 2-primary.
```

No such zero result is claimed in this submission.

## Evaluation still separate

Even a nonzero class in `Br(U)` is not automatically a Brauer--Manin obstruction.  The local evaluation maps

```text
U(Q_v) -> Br(Q_v)
```

must be computed and compared across all places.  Evaluation belongs to `R29-BR2B`, not to this residue enumeration.
