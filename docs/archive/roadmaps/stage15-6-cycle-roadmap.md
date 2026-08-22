# Stage15-6 unified cycle roadmap

## Permanent command

```text
Stage15-6-cycle
```

This is the single execution command for the remainder of Stage15-6. It replaces the proposed separate `Stage15-6-batch`, `Stage15-6-audit`, and `Stage15-6-review` commands.

## One cycle

Every invocation starts from latest merged `main` and performs, in order:

1. **Pre-flight audit/review**
   - read the last merged Stage15-6 exit and all named theorem dependencies;
   - audit the dependency chain back as far as needed, including earlier Stage15-6 substages when a claim depends on them;
   - verify physical measure/cutoff, primitive/gcd masks, orientation, quantifier order, reconstruction multiplicity, Arsenal trigger/adapters, and charged-once/no-double-charge rules;
   - check that no conjectural exponent, necessary-only projection, or restricted-branch saving has been promoted to a whole-family theorem;
   - repair a discovered material defect before advancing. A rigorous counterexample or unresolved material defect is an immediate stop.

2. **Batch advance**
   - follow the unique merged `NEXT`;
   - advance normally 3--5 substantive mathematical work units on one branch and one Draft PR;
   - each internal unit gets an exact boundary, deterministic narrow replay when feasible, Arsenal trigger-signature check when relevant, and a concrete `NEXT`;
   - a restatement/rename/dependency refresh is not a substantive unit.

3. **Integrated post-flight audit/review**
   - re-audit every new unit plus the affected dependency chain;
   - rerun relevant predecessor regressions and path-scoped CI;
   - check theorem scope, measure transfer, quantifiers, reconstruction fibers, Arsenal legality, and double-charge firewall;
   - if the batch changed the receiver, explicitly freeze the new minimal receiver and obstruction.

4. **Publish and stop**
   - publish one Draft PR containing the whole cycle;
   - do not automatically start another cycle in the same invocation.

Thus the user normally needs only to say `Stage15-6-cycle`, merge the resulting PR when satisfied, and say `Stage15-6-cycle` again.

## Stop rules

Stop at the first of:

- a mathematically material receiver/theorem-species change that should be frozen before another route is opened;
- an unresolved external theorem/literature gate;
- a rigorous counterexample or audit failure that cannot be repaired inside the current unit;
- Stage15-6 closure/transition candidate;
- five completed substantive work units.

The normal target is 3--5 units. An early stop before three is valid for the first four mathematical events above. Do not pad a cycle with cosmetic substages merely to reach three.

## Arsenal policy

Use `docs/stage14-arsenal-index.md`, `docs/stage14-arsenal.md`, and `docs/stage14-arsenal-stage15-map.md` as the normal lookup surface. Search Stage14 history only through a named canonical source when an Arsenal entry points there or when the current trigger signature gives a specific buried-gold candidate. Never indiscriminately reopen Stage14 history.

For every reused weapon classify it as one of:

```text
DIRECT_REUSE
EXACT_ADAPTER_PROVED
ADAPTER_REQUIRED
NOT_TRIGGERED
REJECTED_MEASURE_OR_QUANTIFIER_MISMATCH
```

No saving may be charged twice under two Arsenal labels.

## Audit scope is automatically elastic

There is no separate `review` command. The audit phase expands automatically when needed:

- ordinary cycle: audit the immediately affected dependency cone;
- after several cycles or a major receiver change: audit from the last stable Stage15-6 checkpoint;
- before declaring Stage15-6 closed: audit the full Stage15-6 theorem chain from 6aa through the proposed final exit.

The user does not need to decide which depth is required.

## Current handoff

As of merged Stage15-6ah, the next narrow gate is the one-point small-total-support receiver. The first `Stage15-6-cycle` should begin by auditing the 6aa--6ah chain sufficiently to validate that handoff, then continue from the merged `NEXT` rather than inventing a parallel numbering route.

## Required cycle footer

Every cycle report must include:

```text
STAGE15_6_CYCLE_START_MAIN_SHA=<sha>
STAGE15_6_CYCLE_FIRST_STAGE=<stage>
STAGE15_6_CYCLE_LAST_STAGE=<stage>
STAGE15_6_CYCLE_WORK_UNIT_COUNT=<1..5>
STAGE15_6_CYCLE_PREFLIGHT_AUDIT=PASS|REPAIRED|BLOCKED
STAGE15_6_CYCLE_POSTFLIGHT_AUDIT=PASS|REPAIRED|BLOCKED
STAGE15_6_CYCLE_AUDIT_DEPTH=<dependency-cone|checkpoint-to-head|full-stage15-6>
STAGE15_6_CYCLE_STOP_REASON=<receiver_change|external_gate|counterexample_or_audit_failure|stage15_6_closure_candidate|five_unit_cap>
STAGE15_6_CURRENT_RECEIVER=<exact frozen receiver>
STAGE15_6_CURRENT_OBSTRUCTION=<exact unresolved obstruction or NONE>
STAGE15_6_GLOBAL_COUNT_PROVED=<true|false>
STAGE15_6_CAUSAL_THINNING_EXPONENT_DERIVED=<true|false>
NEXT=<next concrete stage or exact unresolved gate>
```
