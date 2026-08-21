# Stage29-02f — fresh audit

```text
AUDITED_PR=1300
AUDITED_SUBMISSION_HEAD=0fa6cf5097be63a2026e012679ba94fa482f664c
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Verdict

The physical-open boundary ledger is correct and the proper-surface odd-primary transcendental Brauer witness is valid.  The submission-time claim that the **open algebraic** Brauer correction is automatically 2-primary from the finite `V4` action is not valid and is not promoted.

The bounded repair has two parts:

1. use the standard extended Picard complex convention

```text
UPic(U_Qbar) ~= [Div_D(S_Qbar) -> Pic(S_Qbar)]
Div_D degree=0
Pic degree=1,
```

with

```text
Br_a(U) ~= H^2(Q,UPic(U_Qbar));
```

2. retain the proper odd-`ell` Kummer argument using the odd-prime integral Picard/transcendental splitting.

The first correction means that finite `V4` lattice action alone does not kill odd-primary algebraic classes on the open: the unit lattice can contribute absolute-Galois inflation/character terms.  See `open-algebraic-brauer-adapter.md`.

## Physical open and boundary

Testa--Stoll Lemma 3 verifies smoothness wherever `a1*a2*a3 != 0`.  Hence the rational-box open is

```text
Ubar=Sbar intersect D_+(a1*a2*a3),
```

and the minimal resolution is an isomorphism over it.

The complement on `S_Qbar` has exactly

```text
24 Q-defined side conics
48 exceptional curves
72 geometric irreducible components.
```

The exceptional curves split as `24/Q + 24/Q(i)`, giving

```text
Div_D ~= Z^48 direct_sum (Z[G/H_i])^12,
G=Gal(Q(i,sqrt(2))/Q) ~= V4.
```

```text
PHYSICAL_OPEN_AUDIT=PASS
BOUNDARY_72_COMPONENT_LEDGER_AUDIT=PASS
BOUNDARY_GALOIS_MODULE_AUDIT=PASS
```

## Open algebraic Brauer correction

Borovoi--van Hamel's extended Picard formalism places the compactification complex in degrees `0,1` and identifies the algebraic Brauer quotient over a number field with `H^2(Q,UPic)`.

Although the visible lattices and differential factor through `V4`, the unit lattice

```text
K_D=ker(Div_D -> Pic(S_Qbar))
```

can contribute absolute-Galois `H^2` terms.  Therefore

```text
OPEN_ALGEBRAIC_ODD_PRIMARY_CLOSED=false.
```

The corrected receiver is

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryExtendedPicardAbsoluteGaloisHypercohomology
```

with finite `V4` cohomology retained only as a subcomputation of `R29-BR0B`.

## Proper odd-primary transcendental Brauer

The proper surface has `b2=78`, `rho=64`, and `disc Pic=-2^28`.  At every odd `ell`, the Picard lattice and its transcendental orthogonal complement split over `Z_ell`, so the geometric Brauer `ell`-torsion is represented by the reduction of the rank-14 transcendental quotient.

The audited Stage29-02e semisimple transcendental characteristic polynomial is

```text
3*h16 + h32 + 3*h8.
```

At a good prime `p != ell`, a fixed vector after Tate twist forces

```text
ell | D_p,
D_p=(2p-a16)^3*(2p-a32)*(2p-a8)^3.
```

The committed exact witness gives

```text
gcd_p D_p=128.
```

Fresh audit independently recomputed this value.  After deleting the forbidden `p=ell` row for each tested odd `ell`, the gcd remains exactly `128`; for odd `ell` outside the test-prime set all rows are admissible.  Thus every odd `ell` has an admissible witness Frobenius with no eigenvalue `1` on the twisted transcendental quotient.

Hence

```text
Br(S_Qbar)[ell]^{G_Q}=0 for every odd ell.
```

Together with the proper algebraic Brauer theorem, every nonconstant Brauer class on proper `S/Q` is 2-primary.

```text
PROPER_ODD_TRANSCENDENTAL_BRAUER_AUDIT=PASS
R29-BR1-PROPER-ODD=DISCHARGED
```

## What remains open on U

The proper result does not remove classes on `U` that fail to extend across the boundary.  The live receivers are

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryExtendedPicardAbsoluteGaloisHypercohomology
R29-BR0G=BoundaryGerstenResidueAndIntersectionComplexFor72Components
R29-BR2A=PhysicalOpenTwoPrimaryBrauerIntegralLattice
R29-BR2B=PhysicalOpenTwoPrimaryEvaluationMapsOnQvPoints
```

`R29-BR0B` controls the algebraic open arithmetic, including possible odd-primary unit/character terms.  `R29-BR0G` controls genuinely geometric nonextendable boundary residues.  No Brauer--Manin obstruction is claimed until local evaluation maps are computed.

## Routing

PR #1298 / Stage29-02e is already merged as `adbf407c57f21a01eaf625bc53a92bb01e940058`.  No Stage16--28 backflow is required.  The independent suffix queue may advance to `29-02g` while the explicit Brauer receivers remain live.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02F_AUDIT=PASS
BOUNDED_REPAIR=OPEN_EXTENDED_PICARD_ABSOLUTE_GALOIS_SCOPE_PLUS_ODD_ELL_INTEGRAL_ADAPTER
PHYSICAL_OPEN_AUDIT=PASS
BOUNDARY_72_COMPONENT_LEDGER_AUDIT=PASS
OPEN_ALGEBRAIC_ODD_PRIMARY_CLOSED=false
PROPER_ODD_TRANSCENDENTAL_BRAUER=ABSENT
R29_BR1_PROPER_ODD=DISCHARGED
OPEN_BOUNDARY_ODD_PRIMARY_CLOSED=false
TWO_PRIMARY_BRAUER_CLOSED=false
BRAUER_MANIN_OBSTRUCTION_PROVED=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02g
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
