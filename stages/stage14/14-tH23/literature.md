# Stage14-tH23 literature applicability note — t82-refined fixed-U divisor modulus

Target:

```text
FixedUCoordinateDivisorModulusSingleFrequencyCanonicalPrimeShortCoverInverseFractionLargeSieve
```

This note is applicability-only. No external theorem below is imported as a proof of the Stage14 receiver.

## 1. What merged t82 removes

The t82 refinement proves internally

```text
d_diag | D_Ubeta | |R*S|,
d_diag <= m/2 < ell/4,
# {d_diag for fixed U} = B^o(1),
[pi]=sigma([V]) mod d_diag.
```

Therefore the external theorem does **not** need to supply moving modulus averaging, fixed-U projective coefficient removal, two-frequency reduction, Hecke-conductor compression, or fixed-power fractional/mismatch support savings.

The remaining object is a fixed-divisor-modulus, one-frequency physical correlation.

## 2. Bettin–Chandee and later Kloosterman-fraction bounds

Bettin–Chandee, *Trilinear forms with Kloosterman fractions* (arXiv:1502.00769), estimates trilinear sums schematically of the form

```text
sum_{a,m,n} nu_a alpha_m beta_n e(a*inv(m)/n),
```

with a moving denominator `n`.

Recent improvements such as Dong–Robles–Zeindler (arXiv:2601.00292) remain in moving-denominator Kloosterman-fraction geometry.

The t82 hard object has fixed `d_diag|R*S` after `U` is fixed. Additive reciprocity can create moving coordinate denominators, but the resulting coefficients retain the canonical Gaussian-prime restriction and the `ell`-coupled short-cover masks. No exact adapter preserving those coefficients and ranges is available.

```text
BETTIN_CHANDEE_DIRECT_ADAPTER=false
MOVING_DENOMINATOR_KLOOSTERMAN_FRACTION_APPLICABLE=false
```

## 3. Wright's partially fixed modulus

Thomas Wright, *Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced convolutions* (arXiv:2604.25177), improves Kloosterman-fraction technology when the denominator contains a fixed factor.

This is structurally closer to t82 than the original Bettin–Chandee form, but the theorem still obtains cancellation from a remaining moving denominator family. In the t82 hard packet the modulus is itself a divisor-hosted fixed coefficient and the remaining physical variables are canonical-prime and primitive-cover slopes.

```text
PARTIALLY_FIXED_DENOMINATOR_ADAPTER=false
```

## 4. Kuznetsov / complete Kloosterman bilinear bounds

Deshouillers–Iwaniec/Kuznetsov technology becomes applicable after a physical sum has been completed to a family of classical Kloosterman sums `S(m,n;c)` with explicit argument and modulus ranges.

Blomer–Pascadi, *Bilinear forms with Kloosterman sums via quadratic characters* (arXiv:2607.24311), proves all-moduli bilinear Kloosterman bounds. Their main theorem treats arbitrary modulus `c` and interval-supported argument sequences; in the critical square-root range the paper obtains a fixed power saving, stated in the introduction as `c^-1/32` over trivial size.

This is the closest modern fixed-modulus technology. It is still not directly applicable because t82 gives

```text
[pi]=sigma([V]) mod d_diag
```

with incomplete canonical Gaussian-prime and balanced-cover slope sequences, not an already-completed bilinear form in `S(m,n;d_diag)`.

A new Poisson/completion step must first prove that:

1. the Kloosterman arguments fall into the theorem's interval/range hypotheses;
2. no second independent frequency or modulus family is recreated;
3. the canonical Gaussian-prime weight becomes an admissible coefficient sequence;
4. the short ellipse, `ell*H*R*T`, and `ell*delta` masks remain in coefficients at only `B^o(1)` loss.

No such adapter is currently proved.

```text
POISSON_COMPLETE_KLOOSTERMAN_ADAPTER_PROVED=false
MODERN_FIXED_MODULUS_KLOOSTERMAN_BILINEAR_APPLICABLE=false
SPECTRAL_DUALITY_APPLICABLE=false
```

## 5. Range significance of d_diag < ell/4

The new inequality

```text
d_diag <= m/2 < ell/4
```

is real structural information. It rules out a modulus exceeding the prime norm scale and removes an artificial modulus-family parameter.

It does **not** force a uniform favorable incomplete-sum regime, because the coordinates of the Gaussian prime have scale about `sqrt(ell)` while `d_diag` may still lie either below or above that coordinate scale. A theorem based only on `d_diag<ell` therefore does not provide a fixed `B`-power saving over the entire t82 hard range.

```text
FIXED_DIVISOR_MODULUS_LT_ELL_OVER_4_SUFFICIENT_FOR_POWER_SAVING=false
```

## 6. Canonical Gaussian-prime weight

The remaining direction sequence is a fixed linear transform of a canonical Gaussian direction prime. Generic rational-prime or arbitrary-coefficient Kloosterman estimates do not automatically give a uniform estimate for this projective Gaussian-prime slope with the same `ell` participating in the cover cutoffs.

```text
CANONICAL_GAUSSIAN_PRIME_SIDE_BOUND_APPLICABLE=false
```

## 7. Cover coefficients

Merged t78 already proves exact four-cell Möbius tensorization. After dyadic/Mellin localization the divisor expansion costs only `B^o(1)` in coefficient `L2` norms.

```text
FOUR_CELL_COEFFICIENT_L2_THEOREM_READY=true
FOUR_CELL_COEFFICIENT_L2_LOSS=Bo1
```

The remaining cover sequence is nevertheless balanced, primitive, slope-sensitive, and coupled to `ell` by the short ellipse and sharp hyperbolas. No located standard fixed-modulus theorem estimates that sequence with the canonical-prime side under all masks.

## 8. Final applicability verdict

The t82 refinement narrows the obstruction to

```text
FixedUCoordinateDivisorModulusCanonicalGaussianPrimeShortCoverSingleFrequencyCollisionDispersion
```

No off-the-shelf theorem currently supplies a complete adapter preserving the fixed divisor modulus, single frequency, canonical Gaussian-prime slope, balanced primitive cover, and all physical masks.

```text
OFF_THE_SHELF_FIXED_DIVISOR_SINGLE_FREQUENCY_POWER_SAVING_PROVED=false
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0
```
