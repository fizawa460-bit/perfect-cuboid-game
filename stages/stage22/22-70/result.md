# Stage22-70 — bounded maximal synthesis / closeout

EVIDENCE_LEVEL=PROVED
CHECKPOINT=70
STATUS=CLOSEOUT_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Transition theorem

Under the common primitive/canonical physical cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B,
\]

Stage22 compares the disjoint adjacent strata

- `M1(B)`: exactly one integral face diagonal;
- `M2(B)`: exactly two integral face diagonals;

with no space-diagonal requirement. The transition is a population-size ratio, not a literal subset survival probability.

The audited source and target laws are

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0.
\]

Hence

\[
\boxed{\frac{M_2(B)}{M_1(B)}\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}\to0}.
\]

Checkpoints40 and 50 certify matching upper and lower order, so

\[
\frac{M_2(B)}{M_1(B)}\asymp \frac{(\log B)^4}{B}.
\]

## 2. Certified causal synthesis

The source architecture is one scaled primitive Pythagorean face with a harmonic scale sum and a complementary edge free at polynomial order `B`, producing `B^2 log B`.

The target architecture is two Pythagorean faces coupled through their unique shared edge. The resulting bulk is counted on the smooth split rank-6 anticanonical toric resolution, producing `B(log B)^5`.

Thus the main-order architectural replacement is

```text
one Pythagorean face + free complementary edge
    B^2 log B
        ->
shared-edge double-Pythagorean toric bulk
    B(log B)^5
```

and therefore

```text
POLYNOMIAL_LOSS=B^-1
LOG_COMPENSATION=(log B)^4
```

At the certified resolution, the polynomial loss is localized to replacing the source's free complementary-edge degree of freedom by the coupled second Pythagorean condition. The logarithmic compensation is localized to the difference between the source harmonic scale architecture and the target rank-6 anticanonical toric bulk.

## 3. Causes excluded from the leading transition

The following are not newly charged leading causes:

- strict canonicalization;
- global primitivity;
- the common cutoff `R<=B`;
- physical-object multiplicity conventions.

They are shared interfaces on both sides.

The exactly-two target also excludes the third square face, but Stage15 proves the three-face locus is `o(B(log B)^5)`. Hence that postfilter changes only lower-order terms and is not responsible for the leading `B^-1(log B)^4` transition.

Checkpoint20 finite ratios are diagnostic only and are not used as proof.

## 4. Maximality boundary

Stage22 has reached the strongest synthesis justified by the audited repository interfaces. In particular, the repository does not prove a canonical factorization of the relative `log^4` into four independent arithmetic causes, local probabilities, valuation channels, squareclass channels, or four named toric divisors.

The following remain explicitly unproved:

```text
FOUR_INDEPENDENT_LOG_FACTORS=false
LOCAL_PROBABILITY_PRODUCT=false
VALUATION_FACTORIZATION=false
SQUARECLASS_FACTORIZATION=false
UNIQUE_FINE_CAUSAL_DECOMPOSITION=false
```

This fine-mechanism gap does not weaken the exact asymptotic transition theorem or the bulk architectural localization.

## 5. Intrinsic / promotion status

The Stage22 result is intrinsically useful as a transition law and causal ledger between Stage16 and Stage18. Its theorem content is already inherited from audited source/target asymptotics plus the Stage22 interface comparison; no additional standalone analytic theorem is required for closeout.

No new ARSENAL/NUM theorem promotion is asserted solely from this closeout. If a future roadmap wants the transition law as a named reusable interface, that should be materialized explicitly in the appropriate registry rather than treating this classification sentence as promotion.

```text
INTRINSIC_STATUS=YES_AS_TRANSITION_SYNTHESIS
NEW_STANDALONE_THEOREM_PROMOTION_REQUIRED=false
PROMOTION_MATERIALIZED=false
PROMOTION_BY_CLASSIFICATION_ONLY=false
```

## 6. Stage22 final ledger

```text
TRANSITION=Stage16 -> Stage18
SOURCE=exactly one integral face diagonal
TARGET=exactly two integral face diagonals
COMMON_CUTOFF=R<=B
SPACE_DIAGONAL_REQUIRED=false
LITERAL_SUBSET_TRANSITION=false

SOURCE_ASYMPTOTIC=M1(B) ~ 3/(4*pi^2) B^2 log B
TARGET_ASYMPTOTIC=M2(B) ~ C_M2 B(log B)^5 ; C_M2>0
RATIO_ASYMPTOTIC=M2/M1 ~ (4*pi^2*C_M2/3)(log B)^4/B
RATIO_LIMIT=0
SHARP_SCALE=(log B)^4/B

POLYNOMIAL_LOSS=B^-1
POLYNOMIAL_LOCALIZATION=free complementary edge replaced by coupled second Pythagorean face
LOG_COMPENSATION=(log B)^4
LOG_LOCALIZATION=source harmonic scale architecture vs target rank-6 anticanonical toric bulk
THIRD_FACE_EXCLUSION_IS_LEADING_CAUSE=false
COMMON_INTERFACE_DOUBLE_CHARGE=false
FINITE_DATA_USED_AS_PROOF=false
FINE_MECHANISM_OPEN=true
PERFECT_CUBOID_CONCLUSION=NONE
```

## 7. Exit

Stage22 has no checkpoint after 70. Fresh audit is required before the stage can be declared closed.

```text
UPSTREAM_PREMISE_CHECK=PASS
DOUBLE_CHARGE_CHECK=PASS
NEW_COMPUTATION_REQUIRED=false
NEW_ANALYTIC_INPUT=false
NEXT_CHECKPOINT=
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage22-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CLOSE_STAGE_AFTER_AUDIT_PASS=true
CODEX_REQUIRED=false
```
