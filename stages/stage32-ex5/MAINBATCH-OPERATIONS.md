# Stage32EX5 MAINBATCH operations

This file is an operational contract only. It grants no mathematical, FULL178, Stage32 MAIN, N350, receiver, theorem, endpoint, or Perfect Cuboid credit.

## Single active MAINBATCH authority

PR #1765 on `impl/stage32ex5-bc2-12-outer-rank3` is the sole Stage32EX5 MAINBATCH working PR. PR #1764 remains superseded, closed and unmerged. The user has explicitly requested merge priority for PR #1765; therefore the operational goal is closeout and merge, not another research unit.

## Current retained boundary

BC2-24 is retained. The e=4 local exact UNSAT prefix is `0..797`. In the e=8 first block, the retained BC2-24 slice proves 4 new parents UNSAT and leaves `19` retained UNKNOWN / 0 SAT, giving known parent-UNSAT lower bound `7145`; `172` other BC2-19 UNKNOWN identities remain uninferred. This is a checkpoint only, not whole-block or FULL178 closure. N355 remains consumed Stage32 authority and N356 remains deferred/AUDIT_REQUIRED.

## Workflow lifecycle / anti-refire rule

All bounded-unit computation provenance is retained in source, checkpoint, run key and GitHub run ids. The BC2-24 heavy workflow has already completed successfully and is no longer needed as an automatic PR trigger at the merge boundary. Remove that branch-local automatic workflow from the merge surface instead of carrying it into `main`. The permanent Stage32EX5 main integrity gate remains active. Repository workflow lifecycle policy in `AGENTS.md` and `docs/research-os/policies/pr-workflow-trigger-lifecycle.md` remains authoritative.

## Merge-first stop rule

Do not launch BC2-25 or rerun BC2-20..24 on PR #1765. Repair the retained-state schema, synchronize current docs/state, make active integrity/lifecycle gates green, hostile re-audit the exact frozen head, then merge PR #1765. After merge, a new working surface may decide whether BC2-25 is worth opening. UNKNOWN must remain UNKNOWN and no Stage32 MAIN promotion is implied.
