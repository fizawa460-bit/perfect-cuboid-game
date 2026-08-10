# Stage14-4dH literature / theorem applicability matrix

Frozen audit contract:

```text
AUDITED_THROUGH=Stage14-4dc
SOURCE_SNAPSHOT_SHA=949718da097bb8aa2dec95095ba72de54bf088ba
TARGET_FILE=stages/stage14/14-4dc/result.md
TARGET_FROZEN=true
```

Current main and merged q10 are used only for bibliographic context; the mathematical receiver is not changed.

## Exact target

```text
sum_C I_C^phys << B^(1/2-delta+o(1)), delta>0,
```

for the frozen Gaussian-product physical-completion receiver.

## Bettin--Chandee

S. Bettin, V. Chandee, *Trilinear forms with Kloosterman fractions*, arXiv:1502.00769.
https://arxiv.org/abs/1502.00769

```text
DIRECTLY_APPLICABLE=false
```

No inverse-fraction kernel with removed zero mode is derived by the frozen source.

## Dong--Robles--Zeindler 2026

A. Dong, N. Robles, D. Zeindler, *Bilinear forms with Kloosterman fractions and applications*, arXiv:2601.00292.
https://arxiv.org/abs/2601.00292

```text
DIRECTLY_APPLICABLE=false
```

The physical selector is positive and no inverse-fraction adapter with a controlled main term is available.

## Wright 2026

T. Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177.
https://arxiv.org/abs/2604.25177

```text
DIRECTLY_APPLICABLE=false
SIEGEL_WALFISZ_PHYSICAL_WEIGHT_PROVED=false
ZERO_FREQUENCY_REMOVED=false
```

## Blomer--Pascadi 2026

V. Blomer, A. Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311.
https://arxiv.org/abs/2607.24311

The paper gives a power saving for complete-Kloosterman bilinear forms even in the critical square-root-length range.

```text
DIRECTLY_APPLICABLE=false
COMPLETE_KLOOSTERMAN_KERNEL_DERIVED=false
```

The frozen receiver remains a positive norm-congruence count, not a completed Kloosterman bilinear form with removed main term.

## Baier--Bansal Gaussian sparse large sieve

S. Baier, A. Bansal, *Large sieve with sparse sets of moduli for Z[i]*, arXiv:1811.07300.
https://arxiv.org/abs/1811.07300

```text
DIRECTLY_APPLICABLE=false
MEAN_ZERO_GAUSSIAN_COEFFICIENT_SEQUENCE_PROVED=false
```

## Baier 2026 modular-square-root energy

S. Baier, *On certain bilinear sums with modular square roots and applications*, arXiv:2601.15448.
https://arxiv.org/abs/2601.15448

S. Baier, *A note on bilinear sums with modular square roots*, arXiv:2605.01635.
https://arxiv.org/abs/2605.01635

```text
DIRECTLY_APPLICABLE=false
```

These are oscillatory modular-root estimates; the frozen object is a positive composite-core physical total mass and no zero-mode-removing adapter is known.

## Reuss 2015 — merged-q10 transfer candidate

T. Reuss, *Counting points on bilinear and trilinear hypersurfaces*, arXiv:1502.07594.
https://arxiv.org/abs/1502.07594

Reuss is tested because his bounds improve with the determinant of an irreducible bilinear form or the Cayley hyperdeterminant of an irreducible nonsingular trilinear form.

Frozen-source transfer test:

```text
REUSS_TRANSFER_TESTED=true
IRREDUCIBLE_BILINEAR_ELIMINANT_EXHIBITED=false
NONSINGULAR_TRILINEAR_ELIMINANT_EXHIBITED=false
FRESH_FIXED_POWER_DETERMINANT_EXHIBITED=false
DIRECTLY_APPLICABLE=false
```

The source exposes only `P^2+Q^2=C0R`. Its rational cross determinant/sum with the endpoint line is coprime to `C0`, while cross norms carrying `C0` are consequences of already charged root equations.

## Quadratic-root equidistribution

E. Musicantov, S. Zehavi, *Sectorial equidistribution of the roots of x^2+1 modulo primes*, arXiv:2112.07494.
https://arxiv.org/abs/2112.07494

H. T. Ngo, *On roots of quadratic congruences*, arXiv:2107.13301.
https://arxiv.org/abs/2107.13301

```text
DIRECT_TOTAL_MASS_POWER_SAVING_APPLICABLE=false
```

The source already pays only `B^o(1)` root-choice entropy; discrepancy does not prove a power-small average physical density.

## Generic determinant method

T. D. Browning, D. R. Heath-Brown, *Counting rational points on hypersurfaces*, arXiv:math/0404456.
https://arxiv.org/abs/math/0404456

T. D. Browning, D. R. Heath-Brown, P. Salberger, *Counting rational points on algebraic varieties*, arXiv:math/0410117.
https://arxiv.org/abs/math/0410117

The norm surface

```text
P^2+Q^2=C0R
```

has the abundant Gaussian multiplication parametrization

```text
C0=c1^2+c2^2,
R=r1^2+r2^2,
P=c1*r1-c2*r2,
Q=c1*r2+c2*r1.
```

The frozen physical masks are not an additional fixed-degree irreducible equation.

```text
GENERIC_NORM_SURFACE_DIRECTLY_APPLICABLE_FOR_FIXED_POWER_SAVING=false
```

## Final matrix

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

The common missing input is a fixed-power upper-density theorem for the physical divisor-split completion weight, or an equivalent transform proving its zero-frequency/main term power-small before cancellation machinery is invoked.
