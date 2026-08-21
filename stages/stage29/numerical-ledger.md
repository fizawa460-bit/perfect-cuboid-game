# Stage29 numerical ledger

```text
LEDGER=STAGE29_NUMERICAL_MAINLINE_R04
SOURCE_TRACKS=Stage29-num1,Stage29-num2,Stage29-num3
ROLE=FINITE_EXACT_EVIDENCE_ONLY
COMMON_MAX_CUTOFF_B=1000000000
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This is the Stage29 mainline entry point for exact numerical side-track results. It does not replace the proof spine and finite computations are not promoted to asymptotic theorems.

## Population contracts

All three tracks use the common physical contract

```text
0<a<b<c
gcd(a,b,c)=1
R^2=a^2+b^2+c^2<=B^2
```

with exact integer arithmetic.

- `M2(B)`: exactly two integral face diagonals; space diagonal not required.
- `N2(B)`: exactly two integral face diagonals and integral space diagonal.
- `M3(B)`: all three integral face diagonals; space diagonal not required.
- `P(B)`: all three integral face diagonals and integral space diagonal.

Thus `N2(B)` is literally the matched `M2(B)` population intersected with `{R integral}`, so `N2/M2` is a legal finite survival fraction. `M3` is a different adjacent stratum, so `M3/M2` and `M3/N2` are matched-cutoff finite diagnostics, not objectwise survival probabilities.

## Matched exact checkpoints

| B | M2(B) | N2(B) | M3(B) | P(B) | finite N2/M2 | finite M3/M2 | finite M3/N2 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1,000,000 | 13,817,725 | 255 | 219 | 0 | 1.845456e-5 | 1.584921e-5 | 0.8588 |
| 5,000,000 | 97,499,562 | 531 | 480 | 0 | 5.446178e-6 | 4.923099e-6 | 0.9040 |
| 10,000,000 | 224,273,087 | 720 | 656 | 0 | 3.210372e-6 | 2.925005e-6 | 0.9111 |
| 50,000,000 | 1,525,891,974 | 1,428 | 1,298 | 0 | 9.358461e-7 | 8.506500e-7 | 0.9090 |
| 100,000,000 | 3,462,162,225 | 1,875 | 1,757 | 0 | 5.415691e-7 | 5.074863e-7 | 0.9371 |
| 200,000,000 | 7,827,445,549 | 2,457 | 2,339 | 0 | 3.138955e-7 | 2.988203e-7 | 0.9520 |
| 500,000,000 | 22,894,939,276 | 3,495 | 3,331 | 0 | 1.526538e-7 | 1.454907e-7 | 0.9531 |
| 1,000,000,000 | **51,379,127,865** | **4,566** | **4,362** | **0** | **8.886877e-8** | **8.489829e-8** | **0.9553** |

The dramatic finite thinning from `M2` to `N2` and the much smaller `M3` population are useful diagnostics, but no true exponent or eventual ordering is inferred from this table.

## M2 production track

Stage29-num3 supplies the exact Stage18 denominator population through `B=1e9` using an audited aggregate shared-edge counter. Its exact identity is

```text
G(B)=M2(B)+3*M3(B)
M2(B)=G(B)-3*M3(B)
```

with primitivity enforced by Möbius inversion. A materially different direct enumerator agrees exactly in total and all three directional counts at `B=1e6` and `B=1e7`.

Canonical source records:

- `stages/stage29/num3/result.md`
- `stages/stage29/num3/data/m2_census_manifest.json`
- `stages/stage29/num3/audit.md`

The `B=1e9` aggregate run certifies

```text
M2(1e9)=51379127865
M2_direction=(18376842946,21192298114,11809986805)
```

## N2 extension checkpoints

The canonical Stage19 N2 series is independently restored and extended:

| B | N2(B) | T(B) |
|---:|---:|---:|
| 500,000,000 | 3,495 | 0 |
| 600,000,000 | 3,767 | 0 |
| 700,000,000 | 3,991 | 0 |
| 800,000,000 | 4,192 | 0 |
| 900,000,000 | 4,379 | 0 |
| 1,000,000,000 | **4,566** | **0** |

Here `T` denotes triple-face records with integral space diagonal, i.e. perfect-cuboid hits. The new `500m<d<=1b` shell contributes exactly 1,071 N2 objects.

## Validation summary

M3 uses the complete odd-edge/divisor enumerator and records `M3(1e9)=4362`, `P(1e9)=0`.

N2 reuses the validated Stage14 diagonal-first engine, hash-locks the frozen `B=5e8` source, scans only the upper shell in twenty disjoint shards, and returns `N2(1e9)=4566`, `T(1e9)=0`.

M2 uses the audited Möbius aggregate counter and independent direct regressions described above. Its production artifacts cover every matched checkpoint in this ledger through `B=1e9`.

## Endpoint finite ledger

The exact endpoint-negative controls now reach the common physical cutoff

```text
P(B)=0 for B<=1000000000
```

through both the complete M3-side space-diagonal check and the canonical N2-side triple-face check. This is exact finite evidence only, not a global nonexistence theorem.

## Reuse policy

The M2, M3 and N2 panels are approved as Stage29 inputs for:

- `29-04` condition-cost diagnostics;
- `29-08` parametrization-coverage/regression checks;
- endpoint regression and negative controls;
- matched-cutoff finite diagnostics;
- the literal finite survival fraction `N2/M2`.

They are not approved for fitting true asymptotic exponents, promoting finite ratios to limiting laws, asserting eventual M3/N2 ordering, extrapolating `P(B)=0`, or multiplying finite trends into proof-level savings.

```text
M2_1E9=51379127865
M3_1E9=4362
N2_1E9=4566
P_FINITE_ZERO_THROUGH_B=1000000000
M2_PRODUCTION_COMPLETE=true
N2_CANONICAL_RECOMPUTE_COMPLETE=true
FINITE_M3_N2_ASYMPTOTIC_CLAIM=false
P_GLOBAL_ZERO_THEOREM=false
```
