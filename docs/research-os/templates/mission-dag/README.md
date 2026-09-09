# Mission DAG research template

Purpose: reusable research harness for Stage32EX-style work, inspired by the Prove2Me/FLT pattern of decomposing a hard mission into reusable dependency nodes while preventing duplicate work and repeated failed-route loops.

This template does not replace Stage-local mathematics, proof authority, hostile audit, or the repository-wide Cycle Exploration Safety Protocol. It provides a thin orchestration layer above them.

## Human operator surface

The human operator should need only three command families:

1. `research-start <mission>: <target>`
   - instantiate this template;
   - set the mission target and optional max parallelism;
   - decompose only enough to expose a useful initial frontier;
   - if parallel work is justified, print the exact short lane commands automatically.
2. `<mission>-mainbatch`
   - read mission state;
   - compute the current open frontier;
   - run or assign materially distinct ready nodes;
   - freeze blockers and reuse existing results instead of recreating equivalent nodes;
   - when multiple READY nodes are independent, bind stable lane slots and print commands such as `<mission>-a`, `<mission>-b`, `<mission>-c`;
   - stop at a coherent checkpoint.
3. `<mission>-audit`
   - perform the repository hostile-audit contract on an exact retained checkpoint;
   - never self-grant audit credit from mainbatch.

The operator does not manually maintain the DAG, candidate ledger, frontier, or lane names.

## Minimal files

- `MISSION.json`: mission target, node registry, dependencies, statuses, execution limits, and current stable dispatch bindings.
- `nodes/<NODE-ID>/STATE.json`: one research node, its semantic identity, attempts, blockers, retained result, and reuse provenance.
- `MAINBATCH.md`: generic execution contract.
- `dispatch_ready.py`: derives the READY frontier, binds independent nodes to stable `a/b/c...` slots, and prints the exact commands.
- `verify_mission.py`: cheap structural verifier for both DAG and dispatch bindings.

`frontier.json` is intentionally not stored. The frontier is derived from the DAG to avoid state drift. `MISSION.json.dispatch` is not a second frontier; it is only a stable snapshot binding already-selected READY nodes to human-facing lane commands so that `-b` cannot silently change meaning after `-a` finishes.

## Parallel startup contract

Parallel commands are produced only when at least two materially distinct READY nodes can run independently. `max_parallel` is a ceiling, not a target.

Before displaying commands, mainbatch/dispatcher records a new dispatch generation and assignments like:

```json
{
  "slot": "a",
  "node_id": "N004",
  "command": "stage40ex1-a",
  "work_branch": "stage40ex1-lane-a-g2",
  "status": "ISSUED"
}
```

The human launches the printed commands in separate chats. Each lane resolves its node only from that recorded assignment and must not recompute a different node from the live frontier. If an assignment is missing or stale, the lane returns to `<mission>-mainbatch` for redispatch.

Exploratory child work should normally use branches/scratch, not one PR per node. The long-lived mission/mainbatch surface integrates retained checkpoints.

## Anti-duplication rule

Before creating a node, mainbatch must search the current mission and relevant repository assets for an equivalent result or research obligation. A new node requires a stable `semantic_key` and a recorded `reuse_check`.

Exact duplicate `semantic_key` values are forbidden. A near-duplicate may coexist only when the state explains why the hypotheses, population, field/model, quantifiers, or required output are materially different.

## Anti-loop rule

Failed attempts stay in the node state with a stable `route_id` and blocker. Mainbatch must not retry the same route unless its recorded reopen condition became true.

Route statuses use the repository Cycle Exploration Safety Protocol vocabulary where applicable: `LIVE`, `UNTESTED`, `EQUIVALENT`, `DOMINATED`, `BLOCKED`.

When broadening/parking/exhaustion becomes load-bearing, open `docs/research-os/policies/cycle-exploration-safety-protocol.md` rather than copying its full rules into every mission.

## DAG rule

A node becomes READY only when all dependencies are DONE. DONE means the node's own retained output exists at its declared credit ceiling; it does not imply downstream theorem, Stage, or endpoint credit.

A parent may not close merely because one child blocked. Mainbatch may decompose, replace with a stronger equivalent node, or record a genuine unresolved survivor.

## Copy contract

Copy this directory into the target research area, rename the mission placeholders, create the initial `MISSION.json`, and create one `STATE.json` per initial node from `NODE.template.json`. The mainbatch agent owns subsequent DAG/frontier/dispatch maintenance.

The template deliberately keeps the human-facing rules small. Repository-wide safety, credit, audit, evidence, and heavy-compute policies remain on-demand rather than being duplicated here.
