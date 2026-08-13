# Stage14-num2 — exact enumerator acceleration and incremental architecture

> STATUS: `STAGE14_NUM2=COMPLETE_EXACT_ENUMERATOR_ACCELERATION`
>
> CLASSIFICATION: finite exact regression + engineering result only.
>
> No asymptotic, square-root-law, directional-limit, or perfect-cuboid existence/nonexistence claim is made here.

## 1. Input contract

Num2 inherits the immutable num1 `B=2,000,000` ledger locks:

```text
(N_a^(2),N_b^(2),N_c^(2)) = (142,134,80)
N2 = 356
T = 0
raw pair edges = 356
active oriented face vertices = 490
max graph degree = 9
```

and the four SHA-256 digests:

```text
object key
1869ce6d30b661a3ea53049f2c86ffda5dd3d23b14aa9511301d72b1d4e8a89a

object key + mask
84ce4239d482207ef8d961514c06b966f2eb9043fbbd5be3a7aea83d779314ce

active vertex ledger
0c91e088324a703253cf7c100569eb25971135a4481512de1f63aa7657396e5b

raw-pair edge ledger
cd8f0ffa7d26ce38e316b65644bb25d39857b5d074a8bb1b96db2e05e8714a1f
```

Num2 reproduces all four exactly, and also reproduces all eleven historical cutoff rows from `B=1,000` through `B=2,000,000`.

## 2. Exact early primitiveness gate

For a scaled primitive Pythagorean face

\[
x^2+y^2=p^2,
\]

write the Euclid scaling factor as

\[
k=\gcd(x,y).
\]

When this face is extended by

\[
p^2+z^2=d^2,
\]

the resulting cuboid is primitive exactly when

\[
\gcd(x,y,z)=\gcd(k,z)=1.
\]

The old production-family loop canonicalized `(x,y,z)` before discovering that most records were nonprimitive. Num2 carries `k` in the hypotenuse index and evaluates `gcd(k,z)` first.

At `B=2m` this rejects

```text
23,286,679
```

of the

```text
28,754,577
```

glue events before canonical sorting.

## 3. Exact second-face membership gate

Num2 also builds the exact set of Pythagorean leg pairs generated with hypotenuse at most `B`.

After the primitive gate, the base face `x-y` is already integral. The cuboid has a second integral face exactly when at least one of

```text
(x,z)
(y,z)
```

appears in this Pythagorean mate set.

There is no loss from the `hypotenuse <= B` mate-set cutoff: any face diagonal is strictly smaller than the physical space diagonal `d<=B`.

Only records passing this set-membership gate are canonically sorted and then revalidated by direct integer square tests on all three faces.

The workload changes from

```text
num1 full face-mask tests = 5,467,898
num2 validation tests     =       712
```

so the fraction removed is

```text
0.9998697854275994
```

or about `99.987%`.

Likewise canonical sorting is postponed from the old candidate stream to only `712` surviving generation records:

```text
num1 pre-gate candidate glues = 28,754,577
num2 post-gate sorts          =        712
removed fraction              = 0.9999752387246037
```

The candidate-glue stream itself is not yet reduced; that is an available future engineering target if num3 scaling requires it.

## 4. Exact retained stream

At `B=2m` the accelerated kernel records

```text
candidate glues                         28,754,577
early nonprimitive rejects             23,286,679
second-face pair membership lookups    10,935,796
<2-face rejects after primitive gate    5,467,186
post-gate sorts                               712
full face-mask validation tests               712
retained generation records                   712
duplicate records suppressed                  356
distinct canonical two-plus objects           356
```

The duplicate count is expected: each exact-two object is reached through both of its integral faces before canonical object deduplication.

## 5. Incremental shell architecture

A single exact Pythagorean index built to a ceiling `B_max` can feed disjoint physical-height shells

\[
B_0<d\le B_1.
\]

Num2 validates the decomposition

```text
(0,200000]
(200000,500000]
(500000,1000000]
(1000000,2000000]
```

and the union of the four shell ledgers is exactly the full `B=2m` ledger.

This establishes the architecture needed by num3 to append new `d` shells rather than changing the population definition at every new cutoff. The current Python prototype still constructs the ceiling index in memory; persistent/on-disk index reuse is an engineering option, not a mathematical requirement of this stage.

## 6. Deterministic chunk architecture

Generation events are partitioned by the shared face hypotenuse

```text
p mod 8.
```

The union of all eight chunk object sets reproduces the complete ledger exactly. An object may appear in more than one chunk before canonical dedup because its two integral faces can have different shared hypotenuses; global canonical dedup is therefore part of the chunk contract.

```text
PARALLEL_CHUNK_REPRODUCIBILITY=true
```

means that deterministic chunk union reproduces the exact ledger, not that the current CI launches eight memory-heavy workers simultaneously.

## 7. Resource profile

Reference GitHub Actions run, Ubuntu 24.04 / CPython 3.12.13:

```text
index build (Python timer)   10.0704 s
optimized kernel             12.2379 s
Python total                 22.3083 s
/usr/bin/time wall           25.76 s
user CPU                     24.84 s
system CPU                    0.88 s
max RSS                 2,035,840 KiB  (~1.94 GiB)
```

For context, num1's combined independent two-route audit measured `107.63 s` wall and `1,637,680 KiB` RSS on a comparable GitHub runner.

That is **not** an apples-to-apples production-kernel speedup ratio: num1 intentionally ran two independent generation routes, whereas num2 runs one accelerated production kernel and validates it against frozen hashes. The stable acceleration evidence is the exact removal of millions of sorts/face-square tests. The wall-time drop is a useful engineering observation only.

The memory increase is real and intentional: num2 purchases speed with an exact in-memory Pythagorean mate-pair set. Num3 must monitor whether this remains acceptable at larger ceilings.

## 8. Frozen boundary

```text
STAGE14_NUM2=COMPLETE_EXACT_ENUMERATOR_ACCELERATION
BASELINE_LEDGER_UNCHANGED=true
ALL_11_FROZEN_CUTOFFS_UNCHANGED=true
INCREMENTAL_CUTOFF_ARCHITECTURE=true
PARALLEL_CHUNK_REPRODUCIBILITY=true
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
SQRT_B_ASYMPTOTIC_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT=Stage14-num3 extended exact census
```

Canonical artifacts:

```text
stages/stage14/14-num2/result.md
stages/stage14/scripts/14-num2/accelerated_enumerator.py
stages/stage14/data/14-num2/benchmark_before.json
stages/stage14/data/14-num2/benchmark_after.json
.github/workflows/stage14-num2-accelerated-enumerator.yml
```
