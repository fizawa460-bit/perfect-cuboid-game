# Stage29-02f — boundary/Picard complex

## Exact complex

Let `D=S\U` be the 72-component boundary from `physical-open-boundary.md`.  Over `Qbar`, projectivity of `S` gives the standard exact sequence

```text
0 -> Qbar^*
  -> O(U_Qbar)^*
  -> Div_D(S_Qbar)
  -> Pic(S_Qbar)
  -> Pic(U_Qbar)
  -> 0.
```

The load-bearing finite object is therefore the two-term lattice complex

```text
C_D = [ Div_D(S_Qbar) -> Pic(S_Qbar) ].
```

It simultaneously remembers

1. principal relations among boundary divisors / nonconstant units on `U`;
2. the boundary sublattice in the rank-64 Picard group;
3. the quotient `Pic(U_Qbar)`;
4. the Galois action needed for the algebraic Brauer group of the nonproper open.

This avoids the invalid shortcut

```text
Br_1(U)/Br(Q) ?= H^1(Q,Pic(U_Qbar))
```

without first accounting for nonconstant units.

## Finite Galois reduction

Testa--Stoll explicitly realize the Picard Galois action over

```text
K=Q(i,sqrt(2)),
G=Gal(K/Q) ~= V4.
```

All boundary components are also defined over `K`, and their permutation action is explicit.  Thus the relative algebraic calculation is a finite `G`-hypercohomology problem for `C_D`.

Since `G` has order four, positive-degree finite-group cohomology is annihilated by four.  Consequently any new algebraic Brauer contribution created by deleting `D`, after constants are removed and the above finite descent complex is used, is 2-primary.

This does **not** compute the exact 2-primary group.  The following integral data must be extracted from the known Picard lattice:

```text
B = image(Div_D -> Pic(S_Qbar))
rank(B)
saturation(B in Pic(S_Qbar))
K_D = kernel(Div_D -> Pic(S_Qbar))
Q_D = coker(Div_D -> Pic(S_Qbar)) = Pic(U_Qbar)
G-actions on K_D, B, Q_D
```

## Existing executable input

Michael Stoll's public verification file already constructs

```text
Pic
PicL
pmPic
ccPic      # complex conjugation
ctPic      # sqrt(2) conjugation
C1s        # first 24 are the rational side-boundary conics
pts        # the 48 exceptional curves
```

at the immutable source lock used by 29-02c-LG2.  Therefore `R29-BR0A/B` requires no new geometric enumeration: it is an extraction/cohomology computation on already certified matrices.

A probe script is included as `boundary_module_probe.m`; it identifies the exact subgroup generators and checks Galois stability before any cohomology calculation is attempted.

## Residual receivers

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryPicardComplexV4Cohomology
```

Sufficient output for `R29-BR0B` is an explicit finite abelian group for the relative algebraic part together with maps back to divisor residues.  A zero answer is allowed; nonzero 2-primary output is also allowed and must not be promoted to an obstruction until local evaluation is computed.
