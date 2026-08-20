# Stage16-29 Population / Condition-Interaction Roadmap

Status: **canonical roadmap for Stage16-29**.

This document is the authoritative roadmap for the Stage16-29 population program. It incorporates the Stage27 numbering correction: Stage27 is the repository-defined `Stage18 -> Stage19` strict reattack, Stage28 is the `Stage19 -> Stage20` bridge comparison, and Stage29 is the interaction synthesis formerly assigned to Stage28.

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
| **Stage27** | **18 -> 19** | strict research reattack/closure of the two-face-to-space-survivor transition; repository controller contract governs |
| **Stage28** | **19 -> 20** | matched Stage19/Stage20 bridge comparison under common cutoff/canonicalization; do not assume a literal subset relation |
| **Stage29** | **interaction synthesis** | compare all certified transition laws, overlaps, dependencies, and dominant population-killing mechanisms |

### Stage27 authority

`stages/stage27/27-controller.json` is authoritative for Stage27. Its frozen transition is:

```text
Stage18 -> Stage19
```

The Stage27 work tree may contain historically named `27-20-*` checkpoint or derived-route artifacts. Those names are provenance inside Stage27 and are not evidence that the stage-level population transition is `Stage19 -> Stage20`. Do not bulk-move or renumber those historical artifacts solely because of this roadmap correction.

### Stage28 contract

Stage28 studies the relationship between the already established Stage19 and Stage20 populations under matched conventions:

```text
SOURCE_POPULATION = Stage19 population
TARGET_POPULATION = Stage20 population
COMPARISON         = Stage19 -> Stage20
```

Because Stage19 includes integral space diagonal while Stage20 is the Euler-cuboid population without a space-diagonal requirement, Stage28 must not silently describe the comparison as literal subset thinning. Checkpoint 10 must freeze the exact comparison semantics and any host/intersection adapter before ratios or exponent differences are interpreted causally.

Stage28 uses the ordinary checkpoint sequence and canonical commands:

```text
Stage28-10,20,30,40,50,60,70
Stage28-main-batch
Stage28-audit
```

The stage should reuse the audited Stage19 and Stage20 controllers/final bundles before opening new research. In particular, it must preserve the distinction between certified bounds and true asymptotic exponents.

### Stage29 contract

Stage29 inherits the former Stage28 role: interaction/exception synthesis across the completed population map. It is not a new population state and must not manufacture an extra condition merely to justify the new number.

Its primary outputs are:

1. a common-cutoff comparison table for all certified populations and transitions;
2. a dependency/overlap ledger preventing the same arithmetic restriction from being charged twice;
3. identification of condition independence, dependence, and interaction effects;
4. a strongest-certified upper/lower-bound ledger with true-exponent status kept explicit;
5. a residual-obstruction statement describing what remains before the perfect-cuboid endpoint is opened.

Stage29 uses the ordinary checkpoint sequence and commands:

```text
Stage29-10,20,30,40,50,60,70
Stage29-main-batch
Stage29-audit
```

## Common completion gates

Every Stage16-29 parent stage uses the standard StageX checkpoints:

- `10`: population/comparison contract;
- `20`: finite-data baseline;
- `30`: ratio/thinning/comparison law;
- `40`: strongest certified upper-bound ledger;
- `50`: strongest certified lower-bound/construction ledger;
- `60`: causal decomposition and double-charge check;
- `70`: bounded maximal synthesis, intrinsic-status classification, artifact/arsenal decision, and closeout synchronization.

Every checkpoint must keep `PROVED`, `LITERATURE`, `COMPUTED`, and `HEURISTIC` evidence separate. An audited `OPEN_GATE` is a legitimate endpoint when the missing input is precisely identified. Re-running the same route without a genuinely new theorem, dataset, reusable weapon, or literature input is not progress.

## Deep-exploration rule before OPEN_GATE / closeout

An unresolved checkpoint must not be converted immediately into `OPEN_GATE` or stage closeout merely because the first attempted route fails. Before declaring that genuinely new external input is required, the stage must perform a bounded but aggressive internal exploration of materially distinct routes that are reasonably available from the current repository state.

This exploration should include, when relevant:

- alternate exact identities, eliminations, factorizations, parameterizations, fibrations, covers, and height normalizations;
- arithmetic, geometric, analytic, sieve, incidence/determinant, correlation/moment, local-global, and construction viewpoints that are genuinely distinct rather than renamed copies of the same gate;
- repository-wide Arsenal / StructureRadar / prior-stage / supplement / archive rematches against the exact current receiver and physical measure;
- upper and lower routes separately, including attempts to change the obstruction rather than only sharpen the same estimate;
- bounded targeted computation when it can distinguish routes or expose a structural lead, without promoting finite evidence to an asymptotic theorem.

The AI/controller is expected to choose and pursue promising unexplored routes proactively. Operator intervention is not required merely to authorize another mathematically distinct internal attack. Conversely, blind repetition, cosmetic renaming, or repeatedly re-running a theorem gate with no new structural input remains forbidden.

A stage may freeze an unresolved research lane only after the remaining obstruction has been narrowed enough that the missing input can be stated as a concrete theorem/construction/adapter receiver with explicit population, measure, quantifiers, parameter ranges, and required strength. For literature-dependent gates, the preferred stopping point is strong enough to write a detailed external-research request specifying what theorem species must be found, what existing near-misses are insufficient, and exactly what would discharge the receiver. Reaching that "research-request-ready" state is sufficient; actually conducting an unbounded new literature program inside the stage is not required.

```text
UNRESOLVED_FIRST_ROUTE_FAILED => CONTINUE_MATERIALLY_DISTINCT_INTERNAL_EXPLORATION
AI_PROACTIVE_ROUTE_SELECTION_REQUIRED=true
RENAMED_OR_DUPLICATE_ROUTE_COUNTS_AS_PROGRESS=false
OPEN_GATE_REQUIRES_PRECISE_RECEIVER=true
LITERATURE_GATE_TARGET=RESEARCH_REQUEST_READY
UNBOUNDED_EXTERNAL_RESEARCH_REQUIRED_BEFORE_CLOSE=false
```

## Stage16S population contract and role

Stage16S studies primitive/canonical positive cuboids under the same compatible size and symmetry conventions used by the Stage16-29 roadmap, with

```text
SPACE_AT_LEAST = integer space diagonal, no face-diagonal restriction
SPACE_ONLY     = integer space diagonal and zero integer face diagonals
```

It is an auxiliary parallel baseline, not a renumbering or mandatory serial stage. It exists to separate the intrinsic cost of space-diagonal integrality from interaction costs after face conditions have already been imposed.

## Repository-wide reuse and audit safety

Every `StageX-main-batch` in Stage16-29 and Stage16S must run the bounded repository-wide preflight defined in `docs/stage16-29-reuse-preflight.md` before opening new theorem, construction, computation, or literature work. Numerical work must also inspect `docs/stage14-num-reuse-index.md` when applicable.

Audit verdicts are durable repository state. A canonical audit PASS must be persisted to the relevant audit record/controller/status surfaces before it is reported as authoritative. Repository write mechanics are governed by `docs/stage16-29-github-write-policy.md` and must not change mathematical claims or audit semantics.

In addition, every `StageX-audit` must publish its final audit verdict directly on the audited pull request's main Conversation surface. The PR must visibly record at least the audit verdict, whether repair is required, `MERGE_ALLOWED`, advancement status / next checkpoint, and `NEXT_EXPECTED_COMMAND`. Submission-time PR text such as `AUDIT_REQUIRED=true`, `ADVANCE_ALLOWED=false`, or `MERGE_ALLOWED=false` describes the pre-audit state and must not be left as the only visible status after the audit has completed. A PR comment containing the authoritative post-audit state is sufficient; the original PR description need not be rewritten solely to replace historical submission-state fields.

```text
AUDIT_RESULT_MUST_BE_PUBLISHED_TO_PR_MAIN_CONVERSATION=true
AUDIT_PR_MINIMUM_FIELDS=AUDIT_VERDICT,REPAIR_REQUIRED,MERGE_ALLOWED,ADVANCE_STATUS,NEXT_EXPECTED_COMMAND
SUBMISSION_STATE_FIELDS_REMAIN_HISTORICAL=true
PR_DESCRIPTION_REWRITE_REQUIRED=false
```

StageX-70 follows `docs/stage16-29-stage70-policy.md`: synthesize aggressively from certified inputs, but stop before work requiring a substantially new theorem, large computation, literature program, or off-stage branch. The deep-exploration rule above applies before such a stop is accepted: the stage should first exhaust a reasonable bounded set of materially distinct repo-native attacks and sharpen any surviving external gate to research-request-ready form.

## Stage20 literature reuse rule

Stage20 may begin with more pre-filled material than earlier population stages because Euler cuboids have a large existing literature and strong prior repository results. Inherited constructions and estimates must still be adapted to the common cutoff and population contract; an infinite family is not automatically a matched asymptotic lower bound.

## Stage19 carry-over

Stage19 must preserve the distinction between the certified upper bound for the two-face + space-diagonal population, the independent Stage15 causal zero-density mechanism, and the still-open questions of a matching lower bound and true growth exponent. No later stage may silently treat the half-power upper exponent as a known asymptotic law.

## Endpoint remains deferred

The perfect-cuboid population — three integral face diagonals plus an integral space diagonal — remains outside the Stage16-29 numbering. Stage29 synthesizes the population map and identifies the residual obstruction; it does not assume existence or nonexistence of the endpoint.

## Migration rule

The legacy full-roadmap label `Stage16-28` is obsolete for current operational scope and is replaced by `Stage16-29`. Historical stage/checkpoint identifiers that contain `28` for genuine provenance are not renamed merely because the roadmap range expanded.
