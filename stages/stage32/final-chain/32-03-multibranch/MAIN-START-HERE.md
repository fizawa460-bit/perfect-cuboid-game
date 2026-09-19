# Stage32 32-03 multibranch startup

This file is the single authoritative startup/read-order contract for ordinary `stage32mb-mainbatch`. `COMMANDS.md` resolves the command to this entrypoint; `PREFLIGHT.json`, `MISSION.json`, priority/history files, audit receipts, and shared explanatory contracts must not define a competing ordinary startup order.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json` from the live Stage32 MAIN authority surface;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json` from that same live authority surface;
5. `stages/stage32/final-chain/32-03-multibranch/STATE.json`, focusing on the current node, active leaf, `next_obligation`, routing, and credit firewall;
6. only the exact source/evidence paths required by that active leaf or by an applicable demand.

Do not preload the rest of MB history. In particular, `stages/stage32/COMMANDS.md`, `PREFLIGHT.json`, `MISSION.json`, `PRIORITY-OVERRIDE-20260912.json`, `AGENTS-COMPLIANCE-AUDIT-20260913.md`, and `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md` are on-demand after command resolution. Read them only when the current authority, active leaf, audit task, or duplicate-route/reopen question explicitly requires them. Research OS files remain on-demand under `AGENTS.md` triggers.

## Active PR / audit target resolution

For both `stage32mb-mainbatch` and `stage32mb-audit`, the current MB surface is selected by
`stages/stage32/final-chain/32-03-multibranch/STATE.json -> active_surface`.

Rules:

- if `active_surface.pr_number` is OPEN, both commands MUST use that PR and its branch as the current MB surface;
- a closed/superseded predecessor PR is archive-only and MUST NOT be selected as the current mainbatch or audit target;
- a hostile-audit PASS applies only to its recorded exact head; later commits do not inherit PASS;
- if the current active PR head is later than `routing.latest_audited_exact_head` and `routing.current_head_reaudit_required=true`, ordinary retained research and heavy execution fail closed until that current head receives hostile-audit PASS;
- if more than one OPEN PR claims to be the active MB surface, stop as a routing conflict rather than choosing heuristically.

Current routing is intentionally encoded in STATE rather than this startup file so PR/head changes do not create a competing authority.

## Authority and drift

Current live `MAIN-STATE.json` is mathematical routing authority. `CROSS-LANE-DEMANDS.json` controls operational priority only. The MB `STATE.json` selects the lane-local retained frontier inside that authority; historical mission/preflight text cannot override it.

If live MAIN identity cannot be resolved, or the lane-local mirror materially disagrees with live authority, fail closed before substantive research. An outstanding hostile-audit FAIL or frozen audit boundary also blocks further substantive retained mathematics until repaired/re-audited; startup cleanup itself grants no mathematical credit.

## Cross-lane routing

Inspect only demands involving lane `MB`. A higher-priority OPEN demand where MB is producer preempts lower-priority local work. If MB is consumer of an OPEN demand, wait rather than duplicate producer mathematics. For SATISFIED re-entry, validate the satisfying artifact identity and source-population semantics before use. Do not preload unrelated demand artifacts.

Demand SATISFIED does not grant mathematical credit. Demand status never grants receiver, effectivity, theorem, endpoint, closure, or merge credit. Hostile audit, claim synchronization, current-target adapters where applicable, and explicit MAIN consumption/promotion remain separate gates.

## Ownership and anti-loop boundary

MB owns the R29-LG2-MB multibranch final-chain obligations: exact population/normalization semantics, local branch/delta/genus accounting, Aut(S) quotient semantics, justified finite degree/intersection restrictions, and later Picard/effectivity work only after that finite window is proved.

MB does not own FULL178 numerical census/cuts, EX5 Picard64 producer work, consumed V6/O210/Q602 exclusions, unibranch 176/192 caps without a new multibranch proof, dominated EX6 O266 tensor routes, or MAIN promotion/endpoint/merge authority. Do not identify exceptional contact mass, normalization-preimage count, and delta invariant without an exact adapter.

## Execution and audit

`stage32mb-mainbatch` may run in parallel with other Stage32 specialist lanes unless current MAIN routing or a higher-priority demand assigns the same semantic leaf elsewhere. Ordinary startup does not arm heavy compute.

Use `stage32mb-audit` only for a frozen exact MB audit boundary. MB never self-grants MAIN credit. Do not merge without explicit user authorization.
