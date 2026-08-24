# Stage33-04 — BR0G physical-boundary residue audited state

Final hostile-audit verdict:

`PASS_AFTER_QI_FADDEEV_SIDE_CLARIFICATION`

The previously isolated higher-two-power residual has been executed and independently re-audited. The numerical/module outputs are unchanged by the audit repair; the repair makes explicit the two distinct Faddeev relations at a `Q(i)` crossing: on a `P^1_{Q(i)}` component the two `Q(i)`-rational crossing residues satisfy the ordinary sum relation `a+b=0`, while on the adjacent `P^1_Q` component the degree-two closed point contributes through `Cor_{Q(i)/Q}=1+c`, which is zero on the order-four Tate-twist invariants because complex conjugation acts by `-1`.

```text
STAGE33_UNIT=33-04
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=true
BR0G=DISCHARGED
PHYSICAL_BOUNDARY_72_INVENTORY_COMPLETE=true
BOUNDARY_STABLE_IDS_COMPLETE=true
RESIDUE_INCIDENCE_MATRIX_EXACT=true
MULTIQUADRATIC_PULLBACK_RESIDUES_EXACT=true
EXCEPTIONAL_DIVISOR_RESIDUES_EXACT=true
PHYSICAL_BOUNDARY_OMISSIONS=0
ARITHMETIC_ODD_CHARACTER_DESCENT_COMPLETE=true
FULL_TWO_PRIMARY_PRIME_POWER_GERSTEN_CHARACTER_DESCENT_COMPLETE=true
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
NEW_KERNEL_ID=NONE
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Locked exact boundary prefix

```text
boundary components = 72 = 24 side + 48 exceptional
geometric crossings = 144
integral incidence rank = 71
integral cycle rank = 73
rank(cc-I) = 12
Smith nonzero factors(cc-I) = [1 x 12]
geometric fixed cycle module = (Q/Z)^61
two-primary geometric fixed module = (Q_2/Z_2)^61
Ford/Kummer pullback rank = 0
F2 Q-fixed cycle dimension = 61
unit-symbol secondary-residue span rank_F2 = 44
explicit exponent-two graph residual dimension = 17
```

The exponent-two 17D residual has exact mod-2 first-residue realizability, V4 divisor descent, and function/constant-squareclass descent.

## Odd-primary arithmetic descent

The arithmetic boundary prime-divisor and crossing orbits are

```text
boundary prime-divisor orbits = 60
  Q singletons = 48
  Q(i) pairs   = 12
crossing orbits = 120
  Q singletons = 96
  Q(i) pairs   = 24
```

For odd-primary torsion the crossing Tate-twist invariants vanish over both `Q` and `Q(i)`, so the compatible first residues reduce to constant-field characters:

```text
Hom_cont(G_Q,Q/Z)_odd^48
  direct_sum
Hom_cont(G_Q(i),Q/Z)_odd^12.
```

## Full two-primary prime-power Gersten descent

For the 48 `Q` component orbits and 96 `Q` crossing orbits, the `F2` incidence matrix has rank `47`; the connected `Q` crossing subgraph therefore contributes

```text
96 - 47 = 49
```

independent order-two ramified directions.

For each of the twelve `Q(i)` component orbits, the normalization is `P^1_{Q(i)}` and has exactly two `Q(i)`-rational marked crossing points. The Faddeev residue relation on that component is

```text
a + b = 0 in H^0(Q(i), Q_2/Z_2(-1)),
```

so the implementation uses coefficients `[1,3]` modulo four and obtains one independent `Z/4` direction per `Q(i)` component orbit. On the adjacent `P^1_Q` side, the same crossing is a degree-two closed point and its residue enters through

```text
Cor_{Q(i)/Q} = 1 + c.
```

Complex conjugation acts by `-1` on the order-four Tate-twist invariants, hence this transfer is zero and imposes no additional relation. Thus the complete finite ramified two-primary crossing module is

```text
(Z/2)^49 direct_sum (Z/4)^12.
```

Consequently

```text
ramified exponent <= 4
order-8-or-higher ramified crossing classes = 0
ramified 2-torsion dimension over F2 = 49 + 12 = 61.
```

This independently recovers the audited exponent-two dimension `61`. Arbitrary higher 2-power order occurs only in the unramified constant-field character factors:

```text
Hom_cont(G_Q,Q_2/Z_2)^48
  direct_sum
Hom_cont(G_Q(i),Q_2/Z_2)^12.
```

The exact two-primary boundary-character kernel is therefore recorded by

```text
0 -> Hom_cont(G_Q,Q_2/Z_2)^48
       direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12
  -> BR0G_boundary[2^infinity]
  -> (Z/2)^49 direct_sum (Z/4)^12
  -> 0.
```

Proper Brauer classes have zero boundary residue, so quotienting by proper residues does not alter this boundary kernel.

Source adapter: Gille--Szamuely, *Central Simple Algebras and Galois Cohomology*, Theorem 6.9.1 and Remark 6.9.5 (Faddeev/localization sequence with residue corestrictions).

## Compatibility with the audited F2 decomposition

The twelve order-four generators have independent doubles of rank `12` in the accepted 61D exponent-two cycle module. Against the known 44D unit-symbol secondary-residue image:

```text
rank_F2(order4 doubles) = 12
rank_F2(order4 doubles intersect unit-symbol span) = 9
rank_F2(order4 doubles mod unit-symbol span) = 3.
```

The three quotient directions lie in the previously materialized 17D residual. As a diagnostic only, quotienting the finite ramified module by the known exponent-two unit-symbol image has shape

```text
(Z/2)^23 direct sum (Z/4)^3.
```

This diagnostic is not promoted to the final Stage33 Q-defined class list; duplicate/class integration remains Stage33-07 work.

## Production and independent audit evidence

```text
production_functional_head=a6c892bd0a9a865271070ac3c63fe2c55a4d178a
preaudit_head=fb02a61b970368e394fd42c68686170a12cfccb1
workflow_run=32709905847
workflow_conclusion=success
artifact_id=9513712470
artifact_zip_sha256=4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637
two_primary_prime_power_certificate_sha256=f8c7af7e365bf579ce7e4288662130a90976cd8b22aa8f019eae266cd63714ea
```

The hostile audit independently recomputed the artifact ZIP digest and canonical certificate digest; reconstructed the `60=48+12` arithmetic component orbits and `120=96+24` crossing orbits; recomputed the connected `Q`-subgraph rank `49`; verified every `Q(i)` component orbit has exactly two `Q(i)` crossing incidences; and independently reproduced the ranks `12`, `9`, and `3` for the order-four doubles and unit-symbol subspace.

The three commits after the successful production head modify only result/handoff/controller state and do not alter the mathematical scripts or certificates.

## Closure and release firewall

```text
CLOSURE_CRITERIA_TOTAL=10
CLOSURE_CRITERIA_SATISFIED=10
UNRESOLVED_UNKNOWN_IN_SCOPE=0
NEW_KERNEL_ID=NONE
HOSTILE_AUDIT=PASS_AFTER_QI_FADDEEV_SIDE_CLARIFICATION
UNIT_STATUS=CLOSED
UNIT_CLOSED=true
DOWNSTREAM_RELEASED=true
BR0G=DISCHARGED
STAGE33_PROGRESS=3/11
```

`DOWNSTREAM_RELEASED=true` means Stage33-04 is now a valid prerequisite. It does **not** release Stage33-06 by itself: Stage33-06 still requires Stage33-03 to be `CLOSED` as well.

No complete Q-defined Brauer-class list, Brauer--Manin obstruction, endpoint theorem, or Perfect Cuboid existence/nonexistence conclusion is claimed by Stage33-04 closure alone.
