# Stage34 MAIN batch handoff

```text
STATUS=PAUSED_BY_USER
PR=#1480 OPEN
BRANCH=stage34-02-sequence-classification-theorem-funnel
LAST_VERIFIED_HEAD_BEFORE_HANDOFF=2f73781d73f7f0f8e990f9fa5bd140586fa0cee3
DO_NOT_MERGE=true
DO_NOT_CREATE_NEW_PR=true
```

## Authoritative current state

`MAIN-STATE.json` is already synchronized to schema
`STAGE34_EXT_C_MAIN_STATE_V15_D2_STAGEA2_44_BRANCHES_AFTER_GENUS2_RANKZERO_CLOSURE`.
Do not reconstruct current mathematics from this handoff when `MAIN-STATE.json` is available; this file only preserves the stop-point delta and resume instructions.

Current exact residual count is **44 d1 branches**. Receiver `R29-EXT-CHANG-C` remains OPEN.
No parent-route / endpoint / perfect-cuboid closure is claimed.

Durable reduction chain now locked in `MAIN-STATE.json`:

- StageA2 factor descent: `92` exact d1 branches, d2 closed.
- rank-zero elliptic `A*B` quotient complete pointsets + exact pullback: `92 -> 76` (16 closed).
- selected rank-one elliptic quotient full-MW congruence sieve: `76 -> 52` (24 closed).
- residual triple-product genus-two diagnostic: `52 * 4 = 208` quotient conditions and **208 distinct exact sextic models**; there is no exact-model reuse/compression across branches.
- branch-minimal genus-two RankBounds census resolved 33/52 with histogram `{(0,0):8,(0,1):14,(0,2):8,(1,1):3}`; 19 external responses remained unresolved in that census.
- dedicated exact genus-two rank-zero closure replay: all 8 rank-zero quotient curves had complete six-point `Chabauty0` sets and every point failed the exact four-factor parent lift / mapped only to receiver-excluded torsion/origin; exactly 8 parent branches closed.
- current residual: `52 -> 44`.
- current 44 partition: 17 branches already have a selected genus-two quotient with certified rank upper bound <=1; 8 have selected bound `(0,2)`; 19 had unresolved external RankBounds response.

## Current exact leaf

`D2_STAGEA2_GENUS2_RANK_UPPER_LE_1_RATIONALPOINTSGENUS2_17_BRANCH_DIAGNOSTIC`

Reason: Magma 2.29 `RationalPointsGenus2` is being tested only on the 17 selected quotient curves with certified rank upper bound <=1. Any returned pointset must still be checked by the exact four-factor parent-lift condition before branch closure credit.

At the stop snapshot, Actions run `33561056094` (`Stage34-02 D2 StageA2 genus-two rank<=1 RationalPoints probe`) was **in_progress**. Do not assume success or mathematical credit from that run. On resume, fresh-check the run/job/artifact before any further write.

Current working set from `MAIN-STATE.json`:

- `stages/stage34/34-02/d2-stageA2-genus2-rankzero-closure-certificate.json`
- `stages/stage34/34-02/d2-stageA2-genus2-rankle1-rationalpoints-lock.json`
- `stages/stage34/34-02/probe_d2_stageA2_genus2_rankle1_rationalpoints.py`
- `stages/stage34/34-02/probe_d2_stageA2_triple_quotient_models.py`

## Stop-point provenance

Useful commits on the path to the current state:

- `caf2437da6cf283e40e295c6e2ab7073ee5f09fe` — add residual genus-two triple quotient probe.
- `39384dc46c34b946c2b1532cd26d0f2147f6460b` — seven-q genus-two `RankBounds` smoke script.
- `b8824257ba382bf5c4d582cac499b6055a9fbfad` — smoke workflow.
- `33323a8e634d49c9f5560c33773b5d45dd009621` — persist exact eight-branch genus-two closure certificate.
- `4e4342204952a7220053ae4b56dd6e47d6d1ff93` — sync MAIN state to 44 branches.
- `2f73781d73f7f0f8e990f9fa5bd140586fa0cee3` — arm 17-curve genus-two rank<=1 `RationalPoints` probe.

Diagnostic triple-quotient run `33559532976`, job `100028416415`, artifact `9820684312` established 208 conditions = 208 exact sextic models. This diagnostic alone grants no parent closure.

## Resume protocol

1. Fresh-check PR #1480 is OPEN and branch head.
2. Read only `AGENTS.md`, `MAIN-START-HERE.md`, `MAIN-STATE.json`, this handoff, then the current-leaf working set.
3. Inspect run `33561056094` first. If it finished, validate completeness semantics and exact parent-lift filtering before promotion.
4. Do not rerun or reopen the already certified 8 genus-two rank-zero closures without contradictory evidence.
5. Do not launch all 208 genus-two models blindly; exact-model compression is zero and the current strategy is branch-minimal targeted completeness.
6. Preserve firewalls: rank bounds, local/congruence survivors, quotient rational points, or successful CAS execution alone do not close a parent branch or receiver.

## Firewalls at pause

- `D2_all_factor_branches_closed=false`
- `direct_cover_rational_points_complete=false`
- `all_multiples_closed=false`
- `R29_EXT_CHANG_C_closed=false`
- no perfect-cuboid existence/nonexistence claim
