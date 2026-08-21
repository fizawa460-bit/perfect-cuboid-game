# Stage29-num2 — canonical N2 exact finite census through B=1e9

Status: **EXACT CENSUS COMPLETE THROUGH `B=1,000,000,000`**

```text
NUM_REUSE_PREFLIGHT=PASS
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
N2_TRUE_EXPONENT_INFERRED=false
```

## Population contract

`N2(B)` is the Stage19 population of primitive canonical cuboids

```text
0<a<b<c
gcd(a,b,c)=1
a^2+b^2+c^2=d^2
R=d<=B
exactly two of a^2+b^2, a^2+c^2, b^2+c^2 are squares
```

Triple-face records with integral space diagonal are excluded from `N2` and tracked separately as `T` (perfect-cuboid hits).

## Exact checkpoints

| B | N2(B) | T(B) |
|---:|---:|---:|
| 1,000,000 | 255 | 0 |
| 5,000,000 | 531 | 0 |
| 10,000,000 | 720 | 0 |
| 50,000,000 | 1,428 | 0 |
| 100,000,000 | 1,875 | 0 |
| 200,000,000 | 2,457 | 0 |
| 500,000,000 | 3,495 | 0 |
| 600,000,000 | 3,767 | 0 |
| 700,000,000 | 3,991 | 0 |
| 800,000,000 | 4,192 | 0 |
| 900,000,000 | 4,379 | 0 |
| 1,000,000,000 | **4,566** | **0** |

New 100m-shell increments above the frozen B500m base are `+272,+224,+201,+187,+187`, for a total new shell contribution of `+1071` objects.

At B=1e9 the directional exact-two counts are

```text
(Na,Nb,Nc)=(1810,1798,958)
N2=4566
T=0
```

Endpoint hashes:

```text
object_key_sha256=2b3297e9709053312cf14e3e82db52ee5bcab21be24f3c04349512a9a9d7657b
object_key_mask_sha256=52597e854e44af14682462436a31d843fcd64ef8a604e51e87caa20b570b6bc0
```

## Reuse-first exact architecture

The run reuses the validated Stage14 diagonal-first alpha engine (`NUM-R01/R02/R03`). The frozen B500m compressed object source is decoded and checked against its CSV/BZ2/base64 SHA-256 locks and its complete Stage14 summary before extension.

Only the new shell `500,000,000 < d <= 1,000,000,000` is scanned. It is partitioned into twenty disjoint 25m diagonal shards. Each shard performs segmented exact factorization, primitive-impossible inert-prime rejection, exact sum-of-two-squares representation generation, collision enumeration, exact square testing, strict canonicalization, and primitive normalization. Because a physical object has one fixed integral body diagonal `d`, the shard union is exact and disjoint.

Locked regressions passed:

```text
N2(200,000,000)=2457
N2(500,000,000)=3495
T(500,000,000)=0
```

The twenty shard runtimes were about 201.6–303.1 seconds each on GitHub-hosted runners and ran in parallel. Their summed shard CPU/wall contribution was about 5723.8 seconds; this is not a scaling-law claim.

## Reproducibility

```text
algorithm=stage29-num2-reuse-alpha8-diagonal-shard-v1
wrapper_source=stages/stage29/num2/scripts/n2_extend_1e9.py
wrapper_git_blob_sha=6522b01fea7d241c5064cf9e82c41ba4c9c0f184
CI_RUN=32446975833
FINAL_ARTIFACT=9434485432
FINAL_ARTIFACT_SHA256=d3c546dda768aa25e71215eb7dcd422fe30e037162c856a25c0b329d38d7fcf0
FULL_OBJECT_ROWS=4566
```

The final artifact contains both the full exact report and the compressed 4566-row object ledger.

## Interpretation boundary

`T(B)=0` through `B=1e9` is exact finite evidence only. It is not a global perfect-cuboid nonexistence theorem. No asymptotic exponent for `N2` is inferred from these checkpoints. The data are intended for matched-cutoff finite diagnostics and later Stage29 endpoint/coverage work.
