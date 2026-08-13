# Stage14-4dn — zero-mode cofactor covariance as conditional uplift

## Status

`COMPLETE_ZERO_MODE_COFACTOR_COVARIANCE_CONDITIONAL_UPLIFT_REDUCTION`

Consumes merged `Stage14-4dm`, merged `Stage14-s7-56`, merged `Stage14-s7-52`, merged `Stage14-s7-54`, and merged `Stage14-X15`.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Stage14-4dm reduced the only positive pairwise obstruction to one representative two-projection receiver with two pieces:

```text
(1/C_*) Cov(A_+,W_-)
+
Cov(A_+ K_rho,W_-).
```

This stage attacks only the first, zero-frequency cofactor covariance. The masked full-conductor inverse-fraction covariance is retained unchanged.

## 1. Binary two-slice identity

On one surviving full-conductor interior cell let

```text
A:=A_+ in {0,1},
B:=W_- in {0,1},
mu_A:=E[A].
```

Define the two conditional minus-side means

```text
nu_1:=E[B | A=1],
nu_0:=E[B | A=0].
```

On the interior packet both slices are nonempty at fixed-power scale; endpoint-empty exceptional cells are already covered by the merged marginal-deficit peels.

Since

```text
E[AB]=mu_A nu_1,
E[B]=mu_A nu_1+(1-mu_A)nu_0,
```

we have exactly

```text
boxed:
Cov(A,B)=mu_A(1-mu_A)(nu_1-nu_0).                 (1.1)
```

Equivalently, if `mu_B=E[B]`,

```text
Cov(A,B)=mu_A(nu_1-mu_B)
        =(1-mu_A)(mu_B-nu_0).                     (1.2)
```

Thus the zero-mode covariance is not an abstract joint-density defect after conditioning: it is one signed difference between the minus-selector density on the plus-cofactor ON slice and OFF slice.

```text
ZERO_MODE_COVARIANCE_TWO_SLICE_IDENTITY_PROVED=true
ZERO_MODE_COVARIANCE_IS_CONDITIONAL_MEAN_CONTRAST=true
```

## 2. Positive covariance is positive conditional uplift

Because `mu_A(1-mu_A)>=0`,

```text
Cov(A,B)>0
iff
nu_1>nu_0.
```

For the upper-bound obstruction only the positive part matters by merged 4dm, so

```text
boxed:
Cov(A,B)^+
 = mu_A(1-mu_A)(nu_1-nu_0)^+.                    (2.1)
```

Define the positive conditional uplift

```text
Uplift_{+|-}:=(nu_1-nu_0)^+ in [0,1].
```

Then the zero-mode term from 4dm is exactly

```text
boxed:
Z_pair^+
 = (1/C_*) mu_A(1-mu_A) Uplift_{+|-}.             (2.2)
```

Negative or zero conditional contrast is harmless for the positive upper-bound branch.

```text
ZERO_MODE_POSITIVE_OBSTRUCTION_EQUALS_POSITIVE_CONDITIONAL_UPLIFT=true
NEGATIVE_CONDITIONAL_CONTRAST_IS_UPPER_BOUND_OBSTRUCTION=false
```

## 3. Fixed-power conditional-uplift deficit is strict sub-square-root

Merged s7-52 confines any square-root-saturating interior cell to

```text
mu_A=B^(-o(1)),
1-mu_A=B^(-o(1)).
```

The zero-mode factor `1/C_*` is balanced by the already charged `C_*` support exactly as in merged s7-49/4dm, leaving the ambient exponent `1/2`.

Fix `delta>0`. On a conditional-contrast stratum

```text
Uplift_{+|-} <= B^(-delta+o(1)),
```

the zero-mode positive pairwise contribution is therefore

```text
<< B^(1/2-delta+o(1)).                             (3.1)
```

No extra loss from `mu_A(1-mu_A)` is needed; those factors are at most one and are already forced to exponent zero on any saturation sequence.

Hence zero-mode square-root saturation requires

```text
boxed:
Uplift_{+|-}=B^(-o(1)).                            (3.2)
```

```text
FIXED_POWER_CONDITIONAL_UPLIFT_DEFICIT_STRICT_SUBSQRT=true
ZERO_MODE_SQRT_SATURATION_REQUIRES_CONDITIONAL_UPLIFT=Bo0=true
```

## 4. Equivalent conditional-probability forms

Let

```text
mu_B:=E[B],
mu_AB:=E[AB].
```

Then

```text
nu_1 = mu_AB/mu_A,
nu_0 = (mu_B-mu_AB)/(1-mu_A),
```

so

```text
nu_1-nu_0
 = (mu_AB-mu_A mu_B)/(mu_A(1-mu_A)).              (4.1)
```

This simply inverts (1.1); it introduces no new support.

A second useful normalization is

```text
eta_{+|-}:=(nu_1-mu_B)^+/(1-mu_B)
```

whenever `mu_B<1`. Since

```text
nu_1-mu_B=(1-mu_A)(nu_1-nu_0),
```

we obtain

```text
Cov(A,B)^+
 = mu_A(1-mu_B) eta_{+|-}.                         (4.2)
```

Merged s7-52 also has `1-mu_B=B^(-o(1))` on saturation cells. Thus either contrast normalization leads to the same fixed-power conclusion.

```text
CONDITIONAL_UPLIFT_NORMALIZATIONS_POWER_EQUIVALENT=true
```

## 5. Receiver contraction

The zero-mode pairwise receiver from 4dm

```text
PositiveZeroModeCofactorCovariance
```

contracts to

```text
FullConductorInteriorDensePrimitiveQuarterPythagoreanPositiveConditionalCofactorUplift
```

with exact statistic

```text
Uplift_{+|-}
 = [ E(W_- | A_+=1) - E(W_- | A_+=0) ]^+.
```

Because merged s7-54 proves all three pairwise coordinate descriptions power-equivalent, this remains one charged-once representative pair. We do not create three separate conditional-uplift receivers.

```text
PAIRWISE_CONDITIONAL_UPLIFT_FIXED_POWER_BRANCH_COUNT=1
PAIRWISE_CONDITIONAL_UPLIFT_DOUBLE_CHARGE_ALLOWED=false
```

## 6. What is and is not proved

The exact identity does not prove that `Uplift_{+|-}` has a fixed-power deficit. Dense plus-cofactor admissibility could, in principle, enhance minus-side admissibility by exponent-zero amount.

Therefore the current positive pairwise branch is now the union of

```text
A. exponent-zero positive conditional cofactor uplift;
B. positive masked full-conductor inverse-fraction covariance.
```

The principal near-maximal occupancy branch and the positive connected third cumulant remain distinct.

No whole-family exponent improvement follows yet.

```text
CONDITIONAL_UPLIFT_FIXED_POWER_DEFICIT_PROVED_UNIFORMLY=false
MASKED_CENTERED_INVERSE_FRACTION_BRANCH_RETAINED=true
CONNECTED_TRIPLE_POSITIVE_BRANCH_RETAINED=true
PRINCIPAL_NEAR_MAX_POSITIVE_BRANCH_RETAINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 7. q11 / multiplicative-structure compatibility

Merged q11 proposed testing whether the physical selectors admit a bounded-complexity multiplicative/Hecke-multiplicative phase decomposition. The new conditional-uplift statistic is a sharper internal target for that test: one only needs to understand how conditioning on the plus cofactor selector changes the minus selector density.

No multiplicative representation is proved here, and q11 remains advisory architecture rather than theorem input.

```text
Q11_MULTIPLICATIVE_PHASE_DECOMPOSITION_PROVED=false
Q11_SAVING_CROSS_PROMOTED=false
```

## 8. H decision

No new mainline H is opened at 4dn.

Reason: the zero-mode branch has just become an exact conditional-density contrast and should first be expressed in the physical factor coordinates `(C_*,S,T;u_*,R,J)` to determine whether it factors, admits a prime-by-prime influence decomposition, or collapses to the q11 multiplicative-phase transfer test. The masked centered branch already has its existing inverse-fraction theorem shelf.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
NEXT_H_NEEDED=false
```

## Boundary

```text
STAGE14_4DN=COMPLETE_ZERO_MODE_COFACTOR_COVARIANCE_CONDITIONAL_UPLIFT_REDUCTION
MERGED_4DM_IMPORTED=true
MERGED_S7_56_IMPORTED=true
ZERO_MODE_COVARIANCE_TWO_SLICE_IDENTITY_PROVED=true
ZERO_MODE_COVARIANCE_IS_CONDITIONAL_MEAN_CONTRAST=true
ZERO_MODE_POSITIVE_OBSTRUCTION_EQUALS_POSITIVE_CONDITIONAL_UPLIFT=true
NEGATIVE_CONDITIONAL_CONTRAST_IS_UPPER_BOUND_OBSTRUCTION=false
FIXED_POWER_CONDITIONAL_UPLIFT_DEFICIT_STRICT_SUBSQRT=true
ZERO_MODE_SQRT_SATURATION_REQUIRES_CONDITIONAL_UPLIFT=Bo0=true
CONDITIONAL_UPLIFT_NORMALIZATIONS_POWER_EQUIVALENT=true
PAIRWISE_CONDITIONAL_UPLIFT_FIXED_POWER_BRANCH_COUNT=1
CONDITIONAL_UPLIFT_FIXED_POWER_DEFICIT_PROVED_UNIFORMLY=false
MASKED_CENTERED_INVERSE_FRACTION_BRANCH_RETAINED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4do
```
