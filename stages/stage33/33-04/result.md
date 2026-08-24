# Stage33-04 — BR0G physical-boundary residue audited state

Re-audit verdict:

`PASS_ODD_PRIMARY_RESIDUAL_REJECT_ALL_PRIMARY_CLOSURE_ON_HIGHER_TWO_POWER_GERSTEN_DESCENT`

The previously named odd-primary residual has been executed and is accepted. The unit still does not close because the full two-primary prime-power arithmetic Gersten layer is not certified by the existing exponent-two evidence.

```text
STAGE33_UNIT=33-04
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0G=OPEN
PHYSICAL_BOUNDARY_72_INVENTORY_COMPLETE=true
BOUNDARY_STABLE_IDS_COMPLETE=true
RESIDUE_INCIDENCE_MATRIX_EXACT=true
MULTIQUADRATIC_PULLBACK_RESIDUES_EXACT=true
EXCEPTIONAL_DIVISOR_RESIDUES_EXACT=true
PHYSICAL_BOUNDARY_OMISSIONS=0
ARITHMETIC_ODD_CHARACTER_DESCENT_COMPLETE=true
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=false
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-TWO-PRIMARY-PRIME-POWER-GERSTEN-CHARACTER-DESCENT
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Locked exact prefix

```text
boundary components = 72 = 24 side + 48 exceptional
crossings = 144
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

The 17 exponent-two residual directions have exact mod-2 first-residue realizability, V4 divisor descent, and function/constant-squareclass descent.

## Odd-primary arithmetic descent — now accepted

The boundary action gives

```text
48 Q-defined geometric-component singletons
12 Q(i)-conjugate component pairs
```

and the crossings give

```text
96 Q-singletons
24 Q(i)-conjugate pairs.
```

For odd-primary torsion, the crossing Tate-twist invariants vanish over `Q` and `Q(i)`. The compatible residue characters are therefore unramified on each complete boundary `P1` and reduce to constant-field characters. The exact parametric module is

```text
Hom_cont(G_Q,Q/Z)_odd^48
  direct_sum
Hom_cont(G_Q(i),Q/Z)_odd^12.
```

Current-head evidence:

```text
workflow_run=32705824742
workflow_conclusion=success
artifact_id=9512234314
artifact_zip_sha256=19aa8fa2ca3fe137a96865a2cc4dad4fe9e47eae6896904d2bcbf74db37b2792
odd_primary_character_descent_sha256=26af6864fd85f4a0be2a139ca353ec558ffc00520cc1e4bc5e8af64d5613a24a
```

## Remaining exact wall

The current two-primary arithmetic certificate is explicitly

```text
scope=EXPONENT_TWO_RESIDUAL_ONLY
actual_first_residue_function_descent_complete_mod2=true
constant_squareclass_descent_complete_mod2=true.
```

This cannot by itself certify the full `(Q_2/Z_2)^61` boundary module. At the actual codimension-two fields the two-primary Tate-twist targets are nonzero: `Q` has order-2 roots of unity and `Q(i)` has roots through order 4. Hence order-4 crossing compatibility, higher `2^n` constant-character families, and their exact quotient/descent remain outside the F2 computation.

The next exact leaf is

`L33-04-COMPUTE-FULL-Q2Z2-BOUNDARY-H1-AND-MU2-MU4-CROSSING-COMPATIBILITY`.

It must preserve the accepted F2 result as a prefix and compute the full two-primary first-residue character module, prime-power second residues at all arithmetic crossing orbits, proper-residue quotient, and exact survival/primary orders.

```text
STAGE33_PROGRESS=2/11
STAGE33_06_RELEASED=false
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```

No complete Q-defined Brauer-class list, Brauer-Manin obstruction, endpoint theorem, or perfect-cuboid conclusion follows from this checkpoint.
