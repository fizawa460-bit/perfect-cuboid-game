# Stage14-tH22 literature applicability note — through merged t79

Target:

```text
CanonicalGaussianPrimeProjectiveRayCharacterBalancedCoverBilinearLargeSieve
```

No external source below is imported as a proof of the Stage14 receiver.  Merged t78 and t79 already remove two internal issues before literature is tested:

1. t78 proves exact four-cell Möbius tensorization and rewrites the strongest hyperbola as `ell*H*R*T<2B`;
2. t79 removes the principal character, endpoint-small ray groups, and every nonprincipal character with fixed-power inactive-support deficit.

Thus the hard family is

```text
M=B^(positive power+o(1)),
d_chi=M/B^o(1),
N f_fin(chi)=M^2 B^o(1),
```

with the balanced primitive-cover and physical masks retained.

## 1. Actual projective conductor

A projective character is trivial on rational scalars.  After a two-parity split according to `chi(i)=+/-1`, it embeds into standard Hecke-character language over `Q(i)`; the odd parity is corrected by one fixed infinity type.

For every nontrivial local projective factor at `p|M`, both inert and split cases require the full rational ideal `(p)`.  Hence

```text
f_fin(chi)=(d_chi),
N f_fin(chi)=d_chi^2.
```

The key mismatch is therefore

```text
projective family size: M*B^o(1),
hard Hecke conductor norm: M^2*B^o(1).
```

## 2. Huxley-type ambient large sieve

Huxley's algebraic-number-field large sieve is the correct ambient paradigm: modulus/conductor ideals are the arithmetic scale.

It does not by itself exploit a projective subfamily of cardinality only `~M` inside conductor norm `~M^2`, nor does it supply the t78 divisor-decomposed `pi x V` coefficient moments with the Stage14 masks.

Verdict: relevant ambient technology, not a direct adapter.

## 3. Han Wu — GL1 conductor-aspect subconvexity

Han Wu, *Burgess-like subconvexity for GL1* (arXiv:1604.08551; Compositio Math. 155 (2019)).

This gives genuine conductor-aspect subconvexity for Hecke characters over a fixed number field.  It confirms that an identified Hecke conductor can lead to short character-sum cancellation.

It is not a projective-subfamily hybrid large sieve and does not directly control the Stage14 divisor-decomposed Gaussian-prime/cover correlation.

## 4. Likun Xie — ray-class short sums

Likun Xie, *Products of prime ideals in ray class groups* (arXiv:2606.30567, 2026), formulates ray-class character input with

```text
Q=N(q)
```

as the ideal modulus/conductor norm scale and records the Wu-based short-sum exponent `103/256`.

For the t79 hard projective family this standard scale is

```text
Q=d_chi^2=M^2 B^o(1).
```

The raw cover length remains promising in portions of the deficient range, but Xie's sequence is an ordinary ray-class/ideal sequence, not the Stage14 balanced primitive four-cell divisor sequence with the short ellipse and hyperbolas.

## 5. Gaussian / number-field Bombieri–Vinogradov

Tanmay Khale, Cooper O'Kuhn, Apoorva Panidapu, Alec Sun, Shengtong Zhang, *A Bombieri-Vinogradov Theorem for primes in short intervals and small sectors* (arXiv:2008.09677).

Yujiao Jiang, Guangshi Lü, Jesse Thorner, Zihao Wang, *A Bombieri-Vinogradov theorem for higher rank groups* (arXiv:2104.02711).

These works demonstrate that Hecke/sector restrictions can coexist with strong averaged distribution over arithmetic moduli.  The Stage14 quantifier order is different: after packet conditioning there is no broad free `M` average, the hard conductor is near maximal `M^2`, and the canonical Gaussian prime remains coupled to the short cover masks.

Verdict: no uniform full-range adapter.

## 6. Structured Hecke-character large sieves

Leo Goldmakher and Benoit Louvel, *A quadratic large sieve inequality over number fields* (arXiv:1112.1642), gives a strong large sieve for structured bounded-order Hecke families.

The t77/t79 projective local character order can divide `p-chi_4(p)` and is not a quadratic family. Restricting to quadratic characters would not reproduce the projective class indicator.

## 7. Refined literature conclusion after t79

The external theorem no longer needs to solve angular-gcd tensorization, principal density, endpoint-small character enumeration, or support-deficient characters.

It would need to prove a **near-full-support, near-maximal-conductor** hybrid estimate exploiting projective family compression:

```text
MINIMAL_REMAINING_OBSTRUCTION=NearFullSupportProjectiveConductorCompressedGaussianPrimeFourCellMobiusCoverHybridLargeSieve
```

Required simultaneous ingredients:

1. exploit only `M*B^o(1)` projective characters despite conductor norm `M^2 B^o(1)`;
2. moving canonical Gaussian-prime character moments;
3. t78 four-cell Möbius/divisor-decomposed cover coefficients with uniform `L2` control;
4. balanced primitive cover and the `ell*H*R*T`, short ellipse, and `ell*delta` masks.

No located off-the-shelf theorem supplies all four.

```text
OFF_THE_SHELF_RAY_CHARACTER_POWER_SAVING_PROVED=false
CERTIFIED_RAY_CHARACTER_B_POWER_SAVING_EXPONENT=0
```
