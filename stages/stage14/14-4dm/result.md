# Stage14-4dm — sign-sensitive pairwise receiver and exact covariance recentering

## Status

`COMPLETE_POSITIVE_PAIRWISE_ZERO_MODE_COFACTOR_AND_MASKED_CENTERED_COVARIANCE_REDUCTION`

Consumes merged `Stage14-4dl`, merged `Stage14-s7-54`, merged `Stage14-s7-55`, merged `Stage14-s7-49`, merged `Stage14-s7-50`, and merged `Stage14-X15` on latest main.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged s7-54 identifies the three pairwise projection branches as one fixed-power finite-fiber two-projection mass. Merged s7-55 then separates that representative covariance into a pairwise joint-density defect and a centered inverse-fraction error. Stage14-4dm performs the upper-bound sign reduction and an exact covariance recentering of the s7-55 split.

## 1. Sign-sensitive upper-bound reduction

On a surviving interior full-conductor cell `Omega`, retain

```text
W_+,W_-,W_k in {0,1},
mu_j=E W_j,
X_j=W_j-mu_j,
Gamma_ij=E(X_i X_j),
Kappa_3=E(X_+X_-X_k).
```

The exact cumulant identity is

```text
E(W_+W_-W_k)
 = mu_+mu_-mu_k
 + mu_k Gamma_{+-}
 + mu_- Gamma_{+k}
 + mu_+ Gamma_{-k}
 + Kappa_3.
```

Since every `mu_j>=0`,

```text
E(W_+W_-W_k)
 <= mu_+mu_-mu_k
 + mu_k Gamma_{+-}^+
 + mu_- Gamma_{+k}^+
 + mu_+ Gamma_{-k}^+
 + Kappa_3^+,
```

where `x^+=max(x,0)`.

Hence negative pairwise covariance is helpful for an upper bound and is not a positive exceptional family that must be counted.

```text
NEGATIVE_PAIRWISE_COVARIANCE_IS_UPPER_BOUND_OBSTRUCTION=false
PAIRWISE_UPPER_BOUND_OBSTRUCTION_USES_POSITIVE_PART_ONLY=true
CONNECTED_TRIPLE_UPPER_BOUND_OBSTRUCTION_USES_POSITIVE_PART_ONLY=true
```

## 2. Positive pairwise excess requires dense joint occupancy

For a pair `(i,j)` define

```text
p_ij=E(W_iW_j).
```

Then

```text
Gamma_ij=p_ij-mu_i mu_j,
0<=Gamma_ij^+<=p_ij.
```

Therefore any fixed-power pairwise joint-density deficit

```text
p_ij <= B^(-delta+o(1)),
delta>0,
```

forces the positive pairwise contribution to

```text
<< B^(1/2-delta+o(1)).
```

Possible positive pairwise square-root saturation is thus confined to

```text
p_ij=B^(-o(1)).
```

Merged s7-54 proves that the three pairs `(+,-)`, `(+,k)`, `(-,k)` are power-equivalent coordinate realizations of one physical two-projection mass. They cannot be charged independently.

```text
POSITIVE_PAIRWISE_FIXED_POWER_JOINT_DENSITY_DEFICIT_STRICT_SUBSQRT=true
POSITIVE_PAIRWISE_SQRT_OBSTRUCTION_REQUIRES_JOINT_DENSITY=Bo0=true
PAIRWISE_BRANCH_COUNT_AT_FIXED_POWER=1
PAIRWISE_DOUBLE_CHARGE_ALLOWED=false
```

## 3. Canonical representative and rootline factorization

Choose the merged s7-54 representative `(+,-)`. Put

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
R_rho(m,n)=1_{m == rho*n (mod C_*)}.
```

Merged s7-49 gives exactly

```text
R_rho = 1/C_* + K_rho,
```

where

```text
K_rho(m,n)
 =(1/C_*) sum_{0!=h mod C_*} e_{C_*}(h(m-rho*n)).
```

Write the plus selector as

```text
W_+ = A_+ R_rho,
```

where `A_+` contains every remaining plus-side physical mask: balanced/squarefree factorization, pairwise separation, reciprocal reconstruction, endpoint-small decoration and orientation data. Put

```text
B_-:=W_-.
```

No physical filter is removed.

## 4. Exact recentering of the merged s7-55 split

By bilinearity of covariance,

```text
Gamma_{+-}
 = Cov(A_+R_rho,B_-)
 = (1/C_*) Cov(A_+,B_-)
   + Cov(A_+K_rho,B_-).                     (4.1)
```

This is an exact refinement/recentering of the merged s7-55 identity

```text
Gamma_{+-}=Delta_pair+Err_pair.
```

The allocation between the two summands is changed only by adding and subtracting the exact masked-centered mean term; their sum is the same covariance.

Define

```text
Z_pair := (1/C_*) Cov(A_+,B_-),
E_pair := Cov(A_+K_rho,B_-).
```

Then

```text
Gamma_{+-}=Z_pair+E_pair,
Gamma_{+-}^+ <= Z_pair^+ + E_pair^+.
```

Thus the common positive pairwise receiver has exactly two internal mechanisms:

```text
A. positive zero-mode cofactor covariance Z_pair^+;
B. positive masked centered inverse-fraction covariance E_pair^+.
```

In particular, the pairwise receiver is not only the s7-49/s7-50 centered Kloosterman-type error.

```text
COMMON_PAIRWISE_COVARIANCE_ZERO_CENTERED_RECENTERING_PROVED=true
PAIRWISE_RECEIVER_EQUALS_ONLY_INVERSE_FRACTION_ERROR=false
PAIRWISE_ZERO_MODE_COFACTOR_COVARIANCE_REMAINS=true
PAIRWISE_MASKED_CENTERED_INVERSE_FRACTION_COVARIANCE_REMAINS=true
```

## 5. Zero-mode cofactor covariance remains at square-root scale

The rootline zero-frequency factor is

```text
1/C_*=B^(-chi+o(1)).
```

and the dyadic `C_*` support has `B^(chi+o(1))` possibilities. These cancel at fixed-power scale exactly as in s7-49. Hence extracting `Z_pair` alone does not improve the global exponent:

```text
PAIRWISE_ZERO_MODE_LEDGER_EXPONENT=1/2
PAIRWISE_ZERO_MODE_EXTRACTION_STRICT_SUBSQRT=false
```

For binary/bounded selectors,

```text
Cov(A_+,B_-)^+ <= E(A_+B_-).
```

Therefore any fixed-power deficit in the cofactor joint occupancy is strict sub-square-root; possible saturation requires exponent-zero dense cofactor overlap.

## 6. Centered term is the full-conductor masked inverse-fraction family

On the product side, merged s7-49 gives

```text
P_-=mn,
n == P_- inverse(m) mod C_*.
```

Thus each nonzero-frequency phase in `K_rho` is

```text
e_{C_*}(h*m-h*rho*P_-*inverse(m)).
```

Merged s7-50 proves that every fixed-power conductor loss is strict sub-square-root, so possible saturation is restricted to

```text
q=C_* B^o(1),
gcd(h0,q)=1.
```

Therefore `E_pair` is a physically masked full-conductor inverse-fraction covariance. The physical coefficient `A_+` and minus selector `B_-` are mandatory.

```text
PAIRWISE_CENTERED_FULL_CONDUCTOR_ADAPTER_IMPORTED=true
PAIRWISE_CENTERED_PHYSICAL_MASK_MANDATORY=true
CONDUCTOR_LOSS_REOPENED=false
```

The completed sH50/4diH audits certify no fixed positive delta for this full weighted object; they are not reopened.

## 7. q11 compatibility

Merged `Stage14-q11` independently confirms that no surveyed theorem directly gives a fixed-power strict sub-square-root saving for the current near-maximal Pythagorean correlation packet. Its q10 carry-forward keeps the inverse-fraction shelf active for the centered branch and recommends an internal multiplicative/Hecke-phase factorization test for the new principal/joint-density branch.

This stage does not promote a q11 `NEAR` source to a theorem. The q11 radar is compatible context only.

```text
MERGED_Q11_COMPATIBLE=true
Q11_DIRECT_THEOREM_IMPORTED=false
Q10_INVERSE_FRACTION_BRANCH_RETAINED=true
```

## 8. Remaining whole-family mechanisms

For upper-bound purposes, the surviving mechanisms are now

```text
1. positive near-maximal principal occupancy;
2. positive zero-mode two-projection cofactor covariance;
3. positive masked full-conductor inverse-fraction covariance;
4. positive connected third cumulant.
```

The three pairwise coordinate views count only once at fixed-power scale.

No current exact identity makes any of these four mechanisms uniformly power-small, so the canonical exponent remains `1/2`.

## 9. H decision

No new H is opened.

The centered pairwise mechanism has already been covered by the negative applicability audits sH50/4diH at the full physical-weight level. The newly isolated zero-mode cofactor covariance is still an internal conditional-density object; q11 likewise returns no direct theorem and recommends an internal factorization test first.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
SH50_REOPENED=false
DIH_REOPENED=false
```

## Boundary

```text
STAGE14_4DM=COMPLETE_POSITIVE_PAIRWISE_ZERO_MODE_COFACTOR_AND_MASKED_CENTERED_COVARIANCE_REDUCTION
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MERGED_S7_55_IMPORTED=true
MERGED_Q11_COMPATIBLE=true
NEGATIVE_PAIRWISE_COVARIANCE_IS_UPPER_BOUND_OBSTRUCTION=false
PAIRWISE_UPPER_BOUND_OBSTRUCTION_USES_POSITIVE_PART_ONLY=true
POSITIVE_PAIRWISE_FIXED_POWER_JOINT_DENSITY_DEFICIT_STRICT_SUBSQRT=true
POSITIVE_PAIRWISE_SQRT_OBSTRUCTION_REQUIRES_JOINT_DENSITY=Bo0=true
PAIRWISE_BRANCH_COUNT_AT_FIXED_POWER=1
COMMON_PAIRWISE_COVARIANCE_ZERO_CENTERED_RECENTERING_PROVED=true
PAIRWISE_RECEIVER_EQUALS_ONLY_INVERSE_FRACTION_ERROR=false
PAIRWISE_ZERO_MODE_COFACTOR_COVARIANCE_REMAINS=true
PAIRWISE_MASKED_CENTERED_INVERSE_FRACTION_COVARIANCE_REMAINS=true
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
FullConductorInteriorDensePrimitiveQuarterPythagoreanPositiveTwoProjectionZeroModeCofactorOrMaskedCenteredInverseFractionCovariance
```

Connected receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanPositiveConnectedThreeProjectionCumulant
```

Principal receiver:

```text
FullConductorNearMaximalConditionalPrincipalOccupancy
```

Next: `Stage14-4dn`.
