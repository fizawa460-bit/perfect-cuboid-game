# Stage32 MAIN startup

Ordinary `Stage32-main-batch` reads, in this order:

1. `AGENTS.md`;
2. `stages/stage32/MAIN-START-HERE.md`;
3. `stages/stage32/MAIN-STATE.json`;
4. only the paths listed in `MAIN-STATE.json.current_leaf_working_set`.

This file is the fixed ordinary startup contract. It does not contain the mutable Stage32 frontier, current target, survivor set, next route, current firewall values, or cleanup progress. Read all such current values only from `MAIN-STATE.json`.

Do not preload the Stage32 root directory, historical roadmaps, controller history, production state, runkeys, audits, or Research OS unless `MAIN-STATE.json`, `AGENTS.md`, or the active task explicitly requires them.

## MAIN role and EX ownership

Stage32 MAIN is the integration/frontier-coordination lane and should not become a generic extra vertical attack lane by default.

The ownership classes below are **default anti-duplication routing hints**, not a replacement routing authority. Explicit current routing in `MAIN-STATE.json` remains authoritative for ordinary MAIN startup. If `MAIN-STATE.json` explicitly assigns a current MAIN route that overlaps one of these classes, MAIN follows that exact route until routing is changed through the existing state/claim-sync process; the ownership table alone must not silently reroute or suppress it.

Default ownership classes are:

- `EX1`: V6 carrier, normalization, singularity, and branch-disposal attacks;
- `EX2`: actual V6 member, complete linear system, fixed/moving decomposition, and member reconstruction;
- `EX3`: O210 cover geometry, cover tower, and monodromy;
- `EX4`: absolute marking, W-line identification, and Q602 residue discrimination;
- `EX5`: receiver breadth, materially distinct bypass routes, and independent weapon qualification;
- `EX6`: reverse/upper-endpoint O266 attack and endpoint-specific diagnostics.

The exact live status of an EX lane is mutable and is not duplicated here. When ownership is clear but current lane status matters, inspect only that EX lane's startup/state on demand rather than preloading all EX state.

Before starting a new MAIN mathematical leaf that is **not already explicitly routed by current `MAIN-STATE.json`**, classify the obligation:

1. If it is semantically owned by an EX lane, MAIN should route the work to that EX lane or consume its retained/audited result when authorized rather than creating a duplicate attack.
2. MAIN may perform mathematics when the obligation is genuinely cross-lane: an adapter joining results from multiple EX lanes, an integrated same-object/same-member identity, an unowned bridge required by more than one lane, or a synthesis needed to decide the remaining Stage32 frontier.
3. MAIN may perform consolidation, claim/frontier integration, authority routing, and `CLOSED` / `CURRENT_THEORY_BLOCKED` synthesis without creating a duplicate EX attack.
4. If a new unowned MAIN scratch obligation develops into a sustained vertical research program, propose/perform the existing explicit routing or `ACTIVE_FRONTIER_REMAP` procedure before treating EX ownership as changed. Do not silently change routing authority from this table alone.

Precedence is therefore:

`explicit current MAIN-STATE routing` > `default anti-duplication ownership hint`.

A future ownership change that is intended to override current routing must be represented in the routing authority and, when applicable, synchronized through the existing claim-DAG trigger contract.

This role split grants no mathematical credit, does not promote any EX result, does not change the active frontier by itself, and does not authorize merge.

## Authority split

`MAIN-STATE.json` is the current mutable ordinary startup projection. It is not a proof certificate and does not rewrite historical evidence.

Exact mathematical claims remain grounded in the hostile-audited certificates and source locks referenced by `MAIN-STATE.json`. Historical controller, production-state, runkey, roadmap, audit, and history files remain evidence or operational history; they are not ordinary current-leaf startup authority merely because they exist.

If historical material conflicts with `MAIN-STATE.json` about current routing, use `MAIN-STATE.json` for ordinary routing and use the exact referenced certificate chain for mathematical claims. Do not infer new mathematical credit from the compact state itself.

## Search and Arsenal routing

Repository discovery is search-first; never request a recursive/full repository tree. For an existing weapon or evidence lookup, follow the repository discovery policy referenced by `AGENTS.md`, then `docs/arsenal/index.json`, then only the relevant card(s) and exact referenced assets.

A search miss is not repository-wide absence and is not mathematical nonexistence.

## On-demand history

Historical Stage32 files may be opened only when the current state or active task requires their exact semantics, provenance, heavy-workflow history, source lock, audit record, or cleanup-reference analysis. Their presence does not authorize heavy compute or change current credit.

## Timeout-safe batch execution

For exploratory or micro-diagnostic Stage32 MAIN work, do not push every narrow experiment directly onto a large shared PR when that push would re-trigger the PR-wide Stage32 workflow set. Prefer a scratch branch or equivalent isolated working branch, keep scratch results non-authoritative, and consolidate only successful retained leaves into the shared PR at an audit-ready checkpoint. Perform freshness synchronization/rebase and broad exact-head CI verification at that consolidation checkpoint rather than after every micro-diagnostic. This execution rule changes workflow cadence only; it does not weaken source locks, credit firewalls, hostile-audit requirements, or merge gates.

## Claim-DAG synchronization trigger

Ordinary `stage32main batch` startup remains exactly the four-item startup set above and does not preload Stage32 proof-management files.

When MAIN reaches any `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and complete its on-demand synchronization procedure before treating that checkpoint or downstream credit transition as complete.

Scratch-only diagnostics do not trigger claim-DAG writes. A separate hostile-audit PASS/FAIL receipt does not silently mutate claim authority; any downstream use waits for claim synchronization.

## Write and merge discipline

Before writes, follow the current gate and firewalls in `MAIN-STATE.json`. Proof/source-locked assets must not be deleted or relocated without an explicit reference audit authorized by the current state.

Do not merge without explicit user authorization.
