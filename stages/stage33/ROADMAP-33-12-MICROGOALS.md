# Stage33 33-12 micro-goal execution roadmap

```text
ROLE=PLANNING_AND_EXECUTION_CHECKLIST_ONLY
LIVE_AUTHORITY=stages/stage33/controller.json + stages/stage33/MAIN-STATE.json
CURRENT_LOCKED_FRONTIER=V41_THROUGH_V53
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
- V43 records that reviewed interfaces do not yet provide an exact reusable proper14-to-Cech/full-surface `H2(mu2)` adapter for e3.
- V45 locks the proper14 and working-boundary 14-element ordered lists as two separate presentations only.
- V47's proposed 14x14 `P_W` construction is historical and superseded.
- V48-V49 test the PW05/equivariant interpretation and reject the naive divisor-package bridge.
- V50 proves the decisive type correction: the boundary residue source is the Stage-A `F2^26` squareclass-tensor domain, not the coefficient module `K=Br(Sbar)[2]`; therefore the proposed working14-to-proper14 `P_W` is the wrong object type.
- V51 rewires the active e3 route to the reusable V25 pattern: independent Brauer source -> concrete Cech `H2(mu2)` preimage -> exact marked Brauer-image binding -> exact pullback/naturality when available -> downstream Kummer computation.
- V52 source-locks the bounded A2 miss: the current literal Cech object `{f2,g22}` and semantic orientation are J2-specific, while the marked Picard/adjoint interfaces do not materialize a literal function/divisor/transition preimage for e3 proper14 mask `20`. This is not a repository-absence or nonexistence claim.
- V53 computes the exact degree-2 Picard-adjoint image of mask `20=axis3+axis5`: marked half-lattice numerator `[1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0]` with semantic projection `[1,0]`. This is a marked adjoint candidate only, not a genuine full-surface Cech `H2(mu2)` lift; equality of the 2D projection with J2 does not identify e3 with J2.
- Stage33 remains at `6/11`; Stage33-12 is not exactly closed; Stage33-13 is not released.

## Phase A — finish one independent e3 column

### A1 — lock the e3 source and the valid lift-construction route

#### A1.0 — independent e3 proper14 source lock — PASS V41

Arsenal: `○ S33-PW04 + S30-WF02`. Use only for marked-coordinate/provenance discipline; no boundary-source bridge is implied.

Acceptance already certified:
- retained10 standard mask `4`;
- proper14 mask `20`, support `{3,5}`;
- source derived independently from the exact V4-fixed proper Br[2] basis;
- no `J2=e2+e3` split.

#### A1.1 — retire the invalid boundary14 -> proper14 bridge route — PASS V45-V50

Arsenal: `◎ S33-PW05 + S30-W01/S30-WF01 + S33-PW04` was tested only as a candidate identification route. V50 controls the final type judgment. `S30-WF03` prevents finite/zero connecting data from being promoted across semantic layers.

Acceptance already certified:
- V45 keeps the two 14-element ordered lists separate;
- V49 rejects the naive divisor-package equivariant isomorphism;
- V50 proves `P_W` is `RETIRED_WRONG_OBJECT_TYPE`;
- V47's 14-column construction contract is superseded;
- no positional identification or arbitrary equivariant intertwiner is authorized.

Historical note: the V45 basis metadata remains valid provenance. It must not be read as a basis identification.

#### A1.2 — rewire to the direct V25 source-bound Cech route — PASS V51

Arsenal: `◎ S33-PW07 + S33-PW04`, `△ S30-WF03`; `S33-PW08` is conditional only if the chosen representative is actually constructed through Gersten/residue data.

Acceptance already certified:
- reusable V25 pattern is separated from J2-specific data;
- J2-specific `beta1`, marked coordinate `[1,0]`, proper14 mask `25`, and `{f2,g22}`/`lambda_D` are not reusable as e3 data;
- the required Brauer image is proper14 mask `20` / retained10 standard mask `4`;
- direct PW05 14D bridge routing remains disabled.

A1 is complete at V51.

### A2 — materialize an explicit source-bound e3 Cech `H2(mu2)` preimage

Arsenal: `◎ S33-PW07 + S33-PW04`, with `S33-PW08` only when the construction genuinely factors through Gersten/residue data. `S30-W02` may be used only if a semilinear descent step satisfies its exact hypotheses.

#### A2.0 — bounded literal/marked interface classification — PASS-BLOCKED V52

V52 certifies the exact current obstruction without promoting an absence theorem:
- J2 has a literal source-bound Cech representative `{f2,g22}` with its own residue/resolution audit;
- J2 semantic orientation is source-specific and cannot bind e3 mask `20` by relabelling;
- exact Picard adjoint/marked-Picard data exist but do not materialize the required e3 literal function/divisor/transition representative;
- proper14 action-axis positions do not license reconstruction of a branch subset `D`;
- the smallest missing datum is one source-specific marked geometric Cech preimage whose exact Brauer image is proper14 mask `20` / retained10 mask `4`.

#### A2.1 — materialize the exact mask20 marked Picard-adjoint candidate — PASS V53

Arsenal: `◎ S33-PW04`, with `S30-WF03` as the promotion firewall. PW04 licenses exact marked-coordinate transport only; it does not turn the output into literal Cech geometry.

Acceptance already certified:
- mask `20` is recomputed from proper14 support `{3,5}`;
- exact degree-2 Picard-adjoint output is the 20D half-lattice numerator `[1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0]`;
- semantic projection is `[1,0]`;
- the output scope is `DEGREE2_PICARD_ADJOINT_MARKED_CANDIDATE_ONLY`;
- the coincident J2 semantic projection `[1,0]` is explicitly not promoted to an e3=J2 identification;
- no literal function/divisor/transition data, genuine full-surface `H2(mu2)` lift, or e3 Kummer column is claimed.

#### A2.2 — realize the V53 marked candidate as source-specific full-surface Cech geometry — CURRENT

Arsenal: `◎ S33-PW07 + S33-PW04`. PW07 governs literal transition/divisor/Cartier/common-cocycle realization; PW04 governs the exact marked binding back to V41 e3. `S30-WF03` blocks promotion across either missing layer.

Goal: realize the exact V53 20D marked Picard-adjoint candidate by literal function/divisor/transition data, or a mechanically equivalent exact geometric adapter, and certify a genuine full-surface `H2(mu2)` preimage with Brauer image V41 e3.

Acceptance:
- concrete cocycle/symbol/overlap or mechanically equivalent geometric representative is materialized;
- the construction maps to the exact V53 20D marked candidate under the source-locked marked Picard/adjoint interface;
- full-surface scope, field, domains, branch/support data, and source locks are explicit;
- exact Brauer image is proper14 mask `20` / retained10 mask `4`;
- no J2 `{f2,g22}` relabelling, no `[1,0]` semantic-projection shortcut, no branch inference from axes 3/5, and no boundary-residue/proper14 positional identification;
- if the realization exposes a smaller missing transition/divisor/function datum, name that datum exactly and make it the next leaf.

Current next exact leaf:
`E3_V25_S1B_REALIZE_MASK20_PICARD_ADJOINT_CANDIDATE_AS_SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_CLASS`.

A2 is not complete until A2.2 passes.

### A3 — residue and resolution audit of the concrete e3 representative

Arsenal: `◎ S33-PW07`; `◎ S33-PW08` only for an actual Gersten/residue realization.

Goal: verify that the A2 object extends with the required full-surface unramified scope.

Acceptance PASS branch:
- complete relevant codimension-one/resolution support is certified;
- every required residue/square trivialization is exact;
- exceptional contributions are included where applicable.

Acceptance FAIL branch:
- exact nonzero residue support is listed;
- the next item is the finite correction problem on that support, not broad search.

### A4 — bind the residue-clean lift to exact e3

Arsenal: `◎ S33-PW04 + S33-PW07`, with `S30-WF03` enforcing the credit boundary. Use `S33-PW05` only if an independently defined source-target module compatibility check is genuinely required; do not resurrect the retired 14D bridge.

Goal: prove that the A2/A3 lift maps to V41 e3, not merely to a nonzero Brauer class or a J2-related class.

Acceptance:
- Brauer image equals proper14 mask `20` / retained10 mask `4` under an explicit checked marked adapter;
- independence from `J2=e2+e3` splitting is certified;
- the full-surface `H2(mu2)` scope is exact;
- this is the first point at which `GENUINE_FULL_SURFACE_H2_MU2_LIFT_FOR_E3=true` may be recorded.

### A5 — compute the e3 Kummer column

Arsenal: `◎ S33-PW05`, with `S33-PW02` as extension/liftability support where mixed-order source data enter.

Goal: apply the exact Kummer target map to the A4 source-bound lift.

Acceptance:
- target basis/order locked;
- full target column explicit;
- replay recomputes the column from the A4 lift;
- no guessed standard col2/col3 decomposition.

### A6 — integrate and audit the `2/10` adapted-column frontier

Arsenal: `△ S30-WF02 + S30-WF03`.

Goal: update the live Stage33 frontier only after A1-A5 pass.

Acceptance:
- J2-adapted columns materialized becomes `2/10`;
- original standard columns remain credited only when individually justified;
- controller/state/certificate projection agree;
- dedicated exact-head CI passes before further source work.

## Phase B — finish the remaining adapted sources

Process sources in the locked priority order after e3:

`e1, e4, e5, e6, e7, e8, e9, e10`.

For each source `s`, use the V50/V53-corrected atomic sequence. Do not recreate a proper14 -> boundary-source `P_W` bridge:

- B(s).0 lock the independent proper14/retained10 source coordinate — `○ S33-PW04 + S30-WF02`;
- B(s).1 materialize the exact marked Picard-adjoint candidate when the source-locked adjoint applies — `◎ S33-PW04`, with `S30-WF03`;
- B(s).2 realize a concrete source-bound Cech `H2(mu2)` representative — `◎ S33-PW07 + S33-PW04`; `S33-PW08` conditional on a genuine Gersten construction;
- B(s).3 residue/resolution audit — `◎ S33-PW07`, and `S33-PW08` when its valuation/purity hypotheses apply;
- B(s).4 exact Brauer-image/full-surface-lift binding to `s` — `◎ S33-PW04 + S33-PW07`, with `S30-WF03`;
- B(s).5 exact Kummer column — `◎ S33-PW05`, support `S33-PW02` where extension/liftability data are relevant;
- B(s).6 frontier integration and exact-head replay — `△ S30-WF02 + S30-WF03`.

If A2-A4 establish a genuinely linear reusable direct Cech/source-binding adapter for arbitrary proper14 inputs, later B(s) items may reuse it, but each source still requires a separate instantiation/binding/column certificate. Reuse must be explicit; do not infer a boundary-source basis identification and do not collapse multiple source credits into one batch.

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