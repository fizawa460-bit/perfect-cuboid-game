# Stage29-02f — boundary/Picard complex

## Exact compactification model

Let `D=S\U` be the 72-component boundary.  Over `Qbar` the divisor/unit/Picard exact sequence is

```text
0 -> Qbar^*
  -> O(U_Qbar)^*
  -> Div_D(S_Qbar)
  -> Pic(S_Qbar)
  -> Pic(U_Qbar)
  -> 0.
```

The compactification model of the extended Picard complex is

```text
UPic(U_Qbar) ~= [Div_D(S_Qbar) -> Pic(S_Qbar)],
Div_D in degree 0,
Pic(S_Qbar) in degree 1.
```

For a number field, the algebraic Brauer quotient is

```text
Br_a(U)=Br_1(U)/im Br(Q)
      ~= H^2(Q,UPic(U_Qbar)).
```

This complex remembers the unit lattice, the boundary image in Picard, `Pic(U_Qbar)`, and their Galois actions.

## V4 input is finite but not the whole arithmetic cohomology

Testa--Stoll realize the visible lattice action over

```text
K=Q(i,sqrt(2)),
G=Gal(K/Q) ~= V4.
```

All boundary components are defined over `K`, and the differential is Galois equivariant.  Hence finite `V4` cohomology is an explicit subproblem.

However it is **not** valid to replace absolute Galois `H^2(Q,UPic)` by finite `V4` hypercohomology solely because the lattice action factors through `V4`.  The unit lattice

```text
K_D=ker(Div_D -> Pic(S_Qbar))
   =O(U_Qbar)^*/Qbar^*
```

can contribute inflation/character terms through the absolute Galois group of `K`; such terms need not be 2-primary.  Therefore

```text
OPEN_ALGEBRAIC_ODD_PRIMARY_CLOSED=false.
```

The finite `V4` calculation remains useful, but it cannot by itself prove `Br_a(U)[odd]=0`.

## Exact integral input still required

```text
B = image(Div_D -> Pic(S_Qbar))
rank(B)
saturation(B in Pic(S_Qbar))
K_D = kernel(Div_D -> Pic(S_Qbar))
Q_D = coker(Div_D -> Pic(S_Qbar)) = Pic(U_Qbar)
G-actions on K_D, B, Q_D
```

Michael Stoll's verification source already constructs the Picard lattice, the first 24 rational side-boundary conics, all 48 exceptional curves, and the two generators of the `V4` action.  `boundary_module_probe.m` therefore remains a valid extraction preflight.

## Residual receivers

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel

R29-BR0B=BoundaryExtendedPicardAbsoluteGaloisHypercohomology
         including unit-kernel inflation/character terms,
         with finite V4 cohomology as a subcomputation.
```

A zero odd-primary answer is allowed, but it must come from this full arithmetic calculation, not from the order of `V4` alone.  Any nonzero class must still be separated from geometric boundary-residue classes and cannot be promoted to a Brauer--Manin obstruction before local evaluation.

See `open-algebraic-brauer-adapter.md` for the audit correction.
