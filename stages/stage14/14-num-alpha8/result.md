# Stage14-num-α8 — exact segmented alpha scaleout beyond B150m

> STATUS: `STAGE14_NUM_ALPHA8=PENDING_GITHUB_ACTIONS_FINAL_LOCK`
>
> CLASSIFICATION: finite exact census / production-scale numerical extension; no asymptotic claim.

## Goal

Promote the validated alpha engine from an audit/benchmark path into a real exact-census engine and extend the Stage14 two-face-or-more population beyond the ordinary rolling cutoff `B=150,000,000`.

## Production architecture

The body-diagonal domain

```text
1 <= d <= 200,000,000
```

is partitioned into eight disjoint contiguous shards of width 25,000,000. Each shard independently performs:

```text
segmented exact factorization of odd d
-> reject any 3 mod 4 prime support
-> require at least two positive nontrivial representations of d^2
-> Cornacchia sum-of-two-squares prime synthesis
-> Gaussian/Girard representation generation
-> alpha4 compressed collision
-> alpha5 primitive-safe pair filter
-> exact canonical (a,b,c,d,mask) records
```

Because every collision is entirely internal to one fixed body diagonal `d`, the shard union is mathematically exact and requires no cross-shard collision step.

## Regression gate

Before accepting any new B200m result, the union restricted to `d<=150,000,000` must reproduce the merged Stage14-num6 census in all frozen fields:

- directional counts and triple count;
- distinct physical object count;
- object-key SHA;
- object+mask SHA;
- raw-edge and active-face graph counts;
- max degree;
- vertex and edge ledger SHA values.

Only after that full regression passes is `150m < d <= 200m` treated as new exact territory.

## Boundary

This stage extends a finite exact computational census. It does not establish an asymptotic runtime exponent, an asymptotic counting law, or existence/nonexistence of a perfect cuboid.

```text
B150M_NUM6_FULL_HASH_REGRESSION_MATCH=PENDING_ACTIONS
B200M_EXACT_CENSUS_FROZEN=PENDING_ACTIONS
EXTENDS_BEYOND_ORDINARY_B150M_CUTOFF=PENDING_ACTIONS
NEXT_AFTER_SUCCESS=Stage14-num-alpha9 optional historical-interval validation / alpha10+ only on demonstrated value
```
