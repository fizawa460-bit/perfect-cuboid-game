# Stage33-04 — BR0G physical-boundary residue production state

The previous hostile audit of PR #1362 accepted the exact geometric/two-primary prefix and correctly blocked closure on one residual:

```text
PREVIOUS_AUDIT_VERDICT=PASS_EXACT_PREFIX_BLOCKED_NEW_KERNEL_AFTER_REJECTING_PREMATURE_BR0G_CLOSURE
PREVIOUS_NEW_KERNEL_ID=R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT
```

That named residual has now been executed directly. No sibling unit is used to weaken the Stage33-04 contract.

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
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
NEW_KERNEL_ID=NONE
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Previously audited exact prefix

The accepted prefix remains unchanged:

```text
boundary components = 72 = 24 side + 48 exceptional
crossings = 144
connected components = 1
integral incidence rank = 71
integral cycle rank = 73
ct = identity
rank(cc-I) = 12
Smith nonzero factors(cc-I) = [1 x 12]
geometric fixed cycle module = (Q/Z)^61
Ford/Kummer pullback rank = 0
F2 Q-fixed cycle dimension = 61
unit-symbol secondary-residue span = 44
explicit F2 graph residual = 17
```

The exponent-two 17D residual already has exact first-residue realizability, finite V4 divisor descent, and function/constant-squareclass descent with constant cocycle dimension zero.

## Newly executed odd-primary arithmetic-character descent

The source-locked boundary Galois action has 60 arithmetic prime-divisor orbits:

```text
48 geometric boundary components fixed individually by Gal(Q(i,sqrt(2))/Q)
12 complex-conjugate pairs, fixed by the sqrt(2)-involution
```

Thus the boundary constant fields are exactly `Q` for 48 orbits and `Q(i)` for 12 orbits. The 144 geometric crossings similarly split as

```text
96 Q-singletons + 24 Q(i)-conjugate pairs.
```

For every odd prime power, neither `Q` nor `Q(i)` has nontrivial odd-order roots of unity. Hence the odd-primary Tate-twist coefficient at every codimension-two crossing has zero invariants. Every compatible odd-primary first residue is therefore unramified on its complete boundary `P^1`, and the unramified character is exactly a constant-field character.

The resulting exact parametric odd-primary boundary character module is

```text
Hom_cont(G_Q,Q/Z)_odd^48
  direct_sum
Hom_cont(G_Q(i),Q/Z)_odd^12.
```

This is a parametric exact description, not a finite list of Q-defined Brauer generators. Stage29 already certifies that nonconstant proper-surface odd-primary Brauer classes are absent, while constant proper classes have zero boundary residues. Therefore no additional proper odd-primary quotient changes this boundary residue module.

New production evidence:

```text
workflow_run=32704767658
workflow_rerun_job=97364320359
workflow_conclusion=success
artifact_id=9511990569
artifact_zip_sha256=1b1ad90b4ece3ace6bf378cb33afd3e09688efdcdc4c99ce460820beb9ab530f
odd_primary_character_descent_sha256=c89e2c2d71a6b48685f4670481bd7b97245b7e772c44ab58da2ca89f5950d3bc
```

The first attempt of the same workflow failed before the new leaf because the external Magma calculator returned a transient 504 during the already-audited boundary-Galois reconstruction. Re-running only the failed job succeeded through every step, including the new odd-primary leaf.

## Closure claim returned to hostile audit

The previously isolated unknown is now claimed discharged:

```text
CLOSURE_CRITERIA_TOTAL=10
CLOSURE_CRITERIA_SATISFIED=10
UNRESOLVED_UNKNOWN_IN_SCOPE=0
NEW_KERNEL_ID=NONE
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
```

This is not a self-certified closure. Stage33 progress remains `2/11`, and Stage33-06 remains locked until hostile audit accepts Stage33-04 as `CLOSED`.

Firewalls:

```text
COMPLETE_Q_DEFINED_BRAUER_CLASS_LIST=false
BRAUER_MANIN_OBSTRUCTION_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

```text
NEXT_EXPECTED_COMMAND=Stage33-audit
```
