# Stage16-29 Population / Condition-Interaction Roadmap

Status: **canonical roadmap for Stage16-29**.

This document is the authoritative roadmap for the Stage16-29 population program. Stage27 is the repository-defined `Stage18 -> Stage19` strict reattack, Stage28 is the `Stage19 -> Stage20` bridge comparison, and Stage29 is the new-foundation screening / interaction synthesis / perfect-cuboid endpoint-routing stage.

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
| **Stage28** | **19 -> 20** | matched Stage19/Stage20 bridge comparison under common cutoff/canonicalization; closed/audited/merged |
| **Stage29** | **new-foundation screening + interaction synthesis** | search for materially new foundations, then route the best direct perfect-cuboid endpoint attack |

### Stage27 authority

`stages/stage27/27-controller.json` is authoritative for Stage27. Its frozen transition is:

```text
Stage18 -> Stage19
```

The Stage27 work tree may contain historically named `27-20-*` checkpoint or derived-route artifacts. Those names are provenance inside Stage27 and are not evidence that the stage-level population transition is `Stage19 -> Stage20`. Do not bulk-move or renumber those historical artifacts solely because later roadmap language changes.

### Stage28 closeout

Stage28 studied the relationship between the already established Stage19 and Stage20 populations under matched conventions:

```text
SOURCE_POPULATION = Stage19 population
TARGET_POPULATION = Stage20 population
COMPARISON         = Stage19 -> Stage20
```

Stage28 is now:

```text
STATUS=CLOSED_AUDITED_PASS_MERGED
FINAL_PR=1284
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
NEXT_STAGE=Stage29
```

Its final bridge-curvature interface, common-polarization K3 comparison, fixed-curve spectrum findings, residual moving-complement receiver, and closeout arsenal promotion are certified Stage29 inputs. Stage29 does not reopen Stage28 merely because its final asymptotic ordering remains unresolved.

### Stage29 contract

Stage29 is different from the earlier population stages. It does **not** use the inherited `10,20,...,70` checkpoint sequence. Its authoritative roadmap is:

```text
stages/stage29/roadmap.md
```

with ordinary incremental items `29-01, 29-02, 29-03, ...`.

Stage29 first performs broad **new-foundation screening** across Stage16-28, testing whether a materially different global model, joint cover, parametrization-coverage viewpoint, joint local invariant, or other coordinate system changes the endpoint receiver. It then synthesizes the existing condition interactions and compares direct perfect-cuboid endpoint routes.

The initial required lenses are:

1. global perfect-cuboid algebraic geometry;
2. joint space-completion × third-face-completion cover/fiber product;
3. parametrization coverage atlas;
4. joint local arithmetic / completion correlation.

A targeted return to an earlier stage is allowed only when this screening creates a genuinely new receiver, model, adapter, invariant, or theorem species. Stage29 does not rerun Stage16 through Stage28 sequentially and does not replay old frozen gates without new input.

```text
STAGE29_NUMBERING=INCREMENTAL_01_02_03
STAGE29_BROAD_SCREEN_FIRST=true
TARGETED_BACKFLOW_IF_NEW_FOUNDATION=true
SEQUENTIAL_STAGE16_TO_STAGE28_RERUN=false
OLD_FROZEN_GATE_REPLAY_WITHOUT_NEW_INPUT=false
ARSENAL_STRUCTURE_RADAR_PREFLIGHT_STANDING=true
```

Stage29 compares three endpoint descriptions:

```text
A = Stage19 + third face
B = Stage20 + space diagonal
C = direct global/joint endpoint model
```

The purpose is not to infer existence/nonexistence from rarity, but to identify the strongest exact model and the smallest residual theorem/construction/adapter receivers for a later direct perfect-cuboid attack stage.

## Completion / evidence rules

Stages16-28 retain their historical checkpoint contracts. Stage29 follows its own incremental roadmap.

Every research item must keep `PROVED`, `LITERATURE`, `COMPUTED`, and `HEURISTIC` evidence separate. An audited `OPEN_GATE` is legitimate when the missing input is precisely identified. Re-running the same route without a genuinely new theorem, dataset, reusable weapon, model, adapter, or literature input is not progress.

## Deep-exploration rule before OPEN_GATE / closeout

An unresolved item must not be converted immediately into `OPEN_GATE` or closeout merely because the first attempted route fails. Before declaring that genuinely new external input is required, the stage must perform a bounded but aggressive internal exploration of materially distinct routes reasonably available from the current repository state.

This exploration should include, when relevant:

- alternate exact identities, eliminations, factorizations, parameterizations, fibrations, covers, and height normalizations;
- arithmetic, geometric, analytic, sieve, incidence/determinant, correlation/moment, local-global, and construction viewpoints that are genuinely distinct rather than renamed copies of the same gate;
- repository-wide Arsenal / StructureRadar / prior-stage / supplement / archive rematches against the exact current receiver and physical measure;
- upper and lower routes separately, including attempts to change the obstruction rather than only sharpen the same estimate;
- bounded targeted computation when it can distinguish routes or expose a structural lead, without promoting finite evidence to an asymptotic theorem.

The AI/controller is expected to choose and pursue promising unexplored routes proactively. Operator intervention is not required merely to authorize another mathematically distinct internal attack. Blind repetition, cosmetic renaming, or repeatedly re-running a theorem gate with no new structural input remains forbidden.

A research lane may freeze only after the remaining obstruction has been narrowed enough that the missing input can be stated as a concrete theorem/construction/adapter receiver with explicit population, measure, quantifiers, parameter ranges, and required strength. For literature-dependent gates, the preferred stopping point is a research-request-ready specification; an unbounded new literature program is not required before closeout.

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

Every Stage16-29 research item must run the bounded repository-wide preflight defined in `docs/stage16-29-reuse-preflight.md` before opening new theorem, construction, computation, or literature work. Numerical work must also inspect `docs/stage14-num-reuse-index.md` when applicable.

Audit verdicts are durable repository state. A canonical audit PASS must be persisted to the relevant audit record/controller/status surfaces before it is reported as authoritative. Repository write mechanics are governed by `docs/stage16-29-github-write-policy.md` and must not change mathematical claims or audit semantics.

Every StageX-audit must update the audited pull request's main PR description/body so that the authoritative post-audit state is visible at the top-level PR surface.

```text
AUDIT_RESULT_MUST_BE_PUBLISHED_TO_PR_BODY=true
AUDIT_PR_MINIMUM_FIELDS=AUDIT_VERDICT,REPAIR_REQUIRED,MERGE_ALLOWED,ADVANCE_STATUS,NEXT_EXPECTED_COMMAND
POST_AUDIT_PR_BODY_IS_AUTHORITATIVE=true
PR_DESCRIPTION_REWRITE_REQUIRED=true
COMMENT_ONLY_AUDIT_STATUS_SUFFICIENT=false
```

### Stage16-28 Stage70 policy remains active

For Stage16-28, `StageX-70` continues to follow `docs/stage16-29-stage70-policy.md`: synthesize aggressively from certified inputs, but stop before work requiring a substantially new theorem, large computation, literature program, or off-stage branch. The deep-exploration rule applies before such a stop is accepted. Stage29 is the explicit exception because it uses its own incremental roadmap and has no inherited Stage29-70 checkpoint.

## Stage20 literature reuse rule

Stage20 may begin with more pre-filled material than earlier population stages because Euler cuboids have a large existing literature and strong prior repository results. Inherited constructions and estimates must still be adapted to the common cutoff and population contract; an infinite family is not automatically a matched asymptotic lower bound. This historical contract remains a downstream firewall when Stage29 reuses Stage20 material.

## Stage19 carry-over

Stage19 must preserve the distinction between the certified upper bound for the two-face + space-diagonal population, the independent Stage15 causal zero-density mechanism, and the still-open questions of a matching lower bound and true growth exponent. No later stage may silently treat the half-power upper exponent as a known asymptotic law. Stage29 inherits this firewall unchanged.

## Endpoint remains deferred

The perfect-cuboid population — three integral face diagonals plus an integral space diagonal — remains outside the Stage16-29 population numbering. Stage29 may develop the direct global/joint endpoint geometry and exact endpoint receivers, but it does not assume existence or nonexistence and does not promote rarity heuristics or bounded finite zero counts into an endpoint theorem.

## Migration / provenance rule

The legacy full-roadmap label `Stage16-28` is obsolete for current operational scope and is replaced by `Stage16-29`. Historical stage/checkpoint identifiers remain provenance and are not renamed merely because the roadmap range or Stage29 operating model changed.
