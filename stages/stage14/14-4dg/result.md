# Stage14-4dg — primitive product/norm centering and principal-density boundary

## Status

`COMPLETE_PRIMITIVE_PRODUCT_NORM_CENTERING_AND_PRINCIPAL_DENSITY_BOUNDARY`

Stage14-4dg consumes merged `Stage14-4df`, merged `Stage14-s7-48`, and the completed frozen `Stage14-sH48` applicability audit.

The entering whole-family theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family saving is proved here.  The purpose of this stage is to make the `sH48` preferred centered receiver mathematically precise on the mainline and to isolate the principal-density term that any absolute dispersion argument must still control.

---

## 1. Imported six-block saturation packet

Merged 4df proves that every possible square-root-saturating packet can be represented, after the frozen endpoint-small / 2-primary decoration, by six fixed-power pairwise-separated blocks

```text
C_*, S, T, u_*, R, J
```

with

```text
C_* S T = D^2+A^2,
u_* R J = D^2-A^2,
D,A=B^(1/4+o(1)),
D>A>0.
```

It also proves

```text
fixed (C_*,S,T,u_*,R,J)
=> #(D,A)=B^o(1),
```

and that the mixed fourth-root label has no independent fixed-power support after the six blocks are fixed.

Thus the remaining obstruction is a density/correlation problem, not another multiplicity problem.

```text
MERGED_4DF_IMPORTED=true
SIX_ATOMIC_NORM_BLOCKS_PAIRWISE_SEPARATED=true
SIX_BLOCK_PACKET_TO_BALANCED_PAIR_MULTIPLICITY=Bo1
```

---

## 2. Import the s7-48 rotated-pair coordinate system

Put

```text
m=D+A,
n=D-A.
```

Then

```text
D=(m+n)/2,
A=(m-n)/2,
```

and the two complementary square identities become

```text
boxed:
mn = D^2-A^2 = epsilon_- u_* R J,

boxed:
m^2+n^2
 =2(D^2+A^2)
 =2 epsilon_+ C_* S T.
```

The frozen signs `epsilon_+`, `epsilon_-` are part of the `B^o(1)` endpoint/2-primary decoration and carry no fixed-power entropy.

Because

```text
gcd(m,n)=gcd(D+A,D-A)
```

divides `2 gcd(D,A)`, merged 4de--4df imply

```text
gcd(m,n)=B^o(1)
```

at fixed-power scale.  After the permitted common peel we work with a primitive rotated pair.

The physical scale is

```text
m,n=B^(1/4+o(1)).
```

Therefore the ambient primitive quarter-pair base has

```text
#P_B <= B^(1/2+o(1)).
```

This is exactly the theorem-ready coordinate system of merged s7-48/sH48.

```text
MERGED_S7_48_IMPORTED=true
ROTATED_PRIMITIVE_PAIR_DEFINED=true
ROTATED_PAIR_PRODUCT_IDENTITY=true
ROTATED_PAIR_NORM_IDENTITY=true
PRIMITIVE_QUARTER_PAIR_BASE_EXPONENT=1/2
```

---

## 3. Side-specific physical factorization weights

Let `P_B` denote the primitive quarter-pair base after all common masks that do not require choosing the six cell factors have been imposed.  These common masks include the frozen dyadic ranges, positivity/order convention, endpoint-small support, parity convention, and the statewise restrictions already fixed before the final factorization choice.

For `(m,n) in P_B`, define the plus-side weight

```text
W_+(m,n)
```

to be the number of admissible triples `(C_*,S,T)` satisfying

```text
m^2+n^2 = 2 epsilon_+ C_* S T
```

with the inherited plus-side scales, squarefreeness, pairwise-separation, Gaussian orientation, and all plus-local physical masks.

Define the minus-side weight

```text
W_-(m,n)
```

to be the number of admissible triples `(u_*,R,J)` satisfying

```text
mn = epsilon_- u_* R J
```

with the inherited minus-side scales, squarefreeness, pairwise-separation, sign allocation, and all minus-local physical masks.

For a fixed integer, each ordered three-factor split is bounded by a ternary divisor function.  Hence throughout the physical ranges

```text
boxed:
W_+(m,n)=B^o(1),
W_-(m,n)=B^o(1).
```

The weights are nonnegative integers.  They are not assumed to be indicators.

```text
PLUS_FACTOR_WEIGHT_DIVISOR_MANY=true
MINUS_FACTOR_WEIGHT_DIVISOR_MANY=true
SIDE_WEIGHT_MAX_MULTIPLICITY=Bo1
```

---

## 4. The product of the two weights is a legal outer incidence majorant

Every physical square-root packet determines

```text
(m,n),
(C_*,S,T),
(u_*,R,J).
```

The chosen plus triple is counted by `W_+(m,n)` and the chosen minus triple is counted by `W_-(m,n)`.

Some combinations counted by the product may fail a remaining joint reciprocal/orientation consistency test.  Therefore the product weight is used as a majorant, not silently identified with the exact physical indicator.

Merged s7-46/s7-48 give only `B^o(1)` reconstruction/completion multiplicity after both sides are fixed.  Consequently the square-root saturation contribution satisfies

```text
boxed:
N_sat(B)
 <= B^o(1) I(B),

I(B)
 := sum_{(m,n) in P_B} W_+(m,n) W_-(m,n).
```

Thus a fixed-power saving for `I(B)` is sufficient for a fixed-power saving for the physical saturation family.

```text
PRODUCT_WEIGHT_IS_OUTER_PHYSICAL_MAJORANT=true
JOINT_COMPLETION_AFTER_TWO_SIDE_FACTORS=Bo1
PHYSICAL_SATURATION_COUNT_LEQ_Bo1_TIMES_PRODUCT_NORM_INCIDENCE=true
```

---

## 5. Exact two-sided global centering identity

Assume `P_B` is nonempty and write

```text
P := #P_B,

mu_+
 := (1/P) sum_{P_B} W_+,

mu_-
 := (1/P) sum_{P_B} W_-.
```

Define centered weights

```text
W_+^0 := W_+ - mu_+,
W_-^0 := W_- - mu_-.
```

By definition

```text
sum_{P_B} W_+^0=0,
sum_{P_B} W_-^0=0.
```

Expanding the product gives the exact identity

```text
boxed:
I(B)
 = P mu_+ mu_-
 + sum_{P_B} W_+^0 W_-^0.                         (5.1)
```

There are no linear remainder terms.

For an empty base the identity is interpreted trivially with `I(B)=0`.

This is the precise mainline version of the centered product-vs-norm correlation suggested by sH48.

```text
GLOBAL_TWO_SIDED_CENTERING_IDENTITY_PROVED=true
CENTERING_LINEAR_TERMS_VANISH_EXACTLY=true
PRINCIPAL_TERM=P*mu_plus*mu_minus
CENTERED_COVARIANCE_TERM=sum_Wplus0_Wminus0
```

---

## 6. Why absolute dispersion on the centered term alone is insufficient

Suppose a future dispersion theorem proves, for some fixed `delta>0`,

```text
|sum W_+^0 W_-^0|
 << B^(1/2-delta+o(1)).                            (6.1)
```

Equation (5.1) still contains the nonnegative principal term

```text
P mu_+ mu_-.
```

Since

```text
P<=B^(1/2+o(1)),
```

a proof based on the absolute covariance estimate (6.1) also needs a fixed-power estimate of the form

```text
boxed:
P mu_+ mu_-
 << B^(1/2-delta_0+o(1))                           (6.2)
```

for some fixed `delta_0>0`, or a stronger structured argument that couples the principal piece back into a cancellation mechanism.

Merely replacing the positive incidence by its centered covariance does not make the principal density disappear.

```text
ABSOLUTE_CENTERED_DISPERSION_ALONE_SUFFICIENT=false
PRINCIPAL_DENSITY_CONTROL_REQUIRED_FOR_ABSOLUTE_DISPERSION_ROUTE=true
```

This statement does not claim that (6.2) is mathematically necessary for every conceivable proof: a proof could in principle exploit signed cancellation between the two terms of (5.1).  It states the exact requirement for the standard route in which the centered covariance is bounded in absolute value.

---

## 7. Import the sH48 negative marginal theorem audit exactly once

Merged frozen sH48 audits precisely the primitive product/norm receiver

```text
mn = epsilon_- u_* R J,
m^2+n^2 = 2 epsilon_+ C_* S T
```

with the required physical masks retained.

Its strict applicability verdict is

```text
OFF_THE_SHELF_THEOREM_APPLICABLE=false,
FIXED_POWER_SAVING_PROVED=false,
CERTIFIED_B_POWER_SAVING_EXPONENT=0.
```

In particular it records

```text
ONE_SIDED_BALANCED_DIVISOR_SIEVE_FIXED_POWER_SUFFICIENT=false,
ONE_SIDED_SUM_OF_TWO_SQUARES_SIEVE_FIXED_POWER_SUFFICIENT=false,
MARGINAL_SIEVE_DENSITIES_MAY_NOT_BE_MULTIPLIED=true.
```

Therefore the available one-sided theorem inventory does not certify a fixed `B`-power estimate for `mu_+`, `mu_-`, or their principal product in (6.2).

This is an applicability boundary, not a lower bound: 4dg does **not** claim that `P mu_+mu_-` is actually of square-root size in the physical family.

```text
MERGED_SH48_IMPORTED=true
SH48_CONSUMED_BY_MAINLINE=true
SH48_REOPENED=false
MARGINAL_FIXED_POWER_MEAN_SAVING_CERTIFIED=false
PRINCIPAL_TERM_FIXED_POWER_SAVING_PROVED=false
```

---

## 8. Partition / conditional centering leaves the same principal issue

A more refined dispersion setup may partition `P_B` into disjoint arithmetic cells

```text
P_B = disjoint union_a P_a
```

according to local residue data, dyadic subboxes, orientation states, or another exact common skeleton.

For each nonempty cell define conditional means

```text
mu_{+,a}
 := |P_a|^(-1) sum_{P_a} W_+,

mu_{-,a}
 := |P_a|^(-1) sum_{P_a} W_-.
```

Then the same expansion gives the exact cellwise identity

```text
boxed:
I(B)
 = sum_a |P_a| mu_{+,a} mu_{-,a}
 + sum_a sum_{P_a}
     (W_+-mu_{+,a})(W_--mu_{-,a}).                 (8.1)
```

Thus conditional centering can expose better oscillatory kernels, but it does not by itself delete the cellwise principal density.

A successful conditional adapter must do at least one of the following:

```text
1. prove the cellwise principal sum is power-sparse;
2. build a signed transfer in which the local main term is cancelled by an exact physical identity;
3. refine the common cells until local incompatibility forces a fixed-power loss;
4. derive a theorem that controls the uncentered joint correlation directly.
```

```text
CONDITIONAL_CENTERING_IDENTITY_PROVED=true
CELLWISE_PRINCIPAL_DENSITY_REMAINS_AFTER_CENTERING=true
CENTERING_IS_NOT_FREE_POWER_SAVING=true
```

---

## 9. New minimal mainline receiver

The sH48 preferred receiver

```text
CenteredPrimitiveQuarterPairProductNormDualBalancedCellFactorizationDispersion
```

is therefore refined on the mainline to

```text
boxed:
ConditionallyCenteredPrimitiveQuarterPairProductNormDualBalancedCellFactorizationDispersionWithPrincipalDensityControl.
```

The required future theorem/adapter must retain

```text
m,n=B^(1/4+o(1)),
gcd(m,n)=B^o(1),
mn=epsilon_-u_*RJ,
m^2+n^2=2epsilon_+C_*ST,
C_*,S,T,u_*,R,J pairwise separated at fixed-power scale,
all balanced squarefree cell scales,
all inherited reciprocal/orientation/state masks,
```

and must control both the principal-density contribution and the centered correlation, or replace that decomposition with an exact mechanism that removes the principal term.

```text
REMAINING_RECEIVER=ConditionallyCenteredPrimitiveQuarterPairProductNormDualBalancedCellFactorizationDispersionWithPrincipalDensityControl
```

---

## 10. Whole-family theorem

No new exponent is promoted:

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The progress is structural: a future dispersion theorem can no longer be counted as sufficient unless its principal-density bookkeeping is explicit.

---

## 11. Auxiliary theorem decision

No new mainline H request is opened at 4dg.

Reason: merged sH48 already completed the off-the-shelf theorem audit for the uncentered product/norm receiver and identified centering as the missing adapter.  Stage14-4dg has now shown that even the centered adapter needs explicit principal-density control.  No concrete new oscillatory kernel or conditional local-density formula has yet been constructed for an external theorem to audit.

The next step is therefore internal exact work, not another literature search.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
ADDITIONAL_MAINLINE_H_NEEDED=false
SH48_REOPENED=false
```

The fixed-`U` t/tH route remains a different coefficient space and is not cross-promoted here.

```text
T87_CROSS_PROMOTED_TO_MAINLINE=false
TH25_CROSS_PROMOTED_TO_MAINLINE=false
```

---

## 12. s-route state

The s route is already active and has completed its `sH48` snapshot audit.  Stage14-4dg does not make a route-reactivation judgment.  The completed sH48 certificate says

```text
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT_H_NEEDED=false
NEXT_S_ROUTE=Stage14-s7-49.
```

4dg leaves route lifecycle ownership to the s route/current roadmap and does not rewrite the roadmap.

```text
S_ROUTE_LIFECYCLE_OWNED_BY_S_ROUTE=true
ROADMAP_MODIFIED_BY_4DG=false
```

---

## 13. Next mainline task

`Stage14-4dh` should construct an explicit conditional/local centering skeleton before any new H audit.

It should test whether the pairwise-separated six-block support gives a canonical finite residue-state partition on which

```text
sum_a |P_a| mu_{+,a} mu_{-,a}
```

has an exact local incompatibility or a fixed-power deficit.  Only after the principal term is controlled should it ask whether the centered remainder lands in an inverse-fraction, complete Kloosterman, or nondegenerate determinant form.

```text
NEXT=Stage14-4dh
```

---

## Stage boundary

```text
STAGE14_4DG=COMPLETE_PRIMITIVE_PRODUCT_NORM_CENTERING_AND_PRINCIPAL_DENSITY_BOUNDARY
MERGED_4DF_IMPORTED=true
MERGED_S7_48_IMPORTED=true
MERGED_SH48_IMPORTED=true
ROTATED_PRIMITIVE_PAIR_DEFINED=true
ROTATED_PAIR_PRODUCT_IDENTITY=true
ROTATED_PAIR_NORM_IDENTITY=true
PRIMITIVE_QUARTER_PAIR_BASE_EXPONENT=1/2
PLUS_FACTOR_WEIGHT_DIVISOR_MANY=true
MINUS_FACTOR_WEIGHT_DIVISOR_MANY=true
PRODUCT_WEIGHT_IS_OUTER_PHYSICAL_MAJORANT=true
JOINT_COMPLETION_AFTER_TWO_SIDE_FACTORS=Bo1
GLOBAL_TWO_SIDED_CENTERING_IDENTITY_PROVED=true
CENTERING_LINEAR_TERMS_VANISH_EXACTLY=true
ABSOLUTE_CENTERED_DISPERSION_ALONE_SUFFICIENT=false
PRINCIPAL_DENSITY_CONTROL_REQUIRED_FOR_ABSOLUTE_DISPERSION_ROUTE=true
SH48_CONSUMED_BY_MAINLINE=true
SH48_REOPENED=false
MARGINAL_FIXED_POWER_MEAN_SAVING_CERTIFIED=false
PRINCIPAL_TERM_FIXED_POWER_SAVING_PROVED=false
CONDITIONAL_CENTERING_IDENTITY_PROVED=true
CELLWISE_PRINCIPAL_DENSITY_REMAINS_AFTER_CENTERING=true
CENTERING_IS_NOT_FREE_POWER_SAVING=true
REMAINING_RECEIVER=ConditionallyCenteredPrimitiveQuarterPairProductNormDualBalancedCellFactorizationDispersionWithPrincipalDensityControl
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
T87_CROSS_PROMOTED_TO_MAINLINE=false
TH25_CROSS_PROMOTED_TO_MAINLINE=false
ROADMAP_MODIFIED_BY_4DG=false
NEXT=Stage14-4dh
```
