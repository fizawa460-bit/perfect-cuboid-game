# Stage14-t157 — collapse Kai-inadmissible long survivors to one super-Kai individual-residue theorem target

## Status

`COMPLETE_SUPER_KAI_LONG_POINTWISE_THEOREM_FREEZE_AND_RECEIVER_CHANGE`

Consumes Stage14-t156/t155/t154 and the exact fixed-residue prime incidence frozen since t135.

## 1. Sparse and area differ only on the cofactor side

For every actual cofactor `z`, define

```text
X_z=X_U/N(z),
T_z=#{canonical split Gaussian primes pi:
      pi==beta_* (mod d),
      fixed strict D4 sector,
      L_B<N(pi)<=X_z},
M_z=1/q_d * #{unrestricted canonical split primes in the same sector and interval}.
```

The sparse branch has only `O(1)` actual cofactors and therefore localizes to one `z_*`.  The area branch may contain many cofactors, but its physical count and principal baseline are still nonnegative sums

```text
T_N=sum_z T_z,
M_N=sum_z M_z.
```

Thus any theorem giving the pointwise uniform ratio

```text
T_z >= B^(-o(1))*M_z
```

for every admissible actual cofactor immediately rules out fixed-power depletion after summing over either sparse or area packets.  No cofactor averaging theorem is necessary once such a pointwise prime theorem is available.

```text
SPARSE_AREA_LONG_SHARE_SAME_POINTWISE_PRIME_THEOREM=true
COFACTOR_LATTICE_DIFFERENCE_IRRELEVANT_AFTER_POINTWISE_LOWER_RATIO=true
```

## 2. Exact common unresolved theorem family

Merged t155 already discharges every actual cofactor satisfying

```text
d^2 <= exp(sqrt(log X_z)/C_K).
```

Stage14-t156 proves that every remaining long principal survivor satisfies

```text
d^2 > exp(sqrt(log X_z)/C_K),
log d >= c_{K,theta} sqrt(log B),
d=B^o(1),
X_z/L_B>=B^theta.
```

The prime-side unresolved object is therefore exactly

```text
SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio.
```

The sparse compatibility cap `d^3<=B^(1/2+o(1))` and area cap `d^5<=B^(1/2+o(1))` may be retained as extra target data, but they do not define different theorem species.

## 3. Why this is materially narrower than tH30

Completed tH30 audited the full fixed-residue reciprocal hyperbola while cofactor and prime ranges were still coupled.  The present target has removed that geometry from the theorem question:

- one actual upper norm `X_z` is frozen;
- the interval has fixed-power multiplicative headroom `X_z/L_B>=B^theta`;
- one exact ordinary Gaussian residue `beta_* mod d` is frozen;
- one fixed strict canonical sector is frozen;
- the modulus is explicitly outside tH31's actual-scale Kai envelope;
- the selector is fixed-U hosted and `d=B^o(1)`.

Hence a fresh external audit is justified even though tH30 already identified individual-modulus bias as the broad obstruction.

```text
TH33_TARGET_MATERIALLY_NARROWER_THAN_TH30=true
```

## 4. Freeze tH33

The immutable target is

```text
stages/stage14/14-t157/th33-target.md
```

with requested object

```text
SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio.
```

No tH33 result is executed in this stage.  Per the common batch contract, the material receiver change itself ends the ordinary batch before another theorem audit is charged.

## 5. New minimal fixed-U receiver

The endpoint branches from t152 remain unchanged.  The two long labels from t155 collapse to a single theorem family:

```text
(A) SafeMitsuiSingleCofactorSubKaiExactResidueGroupNearFullPrimeOccupancy
OR
(B) SafeMitsuiGaussianLatticeAreaManyCofactorSubKaiPrimeOccupancy
OR
(C) BeyondMitsuiSingleCofactorExactResidueGroupNearFullPrimeOccupancyBias
OR
(D) BeyondMitsuiGaussianLatticeAreaManyCofactorEndpointPrimeOccupancyBias
OR
(E) SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio.
```

This is a material receiver change.

```text
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=true
T_ROUTE_H_REQUEST=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio
T_ROUTE_H_TARGET=stages/stage14/14-t157/th33-target.md
T_ROUTE_H_BLOCKING=false
TH33_NEEDED=true
TH33_EXECUTED=false
NEXT=Stage14-tH33
```
