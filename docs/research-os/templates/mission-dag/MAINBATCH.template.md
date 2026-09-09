# __MISSION__ MAINBATCH

This file is the reusable execution contract for a Mission DAG research project.

## Ordinary startup

Read only:

1. repository `AGENTS.md`;
2. this mission's `MISSION.json`;
3. `STATE.json` for the currently derived READY frontier nodes;
4. exact source/evidence paths referenced by those nodes.

Do not preload unrelated Stage history, other missions, all Research OS policies, or large retained payloads.

## One batch

1. Verify mission structure with `verify_mission.py`.
2. Derive READY frontier: node status is `OPEN` and every dependency is `DONE`.
3. For each selected READY node, perform search-before-create/reuse checking before inventing a new subnode or route.
4. If an equivalent result exists, bind it explicitly and mark the route/node `EQUIVALENT` or `SUPERSEDED` as appropriate; do not redo the work.
5. Execute bounded, materially distinct work on at most `max_parallel` READY nodes.
6. On failure, freeze a stable `route_id`, exact blocker, and reopen condition. Do not retry that route until the reopen condition becomes true.
7. If the same receiver keeps surviving, multiple distinct routes block, or parking/exhaustion is being considered, invoke `docs/research-os/policies/cycle-exploration-safety-protocol.md` on demand.
8. Retain only outputs with exact scope, assumptions, evidence/replay paths, and credit ceiling.
9. Update node states first, then mission node statuses/dependencies. Recompute the frontier; never hand-edit a cached frontier file.
10. Stop at a coherent checkpoint. Do not merge and do not self-grant hostile-audit credit.

## Node creation rule

Before adding a node:

- search current mission `semantic_key`, title, statement terms, and retained results;
- search relevant repository asset indices when existing evidence/weapon reuse is plausible;
- record the reuse queries/decision in the node;
- use a new `semantic_key` only for a materially distinct obligation.

Different coordinates, notation, or implementation language are not by themselves distinct research nodes.

## Decomposition rule

Decompose a node only when doing so exposes independently checkable obligations or removes context/wall-clock risk. Do not split for the sake of filling all parallel slots.

Child nodes inherit no theorem credit from their parent. Parent closure requires its declared child dependencies plus its own closure condition.

## Human contract

The human operator may simply repeat `__MISSION__-mainbatch`. The agent is responsible for DAG maintenance, reuse search, anti-loop bookkeeping, route broadening triggers, and deciding whether parallelism is justified.
