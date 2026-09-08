# Stage32 MAIN scratch — EX1 terminal promotion preflight

Status: scratch only. No EX1 terminal authority, Stage32 MAIN credit, Q602/O210 exclusion, Stage32 closure, or merge.

## Hostile-audit result

PR #1728 remains open / mergeable / non-draft at exact head `0ea608585ee1c747ee5737240671279f6f595612`, based exactly on current main `70265586b3f97be21c7621af73f443311f1f3fa3` with ahead 8 / behind 0. Freshness and exact-head CI are clear/green.

Hostile audit review `5147121377` is **FAIL**.

The three blockers are:

1. **Actual cokernel-coordinate bridge missing.** The independent cellular Smith replay proves the actual pullback cokernel has Smith tail `[2,2,2,4,4]`, but the 6144 assembly replay uses separately hard-coded `PIVROWS/OBS` coordinates. No exact matrix/change-of-basis identity currently proves that those five coordinates are the coordinates in the independently certified actual cokernel.
2. **Immutable claim core contains transient audit state.** The provisional terminal claim puts `PENDING_HOSTILE_AUDIT` semantics into immutable `scope/does_not_prove` fields, so that claim ID cannot cleanly advance to AUDITED without versioning repair.
3. **Retained audit checkpoint and EX1 startup/state disagree.** EX1 `MAIN-STATE.json` still routes the 05H/05I checkpoint while the retained manifest is 05AF terminal, and the audit contract has no exception that authorizes this mismatch.

The strongest supported audited EX1 credit therefore remains `S32.EX1.CANDIDATE_THROUGH_05H.V2` at its intermediate ceiling.

## Future MAIN alignment after repair only

If EX1 repairs all three blockers and a new exact-head hostile re-audit passes, the natural first MAIN target remains

`S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1`

with scope key `S32.MAIN.V6_CARRIER`.

Even then, EX1 does not self-promote. An explicit population-preserving adapter from `S32.EX1.V6_CARRIER` to `S32.MAIN.V6_CARRIER` is still required. O210 and Q602 have separate scope keys and need their own typed consequence adapters rather than automatic promotion.

Even a later audited/promoted V6 nonexistence claim does not itself close Stage32; FULL178 numerical census and final integrated closure/audit obligations remain.

## Current MAIN routing consequence

Do not consume #1728 terminal mathematics, do not promote its provisional all-29-state / `[73,97,235]` exclusion, and do not duplicate EX1's repair work in MAIN. MAIN stays at the existing audited ceiling and can work on independent Stage32 obligations while EX1 repairs the terminal bridge/state package.
