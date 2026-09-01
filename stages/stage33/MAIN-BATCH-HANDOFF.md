# Stage33 MAIN audit handoff

status: READY_FOR_HOSTILE_AUDIT
pr: #1476
branch: stage33-post1475-j2-v4-generator-adapter
new_pr_before_audit_pass: FORBIDDEN
merge_before_audit_pass: FORBIDDEN

machine_audit_gate: PENDING_HOSTILE_AUDIT
machine_audit_scope: STAGE33_12_V10_QPIC_CERTIFIED_ACTUAL_SWAP_DESCENT_HOSTILE_AUDIT
ordinary_main_before_audit_pass: FORBIDDEN
next_expected_command: Stage33-audit

## Audit boundary

Stop ordinary Stage33 MAIN here and audit PR #1476 at its latest head. The qPic marking blocker has been removed and the actual coordinate swaps have been descended exactly to the retained mixed discriminant basis. The remaining blocker is narrower: the named J2 **order-4 lift** has not yet been source-locked under the actual S3 action.

Do not continue the mathematical leaf during this audit. If hostile audit PASSes, start the next work in a new PR/branch from the audited result.

## Exact progress in this PR

### 1. Literal qPic -> historical Magma Picard bridge is now exact

Authoritative artifacts:

- `stages/stage33/33-07/indlist-to-magma-picard-basis.json`
  - literal 64x64 bridge
  - canonical SHA256 `0a1863928608c2698051b4d22d0ac1b92128164825dbdb7edfb82fe941a05c8f`
- `stages/stage33/33-07/marked-picard-basis-bridge-certified.json`
  - certified canonical SHA256 `039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92`
  - determinant `-1`
  - full Gram transport exact
  - named actions `cc,ct,a1,a2,a3,b1,b2,b3,c` intertwine exactly
  - seven sign conjugations exact
  - actual swap12/swap13 available in the historical Picard basis
  - S3 braid exact
- `stages/stage33/33-12/qpic-bridge-local-recertification-receipt.json`
  - PASS_EXACT_LOCAL_REVERIFY
  - canonical SHA256 `c6e9466c509699b1ef2c037ad248915673d391f00115032782970667f44e7dd0`

The former `SOURCE_AUTHORIZED_PINNED_UPSTREAM_QPIC_64x64_MARKED_PICARD_BRIDGE_MISSING` blocker is superseded. The retained Smith route is still **not** the literal qPic marking and must not be substituted for it historically.

### 2. Actual swaps descended to the literal mixed (2,4,8) discriminant basis

Primary artifact:

- `stages/stage33/33-12/j2-actual-swap-mixed-discriminant-descent.json`
  - status `PASS_EXACT_ACTUAL_SWAPS_DESCENDED_TO_MIXED_DISCRIMINANT_WITH_RESIDUAL_S3_ORBIT_MATERIALIZED`
  - canonical SHA256 `93dc99201a04fdec7c8ad8369409e7cb593ae7f8fba44b772df1b2cc1d29cfa3`
  - mixed moduli `[2,2,2,2,4,4,4,4,4,4,8,8,8,8]`
  - swap12 and swap13 induce full-rank 14-dimensional F2 actions
  - both are involutions and satisfy the S3 braid exactly
  - semantic `u1` is fixed by both actual swaps
  - proper-Br2 dual convention is checked against the retained `cc/ct` actions

Residual order-4 affine candidate action on retained10 masks is now exact:

- mask 4: swap12 -> 7, swap13 -> 4
- mask 5: swap12 -> 5, swap13 -> 7
- mask 6: swap12 -> 6, swap13 -> 6
- mask 7: swap12 -> 4, swap13 -> 5

Thus mask 6 (proper14 mask 25) is the **unique joint S3-fixed candidate**.

### 3. Authority is synced, but mask 6 is NOT named J2

Compact authority:

- `stages/stage33/MAIN-STATE.json`
- schema `STAGE33_MAIN_COMPACT_STATE_V10_QPIC_CERTIFIED_ACTUAL_SWAP_DESCENT`
- controller schema `STAGE33_BRAUER_EXPLICIT_DAG_CONTROLLER_V54_QPIC_CERTIFIED_ACTUAL_SWAP_DESCENT`
- progress remains `6/11`

Current missing interface:

`NAMED_J2_ORDER4_LIFT_ACTUAL_S3_BEHAVIOR_OR_EQUIVALENT_SOURCE_LABEL_MISSING`

Next exact leaf, only after audit PASS/new PR:

`SOURCE_LOCK_NAMED_J2_ORDER4_LIFT_BEHAVIOR_UNDER_ACTUAL_SWAP12_SWAP13; IF_JOINT_FIXED_SELECT_UNIQUE_MASK6_ELSE_USE_THE_EXACT_S3_ORBIT_TO_IDENTIFY_THE_CORRECT_CANDIDATE`

## Critical firewall — audit this aggressively

The following inference is **NOT** established:

`semantic u1 fixed by swap12/swap13` => `named J2 order-4 lift is fixed by swap12/swap13`.

Therefore the following is also **NOT** established:

`unique joint S3-fixed candidate = mask 6` => `mask 6 is the authoritative named J2 source coordinate`.

Historical mask 6 has only been independently rederived as the unique joint S3-fixed candidate. It remains non-authoritative as named J2 until the order-4 lift behavior or an equivalent source-locked label is proved.

Still false/open at this boundary:

- `named_J2_order4_lift_actual_s3_behavior_source_locked = false`
- `named_J2_proper_Br2_source_coordinate_materialized = false`
- `retained10_named_J2_source_coordinate_materialized = false`
- `named_J2_source_target_relation_materialized = false`
- `matrix_standard_columns_materialized = 0`
- `stage33_12_closed_exact = false`
- `stage33_07_reclosed = false`
- `stage33_08_released = false`
- theorem/receiver/endpoint credit = false
- perfect-cuboid existence/nonexistence claim = false
- merge allowed = false

Also remain revoked/do-not-use:

- historical mask 6 as named J2 without new source lock
- `C2+C3=h_J2`
- masks 742/736 as J2 merely from compatibility
- direct copying of `A_T[2]` coefficients as proper-Br2 dual coefficients
- nonunique retained-basis witnesses in place of the literal certified qPic bridge
- retained Smith V as the literal 64x64 qPic marking

## Hostile audit checklist

1. Recompute/canonical-check the raw 64x64 qPic bridge and certified bridge; verify the source lock, determinant, Gram transport, action intertwining, sign conjugations, actual swaps and S3 braid.
2. Replay `verify_j2_actual_swap_mixed_discriminant_descent.py`; independently attack the mixed-modulus transport, divisibility, F2 reduction, full ranks, involutions, braid and proper-Br2 dual transpose convention.
3. Independently recompute the four-candidate S3 orbit and uniqueness of retained10 mask 6 / proper14 mask 25.
4. Try to find any illicit step that turns semantic `u1` invariance into order-4-lift invariance. Any such inference without a source-locked lift label is an audit failure.
5. Verify `controller.json`, `MAIN-STATE.json`, and `sync_main_state.py --check` agree on V54/V10 authority, the current missing interface, anti-loop rules, and all closure/credit firewalls.
6. Confirm qPic-gap archaeology is marked superseded rather than silently rewritten, and the retained Smith route is not promoted to the literal marking.
7. Confirm no Kummer matrix standard column, named J2 proper-Br2 source coordinate, parent reclosure, Stage33 progress increment, merge, or downstream theorem credit was smuggled in.

## Minimal audit reading set

Start with:

1. `AGENTS.md`
2. `stages/stage33/MAIN-STATE.json`
3. this file
4. `stages/stage33/controller.json`
5. `stages/stage33/33-12/qpic-bridge-local-recertification-receipt.json`
6. `stages/stage33/33-07/marked-picard-basis-bridge-certified.json`
7. `stages/stage33/33-12/j2-actual-swap-mixed-discriminant-descent.json`
8. `stages/stage33/33-12/verify_j2_actual_swap_mixed_discriminant_descent.py`
9. `stages/stage33/33-12/j2-marked-order4-lift-label-gap.json`
10. `stages/stage33/33-12/j2-marked-order4-geometric-sign-indistinguishability.json`
11. `stages/stage33/sync_main_state.py`

Only open older evidence when one of these files gives an explicit source lock requiring verification.

## Replay anchors

Branch-local bridge recertification contract is encoded in `.github/workflows/stage33-07-branch-recertify.yml`; it checks the raw canonical bridge and reruns `stages/stage33/33-07/certify_marked_picard_basis_bridge.py` without a new external Magma dispatch.

Current exact Stage33-12 replay is encoded in `.github/workflows/stage33-12-main.yml`; in particular it runs:

- `python stages/stage33/33-12/verify_j2_actual_swap_mixed_discriminant_descent.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

## Cleanup performed before audit

The temporary bounded `stage33-12-workspace-export` workflow and runkey used only to inspect the branch-local workspace were removed before this handoff. They are not part of the mathematical deliverable.
