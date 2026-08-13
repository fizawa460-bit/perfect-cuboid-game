# Stage14-num3 — extended exact census through B=100,000,000

> STATUS: `STAGE14_NUM3=COMPLETE_EXTENDED_EXACT_CENSUS`
>
> CLASSIFICATION: finite exact census + finite engineering diagnostics only.
>
> No asymptotic, square-root-law, directional-limit, or perfect-cuboid existence/nonexistence claim is made here.

## 1. Population contract

Num3 keeps the frozen Stage14 numerical population unchanged:

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\]

\[
a^2+b^2+c^2=d^2,\qquad d\le B,
\]

with at least two integral face diagonals. Exact-two objects are classified by the shared edge (`a`, `b`, or `c`), while any all-three-face object is retained separately as `T`.

The immutable `B=2,000,000` num1 baseline is reproduced exactly before any extended cutoff is accepted:

```text
(N_a^(2),N_b^(2),N_c^(2)) = (142,134,80)
N2 = 356
T = 0
raw pair edges = 356
active oriented face vertices = 490
max graph degree = 9
```

All four frozen num1 SHA-256 ledger locks also match exactly.

## 2. Large-B engineering architecture

Num3 replaces the large global in-memory mate index with deterministic shared-hypotenuse residue chunks. For chunk count `C`, the shared face hypotenuse `p` is partitioned by `p mod C`. Each worker keeps only its own face triples, streams every outer primitive/scaled Pythagorean triple `p^2+z^2=d^2`, applies the exact primitive gate `gcd(face_scale,z)=1`, exact integer-square tests for the possible second faces, canonical sorting `(a,b,c)`, and full exact face-mask revalidation. No floating-point integrality test is used.

Chunk ledgers are canonically unioned and deduplicated. The final `B=100m` run uses `C=32`; the previously frozen 5m/10m/20m/50m ledgers reproduce exactly under this finer partition.

## 3. Frozen exact census milestones

| B | N_a^(2) | N_b^(2) | N_c^(2) | N2 | T | active faces | max degree |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2,000,000 | 142 | 134 | 80 | 356 | 0 | 490 | 9 |
| 5,000,000 | 207 | 211 | 113 | 531 | 0 | 727 | 9 |
| 10,000,000 | 293 | 286 | 141 | 720 | 0 | 1007 | 9 |
| 20,000,000 | 392 | 388 | 197 | 977 | 0 | 1381 | 9 |
| 50,000,000 | 552 | 573 | 303 | 1428 | 0 | 2028 | 10 |
| 100,000,000 | 729 | 758 | 388 | 1875 | 0 | 2687 | 11 |

Every row is an exact finite census under the frozen population contract. The first listed frozen milestone with maximum degree 10 is `B=50m`; the first with maximum degree 11 is `B=100m`. These are finite graph observations only.

## 4. Ledger hashes

### B = 5,000,000

```text
object key            a0ff9319332e6f088721674b9ff85654063ce343b9c57ad6378eba113f950c4b
object key + mask     4970e3aa4dd17b36ba3b4f43d209759468f7e0d0fe82bcc87344dfb247bde611
active vertex ledger  ca6bdbc276c015462b7ceabec45bcdb9eceb97595c2328f815f006ea79e6a0e9
raw-pair edge ledger  a53df55f8fb25862948c419918f613c3fdf16df77a65891bad5e69aa7fd4b544
```

### B = 10,000,000

```text
object key            02688a96a10f1ac600ff68d810eb9eb6e3ec7dd08d36bd9e9219d563453eba7b
object key + mask     ca279aef6e57f1e7c5943b751f3a12293ca3d111f0bcd649377c5341198a7da0
active vertex ledger  5a6b6a209c7b4cace86b2f75563a1c87f6dfaff9e8f02853a743692345275b98
raw-pair edge ledger  43f765c215f07d6aa8ff73c6fb8d6541274a32ad33e3f3697d85168c6454ccc2
```

### B = 20,000,000

```text
object key            b8a79e32c0b14c9cb85831b55f8aee0d08001fab204e0dfd652bd82e61e101db
object key + mask     4bbc70256d5ba76040f2c0d9c0f6eea7459af5d78cdddd0e0946e4a19b9881ab
active vertex ledger  bcfd27d6a6ec48cae77e8f972045d08f5edcd7c4ed7714c3bc457b1e184ed41f
raw-pair edge ledger  38ef26e635e0c8e7d1017b9b18e85e7d7ba43de21e64c125ae58aafb7d2fa52c
```

### B = 50,000,000

```text
object key            974b424a54d1b87bb0152bec37e3b21452f7eeafae5aa5c6b8eb40f949cde28b
object key + mask     b884aef12eb496eb2ecf4191e0e4ef530a7239c28b97d41eeb3112c8b4ca6428
active vertex ledger  c7372cb01837016f6f96cf6f09cef49740f3dc49f64cf895d773931a28a12748
raw-pair edge ledger  ce0cb711e8df26021c1f7db672a9a11e93d9fadf0d1c074c57d64c4933557a5e
```

### B = 100,000,000

```text
object key            b8151aedbf46f33700b213c79a5227fa62653d2279eed954103a2b9e768fff42
object key + mask     2ac9a994f735d2d4f8f3c519145de17d920bdcf9841f32a73793cae3ec94e14f
active vertex ledger  99f9cf72d473df19a2fc27e04032095607995ea43d874afd08a15e7fc7e240f0
raw-pair edge ledger  c54aa6fea7971a44e317a041986ca1197671af2cab97825943ebb9d51cadd97e
```

## 5. Finite scale diagnostics

The exact finite values of `N2/sqrt(B)` are:

```text
B=2,000,000      0.2517300141024109
B=5,000,000      0.23747041921047765
B=10,000,000     0.2276839915321233
B=20,000,000     0.21846384140172945
B=50,000,000     0.20194969670687798
B=100,000,000    0.1875
```

Across the completed finite range this normalized quantity continues to decline. That is evidence against treating the earlier `~0.25` square-root fit as already stabilized, but it is not evidence for a replacement asymptotic law.

At `B=100m` the finite direction proportions are exactly/approximately:

```text
a : 729/1875 = 0.3888
b : 758/1875 = 0.4042666666...
c : 388/1875 = 0.2069333333...
```

These are finite diagnostics only.

## 6. Triple / perfect-cuboid boundary

No retained primitive object through the frozen cutoff `B=100,000,000` has all three face diagonals integral:

```text
T(100,000,000) = 0
```

This statement is strictly bounded by the completed census and does not imply nonexistence beyond the cutoff. The workflow retains the emergency gate: if a future run produces `mask=111`, normal num-stage closure stops and an independent second generation route is required before any candidate is reported as computationally verified.

## 7. Resource profile

Representative exact workload totals:

```text
B=50m, 16 chunks
  face entries across chunks     130,164,675
  candidate glues              1,315,660,162
  early nonprimitive rejects   1,105,072,970
  second-face square tests       421,172,707
  full face-mask validations           2,856

B=100m, 32 chunks
  face entries across chunks     271,360,653
  candidate glues              2,957,514,013
  early nonprimitive rejects   2,499,324,057
  second-face square tests       916,377,696
  full face-mask validations           3,750
```

At `B=100m`, chunk build CPU times were about `26.1--40.9 s` and kernel CPU times about `113.6--306.4 s` on the reference hosted runners. The largest chunk face index contained `9,606,180` entries. These are environment-specific engineering measurements, not mathematical data.

## 8. Frozen boundary

```text
STAGE14_NUM3=COMPLETE_EXTENDED_EXACT_CENSUS
B5M_EXACT_CENSUS_FROZEN=true
B10M_EXACT_CENSUS_FROZEN=true
B20M_EXACT_CENSUS_FROZEN=true
B50M_EXACT_CENSUS_FROZEN=true
B100M_EXACT_CENSUS_FROZEN=true
B2M_BASELINE_LEDGER_UNCHANGED=true
ALL_FROZEN_NUM3_MILESTONES_HASH_LOCKED=true
MEMORY_BOUNDED_CHUNK_ARCHITECTURE=true
MAX_DEGREE_AT_B100M=11
T_B100M=0
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
SQRT_B_ASYMPTOTIC_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT=Stage14-num4 unified cross-track fingerprint ledger
```

Canonical artifacts:

```text
stages/stage14/14-num3/result.md
stages/stage14/scripts/14-num3/extended_exact_census.py
stages/stage14/data/14-num3/census_manifest.json
.github/workflows/stage14-num3-extended-census.yml
```
