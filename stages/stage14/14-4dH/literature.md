# Stage14-4dH literature / theorem applicability matrix

This file records the primary-source theorem families checked against the exact 4dc receiver. The verdicts are strict applicability verdicts, not judgments about the strength of the papers themselves.

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

with all physical factorization / squarefree-cell / interval / sign / reciprocal-completion masks retained.

The key obstruction is that the target is a **positive total mass**, while the strongest available analytic inputs are cancellation/discrepancy theorems after subtraction of a main term or introduction of a nonzero oscillatory phase.

## 1. Bettin--Chandee

S. Bettin, V. Chandee, *Trilinear forms with Kloosterman fractions*, arXiv:1502.00769.

Primary source:
https://arxiv.org/abs/1502.00769

The theorem controls sums with phases of the form

```text
e(theta * a * inverse(m) / n)
```

and arbitrary coefficient sequences. It gives genuine power cancellation in balanced regimes.

4dH verdict:

```text
DIRECTLY_APPLICABLE=false
```

Reason: 4dc has no derived nonzero inverse-fraction phase. Fourier completion of the root-line congruence produces a zero-frequency term equal to the unsaved physical density. Bettin--Chandee can only become relevant after an exact adapter removes or power-saves that zero mode.

## 2. Dong--Robles--Zeindler

A. Dong, N. Robles, D. Zeindler, *Bilinear forms with Kloosterman fractions and applications*, arXiv:2601.00292.

Primary source:
https://arxiv.org/abs/2601.00292

The paper improves bilinear Kloosterman-fraction bounds for arbitrary complex coefficient sequences.

4dH verdict:

```text
DIRECTLY_APPLICABLE=false
```

Reason: same structural mismatch as Bettin--Chandee. The exact receiver is a positive incidence count and no inverse-fraction oscillatory representation with zero mode removed has been proved.

## 3. Wright partially-fixed denominator refinement

T. Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177.

Primary source:
https://arxiv.org/abs/2604.25177

The paper refines Bettin--Chandee when a denominator factor is fixed and develops dispersion applications. Its distribution results require additional coefficient-distribution hypotheses such as Siegel--Walfisz behavior in the relevant sequence.

4dH verdict:

```text
DIRECTLY_APPLICABLE=false
SIEGEL_WALFISZ_PHYSICAL_WEIGHT_PROVED=false
ZERO_FREQUENCY_REMOVED=false
```

The physical admissibility weight in 4dc has not been shown to satisfy the required distribution hypothesis, and the positive zero-frequency density remains the main term.

## 4. Blomer--Pascadi 2026 complete-Kloosterman bilinear bound

V. Blomer, A. Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311.

Primary source:
https://arxiv.org/abs/2607.24311

The abstract states a saving `c^(-1/32)` over the trivial bound in the critical range where the summation length is the square root of the modulus, valid for all moduli.

4dH verdict:

```text
DIRECTLY_APPLICABLE=false
COMPLETE_KLOOSTERMAN_KERNEL_DERIVED=false
```

This is the closest modern power-saving theorem in scale, but 4dc has not produced a bilinear form in complete Kloosterman sums. The receiver consists of the norm congruence `C0|P^2+Q^2` with a positive arithmetic physical selector. An invented completion would still retain its zero-frequency/main-density contribution.

## 5. Gaussian sparse-modulus large sieve

S. Baier, A. Bansal, *Large sieve with sparse sets of moduli for Z[i]*, arXiv:1811.07300.

Primary source:
https://arxiv.org/abs/1811.07300

The paper proves large-sieve inequalities over Gaussian integers for suitable sparse sets of Gaussian moduli, including square moduli and Gaussian primes.

4dH verdict:

```text
DIRECTLY_APPLICABLE=false
MEAN_ZERO_GAUSSIAN_COEFFICIENT_SEQUENCE_PROVED=false
```

The 4dc root-line can be interpreted through a Gaussian divisor of `P+iQ`, but the required physical weight is nonnegative and no mean-zero / `L^2` coefficient formulation has been obtained which removes the ambient average. The large sieve can control dispersion, not the unknown positive average density itself.

## 6. Roots of x^2+1 / quadratic-root equidistribution

E. Musicantov, S. Zehavi, *Sectorial equidistribution of the roots of x^2 + 1 modulo primes*, arXiv:2112.07494.

Primary source:
https://arxiv.org/abs/2112.07494

The paper extends the equidistribution theory for roots of `x^2+1` modulo primes to a sectorially restricted subsequence.

Related general quadratic-root literature checked includes H. T. Ngo, *On roots of quadratic congruences*, arXiv:2107.13301.

Primary source:
https://arxiv.org/abs/2107.13301

4dH verdict:

```text
DIRECT_TOTAL_MASS_POWER_SAVING_APPLICABLE=false
```

These results concern distribution/discrepancy of roots. The 4dc proof already pays only `B^o(1)` for local root choices. Equidistribution does not reduce the total positive number of root-line points unless the physical selector is first shown to have a power-small average density or a mean-zero correlation.

## 7. Determinant method

T. D. Browning, D. R. Heath-Brown, *Counting rational points on hypersurfaces*, arXiv:math/0404456.

Primary source:
https://arxiv.org/abs/math/0404456

T. D. Browning, D. R. Heath-Brown, P. Salberger, *Counting rational points on algebraic varieties*, arXiv:math/0410117.

Primary source:
https://arxiv.org/abs/math/0410117

4dH verdict:

```text
GENERIC_NORM_SURFACE_DIRECTLY_APPLICABLE_FOR_FIXED_POWER_SAVING=false
```

The only universal algebraic relation currently exposed is

```text
P^2+Q^2=C0*R.
```

It has the Gaussian multiplication parametrization

```text
C0=c1^2+c2^2,
R=r1^2+r2^2,
P=c1*r1-c2*r2,
Q=c1*r2+c2*r1.
```

Thus the ambient norm surface contains abundant rational/integer families and is not the sparse physical subset. The physical masks have not been converted to an additional fixed-degree irreducible equation. A generic determinant-method theorem on the norm surface therefore does not certify the desired `B^{-delta}` density loss.

## Final applicability matrix

```text
BETTIN_CHANDEE=false
DONG_ROBLES_ZEINDLER=false
WRIGHT_PARTIALLY_FIXED=false
BLOMER_PASCADI_2026=false
GAUSSIAN_SPARSE_LARGE_SIEVE=false
QUADRATIC_ROOT_EQUIDISTRIBUTION_TOTAL_MASS=false
GENERIC_DETERMINANT_METHOD_NORM_SURFACE=false
```

The common failed hypothesis is not insufficient numerical strength. It is the absence of an exact theorem converting the physical completion indicator into either:

1. a power-small zero-frequency density; or
2. a mean-zero / oscillatory coefficient sequence with a controlled main term.

That exact arithmetic density question is the receiver passed to Stage14-4dd.
