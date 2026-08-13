# Stage14-num-α3 — sum-of-two-squares representation generation audit

> STATUS: `STAGE14_NUM_ALPHA3=PENDING_DEPENDENT_CI`
>
> DEPENDS_ON: Stage14-num-α2 exact-overlap PR #281 and its dedicated Actions success.

## Goal

Compare complete ways to generate `Rep(d^2) = {(u,v): u^2+v^2=d^2}` without changing the α1/α2 census semantics.

## Compared generators

1. `EUCLID_SCALED_REFERENCE`: generate primitive Pythagorean triples and all scales, then group by space diagonal `d`.
2. `GAUSSIAN_FACTOR_SYNTHESIS`: factor eligible `d`, represent each `p≡1 (mod4)` as a Gaussian prime `π`, and enumerate all distributions `π^k conjugate(π)^(2e-k)` for each `p^e || d`; multiply and deduplicate absolute coordinate pairs.

For α3 the prime representation step deliberately uses a simple deterministic square search rather than Cornacchia. That keeps the audit transparent. Cornacchia/segmentation belongs to a later optimization only after exact equality is locked.

## Exact acceptance gate

At `B=200,000`, the workflow requires equality of the complete representation set for every diagonal, not just equal counts:

```text
REPRESENTATION_KEYSETS_EQUAL=true
```

Any single missing or extra `{u,v}` pair fails the stage.

## Interpretation

The Gaussian/Girard route is the historical-style candidate for large diagonal-first search because representation generation cost is tied to factorization and the small representation count of each eligible `d`, rather than materializing every scaled Pythagorean triple globally.

However α3 does **not** claim an end-to-end Stage14 speedup. Even if representation generation is faster, factorization, collision work, canonicalization and memory may dominate. End-to-end performance remains for α7.

## Dependency boundary

PR #281 is still the authority for proving that the α collision engine reproduces the ordinary Stage14 `N2/T` census. α3 may compare representation generators while #281 is queued, but α3 cannot be promoted to a trusted engine component unless α2 passes.

```text
ALPHA2_CI_DEPENDENCY_REQUIRED=true
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=false
NEXT_AFTER_SUCCESS=Stage14-num-alpha4 collision-engine integration
```
