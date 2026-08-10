# Stage14-sH44 literature applicability note

Frozen target:

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreDualRootLineCompatibilityEnergyPowerSaving
```

Frozen source:

```text
Stage14-s7-44
SOURCE_SNAPSHOT_SHA=ca427d50b9afcbae226b6ffe619dba2cc98deebc
SOURCE_STAGE_HEAD_SHA=4588528adb7776978c4071f9d3cb4e6ff5231570
TARGET_FILE=stages/stage14/14-s7-44/result.md
TARGET_SECTION=8-9
```

This note follows the repository H snapshot protocol. Later reductions such as 4dc do not replace the audited mathematical object.

## 1. Applicability standard

A theorem is counted as directly applicable only if an explicit adapter preserves:

```text
theta=1/4,
5/24<=phi<=1/4,
C~B^(2phi-1/4),
primitive Gaussian root line,
primitive endpoint +/- root line,
all squarefree cells,
positivity/interval masks,
statewise reducedness,
global odd primitivity,
full-core row/column sign allocation,
exact reciprocal equations,
Gaussian orientation consistency,
X13 post-column reconstruction,
charged-once treatment of C.
```

Similarity of a phase or congruence shape is insufficient.

## 2. Reuss — bilinear/trilinear hypersurfaces

Thomas Reuss, *Counting points on bilinear and trilinear hypersurfaces*, arXiv:1502.07594.

Primary source:

```text
https://arxiv.org/abs/1502.07594
```

The paper gives determinant-sensitive point bounds for irreducible bilinear forms on `P^1 x P^1`, and analogous bounds for irreducible nonsingular trilinear forms on `P^1 x P^1 x P^1` involving the Cayley hyperdeterminant.

This is a high-priority post-elimination candidate, but no source-snapshot identity puts the full physical compatibility receiver on one such hypersurface with a fresh fixed-power determinant/hyperdeterminant. The two full-core congruences have already used `C`; manufacturing a determinant divisible by the same `C` is not automatically a new saving.

```text
REUSS_BILINEAR_DIRECT_ADAPTER=false
REUSS_TRILINEAR_DIRECT_ADAPTER=false
REUSS_TRANSFER_REQUIRES_NEW_PHYSICAL_ELIMINANT=true
```

## 3. Bettin–Chandee — trilinear Kloosterman fractions

Sandro Bettin and Vorrapan Chandee, *Trilinear forms with Kloosterman fractions*, arXiv:1502.00769.

```text
https://arxiv.org/abs/1502.00769
```

The theorem controls oscillatory trilinear sums with inverse-fraction phases. The frozen Stage14 receiver is a positive compatibility count. No exact Fourier/divisor-switch adapter from that count to the Bettin–Chandee kernel is present in the source snapshot.

```text
BETTIN_CHANDEE_DIRECT_ADAPTER=false
```

## 4. Dong–Robles–Zeindler 2026 — bilinear Kloosterman fractions

Anji Dong, Nicolas Robles, Dirk Zeindler, *Bilinear forms with Kloosterman fractions and applications*, arXiv:2601.00292.

```text
https://arxiv.org/abs/2601.00292
```

The paper improves bilinear Kloosterman-fraction estimates and allows arbitrary coefficient sequences. This is analytically attractive if the physical compatibility condition can be centered and transformed to a genuine inverse-fraction phase.

The frozen source contains no such transformation and no proof that the resulting denominator/frequency variables satisfy the theorem's required independent ranges while all physical masks remain in acceptable coefficients.

```text
DONG_ROBLES_ZEINDLER_DIRECT_ADAPTER=false
DONG_ROBLES_ZEINDLER_TRANSFER_REQUIRES_MEAN_ZERO_INVERSE_FRACTION_ADAPTER=true
```

## 5. Wright 2026 — partially fixed denominator

Thomas Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions*, arXiv:2604.25177.

```text
https://arxiv.org/abs/2604.25177
```

This is structurally relevant when an inverse-fraction denominator has a fixed factor and another genuinely moving factor. The frozen s7-44 receiver has no derived inverse-fraction representation at all, so this theorem is not yet at the correct abstraction layer.

```text
WRIGHT_PARTIALLY_FIXED_DENOMINATOR_DIRECT_ADAPTER=false
```

## 6. Baier 2026 — modular square-root energy

Stephan Baier, *On certain bilinear sums with modular square roots and applications*, arXiv:2601.15448, and *A note on bilinear sums with modular square roots*, arXiv:2605.01635.

```text
https://arxiv.org/abs/2601.15448
https://arxiv.org/abs/2605.01635
```

These results directly concern modular square-root energies/bilinear exponential sums, so they are relevant background to the local root equations. However the Stage14 source receiver simultaneously carries a `t^2=-1` primitive line and a `t^2=1` primitive line on a moving odd composite core, plus exact reciprocal completion and all physical masks. No adapter identifies the complete physical compatibility subset with the one-root-family bilinear exponential sums controlled in these papers.

```text
BAIER_MODULAR_SQUARE_ROOT_ENERGY_DIRECT_ADAPTER=false
```

## 7. Blomer–Pascadi 2026 — fixed-modulus complete Kloosterman bilinear forms

Valentin Blomer and Alexandru Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters*, arXiv:2607.24311.

```text
https://arxiv.org/abs/2607.24311
```

The paper provides power-saving bounds for bilinear forms in complete Kloosterman sums for all moduli, including a power saving in the critical square-root-length range. This theorem would be highly relevant after a Poisson/completion step produces a bilinear family of classical complete Kloosterman sums with controlled arguments and coefficients.

No such completion identity is proved for the frozen s7-44 positive compatibility count. In particular, the canonical physical masks and the charged-once common core must survive the conversion.

```text
BLOMER_PASCADI_DIRECTLY_APPLICABLE=false
FIXED_MODULUS_COMPLETE_KLOOSTERMAN_ADAPTER_PROVED=false
```

## 8. Generic determinant / genus-one background

The reciprocal Edwards family from earlier Stage14 work has singular values `lambda in {0,+4,-4}`. On the full Cayley core of the frozen receiver,

```text
lambda == +/-4 mod p^e
```

for every fixed-power prime power of the common core.

Thus the modulus creating the square-root barrier lies precisely on congruence bad-reduction support for the reciprocal Edwards family. A smooth fixed-parameter determinant/genus-one theorem is therefore not automatically uniform in this modulus.

```text
GENERIC_SMOOTH_GENUS_ONE_DIRECT_ADAPTER=false
```

## 9. Fixed-U t/tH literature is separate

Later fixed-U work obtains projective-character, inverse-fraction, graph-Kloosterman and fixed-divisor-modulus descriptions. Those are useful evidence for possible techniques, but the frozen s7-44 request explicitly forbids cross-promotion without an exact bridge.

```text
T80_T81_T82_TH23_DIRECT_BRIDGE_TO_FROZEN_SH44=false
```

## 10. Final literature verdict

No located theorem directly proves

```text
sum_C I_C << B^(1/2-delta+o(1))
```

for any fixed `delta>0` on the frozen s7-44 receiver while retaining the complete physical masks and charged-once common-core accounting.

```text
OFF_THE_SHELF_THEOREM_APPLICABLE=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
```

The best next theorem-adapter targets are:

```text
1. derive a genuine physical bilinear/trilinear eliminant with fresh determinant
   -> Reuss test;
2. derive a centered inverse-fraction kernel
   -> Dong–Robles–Zeindler / Bettin–Chandee / Wright test;
3. complete that kernel to classical Kloosterman sums
   -> Blomer–Pascadi / Kuznetsov test.
```

Until one of those adapters is proved, none of the cited results can be imported as a strict sub-square-root Stage14 theorem.
