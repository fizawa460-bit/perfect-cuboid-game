# Stage24-50 discovery ledger

CHECKPOINT=50
ROLE=LOWER_BOUND_AND_CONSTRUCTION_DISCOVERY
SEARCH_STATUS=BREAKTHROUGH_SUBMITTED_FOR_FRESH_AUDIT

## Required policy gates

- fresh Stage19 lower surgeon first: PASS
- explicit unbounded-family search: PASS
- positive-power lower-bound search: PASS, none proved
- Stage18 explicit-family space-lift test: PASS
- new candidate generation: 4 candidates recorded
- finite examples alone forbidden: PASS, theorem does not rely on finite growth
- old dead branch revalidation if negative: NOT_TRIGGERED because a positive breakthrough was found

## Candidate matrix

| ID | Candidate | Result | Promotion |
|---|---|---|---|
| F50-S1 | mixed-parity `p^4+q^4=17Z^2` lift of Stage15-2 | positive-rank genus-one quartic; physical cone infinite; triple sublocus genus 5 finite | THEOREM |
| F50-S2 | general `k`: `p^4+q^4=(k^4+1)Z^2` | systematic quartic class; `k=2` closed by S1 | RESEARCH RESERVE |
| F50-S3 | fixed squarefree-core `A=kP^2,B=kQ^2` slices | target-compatible but moving genus-one/Pell obstruction remains | OPEN |
| F50-S4 | common-leg divisor pair plus space norm | no independent family; successful slice subsumed by S1 | SUBSUMED |

## Breakthrough chain

1. Stage15-2 formula:
   `e=4pq`, `x=4p^2-q^2`, `y=4q^2-p^2`.
2. Remove only its old odd/odd specialization.
3. Integral space is exactly `p^4+q^4=17Z^2`, `D=17Z`.
4. The quartic `17z^2=t^4+1` is genus one and maps to `E: Y^2=X^3-1156X`.
5. `(t,z)=(2,1)` maps to `P=(-16,120)`.
6. Good-reduction exact checks: `#E(F31)=32`, `#E(F41)=52`, `ord(P mod31)=16`; hence `P` is non-torsion.
7. Therefore the quartic has positive Mordell-Weil rank and infinitely many rational points.
8. The exact physical point `(p,q,Z)=(38,43,569)` lies inside `1<q/p<(1+sqrt(2))/2`.
9. Non-torsion real elliptic rotation supplies infinitely many rational points in that open physical cone.
10. Opposite parity and coprimality give primitive integer boxes with two guaranteed face squares and integral space diagonal.
11. The third-face-square fiber product has genus five, hence finitely many rational points by Faltings.
12. Removing those finitely many leaves infinitely many primitive canonical exactly-two Stage19 boxes.
13. Standard elliptic height and equidistribution sharpen this to `N2(B)>>sqrt(log B)`.

## Exact regression witnesses

Primary physical-cone witness:

```text
(p,q,Z)=(38,43,569)
(a,b,c,D)=(3927,5952,6536,9673)
face diagonals through c = 7625, 8840
third face square = false
primitive = true
```

Independent mixed-parity witness:

```text
(p,q,Z)=(859,1186,385241)
raw (x,y,e,D)=(1544928,4888503,4075096,6549097)
canonical edges=(1544928,4075096,4888503)
third face square = false
primitive = true
```

These witnesses are regression anchors only. They do not prove infinitude.

## Supersession audit

Stage19 checkpoint50 historically recorded:

```text
UNBOUNDEDNESS_PROVED=false
INFINITE_PRIMITIVE_CONSTRUCTION_CERTIFIED=false
POSITIVE_POWER_LOWER_BOUND=false
```

The first two are now contradicted by a later Stage24 theorem candidate, while the third remains true. No historical frozen file is rewritten before fresh audit. After PASS, Stage24 must backflow a supersession note so consumers do not keep treating the old negative ledger as current.

Stage23-60 R60-01 said the Stage15 explicit family was dead by mod16. The new result does not invalidate its literal odd/odd calculation. It narrows the correct scope:

```text
R60_01_ODD_ODD_DEATH=STILL_VALID
R60_01_BROADER_FORMULA_DEATH=SUPERSEDED
REVIVED_VARIANT=MIXED_PARITY_C17
```

## Quantitative boundary

The proved candidate lower is logarithmic:

\[
N_2(B)\gg(\log B)^{1/2}.
\]

It proves unboundedness but no positive polynomial exponent. The upper remains

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore neither the true exponent nor half-power intrinsic status is identified.

## Numerical reuse

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,24-14num-r201,24-14num-r202
NUM_POPULATION_MATCH=EXACT
NUM_EVIDENCE_LEVEL=EXACT_FINITE_ORACLE_PLUS_NEW_THEOREM_CONSTRUCTION
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_CONSTRUCTION_REGRESSION_ONLY
```

## Exit

```text
DISCOVERY_CHECKPOINT=50
BREAKTHROUGH_FOUND=true
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
NEW_LOWER_BOUND=N2(B)>>sqrt(log B)
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=50
MERGE_ALLOWED=false
```
