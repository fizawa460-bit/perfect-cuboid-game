# Stage14-s7-104 — fixed primitive product: discharge the known squarefree-kernel mask and isolate residual E-local/completion deficits

## Status

`COMPLETE_FIXED_PRIMITIVE_PRODUCT_KNOWN_E_LOCAL_MASK_DISCHARGE_AND_RECEIVER_CHANGE`

Consumes batch-local `Stage14-s7-102/103`, merged `Stage14-s7-100`, merged `Stage14-4fk/4fr/4fs`, and merged `Stage14-Work-bvX34`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. One-dimensional polynomial-E fixed-product branch

Freeze exact primitive data

```text
(m,u,v)=(m0,u0,v0),
m0=u0*v0,
gcd(u0,v0)=1,
```

as in merged s7-100. Then

```text
n=m0*E,
|Xr|=(alpha*u0^2)*E,
|Yr|=(beta*v0^2)*E,
h=(d0*m0)*E,
|Xr|/|Yr|=(alpha/beta)*(u0/v0)^2.
```

Thus all bare archimedean root/radial restrictions are interval restrictions on the one scalar `E`. Freeze one nonempty dyadic/chamber interval cell

```text
I_E=(E_-,E_+],
H_E=#(I_E cap Z)=B^(lambda_E+o(1)).
```

A polynomially heavy realization has `lambda_E>0`.

The exact bare selector from merged 4fr is

```text
B_fix(E)=1{E in I_E}*m_E(E),
```

and the physical selector is

```text
A_fix(E)=B_fix(E)*C_fix(E),
```

with `C_fix(E)` the retained canonical/reverse completion Boolean.

## 2. Extract the known squarefree-kernel local mask

Merged s7-93/4fk records the explicit complementary-dilation condition

```text
m_K(E):=1{gcd(sqf(E),K_Z)=1}.
```

Because `m_E` is the conjunction of all proven E-local predicates, write exactly

```text
m_E(E)=m_K(E)*m_E^res(E),
```

where `m_E^res` is the conjunction of the remaining E-local predicates, if any. This notation asserts no independence.

```text
KNOWN_E_LOCAL_SQUAREFREE_KERNEL_MASK_EXTRACTED=true
E_LOCAL_RESIDUAL_MASK_DEFINED=true
E_LOCAL_MASK_FACTORIZATION_USES_INDEPENDENCE=false
```

## 3. The known squarefree-kernel coprimality mask cannot create a fixed-power loss

Put

```text
Q=rad(K_Z).
```

The frozen coefficient `K_Z` has polynomial Stage14 height, hence `Q=B^O(1)`. Every integer `E` with

```text
gcd(E,Q)=1
```

satisfies `m_K(E)=1`. Therefore, on any integer interval of length `H_E`,

```text
#{E in I_E : m_K(E)=1}
 >= #{E in I_E : gcd(E,Q)=1}
 = H_E*phi(Q)/Q + O(tau(Q)).
```

For polynomial `Q`,

```text
phi(Q)/Q=B^(-o(1)),
tau(Q)=B^o(1).
```

Hence if `H_E=B^(lambda_E+o(1))` with `lambda_E>0`,

```text
#{E in I_E : m_K(E)=1}=B^(lambda_E+o(1)).
```

So the explicit `gcd(sqf(E),K_Z)=1` condition alone has zero fixed-power deficit on this one-dimensional polynomial interval.

```text
KNOWN_SQUAREFREE_KERNEL_MASK_FIXED_POWER_DEFICIT=0
KNOWN_SQUAREFREE_KERNEL_MASK_CANNOT_BE_SOLE_HEAVY_OBSTRUCTION=true
GENERIC_SQUAREFREE_DENSITY_RECHARGED=false
```

## 4. Residual nested support on the fixed-product branch

Define

```text
B_res(E)=1{E in I_E}*m_K(E)*m_E^res(E),
A_fix(E)=B_res(E)*C_fix(E).
```

Write

```text
#supp(B_res)=B^(sigma_fix+o(1)),
#supp(A_fix)=B^(tau_fix+o(1)),
delta_fix=sigma_fix-tau_fix>=0.
```

Heavy survival requires

```text
sigma_fix-delta_fix=tau_fix>=mu.
```

Because `m_K` itself has full scalar exponent, any fixed-power loss on this realization must be carried by

```text
(i) the residual E-local mask m_E^res,
(ii) the conditional physical-completion Boolean C_fix,
```

or by their exact conjunction. No independence or multiplication of their deficits is asserted.

## 5. Material heavy receiver change

Together with s7-103, the four s realizations are now minimized to

```text
(A) fixed-E endpoint:
    one-dimensional conditional physical-completion support;

(B) fixed-E two-sided polynomial:
    bare short-unitary partition shadow versus conditional physical-completion deficit;

(C) polynomial-E fixed primitive product:
    residual E-local mask support versus conditional physical-completion deficit,
    with the explicit squarefree-kernel gcd mask discharged at fixed-power level;

(D) polynomial-E polynomial primitive product:
    outer-pair bare unitary-existence shadow versus conditional physical-completion deficit.
```

Thus the receiver materially changes to

```text
FixedComplementaryDilationFixedPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport
OR
FixedComplementaryDilationTwoSidedPolynomialBareShortUnitaryShadowVersusConditionalPhysicalCompletionDeficit
OR
PolynomialComplementaryDilationFixedPrimitiveProductResidualELocalMaskVersusConditionalPhysicalCompletionDeficit
OR
PolynomialComplementaryDilationPolynomialPrimitiveProductBareUnitaryOuterPairShadowVersusConditionalPhysicalCompletionDeficit.
```

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedComplementaryDilationFixedPrimitiveEndpointOneDimensionalConditionalPhysicalCompletionSupport_OR_FixedComplementaryDilationTwoSidedPolynomialBareShortUnitaryShadowVersusConditionalPhysicalCompletionDeficit_OR_PolynomialComplementaryDilationFixedPrimitiveProductResidualELocalMaskVersusConditionalPhysicalCompletionDeficit_OR_PolynomialComplementaryDilationPolynomialPrimitiveProductBareUnitaryOuterPairShadowVersusConditionalPhysicalCompletionDeficit
RECEIVER_MATERIALLY_CHANGED=true
```

## 6. H and Work decisions

No new sH is opened. The remaining completion Booleans and `m_E^res` must be opened internally before a theorem target is stable. This stage reaches the normal `s7-104` component of the merged Work-bvX34 revisit condition.

```text
S7_104_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
WORK_BVX34_REVISIT_TRIGGER_S7_104_REACHED=true
```

## Boundary

```text
STAGE14_S7_104=COMPLETE_FIXED_PRIMITIVE_PRODUCT_KNOWN_E_LOCAL_MASK_DISCHARGE_AND_RECEIVER_CHANGE
FIXED_E_ENDPOINT_BARE_UNITARY_FIXED_POWER_SAVING=false
KNOWN_SQUAREFREE_KERNEL_MASK_FIXED_POWER_DEFICIT=0
POLYNOMIAL_E_FIXED_PRODUCT_RESIDUAL_E_LOCAL_MASK_RETAINS=true
POLYNOMIAL_E_FIXED_PRODUCT_CONDITIONAL_COMPLETION_RETAINS=true
WORK_BVX34_REVISIT_TRIGGER_S7_104_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_104_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-105
```
