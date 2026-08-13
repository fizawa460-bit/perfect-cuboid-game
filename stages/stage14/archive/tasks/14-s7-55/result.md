# Stage14-s7-55 — pairwise joint-density defect versus centered inverse-fraction error

## Status

`COMPLETE_PAIRWISE_JOINT_DENSITY_DEFECT_VS_CENTERED_ERROR_SPLIT`

Consumes current main through merged `Stage14-s7-54`, merged `Stage14-4dl`, merged `Stage14-s7-50`, and merged `Stage14-X15`.

The entering theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Stage14-s7-54 proves that the three pairwise branches `(+,-)`, `(+ ,k)`, `(-,k)` are fixed-power finite-fiber coordinate realizations of the same primitive Pythagorean two-projection compatibility mass. Therefore it is enough to analyze one representative pair; choose `(+,-)`.

## 1. Representative pairwise covariance

Let the surviving interior full-conductor cell be `Omega`. Write

```text
W_+, W_- in {0,1},
mu_+=E_Omega W_+,
mu_-=E_Omega W_-.
```

The pairwise covariance is exactly

```text
Gamma_{+-}
 = E_Omega[W_+W_-] - mu_+mu_-.
```

Define the joint occupancy density

```text
mu_{+-}:=E_Omega[W_+W_-].
```

Then

```text
Gamma_{+-}=mu_{+-}-mu_+mu_-.
```

This is an exact identity before any Fourier expansion.

## 2. Why s7-49/50 centered error is only part of the pairwise problem

Merged s7-49 expands the norm-root condition locally as

```text
1_{C_*|m^2+n^2}
 = local_zero_mode + centered_nonzero_frequency_kernel.
```

Merged s7-50 then proves a fixed-power saving on every conductor-loss stratum and confines possible oscillatory saturation to the full-conductor endpoint.

However, when a second physical selector `W_-` is retained, multiplying the above decomposition by `W_-` yields schematically

```text
mu_{+-}
 = pair_local_zero_mode
 + pair_centered_error.
```

Subtracting `mu_+mu_-` gives

```text
boxed:
Gamma_{+-}
 = [pair_local_zero_mode - mu_+mu_-]
   + pair_centered_error.                       (2.1)
```

The first bracket is a **pairwise joint-density defect**. It is not the s7-49 nonzero-frequency error. A theorem controlling only the centered inverse-fraction/Kloosterman error leaves this principal pair-density defect untouched.

Therefore

```text
PAIRWISE_COVARIANCE_EQUALS_S7_49_CENTERED_ERROR=false
PAIRWISE_PRINCIPAL_JOINT_DENSITY_DEFECT_PRESENT=true
CENTERED_KLOOSTERMAN_ERROR_ALONE_SUFFICIENT=false.
```

## 3. Pairwise fixed-power deficit split

Write

```text
Delta_pair := pair_local_zero_mode - mu_+mu_-,
Err_pair   := pair_centered_error.
```

Then

```text
Gamma_{+-}=Delta_pair+Err_pair.
```

For any fixed `delta>0`, if both

```text
|Delta_pair| <= B^(-delta+o(1)),
|Err_pair|   <= B^(-delta+o(1)),
```

then the pairwise contribution is strict sub-square-root after multiplying by the charged-once `B^(1/2+o(1))` ambient mass.

Hence square-root pairwise saturation requires at least one of

```text
PAIR_JOINT_DENSITY_BRANCH:
  |Delta_pair| = B^(-o(1));

PAIR_CENTERED_ERROR_BRANCH:
  |Err_pair| = B^(-o(1)).
```

This split is deterministic and exact.

## 4. Three pairwise branches still count only once

By merged s7-54, the pairs

```text
(+,-), (+,k), (-,k)
```

are fixed-power finite-fiber coordinate versions of the same primitive Pythagorean two-projection physical packet. Thus the pairwise joint-density and centered-error branches above must not be repeated three times as independent saving sources.

```text
PAIRWISE_REPRESENTATIVE_PAIR=PLUS_MINUS
PAIRWISE_BRANCHES_POWER_EQUIVALENT=true
PAIRWISE_FIXED_POWER_BRANCH_COUNT=1
PAIRWISE_DOUBLE_CHARGE_ALLOWED=false.
```

## 5. Relation to 4dl near-max correlation

Merged 4dl localizes pairwise square-root saturation to correlation coefficient

```text
r_{ij}=B^(-o(1)).
```

Equation (2.1) refines what can create such near-maximal correlation in s-coordinates: either the conditional joint zero-mode density differs from the product of marginals at main-term scale, or a full-conductor centered inverse-fraction error remains at main-term scale (or both).

No contradiction exists between these descriptions.

## 6. H decision

No new H is opened at s7-55. The pairwise centered-error branch is already theorem-ready only after retaining the second physical mask, while the pairwise joint-density branch is a deterministic conditional-density problem. They should first be separated further internally.

```text
S7_55_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SH50_REOPENED=false.
```

## 7. Next receiver

The pairwise branch is now the union of exactly two representative receivers:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanPairwiseConditionalJointDensityDefect
```

and

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanPairwiseMaskedCenteredInverseFractionError.
```

The connected third-cumulant receiver from s7-53 remains unchanged.

`Stage14-s7-56` should attack the joint-density branch first: condition on one selector and test whether the second selector's conditional mean has a fixed-power deficit from its marginal mean on the near-max pairwise cells. Only after that should a new H be considered for the masked centered-error branch.

## Stage boundary

```text
STAGE14_S7_55=COMPLETE_PAIRWISE_JOINT_DENSITY_DEFECT_VS_CENTERED_ERROR_SPLIT
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PAIRWISE_COVARIANCE_EQUALS_S7_49_CENTERED_ERROR=false
PAIRWISE_PRINCIPAL_JOINT_DENSITY_DEFECT_PRESENT=true
CENTERED_KLOOSTERMAN_ERROR_ALONE_SUFFICIENT=false
PAIRWISE_REPRESENTATIVE_PAIR=PLUS_MINUS
PAIRWISE_BRANCHES_POWER_EQUIVALENT=true
PAIRWISE_FIXED_POWER_BRANCH_COUNT=1
PAIRWISE_DOUBLE_CHARGE_ALLOWED=false
S7_55_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-56
```
