# Stage14-num-alpha11-diag11 — cumulative survival uncertainty and stopping decision

Stage14-num-alpha11-diag11 adds finite-sample uncertainty bands to the merged diag8 cumulative matched denominator panel through `B=1,000,000` and decides whether the numerical diagnostic branch should continue expanding.

## B=1m cumulative signal

Observed relative second-face survival:

```text
ab : ac : bc = 0.604399 : 0.908758 : 1
```

Fitted cumulative multinomial calibration, 50,000 deterministic trials:

```text
ab/ac rate ratio 95% = [0.579408, 0.766555]
ab/bc rate ratio 95% = [0.527031, 0.695660]
ac/bc rate ratio 95% = [0.761017, 1.086201]
```

Therefore `ab` is distinctly less likely than both `ac` and `bc` to acquire a second integral face at the current B=1m finite panel. The `ac` versus `bc` ordering is not resolved at 95%.

This sharpens diag7/8: the robust finite signal is not a full strict `ab<ac<bc` theorem, but a two-tier pattern

```text
ab  <  {ac,bc}
```

with `ac` and `bc` still statistically overlapping.

## Cumulative drift from 100k to 1m

Using the diag10-style common-survival plugin, each disjoint shell keeps its exact raw-source composition and exact N2 total, and only pair directions are resampled. The resulting cumulative trajectory calibration gives:

```text
max cumulative shape deviation p = 0.894762
ab cumulative range p             = 0.899462
ac cumulative range p             = 0.536649
```

Thus the visible cumulative drift is entirely compatible with finite-count noise. No monotone convergence profile is detected.

At B=1m the common-survival trajectory gives pointwise 95% bands

```text
ab/bc : [0.524242, 0.690592]
ac/bc : [0.754087, 1.078756]
```

The conditional bridge target obtained from the proved Stage13 limiting source vector plus a hypothetical Stage14 exactly-two law `2:2:1`,

```text
0.548317 : 0.896253 : 1,
```

lies inside these B=1m bands. This is compatibility only, not evidence for an asymptotic `2:2:1` law.

## Stopping decision

The num-alpha diagnostic branch has now extracted the useful finite structure:

- exact B500m two-face census and near-`2:2:1` cumulative direction vector;
- p=7 local/divisibility signature;
- same-diagonal and face-graph cluster controls;
- exact Stage13 one-face -> Stage14 two-face endpoint bridge;
- persistent lower `ab` second-face survival through B=1m;
- shell volatility shown to be finite-count compatible;
- cumulative drift also shown to be finite-count compatible.

The high-value signal has already been handed to the proof side by the Stage14 bridge route. Extending the same diagnostic sequence by one more small census increment would mainly narrow error bars rather than create a new mathematical obstruction.

Therefore this branch is **parked after diag11**. Reopen it only if either:

1. a substantially larger matched raw-face denominator census becomes available, enough to multiply the exactly-two sample size materially; or
2. a proof-side chamber/local-density theorem produces a predeclared directional prediction that the census can test without post-selection.

No asymptotic second-face survival profile or exactly-two directional law is claimed.

```text
STAGE14_NUM_ALPHA11_DIAG11=CUMULATIVE_SURVIVAL_UNCERTAINTY_AND_STOPPING_DECISION_COMPLETE
B_MAX=1000000
TOTAL_N2=255
B1M_SURVIVAL_REL_BC=0.6043990674035388,0.9087577682163763,1
B1M_AB_AC_RATE_RATIO_95=0.5794082461257155,0.766555273563786
B1M_AB_BC_RATE_RATIO_95=0.5270308715232657,0.6956601229793399
B1M_AC_BC_RATE_RATIO_95=0.7610167844057517,1.0862012153391793
CUMULATIVE_MAX_SHAPE_DRIFT_P=0.8947621047579049
CUMULATIVE_AB_RANGE_P=0.8994620107597848
CUMULATIVE_AC_RANGE_P=0.5366492670146598
AB_RATE_LOWER_THAN_AC_AT_B1M_95_CALIBRATION=true
AB_RATE_LOWER_THAN_BC_AT_B1M_95_CALIBRATION=true
AC_VS_BC_RESOLVED_AT_B1M_95_CALIBRATION=false
CUMULATIVE_DRIFT_EXCEEDS_COMMON_SURVIVAL_NOISE_AT_5PCT=false
HYPOTHETICAL_STAGE13_LIMIT_PLUS_221_TARGET_INSIDE_B1M_POINTWISE_95_BANDS=true
ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM=false
ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM=false
NUM_ALPHA_DIAGNOSTIC_BRANCH_PARK_RECOMMENDED=true
NEXT=PAUSE_NUM_ALPHA_DIAG_BRANCH_AND_HAND_OFF_TO_STAGE14_BRIDGE_OR_PROOF_TRACKS
```
