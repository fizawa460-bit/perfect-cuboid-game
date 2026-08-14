# Stage22 self-contained closeout bundle

BUNDLE_ID=STAGE22-SELF-CONTAINED-CLOSEOUT-20260814
STATUS=CANDIDATE_PENDING_FRESH_AUDIT
STAGE=Stage22
TRANSITION=Stage16 -> Stage18

## Population contract

Let `M1(B)` count primitive canonical cuboids `0<a<b<c`, `gcd(a,b,c)=1`, under the physical cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B,
\]

with exactly one integral face diagonal. Let `M2(B)` count the same primitive/canonical/cutoff population with exactly two integral face diagonals. No integral space diagonal is required. The two strata are disjoint, so `M2/M1` is a matched adjacent-stratum population-size ratio rather than a literal subset-survival probability.

## Frozen source and target laws

The strongest audited source interface is

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

The audited target interface is

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0.
\]

Therefore

\[
\boxed{\frac{M_2(B)}{M_1(B)}\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}\to0}.
\]

Hence

\[
\boxed{\frac{M_2(B)}{M_1(B)}\asymp \frac{(\log B)^4}{B}}.
\]

## Causal ledger

For the exactly-one source, the unique integral face is a scaled primitive Pythagorean triangle. Its shape/scale count is of order `B log B`, with the logarithm arising from the harmonic scale sum, while the complementary edge remains free at polynomial order `B`. This gives `B^2 log B`.

For the exactly-two target, the two successful faces share one edge. Writing the shared edge as `e` and the other two edges as `x,y`, the positive structure is

\[
u^2=e^2+x^2,\qquad v^2=e^2+y^2.
\]

The target bulk lies on the smooth split toric resolution

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),\qquad \rho(Y)=6,
\]

with the physical height `R` anticanonical. The target therefore has order `B(log B)^5`.

Thus the certified main-order transition is

```text
one Pythagorean face + free complementary edge
  B^2 log B
    ->
shared-edge double-Pythagorean rank-6 toric bulk
  B(log B)^5
```

so

```text
POLYNOMIAL_LOSS=B^-1
LOG_COMPENSATION=(log B)^4
```

The polynomial loss is localized to replacing the free complementary-edge degree of freedom by the coupled second Pythagorean condition. The logarithmic compensation is localized, at the audited theorem interface, to the source harmonic scale architecture versus the target rank-6 anticanonical toric bulk.

## Leading-order exclusions

Canonicalization, primitivity, the common cutoff, and physical-object multiplicity are shared interface conditions and are not newly charged causes.

The exactly-two target excludes the third square face. However the three-face locus is

\[
M_3(B)=o(B(\log B)^5),
\]

so this exclusion changes only lower-order terms and does not generate the leading `B^{-1}(log B)^4` transition.

Finite checkpoint20 ratios are diagnostic only and are not used as proof.

## Fine-mechanism boundary

The repository does not prove a canonical decomposition of the relative `(log B)^4` into four independent arithmetic factors, local probabilities, valuation channels, squareclass channels, or four named toric divisors. The exact transition theorem and bulk architectural localization are nevertheless proved at the stated interface.

```text
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
LOCAL_PROBABILITY_PRODUCT_PROVED=false
VALUATION_FACTORIZATION_PROVED=false
SQUARECLASS_FACTORIZATION_PROVED=false
UNIQUE_FINE_CAUSAL_DECOMPOSITION_PROVED=false
FINE_MECHANISM_OPEN=true
```

## Scope

This bundle makes no claim about an integral space diagonal and no claim about existence or nonexistence of a perfect cuboid.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
ARSENAL_PROMOTION_REQUIRED=true
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
```
