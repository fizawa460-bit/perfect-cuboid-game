# Stage22-10 — population contract for the Stage16 -> Stage18 second-face transition

EVIDENCE_LEVEL=PROVED
CHECKPOINT=10
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## Research object

Stage22 studies the transition

\[
\boxed{\text{Stage16 exactly-one face}\longrightarrow\text{Stage18 exactly-two faces}}
\]

under one common primitive/canonical geometric cutoff. Its question is incremental: how much does imposing a second integral face thin the one-face population, and what arithmetic interaction causes that change?

## Source population

Let
\[
\mathcal B_1(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly one integral face diagonal}\},
\]
where
\[
R=\sqrt{a^2+b^2+c^2},
\qquad M_1(B)=\#\mathcal B_1(B).
\]

The frozen Stage16 interface proves
\[
M_1(B)\asymp B^2\log B.
\]

For Stage22, the stronger literal E-1e interface already recovered and audited in Stage21 may also be reused when a leading transition constant is needed:
\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]
Stage22-10 does not yet use that stronger formula to claim a ratio theorem; it only records it as a preflight candidate for checkpoint30.

## Target population

Let
\[
\mathcal B_2(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly two integral face diagonals}\},
\]
with
\[
M_2(B)=\#\mathcal B_2(B).
\]

The frozen Stage18 interface proves
\[
\boxed{M_2(B)\sim C_{M_2}B(\log B)^5},\qquad C_{M_2}>0.
\]

No integral-space-diagonal condition is imposed in either source or target.

## Common contract

```text
SOURCE_STAGE=Stage16
TARGET_STAGE=Stage18
SOURCE_POPULATION=primitive canonical exactly-one-face cuboids
TARGET_POPULATION=primitive canonical exactly-two-face cuboids
CANONICAL_ORDER=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
CUTOFF=R=sqrt(a^2+b^2+c^2)<=B
SOURCE_MULTIPLICITY=one per physical canonical cuboid
TARGET_MULTIPLICITY=one per physical canonical cuboid
SPACE_DIAGONAL_REQUIRED=false
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

Unlike Stage21, Stage22 is not a literal subset-survival probability: `exactly one` and `exactly two` are disjoint masks. The roadmap's word "transition/thinning" therefore means a matched population-size comparison under the same universe/cutoff, not that each target object is selected from the source set by adding a predicate. The quantity
\[
M_2(B)/M_1(B)
\]
is a population-size ratio comparing adjacent face-integrality strata.

This distinction is load-bearing and prevents the false set inclusion `B2 subset B1`.

## Causal normal forms

A Stage16 object has one successful Pythagorean face and two failed faces. A Stage18 object has two successful Pythagorean faces sharing exactly one edge. After naming that shared edge `s` and the other two edges `x,y`, the Stage18 condition is equivalent to
\[
s^2+x^2=p^2,\qquad s^2+y^2=q^2,\qquad x^2+y^2\notin\square.
\]
Thus Stage22 asks how replacing the one-face architecture by a coupled shared-edge pair changes the population scale. The two Pythagorean equations are coupled through `s`; no independence factorization is assumed.

## Frozen upstream contracts

```text
UPSTREAM_STAGE=Stage16
UPSTREAM_THEOREM=M1(B) asymp B^2 log B for primitive canonical exactly-one-face cuboids under R<=B
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
ROLE=source population
```

```text
UPSTREAM_STAGE=Stage18
UPSTREAM_THEOREM=M2(B) ~ C_M2 B(log B)^5, C_M2>0, for primitive canonical exactly-two-face cuboids under R<=B
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
ROLE=target population
```

## Reuse / exploration preflight

Stage21 demonstrated that relying only on the obvious frozen interface can miss a stronger literal source theorem. Stage22 therefore adopts the strengthened search discipline from the outset:

```text
SEARCH_REQUIRED_BEFORE_NEW_THEOREM=true
SEARCH_SCOPE=ARSENAL+NUM_INDEX+STAGES+SUPPLEMENTS+ARCHIVE+PRS
SEARCH_MODES=direct terms;synonyms/notation;structural signatures;dependency neighbors
STRONGEST_KNOWN_CHECK_REQUIRED=true
KNOWN_STRONGER_SOURCE_CANDIDATE=E-1e PR #128 leading M1 asymptotic
TARGET_CONSTANT_SEARCH_REQUIRED=true
```

Checkpoint30 must not settle for a mere order comparison if a compatible leading constant for `M2` or a portable adapter is already present in the repository.

## Stage22 checkpoint plan

```text
20=finite matched baseline and enumerator consistency
30=population-size ratio / thinning law, strongest compatible form
40=upper-bound ledger and mechanism
50=lower-bound / construction ledger
60=causal decomposition and interaction analysis
70=bounded maximal synthesis, artifact decision, and actual arsenal promotion if required
```

Stage70 rule is explicit: if `ARSENAL_PROMOTION_REQUIRED=YES`, the portable arsenal artifact must be materialized before Stage22 may close; a YES classification alone is not completion.

```text
UPSTREAM_PREMISE_CHECK=PASS
FALSE_SUBSET_INTERPRETATION_BLOCKED=true
FINITE_DATA_USED_AS_PROOF=false
NEXT_CHECKPOINT=20
NEXT_EXPECTED_COMMAND=Stage22-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
