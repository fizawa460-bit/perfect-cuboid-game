# Mission start prompt

Use this when creating a new reusable research mission from the Mission DAG template.

```text
research-start __MISSION__: __TARGET__

Use docs/research-os/templates/mission-dag/ as the orchestration template.
Keep the human-facing interface minimal: I should only need to repeat __MISSION__-mainbatch and, at retained checkpoints, __MISSION__-audit.

Instantiate MISSION.json, MAINBATCH.md, and the smallest useful initial set of node STATE files. Derive the open frontier from dependencies; do not store a second mutable frontier file.

Before creating each research node or route, search for equivalent existing mission/repository work and record reuse provenance. Preserve failed route identities, blockers, and reopen conditions so the same blocked approach is not retried without new input.

Use the Cycle Exploration Safety Protocol only when its trigger becomes load-bearing; do not preload or duplicate all Research OS policies.

Parallelize only materially distinct READY nodes, up to the configured max_parallel. When two or more READY nodes can run independently, bind them to stable dispatch slots in MISSION.json before showing commands, create/use branch-only lane lineages, and print the exact commands immediately, for example:

__MISSION__-a
__MISSION__-b
__MISSION__-c

The human should never need to invent lane names or inspect the DAG. A lane command resolves only through its recorded dispatch assignment and must not self-reassign if the frontier changes.

Prefer scratch/branches for exploratory nodes and one long-lived integration surface for retained checkpoints. Do not create one PR per node by default.

Do not self-grant hostile-audit credit. Do not merge without explicit authorization.
```
