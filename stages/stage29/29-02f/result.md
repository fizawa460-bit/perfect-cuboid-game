# Stage29-02f — physical-open boundary and Brauer reduction

Status: **AUDITED PASS after bounded repair**.  Detailed proof/audit: `audit.md`; grading repair: `open-algebraic-brauer-adapter.md`.

## Audited physical open

For rational cuboid points, nondegeneracy is exactly

```text
a1*a2*a3 != 0.
```

Thus

```text
Ubar = Sbar intersect D_+(a1*a2*a3)
```

is the algebraic open relevant to rational boxes.  Testa--Stoll Lemma 3 makes this open smooth, so the minimal resolution `S -> Sbar` is an isomorphism over it.

The geometric boundary `D=S\U` has exactly

```text
24 Q-defined side conics
24 Q-defined exceptional curves
24 exceptional curves strictly over Q(i)
72 components total.
```

For `G=Gal(Q(i,sqrt(2))/Q) ~= V4`, its divisor permutation lattice is

```text
Div_D ~= Z^48 direct_sum (Z[G/H_i])^12.
```

## Audited algebraic Brauer reduction on U

The nonproper calculation uses the extended Picard complex

```text
C_D=[Div_D(S_Qbar) -> Pic(S_Qbar)],
Div_D in degree -1,
Pic in degree 0.
```

After constants are removed, this controls `Br_a(U)=Br_1(U)/im Br(Q)`.  All Galois action and the differential factor through the order-four group `V4`, so positive hypercohomology is 2-primary.  Hence

```text
OPEN_ALGEBRAIC_NEW_ODD_PRIMARY=ABSENT_AUDITED.
```

The exact 2-primary algebraic group remains the finite lattice/cohomology work

```text
R29-BR0A
R29-BR0B.
```

## Audited proper odd-primary transcendental Brauer reduction

For the smooth proper cuboid surface,

```text
b2=78,
rho=64,
disc Pic(S_Qbar)=-2^28.
```

At every odd `ell`, the Picard and transcendental lattices therefore split over `Z_ell`, and the Kummer quotient is the reduction of the rank-14 transcendental module.

The audited Stage29-02e semisimple characteristic polynomial is the package

```text
3*h16 + h32 + 3*h8.
```

For good `p != ell`, a fixed vector after Tate twist forces

```text
ell | D_p,
D_p=(2p-a_p(h16))^3*(2p-a_p(h32))*(2p-a_p(h8))^3.
```

The exact committed witness gives

```text
gcd_p D_p=128.
```

Fresh audit independently recomputed this value; after deleting `p=ell` for every tested odd `ell`, the gcd is still `128`.  Consequently every odd `ell` has an admissible Frobenius witness with no eigenvalue `1` on the twisted transcendental quotient, so

```text
Br(S_Qbar)[ell]^{G_Q}=0 for every odd ell.
```

Together with the proper algebraic Brauer theorem,

```text
R29-BR1-PROPER-ODD=DISCHARGED
PROPER_NONCONSTANT_BRAUER_ODD_PRIMARY=ABSENT_AUDITED.
```

## What remains open on the physical open

The proper calculation does not kill classes on `U` that have nonzero boundary residues.  Any remaining odd-primary class must be genuinely boundary-residue sourced.  The live receivers are

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryPicardComplexV4Cohomology
R29-BR0G=BoundaryGerstenResidueAndIntersectionComplexFor72Components
R29-BR2A=PhysicalOpenTwoPrimaryBrauerIntegralLattice
R29-BR2B=PhysicalOpenTwoPrimaryEvaluationMapsOnQvPoints
```

No Brauer--Manin obstruction is claimed until local evaluation maps are computed.

## Routing

```text
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02g
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
