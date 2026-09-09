# __MISSION__ MAINBATCH

This file is the reusable execution contract for a Mission DAG research project.

## Ordinary startup

Read only:

1. repository `AGENTS.md`;
2. this mission's `MISSION.json`;
3. `STATE.json` for the currently derived READY frontier nodes;
4. exact source/evidence paths referenced by those nodes.

Do not preload unrelated Stage history, other missions, all Research OS policies, or large retained payloads.

## Startup dispatch

After structural verification and READY-frontier derivation:

1. If fewer than two materially distinct READY nodes are suitable for parallel work, do not create lane commands. Continue in mainbatch on the best current unit.
2. If two or more materially distinct READY nodes are independent, select at most `max_parallel`.
3. Before displaying any lane command, bind each selected node to a stable slot in `MISSION.json.dispatch.assignments` for the new dispatch generation.
4. Slots are `a`, `b`, `c`, ... and produce commands `__MISSION__-a`, `__MISSION__-b`, `__MISSION__-c`, ... .
5. Each assignment records at least `slot`, `node_id`, `command`, and `work_branch`. A lane command always resolves through that recorded assignment; it must never recompute its node from the live frontier.
6. Prefer branch-only child lanes. Do not create one PR per lane by default.
7. Print the exact commands with node titles immediately after startup so the human can launch them in separate chats.

Use `dispatch_ready.py MISSION.json` to materialize and print a stable dispatch when parallelism is justified. The dispatcher intentionally does nothing when fewer than two READY nodes exist.

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

## Parallel lane contract

A command such as `__MISSION__-a`:

1. reads `AGENTS.md` and the mission `MISSION.json`;
2. resolves slot `a` only from the current recorded dispatch assignment;
3. opens only that node's `STATE.json` plus exact referenced inputs;
4. verifies search-before-create and prior blocked routes before work;
5. works only that assigned node on its recorded branch/scratch lineage;
6. records a coherent result/blocker/checkpoint and stops;
7. never self-reassigns to another READY node and never creates a PR unless the mission integration policy explicitly requires one.

If the slot is missing or no longer valid, the lane stops and returns to `__MISSION__-mainbatch` for redispatch.

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

The human operator may simply repeat `__MISSION__-mainbatch`. When parallel work is available, startup/mainbatch must print the exact short lane commands to launch. The operator does not need to inspect the DAG or invent lane names.

The agent is responsible for DAG maintenance, stable dispatch binding, reuse search, anti-loop bookkeeping, route broadening triggers, and deciding whether parallelism is justified.
