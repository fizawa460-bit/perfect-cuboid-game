# Stage32 MAIN startup

This file is the single authoritative startup/read-order contract for ordinary `stage32mainbatch` operation. `COMMANDS.md`, `README.md`, historical roadmaps/controllers, audit receipts, and specialist mission files must not define a competing MAIN startup order.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json` from the active Stage32 MAIN authority surface;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json` from that same authority surface;
5. only paths in `MAIN-STATE.json.current_leaf_working_set` plus exact coordination paths required by applicable `OPEN` demands;
6. only exact source/evidence paths referenced by that selected state or demand.

`stages/stage32/COMMANDS.md` is the stable registry used to resolve `stage32mainbatch` to this entrypoint; once resolved, it is **not a second MAIN startup contract** and need not be re-read as startup payload. `stages/stage32/README.md` is a layout map only.

Do not preload the Stage32 root, historical roadmaps/controllers, production state, runkeys, audits, claim DAG, Research OS, Arsenal, or specialist mission history merely because those files exist. Open them only when current state/demand, `AGENTS.md`, or the active task triggers them.

## Authority and routing

`MAIN-STATE.json` is the current mutable ordinary-startup projection, not a proof certificate. Exact mathematical claims remain grounded in the audited certificates and source locks referenced by that state. `CROSS-LANE-DEMANDS.json` is operational dependency authority and cannot grant mathematical credit.

Routing precedence is:

`explicit current MAIN-STATE routing` > `higher-priority applicable OPEN demand` > stable ownership in `COMMANDS.md` > historical roadmap/ownership text.

If a live/current authority identity cannot be resolved safely, or a branch-local mirror conflicts with the live authority being consumed, fail closed rather than research from an uncertain boundary.

## MAIN role and anti-duplication boundary

MAIN is both controller/integrator and a research lane. It performs mathematics directly when current state routes the leaf to MAIN, when the obligation is genuinely cross-lane, or when the work is genuinely unowned. It must not independently attack a sustained semantic leaf already owned by an active specialist.

Stable specialist split: `stage32-01-178-mainbatch` owns sustained concrete FULL178 census/incidence/transport/completeness work; `stage32ex5-mainbatch` owns sustained Picard64/node-support producer/refinement work; `stage32cut-mainbatch` owns direct infeasibility/obstruction work on exact producer interfaces; `stage32mb-mainbatch` owns sustained 32-03 multibranch work. MAIN may inspect, validate, adapt, integrate, consume, or explicitly reassign those results, but two surfaces must not silently research the same semantic leaf.

Historical EX hints remain anti-duplication hints only: EX1 = V6 carrier/normalization/singularity/branch disposal; EX2 = actual V6 member/linear-system/decomposition/reconstruction; EX3 = O210 cover/monodromy; EX4 = absolute marking/W-line/Q602 residue; EX6 = O266 endpoint diagnostics. EX1-EX4/EX6 are inactive unless current authority explicitly reopens them; EX5's active role is defined above and in `COMMANDS.md`.

A specialist handoff returns a retained checkpoint, blocker, or audit handoff; MAIN consumes it only through the required source/target adapter, claim synchronization, audit, and promotion gates. Historical child fanouts such as `stage32-01-178-a..f` and `stage32ex5-a..h` do not reactivate without an explicit new decomposition/reassignment.

## Cross-lane demand monitor

Before substantive work, MAIN inspects all applicable `OPEN` demands and runs:

`python stages/stage32/proof/verify_cross_lane_demands.py`

Shared producer/consumer/re-entry semantics live in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`; that prose is an **on-demand reference**, not another mandatory startup read. `SATISFIED` means an operational artifact exists; it does not grant pruning, receiver, effectivity, theorem, endpoint, closure, or merge credit.

## On-demand transitions and execution

When MAIN reaches `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and complete its on-demand synchronization procedure before consuming the transition. Scratch-only diagnostics and demand-status changes do not themselves trigger claim-credit writes.

Repository discovery, Research OS triggers, workflow lifecycle, and heavy/artifact-producing authorization are governed by `AGENTS.md`; this file does not restate those policies. Keep micro-diagnostics scratch/non-authoritative when pushing each experiment to the shared PR would create avoidable PR-wide reruns, and consolidate retained work at an audit-ready checkpoint.

## Write and merge discipline

Before writes, obey current gates/firewalls in `MAIN-STATE.json`. Do not delete or relocate proof/source-locked assets without the required reference audit. Do not merge without explicit user authorization.
