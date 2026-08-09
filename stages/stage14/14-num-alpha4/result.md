# Stage14-num-α4 — exact compressed collision engine

> STATUS: `STAGE14_NUM_ALPHA4=COMPLETE_EXACT_COMPRESSED_COLLISION_ENGINE`
>
> CLASSIFICATION: exact finite-enumeration engineering audit; no asymptotic claim.

## Goal

Replace the α2 ordered-role pair brute force by an algebraically compressed collision kernel without losing any primitive Stage14 object having at least two integral face diagonals.

## Exact positive-role compression

Take two distinct unordered positive representations of the same body-diagonal square and order them as

```text
d^2 = A^2 + F^2 = B^2 + E^2,
A < B.
```

Because both lie on the same quarter circle, necessarily `F>E`. The four cross-role choices from α2 have residuals

```text
edge roles (A,B):  c^2 = E^2-A^2
edge roles (A,E):  c^2 = B^2-A^2
edge roles (F,B):  c^2 = A^2-B^2 < 0
edge roles (F,E):  c^2 = A^2-E^2
```

Therefore the third branch is impossible, and the fourth exists only when `A>E`. Every positive α2 ordered-role residual is exactly one of at most three displayed differences. This is an identity, not a heuristic pruning rule.

The α4 kernel enumerates those positive differences, tests them for being squares, reconstructs the edge triple, applies the ordinary primitive/canonical gate, recomputes the full face mask, and deduplicates by the ordinary Stage14 object record.

## Safe square-residue prefilter

Before calling `isqrt`, α4 requires the residual to be a quadratic residue modulo both 64 and 63. Every integer square satisfies these conditions, so this can reject work but cannot reject a true collision.

No perfect-cuboid-only congruence condition (including the historical mod-11/mod-19 cuts) is used.

## Exact B=200,000 collision comparison

Dedicated Actions run `31312605661` compared the α2-style ordered-role reference and α4 compressed kernel over the same exact α3 Gaussian/Girard representation table.

```text
objects                                  116 / 116 exact set equality
ordered-role pair tests                  3,612,175
compressed representation-pair tests       839,460
positive residuals                       1,678,920 / 1,678,920
reference isqrt tests                    1,678,920
compressed isqrt tests                     602,930
residue-filter rejects                   1,075,990
isqrt reduction                          64.0882%
reference collision seconds              1.402906
compressed collision seconds             1.145176
collision-only speed ratio               1.22506x
square hits                              2,313 / 2,313
```

The speed number is runner-specific engineering data; the exact set equality and integer workload counts are the durable locks.

## Streaming B=2,000,000 regression

The large audit did not materialize the complete representation table. It scanned `d` in increasing order, generated the exact α3 Gaussian/Girard representation set for that `d`, ran the compressed collision kernel, and discarded the representation set before advancing.

The streamed α3+α4 route reproduced the frozen Stage14-num1 census exactly:

```text
N_a^(2)=142
N_b^(2)=134
N_c^(2)=80
N2=356
T=0
active faces=490
raw edges=356
max degree=9
```

All four frozen SHA-256 locks matched exactly:

```text
object key        1869ce6d30b661a3ea53049f2c86ffda5dd3d23b14aa9511301d72b1d4e8a89a
object + mask     84ce4239d482207ef8d961514c06b966f2eb9043fbbd5be3a7aea83d779314ce
active vertices   0c91e088324a703253cf7c100569eb25971135a4481512de1f63aa7657396e5b
raw edges         cd8f0ffa7d26ce38e316b65644bb25d39857b5d074a8bb1b96db2e05e8714a1f
```

B2m streamed workload:

```text
diagonals scanned                       2,000,000
diagonals with nontrivial representation 1,458,419
diagonals with >=2 representations        575,512
representation-pair tests              14,342,740
positive candidate residuals           28,685,480
residue-filter rejects                 17,858,810
isqrt tests                            10,826,670
square hits                                24,249
objects                                       356
runner seconds                              47.292
```

## Interpretation

α4 proves that the collision layer can be compressed without changing the finite census. The modular square prefilter removes about 64% of exact square-root calls in the B200k comparison and the measured collision-only kernel is about 1.23x faster on that runner.

This is encouraging but deliberately not promoted to an end-to-end speedup claim. Factorization, prime sum-of-two-squares construction, outer diagonal scanning and output handling still contribute substantially; the formal crossover decision remains α7.

```text
STAGE14_NUM_ALPHA4=COMPLETE_EXACT_COMPRESSED_COLLISION_ENGINE
COMPRESSED_COLLISION_OBJECT_SET_EQUALS_ORDERED_ROLE_REFERENCE=true
ALGEBRAIC_POSITIVE_ROLE_COMPRESSION_EXACT=true
SQUARE_RESIDUE_PREFILTER_EXACT_NO_FALSE_NEGATIVES=true
STREAMED_GAUSSIAN_COLLISION_B2M_MATCHES_FROZEN_NUM1=true
B2M_FOUR_HASH_LOCKS_MATCH=true
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=false
FINITE_DIAGNOSTIC_ONLY=true
```

## Dependency status

Stage14-num-α2 exact-overlap CI succeeded and is merged. Stage14-num-α3's corrected scaled Gaussian/Girard generator succeeded in Actions run `31312110117` and is merged through PR #283.

## Next

`Stage14-num-α5`: audit and prove safe primitive/diagonal pruning individually, keeping every exactly-two-face object. In particular, distinguish Stage14-safe primitive filters from historical perfect-only shortcuts.
