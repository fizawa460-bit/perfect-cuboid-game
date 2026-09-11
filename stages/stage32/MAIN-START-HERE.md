# Stage32 MAIN startup

Ordinary `stage32mainbatch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/COMMANDS.md`;
3. `stages/stage32/MAIN-START-HERE.md`;
4. `stages/stage32/MAIN-STATE.json`;
5. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. It does not contain the mutable Stage32 frontier, current target, survivor set, next route, current firewall values, or cleanup progress. Read all such current values only from `MAIN-STATE.json`.

Do not preload the Stage32 root directory, historical roadmaps, controller history, production state, runkeys, audits, or Research OS unless `MAIN-STATE.json`, `AGENTS.md`, or the active task explicitly requires them.

## MAIN role: controller and researcher

Stage32 MAIN is both the integration/frontier coordinator **and a research lane**. It must not be reduced to a passive dispatcher.

MAIN should perform mathematics directly when at least one of the following holds:

1. `MAIN-STATE.json` explicitly routes the current leaf to MAIN;
2. the obligation is genuinely cross-lane, such as an adapter joining specialist results, an integrated same-object/same-member identity, or synthesis required to select the remaining frontier;
3. the obligation is genuinely unowned and must be researched to decide routing or closure.

MAIN should **not** duplicate a sustained vertical leaf that is already owned by an active specialist command. In particular:

- sustained FULL178 numerical census research belongs to `stage32-01-178-mainbatch` unless current MAIN routing explicitly takes it back;
- sustained EX5 Picard64/node-support producer work belongs to `stage32ex5-mainbatch` unless current MAIN routing explicitly takes it back.

MAIN may inspect, validate, adapt, integrate, or consume those specialist results as required. A specialist ownership boundary does not prevent MAIN from doing real research; it prevents two chats from unknowingly attacking the same leaf.

## Historical EX ownership hints

The ownership classes below remain anti-duplication hints, not current routing authority:

- `EX1`: V6 carrier, normalization, singularity, and branch-disposal attacks;
- `EX2`: actual V6 member, complete linear system, fixed/moving decomposition, and member reconstruction;
- `EX3`: O210 cover geometry, cover tower, and monodromy;
- `EX4`: absolute marking, W-line identification, and Q602 residue discrimination;
- `EX5`: receiver breadth / Picard64 producer and materially distinct bypass routes;
- `EX6`: reverse/upper-endpoint O266 attack and endpoint-specific diagnostics.

Ordinary separate EX1-EX4 startup is currently inactive unless Stage32 authority explicitly reopens it. Current routing precedence is:

`explicit current MAIN-STATE routing` > `stages/stage32/COMMANDS.md ownership` > `historical ownership/roadmap text`.

A future ownership change that overrides current routing must be represented in routing authority and, when applicable, synchronized through the existing claim-DAG trigger contract.

## Authority split

`MAIN-STATE.json` is the current mutable ordinary startup projection. It is not a proof certificate and does not rewrite historical evidence.

Exact mathematical claims remain grounded in the hostile-audited certificates and source locks referenced by `MAIN-STATE.json`. Historical controller, production-state, runkey, roadmap, audit, mission, and history files remain evidence or operational history; they are not ordinary current-leaf startup authority merely because they exist.

If historical material conflicts with `MAIN-STATE.json` about current routing, use `MAIN-STATE.json` for ordinary routing and use the exact referenced certificate chain for mathematical claims. Do not infer new mathematical credit from the compact state itself.

## Specialist handoff discipline

When MAIN delegates a sustained vertical leaf to 178 or EX5, record/retain the ownership boundary before running both commands concurrently. The specialist should return a stable retained checkpoint, blocker, or audit handoff. MAIN then consumes it through the required current-target adapter and claim/audit procedure. Do not run MAIN and a specialist independently on the same semantic leaf.

Historical commands `stage32-01-178-a..f` and `stage32ex5-a..h` are not ordinary active fanout. Parallel child dispatch requires an explicit new decomposition and user re-enable decision.

## Search and Arsenal routing

Repository discovery is search-first; never request a recursive/full repository tree. For an existing weapon or evidence lookup, follow the repository discovery policy referenced by `AGENTS.md`, then `docs/arsenal/index.json`, then only the relevant card(s) and exact referenced assets.

A search miss is not repository-wide absence and is not mathematical nonexistence.

## Timeout-safe batch execution

For exploratory or micro-diagnostic Stage32 MAIN work, do not push every narrow experiment directly onto a large shared PR when that push would re-trigger the PR-wide Stage32 workflow set. Prefer a scratch branch or equivalent isolated working branch, keep scratch results non-authoritative, and consolidate only successful retained leaves into the shared PR at an audit-ready checkpoint. Perform freshness synchronization/rebase and broad exact-head CI verification at that consolidation checkpoint rather than after every micro-diagnostic.

## Claim-DAG synchronization trigger

Ordinary `stage32mainbatch` startup remains the startup set above and does not preload Stage32 proof-management files.

When MAIN reaches any `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and complete its on-demand synchronization procedure before treating that checkpoint or downstream credit transition as complete.

Scratch-only diagnostics do not trigger claim-DAG writes. A separate hostile-audit PASS/FAIL receipt does not silently mutate claim authority; any downstream use waits for claim synchronization.

## Write and merge discipline

Before writes, follow the current gate and firewalls in `MAIN-STATE.json`. Proof/source-locked assets must not be deleted or relocated without an explicit reference audit authorized by the current state.

Do not merge without explicit user authorization.
