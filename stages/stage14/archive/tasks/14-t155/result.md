# Stage14-t155 — actual-scale Mitsui envelope on long-headroom lattice packets

## Status

`COMPLETE_ACTUAL_SCALE_MITSUI_LONG_ENVELOPE_AND_RECEIVER_CHANGE`

Consumes Stage14-t153/t154 and completed tH31 without recharging a theorem.

## 1. Use the theorem's actual scale, not the old sufficient safe label

Completed tH31 records the Kai/Mitsui modulus hypothesis in its native form. For `K=Q(i)`, modulus ideal `q=(d)` and cumulative upper scale `X`, the theorem is available inside a pseudopolynomial envelope

```text
N(q)=d^2 <= exp(sqrt(log X)/C_K)
```

for a fixed field constant `C_K>0`, with the possible exceptional real Hecke character retained.

The old t137/tH31 label

```text
d <= exp(c_safe*sqrt(log B))
```

was a convenient sufficient condition uniform over every long endpoint. It was not the definition of the theorem's maximal admissible packet.

For each actual long cofactor define

```text
X_z := X_U/N(z) = L_B*R(z),
KAI_ADMISSIBLE(z,d)
 :<=> d^2 <= exp(sqrt(log X_z)/C_K).
```

Because `R(z)>=B^theta`, cumulative subtraction between `L_B` and `X_z` is exactly the fixed-power-headroom situation audited positively in tH31.

Therefore every long packet satisfying `KAI_ADMISSIBLE(z,d)` obeys

```text
T_z >= B^(-o(1))*M_z,
```

uniformly with the possible Siegel secondary term retained. A fixed-power depletion cannot occur there.

```text
ACTUAL_SCALE_KAI_ENVELOPE_DEFINED=true
TH31_RECONSUMED_WITHOUT_RECHARGE=true
ACTUAL_SCALE_KAI_ADMISSIBLE_LONG_FIXED_POWER_DEPLETION_RULED_OUT=true
POSSIBLE_SIEGEL_ZERO_RETAINED=true
```

## 2. This genuinely refines the old beyond-safe label

The implication

```text
old safe label => KAI_ADMISSIBLE(z,d)
```

is already certified by tH31. The converse need not hold, because the native theorem condition depends on the actual cumulative upper scale `X_z`, while the old label was chosen uniformly from the lower Stage14 scale.

Hence the old receiver

```text
LongHeadroomBeyondMitsuiPseudopolynomialModulusFixedGaussianResiduePrimeOccupancyBias
```

was too coarse. It must be replaced by the subset where the actual theorem condition fails:

```text
KAI_INADMISSIBLE(z,d):
  d^2 > exp(sqrt(log X_z)/C_K).
```

No numerical value of `C_K` is asserted; this is a theorem-interface refinement, not an enlargement by an invented constant.

## 3. Combine with the t154 lattice split

The unresolved long branch is now the union of two exact mechanisms, both restricted to `KAI_INADMISSIBLE` packets.

### Sparse long

```text
N(z)<d^2,
O(1) actual cofactors,
one z_* localizable,
R_* >= q_d*B^(-o(1)),
KAI_INADMISSIBLE(z_*,d).
```

### Area long

```text
N(z)>=d^2,
M_N <= C*X_U/(q_d*d^2),
h*k0*q_d*d^2 <= B^(1/2+o(1)) on a principal shell,
KAI_INADMISSIBLE on the shell's actual upper scales.
```

The endpoint receivers from t152 are unchanged.

## 4. New minimal fixed-U receiver

```text
(A) SafeMitsuiSingleCofactorSubKaiExactResidueGroupNearFullPrimeOccupancy
OR
(B) SafeMitsuiGaussianLatticeAreaManyCofactorSubKaiPrimeOccupancy
OR
(C) BeyondMitsuiSingleCofactorExactResidueGroupNearFullPrimeOccupancyBias
OR
(D) BeyondMitsuiGaussianLatticeAreaManyCofactorEndpointPrimeOccupancyBias
OR
(E) ActualScaleKaiInadmissibleSparseLongSingleCofactorFixedGaussianResiduePrimeOccupancyBias
OR
(F) ActualScaleKaiInadmissibleAreaLongGaussianLatticeHarmonicPrimeOccupancyBias.
```

This is a material receiver change: every long packet that was merely outside the old uniform safe label but still satisfies the theorem at its own upper scale is now discharged.

No tH33 is opened. The positive theorem being used is exactly completed tH31; only its native scale parameter has been restored. A fresh tH would be justified only after the `KAI_INADMISSIBLE` sparse/area packets are converted into a materially new theorem family or averaging object.

```text
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=false
PREFERRED_RECEIVER=EndpointDoubleResidueOccupancyOrActualScaleKaiInadmissibleSparseAreaLongOccupancy
NEXT=Stage14-t156
```