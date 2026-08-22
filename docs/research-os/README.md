# Research OS

This directory contains research-process rules that are useful beyond one Perfect Cuboid stage.

Stage29 is closed. Its concrete mathematical frontier remains under `stages/stage29/29-17/`; this folder is for the reusable operating method, not for pretending the old Stage16-29 controller is still active.

## Current reusable policies

- [`policies/cycle-exploration-safety-protocol.md`](policies/cycle-exploration-safety-protocol.md) — prevents premature narrowing, silent route deletion and Arsenal anchoring; includes blind rediscovery / exhaustive-view audit triggers.
- [`policies/self-contained-review-standard.md`](policies/self-contained-review-standard.md) — standard for self-contained final mathematical review artifacts.

## Stage29-derived restart pattern

The final Stage29 handoff recommends the recursion

```text
chosen kernel
  -> dependency DAG
  -> bounded work packages
  -> leaf-level Class 1/2/3/4 reclassification
```

where:

- Class 1: execute now;
- Class 2: computational/model work, subdivide to exact CAS/code/certificate tasks;
- Class 3: isolate the minimum missing theorem;
- Class 4: dormant until an explicit trigger fires.

Source: [`../../stages/stage29/29-17/post-stage29-research-os.md`](../../stages/stage29/29-17/post-stage29-research-os.md).

The older Stage-specific execution templates and roadmap policies are archived rather than treated as generic OS rules. A later OS-extraction pass can promote only the parts that remain genuinely problem-independent.
