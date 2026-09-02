# Stage34 MAIN batch handoff

```text
STATUS=READY_FOR_HOSTILE_AUDIT_TWO_ORBIT_CLOSURE_PREAUDIT
PR=#1482 OPEN
BRANCH=stage34-02b-genus2-rankle1-rationalpoints
LAST_VERIFIED_HEAD_BEFORE_HANDOFF=65c55a34fd235de983e4fc062e322e1b1a5c534b
DO_NOT_MERGE=true
DO_NOT_CREATE_NEW_PR=true
```

## Authority boundary

`MAIN-STATE.json` remains authoritative at **30 residual d1 branches**. This handoff records only unpromoted delta. Do not change 30 -> 26 until a separate hostile audit PASS explicitly promotes the four candidates below.

Still false:

- `D2_all_factor_branches_closed`
- `direct_cover_rational_points_complete`
- `all_multiples_closed`
- `R29_EXT_CHANG_C_closed`
- any parent-route / perfect-cuboid claim

## Unpromoted delta completed in this batch

The previous three rank<=1 unresolved targets have been reduced to two exact sign-orbit representatives and proof-capable preaudit certificates:

- `6b3bcb70c4fda8e6f1e0` (`q=20/99`): unused `U*V*B` genus-two quotient, exact Jacobian rank 0, complete `Chabauty0` pointset, exact four-factor parent pullback, zero nondegenerate full-parent lifts.
- `03f88290bf80ef2e6c98` (`q=60/11`): `Q(i)` degree-two elliptic quotient, exact rank 1, 2-saturation/index check, elliptic Chabauty completeness, exceptional-point handling, exact reverse parent pullback, zero nondegenerate full-parent lifts.

The exact sign involution `T(X:Z)=(-Z:X)` pairs all current 30 branches into 15 orbits and transports parent-square and receiver-degeneracy truth. Relevant partner transfers are:

- `6b3bcb70c4fda8e6f1e0 <-> bb08690eaf9880e595ea`
- `03f88290bf80ef2e6c98 <-> 231e60279b7c5627c085`

Symmetry alone closes zero branches before hostile audit.

## Exact preaudit replay

Verifier:
`stages/stage34/34-02/verify_d2_stageA2_rankle1_two_orbit_preaudit.py`

The verifier was hardened to fail closed on sign-certificate/source-lock SHA mismatch in commit:
`877a19050865a30b74a0581078668db84626886b`.

Lightweight deterministic replay workflow:
`.github/workflows/stage34-02b-d2-rankle1-two-orbit-preaudit.yml`

Run:
- run `33574850326`
- job `100076448307`
- conclusion `success`
- artifact `9826232419`
- uploaded compact artifact size `1740` bytes, retention `1` day

Replay output:

- `sign_source_hash_matches=true`
- `candidate_closed=4`
- projected post-audit residual `26`
- projected by-q: `20/99:6, 24/7:0, 48/55:2, 60/11:6, 80/39:4, 84/13:8`

Generated bundle was frozen into the branch:
`stages/stage34/34-02/d2-stageA2-rankle1-two-orbit-preaudit-bundle.json`

Bundle commit:
`65c55a34fd235de983e4fc062e322e1b1a5c534b`.

## Hostile-audit input working set

Read only the compact bundle first, then expand only the proof layer being challenged:

1. `stages/stage34/34-02/d2-stageA2-rankle1-two-orbit-preaudit-bundle.json`
2. `stages/stage34/34-02/d2-stageA2-rankle1-two-orbit-preaudit-lock.json`
3. `stages/stage34/34-02/d2-stageA2-sign-involution-remaining30-pair-lock.json`
4. `stages/stage34/34-02/d2-stageA2-sign-involution-remaining30-pair-certificate.json`
5. `stages/stage34/34-02/d2-stageA2-6b-uvb-rankzero-proof-certificate.json`
6. `stages/stage34/34-02/d2-stageA2-genus2-rankle1-gaussian-03f-proof-certificate.json`

Hostile audit must independently verify:

- the sign involution theorem and all 15 pair transports, including parent-square and receiver-degeneracy semantics;
- the 6b integral-model normalization, rank-zero/Chabauty0 completeness, and reverse parent lift;
- the 03f `Q(i)` elliptic quotient, fixed free point, 2-saturation/index argument, elliptic Chabauty completeness, exceptional points, and reverse parent lift.

Only after PASS may MAIN promote the four branch IDs
`6b3bcb70c4fda8e6f1e0`, `bb08690eaf9880e595ea`, `03f88290bf80ef2e6c98`, `231e60279b7c5627c085`
and synchronize `MAIN-STATE.json` from 30 to 26.
