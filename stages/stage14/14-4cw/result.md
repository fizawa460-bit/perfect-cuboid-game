# Stage14-4cw — collapse the extra residual gcd in the row/column ledger and isolate the proportional 9/16 barrier

## Status

`COMPLETE_S7_35_ROW_COLUMN_COUPLING_NONPROPORTIONAL_19_34_AND_9_16_PROMOTION`

Stage14-4cw consumes merged `4cv`, merged `s7-35`, merged `4cu`, and the compatible one-host counts of merged `s7-32`.

The current mainline theorem entering this stage is the stronger of the two newly merged bounds,

```text
V(B) << B^(4/7+o(1)),
```

from `s7-35`.  Merged `4cv` separately supplies an exact charged-once row/column reconstruction of the same joint core.  The purpose of 4cw is to insert the `s7-35` support collapse

```text
g_star/H_star^2 | oddpart(omega_1*omega_2)=B^o(1)
```

back into that row/column ledger.

On the nonproportional branch this improves the complete bound all the way to

```text
E_nonprop <= 19/34.
```

The old proportional branch of merged `4cu`, however, is only bounded by `9/16`.  Since

```text
19/34 < 9/16 < 4/7,
```

the new whole-family theorem is

```text
boxed:
V(B) << B^(9/16+o(1)).
```

No external H/tH theorem is used.

---

## 1. Imported strip and joint-core notation

Use

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

On the nonproportional branch of merged `4cu`, choose the larger cross-root cell and write

```text
H_star = B^(a+o(1)),
H_other= B^(b+o(1)),
a>=b>=0.
```

The two cells are coprime and

```text
H=H_star*H_other.
```

Let

```text
g_star=B^(rho+o(1))
```

be the odd rational coordinate gcd of the selected xi residual host, and let

```text
J=B^(j+o(1))
```

be the selected joint Cayley/residual good core used by 4cu/4cv.

---

## 2. Consume the exact s7-35 extra-gcd collapse

Merged `s7-35` proves primewise that

```text
g_star/H_star^2 | oddpart(omega_1*omega_2),
```

where `omega_i=B^o(1)`.  Therefore on exponent scale

```text
boxed:
rho=2a.                                                   (2.1)
```

This is stronger than merely knowing `rho>=2a`.

The result is exact up to `B^o(1)` endpoint support and does not require a density estimate.

---

## 3. Restore the pre-relaxation joint-core lower bound

Merged `4cu` constructs the joint core by intersecting two good cores.

The Cayley bad support satisfies, up to `B^o(1)`,

```text
C/C_Cayley | H_star^2*H_other^2,
```

while the selected residual-host bad support satisfies

```text
C/C_res | g_star^2.
```

Because `H_star^2|g_star`, the lcm of the two bad supports is bounded by

```text
g_star^2*H_other^2*B^o(1).
```

Hence before the coarse `chi-3rho` relaxation one has the exact exponent inequality

```text
boxed:
j >= chi-2rho-2b.                                      (3.1)
```

Using (2.1),

```text
boxed:
j >= chi-4a-2b.                                       (3.2)
```

This is not a new spacing modulus.  It is the same `J` already charged once in 4cv.

---

## 4. Two alternative complete counts on the same nonproportional block

Merged `s7-34/s7-35` give the fourth-power common-root count

```text
H^4 | q_xi.
```

Fixing the dyadic sizes `a,b`, the xi-host count is

```text
boxed:
E_H <= 3phi-1/8-3(a+b).                               (4.1)
```

Merged `4cv` gives the row/column reconstruction count

```text
E_RC <= 2phi+1/2-2j.                                  (4.2)
```

Substitute (3.2):

```text
boxed:
E_RC <= 2phi+1/2-2chi+8a+4b.                         (4.3)
```

Both are complete counts for the same physical block, so they are compared by `min`, never multiplied.

---

## 5. Weighted cancellation of the cross-root scale

For any reals `A,B`,

```text
min(A,B) <= (8A+3B)/11.
```

Apply this to (4.1) and (4.3).  The `a` coefficient cancels exactly:

```text
8E_H+3E_RC
 <= 30phi+1/2-6chi-12b.
```

Thus

```text
E_nonprop
 <= (30phi+1/2-6chi-12b)/11
 <= (30phi+1/2-6chi)/11.
```

Since

```text
chi=2theta+2phi-3/4,
```

we obtain

```text
boxed:
E_nonprop
 <= (18phi-12theta+5)/11.                            (5.1)
```

Using `phi<=1/4`,

```text
boxed:
E_nonprop
 <= 19/22-(12/11)theta.                              (5.2)
```

The negative leftover term `-12b/11` is important: the worst branch has

```text
b=0,
```

i.e. only one cross-root cell carries fixed-power mass.

---

## 6. Whole-strip nonproportional bound `19/34`

Retain the merged complete counts

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4.
```

### 6.1 `theta<=1/4`

```text
E_k<=1/2<19/34.
```

### 6.2 `1/4<=theta<=19/68`

Here `E_s=2theta`, hence

```text
E_s<=2*(19/68)=19/34.
```

### 6.3 `theta>=19/68`

By (5.2),

```text
E_nonprop
 <=19/22-(12/11)*(19/68)
 =19/34.
```

Therefore

```text
boxed:
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34.   (6.1)
```

The proved nonproportional envelope has a unique equality profile:

```text
boxed:
theta=19/68,
phi=1/4,
chi=21/68,
a=3/136,
b=0,
rho=3/68,
j=15/68.                                           (6.2)
```

At this profile

```text
E_H=E_RC=E_s=19/34,
E_k=10/17,
```

and both row/column short supports have exponent

```text
1/4-j=1/34.                                         (6.3)
```

This profile is already below the eventual whole-family barrier and is recorded only as the next nonproportional receiver if the proportional branch is later eliminated.

---

## 7. The proportional branch becomes the whole-family barrier

Merged `4cu` classifies the zero-product branch.  Positivity gives

```text
L_+>0,
```

so the only proportional possibility is

```text
boxed:
L_-=0,                                               (7.1)
```

i.e.

```text
z_1*r_2*s_2=z_2*r_1*s_1.                            (7.2)
```

After reducing the endpoint-small ratio,

```text
r_1*s_1:r_2*s_2=A_0:B_0,
```

with `A_0,B_0=B^o(1)` and coprime, one has

```text
z_1=A_0*t,
z_2=B_0*t,
t=B^(1/8+o(1)).                                     (7.3)
```

Merged `4cu` inserts this common scale into the k switched residual Gaussian host.  The Gaussian square divisor is coprime to `t`, so the scale survives as a rational coordinate gcd after descent.  The gcd-stratified k one-host count therefore gives

```text
boxed:
E_prop <= 3theta-3/8.                               (7.4)
```

Since `theta<=5/16`,

```text
boxed:
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16.      (7.5)
```

The row/column nonproportional argument of Sections 3--6 is **not** applied to `L_-=0`; in particular no division by `L_-L_+` or finite linear-product cofactor is made on this branch.

---

## 8. Whole-family promotion to `9/16`

Every physical packet is either nonproportional or proportional.  Hence

```text
E
 <= max(19/34,9/16)
 =9/16.
```

Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16,
IMPROVEMENT_OVER_MERGED_S7_35_4_7=1/112,
IMPROVEMENT_OVER_MERGED_4CV_7_12=1/48,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.          (8.1)
```

This is a genuine whole-family improvement over current merged main.

---

## 9. Necessary shape of a `9/16` saturation packet

Equality in (7.4) requires

```text
boxed:
theta=5/16.                                         (9.1)
```

The independent merged xi one-host bound

```text
E_xi<=3phi-1/8
```

shows that a packet can reach `9/16` only if

```text
3phi-1/8 >=9/16,
```

i.e.

```text
boxed:
11/48 <= phi <=1/4.                                 (9.2)
```

Together with the proportional identity, every possible saturation packet therefore lies on the face

```text
boxed:
theta=5/16,
11/48<=phi<=1/4,
L_-=0,
z_1=A_0*t,
z_2=B_0*t,
t=B^(1/8+o(1)).                                    (9.3)
```

Let

```text
g_k=oddpart(gcd(Re W_beta,Im W_beta))
```

for the k residual host used in the 4cu proportional proof.  Since `t|g_k`, any extra fixed-power factor in `g_k/t` gives additional one-host saving.  Thus saturation requires

```text
boxed:
g_k=t*B^o(1).                                      (9.4)
```

This isolates a substantially narrower receiver than the old 4cu proportional estimate.

---

## 10. Remaining receiver

Define

```text
NineSixteenthsProportionalEndpointScaleKResidualGaussianGcdIncidence.
```

It retains

```text
theta=5/16,
11/48<=phi<=1/4,
L_-=0,
z_1=A_0*t,
z_2=B_0*t,
t=B^(1/8+o(1)),
g_k=t*B^o(1),
```

plus the full Cayley row allocation and reciprocal signed-quotient system.

The next exact question is whether the common endpoint scale `t` can be transferred primewise into the k-side common-core / Cayley row data, or whether the two k switched hosts force a second rational-gcd or short-CRT restriction.  This must be exhausted before requesting any analytic H theorem.

The nonproportional fallback receiver, already strictly smaller at `19/34`, is

```text
NineteenThirtyFourthsSingleCrossRootRowColumnTwinShortLiftIncidence.
```

---

## 11. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T74_CROSS_PROMOTED_TO_MAINLINE=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
```

Reason: the new barrier is an exact proportional/gcd branch with unused k-side Gaussian/Cayley algebra.  It is not yet a stable averaged incidence theorem.  The fixed-`U` t74/tH20 coefficient-space receiver remains separate.

---

## Stage boundary

```text
STAGE14_4CW=COMPLETE_S7_35_ROW_COLUMN_COUPLING_NONPROPORTIONAL_19_34_AND_9_16_PROMOTION
MERGED_4CV_IMPORTED=true
MERGED_S7_35_IMPORTED=true
MERGED_4CU_IMPORTED=true
S7_35_EXTRA_XI_GCD_COLLAPSE_IMPORTED=true
SELECTED_XI_RESIDUAL_GCD_EXPONENT_EQUALS_TWICE_SELECTED_CROSS_ROOT_EXPONENT=true
PRE_RELAXATION_JOINT_CORE_LOWER_BOUND_RESTORED=true
NONPROPORTIONAL_WEIGHTED_COMPLETE_COUNT_COMBINATION=8:3
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=19/34
NONPROPORTIONAL_EQUALITY_THETA=19/68
NONPROPORTIONAL_EQUALITY_PHI=1/4
NONPROPORTIONAL_EQUALITY_SELECTED_CROSS_ROOT_EXPONENT=3/136
NONPROPORTIONAL_EQUALITY_JOINT_CORE_EXPONENT=15/68
NONPROPORTIONAL_TWIN_SHORT_SUPPORT_EXPONENT=1/34
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
NINE_SIXTEENTHS_SATURATION_THETA=5/16
NINE_SIXTEENTHS_SATURATION_PHI_LOWER=11/48
NINE_SIXTEENTHS_SATURATION_PHI_UPPER=1/4
NINE_SIXTEENTHS_REQUIRES_L_MINUS_ZERO=true
NINE_SIXTEENTHS_ENDPOINT_COMMON_SCALE_EXPONENT=1/8
NINE_SIXTEENTHS_K_RESIDUAL_GCD_EXTRA_FIXED_POWER=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=9/16
IMPROVEMENT_OVER_MERGED_S7_35_4_7=1/112
IMPROVEMENT_OVER_MERGED_4CV_7_12=1/48
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
REMAINING_RECEIVER=NineSixteenthsProportionalEndpointScaleKResidualGaussianGcdIncidence
NONPROPORTIONAL_FALLBACK_RECEIVER=NineteenThirtyFourthsSingleCrossRootRowColumnTwinShortLiftIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T74_CROSS_PROMOTED_TO_MAINLINE=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cx
```