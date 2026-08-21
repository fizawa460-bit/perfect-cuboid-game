# Stage29 numerical mainline integration — R04

```text
TASK=Stage29-numerical-mainline-integration-R04
SOURCE_TRACKS=Stage29-num1,Stage29-num2,Stage29-num3
SOURCE_PRS=1291,1294,1296
SOURCE_STATUS=MERGED_MAIN
ROLE=IMPORT_EXACT_FINITE_NUMERICAL_RESULTS_INTO_STAGE29_MAINLINE
COMMON_MAX_CUTOFF_B=1000000000
AUDIT_REQUIRED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## Imported facts

The Stage29 numerical side tracks now supply a matched exact finite panel for the three load-bearing populations under the common physical contract

```text
0<a<b<c
gcd(a,b,c)=1
R^2=a^2+b^2+c^2<=B^2
```

at the common checkpoints `1e6, 5e6, 1e7, 5e7, 1e8, 2e8, 5e8, 1e9`.

The common endpoint is

```text
B=1000000000
M2=51379127865
N2=4566
M3=4362
P=0
```

where:

- `M2` = exactly two integral faces, no space-diagonal requirement;
- `N2` = exactly two integral faces plus integral space diagonal;
- `M3` = all three integral faces, no space-diagonal requirement;
- `P` = all three integral faces plus integral space diagonal.

## Stage29 use

This integration creates a clean finite condition-cost panel without changing any proof-level theorem.

At matched cutoff, `N2/M2` is a literal finite survival fraction for the additional integral-space condition. At `B=1e9`,

```text
N2/M2 = 8.886877200401853e-8
```

while

```text
M3/M2 = 8.489828810370757e-8
M3/N2 = 0.9553219448094612
```

are adjacent/different-population diagnostics only. They are not promoted to objectwise survival probabilities or limiting laws.

The exact finite negative-control range is also extended to

```text
P(B)=0 for B<=1000000000
```

with the M3-side complete census and N2-side triple-face check agreeing at the common endpoint. This remains finite exhaustive evidence only and is not a global perfect-cuboid nonexistence theorem.

## Canonical mainline entry points

- `stages/stage29/numerical-ledger.md`
- `stages/stage29/numerical-ledger.json`
- `stages/stage29/num1/result.md`
- `stages/stage29/num1/data/m3_census_manifest.json`
- `stages/stage29/num2/result.md`
- `stages/stage29/num2/data/n2_census_manifest.json`
- `stages/stage29/num3/result.md`
- `stages/stage29/num3/data/m2_census_manifest.json`

The historical audited `29-01/result.md` remains frozen and therefore still records the then-current `5e8` finite endpoint. The current Stage29 finite numerical truth is carried by this integration record, the R04 numerical ledger, and the current controller. No reopen of the audited 29-01 proof checkpoint is required.

## Downstream routing

The R04 panel is approved as an input to the existing Stage29 route, especially:

```text
29-04 condition-cost/mechanism diagnostics
29-08 parametrization coverage atlas/regression
endpoint negative-control checks
matched-cutoff finite diagnostics
```

It does not alter the active `29-02` suffix queue and does not create a new foundation/backflow decision by itself.

```text
STAGE29_NUMERICAL_MAINLINE_IMPORTED=true
NUMERICAL_LEDGER_REVISION=R04
M2_1E9=51379127865
M3_1E9=4362
N2_1E9=4566
P_FINITE_ZERO_THROUGH_B=1000000000
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
P_GLOBAL_ZERO_THEOREM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
STAGE29_02_ROUTE_CHANGED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```
