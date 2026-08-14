# Stage22-50 — sharp lower-bound / construction ledger

EVIDENCE_LEVEL=PROVED
CHECKPOINT=50
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Sharp lower side of the transition

Checkpoint30 proved, under the exact common primitive/canonical `R<=B` contract,

\[
\frac{M_2(B)}{M_1(B)}
\sim
\frac{4\pi^2C_{M_2}}{3}\frac{(\log B)^4}{B},
\qquad C_{M_2}>0.
\]

Therefore

\[
\boxed{\frac{M_2(B)}{M_1(B)}\gg \frac{(\log B)^4}{B}}.
\]

Together with checkpoint40,

\[
\boxed{\frac{M_2(B)}{M_1(B)}\asymp \frac{(\log B)^4}{B}},
\]

and in fact checkpoint30 supplies the positive leading constant. Thus the lower side is order-sharp and no separate finite-data extrapolation is needed.

Equivalently, the target population satisfies

\[
\boxed{M_2(B)\gg B(\log B)^5},
\]

while the source satisfies

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

## 2. Where the target lower bound comes from

Stage15-2b proves

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

on the exact Stage18 / Stage22 target population. The positivity is not an empirical observation. It comes from the positive-volume physical real chamber in the smooth split toric model

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad \rho(Y)=6,
\]

with `R` as the exact anticanonical height. Stage15 also exhibits concrete nonsquare-third-face points in each shared-edge ordering chamber, establishing that these chambers are nonempty; toric equidistribution then gives positive chamber constants. The third-face-square locus is lower order, so removing it does not destroy the main term.

Thus the certified lower-bound mechanism is bulk geometric/arithmetic counting on the full toric target, not a thin hand-picked parametric family.

```text
TARGET_LOWER_BOUND=M2(B) >> B(log B)^5
TARGET_LOWER_SOURCE=POSITIVE_TORIC_MAIN_TERM
TARGET_REAL_CHAMBER_NONEMPTY=true
TARGET_REAL_CHAMBER_POSITIVE_MEASURE=true
THIRD_FACE_SQUARE_SUBTRACTION=LOWER_ORDER
TARGET_LOWER_ORDER_SHARP=true
```

## 3. Construction ledger boundary

Checkpoint50 asks for a lower-bound / construction ledger, but the repository does not need a new explicit order-sharp parametric construction to prove the lower bound: the audited full-population asymptotic is already stronger.

Accordingly Stage22 does **not** claim an elementary injective parameter family of size `B(log B)^5`. No such family has been isolated and audited at the present interface.

This distinction matters. A single sparse explicit family could prove infinitude while explaining little about the bulk `M_2` population. Here the order-sharp lower bound is a bulk theorem, so Stage22 records that fact rather than replacing it with a weaker construction narrative.

```text
EXPLICIT_ORDER_SHARP_PARAMETRIC_SUBFAMILY=NOT_CLAIMED
NEW_CONSTRUCTION_REQUIRED_FOR_LOWER_BOUND=false
BULK_LOWER_BOUND_ALREADY_PROVED=true
INFINITUDE_OF_TARGET_POPULATION=true
```

## 4. Source versus target lower-side architectures

Stage16 has an elementary lower construction for `M_1(B)`: choose a scaled primitive Pythagorean face, choose a complementary edge in a long interval coprime to the scale, and delete the sparse accidental-square cases. This directly produces the `B^2 log B` order.

Stage18's lower side is structurally different. Its full `B(log B)^5` order is supplied through the shared-edge double-Pythagorean toric surface and positive anticanonical chamber volume. Therefore the transition

```text
Stage16 source lower architecture:
  elementary scaled-face construction + free third edge

Stage18 target lower architecture:
  positive-volume toric bulk on the coupled shared-edge surface
```

is itself part of the causal ledger. It does not justify decomposing the relative `(log B)^4` into four independent constructive freedoms.

## 5. Relation to checkpoint40

Checkpoint40 identified the net exponent change

```text
POLYNOMIAL_RATIO_POWER=-1
LOG_RATIO_POWER=4
```

and left any finer local-factor decomposition unproved. Checkpoint50 closes the lower-side quantitative question at exactly the same scale:

```text
SHARP_LOWER_SCALE=(log B)^4/B
SHARP_UPPER_SCALE=(log B)^4/B
TWO_SIDED_ORDER_MATCH=true
LEADING_ASYMPTOTIC_ALREADY_PROVED=true
```

What remains for checkpoint60 is not another bound. It is the bounded causal synthesis: explain, only to the extent certified by the existing interfaces, how the source harmonic scaled-face architecture is replaced by the target Picard-rank-six toric architecture, while avoiding any fictitious factorization or double charging.

## 6. Non-claims

Stage22-50 does not claim:

- an explicit numerical value for `C_M2`;
- an elementary order-sharp parametric family for all `M_2`;
- four independent sources for the relative `log^4`;
- a local Euler-product explanation of the transition;
- any statement about existence or nonexistence of perfect cuboids.

Finite checkpoint20 data are diagnostic only and are not used as proof.

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
NEW_CONSTRUCTION_REQUIRED=false
SHARP_LOWER_SCALE=(log B)^4/B
NEXT_CHECKPOINT=60
NEXT_EXPECTED_COMMAND=Stage22-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
