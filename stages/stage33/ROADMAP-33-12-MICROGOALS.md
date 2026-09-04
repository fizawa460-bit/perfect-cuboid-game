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

## Arsenal routing rule

For every roadmap item, identify the exact missing object/weapon type first, then consult `docs/arsenal/index.json` and read only the generated card(s) named under that item's `Arsenal` line. Do not load the full Arsenal at ordinary startup.

Authority order is strict: the live Stage33 controller/current source locks override formal Arsenal contracts, and formal contracts override PROVISIONAL Stage33 discovery snapshots. `S33-PW*` cards are PROVISIONAL discovery/routing aids: their hypotheses, object/population, field, quantifiers, basis/action conventions, and source locks must be revalidated against the live Stage33 authority before use. An Arsenal miss or inapplicable card does not prove repository absence or mathematical impossibility.

Fit notation below: `◎` direct/high-value route, `○` strong support, `△` audit/workflow support, `×` no direct Arsenal weapon. A `×` means proceed by ordinary exact mathematics/construction; it is not an absence theorem.

The StageA1/A2 -> Stage34 Class3 family (`S34-W01`--`S34-W03`) is not the default route for this Brauer/Gersten/Kummer/H2 roadmap. Use it only if a later leaf independently satisfies those cards' exact hypotheses.

## Locked starting point

The current e3 branch begins after these exact checkpoints:

- V41 independently materializes `e3` as retained10 standard mask `4`, proper14 mask `20`, without using `J2=e2+e3` splitting.
- V42 blocks relabelling/reusing the J2-specific V25 lift as an e3 lift.
- V43 records that reviewed boundary-function / scalar-descent / J2-Cech interfaces do not yet provide an exact reusable proper14-to-Cech or full-surface `H2(mu2)` adapter for e3.
- Stage33 remains at `6/11`; Stage33-12 is not exactly closed; Stage33-13 is not released.

## Phase A — finish one independent e3 column

### A1 — materialize proper14 -> boundary-source coordinates

A1 is itself split because `proper14` and the finite boundary-function package are separately named 14-dimensional coordinate systems. They must not be identified by position without an exact bridge.

#### A1.0 — lock both 14-dimensional basis definitions

Arsenal: `○ S33-PW04 + S30-WF02`. Use PW04 for marked-basis/adapter conventions and WF02 for immutable provenance/certificate binding; neither by itself constructs the bridge.

Goal: materialize the ordered basis metadata for (i) `proper-brauer2-from-discriminant.json` ext14/proper14 coordinates and (ii) the finite boundary-function retained-one source directions.

Acceptance:
- both 14-element ordered basis definitions are explicit;
- provenance artifact and digest/commit are recorded for each;
- no claim yet that the two orders are equal.

#### A1.1 — construct or certify the exact change-of-basis bridge

Arsenal: `◎ S33-PW05 -> S30-W01/S30-WF01 -> S33-PW04`. First materialize exact finite actions in both 14D presentations; use PW05 to solve the exact intertwiner/compatible-extension space; use S30-W01/WF01 to require a common/source-derived semantic anchor rather than finite matching alone; only then certify the unique marked adapter with PW04. Do not hand-build 14 columns before exhausting this exact route.

Goal: produce an exact GF(2) map from proper14/ext14 coordinates to boundary-function source coordinates.

Acceptance PASS branch:
- explicit 14x14 matrix or mechanically equivalent ordered-basis identification;
- rank/invertibility checked when the intended map is an isomorphism;
- each output coordinate has exact source provenance;
- exact source/target actions used by PW05 and the semantic anchor used by S30-W01/WF01 are source-locked;
- finite equivariance alone is not promoted to geometric/semantic identification.

Acceptance BLOCKED branch:
- one certificate names the exact missing table/matrix/convention/action/semantic anchor needed to define the bridge;
- it records the two already-known basis definitions and proves why positional identification is not yet licensed;
- it records which Arsenal route stage failed (`PW05`, semantic anchor, or `PW04`) and the smallest missing input;
- the next micro-goal becomes construction of that one missing bridge input from its immediate upstream provenance, not a broad repository search.

#### A1.2 — apply the bridge to e3 proper14 mask `20`

Arsenal: `○ S33-PW04`. Once A1.1 is certified this should be exact GF(2) transport through the marked adapter, not a new semantic identification problem.

Goal: compute only the boundary-source coefficient vector for V41 e3.

Acceptance:
- exact input `proper14_mask=20` source-locked;
- exact output 14-bit vector and nonzero boundary source labels materialized;
- replay recomputes output from A1.1 bridge.

#### A1.3 — bind the selected boundary generators

Arsenal: `○ S33-PW04 + S30-WF02`. Use PW04 for exact marked source binding and WF02 for immutable generator/scalar provenance.

Goal: resolve each nonzero A1.2 boundary-source coordinate to its exact finite boundary-function generator package and scalar-descent record.

Acceptance:
- every selected generator file/id and coefficient explicitly listed;
- generator source-basis column/order checked;
- scalar correction record linked for each selected generator;
- no Gersten/Cech/H2/Kummer-column claim yet.

A1 is complete only when A1.0-A1.3 pass.

### A2 — assemble the global Gersten 2-cochain for e3

Arsenal: `◎ S33-PW08`. Follow its locked Gersten/source-basis -> representative lift -> actual height-one valuation attachment -> purity correction construction protocol; use only the portion applicable before the residue/localization audit.

Goal: use A1 plus the locked boundary-function generator packages and finite scalar table to assemble a concrete global Gersten 2-cochain candidate representing e3.

Acceptance:
- every nonzero generator contribution is listed with coefficient and source lock;
- constant/scalar corrections are explicit;
- no J2-specific symbol is silently relabelled;
- candidate is deterministic and replayable.

### A3 — residue audit the e3 Gersten candidate

Arsenal: `◎ S33-PW08`. Require actual valuation attachment, exceptional contributions where present, purity/off-boundary correction, complete residue-index coverage, and exact verification. Never infer a global-Q lift merely from zero localization/residues.

Goal: compute the codimension-one residue vector of the A2 candidate over the complete locked boundary index.

Acceptance PASS branch:
- complete residue index coverage is certified;
- all required residues vanish exactly;
- candidate is certified unramified in the required full-surface scope.

Acceptance FAIL branch:
- nonzero residue support is exactly listed;
- the next goal is a finite correction problem on that support, not a new broad search.

### A4 — materialize an independent e3 Cech `H2(mu2)` representative

Arsenal: `○ S33-PW07 + S30-W02`. PW07 supplies literal transition/divisor/Cartier and common-cocycle semantics; S30-W02 may support exact semilinear descent. No generic completed Gersten->Cech adapter is currently granted by these cards, so the actual adapter still requires exact construction/certification.

Goal: convert the residue-clean A2/A3 object into an explicit full-surface Cech `H2(mu2)` lift.

Acceptance:
- explicit cocycle/overlap data materialized;
- cocycle condition checked exactly;
- square/constant corrections checked;
- full-surface scope and source locks explicit.

### A5 — bind the Cech lift back to exact e3

Arsenal: `◎ S33-PW04 + S33-PW05 + S33-PW07`. Combine exact marked-source coordinates, independently checked source-target compatibility, and literal Brauer/Cech semantics. No dimension-only, nonzero-only, or J2-related identification is sufficient.

Goal: prove that the A4 lift maps to the exact V41 e3 Brauer source and not merely to some nonzero or J2-related class.

Acceptance:
- Brauer image equals retained10 mask `4` / proper14 mask `20` under an explicit checked adapter;
- independence from the forbidden `J2=e2+e3` split is certified;
- this is the first point at which `GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_E3=true` may be recorded.

### A6 — compute the e3 Kummer column

Arsenal: `◎ S33-PW05`, with `S33-PW02` as extension/liftability support where mixed-order source data enter. PW05 must check the exact source-target module relation; PW02 does not itself grant a global-Q or Brauer lift.

Goal: apply the exact Kummer target map to the A5 lift and materialize the second J2-adapted source column.

Acceptance:
- target basis/order locked;
- full target column explicit;
- replay recomputes the column from the A5 lift;
- no guessed standard col2/col3 decomposition.

### A7 — integrate and audit the `2/10` adapted-column frontier

Arsenal: `△ S30-WF02 + S30-WF03`. Use immutable layered replay and the adapter/credit firewall; these workflows validate integration/credit boundaries but add no mathematical column by themselves.

Goal: update the live Stage33 frontier only after A1-A6 pass.

Acceptance:
- J2-adapted columns materialized becomes `2/10`;
- original standard columns remain credited only when individually justified;
- controller/state/certificate projection agree;
- dedicated exact-head CI passes before further source work.

## Phase B — finish the remaining adapted sources

Process sources in the locked priority order after e3:

`e1, e4, e5, e6, e7, e8, e9, e10`.

For each source `s`, use the same atomic sequence and consult the listed Arsenal route before new construction:

- B(s).0 lock source proper14 coordinate and the reusable bridge version — `○ S33-PW04 + S33-PW05`;
- B(s).1 apply the proper14 -> boundary-source bridge — `○ S33-PW04`, then exact GF(2) transport;
- B(s).2 bind selected boundary generators/scalar records — `○ S33-PW04 + S30-WF02`;
- B(s).3 assemble global Gersten 2-cochain — `◎ S33-PW08`;
- B(s).4 residue audit — `◎ S33-PW08`;
- B(s).5 independent Cech `H2(mu2)` lift — `○ S33-PW07`, with `S30-W02` only when its semilinear hypotheses match;
- B(s).6 exact Brauer-image binding to `s` — `◎ S33-PW04 + S33-PW05 + S33-PW07`;
- B(s).7 exact Kummer column — `◎ S33-PW05`, support `S33-PW02` where extension/liftability data are relevant;
- B(s).8 frontier integration and exact-head replay — `△ S30-WF02 + S30-WF03`.

If A1-A5 establish a genuinely linear reusable adapter for arbitrary proper14 inputs, later B(s) items may reuse it, but each source still requires a separate instantiation/binding/column certificate. Reuse must be explicit; do not collapse multiple source credits into one inferred batch.

## Phase C — close the finite V4 Kummer matrix repair

### C1 — assemble the complete adapted-source matrix

Arsenal: `○ S33-PW05 + S33-PW02`, primarily for source-target compatibility and any extension/liftability gate. The matrix assembly itself is exact bookkeeping from already certified columns.

Acceptance: all 10 adapted source columns are materialized from genuine source-bound lifts; matrix basis/order and column provenance are explicit.

### C2 — compute exact rank/kernel/image data

Arsenal: `×` no special weapon required. Use ordinary exact F2 linear algebra on the source-locked C1 matrix.

Acceptance: exact F2 rank, kernel basis, image basis, and every named surviving/vanishing source are replayed mechanically.

### C3 — translate matrix output into the Stage33 relevant Q-defined class inventory

Arsenal: `○ S33-PW01 + S33-PW06`. PW01 supports exact arithmetic-HS classification of a complete source-locked invariant block; PW06 defines the absolute H1/localization receiver without collapsing finite quotient cohomology into absolute Galois cohomology.

Acceptance: every relevant class has order, provenance, source representative, and survival/disposition; no class is credited solely from a dimension count.

### C4 — satisfy all Stage33-12 contract exit requirements

The controller currently requires:

- `ARITHMETIC_HS_D2_COMPUTED` — `◎ S33-PW01`;
- `GLOBAL_Q_RESIDUE_LIFT_COMPLETION` — `×~○ no direct completion weapon`; `S33-PW06`, `S33-PW08`, and `S30-W02` may constrain/prepare the receiver, localization, or descent data, but none licenses global-Q existence from finite descent or zero localization;
- `COMPLETE_RELEVANT_Q_DEFINED_CLASS_INVENTORY_FOR_FROZEN_STAGE33_BRAUER_SCOPE` — `○ S33-PW01 + S33-PW06`;
- `STAGE33_07_HOSTILE_RECERTIFICATION_PASS` — `△ S30-WF02 + S30-WF03`.

Treat each unmet requirement as its own commit/gate. Stage33-12 is not closed until all four are exact and audited as required. In particular, do not turn the absence of a direct Arsenal card for `GLOBAL_Q_RESIDUE_LIFT_COMPLETION` into a negative theorem; this leaf may require genuinely new mathematics.

### C5 — Stage33-07 hostile recertification and parent reclose

Arsenal: `△ S30-WF02 + S30-WF03`. Replay immutable source layers and enforce typed credit/promotion boundaries.

Acceptance: hostile replay covers the repaired arithmetic/Kummer path at an exact head and Stage33-07 is explicitly reclosed by current authority.

## Phase D — finish the remaining five big Stage33 tasks

The Stage33 denominator stays the original 11 big tasks. Repair children do not increment it by themselves.

### D1 — Stage33-08 explicit endpoint representatives

Arsenal: `○ S33-PW07`. Use literal transition-function/divisor/Cartier data and common-cocycle Brauer/torsor semantics where applicable. PW07 is not a Q-defined descent theorem.

Split by surviving class. For each class: materialize one locally evaluable representative, field/domain/ramification data, then verify equivalence/independence. Only after all classes are covered may Stage33-08 close.

### D2 — Stage33-40 relevant places

Arsenal: `×` no direct card currently closes relevant-place discovery. Derive the finite set from the actual D1 representatives and source-locked ramification/domain data.

First derive the finite relevant-place set from actual representatives. Then certify the required physical local loci/components place-by-place. Do not combine place discovery and local evaluation credit.

### D3 — Stage33-41 exact local evaluations

Arsenal: `○ S33-PW06 + S33-PW08` as receiver/localization support only. They do not replace exact evaluation on the physical local locus.

Work one `(place, class, physical-locus)` evaluation block at a time. Each commit records the exact image and constancy/nonconstancy certificate. Close only after the complete evaluation table is covered.

### D4 — Stage33-42 adelic compatibility

Arsenal: `×` no direct card currently closes the final adelic compatibility/reciprocity assembly. Use exact local images from D3 and prove the required compatibility directly.

Assemble the exact local images under reciprocity, compute the final Brauer disposition for the frozen Stage33 scope, and keep this separate from endpoint promotion.

### D5 — hostile audit and endpoint promotion gate

Arsenal: `△ S30-WF02 + S30-WF03`. Use exact-head layered replay and the credit firewall; workflow PASS alone cannot create missing mathematical endpoint content.

Run the required final hostile audit at an exact head. Only a passing authority transition may grant Stage33 completion/endpoint credit. Perfect-cuboid existence or nonexistence remains forbidden unless a separate explicit audited full-endpoint certificate authorizes it.

## Batch selection rule

At the start of every `stage33main batch`:

1. read live controller/state;
2. identify the first roadmap item whose prerequisites are satisfied and whose acceptance is not yet certified;
3. identify that item's exact missing object/weapon type, consult `docs/arsenal/index.json`, then read only the card(s) named by that item's `Arsenal` line and revalidate them against live Stage33 authority;
4. work only that item, preferring the applicable Arsenal route before inventing a new route;
5. commit it;
6. if enough context remains, proceed to the next item as a new commit and repeat the Arsenal check for that item.

Never skip forward because a later calculation looks easier. Never reopen a completed item without a new contradiction, failed verifier, hostile-audit finding, or changed authoritative input. Arsenal routing never overrides the controller/source-locks, and an Arsenal miss never authorizes an absence claim.
