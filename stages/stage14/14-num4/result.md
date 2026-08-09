# Stage14-num4 — unified cross-track fingerprint ledger

> STATUS: `STAGE14_NUM4=COMPLETE_UNIFIED_FINITE_FINGERPRINT_LEDGER`
>
> CLASSIFICATION: exact finite/derived finite data only. No asymptotic or perfect-cuboid existence/nonexistence claim is made here.

## 1. Frozen B=100m base

Stage14-num4 promotes the exact `B=100,000,000` Stage14-num3 census into a durable canonical object source and first revalidates all frozen num3 locks before joining any other track:

```text
physical objects                  1875
active oriented first faces       2687
raw pair edges                     1875
max graph degree                     11
(N_a^(2),N_b^(2),N_c^(2)) = (729,758,388)
T                                      0
```

The four num3 SHA-256 locks reproduce exactly:

```text
object key       b8151aedbf46f33700b213c79a5227fa62653d2279eed954103a2b9e768fff42
object+mask      2ac9a994f735d2d4f8f3c519145de17d920bdcf9841f32a73793cae3ec94e14f
active face      99f9cf72d473df19a2fc27e04032095607995ea43d874afd08a15e7fc7e240f0
raw-pair edge    c54aa6fea7971a44e317a041986ca1197671af2cab97825943ebb9d51cadd97e
```

The committed `b100m_objects.csv.parts/` is a compact chunked canonical CSV source reconstructed from all 32 deterministic num3 Actions chunks; the audit combines its deterministic rows before validating the frozen hashes. The full cross-track ledger is generated deterministically in CI rather than committed as a multi-megabyte raw dump.

## 2. Joined fingerprints

For every one of the 2687 active first-face keys `(S,X,H)`, num4 records its exact first physical hit `d`, partner multiplicity through `B=100m`, first-hit object/partner, directions seen, and the Stage14-s1 integral elliptic specialization

```text
W^2 = Z(Z-S^2)(Z+X^2),
a2 = X^2-S^2,
a4 = -S^2 X^2.
```

For every one of the 1875 physical raw-pair edges, num4 reconstructs the Stage14-e9 canonical ambient ordering `x<y` and imports the exact inverse

```text
u=gcd(e,x), v=gcd(e,y), g=e/(uv), gcd(u,v)=1,
S1=g v, S2=g u, lcm(S1,S2)=e,
```

plus the six-state fingerprints at `p=2,3,5,7,11,13`.

Finite diagnostics at `B=100m` include `971` distinct `g` values and `59` edges with `g=1`. The active-face degree histogram reaches the frozen maximum `11`; the unique degree-11 face is `(528,455,697)` and its first physical hit is `d=4453`.

## 3. Honest null policy

The roadmap requires missing theorem-sensitive fields to remain null rather than being recomputed under a potentially different normalization. The merged s1 and s3 compact JSON artifacts contain aggregate/sample summaries but intentionally omit their per-face rows. Therefore the unified ledger leaves the following fields null unless a future merged row-level artifact supplies them:

```text
certified_rank_interval
selmer_2_summary
canonical_height_of_actual_first_hit
kummer_square_class_fingerprint
low_degree_bisection_class
```

No PARI rank, Selmer, or canonical-height calculation is rerun by num4. Provenance records the exact source stage, path/blob when available, PR, and merge commit for every imported normalization.

## 4. New reproducibility locks

```text
full unified ledger  fade5a039ae63490ff3422ec0b25b1474063ec5f47906826b838f656959a580c
face core ledger     52a214b0bbb782525f7b15afd275fc49662c19699b098054f01332d18264e8a5
edge fingerprints    9d49ad5643d2aa3753ebd142609c51e546aab281ee4fcbe4c844030e0ae06db8
provenance catalog   8aa69b3788b8e359314775c43f349a03fbb60f44a87c8ae2685d687d4a7c5192
```

CI regenerates the full ledger in temporary storage, compares the compact committed manifest byte-for-byte, and independently rechecks the frozen num3 base hashes.

## 5. Exit lock

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

Canonical artifacts:

```text
stages/stage14/14-num4/result.md
stages/stage14/scripts/14-num4/unified_fingerprint_ledger.py
stages/stage14/data/14-num4/b100m_objects.csv.parts/
stages/stage14/data/14-num4/unified_fingerprint_manifest.json
.github/workflows/stage14-num4-unified-fingerprint-ledger.yml
```
