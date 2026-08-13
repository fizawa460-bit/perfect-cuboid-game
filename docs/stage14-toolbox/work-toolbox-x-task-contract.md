# Stage14-Work-toolbox-XQ — canonical integrated task contract

## Canonical invocation

The permanent task name is:

```text
Stage14-Work-toolbox-XQ
```

When this exact task name is requested, read this file **before** deriving a stage
number, inspecting candidate receivers, or creating a branch.  The permanent name
is an entry point, not a completed mathematical stage.  Concrete outputs continue
the two ledgers, for example `Stage14-Work-beX17`, without reusing an already
merged toolbox or X number. If the integrated audit exposes a legitimate q
trigger, the same operation also consumes the next unused q number.

The historical invocation `Stage14-Work-toolbox-X` remains a compatibility alias
for the same contract. New requests and handoffs should use the `XQ` name so that
the post-X q gate is not silently omitted.

## Start gate

1. Read latest merged `main`.
2. Derive and read the most recent merged integrated `Stage14-Work-*X*` result;
   never rely on a hard-coded example from this contract.
3. Locate the latest merged boundaries of mainline `14-4*`, route `14-s*`,
   fixed-`U` route `14-t*`/`14-tH*`, toolbox, and `14-X*`.
4. Exclude every draft, open, closed-unmerged, or local-only descendant.
5. Compare progress with the previous integrated Work boundary.

Do not infer readiness merely because one advertised immediate successor merged.
Normally require a material accumulation: mainline and s should each advance
roughly 2–4 substantive consumers, with enough t/tH progress to change or
materially test the fixed-`U` receiver.  A new exponent, receiver change, H
audit, supersession ambiguity, or plausible cross-route adapter may justify an
earlier run.

If the material is insufficient, stop after reporting:

```text
STAGE14_WORK_TOOLBOX_X=WAIT
```

State the exact merged boundaries and a concrete revisit condition.  Do not create
a result stage, branch, commit, workflow, or PR for a WAIT decision.

## Integrated X execution

When the gate passes, perform one charged-once operation containing both:

- the next toolbox component: cross-route exponent, receiver, dependency,
  supersession, and H-need audit;
- the next X component: independent test for a common receiver, adapter, exact
  identity, or transferable saving.

Keep global main/s and fixed-`U` coefficient spaces, measures, and quantifier
orders separate unless an explicit proof identifies them.  A shared vocabulary
or decomposition is not a saving bridge.  Do not multiply finite-fiber equivalent
coordinate counts, recharge an already charged cone, cross-promote a fixed-`U`
saving, or declare a positive delta without a proved uniform estimate preserving
all physical filters.

## Post-X q gate

After the toolbox and X components are complete, but before publication:

1. freeze the new merged-source receiver and the exact obstruction produced by X;
2. read `stages/stage14/archive/docs/q-research/stage14-q-task-contract.md`, the latest merged q result, and the q literature ledger;
3. decide whether the frozen obstruction is materially new relative to that ledger;
4. if it is not new, record `Q_COMPONENT=NOT_TRIGGERED` and finish the X result;
5. if it is new, execute the next unused q stage immediately as one additional charged-once work unit on the **same branch and in the same Draft PR**;
6. return the q classification and falsifiable handoff to the integrated Work result before publication.

The q component is triggered research, not an automatic literature search after
every X run. Stage-number progress, renamed variables, or a receiver already
covered by the current q ledger are not triggers. A triggered q component must
preserve the frozen X target: it may test external theorems and derive an adapter
or obstruction, but it must not silently broaden or replace the target after the
search begins.

If the triggered q investigation is too large to finish safely in the current
operation, freeze exactly one q target, record `Q_COMPONENT=DEFERRED_SCOPED`, and
stop without claiming that q is complete. This is the only normal split point;
do not create a second PR merely because q used to be a separate invocation.

## Required decision record

Every completed result must lock at least:

```text
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
Q_COMPONENT=<COMPLETE|NOT_TRIGGERED|DEFERRED_SCOPED>
Q_TRIGGER_STAGE=<stage-or-NONE>
EXACT_Q_OBSTRUCTION=<obstruction-or-NONE>
Q_LEDGER_BASELINE=<latest-merged-q>
Q_RESULT_IMPORTED_BACK_TO_X=<true|false|not-applicable>
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<value>
STRICT_SUBSQRT_POWER_SAVING_PROVED=<true|false>
CURRENT_GLOBAL_RECEIVER=<receiver>
CURRENT_FIXED_U_RECEIVER=<receiver>
COMMON_ADAPTER_PROVED=<true|false>
SAVING_CROSS_PROMOTABLE=<true|false>
MAINLINE_H_NEEDED=<true|false>
S_ROUTE_H_NEEDED=<true|false>
FIXED_U_H_NEEDED=<true|false>
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=<true|false>
NEXT_REVISIT_CONDITION=<merged milestones>
```

For every H flag, name the exact frozen theorem target if true; if false, say why
another external audit is premature.  The integrated stage must say whether it
only contracted a receiver or actually improved the exponent. For the q fields,
name the exact difference from the last q baseline or explain why no new search
was triggered.

## Deliverables when RUN

Create only task-owned files:

1. an integrated result under `stages/stage14/14-Work-<toolbox><X>/result.md`;
2. a deterministic audit under the matching scripts directory;
3. a concise receiver/supersession matrix under `docs/stage14-toolbox/`;
4. a path-scoped dedicated GitHub Actions workflow.

Only when the q gate triggers, also create the canonical q radar and summary files
required by `stages/stage14/archive/docs/q-research/stage14-q-task-contract.md`. They belong to the same branch,
commit series, validation pass, and Draft PR as the Work result. Do not duplicate
the Work receiver matrix in the q summary.

Run the integrated audit and all referenced current-boundary regressions.  Keep
existing stage ledgers read-only.  Recheck latest `main` immediately before
publication, update only the integrated task if new merged consumers matter, and
publish a Draft PR through the connected GitHub integration.

## Numbering rule

Derive both successors from merged history, never from a prompt guess:

- toolbox successor = alphabetic successor of the latest merged toolbox component;
- X successor = numeric successor of the latest merged X component.
- q successor, when triggered = numeric successor of the latest merged q stage.

If either number is already consumed by an independent merged stage, advance to
the next unused pair and record the supersession.  The permanent invocation name
is `Stage14-Work-toolbox-XQ`; the old `Stage14-Work-toolbox-X` spelling is only a compatibility alias.
