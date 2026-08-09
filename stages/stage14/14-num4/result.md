# Stage14-num4 — unified cross-track fingerprint ledger

> STATUS: `STAGE14_NUM4=COMPLETE_UNIFIED_FINITE_FINGERPRINT_LEDGER`
>
> CLASSIFICATION: exact finite / derived finite data only. No asymptotic or perfect-cuboid existence/nonexistence claim is made here.

## Frozen B=100m base

The Stage14-num3 `B=100,000,000` population was reconstructed from all 32 deterministic Actions chunks and independently revalidated before any cross-track join:

```text
physical objects                  1875
active oriented first faces       2687
raw pair edges                     1875
max graph degree                     11
(N_a^(2),N_b^(2),N_c^(2)) = (729,758,388)
T                                      0
```

All four num3 locks reproduced exactly:

```text
object key       b8151aedbf46f33700b213c79a5227fa62653d2279eed954103a2b9e768fff42
object+mask      2ac9a994f735d2d4f8f3c519145de17d920bdcf9841f32a73793cae3ec94e14f
active face      99f9cf72d473df19a2fc27e04032095607995ea43d874afd08a15e7fc7e240f0
raw-pair edge    c54aa6fea7971a44e317a041986ca1197671af2cab97825943ebb9d51cadd97e
```

The num roadmap explicitly forbids turning the repository into a raw-data dump, so num4 commits the compact manifest/hashes and a replay tool rather than duplicating the 32 num3 chunk artifacts. The exact num3 Actions run and head SHA are recorded in provenance.

## Joined fingerprints

For every active first-face key `(S,X,H)`, num4 derives exact first physical hit `d`, partner multiplicity through `B=100m`, first-hit object/partner, directions seen, and the Stage14-s1 integral elliptic specialization

```text
W^2 = Z(Z-S^2)(Z+X^2),
a2 = X^2-S^2,
a4 = -S^2 X^2.
```

For every physical raw-pair edge, num4 reconstructs the Stage14-e9 canonical ambient ordering and imports

```text
u=gcd(e,x), v=gcd(e,y), g=e/(uv), gcd(u,v)=1,
S1=g v, S2=g u, lcm(S1,S2)=e,
```

plus six-state local fingerprints at `p=2,3,5,7,11,13`.

Finite diagnostics at `B=100m` include `971` distinct `g` values and `59` edges with `g=1`. The degree histogram reaches max degree `11`; the unique degree-11 face is `(528,455,697)` with first physical hit `d=4453`.

## Honest null policy

Merged s1/s3 artifacts contain aggregate/sample results but no frozen per-face row ledger. Therefore num4 does **not** rerun theorem-sensitive PARI rank/Selmer/canonical-height calculations under a fresh normalization. These remain null unless a future merged row-level source supplies them:

```text
certified_rank_interval
selmer_2_summary
canonical_height_of_actual_first_hit
kummer_square_class_fingerprint
low_degree_bisection_class
```

This is intentional provenance discipline, not missing-data imputation.

## Unified locks

```text
full unified ledger  fade5a039ae63490ff3422ec0b25b1474063ec5f47906826b838f656959a580c
face core ledger     52a214b0bbb782525f7b15afd275fc49662c19699b098054f01332d18264e8a5
edge fingerprints    9d49ad5643d2aa3753ebd142609c51e546aab281ee4fcbe4c844030e0ae06db8
provenance catalog   8aa69b3788b8e359314775c43f349a03fbb60f44a87c8ae2685d687d4a7c5192
```

## Exit lock

```text
STAGE14_NUM4=COMPLETE_UNIFIED_FINITE_FINGERPRINT_LEDGER
CANONICAL_OBJECT_KEYS_STABLE=true
SOURCE_PROVENANCE_RECORDED=true
CROSS_TRACK_JOIN_REPRODUCIBLE=true
THEOREM_SENSITIVE_FIELDS_RECOMPUTED=false
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num5 scaling and anomaly diagnostics
```

Canonical repository artifacts:

```text
stages/stage14/14-num4/result.md
stages/stage14/scripts/14-num4/unified_fingerprint_ledger.py
stages/stage14/data/14-num4/unified_fingerprint_manifest.json
.github/workflows/stage14-num4-unified-fingerprint-ledger.yml
```
