# Stage33 33-12 micro-goal execution roadmap

```text
ROLE=PLANNING_AND_EXECUTION_CHECKLIST_ONLY
LIVE_AUTHORITY=stages/stage33/controller.json + stages/stage33/MAIN-STATE.json
CURRENT_LOCKED_FRONTIER=V41_V42_V43
ATOMICITY_RULE=ONE_SMALL_VERIFIABLE_GOAL_PER_COMMIT
MERGE_ALLOWED=false
```

This file changes execution granularity, not mathematical credit. Current authority and release gates remain in the controller/state. A roadmap item is complete only when its stated acceptance condition is mechanically checkable from committed artifacts.

## Operating rule

Do not use broad goals such as "construct the remaining lift" or "continue Stage33" as a batch target. Every batch must select the first unfinished item below, produce either the exact object or a narrowly stated exact obstruction, run its dedicated verifier, and commit that item before moving to the next item.

For mathematical construction commits:

1. one missing interface/object only;
2. one deterministic certificate/output artifact;
3. one dedicated verifier or a clearly existing verifier that checks the new object;
4. no downstream credit in the same commit unless that credit is itself the next roadmap item;
5. if blocked, record the smallest missing datum/interface and make that the next item rather than reopening broad search.

## Locked starting point

The current e3 branch begins after these exact checkpoints:

- V41 independently materializes `e3` as retained10 standard mask `4`, proper14 mask `20`, without using `J2=e2+e3` splitting.
- V42 blocks relabelling/reusing the J2-specific V25 lift as an e3 lift.
- V43 records that reviewed boundary-function / scalar-descent / J2-Cech interfaces do not yet provide an exact reusable proper14-to-Cech or full-surface `H2(mu2)` adapter for e3.
- Stage33 remains at `6/11`; Stage33-12 is not exactly closed; Stage33-13 is not released.

## Phase A — finish one independent e3 column

### A1 — materialize proper14 -> boundary-source coordinates

Goal: construct the exact map taking e3 proper14 mask `20` to the boundary-function source data needed by the finite generator packages, or an equivalent exact global Gersten source coordinate.

Acceptance:
- exact input `proper14_mask=20` source-locked;
- output coefficient/source vector explicitly materialized;
- basis/order conventions mechanically checked;
- no Cech/H2/Kummer-column claim yet.

Blocked outcome allowed: a certificate identifying one specific missing matrix/table/convention required to define this map. "No adapter found" is not sufficient.

### A2 — assemble the global Gersten 2-cochain for e3

Goal: use A1 plus the locked boundary-function generator packages and finite scalar table to assemble a concrete global Gersten 2-cochain candidate representing e3.

Acceptance:
- every nonzero generator contribution is listed with coefficient and source lock;
- constant/scalar corrections are explicit;
- no J2-specific symbol is silently relabelled;
- candidate is deterministic and replayable.

### A3 — residue audit the e3 Gersten candidate

Goal: compute the codimension-one residue vector of the A2 candidate over the complete locked boundary index.

Acceptance PASS branch:
- complete residue index coverage is certified;
- all required residues vanish exactly;
- candidate is certified unramified in the required full-surface scope.

Acceptance FAIL branch:
- nonzero residue support is exactly listed;
- the next goal is a finite correction problem on that support, not a new broad search.

### A4 — materialize an independent e3 Cech `H2(mu2)` representative

Goal: convert the residue-clean A2/A3 object into an explicit full-surface Cech `H2(mu2)` lift.

Acceptance:
- explicit cocycle/overlap data materialized;
- cocycle condition checked exactly;
- square/constant corrections checked;
- full-surface scope and source locks explicit.

### A5 — bind the Cech lift back to exact e3

Goal: prove that the A4 lift maps to the exact V41 e3 Brauer source and not merely to some nonzero or J2-related class.

Acceptance:
- Brauer image equals retained10 mask `4` / proper14 mask `20` under an explicit checked adapter;
- independence from the forbidden `J2=e2+e3` split is certified;
- this is the first point at which `GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_E3=true` may be recorded.

### A6 — compute the e3 Kummer column

Goal: apply the exact Kummer target map to the A5 lift and materialize the second J2-adapted source column.

Acceptance:
- target basis/order locked;
- full target column explicit;
- replay recomputes the column from the A5 lift;
- no guessed standard col2/col3 decomposition.

### A7 — integrate and audit the `2/10` adapted-column frontier

Goal: update the live Stage33 frontier only after A1-A6 pass.

Acceptance:
- J2-adapted columns materialized becomes `2/10`;
- original standard columns remain credited only when individually justified;
- controller/state/certificate projection agree;
- dedicated exact-head CI passes before further source work.

## Phase B — finish the remaining adapted sources

Process sources in the locked priority order after e3:

`e1, e4, e5, e6, e7, e8, e9, e10`.

For each source `s`, use the same atomic sequence:

- B(s).1 exact proper14/source coordinate;
- B(s).2 instantiate the proper14 -> boundary/Gersten source map;
- B(s).3 assemble global Gersten 2-cochain;
- B(s).4 residue audit;
- B(s).5 independent Cech `H2(mu2)` lift;
- B(s).6 exact Brauer-image binding to `s`;
- B(s).7 exact Kummer column;
- B(s).8 frontier integration and exact-head replay.

If A1-A5 establish a genuinely linear reusable adapter for arbitrary proper14 inputs, later B(s) items may reuse it, but each source still requires a separate instantiation/binding/column certificate. Reuse must be explicit; do not collapse multiple source credits into one inferred batch.

## Phase C — close the finite V4 Kummer matrix repair

### C1 — assemble the complete adapted-source matrix

Acceptance: all 10 adapted source columns are materialized from genuine source-bound lifts; matrix basis/order and column provenance are explicit.

### C2 — compute exact rank/kernel/image data

Acceptance: exact F2 rank, kernel basis, image basis, and every named surviving/vanishing source are replayed mechanically.

### C3 — translate matrix output into the Stage33 relevant Q-defined class inventory

Acceptance: every relevant class has order, provenance, source representative, and survival/disposition; no class is credited solely from a dimension count.

### C4 — satisfy all Stage33-12 contract exit requirements

The controller currently requires:

- `ARITHMETIC_HS_D2_COMPUTED`;
- `GLOBAL_Q_RESIDUE_LIFT_COMPLETION`;
- `COMPLETE_RELEVANT_Q_DEFINED_CLASS_INVENTORY_FOR_FROZEN_STAGE33_BRAUER_SCOPE`;
- `STAGE33_07_HOSTILE_RECERTIFICATION_PASS`.

Treat each unmet requirement as its own commit/gate. Stage33-12 is not closed until all four are exact and audited as required.

### C5 — Stage33-07 hostile recertification and parent reclose

Acceptance: hostile replay covers the repaired arithmetic/Kummer path at an exact head and Stage33-07 is explicitly reclosed by current authority.

## Phase D — finish the remaining five big Stage33 tasks

The Stage33 denominator stays the original 11 big tasks. Repair children do not increment it by themselves.

### D1 — Stage33-08 explicit endpoint representatives

Split by surviving class. For each class: materialize one locally evaluable representative, field/domain/ramification data, then verify equivalence/independence. Only after all classes are covered may Stage33-08 close.

### D2 — Stage33-40 relevant places

First derive the finite relevant-place set from actual representatives. Then certify the required physical local loci/components place-by-place. Do not combine place discovery and local evaluation credit.

### D3 — Stage33-41 exact local evaluations

Work one `(place, class, physical-locus)` evaluation block at a time. Each commit records the exact image and constancy/nonconstancy certificate. Close only after the complete evaluation table is covered.

### D4 — Stage33-42 adelic compatibility

Assemble the exact local images under reciprocity, compute the final Brauer disposition for the frozen Stage33 scope, and keep this separate from endpoint promotion.

### D5 — hostile audit and endpoint promotion gate

Run the required final hostile audit at an exact head. Only a passing authority transition may grant Stage33 completion/endpoint credit. Perfect-cuboid existence or nonexistence remains forbidden unless a separate explicit audited full-endpoint certificate authorizes it.

## Batch selection rule

At the start of every `stage33main batch`:

1. read live controller/state;
2. identify the first roadmap item whose prerequisites are satisfied and whose acceptance is not yet certified;
3. work only that item;
4. commit it;
5. if enough context remains, proceed to the next item as a new commit.

Never skip forward because a later calculation looks easier. Never reopen a completed item without a new contradiction, failed verifier, hostile-audit finding, or changed authoritative input.
