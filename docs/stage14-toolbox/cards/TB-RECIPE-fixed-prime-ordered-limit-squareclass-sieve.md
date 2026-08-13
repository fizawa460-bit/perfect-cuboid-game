# Same-measure fixed-prime ordered-limit squareclass sieve

```yaml
ID: TB-RECIPE-fixed-prime-ordered-limit-squareclass-sieve
TYPE: RECIPE
STATUS: CURRENT
TITLE: Same-measure fixed-prime ordered-limit squareclass sieve
SCOPE: BOTH
SOURCE_STAGE: Stage15-6ea
SOURCE_PR: 885
SOURCE_MERGE_SHA: 7fb9837c624b916b885ee6716724d01549a67306
SOURCE_FILES:
  - stages/stage15/15-6dy/result.md
  - stages/stage15/15-6dz/result.md
  - stages/stage15/15-6ea/result.md
```

## INPUT

- A physical counting population (P(B)) and survivor population (Q(B)subseteq P(B)) with exactly matching cutoff, primitive/canonical conventions, orientation, masks, and charged measure.
- For every fixed finite set (S) of good primes, a congruence-refined asymptotic on that same physical population.
- A pointwise necessary local survivor condition at each (pin S), with exact acceptance density (ho_p).
- CRT compatibility for fixed (S), and an explicit proof that local labels, reconstruction fibers, and completion factors are charged once.
- The limit order (B	oinfty) for fixed (S), followed only afterward by expansion of (S).

## OUTPUT

For each fixed finite (S),
[
limsup_{B	oinfty}rac{#Q(B)}{#P(B)}
le prod_{pin S}ho_p.
]
If an increasing sequence (S_z) satisfies
[
prod_{pin S_z}ho_p	o0,
]
then
[
rac{#Q(B)}{#P(B)}	o0.
]

In the Stage15-6 application, good split primes (pequiv1pmod4) have
[
ho_p=
rac{p^4+4p^3+22p^2+4p+1}
{(p+1)^2(p^2+6p+1)},
qquad
1-ho_p=rac4p+O(p^{-2}),
]
while inert primes have (ho_p=1). This proves (N_2(B)/M_2(B)	o0) independently of the imported Stage14 half-power bound.

## VARIABLE DICTIONARY

- (P(B)) = ambient physical population under the declared cutoff.
- (Q(B)) = subpopulation satisfying the additional squareclass/survivor condition.
- (S) = one fixed finite set of good primes.
- (ho_p) = exact same-measure local acceptance probability at (p).
- (M_2(B)) = Stage15 ambient primitive canonical exactly-two population.
- (N_2(B)) = its integral-space-diagonal survivor population.

## USED BY

- Squareclass, valuation-parity, and local-overlap problems where every survivor obeys a pointwise local condition.
- Future stages that can prove fixed-modulus equidistribution on their own physical measure.
- Qualitative zero-density proofs that do not require a modulus growing with (B).

## DO NOT USE FOR

- Do not import the displayed Stage15 (ho_p) into a different population.
- Do not replace a physical pair/incidence measure by a scalar host without a measure-preserving adapter.
- Do not let (S) or its modulus grow with (B) unless a uniform theorem is separately proved.
- Do not infer a fixed-power saving merely because the ordered product tends to zero.
- Do not count reconstruction, core, root, or completion multiplicities twice.

## PROVENANCE NOTES

- The proof architecture descends from the Stage14-e fixed-prime local-sieve design, but Stage15-6dy/dz recomputed the local law and proved the fixed-set asymptotic on the Stage15 physical measure.
- Stage15-6ea completed the ordered-limit argument and isolated its exact quantitative boundary.
