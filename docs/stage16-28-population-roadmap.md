# Stage16-28 Population / Condition-Interaction Roadmap

Status: **future roadmap after Stage15 closure**.

This roadmap does not reopen Stage15-6 and does not assign a stage number to the
perfect-cuboid endpoint.  Its purpose is to understand, one condition at a time,
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
```

Numerical evidence and asymptotic theorems must remain explicitly separated.

## Deferred endpoint

The population with **three integer face diagonals plus an integer space diagonal**
is the perfect-cuboid endpoint.  It is intentionally **not assigned a Stage16-28
number here**.  The project should first complete enough of the population and
interaction map to know what the final condition is actually doing before opening
that endpoint as a dedicated stage.
