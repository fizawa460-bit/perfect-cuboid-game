# Stage23-10 — population contract for Stage17 -> Stage19

EVIDENCE_LEVEL=PROVED
CHECKPOINT=10
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Transition

Stage23 studies the roadmap transition

```text
Stage17 -> Stage19
```

under the condition that the space diagonal is already integral on both source and target populations.

Let

\[
N_1(B)=\#\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B,\ R\in\mathbb Z,\ \text{exactly one integral face diagonal}\},
\]

and

\[
N_2(B)=\#\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B,\ R\in\mathbb Z,\ \text{exactly two integral face diagonals}\}.
\]

Here

\[
R=\sqrt{a^2+b^2+c^2}.
\]

On both populations the integral space diagonal is exactly `d=R`, so `R<=B` and `d<=B` are identical cutoffs.

## 2. Common contract

The source and target share:

```text
CANONICAL_ORDER=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
COMMON_CUTOFF=R<=B
SPACE_DIAGONAL_REQUIRED=true
PHYSICAL_MULTIPLICITY=one canonical primitive cuboid per object
```

The only face-mask change is

```text
SOURCE_MASK=exactly one integral face diagonal
TARGET_MASK=exactly two integral face diagonals
```

Therefore no cutoff, symmetry, primitive, or multiplicity adapter is required.

```text
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
COMPARISON_ADAPTER_REQUIRED=false
```

## 3. Ratio semantics

The exactly-one and exactly-two strata are disjoint. Stage23 therefore does not define an objectwise subset-survival probability. Its canonical quantitative comparison is the matched adjacent-stratum population-size ratio

\[
\boxed{N_2(B)/N_1(B)}.
\]

This ratio answers: among the common geometric scale and integral-space-diagonal environment, how much smaller is the exactly-two-face stratum than the exactly-one-face stratum?

```text
LITERAL_SUBSET_TRANSITION=false
RATIO_SEMANTICS=matched adjacent-stratum population-size ratio N2/N1
```

## 4. Upstream theorem interfaces frozen for later checkpoints

Stage17 supplies

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3.
\]

Stage19 supplies the certified upper bound

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

but does not prove a matching lower bound, unboundedness, or a true half-power asymptotic. Therefore Stage23 must not silently turn the Stage19 upper exponent into an intrinsic thinning law.

The Stage19 causal result identifies a paired Gaussian-norm squareclass coincidence and split-prime valuation-parity sieve as a zero-density mechanism, while explicitly leaving the independence comparison against prior conditions unresolved for Stage23/24.

These interfaces are inputs for checkpoints30-60, not conclusions of checkpoint10.

## 5. Reuse / strongest-known preflight

Before any new theorem or computation, Stage23 must search and compare at least:

- Stage17 final theorem / census;
- Stage19 upper, lower-open-gate, and causal ledgers;
- Stage14 arsenal and NUM reuse index;
- Stage21 and Stage22 transition syntheses for interaction comparisons;
- relevant archive / PR material for stronger `N2` lower bounds or sharper matched laws.

In particular, a finite lower floor for `N2` must never be promoted to an asymptotic lower bound, and the current half-power upper exponent must remain `UPPER_BOUND_ONLY` unless a later checkpoint proves otherwise.

## 6. Exit

```text
UPSTREAM_PREMISE_CHECK=PASS
SOURCE_STAGE=Stage17
TARGET_STAGE=Stage19
SOURCE_COUNT=N1(B)
TARGET_COUNT=N2(B)
COMMON_CUTOFF=R<=B=d<=B_on_both_populations
SPACE_DIAGONAL_REQUIRED=true
FALSE_SUBSET_INTERPRETATION_BLOCKED=true
COMPARISON_ADAPTER_REQUIRED=false
FINITE_DATA_USED_AS_PROOF=false
TRUE_EXPONENT_IDENTIFIED=false_for_Stage19_target
NEXT_CHECKPOINT=20
NEXT_EXPECTED_COMMAND=Stage23-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
