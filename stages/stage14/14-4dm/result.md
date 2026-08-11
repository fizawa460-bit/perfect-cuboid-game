# Stage14-4dm — sign-sensitive common pairwise covariance and zero/centered split

## Status

`COMPLETE_COMMON_PAIRWISE_POSITIVE_EXCESS_ZERO_MODE_AND_CENTERED_INVERSE_FRACTION_SPLIT`

Consumes merged `Stage14-4dl`, merged `Stage14-s7-54`, merged `Stage14-s7-49`, merged `Stage14-s7-50`, and merged `Stage14-X15` on latest main.

The whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Stage14-4dl localized any pairwise square-root obstruction to fixed-power near-maximal correlation. Merged s7-54 then proves that the three pairwise projections `(+,-)`, `(+,k)`, and `(-,k)` are finite-fiber coordinate views of one common two-projection compatibility mass. Stage14-4dm now performs the sign-sensitive upper-bound reduction and identifies the exact zero-frequency piece inside that common pairwise receiver.

## 1. Only positive pairwise excess is an upper-bound obstruction

On a full-conductor interior conditioning cell `Omega`, keep the binary selectors

```text
W_+, W_-, W_k in {0,1},
mu_j=E_Omega W_j,
X_j=W_j-mu_j,
Gamma_ij=E_Omega X_i X_j,
Kappa_3=E_Omega X_+X_-X_k.
```

Merged s7-53 gives exactly

```text
E[W_+W_-W_k]
 = mu_+mu_-mu_k
 + mu_k Gamma_{+-}
 + mu_- Gamma_{+k}
 + mu_+ Gamma_{-k}
 + Kappa_3.
```

Since all `mu_j>=0`, for an upper bound we may replace each signed term by its positive part:

```text
E[W_+W_-W_k]
 <= mu_+mu_-mu_k
  + mu_k Gamma_{+-}^+
  + mu_- Gamma_{+k}^+
  + mu_+ Gamma_{-k}^+
  + Kappa_3^+,
```

where `x^+=max(x,0)`.

Therefore negative pairwise covariance is not an obstruction to a strict upper bound. It is a potentially helpful anti-correlation and must not be charged as a positive exceptional family.

```text
NEGATIVE_PAIRWISE_COVARIANCE_IS_UPPER_BOUND_OBSTRUCTION=false
PAIRWISE_UPPER_BOUND_OBSTRUCTION_USES_POSITIVE_PART_ONLY=true
CONNECTED_TRIPLE_UPPER_BOUND_OBSTRUCTION_USES_POSITIVE_PART_ONLY=true
```

## 2. Positive pairwise excess requires dense pairwise physical intersection

For each pair `(i,j)`, let

```text
p_ij := E_Omega[W_i W_j].
```

Because

```text
Gamma_ij = p_ij-mu_i mu_j,
```

and `mu_i mu_j>=0`,

```text
0 <= Gamma_ij^+ <= p_ij.
```

Hence on any fixed-power joint-density deficit stratum

```text
p_ij <= B^(-delta+o(1)),
delta>0,
```

the positive pairwise covariance contribution is at most

```text
B^(1/2-delta+o(1))
```

after the charged-once ambient quarter-pair mass is summed.

Thus a positive pairwise square-root obstruction requires

```text
p_ij=B^(-o(1))
```

for at least one pair.

Merged s7-54 identifies all three pairs as power-equivalent coordinate views of one common two-projection physical compatibility mass, so they cannot be multiplied or counted as three independent dense receivers.

```text
POSITIVE_PAIRWISE_FIXED_POWER_JOINT_DENSITY_DEFICIT_STRICT_SUBSQRT=true
POSITIVE_PAIRWISE_SQRT_OBSTRUCTION_REQUIRES_JOINT_DENSITY=Bo0=true
PAIRWISE_BRANCHES_POWER_EQUIVALENT_IMPORTED=true
PAIRWISE_BRANCH_COUNT_AT_FIXED_POWER=1
```

## 3. Canonical `(+,-)` coordinate and exact rootline split

By merged s7-54 we may choose `(+,-)` as the canonical pair without loss at fixed-power scale.

Use the merged s7-49 rotated pair

```text
m=D+A,
n=D-A,
```

and freeze one full-conductor Gaussian root cell

```text
C_*=B^(chi+o(1)),
1/6<=chi<=1/4,
rho^2=-1 mod C_*.
```

Let

```text
R_rho(m,n):=1_{m == rho*n (mod C_*)}.
```

Orthogonality gives exactly

```text
R_rho(m,n)
 = 1/C_* + K_rho(m,n),
```

with

```text
K_rho(m,n)
 = (1/C_*) sum_{0!=h mod C_*} e_{C_*}(h(m-rho*n)),
```

and `K_rho` has zero mean in the complete residue variable.

Separate the plus physical selector as

```text
W_+ = A_+ * R_rho,
```

where `A_+` retains all non-rootline plus-side requirements: balanced/squarefree `(C_*,S,T)` factorization data, pairwise-separation, reciprocal completion, endpoint-small and orientation masks. Let

```text
B_- := W_-.
```

No physical filter is removed by this notation.

## 4. Exact pairwise covariance decomposition

For any cell probability/normalized counting measure, covariance is bilinear. Therefore

```text
Gamma_{+-}
 = Cov(A_+ R_rho, B_-)
 = (1/C_*) Cov(A_+,B_-)
   + Cov(A_+ K_rho,B_-).                    (4.1)
```

This identity is exact.

It proves that the common pairwise covariance receiver is **not** merely the s7-49/s7-50 inverse-fraction oscillatory error. It has two pieces:

```text
PAIRWISE_ZERO_MODE_COFATOR_COVARIANCE
  := (1/C_*) Cov(A_+,B_-),

PAIRWISE_CENTERED_INVERSE_FRACTION_COVARIANCE
  := Cov(A_+K_rho,B_-).
```

(The spelling `COFATOR` in the marker below is avoided; the canonical name is `COFACTOR`.)

By `max(x+y,0)<=x^+ + y^+`,

```text
Gamma_{+-}^+
 <= [(1/C_*) Cov(A_+,B_-)]^+
  + [Cov(A_+K_rho,B_-)]^+.                 (4.2)
```

Hence any positive pairwise square-root obstruction must survive in at least one of those two components.

```text
COMMON_PAIRWISE_COVARIANCE_ZERO_CENTERED_SPLIT_PROVED=true
PAIRWISE_RECEIVER_EQUALS_ONLY_INVERSE_FRACTION_ERROR=false
PAIRWISE_ZERO_MODE_COFACTOR_COVARIANCE_REMAINS=true
PAIRWISE_CENTERED_INVERSE_FRACTION_COVARIANCE_REMAINS=true
```

## 5. The zero-mode pairwise piece still has square-root ledger

The zero-frequency density contributes

```text
1/C_* = B^(-chi+o(1)).
```

while the dyadic `C_*` family has `B^(chi+o(1))` support. As in merged s7-49, these cancel at fixed-power scale. The remaining `(A_+,B_-)` covariance is a bounded physical coefficient on a charged-once `1/2` ambient coordinate system.

Therefore no deterministic fixed-power saving follows merely from extracting the rootline zero mode:

```text
PAIRWISE_ZERO_MODE_LEDGER_EXPONENT=1/2
PAIRWISE_ZERO_MODE_EXTRACTION_STRICT_SUBSQRT=false
```

If the normalized positive cofactor covariance has a fixed-power deficit `B^-delta`, that stratum is strict sub-square-root by the same density-localization principle as 4dj/4dl. But a `B^-o(1)` cofactor covariance remains possible from current identities.

## 6. The centered piece is the full-conductor inverse-fraction family with a physical coefficient

Merged s7-49 gives on the product side

```text
P_-=mn,
n == P_- * inverse(m) (mod C_*),
```

so each nonzero-frequency phase in `K_rho` becomes

```text
e_{C_*}(h*m-h*rho*P_-*inverse(m)).
```

Merged s7-50 removes all fixed-power conductor loss; square-root saturation is confined to

```text
q=C_* B^o(1),
gcd(h0,q)=1.
```

Thus the second term in (4.1) is exactly a **physically weighted full-conductor inverse-fraction covariance**. The coefficient `A_+ B_-`/its centered form is mandatory; it cannot be replaced by an unweighted Kloosterman sum.

```text
PAIRWISE_CENTERED_FULL_CONDUCTOR_ADAPTER_IMPORTED=true
PAIRWISE_CENTERED_COEFFICIENT_PHYSICAL_MASK_MANDATORY=true
CONDUCTOR_LOSS_REOPENED=false
```

The completed sH50/4diH audits do not certify a fixed power saving for the full physical weighted object, so no H certificate is upgraded here.

## 7. Exact state of the pairwise branch

Combining merged s7-54 with Sections 1--6, the three old pairwise covariance branches reduce, for upper-bound purposes, to one common positive receiver with two internal mechanisms:

```text
A. positive zero-mode balanced-cofactor covariance;
B. positive full-conductor centered inverse-fraction covariance.
```

Negative covariance is helpful and removed from the obstruction list. A second or third pairwise projection supplies no new modulus density because s7-54/X15 finite-fiber equivalence recovers the third projection with `B^o(1)` ambiguity.

The connected positive third cumulant and the positive near-maximal principal occupancy remain distinct.

## 8. H decision

No new mainline H is opened at 4dm.

Reason: the centered component is already within the theorem family audited negatively by sH50/4diH, while the newly isolated zero-mode cofactor covariance is still an internal arithmetic density/correlation object without a new theorem-ready kernel. The next useful step is to factor/localize that cofactor covariance and compare it with the physical balanced-cell incidence before another theorem audit.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
SH50_REOPENED=false
DIH_REOPENED=false
```

## Boundary

```text
STAGE14_4DM=COMPLETE_COMMON_PAIRWISE_POSITIVE_EXCESS_ZERO_MODE_AND_CENTERED_INVERSE_FRACTION_SPLIT
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEGATIVE_PAIRWISE_COVARIANCE_IS_UPPER_BOUND_OBSTRUCTION=false
PAIRWISE_UPPER_BOUND_OBSTRUCTION_USES_POSITIVE_PART_ONLY=true
POSITIVE_PAIRWISE_FIXED_POWER_JOINT_DENSITY_DEFICIT_STRICT_SUBSQRT=true
POSITIVE_PAIRWISE_SQRT_OBSTRUCTION_REQUIRES_JOINT_DENSITY=Bo0=true
PAIRWISE_BRANCH_COUNT_AT_FIXED_POWER=1
COMMON_PAIRWISE_COVARIANCE_ZERO_CENTERED_SPLIT_PROVED=true
PAIRWISE_RECEIVER_EQUALS_ONLY_INVERSE_FRACTION_ERROR=false
PAIRWISE_ZERO_MODE_COFACTOR_COVARIANCE_REMAINS=true
PAIRWISE_CENTERED_INVERSE_FRACTION_COVARIANCE_REMAINS=true
PAIRWISE_ZERO_MODE_LEDGER_EXPONENT=1/2
PAIRWISE_CENTERED_FULL_CONDUCTOR_ADAPTER_IMPORTED=true
CONNECTED_TRIPLE_POSITIVE_BRANCH_RETAINED=true
PRINCIPAL_NEAR_MAX_POSITIVE_BRANCH_RETAINED=true
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

New pairwise receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanPositiveTwoProjectionZeroModeCofactorOrCenteredInverseFractionCovariance
```

Connected receiver remains:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanPositiveConnectedThreeProjectionCumulant
```

Principal receiver remains:

```text
FullConductorNearMaximalConditionalPrincipalOccupancy
```

Next: `Stage14-4dn`.
