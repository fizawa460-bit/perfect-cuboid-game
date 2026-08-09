# Stage14-num-α4 — exact compressed collision engine

> STATUS: `STAGE14_NUM_ALPHA4=PENDING_GITHUB_ACTIONS_FINAL_LOCK`
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

## Streaming integration

The large audit does not materialize the complete representation table. It scans `d` in increasing order, generates the exact α3 Gaussian/Girard representation set for that single `d`, runs the compressed collision kernel, and discards the representation set before advancing. This tests the intended memory-light architecture rather than only a table-to-table toy comparison.

## Acceptance gates

At `B=200,000`:

```text
COMPRESSED_COLLISION_OBJECT_SET_EQUALS_ORDERED_ROLE_REFERENCE=true
```

At the frozen `B=2,000,000` cutoff the streamed α3+α4 path must reproduce:

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

and all four frozen SHA-256 locks for object keys, object+mask keys, active-face vertices and raw-pair edges.

## Performance boundary

α4 records role-pair counts, compressed residual counts, residue-filter rejection counts, `isqrt` counts and collision-only timing. These are engineering measurements only.

Even a favorable α4 collision ratio is **not** yet the end-to-end α speedup claim. Factorization, prime sum-of-two-squares construction, outer diagonal scanning and output handling still contribute. The formal crossover decision remains α7.

```text
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=false
```

## Dependency status

Stage14-num-α2 exact-overlap CI succeeded and is merged. Stage14-num-α3's corrected scaled Gaussian/Girard generator also succeeded in Actions run `31312110117` and is merged through PR #283.

## Next after success

`Stage14-num-α5`: audit and prove safe primitive/diagonal pruning individually, keeping every exactly-two-face object. In particular, distinguish Stage14-safe primitive filters from historical perfect-only shortcuts.
