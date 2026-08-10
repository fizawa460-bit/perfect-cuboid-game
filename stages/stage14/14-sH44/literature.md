# Stage14-sH44 theorem applicability note

Canonical target after merged `Stage14-4dc` and merged `Stage14-q10`:

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving
```

The exact counting object is

```text
sum_{C~B^chi}
  sum_{primitive (P,Q), C0|P^2+Q^2, P*Q<=B^(1/2+o(1))}
    1_physical_completion(C,P,Q).
```

Fixed `(C,P,Q)` has only `B^o(1)` possible physical completions, but no checked theorem currently proves that the completable subset is power-sparse.

## 1. Determinant method

The earlier Stage14 reciprocal-Edwards audit certified a degree-four Segre determinant estimate for fixed `lambda`.  That remains a valid fixed-parameter theorem but is not a direct theorem on the 4dc Gaussian product variables.

The physical `lambda=4M/N` moves with the completion.  No charged-once average over the moving `lambda` family is proved.  In addition, the full Cayley/common core satisfies

```text
lambda == +/-4 mod p^e
```

for every active `p^e` in `C/B^o(1)`, so that core is singular-reduction support for the reciprocal curve and cannot be reused as a fresh good-reduction determinant modulus.

```text
FIXED_LAMBDA_DETERMINANT_METHOD_APPLICABLE=true
GENERIC_DETERMINANT_METHOD_DIRECT_4DC_ADAPTER=false
MOVING_PHYSICAL_LAMBDA_AVERAGE_CONTROLLED=false
COMMON_CORE_REUSABLE_AS_GOOD_REDUCTION_DETERMINANT_MODULUS=false
```

## 2. Reuss bilinear/trilinear determinant transfer

Merged q10 identifies Reuss's determinant-sensitive integer-point bounds for bilinear/trilinear forms as a high-priority transfer candidate.  Those results become relevant if the exact physical completion can be eliminated to an irreducible bilinear form or a nonsingular trilinear form whose determinant/hyperdeterminant carries a fresh fixed-power factor.

No such eliminant has yet been proved.  In fact merged 4dc gives the transverse resultant

```text
Res(t^2+1,t^2-1)=4
```

and proves that the obvious cross determinant and cross sum are coprime to the odd full good core.  Thus the easiest candidate for a fresh determinant does not carry `C`.

```text
REUSS_BILINEAR_TRILINEAR_THEOREM_RELEVANT_AFTER_ELIMINANT=true
REUSS_LARGE_DETERMINANT_ELIMINANT_PROVED=false
REUSS_DIRECT_ADAPTER=false
```

## 3. Equidistribution of quadratic roots

Results on equidistribution of roots of quadratic congruences are not a direct fit.  Here the local root is one of the two roots of

```text
rho^2=-1 mod p^e,
```

and all CRT root choices together have only `B^o(1)` entropy.  The polynomial mass comes from integer lifts on the root line and from the positive physical-completion indicator.  Improving root-label discrepancy cannot remove the expected `1/C` principal density.

```text
QUADRATIC_ROOT_EQUIDISTRIBUTION_DIRECT_ADAPTER=false
ROOT_DISTRIBUTION_PRINCIPAL_TERM_REMAINS=true
```

## 4. Modular-square-root energy

Recent modular-square-root energy estimates obtain cancellation from roots of moving residues, schematically

```text
k^2 == j*m (mod r)
```

with `m` moving through a substantial support.  The 4dc object instead has a fixed local root of `-1`; its moving variables are integer lifts `(P,Q)` satisfying `P=rho Q (mod C0)`.

No exact adapter to that moving-residue coefficient space preserves the reciprocal physical completion and charged-once common-core count.

```text
MODULAR_SQUARE_ROOT_ENERGY_DIRECT_ADAPTER=false
```

## 5. Multiplicative-congruence energy

Strong multiplicative-energy results control box solutions of congruences such as

```text
x1*x2 == x3*x4 (mod q)
```

and their character-moment errors around expected modular density.

The 4dc receiver is not currently a single such congruence in independent weighted boxes.  More fundamentally, the Gaussian line expected density already contributes exponent `1/2`; an error-term theorem around that density cannot remove the positive principal term.

```text
MULTIPLICATIVE_ENERGY_DIRECT_ADAPTER=false
MULTIPLICATIVE_ENERGY_PRINCIPAL_TERM_REMOVES_SQRT_BARRIER=false
```

## 6. Kloosterman-fraction transfer tests

Bettin--Chandee and newer improvements, including Dong--Robles--Zeindler, treat genuine bilinear/trilinear inverse-fraction kernels with moving denominator variables and flexible coefficient sequences.  Wright's partially-fixed-modulus refinement still retains a genuine moving denominator factor.

Merged q10 correctly marks Dong--Robles--Zeindler as a high-priority analytic candidate **after** an exact Fourier/divisor-switch bridge from the physical completion count to an inverse-fraction kernel.

No such identity is currently proved for

```text
sum_{C~B^chi}
  sum_{primitive (P,Q), C0|P^2+Q^2}
    1_physical_completion(C,P,Q)
```

while preserving the squarefree-cell, positivity, interval, global-primitivity, reciprocal, Cayley-orientation, and X13 reconstruction masks.

```text
DONG_ROBLES_ZEINDLER_RELEVANT_AFTER_INVERSE_FRACTION_ADAPTER=true
INVERSE_FRACTION_PHYSICAL_COMPLETION_ADAPTER_PROVED=false
KLOOSTERMAN_FRACTION_DIRECT_ADAPTER=false
PARTIALLY_FIXED_DENOMINATOR_DIRECT_ADAPTER=false
```

## 7. Fixed-modulus complete Kloosterman bilinear forms

Modern fixed-modulus results give genuine power savings for bilinear forms already expressed in complete Kloosterman sums

```text
S(a*m,n;C)
```

in suitable length ranges.  The 4dc receiver is not currently a complete Kloosterman form; it is a positive count of Gaussian root-line lifts carrying a physical completion indicator.

Before such a theorem can be invoked one must prove a Poisson/completion identity

```text
1_physical_completion on Gaussian root-line lifts
 -> principal term + mean-zero weighted complete Kloosterman family mod C,
```

verify transformed lengths and coefficient norms, preserve every physical mask, and avoid a second charge of `C`.

```text
BLOMER_PASCADI_RELEVANT_AFTER_PHYSICAL_COMPLETION_ADAPTER=true
FIXED_MODULUS_COMPLETE_KLOOSTERMAN_ADAPTER_PROVED=false
COMPLETE_KLOOSTERMAN_BILINEAR_THEOREM_DIRECTLY_APPLICABLE=false
```

No fixed-modulus Kloosterman saving is imported before that adapter exists.

## 8. Relation to t80/t81/t82/tH23

The t route fixes a projective `U` before its hard analytic sum and reaches a fixed-divisor one-frequency inverse-fraction/Kloosterman-type coefficient space.  The 4dc s/mainline object instead sums the moving Gaussian product pair `(P,Q)` and recovers its `(a0,b0,U,V)` split divisor-many afterward.

These quantifier orders are not identified by any proved charged-once bijection.  The merged tH23 conclusion that a physical completion/Poisson adapter is missing is diagnostic context only.

```text
T80_T81_T82_COEFFICIENT_SPACE_IDENTICAL_TO_SH44=false
T80_CROSS_PROMOTED_TO_SH44=false
T81_CROSS_PROMOTED_TO_SH44=false
T82_CROSS_PROMOTED_TO_SH44=false
TH23_CROSS_PROMOTED_TO_SH44=false
```

## 9. Final applicability verdict

No checked theorem directly proves

```text
sum_C I_C^phys << B^(1/2-delta+o(1))
```

for any certified fixed `delta>0` with all 4dc masks retained.

The minimal remaining theorem-sized object is

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreBadReductionGaussianProductPhysicalCompletionDispersion
```

and the three concrete routes are:

```text
A. exact bilinear/trilinear eliminant with a fresh large determinant;
B. exact inverse-fraction kernel with controlled physical weights;
C. principal-term subtraction plus mean-zero completed Kloosterman/dispersion identity.
```

```text
OFF_THE_SHELF_GAUSSIAN_PRODUCT_POWER_SAVING_PROVED=false
CERTIFIED_GAUSSIAN_PRODUCT_DELTA=0
```
