# Stage29-02f — fresh audit

```text
AUDITED_PR=1300
AUDITED_SUBMISSION_HEAD=0fa6cf5097be63a2026e012679ba94fa482f664c
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
```

## Verdict

The physical-open boundary ledger is correct, the proper-surface odd-primary Brauer witness is valid, and the remaining open-surface Brauer problem is correctly reduced to explicit boundary and 2-primary receivers.

The bounded repair is to fix the degree convention of the extended Picard complex controlling the algebraic Brauer group of the nonproper open.  With

```text
C_D=[Div_D(S_Qbar) -> Pic(S_Qbar)]
Div_D degree=-1
Pic degree=0
```

and constants removed, `Br_a(U)` is controlled by positive `V4` hypercohomology.  Since `|V4|=4`, the new algebraic contribution is 2-primary.  See `open-algebraic-brauer-adapter.md`.

## Physical open and boundary

Testa--Stoll Lemma 3 verifies smoothness wherever `a1*a2*a3 != 0`.  Therefore the physical rational-box open is represented by

```text
Ubar=Sbar intersect D_+(a1*a2*a3)
```

and the minimal resolution is an isomorphism over it.

The complement on `S_Qbar` has exactly

```text
24 Q-defined side conics
48 exceptional curves
72 geometric irreducible components.
```

The exceptional curves split as `24/Q + 24/Q(i)`, so the boundary permutation module is

```text
Z^48 direct_sum (Z[G/H_i])^12,
G=Gal(Q(i,sqrt(2))/Q) ~= V4.
```

```text
PHYSICAL_OPEN_AUDIT=PASS
BOUNDARY_72_COMPONENT_LEDGER_AUDIT=PASS
BOUNDARY_GALOIS_MODULE_AUDIT=PASS
```

## Proper odd-primary transcendental Brauer

The proper surface has `b2=78`, `rho=64`, and `disc Pic=-2^28`.  For every odd `ell`, the Picard lattice is therefore an `ell`-adic direct summand of `H^2`, so the geometric Brauer `ell`-torsion is represented by the reduction of the rank-14 transcendental quotient.

The audited Stage29-02e semisimple transcendental characteristic polynomial is the package

```text
3*h16 + h32 + 3*h8.
```

At a good prime `p != ell`, a fixed vector after Tate twist forces the determinant factor

```text
D_p=(2p-a16)^3*(2p-a32)*(2p-a8)^3
```

to vanish modulo `ell`.  The committed exact integer witness gives

```text
gcd_p D_p=128.
```

Fresh audit independently recomputed the gcd.  After deleting the row `p=ell` for every tested `ell`, the gcd remains exactly `128`; for odd `ell` outside the test-prime set all rows are admissible.  Thus every odd `ell` has an admissible witness Frobenius with no eigenvalue `1` on the twisted transcendental quotient modulo `ell`.

Hence

```text
Br(S_Qbar)[ell]^{G_Q}=0 for every odd ell.
```

Together with the proper algebraic Brauer result, every nonconstant Brauer class on proper `S/Q` is 2-primary.

```text
PROPER_ODD_TRANSCENDENTAL_BRAUER_AUDIT=PASS
R29-BR1-PROPER-ODD=DISCHARGED
```

## What remains open

The proper result does not remove nonextendable classes on `U`.  Odd-primary classes on `U`, if any, must occur through boundary residues.  The remaining receivers are therefore

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryPicardComplexV4Cohomology
R29-BR0G=BoundaryGerstenResidueAndIntersectionComplexFor72Components
R29-BR2A=PhysicalOpenTwoPrimaryBrauerIntegralLattice
R29-BR2B=PhysicalOpenTwoPrimaryEvaluationMapsOnQvPoints
```

`R29-BR0A/B` are finite explicit lattice/cohomology computations; `R29-BR0G` remains necessary for nonextendable boundary-residue classes.  No Brauer--Manin obstruction is claimed until local evaluation maps are computed.

## Routing

PR #1298 / Stage29-02e is already merged as `adbf407c57f21a01eaf625bc53a92bb01e940058`.  No Stage16--28 backflow is required.  The next independent suffix is `29-02g`.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02F_AUDIT=PASS
BOUNDED_REPAIR=EXTENDED_PICARD_COMPLEX_GRADING_AND_ODD_ELL_INTEGRAL_ADAPTER
PHYSICAL_OPEN_AUDIT=PASS
BOUNDARY_72_COMPONENT_LEDGER_AUDIT=PASS
OPEN_ALGEBRAIC_ODD_PRIMARY=ABSENT
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
