# Stage33-04 — BR0G physical-boundary residue production state

The previous hostile audit of PR #1362 accepted the exact geometric/two-primary prefix and correctly blocked closure on one residual:

```text
PREVIOUS_AUDIT_VERDICT=PASS_EXACT_PREFIX_BLOCKED_NEW_KERNEL_AFTER_REJECTING_PREMATURE_BR0G_CLOSURE
PREVIOUS_NEW_KERNEL_ID=R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT
```

That named residual has now been executed directly. No sibling unit is used to weaken the Stage33-04 contract, and no further production subquest is opened before re-audit.

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

## Audited prefix

```text
boundary components = 72 = 24 side + 48 exceptional
crossings = 144
integral incidence rank = 71
integral cycle rank = 73
rank(cc-I) = 12
Smith nonzero factors(cc-I) = [1 x 12]
geometric fixed cycle module = (Q/Z)^61
Ford/Kummer pullback rank = 0
F2 Q-fixed cycle dimension = 61
unit-symbol secondary-residue span = 44
explicit F2 graph residual = 17
```

The exponent-two 17D residual already has exact first-residue realizability, finite V4 divisor descent, and function/constant-squareclass descent with constant cocycle dimension zero.

## Odd-primary residual execution

The boundary Galois action gives 60 arithmetic prime-divisor orbits:

```text
48 Q-orbits represented by individually fixed geometric components
12 Q(i)-orbits represented by complex-conjugate geometric pairs
```

The 144 geometric crossings split as

```text
96 Q-singletons + 24 Q(i)-conjugate pairs.
```

For odd primary torsion, neither Q nor Q(i) has nontrivial odd-order roots of unity, so the Tate-twist invariant at every codimension-two crossing is zero. Compatible first-residue characters are therefore unramified on each complete boundary P1 and reduce exactly to constant-field characters.

Thus the odd-primary boundary character module is exactly

```text
Hom_cont(G_Q,Q/Z)_odd^48
  direct_sum
Hom_cont(G_Q(i),Q/Z)_odd^12.
```

This is a parametric exact module, not a finite list of Q-defined Brauer generators. Proper nonconstant odd-primary source classes are already absent by the Stage29 audited input, and proper constants have zero boundary residues.

Execution evidence:

```text
workflow_run=32704767658
workflow_rerun_job=97364320359
workflow_conclusion=success
artifact_id=9511990569
artifact_zip_sha256=1b1ad90b4ece3ace6bf378cb33afd3e09688efdcdc4c99ce460820beb9ab530f
odd_primary_character_descent_sha256=c89e2c2d71a6b48685f4670481bd7b97245b7e772c44ab58da2ca89f5950d3bc
```

The initial attempt failed before the new leaf on a transient external-Magma 504. Re-running only that failed job succeeded through all steps, including the odd-primary descent.

## Re-audit boundary

```text
CLOSURE_CRITERIA_TOTAL=10
CLOSURE_CRITERIA_SATISFIED=10
UNRESOLVED_UNKNOWN_IN_SCOPE=0
NEW_KERNEL_ID=NONE
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
```

Stage33 progress remains `2/11`; Stage33-06 remains locked. Only hostile audit may promote this unit to CLOSED and release downstream work.

```text
DO_NOT_OPEN_ANOTHER_STAGE33_04_SUBQUEST_BEFORE_REAUDIT=true
COMPLETE_Q_DEFINED_BRAUER_CLASS_LIST=false
BRAUER_MANIN_OBSTRUCTION_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT_EXPECTED_COMMAND=Stage33-audit
```
