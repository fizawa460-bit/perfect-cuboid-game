# Stage33 MAIN transient handoff

status: UNPROMOTED_DELTA
base_main_state_canonical_sha256: d2c85c1a00acaf5db0662cc3e8a8894ad5bf666b3ae8842eea022e2646c80834

This file contains only work learned after that `MAIN-STATE.json` state.
Do not use it as history or repeat facts already present in `MAIN-STATE.json`.

## Latest narrowing

- Provenance of the locked named-J2 75D target is now resolved exactly.
- It was introduced at commit `f63a36dac006de3ef67acfa851ff458882bcaf99` by:
  `stages/stage33/33-12/materialize_j2_named_v4_h1_target_before_source_orientation.py`.
- That producer has two logically separate parts:
  1. construct the exact raw V4 cocycle `(raw_cc, raw_ct)` in historical-Magma Pic64 mod 2;
  2. project that raw cocycle to the locked 75D H1 quotient basis.
- Part (2) is generic. Part (1) is J2-specific.
- For J2, `raw_cc=0` comes from the actual Cech-overlap certificate and `raw_ct` comes from exact BigK support `[26,35,42,47,49,52]` transported to full Pic64.
- Semantic `u2` has a different discriminant support interface; do NOT substitute its `[52,54]` support for the J2 raw `ct` defect.
- Companion `beta2` is V4-fixed/retained, but the adjoint certificate still records `Q_defined_descent_credit_restored=false`. Do NOT call beta2 Q-defined without a new exact descent argument.

## Implemented reusable interface

- Added `stages/stage33/33-12/v4_pic2_raw_cocycle_projection.py`.
- Added `stages/stage33/33-12/verify_v4_pic2_raw_cocycle_projection.py`.
- The adapter accepts exact 64+64 raw cocycle components, checks the V4 cocycle equations, and projects them to the locked 75D H1 basis with an exact reconstruction witness.
- Actions run `33456711239` passed: adapter compile, exact replay of the locked J2 75D target, existing J2 verifier, and `sync_main_state.py --check`.
- Temporary workflow was removed after the successful replay.

## Exact remaining blocker

The 75D projection is no longer the missing interface. The missing datum is now exactly the one already isolated by `first-exact-kummer-column-input-audit.json`:

> one exact equivariant full-surface `mu_2` lift `b` for a retained proper-Br2 source vector, with enough `cc/ct` action to compute `(cc(b)-b, ct(b)-b)` in Pic/2, or equivalent equivariant unimodular Picard-transcendental glue data.

For the standard-column split route, prefer retained basis `e2` or `e3`. Once either raw cocycle is exact, feed it directly to the new projection adapter; then use the already-certified named-J2 relation to derive the sibling column.

## Do not repeat

- Do not search again for the J2 75D target producer; provenance is resolved above.
- Do not infer a beta2 75D target from semantic `u2`, retained10 coordinates, or discriminant support.
- Do not treat beta2 as Q-defined merely because it is V4-fixed.
- Do not reconstruct the rejected q1 route.
- Do not try to derive a column from Picard/proper-Br2 actions alone; the exact input audit already proves those are insufficient without a `mu_2` lift or equivalent glue datum.

## Immediate next action

Recover or construct one equivariant full-surface `mu_2` lift for retained `e2` or `e3`; compute its exact raw `cc/ct` cocycle; project it with `v4_pic2_raw_cocycle_projection.py`; verify the resulting standard 75D column and derive the sibling via the existing J2 relation.

No controller / `MAIN-STATE.json` mathematical promotion has occurred yet. If an exact column is promoted and state sync succeeds, reset this handoff immediately under the reset law.
