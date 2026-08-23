# Codex Task Scope and Stop Policy

Status: reusable Research OS policy

Purpose: prevent a technically successful Codex task from expanding into unnecessary algorithm research, optimization, census extension, or follow-on work and consuming a disproportionate amount of finite token / compute budget.

This policy MUST be read before drafting a Codex work request for this repository.

## 1. Core rule

A Codex request is a **bounded work package**, not an invitation to continue research as far as possible.

Every request must define, before execution:

1. **Required goal** — the minimum concrete state that makes the task successful.
2. **Required evidence** — exact artifacts, tests, certificates, regression checks, or documentation needed to support that goal.
3. **Non-goals** — adjacent work that is explicitly out of scope.
4. **Stop condition** — the exact point at which Codex must stop even if it sees an obvious next improvement.
5. **Escalation condition** — what Codex should do if the required goal cannot be completed with the currently authorized method.

If any of these five items is missing, the prompt is not ready.

## 2. Default behavior: conserve tokens and compute

Unless the user explicitly authorizes exploration, Codex must prefer the smallest reliable path to the required goal.

Default rules:

- Reuse existing repository code, artifacts, checkpoints, certificates, and audit evidence before rebuilding anything.
- Do not optimize code that already completes the required goal reliably.
- Do not generalize a one-off fix into a production framework unless productionization is itself the required goal.
- Do not extend a successful low-degree / low-range result into a larger census unless that extension is explicitly requested.
- Do not open a new theorem search, backend research branch, partition hierarchy, or algorithm family merely because it may improve future scaling.
- Record useful follow-up ideas briefly; do not implement them in the current task.
- A newly discovered bottleneck is normally an **output of the task**, not automatic permission to solve the next bottleneck.

The phrase **"advance as far as computationally reasonable"** and equivalent open-ended language is prohibited by default because it creates an unbounded task.

Similarly avoid:

- "continue as far as possible"
- "optimize further if useful"
- "extend to production if time permits"
- "explore better methods"
- "keep improving the backend"

unless the user explicitly chooses an exploratory task and accepts the cost.

## 3. One PR / task, one finish line

A normal implementation or computational PR should have one primary finish line.

Examples:

Good:

> Close the 28 already-identified residual shards exactly, run the specified predecessor regression, record the evidence, and stop.

Too broad:

> Close the residuals, redesign the backend, optimize future scaling, extend the census, identify the next bottleneck, and continue as far as reasonable.

If completion of the required goal reveals a next-stage opportunity, create a successor-task note instead of silently expanding the current task.

## 4. Blockers and fallback work

Codex may perform implementation work necessary to overcome a blocker **only to the depth needed for the required goal**.

When a blocker appears:

1. Diagnose it sufficiently to decide whether the current authorized method can finish the task.
2. Apply the smallest exact / reproducible fallback that can close the required cases.
3. If the fallback works, finish the requested cases and stop.
4. If the fallback still leaves UNKNOWN / incomplete cases, preserve checkpoints, state the exact blocker, and stop unless the prompt explicitly authorizes a new research branch.

Do not repeatedly add deeper fallback layers just for performance improvement after the required cases are already closed.

## 5. Audit and mathematical firewalls remain independent

Finishing a Codex task does not automatically grant theorem, route, receiver, or census credit.

The prompt must preserve existing audit firewalls and require evidence-appropriate claims only.

In particular:

- implementation success != theorem proof;
- numerical completion != orbit completion unless orbit handling is actually done;
- a prefix census != a full census;
- a new backend agreeing on selected examples != complete regression unless the requested regression set is actually checked;
- heuristic / floating evidence must not be promoted to exact credit.

## 6. Mandatory stop language

Every Codex prompt should include an explicit stop clause similar to:

```text
STOP CONDITION

Once the required goal and required verification listed above are complete, finalize the requested artifacts / PR and STOP.

Do not expand the scope even if you discover a better method or an obvious next research step. Record follow-up ideas only.

Do not start the next stage, larger census range, additional optimization, or new algorithm research unless it is explicitly part of the required goal.

If the required goal cannot be completed with the currently authorized fallback, preserve all completed evidence, report the exact remaining blocker, and STOP rather than opening a new research branch.
```

This clause should be omitted only when the user has explicitly requested open-ended exploration.

## 7. Prompt-author checklist

Before giving a Codex prompt to the user, the prompt author must be able to answer all of these in one sentence each:

- **What exactly must Codex finish?**
- **What proves that it finished?**
- **What must Codex not do?**
- **Exactly when must Codex stop?**
- **What happens if it hits a new blocker?**

The prompt author should also tell the user, in plain Japanese before the copyable prompt:

```text
今回Codexにやらせる範囲: <required goal>
ここから先はやらせない: <main non-goals>
停止点: <stop condition>
```

This lets the user check scope before spending tokens.

## 8. Recommended bounded prompt template

```text
Read and obey:
docs/research-os/policies/codex-task-scope-stop-policy.md

TASK
<one bounded task>

REQUIRED GOAL
- <goal 1>
- <goal 2 only if necessary>

REQUIRED EVIDENCE
- <test / exact certificate / artifact / regression>

REUSE FIRST
- Inspect and reuse <existing PR / code / artifact / checkpoint> before writing replacements.

NON-GOALS
- Do not <adjacent research>.
- Do not <larger range / next stage>.
- Do not <optional optimization>.

BLOCKER RULE
If the required goal cannot be completed using the currently authorized implementation/fallback, preserve completed work, identify the exact blocker, and stop. Do not start a new research branch without explicit approval.

STOP CONDITION
Once the required goal and required evidence are complete, finalize the requested PR/artifacts and STOP.
Record follow-up ideas only; do not implement them.

AUDIT FIREWALLS
<current route / receiver / theorem / census statuses that must not be upgraded without exact evidence>
```

## 9. Exploration exception

Sometimes the task genuinely is exploratory research. In that case the prompt must say so explicitly and should still impose a budget boundary such as:

- a fixed number of candidate approaches;
- a fixed set of sources;
- a fixed runtime / experiment count;
- one proof-of-concept only;
- stop after identifying the best next route, without implementing it.

"Exploratory" is not a reason to make the task unlimited.

## 10. Lesson encoded by this policy

A capable agent will often continue improving a working solution when the prompt rewards progress without defining completion. That behavior can be technically correct and still be operationally wasteful.

The Research OS therefore treats **scope design and stopping criteria as part of correctness** for agent-driven research.
