# Stage33-04 — BR0G physical-boundary residue production state

The second hostile audit accepted the odd-primary arithmetic branch and isolated exactly one remaining production residual:

```text
PREVIOUS_AUDIT_VERDICT=PASS_ODD_PRIMARY_RESIDUAL_REJECT_ALL_PRIMARY_CLOSURE_ON_HIGHER_TWO_POWER_GERSTEN_DESCENT
PREVIOUS_NEW_KERNEL_ID=R33-BR0G-TWO-PRIMARY-PRIME-POWER-GERSTEN-CHARACTER-DESCENT
```

That residual has now been executed directly. No sibling unit is used to weaken the Stage33-04 closure contract. The unit returns to the hostile-audit boundary; it is not CLOSED and releases nothing before audit PASS.

```text
STAGE33_UNIT=33-04
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0G=CLAIMED_DISCHARGED_PENDING_HOSTILE_AUDIT
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

## Locked exact prefix

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

The accepted exponent-two 17D residual retains exact mod-2 first-residue realizability, V4 divisor descent, and function/constant-squareclass descent.

## Odd-primary arithmetic descent — hostile-audited prefix

The previous residual remains closed exactly as audited:

```text
boundary arithmetic prime-divisor orbits = 60
  Q singletons      = 48
  Q(i) pairs        = 12
crossing orbits:
  Q singletons      = 96
  Q(i) pairs        = 24

odd-primary boundary character module =
Hom_cont(G_Q,Q/Z)_odd^48
  direct_sum
Hom_cont(G_Q(i),Q/Z)_odd^12.
```

No odd-primary reopening occurs in this leaf.

## Full two-primary prime-power Gersten descent

The arithmetic boundary quotient has exactly 60 component orbits and 120 crossing orbits. At a Q crossing the two-primary Tate-twist target is `Z/2`; at a Q(i) crossing it is `Z/4`. The curve localization/Faddeev residue sequence reduces the ramified part to these crossing groups with the sum-of-corestrictions relation on each arithmetic boundary P1.

For the Q crossing subgraph:

```text
vertices = 48
edges = 96
connected components = 1
incidence rank_F2 = 47
kernel rank_F2 = 49.
```

For the twelve Q(i) component orbits, each has exactly two Q(i)-crossing incidences. Corestriction from Q(i) to Q on the two-primary Tate-twist target is zero (`1+cc`, with `cc=-1` on order four). Hence each such orbit contributes one independent order-four ramified direction. Therefore the complete finite ramified two-primary crossing module is

```text
(Z/2)^49 direct_sum (Z/4)^12.
```

In particular:

```text
ramified exponent <= 4
order-8-or-higher ramified crossing classes = 0
ramified 2-torsion dimension over F2 = 49 + 12 = 61.
```

The last identity independently recovers the hostile-audited exponent-two dimension `61`; the new prime-power calculation is therefore a genuine lift of the accepted F2 prefix, not a replacement of it.

Arbitrary higher 2-power order occurs only in the unramified constant-field character factors:

```text
Hom_cont(G_Q,Q_2/Z_2)^48
  direct_sum
Hom_cont(G_Q(i),Q_2/Z_2)^12.
```

Thus the exact two-primary boundary-character kernel is recorded by

```text
0 -> Hom_cont(G_Q,Q_2/Z_2)^48
       direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12
  -> BR0G_boundary[2^infinity]
  -> (Z/2)^49 direct_sum (Z/4)^12
  -> 0.
```

Proper Brauer classes have zero boundary residue, so the proper-residue quotient does not alter this boundary kernel.

Source locator for the curve residue law: Gille--Szamuely, *Central Simple Algebras and Galois Cohomology*, Theorem 6.9.1 and Remark 6.9.5 (Faddeev sequence and its finite-Galois-module form).

## Order-four compatibility with the accepted F2 decomposition

The twelve order-four generators have twelve independent doubles inside the accepted 61D F2 cycle module. Against the known 44D unit-symbol secondary-residue image:

```text
rank_F2(order4 doubles) = 12
rank_F2(order4 doubles intersect unit-symbol span) = 9
rank_F2(order4 doubles mod unit-symbol span) = 3.
```

The latter three directions land inside the old 17D F2 residual quotient. As a diagnostic only, quotienting the finite ramified module by the known exponent-two unit-symbol image has invariant-factor shape

```text
(Z/2)^23 direct_sum (Z/4)^3.
```

This is **not** promoted to the final Stage33 class list: duplicate/class integration is downstream Stage33-07 work.

## Production evidence

```text
workflow_run=32709905847
workflow_conclusion=success
artifact_id=9513712470
artifact_zip_sha256=4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637
two_primary_prime_power_certificate_sha256=f8c7af7e365bf579ce7e4288662130a90976cd8b22aa8f019eae266cd63714ea
```

Every workflow step passed, including odd-primary prefix revalidation, the full prime-power two-primary calculation, and all inherited regressions.

## Re-audit boundary

```text
CLOSURE_CRITERIA_TOTAL=10
CLOSURE_CRITERIA_SATISFIED=10
UNRESOLVED_UNKNOWN_IN_SCOPE=0
NEW_KERNEL_ID=NONE
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
STAGE33_PROGRESS=2/11
STAGE33_06_RELEASED=false
NEXT_EXPECTED_COMMAND=Stage33-audit
```

Only hostile audit may promote Stage33-04 to CLOSED and release Stage33-06. No complete Q-defined Brauer-class list, Brauer--Manin obstruction, endpoint theorem, or perfect-cuboid conclusion follows from this production checkpoint.
