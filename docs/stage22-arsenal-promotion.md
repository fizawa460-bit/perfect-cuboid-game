# Stage22 arsenal promotion — one-face to two-face transition law

PROMOTION_ID=AR-STAGE22-TRANSITION-M1-M2
STATUS=CANDIDATE_PENDING_FRESH_AUDIT
SOURCE_STAGE=Stage22
SOURCE_CHECKPOINT=70

## Purpose

Reusable transition interface comparing primitive canonical exactly-one-face and exactly-two-face cuboid populations under the same physical cutoff `R<=B`.

## Input contract

```text
POPULATION_SOURCE=primitive canonical exactly-one integral face diagonal
POPULATION_TARGET=primitive canonical exactly-two integral face diagonals
CANONICAL=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
CUTOFF=R=sqrt(a^2+b^2+c^2)<=B
SPACE_DIAGONAL_REQUIRED=false
RATIO_SEMANTICS=matched adjacent-stratum population-size ratio
LITERAL_SUBSET_TRANSITION=false
```

## Output theorem

With

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B
\]

and

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

one has

\[
\boxed{\frac{M_2(B)}{M_1(B)}\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}}.
\]

Consequently

\[
M_2(B)=o(M_1(B)),
\qquad
\frac{M_2(B)}{M_1(B)}\asymp\frac{(\log B)^4}{B}.
\]

## Causal reuse note

At the theorem interface, the source is one scaled primitive Pythagorean face plus a complementary edge free at order `B`, while the target is the shared-edge double-Pythagorean rank-6 anticanonical toric bulk. The transition therefore loses one polynomial power and gains four logarithmic powers.

The third-face nonsquare exclusion is lower order because the three-face locus is `o(B(log B)^5)` and is not a leading cause.

## Reuse conditions

Use directly only when all of the following match:

- primitive physical objects, not raw parametrization records;
- strict canonicalization `0<a<b<c`;
- exactly-one source and exactly-two target masks;
- identical `R<=B` cutoff;
- ratio interpreted as adjacent-stratum population comparison, not conditional probability of an objectwise map.

Do not reuse the leading constant if the target height, mask, multiplicity, or canonical chamber is altered without a proved adapter.

## Nonclaims

No decomposition of `(log B)^4` into four independent local factors is proved. No statement about an integral space diagonal or perfect-cuboid existence/nonexistence is included.

```text
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_MATERIALIZED=true
REUSE_CLASS=DIRECT_REUSE_ON_EXACT_STAGE22_CONTRACT
FINE_MECHANISM_OPEN=true
PERFECT_CUBOID_CONCLUSION=NONE
```
