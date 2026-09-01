# Stage33 MAIN transient handoff

status: UNPROMOTED_DELTA
base_main_state_canonical_sha256: 7d52c93a517fc96050b2f78583ae05e5e4ff4f983c2533c673ca008060bd0226

## Exact narrowing from this batch

New certificate:
- `stages/stage33/33-12/j2-marked-order4-lift-label-gap.json`
- verifier: `stages/stage33/33-12/verify_j2_marked_order4_lift_label_gap.py`

The locked semantic `u1` has exactly `2^14=16384` mixed-Smith half-lifts. Exact bilinear evaluation gives 16 proper-Br2 functionals; current source-side `cc/ct` invariance leaves four retained-10D masks `{4,5,6,7}`, each represented by 1024 half-lifts. Historical mask 6 is therefore only one of four and is not restored.

Every one of the four invariant classes has quadratic numerator `12 mod 16`. The previously proposed degree-two value `4 mod 16` has zero survivors and its transfer law is not source-locked, so it cannot select a label.

## Refined next exact leaf

`SOURCE_LOCK_ACTUAL_MARKED_ORDER4_LIFT_OR_DIRECT_14_EVALUATION_ROW_FOR_U1_WITHOUT_TARGET_COMPATIBILITY_SELECTION_THEN_REPEAT_FOR_U2`

For the named J2 row, the minimal positive datum is one actual marked order-4 lift `w_J2` in the retained mixed Smith basis satisfying `2*w_J2=u1`, source-locked by the geometric correspondence; equivalently, supply its fourteen evaluations on the retained `T/2T` basis. A labeled index-512 glue or full marked `NS<->T` anti-isometry remains a stronger sufficient input. The full 2x14 adapter additionally needs the analogous `u2` datum.

Do not use raw-75D/V4 compatibility, masks 742/736, or historical mask 6 to choose among the four source-side candidates. No source coordinate, Kummer column, closure, receiver, theorem, endpoint, or release credit is added.
