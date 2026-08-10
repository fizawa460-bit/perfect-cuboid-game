# Stage14-4dH — Gaussian product physical-completion energy applicability audit

## Snapshot contract

```text
H_STAGE=Stage14-4dH
H_SOURCE_STAGE=Stage14-4dc
AUDITED_THROUGH=Stage14-4dc
SOURCE_SNAPSHOT_SHA=949718da097bb8aa2dec95095ba72de54bf088ba
TARGET_FILE=stages/stage14/14-4dc/result.md
REQUESTED_OBJECT=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving
TARGET_FROZEN=true
H_SOURCE_SNAPSHOT_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true
```

This is the immutable Stage14-4dc head that emitted the mainline H request. Later q10/H-protocol merges are used only as literature/protocol context; they do not mutate the audited receiver.

## Status

`COMPLETE_MAINLINE_H_APPLICABILITY_AUDIT_NO_CERTIFIED_UNIFORM_DELTA`

The requested theorem was

```text
sum_C I_C^phys << B^(1/2-delta+o(1))
```

for some fixed `delta>0`, uniformly on

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4.
```

No currently identified off-the-shelf theorem certifies such a delta for the exact frozen physical receiver. This is a completed negative applicability certificate, not a pending H request.

## 1. Frozen 4dc receiver

After the known `B^o(1)` peels,

```text
P=a0*U,
Q=b0*V,
gcd(P,Q)=1 at fixed-power scale,
P*Q<=B^(1/2+o(1)),
C0=C/B^o(1),
C0 | P^2+Q^2,
gcd(C0,PQ)=1.
```

For each fixed `C` and one of the `B^o(1)` roots of `t^2=-1 mod C0`, primitive determinant spacing gives

```text
#(P,Q) <= B^(1/2-chi+o(1)).
```

Hence

```text
C choice                    : chi
Gaussian product root line  : 1/2-chi
physical completion         : 0
---------------------------------
total                       : 1/2.
```

Let `w_C(P,Q)` be the nonnegative physical completion multiplicity after all divisor-split, squarefree-cell, interval, sign/orientation and reciprocal filters. The frozen source proves only

```text
0 <= w_C(P,Q) <= B^o(1).
```

Thus a fixed-power improvement must come from a power-small density theorem for the support of `w_C` inside the ambient Gaussian root-line population.

## 2. Zero-frequency obstruction

Any additive-character/Fourier completion of the root-line congruence splits into

```text
zero frequency + nonzero frequencies.
```

The zero-frequency term is the positive average density of `w_C(P,Q)` on the ambient root-line family. Without an independent theorem showing that this density is `B^{-delta+o(1)}`, this term can remain as large as

```text
B^(1/2+o(1)).
```

Therefore nonzero-frequency cancellation alone cannot prove the requested strict sub-square-root estimate.

```text
ZERO_FREQUENCY_PHYSICAL_DENSITY_OBSTRUCTION=true
```

## 3. Kloosterman-fraction / dispersion candidates

Bettin--Chandee, Dong--Robles--Zeindler and Wright control oscillatory inverse-fraction sums after a Fourier/dispersion reduction. The frozen 4dc receiver has no proved nonzero inverse-fraction kernel, no removed zero mode, and no Siegel--Walfisz theorem for the physical selector.

```text
BETTIN_CHANDEE_DIRECTLY_APPLICABLE=false
DONG_ROBLES_ZEINDLER_DIRECTLY_APPLICABLE=false
WRIGHT_PARTIALLY_FIXED_DENOMINATOR_DIRECTLY_APPLICABLE=false
SIEGEL_WALFISZ_PHYSICAL_WEIGHT_PROVED=false
KLOOSTERMAN_FRACTION_ZERO_FREQUENCY_REMOVED=false
```

## 4. Complete Kloosterman bilinear bounds

Blomer--Pascadi (2026) give a genuine saving for bilinear forms with complete Kloosterman sums in the critical square-root-length range. The frozen receiver has not been transformed into a completed Kloosterman kernel `S(m,n;C)` with a controlled main term; it remains the positive norm congruence

```text
C0 | P^2+Q^2
```

weighted by `w_C(P,Q)`.

```text
BLOMER_PASCADI_COMPLETE_KLOOSTERMAN_DIRECTLY_APPLICABLE=false
COMPLETE_KLOOSTERMAN_ADAPTER_PROVED=false
```

## 5. Gaussian / modular-square-root energy candidates

Baier--Bansal Gaussian sparse large-sieve results and Baier's 2026 modular-square-root bilinear/energy results control oscillatory or `L^2` quantities. They do not directly bound the positive composite-core total mass with the frozen physical selector, and no mean-zero adapter retaining all masks is known.

```text
GAUSSIAN_SPARSE_MODULUS_LARGE_SIEVE_DIRECTLY_APPLICABLE=false
BAIER_2026_MODULAR_SQRT_ENERGY_DIRECTLY_APPLICABLE=false
MEAN_ZERO_GAUSSIAN_PHYSICAL_WEIGHT_PROVED=false
```

## 6. Reuss transfer test

Merged q10, used here only as literature context, marks Reuss's bilinear/trilinear point-counting theorem as the strongest deterministic transfer candidate. Its useful regime requires an irreducible bilinear form with a fresh large determinant, or an irreducible nonsingular trilinear form with a fresh Cayley hyperdeterminant.

The frozen 4dc source does not expose such an eliminant. Its universal algebraic relation is only

```text
P^2+Q^2=C0*R.                                      (6.1)
```

The rational cross determinant/sum with the endpoint root line is coprime to `C0` by the source's resultant-4 theorem. Quadratic cross norms divisible by `C0` are algebraic consequences of already-charged root equations and cannot be reused as a fresh determinant.

Thus

```text
REUSS_TRANSFER_TESTED=true
REUSS_IRREDUCIBLE_BILINEAR_ELIMINANT_EXHIBITED=false
REUSS_NONSINGULAR_TRILINEAR_ELIMINANT_EXHIBITED=false
REUSS_FRESH_FIXED_POWER_DETERMINANT_EXHIBITED=false
REUSS_DIRECTLY_APPLICABLE=false
```

## 7. Generic determinant method

The ambient norm relation (6.1) has the Gaussian multiplication parametrization

```text
C0=c1^2+c2^2,
R =r1^2+r2^2,
P=c1*r1-c2*r2,
Q=c1*r2+c2*r1.
```

Hence the norm surface itself contains abundant integral families. The physical factorization, squarefree-cell, sign/orientation, interval and reciprocal-completion masks have not been converted into an additional fixed-degree irreducible equation defining a smaller variety.

```text
GENERIC_DETERMINANT_METHOD_ON_NORM_SURFACE_DIRECTLY_APPLICABLE=false
FIXED_DEGREE_JOINT_PHYSICAL_INCIDENCE_VARIETY_EXHIBITED=false
```

## 8. Refined exact receiver

For each `C~B^chi`, define

```text
A_C={
  primitive (P,Q):
  C0 | P^2+Q^2,
  P*Q<=B^(1/2+o(1)),
  some divisor split P=a0U,Q=b0V admits every frozen physical reciprocal mask
}.
```

A strict sub-square-root theorem is now exactly a fixed-power upper-density bound

```text
sum_{C~B^chi} #A_C << B^(1/2-delta+o(1)).
```

The minimal remaining obstruction is

```text
SquareRootThetaQuarterGaussianNormDivisorSplitPhysicalAdmissibilityZeroFrequencyDensity
```

and this is an exact-arithmetic density problem for Stage14-4dd, not a reason to launch another generic H search.

## 9. H verdict

```text
OFF_THE_SHELF_THEOREM_APPLICABLE=false
CERTIFIED_B_POWER_SAVING_EXPONENT=0
MAINLINE_H_COMPLETED=true
MAINLINE_H_RESULT=NO_CERTIFIED_UNIFORM_POWER_SAVING
CERTIFIED_MAINLINE_H_DELTA=0
OFF_THE_SHELF_UNIFORM_POWER_SAVING_PROVED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
```

No whole-family exponent change is certified:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
```

Preferred receiver / next step:

```text
MINIMAL_REMAINING_OBSTRUCTION=SquareRootThetaQuarterGaussianNormDivisorSplitPhysicalAdmissibilityZeroFrequencyDensity
PREFERRED_RECEIVER=SquareRootThetaQuarterGaussianNormDivisorSplitPhysicalAdmissibilityZeroFrequencyDensity
NEXT=Stage14-4dd
```

## Stage boundary

```text
STAGE14_4DH=COMPLETE_MAINLINE_H_APPLICABILITY_AUDIT_NO_CERTIFIED_UNIFORM_DELTA
H_STAGE=Stage14-4dH
AUDITED_THROUGH=Stage14-4dc
SOURCE_SNAPSHOT_SHA=949718da097bb8aa2dec95095ba72de54bf088ba
TARGET_FILE=stages/stage14/14-4dc/result.md
REQUESTED_OBJECT=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving
TARGET_FROZEN=true
H_SOURCE_SNAPSHOT_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true
MERGED_Q10_CONTEXT_CONSUMED=true
MAINLINE_H_COMPLETED=true
MAINLINE_H_RESULT=NO_CERTIFIED_UNIFORM_POWER_SAVING
CERTIFIED_MAINLINE_H_DELTA=0
ZERO_FREQUENCY_PHYSICAL_DENSITY_OBSTRUCTION=true
BETTIN_CHANDEE_DIRECTLY_APPLICABLE=false
DONG_ROBLES_ZEINDLER_DIRECTLY_APPLICABLE=false
WRIGHT_PARTIALLY_FIXED_DENOMINATOR_DIRECTLY_APPLICABLE=false
BLOMER_PASCADI_COMPLETE_KLOOSTERMAN_DIRECTLY_APPLICABLE=false
GAUSSIAN_SPARSE_MODULUS_LARGE_SIEVE_DIRECTLY_APPLICABLE=false
BAIER_2026_MODULAR_SQRT_ENERGY_DIRECTLY_APPLICABLE=false
REUSS_TRANSFER_TESTED=true
REUSS_FRESH_FIXED_POWER_DETERMINANT_EXHIBITED=false
REUSS_DIRECTLY_APPLICABLE=false
GENERIC_DETERMINANT_METHOD_ON_NORM_SURFACE_DIRECTLY_APPLICABLE=false
OFF_THE_SHELF_UNIFORM_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
REMAINING_RECEIVER=SquareRootThetaQuarterGaussianNormDivisorSplitPhysicalAdmissibilityZeroFrequencyDensity
NEXT=Stage14-4dd
```
