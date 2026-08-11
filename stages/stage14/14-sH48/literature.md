# Stage14-sH48 literature / theorem applicability matrix

Frozen source:

```text
SOURCE_SNAPSHOT_SHA=e228c62d6e0fa7d4bf2939bd8e1710f67aa4a9be
AUDITED_THROUGH=Stage14-s7-48
```

The receiver is the primitive quarter-scale pair

```text
m*n = epsilon_- u_* R J,
m^2+n^2 = 2*epsilon_+ C_* S T,
```

with all six physical factor scales, squarefree/coprime masks, pairwise fixed-power separation, mixed-root allocation and reciprocal completion retained.

## 1. Reuss — bilinear/trilinear hypersurface counting

Primary source:

- Thomas Reuss, *Counting points on bilinear and trilinear hypersurfaces*, arXiv:1502.07594.

The theorem gives determinant/hyperdeterminant-sensitive bounds for irreducible bilinear and non-singular trilinear forms in boxes.

Verdict:

```text
DIRECT=false
```

Reason: s7-48 proves that eliminating the square coordinates produces no fresh polynomial relation in the plus/minus products.  Expanding Gaussian factors turns the rotated coordinate product into a higher-degree composite relation; no canonical irreducible bilinear/trilinear form with a fresh fixed-power determinant is presently derived.

## 2. Dong--Robles--Zeindler — Kloosterman fractions

Primary source:

- Anji Dong, Nicolas Robles, Dirk Zeindler, *Bilinear forms with Kloosterman fractions and applications*, arXiv:2601.00292.

The paper gives improved bounds for genuine inverse-fraction bilinear phases with arbitrary coefficient sequences.

Verdict:

```text
DIRECT=false
NEAR_RELEVANT=true
```

Missing adapter: a legal centering/divisor-switch/Fourier step converting the frozen positive compatibility count to the required inverse-fraction kernel without losing physical masks or recharging a used modulus.

## 3. Blomer--Pascadi — complete Kloosterman bilinear forms

Primary source:

- Valentin Blomer, Alexandru Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311.

The paper proves fixed-power cancellation for bilinear forms with complete Kloosterman sums, including the critical square-root length regime.

Verdict:

```text
DIRECT=false
HIGH_VALUE_AFTER_COMPLETION_ADAPTER=true
```

Missing adapters:

```text
positive physical indicator -> centered mean-zero object,
centered object -> complete S(m,n;c) family,
coefficient L2 control with all cell masks.
```

Without zero-frequency removal, the theorem does not control the principal positive physical density.

## 4. Baier — modular square-root bilinear sums

Primary sources:

- Stephan Baier, *On bilinear sums with modular square roots and applications III*, arXiv:2603.25814.
- Stephan Baier, *A note on bilinear sums with modular square roots*, arXiv:2605.01635.

Verdict:

```text
DIRECT=false
```

The frozen s7-48 receiver is downstream of the mixed-root spacing already used in s7-46/47.  No fresh independent prime or prime-square root modulus remains.  The live variable is product-vs-norm factorization correlation for the same primitive integer pair.

## 5. Ford — balanced divisors / multiplication table

Primary sources:

- Kevin Ford, *The distribution of integers with a divisor in a given interval*, arXiv:math/0401223.
- Kevin Ford, *Integers with a divisor in (y,2y]*, arXiv:math/0607473.
- Kevin Ford, *Rough integers with a divisor in a given interval*, arXiv:1901.02548.

Verdict:

```text
MARGINAL_INFORMATION_RELEVANT=true
FIXED_B_POWER_SAVING_FOR_FROZEN_CORRELATION=false
```

These results show that balanced-divisor conditions have subtle logarithmic-scale densities and multiplication-table phenomena; they do not supply a uniform fixed `B^{-delta}` loss for the simultaneous product/sum-of-squares physical correlation.

## 6. Sums of two squares

Background primary source checked:

- James Maynard, *Sums of two squares in short intervals*, arXiv:1910.13384.

The classical sum-of-two-squares marginal is only logarithmically sparse.  Modern short-interval results likewise do not furnish the required fixed-power thinning of the frozen dual factorization packet.

Verdict:

```text
ONE_SIDED_SUM_TWO_SQUARES_FIXED_POWER_SAVING=false
```

## 7. Stage14 q10 compatibility

Merged `Stage14-q10` already classified Reuss and inverse-fraction technology as near candidates for the older post-sqrt receiver.  s7-48 provides a much cleaner product/sum-of-squares kernel but still does not provide the missing mean-zero inverse-fraction, complete-Kloosterman, or nondegenerate determinant adapter.

No q10 theorem is cross-promoted merely from similarity.

## Final matrix

```text
REUSS_DIRECT=false
DONG_ROBLES_ZEINDLER_DIRECT=false
BLOMER_PASCADI_DIRECT=false
BAIER_MODULAR_ROOT_DIRECT=false
FORD_BALANCED_DIVISOR_DIRECT_FIXED_POWER=false
ONE_SIDED_SUM_TWO_SQUARES_FIXED_POWER=false
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
```

Preferred next construction:

```text
CenteredPrimitiveQuarterPairProductNormDualBalancedCellFactorizationDispersion
```

The first task is not another literature search.  It is to derive a centered physical correlation kernel and identify whether its nonzero frequencies land in an existing theorem class.
