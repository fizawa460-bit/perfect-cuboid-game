# stage32-01-178 MAINBATCH

Mission target: complete Stage32 32-01 FULL178 numerical Picard census with machine-checkable completeness while preventing duplicate work and blocked-route loops.

## Startup

Read only:

1. `AGENTS.md`;
2. `stages/stage32/32-01-178/MISSION.json`;
3. `STATE.json` for READY frontier nodes or the exact assigned lane;
4. exact source/evidence paths referenced by those states.

Use `docs/research-os/templates/mission-dag/verify_mission.py` for structural checks and the Research OS policies only on their explicit triggers.

## Batch behavior

1. Derive READY nodes from the DAG; do not maintain a second mutable frontier file.
2. Honor current dispatch slot bindings until consumed/cancelled.
3. Search-before-create for every node/route and record reuse provenance.
4. Do not retry a stable BLOCKED route unless its reopen condition became true.
5. Run or integrate at most `MISSION.json.max_parallel` materially distinct nodes.
6. Child lanes use branches/scratch by default, not one PR per lane.
7. A lane may itself become a nested Mission DAG if its node is too large; the parent consumes only the nested checkpoint/result.
8. EX5 remains an external producer. Do not duplicate its active BC2-02 FULL178-target-to-59D adapter work; consume only explicit retained/audited outputs through an adapter.
9. Heavy compute is not authorized by mission startup. Use the repository heavy-workflow gate before any artifact-producing scale-out.
10. MAINBATCH owns reconciliation, node status/dependency mutation, redispatch, promotion and audit handoff.
11. Stop at coherent checkpoints. Do not merge and do not self-grant hostile-audit credit.

## Generation-1 purpose

The first six lanes are deliberately different obligations rather than row shards:

- N101 exact indexed-terminal compression redesign;
- N102 eight hard-tail-row structure;
- N103 production-side witness/support retention interface;
- N104 completeness/replay certificate architecture;
- N105 independent global-cut/reusable-weapon discovery;
- N106 compressed execution/sharding design.

N150 is a blocked external EX5 consumption gate and receives no lane until EX5 produces a current-target result. N190 becomes READY only after the six Generation-1 obligations are resolved and then selects the next load-bearing frontier.

## Human interface

The operator normally repeats:

`stage32-01-178-mainbatch`

When MAINBATCH/startup prints issued lane commands, launch each in a separate chat. Current generation-1 commands are recorded in `MISSION.json` and must not be inferred from letters alone.
