# Stage14-num3 — extended exact census through B=50,000,000

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

with at least two integral face diagonals.  Exact-two objects are classified by the shared edge (`a`, `b`, or `c`), while any all-three-face object is retained separately as `T`.

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

## 2. Large-B engineering change

Num2's accelerated production kernel used both a full hypotenuse index and a global exact Pythagorean mate-pair set in memory.  That was fast at `B=2m`, but the reference run used about `1.94 GiB` RSS.

Num3 changes the engineering architecture without changing the mathematical population.

For a selected chunk count `C`, the shared face hypotenuse `p` is partitioned by

```text
p mod C.
```

Each worker keeps only the face triples in its own residue class, streams every outer primitive/scaled Pythagorean triple

\[
p^2+z^2=d^2,
\]

and then applies:

1. the exact early primitive gate `gcd(face_scale,z)=1`;
2. exact integer-square tests for the two possible second faces;
3. canonical sorting `(a,b,c)`;
4. a full exact revalidation of the space square and all three face masks.

No floating-point test is used for integrality.

The chunk ledgers are then canonically unioned and deduplicated.  The final 50m run uses `C=16`; all earlier frozen cutoff hashes remain unchanged under this finer partition.

## 3. Frozen exact census milestones

The completed num3 milestones are:

| B | N_a^(2) | N_b^(2) | N_c^(2) | N2 | T | active faces | max degree |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2,000,000 | 142 | 134 | 80 | 356 | 0 | 490 | 9 |
| 5,000,000 | 207 | 211 | 113 | 531 | 0 | 727 | 9 |
| 10,000,000 | 293 | 286 | 141 | 720 | 0 | 1007 | 9 |
| 20,000,000 | 392 | 388 | 197 | 977 | 0 | 1381 | 9 |
| 50,000,000 | 552 | 573 | 303 | 1428 | 0 | 2028 | 10 |

Every row is an exact finite census under the frozen population contract.

The first frozen milestone in this sequence at which the active-face graph maximum degree rises above 9 is `B=50,000,000`, where it reaches 10.  This is a finite graph observation only.

## 4. Ledger hashes

### B = 5,000,000

```text
object key
 a0ff9319332e6f088721674b9ff85654063ce343b9c57ad6378eba113f950c4b

object key + mask
 4970e3aa4dd17b36ba3b4f43d209759468f7e0d0fe82bcc87344dfb247bde611

active vertex ledger
 ca6bdbc276c015462b7ceabec45bcdb9eceb97595c2328f815f006ea79e6a0e9

raw-pair edge ledger
 a53df55f8fb25862948c419918f613c3fdf16df77a65891bad5e69aa7fd4b544
```

### B = 10,000,000

```text
object key
 02688a96a10f1ac600ff68d810eb9eb6e3ec7dd08d36bd9e9219d563453eba7b

object key + mask
 ca279aef6e57f1e7c5943b751f3a12293ca3d111f0bcd649377c5341198a7da0

active vertex ledger
 5a6b6a209c7b4cace86b2f75563a1c87f6dfaff9e8f02853a743692345275b98

raw-pair edge ledger
 43f765c215f07d6aa8ff73c6fb8d6541274a32ad33e3f3697d85168c6454ccc2
```

### B = 20,000,000

```text
object key
 b8a79e32c0b14c9cb85831b55f8aee0d08001fab204e0dfd652bd82e61e101db

object key + mask
 4bbc70256d5ba76040f2c0d9c0f6eea7459af5d78cdddd0e0946e4a19b9881ab

active vertex ledger
 bcfd27d6a6ec48cae77e8f972045d08f5edcd7c4ed7714c3bc457b1e184ed41f

raw-pair edge ledger
 38ef26e635e0c8e7d1017b9b18e85e7d7ba43de21e64c125ae58aafb7d2fa52c
```

### B = 50,000,000

```text
object key
 974b424a54d1b87bb0152bec37e3b21452f7eeafae5aa5c6b8eb40f949cde28b

object key + mask
 b884aef12eb496eb2ecf4191e0e4ef530a7239c28b97d41eeb3112c8b4ca6428

active vertex ledger
 c7372cb01837016f6f96cf6f09cef49740f3dc49f64cf895d773931a28a12748

raw-pair edge ledger
 ce0cb711e8df26021c1f7db672a9a11e93d9fadf0d1c074c57d64c4933557a5e
```

## 5. Finite scale diagnostics

For continuity with the earlier Stage14 finite observations, the exact values of `N2/sqrt(B)` at the frozen cutoffs are:

```text
B=2,000,000    0.2517300141024109
B=5,000,000    0.23747041921047765
B=10,000,000   0.2276839915321233
B=20,000,000   0.21846384140172945
B=50,000,000   0.20194969670687798
```

Across this finite range the normalized quantity declines rather than remaining near the earlier `~0.25` band.  This is useful evidence against treating the old square-root fit as already stabilized, but it is **not** evidence for any replacement asymptotic law.

At `B=50m` the finite direction proportions are approximately

```text
a : 552/1428 = 0.38655...
b : 573/1428 = 0.40126...
c : 303/1428 = 0.21218...
```

Again these are finite diagnostics only.

## 6. Triple / perfect-cuboid boundary

No retained primitive object through the frozen cutoff `B=50,000,000` has all three face diagonals integral:

```text
T(50,000,000) = 0
```

This statement is strictly bounded by the completed census.  It does **not** imply nonexistence of a perfect cuboid beyond the cutoff.

The workflow contains an emergency gate: if a future run produces `mask=111`, the normal num-stage closure is stopped and an independent second generation route is required before any candidate is reported as computationally verified.

## 7. Resource profile

The memory-bounded architecture makes the requested milestone range practical in GitHub Actions.

Representative exact workload totals:

```text
B=5m
  face entries across chunks      11,184,006
  candidate glues                 86,383,449
  full face-mask validations           1,062

B=20m
  face entries across chunks      49,149,097
  candidate glues                447,975,295
  full face-mask validations           1,954

B=50m, 16 chunks
  face entries across chunks     130,164,675
  candidate glues              1,315,660,162
  early nonprimitive rejects   1,105,072,970
  second-face square tests       421,172,707
  full face-mask validations           2,856
```

At `B=50m`, chunk build times were about `17.5--22.3 s` and kernel times about `63--186 s` on the reference hosted runners.  These timing numbers are environment-specific engineering measurements, not mathematical data.

## 8. Frozen boundary

```text
STAGE14_NUM3=COMPLETE_EXTENDED_EXACT_CENSUS
B5M_EXACT_CENSUS_FROZEN=true
B10M_EXACT_CENSUS_FROZEN=true
B20M_EXACT_CENSUS_FROZEN=true
B50M_EXACT_CENSUS_FROZEN=true
B2M_BASELINE_LEDGER_UNCHANGED=true
ALL_FROZEN_NUM3_MILESTONES_HASH_LOCKED=true
MEMORY_BOUNDED_CHUNK_ARCHITECTURE=true
MAX_DEGREE_AT_B50M=10
T_B50M=0
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
