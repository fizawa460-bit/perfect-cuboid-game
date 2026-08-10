# Stage14-4dH — Gaussian product physical-completion energy applicability audit

## Status

`COMPLETE_MAINLINE_H_APPLICABILITY_AUDIT_NO_CERTIFIED_UNIFORM_DELTA`

Stage14-4dH executes the auxiliary H requested by merged `Stage14-4dc` and imports the newly merged `Stage14-q10` literature radar. The entering theorem is

```text
V(B) << B^(1/2+o(1)).
```

The requested H theorem was

```text
sum_C I_C^phys << B^(1/2-delta+o(1))
```

for some fixed `delta>0`, uniformly on

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4.
```

No currently identified off-the-shelf theorem certifies such a delta for the exact physical receiver. This is a completed negative applicability result, not a pending H request. The mainline is therefore unblocked and may continue to `Stage14-4dd` on a narrower exact arithmetic receiver.

---

## 1. Exact 4dc receiver

After all known `B^o(1)` peels,

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

Hence the complete charged-once ledger is

```text
C choice                    : chi
Gaussian product root line  : 1/2-chi
physical completion         : 0
---------------------------------
total                       : 1/2.
```

Write `w_C(P,Q)` for the nonnegative physical completion multiplicity after all divisor-split, squarefree-cell, interval, sign/orientation and reciprocal filters. Merged 4dc gives only

```text
0 <= w_C(P,Q) <= B^o(1).
```

Thus the only remaining possible fixed-power saving is an upper-density theorem for the support of `w_C` inside the ambient Gaussian root-line population.

---

## 2. Zero-frequency obstruction

Any additive-character/Fourier completion of the root-line congruence separates into

```text
zero frequency + nonzero frequencies.
```

The zero frequency is the positive average density of `w_C(P,Q)` on the ambient root-line family. Without an independent theorem showing that this density is `B^{-delta+o(1)}`, the zero-frequency contribution can be as large as the full

```text
B^(1/2+o(1))
```

count.

Therefore cancellation estimates for nonzero frequencies do not by themselves prove a strict sub-square-root bound.

```text
ZERO_FREQUENCY_PHYSICAL_DENSITY_OBSTRUCTION=true.
```

---

## 3. Kloosterman-fraction / dispersion candidates

Bettin--Chandee and later Dong--Robles--Zeindler bounds apply to oscillatory inverse-fraction bilinear/trilinear sums. Wright's partially-fixed denominator refinement likewise acts after a dispersion/Fourier reduction and its distribution applications require coefficient-distribution hypotheses such as Siegel--Walfisz behavior.

The exact 4dc receiver has no derived nonzero inverse-fraction phase and no proof that the physical weight is mean-zero or Siegel--Walfisz. Introducing additive characters for `C0|P^2+Q^2` leaves the zero mode from Section 2.

Hence

```text
BETTIN_CHANDEE_DIRECTLY_APPLICABLE=false,
DONG_ROBLES_ZEINDLER_DIRECTLY_APPLICABLE=false,
WRIGHT_PARTIALLY_FIXED_DENOMINATOR_DIRECTLY_APPLICABLE=false,
SIEGEL_WALFISZ_PHYSICAL_WEIGHT_PROVED=false,
KLOOSTERMAN_FRACTION_ZERO_FREQUENCY_REMOVED=false.
```

---

## 4. Blomer--Pascadi complete-Kloosterman bound

Blomer--Pascadi (2026) prove a genuine saving for bilinear forms with complete Kloosterman sums, including the critical range in which the summation length is the square root of the modulus.

This theorem is not directly applicable here because 4dc has not produced a completed Kloosterman kernel `S(m,n;C)` with coefficient sequences and a removed main term. It has produced the positive norm congruence

```text
C0 | P^2+Q^2
```

with the arithmetic physical selector `w_C(P,Q)`. A formal completion would still leave the zero-frequency physical density untouched.

```text
BLOMER_PASCADI_COMPLETE_KLOOSTERMAN_DIRECTLY_APPLICABLE=false,
COMPLETE_KLOOSTERMAN_ADAPTER_PROVED=false.
```

---

## 5. Gaussian / modular-square-root large-sieve and energy candidates

Baier--Bansal large-sieve results over `Z[i]` and Baier's 2026 modular-square-root energy/bilinear estimates control oscillatory or `L^2` quantities associated with Gaussian/square-root families.

Merged q10 correctly identifies Baier 2026 as a near-secondary transfer candidate, but the exact mismatch remains: the 4dc object is a positive total-mass count over composite rational common cores with an unknown physical selector, not a prime-modulus one-root bilinear exponential sum and not a mean-zero Gaussian coefficient family.

No adapter has been proved which turns `w_C(P,Q)` into a coefficient sequence satisfying the hypotheses while also removing the zero-frequency contribution.

```text
GAUSSIAN_SPARSE_MODULUS_LARGE_SIEVE_DIRECTLY_APPLICABLE=false,
BAIER_2026_MODULAR_SQRT_ENERGY_DIRECTLY_APPLICABLE=false,
MEAN_ZERO_GAUSSIAN_PHYSICAL_WEIGHT_PROVED=false.
```

---

## 6. Reuss transfer test from merged q10

Merged q10 marks Reuss, *Counting points on bilinear and trilinear hypersurfaces* (`arXiv:1502.07594`), as a high-priority transfer candidate because its bounds improve when the determinant / hyperdeterminant of an irreducible bilinear / nonsingular trilinear form is large.

The required transfer object would be an exact physical eliminant of one of the forms

```text
f(x1,x2;y1,y2)=0
```

with nonzero determinant, or

```text
f(x1,x2;y1,y2;z1,z2)=0
```

irreducible and nonsingular with nonzero Cayley hyperdeterminant, such that the determinant/hyperdeterminant carries a fresh fixed-power factor not already charged through `C`.

Stage14-4dc does **not** expose such an eliminant. Its universal algebraic relation is only

```text
P^2+Q^2=C0*R.                                      (6.1)
```

The rational cross determinants with the endpoint line are coprime to `C0` by the resultant-4 theorem, while the quadratic cross norms divisible by `C0` are algebraic consequences of the two already-charged root equations. Thus no new large determinant is available.

Moreover, (6.1) is a norm surface with the Gaussian multiplication parametrization

```text
C0=c1^2+c2^2,
R =r1^2+r2^2,
P=c1*r1-c2*r2,
Q=c1*r2+c2*r1,
```

so the ambient norm equation itself contains abundant integral families.

Therefore the q10 Reuss transfer test fails at the eliminant-construction step:

```text
REUSS_TRANSFER_TESTED=true,
REUSS_IRREDUCIBLE_BILINEAR_ELIMINANT_EXHIBITED=false,
REUSS_NONSINGULAR_TRILINEAR_ELIMINANT_EXHIBITED=false,
REUSS_FRESH_FIXED_POWER_DETERMINANT_EXHIBITED=false,
REUSS_DIRECTLY_APPLICABLE=false.
```

---

## 7. Generic determinant method

The physical restrictions are factorization, squarefree-cell, sign/orientation, interval and reciprocal-completion masks. They have not been converted into an additional fixed-degree algebraic equation cutting the Gaussian norm surface down to a smaller irreducible variety.

Consequently generic determinant-method bounds on

```text
P^2+Q^2=C0R
```

cannot distinguish the physical subset from the abundant Gaussian multiplicative population.

```text
GENERIC_DETERMINANT_METHOD_ON_NORM_SURFACE_DIRECTLY_APPLICABLE=false,
FIXED_DEGREE_JOINT_PHYSICAL_INCIDENCE_VARIETY_EXHIBITED=false.
```

---

## 8. Refined exact receiver

After all analytic transfer candidates above are separated off, the unsaved object is exactly the zero-frequency physical admissibility density.

For each `C~B^chi`, let

```text
A_C = {
  primitive (P,Q):
  C0 | P^2+Q^2,
  P*Q<=B^(1/2+o(1)),
  some divisor split P=a0U,Q=b0V admits every physical reciprocal mask
}.
```

A strict sub-square-root theorem is equivalent to

```text
sum_{C~B^chi} #A_C
 << B^(1/2-delta+o(1))
```

for some fixed `delta>0` uniformly over `5/24<=phi<=1/4`.

Define the narrower receiver

```text
SquareRootThetaQuarterGaussianNormDivisorSplitPhysicalAdmissibilityZeroFrequencyDensity.
```

This is an exact-arithmetic density problem, not a reason to wait for another generic H survey.

---

## 9. H verdict

```text
MAINLINE_H_COMPLETED=true,
MAINLINE_H_RESULT=NO_CERTIFIED_UNIFORM_POWER_SAVING,
CERTIFIED_MAINLINE_H_DELTA=0,
OFF_THE_SHELF_UNIFORM_POWER_SAVING_PROVED=false.
```

The H dependency itself is resolved:

```text
MAINLINE_BLOCKED_BY_H=false,
ADDITIONAL_MAINLINE_H_NEEDED=false.
```

No whole-family exponent change is certified:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

Next:

```text
Stage14-4dd
```

---

## Stage boundary

```text
STAGE14_4DH=COMPLETE_MAINLINE_H_APPLICABILITY_AUDIT_NO_CERTIFIED_UNIFORM_DELTA
MERGED_4DC_IMPORTED=true
MERGED_Q10_IMPORTED=true
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
REUSS_IRREDUCIBLE_BILINEAR_ELIMINANT_EXHIBITED=false
REUSS_NONSINGULAR_TRILINEAR_ELIMINANT_EXHIBITED=false
REUSS_FRESH_FIXED_POWER_DETERMINANT_EXHIBITED=false
REUSS_DIRECTLY_APPLICABLE=false
GENERIC_DETERMINANT_METHOD_ON_NORM_SURFACE_DIRECTLY_APPLICABLE=false
FIXED_DEGREE_JOINT_PHYSICAL_INCIDENCE_VARIETY_EXHIBITED=false
OFF_THE_SHELF_UNIFORM_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
REMAINING_RECEIVER=SquareRootThetaQuarterGaussianNormDivisorSplitPhysicalAdmissibilityZeroFrequencyDensity
NEXT=Stage14-4dd
```
