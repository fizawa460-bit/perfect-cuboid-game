# Stage14-sH71 literature applicability note

Frozen object: `CanonicalAllocationConditionalPrimitiveGaussianRootDensity` from merged Stage14-s7-71.

The audit standard is strict: a source is directly applicable only if it yields a uniform fixed positive `B`-power deficit for the conditional canonical-allocation family while retaining the actual correlation among `C0`, `(X0,Y0)`, the primitive slope, the canonical allocation witness and all physical masks. A result for an unweighted/root-only family is advisory unless a mask-preserving adapter is already proved.

## 1. Duke--Friedlander--Iwaniec root equidistribution and later quadratic-root work

Hieu T. Ngo, *On roots of quadratic congruences*, arXiv:2107.13301.

Primary source: https://arxiv.org/abs/2107.13301

The abstract records that equidistribution of roots of quadratic congruences to prime moduli is driven by Weyl linear forms; it explicitly identifies the Duke--Friedlander--Iwaniec estimate for negative discriminant quadratics and Tóth's corresponding positive-discriminant theory.

Applicability to sH71:

```text
DIRECT=false
```

Reason: the frozen receiver is not the natural root sequence over prime moduli. `C0` may be composite, and more importantly the modulus and root-line test are generated from the same canonical allocation witness as the candidate vector. No source-stage lemma converts the conditional canonical background into the unweighted/smooth modulus family required by the quadratic-root equidistribution theorem.

## 2. Sectorial roots of x^2+1 modulo primes

Evgeny Musicantov and Sa'ar Zehavi, *Sectorial equidistribution of the roots of x^2+1 modulo primes*, arXiv:2112.07494.

Primary source: https://arxiv.org/abs/2112.07494

This is unusually close geometrically. It treats roots of `x^2+1` modulo primes and even preserves an angular restriction on the sum-of-two-squares lattice representative. The paper explains the DFI root/modulus parametrization and uses nonspherical spectral analysis to retain the angular datum.

Applicability to sH71:

```text
DIRECT=false
```

Why it still misses:

- modulus is prime in the main theorem; physical `C0` is an arbitrary split-supported common-core modulus after the frozen peel;
- the angular restriction is a geometric sector, not the canonical balanced integer/Gaussian allocation event with its divisor, squarefree, reciprocal and chart masks;
- the theorem averages the natural root sequence, whereas sH71 conditions on `Omega_can(B)` and then reconstructs `C0,(X0,Y0)` from the same witness;
- even perfect root equidistribution leaves a principal density of order roots(`C0`)/phi(`C0`), which is not a fixed `B`-power if `C0=B^o(1)`.

## 3. Bilinear Weyl sums for modular square roots

Alexander Dunn, Bryce Kerr, Igor E. Shparlinski and Alexandru Zaharescu, *Bilinear forms in Weyl sums for modular square roots and applications*, arXiv:1908.10143.

Primary source: https://arxiv.org/abs/1908.10143

The paper proves a power-saving estimate for a bilinear form involving Weyl sums for modular square roots / Salié sums in a Pólya--Vinogradov range and derives applications to equidistribution of quadratic roots of primes and products of primes.

Applicability to sH71:

```text
DIRECT=false
```

The physical indicator has not been decomposed into separated bilinear coefficient sequences satisfying the theorem's support/range hypotheses. The modulus in the paper's core bilinear setting is prime, whereas `C0` is a candidate-dependent split-supported modulus. The `B^o(1)` candidate fiber is not a second polynomial analytic variable and cannot be promoted to a Type-I/Type-II coefficient family.

## 4. Shifted bilinear Salié sums, 2026

Igor E. Shparlinski and Yixiu Xiao, *Shifted bilinear sums of Salié sums and the distribution of modular square roots of shifted primes*, arXiv:2601.10113.

Primary source: https://arxiv.org/abs/2601.10113

The paper establishes Type-I and Type-II bounds for shifted bilinear sums with Salié sums modulo a large prime `q`, applying them to roots of `x^2 == a p+b (mod q)` over primes `p`.

Applicability to sH71:

```text
DIRECT=false
```

The prime modulus is fixed independently of the prime variable and the coefficient geometry is explicitly Type-I/Type-II. In sH71 the modulus `C0` and candidate vector are reconstructed from the same canonical allocation witness; no separated coefficient package or prime-variable reduction is available.

## 5. Recent modular-square-root large-sieve developments

Recent work by Stephan Baier develops bilinear/additive-energy estimates for modular square roots and large-sieve questions for square or prime-square moduli. One March 2026 installment, arXiv:2603.25814, was later withdrawn and merged into/superseded by arXiv:2605.01635; it is therefore not used as a theorem source for this audit.

Relevant current primary source:

- Stephan Baier, *A note on bilinear sums with modular square roots*, arXiv:2605.01635, https://arxiv.org/abs/2605.01635

These results reinforce that power cancellation is available for structured bilinear modular-square-root families, but they do not provide the missing canonical-allocation conditioning adapter.

```text
DIRECT=false
```

## 6. Principal-density obstruction precedes discrepancy technology

For a prime `p==1 mod 4`, the primitive unit-pair root condition

```text
X^2+Y^2 == 0 (mod p)
```

has exactly two slope classes and density `2/(p-1)` among unit pairs. For squarefree split-supported `C0`, the analogous model density is `2^omega(C0)/phi(C0)`.

Therefore:

```text
C0=B^o(1)
```

implies only a `B^(-o(1))` principal root-line density in general. No cancellation theorem for the centered discrepancy can by itself convert that principal term into a fixed `B`-power loss.

The frozen source supplies no lower bound

```text
C0 >= B^theta
```

with fixed `theta>0` on every physical packet. This is a theorem-level obstruction independent of the finer spectral/large-sieve packaging question.

## 7. Exact missing adapter

The closest useful future theorem input is not another raw root-equidistribution result. First the parent route must prove a scale-stratified, mask-preserving decomposition of the canonical background:

```text
principal local root-line density
+
centered discrepancy of canonical allocation candidates modulo C0.
```

For polynomial `C0`, the centered term could then potentially be passed to quadratic-root large-sieve / spectral / bilinear technology. For subpolynomial `C0`, root spacing alone cannot be the fixed-power saving source.

```text
CANONICAL_BACKGROUND_PSEUDORANDOMNESS_ADAPTER_PROVED=false
DIRECT_GAUSSIAN_ROOT_EQUIDISTRIBUTION_THEOREM_APPLICABLE=false
ROOT_LARGE_SIEVE_DIRECTLY_APPLICABLE=false
BILINEAR_ROOT_DISPERSION_DIRECTLY_APPLICABLE=false
DIVISOR_CORRELATED_NORM_FORM_SIEVE_DIRECTLY_APPLICABLE=false
```
