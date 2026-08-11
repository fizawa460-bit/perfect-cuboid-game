# Stage14-s7-100 — fixed primitive product branch becomes one exact complementary-dilation completion support

## Status

`COMPLETE_FIXED_PRIMITIVE_PRODUCT_TO_ONE_DIMENSIONAL_COMPLEMENTARY_DILATION_PHYSICAL_COMPLETION_SUPPORT`

Consumes batch-local `Stage14-s7-99` and merged `Stage14-s7-89..98` on the same frozen heavy primitive-ray/agreement packet.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze the branch-(B) primitive product/orientation

From s7-99 freeze

```text
m=m0,
u=u0,
v=v0,
m0=u0*v0,
gcd(u0,v0)=1,
```

with polynomial complementary dilation `E` the only polynomial coordinate.

Merged s7-90 gives exactly

```text
n=E*u*v,
|Xr|=alpha*E*u^2,
|Yr|=beta*E*v^2,
```

for fixed positive packet coefficients `alpha,beta`.  Merged s7-87..89 gives

```text
h=d0*n.
```

Therefore on the frozen `(m0,u0,v0)` cell,

```text
n=m0*E,
|Xr|=(alpha*u0^2)*E,
|Yr|=(beta*v0^2)*E,
h=(d0*m0)*E.
```

Every moving root/radial quantity is thus a fixed packet coefficient times the single integer `E`.

```text
FIXED_M_BRANCH_N_LINEAR_IN_E=true
FIXED_M_BRANCH_XR_LINEAR_IN_E=true
FIXED_M_BRANCH_YR_LINEAR_IN_E=true
FIXED_M_BRANCH_H_LINEAR_IN_E=true
```

## 2. Projective root ratio is frozen

The root ratio is independent of `E`:

```text
|Xr|/|Yr|
 = (alpha/beta)*(u0/v0)^2.
```

Hence no projective-ratio entropy remains on this branch.  The transported root-size conditions become one ordinary intersection of intervals for the scalar dilation `E`; any endpoint geometry already charged in merged 4fi/s7-92 is not charged again.

After those deterministic size filters, define

```text
C_fixm(E) in {0,1}
```

to be the exact Boolean that the resulting fixed-coefficient root/radial tuple admits the retained primitive/canonical/root-origin/reverse/post-column completion.

The branch support is exactly

```text
A_fixm(E)=1_{E in I_phys} * C_fixm(E).
```

Fixed `E` has only `B^o(1)` reverse completion multiplicity by merged 4eq; this does not imply `C_fixm(E)=1`.

```text
FIXED_M_PROJECTIVE_ROOT_RATIO_CONSTANT=true
FIXED_M_INNER_UNITARY_SELECTOR_EXHAUSTED=true
FIXED_M_REVERSE_COMPLETION_MULTIPLICITY=Bo1
FIXED_M_REVERSE_COMPLETION_EXISTENCE_AUTOMATIC=false
FIXED_M_PHYSICAL_COMPLETION_BOOLEAN=C_fixm_of_E
```

## 3. Exact one-dimensional receiver on this branch

A surviving branch-(B) cell therefore requires

```text
#{E : E in I_phys, C_fixm(E)=1} >= B^(mu-o(1))
```

for one frozen primitive product/orientation.  The old unitary-divisor language is no longer the minimal description of this realization: after fixing `(m0,u0,v0)`, there is no moving divisor choice at all.

This is an explicit realization of the existing `PolynomialComplementaryDilationFixedPrimitiveProductCanonicalReverseOuterOccupancy` receiver, not yet a new arithmetic theorem class.  The next stage should decompose the fixed-E branch by primitive-factor scale and compare its endpoint realization with the genuinely two-sided unitary-partition realization.

```text
ONE_DIMENSIONAL_FIXED_PRIMITIVE_PRODUCT_DILATION_SUPPORT_EXPLICIT=true
RECEIVER_MATERIALLY_CHANGED=false
S7_100_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
```

## Boundary

```text
STAGE14_S7_100=COMPLETE_FIXED_PRIMITIVE_PRODUCT_TO_ONE_DIMENSIONAL_COMPLEMENTARY_DILATION_PHYSICAL_COMPLETION_SUPPORT
FIXED_M_BRANCH_N_LINEAR_IN_E=true
FIXED_M_BRANCH_XR_LINEAR_IN_E=true
FIXED_M_BRANCH_YR_LINEAR_IN_E=true
FIXED_M_PROJECTIVE_ROOT_RATIO_CONSTANT=true
ONE_DIMENSIONAL_FIXED_PRIMITIVE_PRODUCT_DILATION_SUPPORT_EXPLICIT=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_100_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-101
```
