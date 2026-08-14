# Stage16-28 Population / Condition-Interaction Roadmap

Status: **future roadmap after Stage15 closure**.

This roadmap does not reopen Stage15-6 and does not assign a stage number to the
perfect-cuboid endpoint. Its purpose is to understand, one condition at a time,
how integer-face and integer-space-diagonal conditions change the population of
primitive/canonical cuboids.

## Core research question

For each condition transition, determine:

1. the source population under a common size cutoff;
2. the survivor population after adding the new condition;
3. the survivor ratio as the cutoff grows;
4. upper and lower bounds where available;
5. whether an observed exponent is intrinsic or only the best current bound;
6. the arithmetic mechanism that causes the loss;
7. whether that mechanism is genuinely new or already charged by an earlier condition.

The intended output is a condition-by-condition **population map**, not merely a
sequence of existence/nonexistence tests.

## Population states

| Stage | Population state | Primary question |
|---|---|---|
| **Stage16** | exactly one integer face diagonal | Why is the one-face population abundant, and what are its natural parameter freedoms? |
| **Stage16S** | auxiliary space-diagonal baseline | How large is the population with integral space diagonal before any integer-face condition is imposed, and how much changes when all integer-face cases are excluded? |
| **Stage17** | one integer face diagonal + integer space diagonal | What does the space-diagonal condition remove from the Stage16 population? |
| **Stage18** | exactly two integer face diagonals | Why does adding the second integer face diagonal thin the Stage16 population so strongly? |
| **Stage19** | exactly two integer face diagonals + integer space diagonal | Re-express the Stage14/15 population with matched upper/lower/causal questions; in particular test whether the current half-power upper exponent is intrinsic. |
| **Stage20** | three integer face diagonals (Euler cuboids) | Establish the Euler-cuboid population baseline, using the large existing literature as an input rather than rediscovering it. |

The numbered stages remain the primary roadmap. `Stage16S` is an **auxiliary
parallel baseline**, not a renumbering or a mandatory serial stage between Stage16
and Stage17. It exists because the roadmap needs a control population for the
space-diagonal condition itself, independent of pre-existing integer-face
conditions.

### Stage16S population contract and role

Stage16S studies primitive/canonical positive cuboids under the same compatible
size and symmetry conventions used by the Stage16-28 roadmap, with

```text
SPACE_AT_LEAST = integer space diagonal, no face-diagonal restriction
SPACE_ONLY     = integer space diagonal and zero integer face diagonals
```

The stage should determine both populations when feasible. This separates the
intrinsic cost of imposing

```text
a^2 + b^2 + c^2 = d^2
```

from the interaction cost that appears when the same condition is imposed after
one or more integer-face conditions have already been charged.

Stage16S uses the ordinary checkpoint sequence
`16S-10,20,30,40,50,60,70` and the canonical commands
`Stage16S-main-batch` and `Stage16S-audit`.

Stage16S may run in parallel once the common population/cutoff conventions needed
for comparison are frozen. It must not block routine progress of Stage17 or
Stage18 merely because its analysis is difficult. However, Stage21 may not close
its final causal claim that the space-diagonal condition is intrinsically strong,
weak, independent, or interaction-dependent unless the relevant Stage16S baseline
has been audited. If Stage16S remains unresolved at that point, Stage21 must record
the missing comparison as an explicit `OPEN_GATE` rather than guess.

These are population states, not a claim that the project must traverse them in a
single linear chain.

## Transition / thinning stages

After the primary populations and the auxiliary Stage16S control baseline are
available under compatible conventions, study the meaningful arrows between them
as separate research objects.

| Stage | Transition | Main question |
|---|---|---|
| **Stage21** | **16 -> 17**, compared against **16S** | How much does the space-diagonal condition thin the one-face population, why, and how does that cost compare with the intrinsic space-diagonal baseline? |
| **Stage22** | **16 -> 18** | How much does the second face condition thin the one-face population, and why? |
| **Stage23** | **17 -> 19** | With the space diagonal already integral, how much additional thinning comes from the second face condition? |
| **Stage24** | **18 -> 19** | With two faces already integral, how much additional thinning comes from the space diagonal? This is the natural Stage15 comparison to deepen. |
| **Stage25** | **16 -> 19** | What is the combined thinning from one face to two faces plus space diagonal, and can the separate mechanisms be disentangled without double counting? |
| **Stage26** | **18 -> 20** | How much does the third face condition thin the two-face population, and what new arithmetic obstruction appears? |
| **Stage27** | **16 -> 20** | What is the total thinning from one face to Euler cuboids, and which intermediate condition accounts for which part? |
| **Stage28** | interaction synthesis | Compare all established transition laws and identify condition independence, dependence, overlap, and the dominant population-killing mechanisms. |

## Key comparison square

```text
                 + space diagonal
Stage16  ------------------------------>  Stage17
   |                                        |
   | + second integer face                 | + second integer face
   v                                        v
Stage18  ------------------------------>  Stage19
                 + space diagonal
```

This square is a priority because it separates two questions that are easy to
confuse:

- Is the space-diagonal condition intrinsically strong, or does it become strong
  only after two faces are already integral?
- Is the second-face condition intrinsically strong, or does its effect change
  when the space diagonal is already integral?

Comparing `16->17` with `18->19`, and `16->18` with `17->19`, is the cleanest
way to test those interactions.

Stage16S adds a lower control comparison:

```text
Ambient primitive/canonical cuboids
        |                         |
        | + one integer face      | + integer space diagonal
        v                         v
     Stage16                  Stage16S
        |                         |
        | + space diagonal        | + one integer face
        v                         v
                Stage17 target
```

The two paths need not have equal conditional cost. Their purpose is to test
whether a thinning attributed to the space diagonal is already typical in the
ambient population or emerges only after an integer-face condition has reshaped
the arithmetic population.

## Common stage completion gates

Every Stage16-28 stage, including auxiliary Stage16S, should use the same numbered
checkpoints. Existing literature may pre-fill a checkpoint, but it must still be
translated into the project's common population/cutoff conventions before being
marked complete.

| Checkpoint | Required output | Closure question |
|---|---|---|
| **StageX-10** | population contract | What exactly is being counted? Fix primitive/canonical conventions, symmetry removal, cutoff, and source/target definitions. |
| **StageX-20** | finite-data baseline | How many objects are observed as the cutoff grows, and are the enumerators/replay checks trustworthy? |
| **StageX-30** | ratio / thinning law | What fraction survives the added condition, and does that ratio appear constant, logarithmically small, polynomially small, or zero-density? |
| **StageX-40** | upper-bound ledger | What is the strongest certified upper bound, and which mechanism pays for it? |
| **StageX-50** | lower-bound / construction ledger | How large a family can definitely be constructed, and what lower bound does it imply under the common cutoff? |
| **StageX-60** | causal decomposition | Why does the population decrease? Identify the actual arithmetic restrictions and distinguish new constraints from reformulations of earlier ones. |
| **StageX-70** | bounded maximal synthesis / intrinsic status / closeout | Using the certified StageX-10 through StageX-60 material, what additional consequences, reinterpretations, refinements, and causal comparisons can be extracted before genuinely new research is required? |

The normative bounded-synthesis stopping rule for StageX-70 is defined in
`docs/stage16-28-stage70-policy.md`. StageX-70 should exploit the certified
material aggressively, but it must stop before a substantially new theorem,
large computation, literature program, or off-stage branch becomes necessary.

A stage is considered substantively closed only when all seven checkpoints have
an explicit status: `PROVED`, `COMPUTED`, `LITERATURE_ADAPTED`, `OPEN_GATE`, or
`NOT_APPLICABLE`. A checkpoint does not need a positive theorem to be complete;
a precise, audited `OPEN_GATE` is an acceptable research result when the missing
input is identified.

This gate structure is intended to make the project stop condition explicit: a
stage advances when its known facts, quantitative bounds, causal explanation,
and remaining unknowns have all been classified rather than when a promising
route merely runs out of ideas.

## Stage-end artifact decisions

At `StageX-70`, the AI/controller must also decide whether the stage deserves a
self-contained final bundle and whether any result deserves promotion into the
reusable arsenal. These are **judgment calls made from the stage evidence**, not
blanket requirements for every stage.

Required closeout fields:

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES|NO
SELF_CONTAINED_BUNDLE_REASON=
ARSENAL_PROMOTION_REQUIRED=YES|NO
ARSENAL_CANDIDATES=
```

### Self-contained bundle rule

Default to `NO` when the stage mainly adapts standard literature, records routine
finite data, or closes with no result that future stages need to cite as a single
stable theorem package.

Prefer `YES` when one or more of the following holds:

- the stage proves a new major theorem or quantitatively sharp population law;
- the stage combines several earlier stages into a result whose assumptions would
  otherwise be easy to misstate;
- the result is expected to be cited repeatedly by later stages;
- external adversarial review needs one stable self-contained object;
- a subtle distinction between proved, conditional, numerical, and open claims
  would be unsafe to reconstruct from scattered task files.

The AI/controller records the reason. The existence of a stage alone never forces
a self-contained HTML or equivalent bundle.

### Arsenal promotion rule

The arsenal is for **portable research weapons**, not for everything that was
important inside one stage. Promotion is based primarily on expected reuse in a
different stage.

Strong promotion candidates include:

- reusable lemmas, theorems, inequalities, and asymptotic adapters;
- parametrizations, normal forms, coordinate changes, and factor decompositions;
- general congruence, squareclass, valuation, or local restrictions;
- reusable upper-bound or lower-bound mechanisms;
- negative certificates showing that a whole route cannot deliver a specified
  target without an additional theorem;
- verifiers, enumerators, replay procedures, or search reductions that transfer
  to another population;
- warnings about cutoff mismatch, symmetry, primitivity, double counting, or
  invalid theorem transfer that future stages are likely to encounter again.

Do **not** promote by default:

- one-stage numerical tables or transient experimental observations;
- intermediate calculations already subsumed by the final theorem;
- a stage-specific restatement of an existing arsenal item;
- speculative or unaudited ideas;
- bulky provenance whose only purpose is historical reconstruction.

Every promoted item should carry a compact contract:

```text
NAME=
TYPE=lemma|theorem|method|obstruction|verifier|warning|adapter
SOURCE_STAGE=
ASSUMPTIONS=
VALID_RANGE=
WHAT_IT_DOES=
WHAT_IT_DOES_NOT_DO=
POTENTIAL_RECEIVERS=
AUDIT_STATUS=
```

`WHAT_IT_DOES_NOT_DO` is mandatory for nontrivial mathematical weapons. This is
intended to prevent a later stage from silently strengthening a theorem or using
a mechanism outside its certified range.

A stage may therefore close in any of these legitimate states:

```text
BUNDLE=NO,  ARSENAL=NO   # useful stage, no portable artifact needed
BUNDLE=YES, ARSENAL=NO   # important fixed record, but stage-specific
BUNDLE=NO,  ARSENAL=YES  # portable weapon, no large final bundle needed
BUNDLE=YES, ARSENAL=YES  # major result with reusable components
```

## Stage20 literature reuse rule

Stage20 is expected to begin with more pre-filled checkpoints than the earlier
population stages because Euler cuboids have a large existing literature. In
particular, parameter families, explicit constructions, computational data, and
several arithmetic reformulations may populate parts of `20-10`, `20-20`,
`20-50`, and `20-60`.

Those inherited results must not be treated as automatically solving the
population problem. The project still needs to adapt them to the common cutoff
and determine `20-30`, `20-40`, `20-50`, and `20-70` in the same language used
for Stages16-19. An infinite family, for example, is not automatically a matched
asymptotic lower bound.

## Stage19 special carry-over

Stage19 must preserve the distinction already established by Stage14/15:

- the certified upper bound for the two-face + space-diagonal population;
- the independent Stage15 causal zero-density mechanism;
- the still-open questions of a matching lower bound, the true growth exponent,
  and whether the current half-power exponent is intrinsic rather than merely the
  strongest proved upper exponent.

No future population stage may silently treat the half-power upper exponent as a
known asymptotic law.

## Common protocol for every transition

Every transition stage should answer the same compact checklist:

```text
SOURCE_POPULATION=
TARGET_POPULATION=
COMMON_CUTOFF=
FINITE_DATA_BASELINE=
SURVIVOR_RATIO=
RATIO_LIMIT_STATUS=
BEST_UPPER_BOUND=
BEST_LOWER_BOUND=
TRUE_EXPONENT_IDENTIFIED=
NEW_ARITHMETIC_MECHANISM=
INDEPENDENT_OF_PRIOR_CONDITIONS=
DOUBLE_CHARGE_CHECK=
EXTERNAL_THEOREM_DEPENDENCIES=
AUDIT_STATUS=
SELF_CONTAINED_BUNDLE_REQUIRED=
ARSENAL_PROMOTION_REQUIRED=
ARSENAL_CANDIDATES=
```

Numerical evidence and asymptotic theorems must remain explicitly separated.

For Stage21 specifically, `INDEPENDENT_OF_PRIOR_CONDITIONS` must be assessed
against the audited Stage16S control baseline whenever that conclusion depends on
the intrinsic strength of the space-diagonal condition.

## Deferred endpoint

The population with **three integer face diagonals plus an integer space diagonal**
is the perfect-cuboid endpoint. It is intentionally **not assigned a Stage16-28
number here**.

The working expectation to test, not assume, is that the final space-diagonal
condition may interact with the already highly constrained Euler-cuboid state far
more severely than it does in the one-face or two-face populations. The purpose
of Stages16-28 is to determine whether that expectation is supported by matched
population laws and identified arithmetic mechanisms.

Even a complete Stage16-28 map is not expected to settle the existence or
nonexistence of a perfect cuboid automatically. Its success criterion is more
modest and more useful: by the time the endpoint is opened, the project should
know which restrictions are already understood, which interactions cause the
observed thinning, which bounds are genuinely sharp or not, and exactly what new
obstruction remains at the three-face + space-diagonal boundary.

## Operational safety invariants

These rules apply across Stage16-28 and Stage16S and are intended to prevent
bookkeeping or comparison errors from masquerading as mathematical discoveries.

### 1. Freeze the common population contract

The default Stage16-28 contract for cutoff, primitivity, canonical ordering,
symmetry removal, and `exactly-one` / `exactly-two` meanings must not drift
silently between stages. Stage16S must use the same compatible conventions or a
certified comparison adapter. If any of these conventions changes, record
`POPULATION_CONTRACT_CHANGED=YES`, state the reason, and identify every earlier
stage or transition whose counts, ratios, or bounds require recomputation.

### 2. No direct ratio across incompatible populations

A survivor ratio may be reported only when source and target counts are expressed
under compatible cutoff and canonicalization conventions. If an adapter is
required, record `COMPARISON_ADAPTER_REQUIRED=YES` and certify that adapter before
using the ratio asymptotically. Raw counts from incompatible populations must not
be divided merely because they share a stage label.

### 3. Keep proof, literature, computation, and heuristic claims distinct

Every material result must carry an evidence level:

```text
EVIDENCE_LEVEL=PROVED|LITERATURE|COMPUTED|HEURISTIC
```

Large finite searches do not upgrade themselves to proofs, and a theorem does not
downgrade merely because the finite-data window is small. When a literature claim
is adapted to a new cutoff or population contract, distinguish the cited theorem
from the project's adaptation step.

### 4. Record dependency edges

Every nontrivial theorem, bound, adapter, or causal claim should record its direct
research dependencies, for example:

```text
DEPENDS_ON=Stage16-10,Stage18-40,arsenal:item-name
```

If an upstream population contract, theorem, or weapon is revised or superseded,
the controller must identify dependent stages that need re-audit rather than
assuming the change is local.

### 5. No infinite excavation of an OPEN_GATE

When a checkpoint has reached an audited `OPEN_GATE`, the same route must not be
re-run under new wording unless at least one genuinely new input has appeared:
new theorem, new data, new reusable weapon, or new external literature. Otherwise
record:

```text
NEW_INPUT_REQUIRED=true
```

and stop that route. A precisely identified missing theorem/input is a completed
research outcome for the checkpoint; repeated paraphrases are not progress.

### 6. Arsenal supersession is explicit, never destructive

A new weapon that improves or replaces an earlier item must not silently erase
its predecessor. Record `SUPERSEDES=` on the new item and `SUPERSEDED_BY=` on the
old item, then retain the old item as archive provenance unless there is a separate
repository-cleanup reason to remove it. Later stages should use the newest valid
weapon while historical dependency chains remain auditable.

### 7. Audit verdicts are durable repository state, not chat-only opinions

A canonical `StageX-audit` or `Stage16S-audit` command must not return an
authoritative `PASS` or `FAIL` merely in chat while leaving the branch/controller
in its pre-audit state. Before emitting the final verdict, the audit worker must,
when repository writes are available:

1. write the checkpoint audit record to the canonical `audit.md` location;
2. update the stage controller with the audited status and all gate fields affected
   by the verdict, including `AUDIT_STATUS`, `ADVANCE_ALLOWED`, next checkpoint or
   stage, and any `NEW_INPUT_REQUIRED` / `HUMAN_DECISION_REQUIRED` state;
3. update the current-research/status file when that stage protocol mirrors the
   controller there;
4. set `MERGE_ALLOWED` consistently when that field is part of the stage contract;
5. re-read the written state, or otherwise verify the resulting commit, before
   reporting the verdict to the user.

The chat verdict is therefore a report of already-persisted audit state. In
particular:

```text
AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
```

means the repository already records the PASS and its associated controller/status
transition. A user may rely on that PASS without first repairing stale `PENDING`
or `SUBMITTED` metadata.

A `FAIL` should likewise be persisted with its stop gates and actionable reason
before it is reported. `BLOCKED` should be persisted when possible. If an
infrastructure or write failure prevents persistence, the audit worker must not
upgrade the checkpoint to PASS in chat; it should instead report:

```text
AUDIT_VERDICT=BLOCKED
AUDIT_PERSISTENCE_STATUS=FAILED
UNSYNCED_AUDIT_STATE=<specific files/fields not written>
```

and leave advancement/merge disallowed until synchronization succeeds.

The audit command itself does **not** merge the pull request by default.
`MERGE_ALLOWED=true` means that the audited repository state permits merge; merge
execution remains a separate action unless the user explicitly requests merge in
that same instruction. This keeps audit semantics consistent across chats while
preserving the user's ability to merge after seeing a durable PASS.

At StageX-70 the controller should also report the safety state:

```text
POPULATION_CONTRACT_CHANGED=YES|NO
COMPARISON_ADAPTER_REQUIRED=YES|NO
EVIDENCE_LEVELS_COMPLETE=YES|NO
DEPENDENCY_LEDGER_COMPLETE=YES|NO
OPEN_GATE_REENTRY_JUSTIFIED=YES|NO|NOT_APPLICABLE
ARSENAL_SUPERSESSION_CHECK=PASS|FAIL|NOT_APPLICABLE
```

## Certified closeout synchronization gate

A checkpoint-70 audit PASS does not by itself complete repository closure. In the same audit-persistence change, all four canonical surfaces must be synchronized:

1. the stage controller is `CLOSED`, checkpoint 70 is `AUDITED_PASS`, and its last-audit record points to the canonical audit file;
2. the final bundle records `AUDITED_PASS_CLOSED` while preserving the submitted-candidate provenance and frozen nonclaims;
3. the manifest records checkpoint 70 as `PROVED_AUDITED_PASS` and no longer presents the bundle as awaiting audit;
4. `docs/00_CURRENT_RESEARCH_STATUS.md` registers the closed stage, controller, final bundle, manifest, final audit, and any downstream-baseline readiness flag.

Before merge, the audit-persistence step must search these surfaces for stale tokens such as `OPEN`, `PENDING`, `SUBMITTED_FOR_FRESH_AUDIT`, or `AUDIT_REQUIRED=true`. A stale closeout token makes the persistence state unsynchronized:

```text
AUDIT_PERSISTENCE_STATUS=UNSYNCED
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
```

Closure becomes valid only after all four surfaces agree and the controller records:

```text
AUDIT_PERSISTENCE_STATUS=COMMITTED
UNSYNCED_AUDIT_STATE=NONE
```

The mathematical audit result remains unchanged during a synchronization-only repair. Any edit to a frozen claim or nonclaim instead requires a fresh audit.

## Stage14 numerical observatory handoff

Stage16–28 controllers must treat `docs/stage14-num-reuse-index.md` as the canonical finite-evidence handoff. Exact Stage14 integral-space censuses may be reused directly only after population/cutoff/mask agreement; otherwise they serve as matched intersections, negative controls, software regressions, or hypothesis diagnostics. New computation requires the numerical reuse preflight defined by the execution-controller template.
