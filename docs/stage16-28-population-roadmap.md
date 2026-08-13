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
| **Stage17** | one integer face diagonal + integer space diagonal | What does the space-diagonal condition remove from the Stage16 population? |
| **Stage18** | exactly two integer face diagonals | Why does adding the second integer face diagonal thin the Stage16 population so strongly? |
| **Stage19** | exactly two integer face diagonals + integer space diagonal | Re-express the Stage14/15 population with matched upper/lower/causal questions; in particular test whether the current half-power upper exponent is intrinsic. |
| **Stage20** | three integer face diagonals (Euler cuboids) | Establish the Euler-cuboid population baseline, using the large existing literature as an input rather than rediscovering it. |

These are population states, not a claim that the project must traverse them in a
single linear chain.

## Transition / thinning stages

After the five populations are frozen under compatible conventions, study the
meaningful arrows between them as separate research objects.

| Stage | Transition | Main question |
|---|---|---|
| **Stage21** | **16 -> 17** | How much does the space-diagonal condition thin the one-face population, and why? |
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

## Common stage completion gates

Every Stage16-28 stage should use the same numbered checkpoints. Existing
literature may pre-fill a checkpoint, but it must still be translated into the
project's common population/cutoff conventions before being marked complete.

| Checkpoint | Required output | Closure question |
|---|---|---|
| **StageX-10** | population contract | What exactly is being counted? Fix primitive/canonical conventions, symmetry removal, cutoff, and source/target definitions. |
| **StageX-20** | finite-data baseline | How many objects are observed as the cutoff grows, and are the enumerators/replay checks trustworthy? |
| **StageX-30** | ratio / thinning law | What fraction survives the added condition, and does that ratio appear constant, logarithmically small, polynomially small, or zero-density? |
| **StageX-40** | upper-bound ledger | What is the strongest certified upper bound, and which mechanism pays for it? |
| **StageX-50** | lower-bound / construction ledger | How large a family can definitely be constructed, and what lower bound does it imply under the common cutoff? |
| **StageX-60** | causal decomposition | Why does the population decrease? Identify the actual arithmetic restrictions and distinguish new constraints from reformulations of earlier ones. |
| **StageX-70** | intrinsic-status / audit verdict | Do upper and lower bounds meet? Is the exponent intrinsic? Are the mechanisms independent, correlated, or double-counted? Record what is still genuinely unknown. |

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
