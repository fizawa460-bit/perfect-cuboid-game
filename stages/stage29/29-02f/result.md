# Stage29-02f — physical-open boundary and Brauer reduction

Status: **AUDITED PASS after bounded repair**.  Authoritative audit: `audit.md`; open algebraic correction: `open-algebraic-brauer-adapter.md`.

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

For `G=Gal(Q(i,sqrt(2))/Q) ~= V4`, the visible boundary permutation lattice is

```text
Div_D ~= Z^48 direct_sum (Z[G/H_i])^12.
```

## Open algebraic Brauer: corrected arithmetic target

For the nonproper open, the compactification model of the extended Picard complex is

```text
UPic(U_Qbar) ~= [Div_D(S_Qbar) -> Pic(S_Qbar)],
Div_D in degree 0,
Pic in degree 1.
```

Over `Q`, the algebraic Brauer quotient is controlled by

```text
Br_a(U) ~= H^2(Q,UPic(U_Qbar)).
```

Although the visible lattice action factors through `V4`, this does **not** by itself force the full absolute-Galois group above to be 2-primary: the unit lattice

```text
ker(Div_D -> Pic(S_Qbar))
```

can contribute inflation/character terms.  Therefore

```text
OPEN_ALGEBRAIC_ODD_PRIMARY_CLOSED=false.
```

The live algebraic receivers are

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryExtendedPicardAbsoluteGaloisHypercohomology
```

with finite `V4` cohomology retained as a subcomputation of `R29-BR0B`.

## Proper odd-primary transcendental Brauer: discharged

For the smooth proper cuboid surface,

```text
b2=78,
rho=64,
disc Pic(S_Qbar)=-2^28.
```

At every odd `ell`, the Picard and transcendental lattices split over `Z_ell`, and the Kummer quotient is represented by the reduction of the rank-14 transcendental module.

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

Fresh audit independently recomputed this value; after deleting `p=ell` for each tested odd `ell`, the gcd remains `128`.  Hence every odd `ell` has an admissible Frobenius witness with no eigenvalue `1` on the twisted transcendental quotient, so

```text
Br(S_Qbar)[ell]^{G_Q}=0 for every odd ell.
```

Together with the proper algebraic Brauer theorem,

```text
R29-BR1-PROPER-ODD=DISCHARGED
PROPER_NONCONSTANT_BRAUER_ODD_PRIMARY=ABSENT_AUDITED.
```

## What remains open on the physical open

The proper result does not determine classes on `U` that fail to extend across the boundary.  The live receivers are

```text
R29-BR0A=BoundaryDivisorPicardSublatticeRankSaturationAndUnitKernel
R29-BR0B=BoundaryExtendedPicardAbsoluteGaloisHypercohomology
R29-BR0G=BoundaryGerstenResidueAndIntersectionComplexFor72Components
R29-BR2A=PhysicalOpenTwoPrimaryBrauerIntegralLattice
R29-BR2B=PhysicalOpenTwoPrimaryEvaluationMapsOnQvPoints
```

`R29-BR0B` retains possible algebraic odd-primary unit/character terms.  `R29-BR0G` retains genuinely nonextendable boundary-residue classes.  No Brauer--Manin obstruction is claimed until the relevant group and local evaluation maps are computed.

## Routing

```text
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02F_AUDIT=PASS
BOUNDED_REPAIR=OPEN_EXTENDED_PICARD_ABSOLUTE_GALOIS_SCOPE_PLUS_ODD_ELL_INTEGRAL_ADAPTER
OPEN_ALGEBRAIC_ODD_PRIMARY_CLOSED=false
PROPER_ODD_TRANSCENDENTAL_BRAUER=ABSENT
R29_BR1_PROPER_ODD=DISCHARGED
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-02g
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
