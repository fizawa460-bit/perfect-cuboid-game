# Stage25 checkpoint70 — bounded maximal synthesis and closeout candidate

```text
CHECKPOINT=70
STATUS=CLOSEOUT_SUBMITTED_FOR_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16 -> Stage19
DEEP_RESEARCH_MODE=true
SOURCE_COUNT=M1(B)
TARGET_COUNT=N2(B)
```

## 1. Final theorem stack

Under the frozen primitive/canonical cutoff

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad R=\sqrt{a^2+b^2+c^2}\le B,
\]

Stage25 compares the Stage16 exactly-one-face population `M1(B)` with the Stage19 exactly-two-faces-plus-integral-space population `N2(B)`.

The audited source law is

\[
\boxed{M_1(B)\sim \frac{3}{4\pi^2}B^2\log B}.
\]

Checkpoint50 and checkpoint60 prove the target envelope

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

Therefore

\[
\boxed{B^{-7/4}(\log B)^{-1}\ll \frac{N_2(B)}{M_1(B)}
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}}.
\]

For fixed `epsilon<3/2`, the ratio tends to zero, while the lower bound gives `N2(B)->infinity`. Hence

```text
STAGE25_CLASS=THIN_BUT_POSITIVE_POWER_INFINITE
GLOBAL_ZERO_DENSITY_PROVED=true
TARGET_UNBOUNDEDNESS_PROVED=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
POSITIVE_POWER_LOWER_EXPONENT=1/4
MATCHING_HALF_POWER_LOWER_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

The exponent `1/4` is a proved lower exponent, not a claim that the true exponent equals `1/4`.

## 2. Population semantics

The transition is not a literal subset-survival transition because the source requires exactly one integral face while the target requires exactly two integral faces and integral space diagonal. Stage25 therefore uses a matched population-size ratio, not objectwise survival probability.

```text
SOURCE_CONTRACT=primitive canonical; exactly one integral face; no space requirement
TARGET_CONTRACT=primitive canonical; exactly two integral faces; integral R
COMMON_CUTOFF=R<=B
LITERAL_SUBSET_TRANSITION=false
RATIO_SEMANTICS=MATCHED_COMBINED_POPULATION_SIZE_RATIO
PATH_PRODUCTS_ARE_INDEPENDENCE_CLAIMS=false
```

## 3. Positive-power lower mechanism

R501, the first Meskhishvili rational NPC parametrization, yields a two-parameter primitive family with raw physical height degree eight. On a fixed open cone of reduced rational parameters there are `gg T^2` coprime parameter pairs with `m,n<=T`, the primitive gcd is uniformly bounded, the physical height is `asymp T^8`, and the parameter-to-similarity multiplicity is bounded.

The missing third face is controlled by a squarefree degree-16 polynomial, hence by a genus-7 hyperelliptic curve. Faltings' theorem is used only to remove finitely many rational third-face exceptions. Thus

\[
\boxed{N_{R501}(B)=\Theta(B^{1/4})},
\]

and therefore `N2(B)>>B^(1/4)`.

R502 independently supplies a second same-exponent family,

\[
\boxed{N_{R502}(B)=\Theta(B^{1/4})},
\]

with audited primitive gcd bound `2592`. It certifies robustness of the quarter-power lower but does not raise the exponent.

## 4. Causal interaction theorem

Let

\[
F=M_2/M_1,\qquad S=N_1/M_1,\qquad A=N_2/M_2,\qquad T=N_2/N_1.
\]

The exact cross-ratio identity is

\[
\boxed{I=\frac{A}{S}=\frac{T}{F}=\frac{N_2M_1}{M_2N_1}}.
\]

Using the audited Stage22/Stage23/Stage24 interfaces and the Stage25 quarter-power lower gives

\[
\boxed{I(B)\gg B^{1/4}(\log B)^{-7}\to\infty}.
\]

Thus the second-face and space-diagonal requirements exhibit a positive divergent interaction in population-ratio semantics. This is an exact count-ratio statement, not a probabilistic independence assertion.

## 5. Deep-route registry at closeout

```text
R501=PROVED_AUDITED_THETA_B_QUARTER
R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R504_ORIGINAL_BASE=CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R504_RANK_TWO_PHYSICAL_LATTICE=CLOSED_NO_QUARTER_UPGRADE_AUDITED_PASS
R504_GROWING_LATTICE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE_AUDITED_PASS
R504_FULL_SPLIT_GENERIC_PRYM_E0_FACTOR=EXCLUDED_OVER_GENERIC_BASE_FIELD_AUDITED_PASS
R504_FULL_SPLIT_EXCEPTIONAL_PRYM=EXTERNAL_THEOREM_GATE_AUDITED_PASS
R505=EXTERNAL_THEOREM_GATE_PREVIOUS_MATH_ACCEPTED
R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_PREVIOUS_MATH_ACCEPTED
R507=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
```

The R504 exceptional Prym gate does not assert that exceptional rational specializations are empty or finite. The geometric `Kbar` factor question and unbounded isogeny-degree union remain external.

R505 remains the exact common-squarefree-core receiver; further progress requires genuinely stronger common-core counting mathematics. R506 is the same target in rank-one/common-leg toric coordinates and is not independent.

## 6. Backflow synchronization

Checkpoint50 already propagated the positive-power target lower to Stage19, Stage23 and Stage24. In particular the current audited backflow contains

\[
N_2/N_1\gg B^{-3/4}(\log B)^{-3},
\qquad
N_2/M_2\gg B^{-3/4}(\log B)^{-5},
\]

with the corresponding positive/divergent interaction signs. All later checkpoint60 rounds explicitly retained `GLOBAL_STAGE25_LOWER_CHANGED=false`, so there is no additional theorem delta to propagate at checkpoint70.

```text
BACKFLOW_STATUS=PASS_NO_DELTA_AFTER_CHECKPOINT50
STAGE23_BACKFLOW_CURRENT=true
STAGE24_BACKFLOW_CURRENT=true
GLOBAL_STAGE25_LOWER_CHANGED=false
```

## 7. Checkpoint60 deep stop

PR #999 hostile audit accepted

```text
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=true
CHECKPOINT60_CLOSED=true
STAGE70_ALLOWED=true
```

All identified repo-native high-value routes are now proved/closed or reduced to audited external-theorem gates. This is a bounded research stop, not an assertion that every imaginable future method has been exhausted.

## 8. Checkpoint70 closeout submission state

This file does not self-certify closure. Fresh checkpoint70 audit is required.

```text
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=
MERGE_ALLOWED=false
CLOSE_STAGE_AFTER_AUDIT_PASS=true
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
ARSENAL_PROMOTION_MATERIALIZED=true
AGGRESSIVE_SEARCH_LEDGER_MATERIALIZED=true
STAGE25_REENTRY_UNLOCKED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
```
