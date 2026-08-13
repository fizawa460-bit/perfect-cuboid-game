# A logarithmic local product is not a fixed-power saving

```yaml
ID: TB-WARNING-logarithmic-local-product-not-fixed-power
TYPE: WARNING
STATUS: CURRENT
TITLE: A logarithmic local product is not a fixed-power saving
SCOPE: BOTH
SOURCE_STAGE: Stage15-6ea
SOURCE_PR: 885
SOURCE_MERGE_SHA: 7fb9837c624b916b885ee6716724d01549a67306
SOURCE_FILES:
  - stages/stage15/15-6dy/result.md
  - stages/stage15/15-6ea/result.md
```

## INPUT

- A primewise sieve whose exact acceptance factors satisfy
  [
  1-ho_p=rac{c}{p}+O(p^{-2})
  ]
  on a positive-density prime set, with fixed (c>0).
- One complete local condition per distinct prime; higher powers (p^r) do not supply independent copies of the same rejection.

## OUTPUT

The prime tensor has logarithmic scale:
[
prod_{ple z}ho_p=(log z)^{-C+o(1)}
]
for the corresponding progression/density constant (C>0).

Consequently, even a hypothetical effective theorem uniform through (z=B^	heta) yields only a logarithmic saving in (B), not (B^{-delta}) for any fixed (delta>0).

For Stage15-6, (1-ho_p=4/p+O(p^{-2})) over split primes (pequiv1pmod4), giving the natural scale
[
prod_{substack{ple z\pequiv1(4)}}ho_p
=(log z)^{-2+o(1)}.
]

## VARIABLE DICTIONARY

- (ho_p) = exact local acceptance factor.
- (z) = terminal prime of the finite sieve block.
- (delta) = proposed fixed polynomial-saving exponent.
- (C) = accumulated logarithmic sieve exponent after accounting for the prime set density.

## USED BY

- Early capability tests for local squareclass, valuation-parity, and fixed-prime overlap sieves.
- Negative certificates separating qualitative zero density from polynomial thinning.
- Decisions about whether a growing-modulus theorem could improve only effectiveness or could change the saving species.

## DO NOT USE FOR

- Do not conclude that every global or correlation method is incapable of a fixed-power saving.
- Do not infer a quantitative ((log B)^{-C}) bound without uniformity in the growing prime block.
- Do not count (p,p^2,p^3,ldots) as independent rejection events when the p-adic density already integrates all valuation levels.
- Do not confuse (prodho_p	o0) with polynomial decay.

## PROVENANCE NOTES

- Stage15-6ea is a mechanism-specific negative certificate: the local parity tensor cannot yield fixed power, while genuinely global correlation or reconstruction mechanisms remain logically different species.
