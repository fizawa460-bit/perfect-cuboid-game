# Stage29 numerical ledger

```text
LEDGER=STAGE29_NUMERICAL_MAINLINE_R01
SOURCE_TRACK=Stage29-num1
SOURCE_PR=1289
SOURCE_STATUS=MERGED_MAIN
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

The source track is `stages/stage29/num1/`, merged by PR #1289. Its production enumerator is a complete odd-edge/divisor enumeration with exact integer arithmetic, not a selected known-family generator.

## Exact imported checkpoints

| B | M3(B) | increment from previous main checkpoint | P(B) | N2(B) finite diagnostic |
|---:|---:|---:|---:|---:|
| 1,000,000 | 219 | 137 from 2e5 | 0 | 5 |
| 5,000,000 | 480 | 261 | 0 | 8 |
| 10,000,000 | 656 | 176 | 0 | 10 |
| 50,000,000 | 1,298 | 642 | 0 | 15 |
| 100,000,000 | 1,757 | 459 | 0 | 17 |
| 200,000,000 | 2,339 | 582 | 0 | 18 |
| 500,000,000 | **3,331** | **992** | **0** | 27 |

Locked regression points also remain

```text
M3(10^4)=18
M3(5*10^4)=42
M3(2*10^5)=82
M3(10^6)=219
```

## Independent validation

The side track independently validated all 3556 aligned F. Helenius / Giovanni Resta OEIS records from A031173/A031174/A031175 using exact integer face-diagonal, gcd, and Euclidean-cutoff checks.

```text
CI_RUN=32444158502
CROSSCHECK_ARTIFACT=9433468039
PRIMARY_MANIFEST=stages/stage29/num1/data/m3_census_manifest.json
PRIMARY_RESULT=stages/stage29/num1/result.md
```

## Endpoint finite ledger

No Euler cuboid in the exact finite census through `R<=500,000,000` has integral space diagonal. Therefore

```text
P(B)=0 for B<=500000000
```

is retained as exact finite exhaustive evidence under the matching primitive/canonical physical contract.

This statement is bounded. It is not a theorem that `P(B)=0` for all `B`, and it must never be used as a perfect-cuboid nonexistence proof.

## Mainline reuse policy

The imported census is approved as a finite-data input for:

- Stage29 parametrization coverage checks (`29-08` and relevant suffixes);
- endpoint-family regression and negative-control tests;
- matched-cutoff finite diagnostics involving `M3`, `N2`, and `P`;
- exact testing of maps/coverage claims against the known finite Euler population;
- later Stage29 numerical suffixes that preserve the same population/cutoff adapter.

It is not approved for:

- fitting or asserting the true asymptotic exponent of `M3` or `N2`;
- promoting the finite growth of `M3/N2` to an eventual ordering theorem;
- extrapolating `P(B)=0` beyond the verified cutoff;
- multiplying finite trends into analytic/geometric savings.

```text
STAGE29_NUM1_MAINLINE_IMPORTED=true
M3_5E8=3331
P_FINITE_ZERO_THROUGH_B=500000000
FINITE_M3_OVER_N2_ASYMPTOTIC_CLAIM=false
P_GLOBAL_ZERO_THEOREM=false
NEXT_NUM_REUSE_TARGET=29-08_AND_ENDPOINT_DIAGNOSTICS
```
