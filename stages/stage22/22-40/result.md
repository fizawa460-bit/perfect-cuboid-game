# Stage22-40 — sharp upper-bound ledger and mechanism boundary

EVIDENCE_LEVEL=PROVED
CHECKPOINT=40
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Sharp transition upper bound

Checkpoint30 proved, for the matched primitive canonical exactly-one-face and exactly-two-face strata under the common physical cutoff `R<=B`,

\[
\frac{M_2(B)}{M_1(B)}
\sim
\frac{4\pi^2 C_{M_2}}{3}\frac{(\log B)^4}{B},
\qquad C_{M_2}>0.
\]

Therefore the strongest certified upper bound at the present interface is

\[
\boxed{\frac{M_2(B)}{M_1(B)}\ll \frac{(\log B)^4}{B}}.
\]

It is order-sharp: the positive leading asymptotic constant from checkpoint30 supplies a matching lower bound of the same scale. Hence no bound of strictly smaller polynomial order, or of the form `o((log B)^4/B)`, can hold for these matched populations.

Equivalently,

\[
\boxed{M_2(B)\ll B(\log B)^5}
\]

against

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

Finite checkpoint20 data are not used in this deduction.

## 2. Proven exponent ledger

The audited source and target laws are

\[
M_1(B)\sim C_1 B^2\log B,
\qquad C_1=\frac{3}{4\pi^2},
\]

\[
M_2(B)\sim C_2 B(\log B)^5,
\qquad C_2=C_{M_2}>0.
\]

Thus the ratio ledger is exactly

```text
SOURCE_POLYNOMIAL_POWER=2
TARGET_POLYNOMIAL_POWER=1
NET_POLYNOMIAL_RATIO_POWER=-1
SOURCE_LOG_POWER=1
TARGET_LOG_POWER=5
NET_LOG_RATIO_POWER=4
SHARP_RATIO_SCALE=(log B)^4/B
SHARPNESS_PROVED=true
```

The ratio is a comparison of disjoint adjacent strata. These entries do not define an objectwise survival probability.

## 3. Source-side mechanism already certified by Stage16

Stage16 proves the one-face architecture by writing the unique integral face as a scaled primitive Pythagorean triangle

\[
(kx_0,ky_0,kh)
\]

and leaving the complementary edge `z` free at polynomial order `B`.

The Pythagorean face-shape/scale count has order

\[
\sum_{k\le B}P(B/k)\asymp B\log B,
\]

where the logarithm comes from the harmonic scale sum `sum 1/k`. Multiplying by the free third-edge range gives

\[
(B\log B)\cdot B=B^2\log B.
\]

Therefore the source-side ledger is structurally understood:

```text
SOURCE_FACE_CONSTRAINT=ONE_PYTHAGOREAN_FACE
SOURCE_SCALE_LOG=HARMONIC_FACE_SCALE_SUM
SOURCE_COMPLEMENTARY_EDGE=FREE_AT_ORDER_B
SOURCE_TOTAL_SCALE=B^2 log B
```

## 4. Target-side mechanism already certified by Stage15 / Stage18

For the exactly-two stratum, the two successful Pythagorean faces share one unique edge. With shared edge `e` and remaining legs `x,y`, the target lies on

\[
u^2=e^2+x^2,\qquad v^2=e^2+y^2,
\]

with the third face required to be nonsquare.

Stage15 identifies the smooth split toric resolution

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad \rho(Y)=6,
\]

and proves that the physical height `R` is an anticanonical height. The audited toric count therefore gives

\[
M_2(B)\sim C_{M_2}B(\log B)^{\rho(Y)-1}
=C_{M_2}B(\log B)^5.
\]

The forbidden third-face-square cover is lower order, so it does not alter this leading scale.

Thus the target-side ledger is

```text
TARGET_STRUCTURE=COUPLED_SHARED_EDGE_DOUBLE_PYTHAGOREAN_SURFACE
TARGET_GEOMETRY=SMOOTH_SPLIT_TORIC_RESOLUTION
TARGET_PICARD_RANK=6
TARGET_LOG_POWER=RHO_MINUS_ONE=5
THIRD_FACE_SQUARE_SUBTRACTION=LOWER_ORDER
TARGET_TOTAL_SCALE=B(log B)^5
```

## 5. What pays for the Stage16 -> Stage18 change

At the level of proved counting architectures, moving from exactly one to exactly two integral faces replaces

```text
one Pythagorean face + an order-B free complementary edge
```

by

```text
a coupled pair of Pythagorean faces sharing one edge on the Stage15 toric surface.
```

The net theorem-level effect is

\[
B^2\log B
\longrightarrow
B(\log B)^5,
\]

so one polynomial power of `B` is lost while four logarithmic powers are gained.

The source logarithm is explicitly traced to the harmonic face-scale sum. The target logarithmic exponent five is explicitly traced, at the current theorem interface, to the anticanonical toric count with Picard rank six. Therefore the relative `(log B)^4` factor is rigorously the difference of these two audited logarithmic exponents.

This does **not** prove that the four extra logarithms are four independent local events, four valuation freedoms, or an Euler-product factor. No such finer factorization is currently certified.

## 6. Mechanism boundary

The sharp quantitative statement is closed at this checkpoint, but a finer arithmetic causal decomposition is not yet proved.

```text
SHARP_UPPER_SCALE=(log B)^4/B
SHARPNESS_PROVED=true
POLYNOMIAL_LEDGER=ONE_NET_POWER_OF_B_LOST
SOURCE_POLYNOMIAL_FEATURE=FREE_COMPLEMENTARY_EDGE_AT_ORDER_B
TARGET_STRUCTURAL_REPLACEMENT=SHARED_EDGE_DOUBLE_PYTHAGOREAN_TORIC_SURFACE
SOURCE_LOG_MECHANISM=HARMONIC_FACE_SCALE_SUM
TARGET_LOG_MECHANISM=ANTICANONICAL_TORIC_COUNT_WITH_RHO_6
RELATIVE_LOG_POWER=4
LOCAL_FACTOR_PRODUCT_FOR_LOG4_PROVED=false
SQUARECLASS_EXPLANATION_FOR_LOG4_PROVED=false
VALUATION_EXPLANATION_FOR_LOG4_PROVED=false
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
UNIQUE_FINE_CAUSAL_DECOMPOSITION_PROVED=false
```

Checkpoint50 should next record the matching lower-bound / construction ledger. Checkpoint60 remains the place to decide how far the source harmonic-scale mechanism and target shared-edge toric geometry can be assembled into a causal synthesis without double charging the already-proved exponent difference.

## 7. Exit

```text
UPSTREAM_PREMISE_CHECK=PASS
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
FALSE_SUBSET_INTERPRETATION_BLOCKED=true
FINITE_DATA_USED_AS_PROOF=false
DOUBLE_CHARGE_CHECK=PASS
NEW_ANALYTIC_INPUT=false
NEW_RESEARCH_JUSTIFIED=true
NEXT_CHECKPOINT=50
NEXT_EXPECTED_COMMAND=Stage22-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
