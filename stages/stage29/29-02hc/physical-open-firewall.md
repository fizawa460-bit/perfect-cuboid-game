# Physical-open / arrangement-open firewall — audited

Let

```text
D_all={x y z (x+y)(x+z)(y+z)(x+y+z)=0},
B_arr=P2\D_all.
```

The inverse image of `B_arr` is the unbranched projective congruence-cover open.

Stage29-02f's physical algebraic open instead imposes the nonzero-side condition

```text
a1*a2*a3 != 0.
```

Over `Qbar`, face- or space-diagonal-zero divisors can remain in this physical algebraic open, so

```text
U_phys != U_arr
```

as algebraic varieties.

For rational nondegenerate sides, however, a rational sum of two or three squares cannot be zero unless the relevant sides vanish.  Therefore every genuine rational endpoint point lies in the arrangement open:

```text
U_phys(Q) subset U_arr(Q).
```

Thus `U_arr(Q)=empty` would be a valid endpoint obstruction.  No converse/open equality is used.

The inclusion does **not** transfer the Stage16–20 population contracts or Stage29-02f Brauer calculation.  In particular no automatic adapter is available for

```text
M1,N1,M2,N2,M3,
R<=B,
gcd/primitivity,
canonical ordering,
face multiplicities,
asymptotic density,
Brauer residues.
```

```text
PHYSICAL_OPEN_EQUALS_ARRANGEMENT_OPEN=false
PHYSICAL_Q_POINTS_LIE_IN_ARRANGEMENT_OPEN=true
STAGE16_20_POPULATION_TRANSFER=false
HEIGHT_TRANSFER=false
PRIMITIVITY_TRANSFER=false
CANONICAL_ORDER_TRANSFER=false
ASYMPTOTIC_TRANSFER=false
BRAUER_TRANSFER_AUTOMATIC=false
BACKFLOW_TO_STAGE16_28=false
```

Receivers:

```text
R29-NF-PHYS1 = ArrangementOpenToPhysicalRationalLocusContainment   DISCHARGED
R29-NF-PHYS2 = ArrangementBoundaryResiduesToPhysicalBoundaryResidues OPEN
```
