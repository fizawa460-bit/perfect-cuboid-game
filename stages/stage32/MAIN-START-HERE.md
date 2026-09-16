# Stage32 MAIN startup

This file is the single authoritative startup/read-order contract for ordinary `stage32mainbatch` operation. `COMMANDS.md`, `README.md`, historical roadmaps/controllers, audit receipts, and specialist mission files must not define a competing MAIN startup order.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json` from the active Stage32 MAIN authority surface;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json` from that same authority surface;
5. `stages/stage32/proof/ACTIVE-SPECIALIST-MONITOR-CONTRACT.json`, then perform its required **live specialist sweep** before substantive MAIN research;
6. only paths in `MAIN-STATE.json.current_leaf_working_set`, exact coordination paths required by applicable `OPEN` demands, and synthesis boundaries explicitly named by those demands;
7. only exact source/evidence paths referenced by the selected state, demand, live specialist observation, or synthesis boundary.

`stages/stage32/COMMANDS.md` is the stable registry used to resolve `stage32mainbatch` to this entrypoint; once resolved, it is **not a second MAIN startup contract** and need not be re-read as startup payload. `stages/stage32/README.md` is a layout map only.

Do not preload the Stage32 root, historical roadmaps/controllers, production state, runkeys, audits, claim DAG, Research OS, Arsenal, or specialist mission history merely because those files exist. The mandatory live specialist sweep is deliberately bounded: inspect only the active specialist surfaces enumerated by `ACTIVE-SPECIALIST-MONITOR-CONTRACT.json`, their live startup/current-state boundary, and the exact retained/audit/handoff paths needed to answer the monitor fields.

## Mandatory live specialist sweep

Every ordinary `stage32mainbatch` startup must resolve the **live** current surface for each active specialist listed in `ACTIVE-SPECIALIST-MONITOR-CONTRACT.json` and record, at minimum, the following before MAIN begins new substantive mathematics:

- live PR or active surface and live head;
- current state or exact retained boundary;
- latest retained result;
- current hostile-audit gate/status;
- pending handoff to MAIN or another lane, or explicit `NONE`;
- current-main freshness signal;
- semantic leaf currently being attacked.

The contract's recorded PR numbers are discovery hints, not authority snapshots. Never treat an old head recorded in the monitor contract, PR body, historical receipt, or local branch mirror as live without resolving it again. If an active specialist cannot be resolved, its current retained boundary is ambiguous, a relevant retained/audit-pending result has no explicit MAIN disposition, or two active surfaces silently attack the same semantic leaf, fail closed before new MAIN research and repair the routing/monitor record first.

A specialist may be mathematically independent of MAIN's current leaf and still must appear in the sweep. `32-02` and CERTLIFT remain on-demand and are not promoted to ordinary active specialists merely by being open or retained.

`32-02` is explicitly **PARKED / INCOMPLETE**. If the user asks to resume it with language such as `32-02の研究途中から開始して`, `32-02を途中から再開`, or an equivalent explicit reopen request, open `stages/stage32/final-chain/32-02-effectivity/SCALAR-PRODUCER-RESEARCH-HANDOFF.md` first and resume from its retained #1790 boundary rather than restarting the scalar-producer research from scratch. This routing note grants no MAIN/effectivity/FULL178/theorem credit by itself.

Run:

`python stages/stage32/proof/verify_cross_lane_demands.py`

The verifier checks the retained wiring/monitor contract. The operator/agent is still responsible for resolving live PR heads and live lane state on every startup; a retained verifier cannot prove a remote PR head has not advanced.

## MAIN-STATE live-observation writeback

`stage32mainbatch` is the sole ordinary owner of `stages/stage32/MAIN-STATE.json`. Specialist lanes must update their own lane state, retained evidence, PR, and audit surfaces; they must not write MAIN's `MAIN-STATE.json` merely to advertise progress.

Whenever `stage32mainbatch` resolves specialist information newer than the observation currently recorded in `MAIN-STATE.json`, it must write that newer observation back to `MAIN-STATE.json` on the active Stage32 MAIN branch before the batch stops. At minimum, every newer specialist head, audit status/review, retained-result status, MAIN-handoff status, blocking reason, and semantic leaf that MAIN relied upon during the batch must be reflected in the existing MAIN-state observation surface. Do not create a second live-snapshot/state file for this purpose.

This writeback is **observational synchronization only**. It must not by itself change authoritative remaining strata/terminals, pruning credit, theorem/effectivity/receiver/route/endpoint credit, Stage32 closure, or merge authorization. Those authority fields may change only through the separately required audited MAIN transition and applicable claim-sync/promotion gates. If updating the mutable MAIN projection requires refreshing its own verifier/source-lock metadata, perform that maintenance in the same MAIN batch rather than leaving a deliberately stale specialist observation in `MAIN-STATE.json`.

Before an ordinary `stage32mainbatch` stops, it must therefore satisfy both conditions: (1) all mathematical/authority changes obey their normal audit gates, and (2) `MAIN-STATE.json` is not knowingly stale with respect to any newer specialist state actually resolved and relied upon during that run.

## Authority and routing

`MAIN-STATE.json` is the current mutable ordinary-startup projection, not a proof certificate. Exact mathematical claims remain grounded in the audited certificates and source locks referenced by that state. `CROSS-LANE-DEMANDS.json` is operational dependency authority and cannot grant mathematical credit.

Routing precedence is:

`explicit current MAIN-STATE routing` > `higher-priority applicable OPEN demand` > stable ownership in `COMMANDS.md` > historical roadmap/ownership text.

If a live/current authority identity cannot be resolved safely, or a branch-local mirror conflicts with the live authority being consumed, fail closed rather than research from an uncertain boundary.

## MAIN role and anti-duplication boundary

MAIN is both controller/integrator and a research lane. It performs mathematics directly when current state routes the leaf to MAIN, when the obligation is genuinely cross-lane, or when the work is genuinely unowned. Silent duplicate ownership remains prohibited, but an **explicitly requested independent parallel attack** on a specialist-owned semantic leaf is permitted when it is clearly labeled as an independent MAIN route, source-locks the exact specialist or shared inputs it consumes, does not mutate specialist state, and keeps all overlap/double-charge accounting explicit. Independent reproduction or a distinct attack may validate, strengthen, or contradict specialist work; it does not inherit or duplicate mathematical credit automatically.

Stable specialist split: `stage32-01-178-mainbatch` owns sustained concrete FULL178 census/incidence/transport/completeness work; `stage32ex5-mainbatch` owns sustained Picard64/node-support producer/refinement work; `stage32cut-mainbatch` owns direct infeasibility/obstruction work on exact producer interfaces; `stage32mb-mainbatch` owns sustained 32-03 multibranch work. MAIN may inspect, validate, adapt, integrate, consume, explicitly reassign, or—under the explicit independent-parallel rule above—independently re-attack those results. Separate surfaces must never silently double-charge the same restriction, saving, rejected population, or promotion credit.

Historical EX hints remain anti-duplication hints only: EX1 = V6 carrier/normalization/singularity/branch disposal; EX2 = actual V6 member/linear-system/decomposition/reconstruction; EX3 = O210 cover/monodromy; EX4 = absolute marking/W-line/Q602 residue; EX6 = O266 endpoint diagnostics. EX1-EX4/EX6 are inactive unless current authority explicitly reopens them; EX5's active role is defined above and in `COMMANDS.md`.

A specialist handoff returns a retained checkpoint, blocker, or audit handoff; MAIN consumes it only through the required source/target adapter, claim synchronization, audit, and promotion gates. Historical child fanouts such as `stage32-01-178-a..f` and `stage32ex5-a..h` do not reactivate without an explicit new decomposition/reassignment.

## Cross-lane demand monitor

Before substantive work, MAIN inspects all applicable `OPEN` demands. The historical P0 route `S32.DEMAND.N398.178.MAIN.PARITY_SYNTHESIS.V1` is now `OBSOLETE`: hostile-audited N400 materialized a strictly later compact consumer handoff and superseded that re-entry blocker. The replacement demand `S32.DEMAND.N400.178.MAIN.COMPACT_CONSUMPTION.V1` is `SATISFIED` by audit review `5203374607` at exact producer head `b1a950cbc6edf3cb85e1ea79473105c6f1f67b03`.

`stages/stage32/proof/PICARD64-PARITY-CROSS-LANE-SYNTHESIS-V1.json` is retained as a superseded comparison boundary. Its N398/GRF-09/EX5 cross-population and coordinate equivalences remain `NOT_PROVED`; none is used to justify N400 consumption. N400 instead source-locks the hostile-audited N399 exact predicate and hostile-audited N397 no-double-charge accounting on the retained 97-block / 10,961-terminal population.

V25 MAIN consumed exactly 5,502 terminals once, with prior consumed overlap `0` and `double_charge=false`; the 178 producer lane performed no MAIN authority subtraction. The resulting replacement head `f80b2c87979a980716c9fa3c9b2649f168e0fff8` received exact-head hostile-audit PASS, recorded as review `5204417753`, with merge-ready freshness `CLEAR` at current main `117310b6a9d40273683cab8c08cc9e5e0cc584d9`. V26 synchronizes that audit metadata only: it adds no pruning beyond the already-consumed 5,502 terminals, leaves FULL178 `ACTIVE_INCOMPLETE`, authorizes no heavy computation or merge, and resumes the bounded route `FULL178_THEN_EFFECTIVITY_MULTIBRANCH_AND_FINAL_SYNTHESIS` subject to the mandatory live specialist sweep.

Shared producer/consumer/re-entry semantics live in `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md`; that prose is an **on-demand reference**, not another mandatory startup read. `SATISFIED` by itself never grants pruning, receiver, effectivity, theorem, endpoint, closure, or merge credit.

## On-demand transitions and execution

When MAIN reaches `RETAINED_CONSOLIDATION`, `AUTHORITY_OR_AUDIT_TRANSITION`, `EX_TO_MAIN_PROMOTION`, `ACTIVE_FRONTIER_REMAP`, or `FINAL_MILESTONE_TRANSITION`, open `stages/stage32/proof/CLAIM-SYNC-CONTRACT.md` and complete its on-demand synchronization procedure before consuming the transition. Scratch-only diagnostics and demand-status changes do not themselves trigger claim-credit writes.

Repository discovery, Research OS triggers, workflow lifecycle, and heavy/artifact-producing authorization are governed by `AGENTS.md`; this file does not restate those policies. Keep micro-diagnostics scratch/non-authoritative when pushing each experiment to the shared PR would create avoidable PR-wide reruns, and consolidate retained work at an audit-ready checkpoint.

## Write and merge discipline

Before writes, obey current gates/firewalls in `MAIN-STATE.json`. Do not delete or relocate proof/source-locked assets without the required reference audit. Do not merge without explicit user authorization.