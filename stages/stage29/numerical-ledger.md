# Stage29 numerical ledger

```text
LEDGER=STAGE29_NUMERICAL_MAINLINE_R03
SOURCE_TRACKS=Stage29-num1,Stage29-num2
ROLE=FINITE_EXACT_EVIDENCE_ONLY
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This is the Stage29 mainline entry point for exact numerical side-track results. It does not replace the proof spine and finite computations are not promoted to asymptotic theorems.

## Population contracts

`M3(B)` counts primitive canonical Euler cuboids with all three integral face diagonals and no space-diagonal requirement. `N2(B)` counts primitive canonical cuboids with exactly two integral face diagonals and an integral space diagonal. Both use the same physical cutoff

```text
0<a<b<c
gcd(a,b,c)=1
R^2=a^2+b^2+c^2<=B^2
```

On `N2`, `R=d` is integral, so `R<=B` and `d<=B` are identical. These are different populations; neither is used as a survival denominator for the other.

## Matched exact checkpoints

| B | M3(B) | N2(B) | P(B) | finite M3/N2 |
|---:|---:|---:|---:|---:|
| 1,000,000 | 219 | 255 | 0 | 0.8588 |
| 5,000,000 | 480 | 531 | 0 | 0.9040 |
| 10,000,000 | 656 | 720 | 0 | 0.9111 |
| 50,000,000 | 1,298 | 1,428 | 0 | 0.9090 |
| 100,000,000 | 1,757 | 1,875 | 0 | 0.9371 |
| 200,000,000 | 2,339 | 2,457 | 0 | 0.9520 |
| 500,000,000 | 3,331 | 3,495 | 0 | 0.9531 |
| 1,000,000,000 | **4,362** | **4,566** | **0** | **0.9553** |

The ratio column is a matched-cutoff finite diagnostic only. The populations are structurally different, so it is not a conditional survival probability and no eventual ordering or exponent is inferred.

## N2 extension checkpoints

The canonical Stage19 N2 series has now been independently restored and extended:

| B | N2(B) | T(B) |
|---:|---:|---:|
| 500,000,000 | 3,495 | 0 |
| 600,000,000 | 3,767 | 0 |
| 700,000,000 | 3,991 | 0 |
| 800,000,000 | 4,192 | 0 |
| 900,000,000 | 4,379 | 0 |
| 1,000,000,000 | **4,566** | **0** |

Here `T` denotes triple-face records with integral space diagonal, i.e. perfect-cuboid hits. The new 500m→1b shell contributes exactly 1,071 N2 objects.

## Validation

M3 uses the complete odd-edge/divisor enumerator. Its exact B1b production run records `M3=4362`, `P=0`.

N2 reuses the validated Stage14 alpha diagonal-first engine. The frozen B500m object source is revalidated by its CSV/BZ2/base64 SHA locks and complete summary before scanning only `500m<d<=1b` in twenty disjoint 25m shards. The run re-locks

```text
N2(200m)=2457
N2(500m)=3495
```

and returns

```text
N2(1b)=4566
(Na,Nb,Nc)=(1810,1798,958)
T(1b)=0
N2_CI_RUN=32446975833
N2_ARTIFACT=9434485432
N2_ARTIFACT_SHA256=d3c546dda768aa25e71215eb7dcd422fe30e037162c856a25c0b329d38d7fcf0
N2_MANIFEST=stages/stage29/num2/data/n2_census_manifest.json
```

The earlier provisional series labeled N2 (`5,8,10,15,17,18,27`) remains retracted as a population mismatch and is superseded by this canonical exact panel.

## Endpoint finite ledger

Both complete finite computations agree that there is no perfect-cuboid hit through the common physical cutoff `R<=1,000,000,000`:

```text
P(B)=0 for B<=1000000000
```

This is exact finite evidence only, not a global nonexistence theorem.

## Reuse policy

The M3 and N2 panels are approved for Stage29 parametrization-coverage checks, endpoint regression/negative controls, and matched-cutoff finite diagnostics. They are not approved for fitting true asymptotic exponents, asserting eventual M3/N2 ordering, extrapolating `P(B)=0`, or multiplying finite trends into proof-level savings.

```text
M3_1E9=4362
N2_1E9=4566
P_FINITE_ZERO_THROUGH_B=1000000000
N2_CANONICAL_RECOMPUTE_COMPLETE=true
FINITE_M3_N2_ASYMPTOTIC_CLAIM=false
P_GLOBAL_ZERO_THEOREM=false
```
