# Stage32 32-03 multibranch startup

This file is the single authoritative startup/read-order contract for ordinary `stage32mb-mainbatch`. `COMMANDS.md` resolves the command to this entrypoint; `PREFLIGHT.json`, `MISSION.json`, priority/history files, audit receipts, and shared explanatory contracts must not define a competing ordinary startup order.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json` from the live Stage32 MAIN authority surface;
4. `stages/stage32/final-chain/32-03-multibranch/STATE.json`, focusing on the current node, active leaf, `next_obligation`, routing, and credit firewall;
5. only the exact source/evidence paths required by that active leaf.

Do not preload the rest of MB history. In particular, `stages/stage32/COMMANDS.md`, `PREFLIGHT.json`, `MISSION.json`, `PRIORITY-OVERRIDE-20260912.json`, `AGENTS-COMPLIANCE-AUDIT-20260913.md`, `stages/stage32/proof/CROSS-LANE-DEMANDS.json`, and `stages/stage32/proof/CROSS-LANE-STARTUP-CONTRACT.md` are on-demand after command resolution. Read them only when the current MAIN authority or MB `STATE.json` explicitly routes MB through a cross-lane dependency, or when an audit / duplicate-route / reopen question specifically requires them. Research OS files remain on-demand under `AGENTS.md` triggers.

## Authority and drift

Current live `MAIN-STATE.json` is mathematical routing authority. The MB `STATE.json` selects the lane-local retained frontier inside that authority; historical mission/preflight text cannot override it.

If live MAIN identity cannot be resolved, or the lane-local mirror materially disagrees with live authority, fail closed before substantive research. An outstanding hostile-audit FAIL or frozen audit boundary also blocks further substantive retained mathematics until repaired/re-audited; startup cleanup itself grants no mathematical credit.

## Cross-lane routing

Cross-lane registry inspection is not part of ordinary MB startup. Consult `stages/stage32/proof/CROSS-LANE-DEMANDS.json` only when current `MAIN-STATE.json` or MB `STATE.json` explicitly identifies an MB cross-lane dependency, or when a specific audit / duplicate-route / reopen task requires it. When consulted, inspect only the named MB-relevant demand; do not preload or scan the full registry.

Demand status alone never grants receiver, effectivity, theorem, endpoint, closure, or merge credit. Hostile audit, claim synchronization, current-target adapters where applicable, and explicit MAIN consumption/promotion remain separate gates.

## Ownership and anti-loop boundary

MB owns the R29-LG2-MB multibranch final-chain obligations: exact population/normalization semantics, local branch/delta/genus accounting, Aut(S) quotient semantics, justified finite degree/intersection restrictions, and later Picard/effectivity work only after that finite window is proved.

MB does not own FULL178 numerical census/cuts, EX5 Picard64 producer work, consumed V6/O210/Q602 exclusions, unibranch 176/192 caps without a new multibranch proof, dominated EX6 O266 tensor routes, or MAIN promotion/endpoint/merge authority. Do not identify exceptional contact mass, normalization-preimage count, and delta invariant without an exact adapter.

## Execution and audit

`stage32mb-mainbatch` may run in parallel with other Stage32 specialist lanes unless current MAIN routing explicitly assigns the same semantic leaf elsewhere. Ordinary startup does not arm heavy compute.

Use `stage32mb-audit` only for a frozen exact MB audit boundary. MB never self-grants MAIN credit. Do not merge without explicit user authorization.
