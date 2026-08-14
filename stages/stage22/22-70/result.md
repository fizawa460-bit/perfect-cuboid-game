# Stage22-70 — bounded maximal synthesis / closeout repair

EVIDENCE_LEVEL=PROVED
CHECKPOINT=70
STATUS=CLOSEOUT_REPAIR_SUBMITTED_FOR_FRESH_AUDIT
MATHEMATICS_REOPEN_REQUIRED=false
REPAIR_SCOPE=CLOSEOUT_FLAGS_AND_REQUIRED_ARTIFACT_MATERIALIZATION_ONLY

## 1. Transition theorem

Under the common primitive/canonical physical cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B,
\]

Stage22 compares the disjoint adjacent strata `M1(B)` (exactly one integral face diagonal) and `M2(B)` (exactly two integral face diagonals), with no space-diagonal requirement. The ratio is a matched adjacent-stratum population-size ratio, not an objectwise survival probability.

The audited laws are

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
M_2(B)\sim C_{M_2}B(\log B)^5,
\qquad C_{M_2}>0,
\]

hence

\[
\boxed{\frac{M_2(B)}{M_1(B)}\sim
\frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}\to0}.
\]

Checkpoints40 and 50 supply matching sharp upper/lower order, so `M2/M1 asymp (log B)^4/B`.

## 2. Certified causal synthesis

The source architecture is one scaled primitive Pythagorean face with a harmonic scale sum and a complementary edge free at polynomial order `B`, producing `B^2 log B`.

The target architecture is two Pythagorean faces coupled through their unique shared edge, counted in bulk on the smooth split rank-6 anticanonical toric resolution, producing `B(log B)^5`.

Thus

```text
POLYNOMIAL_LOSS=B^-1
LOG_COMPENSATION=(log B)^4
```

The polynomial loss is localized to replacing the source free complementary-edge degree of freedom by the coupled second Pythagorean condition. The logarithmic compensation is localized, at the audited theorem interface, to the source harmonic scale architecture versus the target rank-6 anticanonical toric bulk.

Canonicalization, primitivity, the common cutoff, and physical multiplicity are shared interfaces rather than new causes. The third-face-square locus is `o(B(log B)^5)`, so the exactly-two nonsquare postfilter is lower order and not a leading cause. Finite checkpoint20 data are diagnostic only.

## 3. Fine-mechanism boundary

No canonical decomposition of the relative `log^4` into four independent arithmetic factors, local probabilities, valuation channels, squareclass channels, or four named toric divisors is proved.

```text
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
LOCAL_PROBABILITY_PRODUCT_PROVED=false
VALUATION_FACTORIZATION_PROVED=false
SQUARECLASS_FACTORIZATION_PROVED=false
UNIQUE_FINE_CAUSAL_DECOMPOSITION_PROVED=false
FINE_MECHANISM_OPEN=true
```

## 4. Required closeout decisions

The failed closeout audit correctly identified that `NEW_STANDALONE_THEOREM_PROMOTION_REQUIRED=false` is not a substitute for the two mandatory artifact decisions. They are now made explicitly.

### 4.1 Self-contained bundle

Stage22 freezes a reusable transition theorem, population contract, sharp ratio scale, causal ledger, leading-order exclusions, and fine-mechanism boundary. Reuse without reconstructing Stages16/18 therefore benefits materially from a standalone bundle.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_DECISION=YES
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
SELF_CONTAINED_BUNDLE_PATH=stages/stage22/22-70/self-contained-bundle.md
```

The required artifact is materialized at `stages/stage22/22-70/self-contained-bundle.md`.

### 4.2 Arsenal promotion

The matched transition law is a reusable interface for later adjacent-stratum comparisons, especially because its semantics explicitly block the false literal-subset interpretation and lock population/cutoff/multiplicity assumptions. This is weaponization-worthy even though it does not require a new standalone analytic theorem.

```text
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_DECISION=YES
ARSENAL_PROMOTION_MATERIALIZED=true
ARSENAL_PROMOTION_PATH=docs/stage22-arsenal-promotion.md
NEW_STANDALONE_THEOREM_PROMOTION_REQUIRED=false
```

The required reusable interface is materialized at `docs/stage22-arsenal-promotion.md`.

These statements are compatible: the arsenal entry packages the already-audited transition synthesis for direct reuse; it does not claim a new external analytic theorem.

## 5. Final ledger

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
LOG_COMPENSATION=(log B)^4
THIRD_FACE_EXCLUSION_IS_LEADING_CAUSE=false
COMMON_INTERFACE_DOUBLE_CHARGE=false
FINITE_DATA_USED_AS_PROOF=false
FINE_MECHANISM_OPEN=true
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_MATERIALIZED=true
PERFECT_CUBOID_CONCLUSION=NONE
```

## 6. Exit

No mathematics was reopened by this repair. Fresh Stage22 audit is required to validate the two closeout decisions and their materialized artifacts.

```text
UPSTREAM_PREMISE_CHECK=PASS
DOUBLE_CHARGE_CHECK=PASS
NEW_COMPUTATION_REQUIRED=false
NEW_ANALYTIC_INPUT=false
MATHEMATICS_REOPEN_REQUIRED=false
REPAIR_SCOPE=CLOSEOUT_FLAGS_AND_REQUIRED_ARTIFACT_MATERIALIZATION_ONLY
NEXT_CHECKPOINT=70
NEXT_STAGE=
NEXT_EXPECTED_COMMAND=Stage22-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CLOSE_STAGE_AFTER_AUDIT_PASS=true
CODEX_REQUIRED=false
```
