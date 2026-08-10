# Stage14-4dH literature / theorem applicability matrix

This file records the primary-source theorem families checked against the exact merged-4dc receiver, including the newly merged q10 radar candidates.

## Exact target

```text
sum_C I_C^phys << B^(1/2-delta+o(1)), delta>0,
```

uniformly on

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
C0 | P^2+Q^2,
P*Q<=B^(1/2+o(1)),
```

with every physical factorization, squarefree-cell, interval, sign/orientation and reciprocal-completion mask retained.

The central obstruction is that the receiver is a positive total mass with an unsaved zero-frequency/main-density term.

## Bettin--Chandee

S. Bettin, V. Chandee, *Trilinear forms with Kloosterman fractions*, arXiv:1502.00769.
https://arxiv.org/abs/1502.00769

Controls oscillatory inverse-fraction sums with arbitrary coefficients.

```text
DIRECTLY_APPLICABLE=false
```

No inverse-fraction kernel with removed zero mode is present in 4dc.

## Dong--Robles--Zeindler 2026

A. Dong, N. Robles, D. Zeindler, *Bilinear forms with Kloosterman fractions and applications*, arXiv:2601.00292.
https://arxiv.org/abs/2601.00292

Improves bilinear Kloosterman-fraction cancellation for arbitrary coefficient sequences.

```text
DIRECTLY_APPLICABLE=false
```

The 4dc physical selector is positive and no inverse-fraction Fourier adapter with a controlled main term has been derived.

## Wright 2026

T. Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177.
https://arxiv.org/abs/2604.25177

Refines the partially fixed denominator regime and dispersion applications; its distribution results require coefficient-distribution hypotheses such as Siegel--Walfisz behavior.

```text
DIRECTLY_APPLICABLE=false
SIEGEL_WALFISZ_PHYSICAL_WEIGHT_PROVED=false
ZERO_FREQUENCY_REMOVED=false
```

## Blomer--Pascadi 2026

V. Blomer, A. Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311.
https://arxiv.org/abs/2607.24311

The abstract gives a `c^(-1/32)` saving in the critical range where summation length is the square root of the modulus.

```text
DIRECTLY_APPLICABLE=false
COMPLETE_KLOOSTERMAN_KERNEL_DERIVED=false
```

The exact receiver has a norm congruence with a positive physical selector, not a completed Kloosterman bilinear form with its main term removed.

## Baier--Bansal Gaussian sparse large sieve

S. Baier, A. Bansal, *Large sieve with sparse sets of moduli for Z[i]*, arXiv:1811.07300.
https://arxiv.org/abs/1811.07300

```text
DIRECTLY_APPLICABLE=false
MEAN_ZERO_GAUSSIAN_COEFFICIENT_SEQUENCE_PROVED=false
```

A Gaussian interpretation of `C0|P^2+Q^2` exists, but no mean-zero `L^2` physical coefficient family removes the positive average.

## Baier 2026 modular-square-root energy

S. Baier, *On certain bilinear sums with modular square roots and applications*, arXiv:2601.15448.
https://arxiv.org/abs/2601.15448

S. Baier, *A note on bilinear sums with modular square roots*, arXiv:2605.01635.
https://arxiv.org/abs/2605.01635

These papers develop additive-energy / bilinear exponential-sum bounds involving modular square roots, with the latter treating phases built from a modular square root over prime fields.

Merged q10 marks this family as a secondary transfer candidate.

```text
DIRECTLY_APPLICABLE=false
```

The 4dc target averages positive incidences over composite rational common cores and a divisor-split physical selector. It is not a prime-modulus modular-square-root bilinear exponential sum, and no transform preserving all physical masks and removing the zero mode is known.

## Reuss 2015 — q10 high-priority transfer test

T. Reuss, *Counting points on bilinear and trilinear hypersurfaces*, arXiv:1502.07594.
https://arxiv.org/abs/1502.07594

Reuss proves bounds for irreducible bilinear forms on `P^1 x P^1`, improving with the absolute determinant, and for irreducible nonsingular trilinear forms on `(P^1)^3`, improving with the Cayley hyperdeterminant.

The exact transfer test is therefore:

```text
Does reciprocal completion eliminate to an irreducible bilinear/trilinear form
with a fresh fixed-power determinant/hyperdeterminant?
```

4dH answer:

```text
REUSS_TRANSFER_TESTED=true
IRREDUCIBLE_BILINEAR_ELIMINANT_EXHIBITED=false
NONSINGULAR_TRILINEAR_ELIMINANT_EXHIBITED=false
FRESH_FIXED_POWER_DETERMINANT_EXHIBITED=false
DIRECTLY_APPLICABLE=false
```

The universal relation remains only `P^2+Q^2=C0R`. The rational cross determinant/sum with the endpoint line are coprime to `C0` by merged 4dc's resultant-4 theorem, and cross norms divisible by `C0` are algebraic consequences of already charged root equations. Hence q10's hoped-for fresh determinant is not exposed.

## Quadratic-root equidistribution

E. Musicantov, S. Zehavi, *Sectorial equidistribution of the roots of x^2+1 modulo primes*, arXiv:2112.07494.
https://arxiv.org/abs/2112.07494

H. T. Ngo, *On roots of quadratic congruences*, arXiv:2107.13301.
https://arxiv.org/abs/2107.13301

```text
DIRECT_TOTAL_MASS_POWER_SAVING_APPLICABLE=false
```

Root equidistribution controls discrepancy, while 4dc already pays only `B^o(1)` root-choice entropy. It does not prove that the physical selector has power-small average density.

## Generic determinant method

T. D. Browning, D. R. Heath-Brown, *Counting rational points on hypersurfaces*, arXiv:math/0404456.
https://arxiv.org/abs/math/0404456

T. D. Browning, D. R. Heath-Brown, P. Salberger, *Counting rational points on algebraic varieties*, arXiv:math/0410117.
https://arxiv.org/abs/math/0410117

The ambient relation

```text
P^2+Q^2=C0R
```

has the Gaussian multiplication parametrization

```text
C0=c1^2+c2^2,
R=r1^2+r2^2,
P=c1*r1-c2*r2,
Q=c1*r2+c2*r1.
```

So the norm surface itself contains abundant integral families. The physical filters are not yet an additional fixed-degree irreducible algebraic equation.

```text
GENERIC_NORM_SURFACE_DIRECTLY_APPLICABLE_FOR_FIXED_POWER_SAVING=false
```

## Final applicability matrix

```text
BETTIN_CHANDEE=false
DONG_ROBLES_ZEINDLER_2026=false
WRIGHT_PARTIALLY_FIXED=false
BLOMER_PASCADI_2026=false
GAUSSIAN_SPARSE_LARGE_SIEVE=false
BAIER_2026_MODULAR_SQRT_ENERGY=false
REUSS_BILINEAR_TRILINEAR_TRANSFER=false
QUADRATIC_ROOT_EQUIDISTRIBUTION_TOTAL_MASS=false
GENERIC_DETERMINANT_METHOD_NORM_SURFACE=false
```

The common missing input is an exact fixed-power upper-density theorem for the physical divisor-split completion weight, or an equivalent transformation that proves its zero-frequency/main term is power-small before invoking cancellation machinery.
