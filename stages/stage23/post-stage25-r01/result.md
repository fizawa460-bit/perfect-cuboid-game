# Stage23 post-Stage25 — current positive-power backflow

STATUS=AUDITED_PASS_SYNCED_BY_STAGE25_REENTRY_70
HISTORICAL_STAGE23_PASS_REVOKED=false
ORIGINAL_SOURCE_STAGE=Stage25
ORIGINAL_SOURCE_CHECKPOINT=50
ORIGINAL_SOURCE_PR=984
LATEST_SOURCE_ROUTE=Stage25-um-r008a
LATEST_PARENT_TASK=Stage25-u24-r002a
LATEST_SOURCE_PR=1003
LATEST_SOURCE_MERGE_COMMIT=1d88e8e3254a383620e221df8a1a1039ebeabcd4
BACKFLOW_PR=1004
BACKFLOW_MERGE_COMMIT=11075adf8e30c73e5058790ee6ed6e2a9b6c9e2b
LATEST_SOURCE_AUDIT=stages/stage25/25-reentry-20/audit.md

The current global Stage19 target lower remains

\[
\boxed{N_2(B)\gg B^{1/4}}.
\]

Accordingly the global Stage23 ratio interface remains

\[
\frac{N_2(B)}{N_1(B)}\gg B^{-3/4}(\log B)^{-3},
\qquad
\frac{N_2(B)}{N_1(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Stage25-reentry phase20 does not change these global exponents. Its new content is that every canonical shared-edge Stage19 chamber has a quarter-power family, which strengthens all three Stage17 raw pair-overlap receiver channels.

## All shared-edge pair-overlap channels

For canonical edges `0<a<b<c`, an exactly-two-face object has one shared edge. The exact map is

- shared `a` -> integral faces `ab` and `ac`;
- shared `b` -> integral faces `ab` and `bc`;
- shared `c` -> integral faces `ac` and `bc`.

The audited phase20 directional theorem therefore gives the one-sided raw-overlap lower bounds

\[
\boxed{A_{ab,ac}(B)\gg B^{1/4}},
\]

\[
\boxed{A_{ab,bc}(B)\gg B^{1/4}},
\]

\[
\boxed{A_{ac,bc}(B)\gg B^{1/4}}.
\]

These are raw Stage17 overlap-measure statements. They are not literal objectwise survival probabilities and they do not provide a new directional asymptotic for the Stage17 source denominator.

```text
A_ab,ac(B)>>B^(1/4)
A_ab,bc(B)>>B^(1/4)
A_ac,bc(B)>>B^(1/4)
ALL_PAIR_OVERLAP_QUARTER_POWER_LOWER_PROVED=true
RAW_OVERLAP_IS_OBJECTWISE_SURVIVAL=false
SHARED_A_PAIR=ab,ac
SHARED_B_PAIR=ab,bc
SHARED_C_PAIR=ac,bc
```

## Global second-order interaction

Stage22 gives

\[
M_2/M_1\asymp B^{-1}(\log B)^4.
\]

Hence the exact global cross-ratio

\[
I=\frac{N_2/N_1}{M_2/M_1}
\]

still obeys

\[
\boxed{I(B)\gg B^{1/4}(\log B)^{-7}\to\infty}.
\]

The global positive/divergent sign remains unchanged; r008a only completes the directional raw-overlap lower surface.

```text
CURRENT_TARGET_LOWER=N2(B)>>B^(1/4)
RATIO_LOWER=N2/N1>>B^(-3/4)(log B)^(-3)
RATIO_UPPER=N2/N1<<_epsilon B^(-1/2+epsilon)(log B)^(-3)
TARGET_POSITIVE_POWER_LOWER_PROVED=true
TARGET_POSITIVE_POWER_EXPONENT=1/4
ALL_PAIR_OVERLAP_QUARTER_POWER_LOWER_PROVED=true
SECOND_ORDER_INTERACTION_SIGN=POSITIVE_DIVERGENT
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
GLOBAL_N2_EXPONENT_UPGRADED=false
BACKFLOW_ROUTE=Stage25-um-r008a
BACKFLOW_AUDIT_STATUS=PASS
BACKFLOW_SYNCHRONIZED=true
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
```
