# Stage29-02f — open algebraic Brauer adapter

This note is the bounded audit repair for the algebraic Brauer calculation on the nonproper physical open.

Let

```text
U = S \ D
```

with `S/Q` smooth proper and `D` the audited 72-component geometric boundary.

## Standard extended Picard convention

Borovoi--van Hamel's extended Picard complex `UPic(U_Qbar)` is represented, using the smooth compactification `S`, by

```text
C_D = [ Div_D(S_Qbar) -> Pic(S_Qbar) ]
```

with

```text
Div_D in degree 0,
Pic(S_Qbar) in degree 1.
```

Equivalently this is the compactification model arising from the distinguished triangle

```text
UPic(U_Qbar) -> Div_D(S_Qbar) -> Pic(S_Qbar) -> UPic(U_Qbar)[1].
```

The divisor/unit/Picard exact sequence is

```text
0 -> Qbar^*
  -> O(U_Qbar)^*
  -> Div_D(S_Qbar)
  -> Pic(S_Qbar)
  -> Pic(U_Qbar)
  -> 0.
```

For a number field, `H^3(Q,G_m)=0`, and the algebraic Brauer quotient is controlled by

```text
Br_a(U)=Br_1(U)/im Br(Q)
      ~= H^2(Q,UPic(U_Qbar)).
```

## Why the finite-V4 shortcut is insufficient

For the cuboid surface, the actions on `Div_D`, `Pic(S_Qbar)`, and their differential factor through

```text
G=Gal(Q(i,sqrt(2))/Q) ~= V4.
```

This makes the finite `V4` lattice calculation valuable, but it does **not** imply that `Br_a(U)` is 2-primary.  The kernel

```text
U_D = ker(Div_D -> Pic(S_Qbar))
    = O(U_Qbar)^*/Qbar^*
```

is a free unit lattice.  Even when the finite quotient acts trivially on such a lattice, absolute Galois `H^2` can contain character/residue torsion of odd order.  Thus inflation from `Gal(Qbar/K)` cannot be discarded merely because the visible lattice action factors through `V4`.

Consequently the submission-time claim

```text
OPEN_ALGEBRAIC_NEW_ODD_PRIMARY=ABSENT_CANDIDATE
```

is **not promoted**.  The corrected state is

```text
OPEN_ALGEBRAIC_ODD_PRIMARY_CLOSED=false.
```

## Correct residual receiver

The existing finite extraction remains useful:

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel.
```

The cohomology receiver must be arithmetic, not only finite-quotient:

```text
R29-BR0B
 = BoundaryExtendedPicardAbsoluteGaloisHypercohomology
 = compute H^2(Q,UPic(U_Qbar)),
   including the unit-kernel inflation/character terms,
   with the V4 calculation retained as its finite-quotient subproblem.
```

This is separate from geometric nonextendable boundary classes in

```text
R29-BR0G=BoundaryGerstenResidueAndIntersectionComplexFor72Components.
```

The proper-surface odd-primary transcendental Brauer kill in `odd-primary-proper-brauer.md` is unaffected by this correction.
