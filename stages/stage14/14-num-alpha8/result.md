# Stage14-num-α8 — exact segmented alpha scaleout beyond B150m

> STATUS: `STAGE14_NUM_ALPHA8=COMPLETE_EXACT_B200M_ALPHA_SCALEOUT`
>
> CLASSIFICATION: finite exact census / production-scale numerical extension; no asymptotic claim.

## Result

Dedicated Actions run `31314521041` completed successfully. The body-diagonal range `1 <= d <= 200,000,000` was split into eight disjoint 25m shards and enumerated through the alpha diagonal-first engine.

The mandatory `d<=150,000,000` regression reproduced merged Stage14-num6 in every frozen field, including all object/mask/vertex/edge SHA locks.

Exact B200m census:

```text
(N_a^(2),N_b^(2),N_c^(2)) = (957,967,533)
N2 = 2457
T = 0
active oriented faces = 3563
raw pair edges = 2457
max graph degree = 11
object SHA = 79f38bc8841ee43505598d07f3b7cbed1fe4127243a3ae58c83e686267ce65ae
object+mask SHA = 048ea27298801dcdb0baea3ac143f011de34b68ba658deb36ebdb37d3e5faeab
vertex SHA = 8a6e151c6eb98f0e23c15715b3968f2fbfc304429836b87fdc69f9af9aa35001
edge SHA = 0d3c4320c530faebba8b157b20473c58f3cc6ff3984ec41cce3eb3c93578ea75
```

The new shell `150m < d <= 200m` contributes exactly:

```text
(+98,+75,+71), total +244, triple +0.
```

The finite diagnostic `N2/sqrt(B)` is `0.17373613613753472`, down about 3.85% from the B150m value `0.18069069335930577`. This remains diagnostic only.

## Production architecture

Each shard performs segmented exact factorization of odd diagonals, removes primitive-impossible `3 mod 4` prime support, requires at least two positive nontrivial representations of `d^2`, synthesizes split-prime representations by Cornacchia, generates Gaussian/Girard representations, and applies the alpha4 compressed collision plus alpha5 primitive-safe pair filters.

Since every representation collision is internal to one fixed body diagonal `d`, the shard union is mathematically exact and no cross-shard collision step is needed.

The exact B200m manifest is frozen at `stages/stage14/data/14-num-alpha8/b200m_manifest.json`. The source Actions artifact contains the 2457-row compressed object source.

## Boundary

This is a finite exhaustive census through B200m. `T=0` through this cutoff is not a proof of perfect-cuboid nonexistence. No asymptotic runtime or counting-law claim is made.

```text
SEGMENTED_DIAGONAL_SHARDS_EXACT_DISJOINT_UNION=true
B150M_NUM6_FULL_HASH_REGRESSION_MATCH=true
B200M_EXACT_CENSUS_FROZEN=true
EXTENDS_BEYOND_ORDINARY_B150M_CUTOFF=true
PERFECT_CUBOID_EMERGENCY=false
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
NEXT=Stage14-num-alpha9 optional historical-interval validation / alpha10+ only on demonstrated value
```
