# Stage32 MAIN post-#1728 active-frontier remap audit handoff

Status: **AUDIT READY / NO MERGE AUTHORIZATION**.

This checkpoint consumes already hostile-audited and merged #1728 MAIN-scope authority `S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2` and remaps the active frontier. It grants no new hostile-audit credit itself.

## Already audited input

- EX1 terminal V2: PASS review `5147627146`, exact head `e3c4a04d5010e6dca9428722e334890e2614297a`.
- EX1 -> MAIN carrier population adapter: PASS review `5147810198`, exact head `89ba026f05f9fe5344c0f0fb41fe8c2366032877`.
- MAIN V6 negative V2: AUDITED under review `5147810198`.
- #1728 merge commit: `56ce8213ffe90635aaa499c46639971c952724f1`.

## Remap

Former V6 actual-member, old V6 negative V1, multibranch, smooth-singularity, absolute-marking, and same-member-Q602 nodes are removed from the **active** frontier because the stronger whole V6 genus-1 population is audited empty. This does not claim those old local/marking statements were independently proved.

Remaining active nodes are exactly:

1. `S32.O210.EXCLUSION.V1`
2. `S32.Q602.SURVIVORS_73_97_235.V1`
3. `S32.Q602.EXCLUSION.V1`
4. `S32.FULL178.NUMERICAL_CENSUS.V1`
5. `S32.GOAL.STAGE32_CLOSURE.V1`

EX routing becomes:

- EX1 completed audited handoff;
- EX2 dominated by audited V6 nonexistence;
- EX3 O210/Q602 alternative pending population adapter;
- EX4 Q602 alternative pending population adapter;
- EX5 active FULL178;
- EX6 stopped.

The ordinary lane routing states are synchronized with this map: `stage32-ex1/MAIN-STATE.json` now reports `COMPLETED_AUDITED_HANDOFF`, and `stage32-ex2/MAIN-STATE.json` reports `DOMINATED_BY_AUDITED_V6_NONEXISTENCE`. Their lane verifiers enforce the stop/re-entry semantics, and the active-frontier verifier checks that inactive lane-adapter status agrees with each ordinary `MAIN-STATE.json`.

## Explicit firewalls

- `V6 genus-1 population empty = true` from already audited authority.
- `O210_excluded = false` pending an explicit typed audited V6-empty -> O210 adapter.
- `Q602_excluded = false` pending a separate typed audited V6-empty -> Q602 population-preserving adapter.
- `[73,97,235]` remains historical audited survivor data and is not rewritten as residue-specific exclusion.
- `FULL178 complete = false`.
- `Stage32 closed = false`.
- no Perfect Cuboid endpoint claim.
- no merge authorization.

## Management change requiring hostile scrutiny

`MAIN-STATE.json` files are mutable routing authority and older claims source-lock pre-remap routing blobs. The claim-DAG wrapper is narrowed so an exact historical `*/MAIN-STATE.json` blob may be supplied from `proof/historical-routing-blobs/<sha>.json` for AUDITED as well as DECLARED_GOAL/SUPERSEDED/REVOKED claims. This exception applies only to routing-state files; all non-routing source evidence remains strict working-tree locked, and PROVISIONAL/SCRATCH routing locks remain strict.

Exact historical routing blobs are retained for MAIN, EX1, and EX2 before their post-#1728 state changes. Hostile audit should explicitly check this routing-snapshot policy and confirm it does not weaken mathematical evidence locking.
