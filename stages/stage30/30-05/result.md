# Stage30-05 — common `Q(i)` geometric/moduli anchor

```text
STAGE=30-05
ITEM=COMMON_QI_GEOMETRIC_OR_MODULI_ANCHOR
STATUS=SUBMITTED_PENDING_AUDIT
```

## Result

The required common anchor exists and is explicit in the already source-locked Testa--Stoll modular model of the **same cuboid surface**:

```text
Sbar_Q(i) ~= (X(8) x X(8))/Delta G0.
```

With quotient coordinates

```text
XY=TZ,
X=a1+c,
Y=-a1+c,
T=a2+i*a3,
Z=a2-i*a3,
```

the seven Stage29-02ha branch squareclasses are exact quadratic forms in `X,Y,T,Z`.  Therefore the modular residual action can be compared to the arrangement action on the same function field rather than by abstract `S4 ~= S4` matching.

## Exact action projection

In one explicit `X(4)` Hauptmodul gauge, the standard modular generators act by

```text
S : [x:y] -> [-x+y:x+y]
T : [x:y] -> [i*x:y].
```

The independent exact checker reduces the transformed seven forms modulo `XY=TZ` and obtains

```text
S_mod -> a06 = (A1 A2)(B1 B2)
T_mod -> a21 = (A1 C)(B2 B3).
```

Extending this assignment through the exact 24-element `PSL2(Z/4)` table gives

```text
MODULAR_PSL2_Z4_ORDER=24
MODULAR_TO_BRANCH_KERNEL_ORDER=4
MODULAR_TO_BRANCH_KERNEL_IDS=g04,g06,g12,g14
MODULAR_TO_BRANCH_KERNEL_EQUALS_V_mod=true
MODULAR_TO_BRANCH_IMAGE_ORDER=6
MODULAR_TO_BRANCH_IMAGE_IDS=a00,a05,a06,a11,a19,a21
```

Thus the source-geometric comparison is **not** a faithful `S4 -> S4` isomorphism on the seven branch squareclasses.

Instead:

```text
1 -> V_mod ~= V4
  -> PSL2(Z/4) ~= S4
  -> S3_branch
  -> 1
```

in this chosen gauge.  A different admissible `X(4)` gauge conjugates the displayed `S3`; the kernel/order statement is the invariant content.

The displayed image is not the previously audited Q-liftable coordinate-permutation `S3`.  This is expected rather than contradictory: the chosen modular gauge is over `Q(i)` and the generator `T` uses `i`.

## Meaning for Stage30-04

Stage30-04 correctly found 24 abstract simultaneous `4+3` action identifications.  Stage30-05 shows why none of those received geometric credit automatically: the actual common-model map to the seven branch squareclasses is nonfaithful.

Therefore:

```text
STAGE30_04_24_CANDIDATES_VALID_FINITE_RELABELINGS=true
STAGE30_04_24_CANDIDATES_GEOMETRIC_ADAPTERS=false
ABSTRACT_S4_TO_S4_IDENTIFICATION_IS_R29_KUM5_SOLUTION=false
```

This is a semantic sharpening, not a contradiction of the audited finite computation.

## What remains

The missing data have become smaller and more concrete.  The `V_mod` kernel must be lifted explicitly into the endpoint sign-deck action, and the resulting lift must be made compatible with the nontrivial element of `Gal(Q(i)/Q)`.

That is the Stage30-06 wall:

```text
L30-V4-SIGN-DECK-GALOIS-LIFT
  = CLASS2_STAGE30_06
```

30-06 must derive the mathematical semilinear/cocycle relation first.  Only after that derivation may 30-06P generate the sole remaining Codex task, and 30-06C may only verify the frozen identities exhaustively.

No new Class3 theorem requirement was exposed by 30-05.

## Reclassification

```text
L30-QI-FINITE-EQUIVARIANT-SEARCH
  = CLASS1_DISCHARGED_STAGE30_04

L30-COMMON-GEOMETRIC-OR-MODULI-ANCHOR
  = CLASS1_SUBMITTED_EXACT_COMMON_MODEL_AND_ACTION_PROJECTION

L30-V4-SIGN-DECK-GALOIS-LIFT
  = CLASS2_STAGE30_06

NEW_CLASS3_THEOREM_GATE
  = NONE

HIDDEN_CLASS1_PENDING_COUNT=0
```

## Reproducibility

Added:

```text
stages/stage30/30-05/source-lock.md
stages/stage30/30-05/common-anchor.json
stages/stage30/30-05/verify_common_anchor.py
```

The checker uses exact rational/Gaussian-rational arithmetic only, recomputes `PSL2(Z/4)`, checks the seven quadratic forms modulo the Segre relation, and verifies the kernel/image against the audited Stage30-02C action ledger.

## Scope firewalls

```text
COMMON_QI_MODEL_ANCHOR=SUBMITTED_VERIFIED_BY_EXACT_CHECKER
MODULAR_S4_EQUALS_ARRANGEMENT_S4=false
V4_SIGN_DECK_LIFT_VERIFIED=false
Q_GALOIS_COCYCLE_VERIFIED=false
DEFECT_ELIMINATION_COUNT=0
R29_KUM5_DISCHARGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false

AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=30-06_QI_OVER_Q_DESCENT_COCYCLE_DERIVATION
NEXT_EXPECTED_COMMAND=Stage30-audit
```
