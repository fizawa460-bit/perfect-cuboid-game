# Stage14 batch — common canonical contract

This file is the normative common contract for the three execution entries

```text
Stage14-main-batch
Stage14-s-batch
Stage14-t-batch
```

The route-specific contract must be read immediately after this file. If common
and route-specific text conflict, the route-specific rule controls only the
explicitly named route-specific field; all other common rules remain binding.

## Source and numbering boundary

Start from latest merged `main`. Only merged commits are theorem sources. Open,
draft, closed-unmerged, local-only, and concurrently produced results are
advisory. Record the start SHA and recheck latest `main` immediately before
publication. Follow the unique merged `NEXT`; the permanent entry name never
creates a parallel numbering system.

## Work-unit and publication rule

Advance 3--5 substantive work units on one branch and publish one Draft PR. An
ordinary mathematical stage is one work unit. A newly required independent H
audit is also one work unit when its target and source snapshot are frozen before
the audit. The H audit may share the batch branch and PR, but it must be
clean-room with respect to later internal stages. Existing or concurrent H work
is read-only/advisory and is never rewritten to chase the batch.

For every ordinary internal stage:

1. read its merged predecessor and named merged dependencies;
2. preserve every physical mask, primitive/gcd condition, orientation,
   quantifier order, and charged-once rule belonging to the route;
3. produce a self-contained boundary and exact `NEXT`;
4. record the route's H decision and frozen request when applicable;
5. run a narrow deterministic audit.

A renaming, dependency refresh, or restatement of the same receiver is not a
substantive work unit. Checkpoint commits are allowed; separate PRs for internal
units are not.

## Stop rules

Stop at the first of:

- a mathematically material receiver change;
- an integrated H audit that leaves an unresolved external gate;
- a rigorous counterexample to the active adapter or reduction;
- five completed substantive work units.

The normal minimum is three work units. A justified early stop before three is
allowed only for one of the first three mathematical events. Merely discovering
that H is useful does not stop the batch: freeze it, execute it as one work unit,
consume its result, and continue when the result permits.

## Validation and theorem claims

The Draft PR contains only batch-owned results, audits/data, path-scoped CI, and
genuinely reusable lemmas. Re-run all internal audits and relevant predecessor
regressions at the end. Existing merged artifacts remain read-only.

No strict sub-square-root saving may be declared unless the batch proves

```text
V(B) << B^(1/2-delta+o(1))
```

for fixed `delta>0` on the full physical packet. A saving on a restricted route
may not be promoted without the required uniform transfer to that packet.

Every final report includes:

```text
BATCH_START_MAIN_SHA=<sha>
BATCH_PUBLICATION_MAIN_SHA=<sha>
BATCH_FIRST_STAGE=<stage>
BATCH_LAST_STAGE=<stage>
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=<3..5, or justified early count>
BATCH_SUBSTANTIVE_STAGE_COUNT=<compatibility alias equal to work-unit count>
BATCH_INTEGRATED_H_UNITS=<comma-separated H stages or NONE>
BATCH_STOP_REASON=receiver_change|unresolved_external_gate|rigorous_counterexample|five_stage_cap
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=<value>
STRICT_SUBSQRT_POWER_SAVING_PROVED=<true|false>
NEXT=<next concrete route stage or exact unresolved gate>
```
