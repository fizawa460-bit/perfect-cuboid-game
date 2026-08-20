# Stage28-20 — matched finite bridge baseline

```text
TASK_ID=Stage28-20
CHECKPOINT=20
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=DERIVED_EXACT_FINITE
```

## 1. Contract carried from checkpoint10

Stage28 compares

- `N2(B)`: primitive canonical exactly-two-face cuboids with integral space diagonal, `R<=B`;
- `M3(B)`: primitive canonical exactly-three-face Euler cuboids with no space requirement, `R<=B`.

The endpoint populations are disjoint by exact face multiplicity. The primary bridge quantity

\[
\mathcal R_{28}(B)=\frac{M_3(B)}{N_2(B)}
\]

is a matched population-size ratio, not a survival probability.

## 2. Numerical reuse preflight

No new enumeration is required. The exact Stage27 `N2` panel and exact Stage20/Stage14-e Euler panel already share several Euclidean cutoffs.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R05;Stage27-20 exact N2 ladder;Stage20 final exact M3 ladder
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_POPULATION_ADAPTER=select exact-two+space mask for N2; select exactly-three no-space Euler population for M3; both use primitive canonical physical objects and exact R<=B cutoff
NUM_EVIDENCE_LEVEL=DERIVED_EXACT_FINITE
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

The Stage14 numerical observatory is used only where the exact face mask and space requirement match the relevant endpoint. Its finite `T=0` statement is not used as any perfect-cuboid conclusion.

## 3. Matched common-cutoff panel

The following values are exact finite counts:

| `B` | `N2(B)` | `M3(B)` | `M3(B)/N2(B)` |
|---:|---:|---:|---:|
| 10,000 | 25 | 18 | 0.720000000 |
| 50,000 | 62 | 42 | 0.677419355 |
| 200,000 | 116 | 82 | 0.706896552 |
| 1,000,000 | 255 | 219 | 0.858823529 |

Thus, on this matched finite panel, `M3/N2<1` at every displayed cutoff. The ratio is not monotone: it falls from `10k` to `50k` and then rises through `200k` and `1m`.

The broad finite effective exponent of the bridge ratio from `10,000` to `1,000,000`,

\[
\alpha_{\rm bridge,eff}
=
\frac{\log((219/255)/(18/25))}{\log(100)},
\]

is approximately

\[
0.038285719.
\]

This is a diagnostic only. It does not prove that `M3/N2` grows, tends to a constant, crosses one, or has a power-law asymptotic.

## 4. Interpretation firewall

The finite panel does not order the asymptotic populations. In particular:

```text
FINITE_PANEL_M3_LT_N2_THROUGH_1M=true
FINITE_RATIO_MONOTONE=false
FINITE_RATIO_LIMIT_IDENTIFIED=false
FINITE_EFFECTIVE_EXPONENT_AS_THEOREM=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
```

No interpolation is inserted at cutoffs where both exact endpoint counts are not available. The Stage27 `N2(500,000,000)=3495` endpoint is not paired with an `M3(500,000,000)` value and is therefore not used in the Stage28 matched bridge panel.

## 5. Checkpoint20 conclusion

Checkpoint20 supplies the finite baseline requested by the canonical roadmap without opening a new computational route.

```text
CHECKPOINT20_FINITE_BASELINE_COMPLETE=true
NUM_REUSE_CHECK=PASS
NEW_COMPUTATION_PERFORMED=false
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=30
MERGE_ALLOWED=false
```
