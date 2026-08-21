# Stage16-29 Population / Condition-Interaction Roadmap

Status: **canonical roadmap for Stage16-29**.

This document is the authoritative roadmap for the Stage16-29 population program. Stage27 is the repository-defined `Stage18 -> Stage19` strict reattack, Stage28 is the `Stage19 -> Stage20` bridge comparison, and Stage29 is the cross-stage synthesis / new-foundation screening / endpoint-routing stage.

The common operational dependencies are:

- `docs/stage16-29-execution-controller-template.md`
- `docs/stage16-29-github-write-policy.md`
- `docs/stage16-29-reuse-preflight.md`
- `docs/stage16-29-stage70-policy.md`

## Canonical population states

| Stage | Population state | Primary question |
|---|---|---|
| **Stage16** | exactly one integer face diagonal | Why is the one-face population abundant, and what are its natural parameter freedoms? |
| **Stage16S** | auxiliary space-diagonal baseline | How large is the population with integral space diagonal before any integer-face condition is imposed? |
| **Stage17** | one integer face diagonal + integer space diagonal | What does the space-diagonal condition remove from Stage16? |
| **Stage18** | exactly two integer face diagonals | Why does adding the second integer face diagonal thin Stage16 so strongly? |
| **Stage19** | exactly two integer face diagonals + integer space diagonal | Determine the true growth scale and sharpen the certified bounds for the Stage14/15 target population. |
| **Stage20** | three integer face diagonals (Euler cuboids), no space-diagonal requirement | Establish and sharpen the Euler-cuboid population baseline. |

`Stage16S` remains an auxiliary parallel baseline and does not change the numbered sequence.

## Canonical transition / comparison stages

Stages through Stage26 retain their already established contracts. The numbering correction begins at Stage27.

| Stage | Transition / comparison | Canonical role |
|---|---|---|
| **Stage21** | **16 -> 17**, compared against **16S** | space-diagonal cost after one face |
| **Stage22** | **16 -> 18** | second-face cost from the one-face population |
| **Stage23** | **17 -> 19** | second-face cost with space integrality already imposed |
| **Stage24** | **18 -> 19** | original two-face-to-two-face-plus-space comparison |
| **Stage25** | **16 -> 19** | combined thinning and double-charge analysis |
| **Stage26** | **18 -> 20** | two-face to Euler comparison |
| **Stage27** | **18 -> 19** | strict research reattack/closure of the two-face-to-space-survivor transition |
| **Stage28** | **19 -> 20** | matched Stage19/Stage20 bridge comparison under common cutoff/canonicalization |
| **Stage29** | **cross-stage synthesis** | screen for genuinely new foundations, synthesize condition interaction, and route the direct perfect-cuboid endpoint attack |

### Stage27 authority

`stages/stage27/27-controller.json` is authoritative for Stage27. Its frozen transition is:

```text
Stage18 -> Stage19
```

Historical Stage27 paths containing `27-20-*` are provenance inside Stage27 and are not evidence that the stage-level transition is Stage19 -> Stage20. Do not bulk-renumber historical artifacts.

### Stage28 contract

Stage28 compares

```text
SOURCE_POPULATION = Stage19 population
TARGET_POPULATION = Stage20 population
COMPARISON         = Stage19 -> Stage20
```

Stage19 and Stage20 are not a literal subset transition: Stage19 has exactly two integral faces plus integral space diagonal, while Stage20 has exactly three integral faces and no space requirement. Ratios must therefore preserve matched-population/common-host semantics and must not be interpreted automatically as objectwise survival probabilities.

Stage28 keeps the ordinary checkpoint sequence:

```text
Stage28-10,20,30,40,50,60,70
Stage28-main-batch
Stage28-audit
```

It must preserve the distinction between certified bounds and true asymptotic exponents.

### Stage29 contract — exception to the old checkpoint template

Stage29 is deliberately different from the Stage16-28 population/transition stages. It does **not** use the fixed 10/20/30/40/50/60/70 template. Its execution authority is:

`stages/stage29/roadmap.md`.

Stage29 uses ordinary incremental numbering:

```text
Stage29-01, Stage29-02, Stage29-03, ...
Stage29-main-batch
Stage29-audit
```

Its job is not merely to restate upper/lower bounds. Before endpoint routing it must ask whether Stage16-28 missed any materially different foundation or coordinate system that could change the problem.

The required early new-foundation lenses include:

1. **global perfect-cuboid geometry** — study the simultaneous endpoint equations as one global algebraic object and relate it to the Stage18/19/20 toric/K3 models;
2. **joint completion cover / fiber product** — study the simultaneous space-completion and third-face-completion covers over the common base rather than only their separate marginals;
3. **parametrization coverage atlas** — treat the major parametrizations/families as maps into the common physical or endpoint geometry and record their actual image dimension, degree/fiber, height distortion, and coverage;
4. **joint local arithmetic** — study the two endpoint completion predicates simultaneously at finite primes, including exact intersection densities/correlation and any new local-global receiver.

These are examples of **new foundations**, not licenses to replay old frozen gates.

### Stage29 targeted-backflow rule

Stage29 first screens Stage16-28 broadly. If that screening reveals that a genuinely new foundation is load-bearing, work may return to the relevant original stage as a narrow addendum/reentry. There is no requirement to create `29-16`, `29-17`, ... or to rerun every stage sequentially.

A Stage16-28 backflow is allowed only when Stage29 supplies a materially new receiver, for example:

- a new exact equation/model;
- a changed receiver;
- a new zero-loss adapter;
- a new invariant/quotient/fibration;
- a theorem species genuinely unavailable when the old route was frozen.

After audit, the result is imported back into Stage29 once.

```text
BROAD_SCREEN_IN_STAGE29=true
SEQUENTIAL_STAGE16_TO_STAGE28_RERUN=false
TARGETED_BACKFLOW_IF_NEW_FOUNDATION=true
OLD_FROZEN_GATE_REPLAY_WITHOUT_NEW_INPUT=false
BACKFLOW_RESULT_REIMPORTED_ONCE=true
```

### Stage29 primary outputs

Stage29 should ultimately produce:

1. a common-cutoff certified population/transition ledger;
2. a dependency/overlap ledger preventing double charge;
3. a verdict on whether new foundations were found and whether targeted backflow was necessary;
4. a global endpoint geometry model and/or joint-cover model;
5. a parametrization coverage atlas and joint-local arithmetic ledger where useful;
6. comparison of three endpoint descriptions:
   - Stage19 + third face;
   - Stage20 + space diagonal;
   - direct global/joint endpoint model;
7. a strongest-certified upper/lower/mechanism ledger with true-exponent status explicit;
8. a small set of precise residual receivers for a later direct perfect-cuboid attack stage.

## Common completion gates for Stage16-28

Stages16-28 use the standard StageX checkpoints when their own controller does not state otherwise:

- `10`: population/comparison contract;
- `20`: finite-data baseline;
- `30`: ratio/thinning/comparison law;
- `40`: strongest certified upper-bound ledger;
- `50`: strongest certified lower-bound/construction ledger;
- `60`: causal decomposition and double-charge check;
- `70`: bounded maximal synthesis, intrinsic-status classification, artifact/arsenal decision, and closeout synchronization.

**Stage29 is explicitly exempt from this fixed sequence.**

Every stage must keep `PROVED`, `LITERATURE`, `COMPUTED`, and `HEURISTIC` evidence separate. An audited `OPEN_GATE` is a legitimate endpoint when the missing input is precisely identified. Re-running the same route without a genuinely new theorem, dataset, reusable weapon, model, or adapter is not progress.

## Deep-exploration rule before OPEN_GATE / closeout

An unresolved route must not be converted immediately into `OPEN_GATE` or closeout merely because the first attack fails. Before declaring that genuinely new external input is required, perform bounded but aggressive exploration of materially distinct repo-native routes when reasonable.

Relevant viewpoints include:

- alternate exact identities, eliminations, factorizations, parameterizations, fibrations, covers, quotient geometries, and height normalizations;
- arithmetic, geometric, analytic, sieve, incidence/determinant, correlation/moment, local-global, rational-point, and construction viewpoints that are genuinely distinct rather than renamed copies of the same gate;
- repository-wide Arsenal / StructureRadar / prior-stage / supplement / archive rematches against the exact receiver and physical measure;
- upper and lower routes separately, including attempts to change the obstruction rather than only sharpen the same estimate;
- bounded targeted computation when it can distinguish routes or expose a structural lead, without promoting finite evidence to an asymptotic theorem.

The AI/controller should choose promising unexplored routes proactively. Blind repetition, cosmetic renaming, or repeatedly re-running a theorem gate with no new structural input is forbidden.

A stage may freeze an unresolved lane only after the obstruction is narrow enough to state a concrete theorem/construction/adapter receiver with explicit population, measure, quantifiers, parameter ranges, and required strength. For literature-dependent gates, a research-request-ready receiver is sufficient; unbounded external research is not required before closeout.

```text
UNRESOLVED_FIRST_ROUTE_FAILED => CONTINUE_MATERIALLY_DISTINCT_INTERNAL_EXPLORATION
AI_PROACTIVE_ROUTE_SELECTION_REQUIRED=true
RENAMED_OR_DUPLICATE_ROUTE_COUNTS_AS_PROGRESS=false
OPEN_GATE_REQUIRES_PRECISE_RECEIVER=true
LITERATURE_GATE_TARGET=RESEARCH_REQUEST_READY
UNBOUNDED_EXTERNAL_RESEARCH_REQUIRED_BEFORE_CLOSE=false
```

## Stage16S population contract and role

Stage16S studies primitive/canonical positive cuboids under compatible size and symmetry conventions with

```text
SPACE_AT_LEAST = integer space diagonal, no face-diagonal restriction
SPACE_ONLY     = integer space diagonal and zero integer face diagonals
```

It is an auxiliary parallel baseline, not a mandatory serial stage. Its role is to separate the intrinsic cost of space-diagonal integrality from interaction costs after face conditions are imposed.

## Repository-wide reuse and audit safety

Every `StageX-main-batch` in Stage16-29 and Stage16S must run the bounded repository-wide preflight defined in `docs/stage16-29-reuse-preflight.md` before opening new theorem, construction, computation, or literature work. Numerical work must also inspect `docs/stage14-num-reuse-index.md` when applicable.

For Stage29 this preflight is **standing** throughout the stage. The later concentrated endpoint-Arsenal rematch supplements rather than replaces the standing reuse check.

Audit verdicts are durable repository state. A canonical audit PASS must be persisted to the relevant audit record/controller/status surfaces before it is reported as authoritative. Repository write mechanics are governed by `docs/stage16-29-github-write-policy.md` and must not change mathematical claims or audit semantics.

Every `StageX-audit` must update the audited pull request's main PR description/body so that the authoritative post-audit state is visible without relying only on Conversation comments. The body must record at least the audit verdict, repair status, `MERGE_ALLOWED`, advancement status / next item, and `NEXT_EXPECTED_COMMAND`.

```text
AUDIT_RESULT_MUST_BE_PUBLISHED_TO_PR_BODY=true
AUDIT_PR_MINIMUM_FIELDS=AUDIT_VERDICT,REPAIR_REQUIRED,MERGE_ALLOWED,ADVANCE_STATUS,NEXT_EXPECTED_COMMAND
POST_AUDIT_PR_BODY_IS_AUTHORITATIVE=true
PR_DESCRIPTION_REWRITE_REQUIRED=true
COMMENT_ONLY_AUDIT_STATUS_SUFFICIENT=false
```

For Stage16-28, StageX-70 follows `docs/stage16-29-stage70-policy.md`. Stage29 instead follows its own incremental roadmap and final gap scan before closeout.

## Stage20 literature reuse rule

Stage20 may begin with more pre-filled material than earlier population stages because Euler cuboids have substantial literature and strong prior repository results. Inherited constructions and estimates must still be adapted to the common cutoff and population contract; an infinite family is not automatically a matched asymptotic lower bound.

## Stage19 carry-over

Stage19 must preserve the distinction between the certified upper bound for the two-face + space-diagonal population, the independent causal zero-density mechanism, and the still-open questions of a matching lower bound and true growth exponent. No later stage may silently treat the half-power upper exponent as a known asymptotic law.

## Endpoint remains deferred

The perfect-cuboid population — three integral face diagonals plus an integral space diagonal — remains outside the Stage16-29 population numbering. Stage29 may study its exact global/joint geometry and local arithmetic for routing purposes, but it must not assume existence or nonexistence and need not produce an endpoint count theorem.

## Migration rule

The legacy full-roadmap label `Stage16-28` is obsolete for current operational scope and is replaced by `Stage16-29`. Historical stage/checkpoint identifiers remain unchanged when they represent genuine provenance.
