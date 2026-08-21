# Stage29 numerical ledger

```text
LEDGER=STAGE29_NUMERICAL_MAINLINE_R02
SOURCE_TRACK=Stage29-num1
SOURCE_PRS=1289,1291
ROLE=FINITE_EXACT_EVIDENCE_ONLY
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This is the Stage29 mainline entry point for audited/merged numerical side-track results. It does not replace the proof spine and it does not promote finite computation to an asymptotic theorem.

## Imported population contract

`M3(B)` counts primitive canonical Euler cuboids under the exact physical Euclidean cutoff

```text
R^2=a^2+b^2+c^2 <= B^2,
gcd(a,b,c)=1,
all three face diagonals integral,
no space-diagonal integrality requirement.
```

The source track is `stages/stage29/num1/`. Its production enumerator is a complete odd-edge/divisor enumeration with exact integer arithmetic, not a selected known-family generator.

## Exact checkpoints

| B | M3(B) | increment from previous checkpoint | P(B) |
|---:|---:|---:|---:|
| 1,000,000 | 219 | 137 from 2e5 | 0 |
| 5,000,000 | 480 | 261 | 0 |
| 10,000,000 | 656 | 176 | 0 |
| 50,000,000 | 1,298 | 642 | 0 |
| 100,000,000 | 1,757 | 459 | 0 |
| 200,000,000 | 2,339 | 582 | 0 |
| 500,000,000 | 3,331 | 992 | 0 |
| 1,000,000,000 | **4,362** | **1,031** | **0** |

Locked regression points remain

```text
M3(10^4)=18
M3(5*10^4)=42
M3(2*10^5)=82
M3(10^6)=219
```

## Validation

Through `B=500,000,000`, the side track independently validated all 3556 aligned F. Helenius / Giovanni Resta OEIS records from A031173/A031174/A031175 using exact integer face-diagonal, gcd, and Euclidean-cutoff checks.

The `B=1,000,000,000` extension is a direct complete-enumerator run:

```text
CI_RUN=32445467962
ALGORITHM=stage29-num1-odd-edge-divisor-v2
M3_1E9=4362
P_1E9=0
RUNTIME_SEC=130.952
THREADS=4
PRODUCTION_ARTIFACT=9433940026
PRODUCTION_ARTIFACT_SHA256=70273cda89d28d2701bf1da77ece739dbfdff36a79a800f895a09f9e726a040a
PRIMARY_MANIFEST=stages/stage29/num1/data/m3_census_manifest.json
RAW_1E9_RECORD=stages/stage29/num1/data/m3_1e9_run.json
```

## N2 comparison correction

The R01 ledger contained a provisional `N2` comparison series `5,8,10,15,17,18,27`. The `10^9` extension rechecked this against the frozen Stage19 interface and found that it is not the canonical Stage19 `N2` population: Stage19 records `N2(500,000,000)=3495` for primitive canonical exactly-two-face cuboids with integral space diagonal.

The provisional N2 fields and all derived `M3/N2` ratios are therefore withdrawn. **No M3 count changes.** A canonical matched-cutoff N2 panel is deferred to the dedicated two-face-plus-space-diagonal numerical run.

```text
N2_PROVISIONAL_SERIES_RETRACTED=true
M3_COUNTS_AFFECTED=false
N2_RECOMPUTE_DEFERRED=true
```

## Endpoint finite ledger

No Euler cuboid in the exact finite census through `R<=1,000,000,000` has integral space diagonal. Therefore

```text
P(B)=0 for B<=1000000000
```

is retained as exact finite exhaustive evidence under the matching primitive/canonical physical contract.

This statement is bounded. It is not a theorem that `P(B)=0` for all `B`, and it must never be used as a perfect-cuboid nonexistence proof.

## Mainline reuse policy

The imported census is approved as a finite-data input for:

- Stage29 parametrization coverage checks (`29-08` and relevant suffixes);
- endpoint-family regression and negative-control tests;
- exact testing of maps/coverage claims against the known finite Euler population;
- later Stage29 numerical suffixes that preserve the same population/cutoff adapter.

It is not approved for:

- fitting or asserting the true asymptotic exponent of `M3`;
- extrapolating `P(B)=0` beyond the verified cutoff;
- multiplying finite trends into analytic/geometric savings;
- any `M3/N2` diagnostic until the canonical N2 panel is re-established.

```text
STAGE29_NUM1_MAINLINE_IMPORTED=true
M3_1E9=4362
P_FINITE_ZERO_THROUGH_B=1000000000
FINITE_M3_ASYMPTOTIC_CLAIM=false
P_GLOBAL_ZERO_THEOREM=false
NEXT_NUM_REUSE_TARGET=29-08_AND_ENDPOINT_DIAGNOSTICS
```
