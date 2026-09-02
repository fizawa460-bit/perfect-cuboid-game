# Stage34 MAIN batch handoff

```text
STATUS=MAIN_AUDITED_8_BRANCHES_MERGE_CANDIDATE_PENDING_FRESH_HEAD_CHECKS
PR=#1482 OPEN
BRANCH=stage34-02b-genus2-rankle1-rationalpoints
AUTHORITATIVE_REMAINING=8
AUTHORITATIVE_SIGN_ORBITS=4
AUTHORITATIVE_BY_Q={20/99:0,24/7:0,48/55:0,60/11:0,80/39:4,84/13:4}
HOSTILE_REAUDIT_REVIEW=5085277218
AUDITED_HEAD=97af78df799a3ef76caf8833c5f1ac3e0251b51c
MERGE_ALLOWED_FROM_AUDIT_ALONE=false
MERGE_CANDIDATE_AFTER_FRESH_CI_AND_MERGEABILITY=true
```

Hostile re-audit review `5085277218` (`PRR_kwDOTr52Y88AAAABLxssIg`) PASSed exact head `97af78df799a3ef76caf8833c5f1ac3e0251b51c` and authorized both non-overlapping promotions:

- Candidate A: five exact representative sign orbits plus their five already-audited sign partners = `10` branches / `5` sign orbits;
- Candidate B: the two hard q=`20/99` receiver/K-intersection sign orbits = `4` branches / `2` sign orbits.

Applied together to the previous authoritative `22 / 11`, Stage34-02b is now authoritatively **8 d1 branches / 4 sign orbits**, by-q `{20/99:0,24/7:0,48/55:0,60/11:0,80/39:4,84/13:4}`.

Promotion certificate:

`stages/stage34/34-02/d2-stageA2-candidateAB-hostile-reaudit-promotion-certificate.json`

Authoritative state:

`stages/stage34/MAIN-STATE.json`

## Exact remaining four sign orbits

Only these four representative orbits remain OPEN:

- q=`80/39`: `169f94dd000a9c5c053f` ↔ `b870eb75fe3db7bf6a04`;
- q=`84/13`: `40dc8f63e92a8a3a65e8` ↔ `8a374a057daf5f92a87e`;
- q=`84/13`: `7a7ef1a67e794fe1651f` ↔ `98b42307b3aa398f1e0c`;
- q=`80/39`: `99448685b81e29427c3f` ↔ `d4f551f1038c705e3a16`.

These are exactly the generation-2 compute-incomplete representative cases. The bounded retry closed `0/4`; HTTP 504 or missing `PROOF_REPLAY_COMPLETE` is operational incompleteness, not mathematical failure.

Read only:

1. `stages/stage34/34-02/d2-stageA2-candidateAB-hostile-reaudit-promotion-certificate.json`;
2. `stages/stage34/34-02/d2-stageA2-six-rankbound-adapter-generation2-retained-certificate.json`;
3. `stages/stage34/34-02/d2-stageA2-four-rankle1-rationalpoints-retry-lock.json`;
4. `stages/stage34/34-02/d2-stageA2-sign-involution-remaining30-pair-lock.json` only for the already-audited pair map.

## Scope firewall

Candidate B is promoted only as **receiver / Face-3-square intersection exclusion**. It does not assert that its four-factor branches themselves have no rational points.

Still OPEN / false:

- `D2_all_factor_branches_closed`;
- `direct_cover_rational_points_complete`;
- `all_multiples_closed`;
- `R29_EXT_CHANG_C_closed`;
- any parent-route closure;
- any perfect-cuboid existence/nonexistence claim.

## PR #1482 merge gate

The hostile re-audit explicitly did not authorize merge by itself. MAIN has now applied only the authorized A/B promotion and synchronized derived state. The next operation is **fresh CI on the resulting exact head plus fresh PR mergeability**. If both are clean, #1482 is a legitimate merge candidate; do not add unrelated mathematics to this PR before making that decision.
