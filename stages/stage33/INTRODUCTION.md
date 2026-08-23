# Stage33 — BRAUER-PROSPECT-SCAN introduction

```text
STAGE33_STATUS=FUTURE_RESERVED_NOT_STARTED
STAGE33_START_AUTHORIZED=false
SOURCE_STAGE29_CLOSED=true
PERFECT_CUBOID_PROBLEM_STATUS=OPEN
PRIMARY_FROZEN_KERNEL=K16-C2-BRAUER-EXPLICIT-CHAIN
AUDITED_INTERNAL_SHAPE=DEPENDENCY_DAG
```

## Purpose

This file is a **future-stage restart note**, not a declaration that Stage33 has started.

If Stage33 is eventually assigned to the Stage29 Brauer frontier, the first task should **not** be to launch the full `BRAUER-EXPLICIT-DAG` immediately.  Stage29 already established that the DAG is decision-capable only if its completed arithmetic produces an actual obstruction, such as an empty physical-open Brauer--Manin set.

The first Stage33 question should instead be:

> Before investing in the full explicit Brauer DAG, can we cheaply determine whether the surviving physical-open / two-primary Brauer machinery has a realistic chance of producing a nontrivial local-evaluation and reciprocity obstruction?

Working name:

```text
BRAUER-PROSPECT-SCAN
```

## Frozen starting point from Stage29

The active kernel is

```text
K16-C2-BRAUER-EXPLICIT-CHAIN
```

The compatibility name says `CHAIN`, but the audited internal structure is a dependency **DAG**:

```text
BR0A -> BR0B
BR0A + boundary incidence -> BR0G
K3-RULED2 + BR0G/physical-boundary data -> BR2A
BR2A + explicit representatives -> BR2B
BR0G/BR2A -> NF-PHYS2 when invoked
BR2A/BR2B -> CAMP4 when invoked
```

Already audited inputs include:

```text
- physical boundary has 72 components;
- Div_D -> Pic extraction preflight exists;
- seven-line base-complement geometric Br[2] precursor has F2-dimension 9;
- K_c has an explicit ruled (4,4) double-cover model over P1 x P1;
- the branch hypotheses needed for the ruled-double-cover calculation were discharged;
- dim_F2 Br(K_c_Qbar)[2] = 2.
```

The full DAG wall remains explicit integral Picard/saturation work, absolute-Galois `UPic/Gersten`, Creutz--Viray relation/symbol matrices, `Q(i)/Q` action/descent, explicit two-primary representatives and local evaluation.

## What Stage29 did and did not prove

Stage29 classified this kernel as **Class 2 / current-tool-limit executed**: no new theorem is known to be logically required at the first wall.

Stage29 did **not** prove that completing the DAG will solve the perfect-cuboid problem.

The exact decision condition is one-way:

```text
if the completed physical-open Brauer--Manin computation certifies an empty
physical adelic Brauer--Manin set (or an exactly equivalent endpoint-lift obstruction),
then there is no physical endpoint Q-point,
therefore there is no perfect cuboid.
```

But:

```text
DAG_COMPLETED does not imply BM_SET_EMPTY.
```

A completed computation may instead show:

```text
- no nonconstant Q-defined class survives;
- surviving classes have constant local evaluation;
- evaluations are nonconstant but the Brauer--Manin set remains nonempty.
```

Any of those outcomes would mean the Brauer route alone does not settle nonexistence.

## External adversarial review checkpoint

A standalone external review was requested under the explicit assumption that the DAG had already been completed correctly.  The reviewer was asked only whether the resulting Brauer obstruction looked likely to **bite**.

This external review is **UNVERIFIED OPINION, not theorem evidence and not repository audit credit**.

Its qualitative verdict was:

```text
SURVIVING_Q_BRAUER_CLASSES_EXPECTATION = LOW_TO_MEDIUM
NONCONSTANT_LOCAL_EVALUATION_EXPECTATION = MEDIUM_IF_CLASSES_SURVIVE
EMPTY_BRAUER_MANIN_SET_PLAUSIBILITY = POSSIBLE_BUT_NOT_FAVORED
MOST_LIKELY_POST_DAG_OUTCOME = BM_SET_NONEMPTY_BUT_RESTRICTED
                                OR BRAUER_EVALUATIONS_MOSTLY_TRIVIAL
CONFIDENCE = LOW
```

The main reason for low confidence was not a negative theorem.  It was lack of information at the precise arithmetic layers that matter most:

```text
Qbar geometric classes
  -> Q-defined surviving classes
  -> nonconstant local evaluation
  -> global reciprocity incompatibility
  -> empty physical Brauer--Manin set.
```

The external reviewer emphasized that the currently known geometric dimensions `9` and `2` do not by themselves predict the last three arrows.

## Important interpretation of the two geometric inputs

### Seven-line `(Z/2)^9`

This is a geometric result for the **base arrangement complement**.  It must not be read as nine endpoint Brauer obstructions.

Before it supports optimism, Stage33 would need to know how much survives the exact endpoint pullback/residue/Galois adapters.

### `dim_F2 Br(K_c_Qbar)[2]=2`

This is a geometric two-primary dimension over `Qbar`.  It does **not** imply two nonconstant `Q`-defined physical Brauer classes.

Before it supports optimism, Stage33 would need the actual `Q(i)/Q` Galois action and the surviving arithmetic representatives.

## Recommended Stage33 opening: prospect scan before full DAG

If Stage33 is activated for this route, begin with a bounded reconnaissance program.

### Probe P1 — arithmetic survival of the K3 two-primary classes

Question:

```text
Of the geometric dim_F2 Br(K_c_Qbar)[2]=2,
how much survives as relevant Q-defined arithmetic Brauer data after Q(i)/Q action/descent?
```

Desired output:

```text
K3_GEOMETRIC_BR2_DIM=2
K3_Q_RELEVANT_SURVIVING_DIM=<0|1|2|not-yet-certified>
GALOIS_ACTION_MATRIX=<explicit/certified>
SURVIVING_SYMBOL_REPRESENTATIVES=<list or NONE>
```

Interpretation:

```text
0 surviving relevant classes -> strong early negative signal for this branch.
1 or 2 surviving classes      -> continue to local-evaluation reconnaissance.
```

Do not infer endpoint obstruction merely from survival.

### Probe P2 — endpoint survival of the seven-line symbol space

Question:

```text
How much of the geometric nine-dimensional base-complement symbol/residue space
actually survives the exact endpoint multiquadratic pullback, physical boundary,
and Q-Galois constraints?
```

Desired output:

```text
BASE_LINE_BR2_DIM=9
ENDPOINT_PULLBACK_NONTRIVIAL_DIM=<certified value or bounded subspace>
PHYSICAL_BOUNDARY_SURVIVING_DIM=<certified value or bounded subspace>
Q_DEFINED_SURVIVING_DIM=<certified value or bounded subspace>
```

Interpretation:

```text
9 -> 0/very small with trivial representatives = pessimistic signal.
several explicit Q-defined nontrivial classes     = meaningful positive signal.
```

Do not confuse a large source space with a large endpoint obstruction space.

### Probe P3 — cheap local-evaluation test on surviving classes

Only after at least one explicit relevant class survives P1 or P2, test a small set of high-information places first.

Candidate first places should be selected from the actual class denominators, bad reduction, boundary/residue support and physical local geometry; do not hard-code a universal list without this check.  `Q_2` and the real place are natural candidates only when the explicit class makes them relevant.

Question:

```text
Does any surviving class have demonstrably nonconstant evaluation
on the physical local-point locus at a relevant place?
```

Desired output per class/place:

```text
CLASS_ID=
PLACE=
PHYSICAL_LOCAL_LOCUS_CERTIFIED=true|false
EVALUATION_IMAGE=<constant 0 | constant 1/2 | {0,1/2} | other exact image>
WITNESS_POINTS_OR_COMPONENTS=
SOURCE_LOCK=
```

Interpretation:

```text
all sampled decisive places constant -> downgrade full-DAG priority;
certified nonconstant evaluation       -> materially stronger reason to continue.
```

A nonconstant evaluation is still not a global Brauer--Manin obstruction.

## Go / stop decision after prospect scan

The prospect scan is not allowed to claim a probability of perfect-cuboid nonexistence.  It is only a route-priority screen.

Suggested routing rule:

```text
GO_FULL_BRAUER_DAG if:
  at least one relevant Q-defined class survives,
  and at least one meaningful local evaluation is certified nonconstant,
  and no immediate reciprocity/symmetry argument makes the obstruction vacuous.

DEPRIORITIZE_OR_FREEZE if:
  no relevant Q-defined class survives,
  or all surviving classes are provably constant on the physical local loci,
  or the completed early arithmetic proves the BM condition is automatically satisfied.

INCONCLUSIVE if:
  the prospect scan itself reaches an unexecuted exact algebra/CAS wall.
```

`INCONCLUSIVE` must not be recorded as negative evidence.

## If the scan is positive

Then Stage33 may promote the full execution program:

```text
BRAUER-PROSPECT-SCAN
  -> BRAUER-EXPLICIT-DAG
  -> explicit local evaluations at all required places
  -> exact physical adelic compatibility test
```

Only the final exact result may decide among:

```text
A. physical BM set empty
   -> perfect-cuboid nonexistence.

B. physical BM set nonempty but restricted
   -> Brauer route does not settle endpoint; record exact restriction and hand off.

C. relevant evaluations trivial / classes vanish
   -> close this Brauer mechanism negatively and return to the Stage29 frontier.
```

## If the scan is negative

Do not continue the huge DAG merely because it is Class 2.

Record the exact negative certificate and return to the frozen Stage29 frontier, where the other decision-capable kernels include:

```text
K16-C3-ENDPOINT-EFFECTIVE-RATIONAL-POINT
K16-C3-CAMPEDELLI-UNIFORM-TORSOR
K16-C3-BEAUVILLE-ONE-STEP-DESCENT
K16-C3-QWEB-CLIFFORD-OBSTRUCTION
K16-C3-PESCH-EXPONENT-ONE
K16-C3-MOVING-FIBER-ARITHMETIC
```

The narrowest currently named theorem target with an audited direct nonexistence implication remains `K16-C3-PESCH-EXPONENT-ONE`; that statement is conjectural and receives no theorem credit from this note.

## Anti-overclaim firewalls

```text
GEOMETRIC_BR2_NONZERO_IMPLIES_Q_BRAUER_NONZERO=false
Q_BRAUER_NONZERO_IMPLIES_NONCONSTANT_EVALUATION=false
NONCONSTANT_EVALUATION_IMPLIES_BM_EMPTY=false
BASE_COMPLEMENT_BR2_DIM9_IMPLIES_ENDPOINT_BR2_DIM9=false
K3_QBAR_BR2_DIM2_IMPLIES_TWO_Q_OBSTRUCTIONS=false
DAG_COMPLETION_IMPLIES_PERFECT_CUBOID_NONEXISTENCE=false
FINITE_NUMERICAL_ZERO_IMPLIES_NONEXISTENCE=false
EXTERNAL_AI_REVIEW_COUNTS_AS_THEOREM_EVIDENCE=false
```

## Restart reading order

When Stage33 is actually started, read in this order before doing new work:

1. `docs/frontier/13-active-kernels.md`
2. `stages/stage29/29-16/audit.md`
3. `stages/stage29/29-16/decision-frontier.md`
4. `stages/stage29/29-15/brauer-line9-execution.md`
5. `stages/stage29/29-15/k3-ruled2-audit-execution.md`
6. `docs/frontier/brauer-explicit-dag-claude-review.html` as review context only, never as authority
7. this file

Then reconstruct the current source state.  Do not assume these frozen observations remain the strongest available inputs if new literature or later stages have appeared.

## Stage33 activation contract

Until explicitly activated:

```text
STAGE33_STARTED=false
STAGE33_RESULT_CLAIM=NONE
BRAUER_PROSPECT_SCAN_EXECUTED=false
BRAUER_DAG_EXECUTION_STARTED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If activated for Brauer work, the preferred first item is:

```text
Stage33-01 = BRAUER-PROSPECT-SCAN
PRIMARY_OBJECTIVE = measure arithmetic survival and local-evaluation nontriviality before committing to the full Brauer DAG
```
