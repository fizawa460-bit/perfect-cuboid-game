# Stage14-s7-34 — xi fourth-power common-root transfer and the 47/80 bound

## Status

`COMPLETE_XI_FOURTH_POWER_ROOT_GCD_TRANSFER_AND_47_80_PROMOTION`

Stage14-s7-34 consumes merged `s7-33` and merged `4cu` on current main.

Merged `4cu` already improves the whole-family theorem to

```text
V(B) << B^(19/32+o(1))
```

and localizes equality in its proved envelope to

```text
theta=19/64,
phi=1/4,
chi=11/32,
rho=1/32,
J_star=B^(1/4+o(1)).
```

The new s7-34 observation is that the two cross-root cells do not merely force square divisors into the two xi residual-host coordinate gcds. Because both switched xi hosts have the same residual norm `q_xi`, those two square divisibilities combine into a **fourth-power divisor of the common xi residual norm**.

If

```text
H_S=oddpart(gcd(x_2,y_1)),
H_T=oddpart(gcd(x_1,y_2)),
H=H_S H_T,
gcd(H_S,H_T)=1,
```

then merged 4cu gives

```text
H_S^2 | g_S,
H_T^2 | g_T,
```

where

```text
g_S=oddpart(gcd(Re W_S,Im W_S)),
g_T=oddpart(gcd(Re W_T,Im W_T)).
```

Since

```text
oddpart(N(W_S))=oddpart(N(W_T))=q_xi,
```

we obtain exactly

```text
boxed:
H_S^4 | q_xi,
H_T^4 | q_xi,
H^4   | q_xi.                                      (0.1)
```

This produces a second legal complete xi one-host count. If

```text
H=B^(eta+o(1)),
```

then the residual norm support loses `3 eta`, not merely `eta`:

```text
boxed:
E_xi,H <= 3phi-1/8-3eta.                           (0.2)
```

Combining (0.2) by `min` with the merged 4cu residual-coordinate-gcd count

```text
E_xi,g <= 3phi-1/8-rho
```

and retaining the exact pre-relaxation 4cu joint-core inequality yields the stronger forced saving

```text
boxed:
Delta >= 3(chi-1/4)/7                              (0.3)
```

on the nonproportional branch. Exact strip minimax then gives

```text
boxed:
V(B) << B^(47/80+o(1)).                            (0.4)
```

Thus

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=47/80
IMPROVEMENT_OVER_PREVIOUS_19_32=1/160
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

No external large sieve, determinant theorem, genus-one theorem, or H/tH input is used.

---

## 1. Imported common-core-cancelled top-corner structure

Merged s7-33 identifies the primitive agreement Gaussian orientation with the canonical xi residual-host common-core orientation and cancels that large common core from the local transfer equation.

The exact normalized identity is

```text
2*T*lambda_S^2*T_C = g_1*g_2*K*E_S
```

with the conjugate `T`-host companion.

Merged s7-33 also freezes the no-go

```text
K ~ lambda_S*conj(lambda_T)
```

as false pointwise, so s7-34 does not attempt a unique UFD collapse.

Merged 4cu instead compares the residual Gaussian orientation with the xi-plus Cayley orientation through the endpoint linear forms

```text
L_- = z_1*r_2*s_2-z_2*r_1*s_1,
L_+ = z_1*r_2*s_2+z_2*r_1*s_1.                    (1.1)
```

For the nonproportional branch

```text
L_-L_+ != 0
```

one has

```text
|L_-L_+| <= B^(1/4+o(1)).                          (1.2)
```

The balanced strip is

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,                                  (1.3)
```

and the common core has exponent

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4.                               (1.4)
```

The three complete counts already available from s7-32/4cu are

```text
E_s  <= max(2theta,1-2theta),
E_k  <= 3theta-1/4,
E_xi <= 3phi-1/8.                                  (1.5)
```

---

## 2. Exact two-cross-cell decomposition

Same-state reducedness gives

```text
gcd(x_1,y_1)=gcd(x_2,y_2)=1.
```

Therefore every odd common prime of

```text
X=x_1x_2,
Y=y_1y_2
```

occurs crosswise. Define

```text
H_S=oddpart(gcd(x_2,y_1)),
H_T=oddpart(gcd(x_1,y_2)).                          (2.1)
```

Merged 4cu proves exactly

```text
boxed:
H=H_S H_T,
gcd(H_S,H_T)=1,                                   (2.2)
```

where `H` is the common odd root gcd already identified in merged 4cs:

```text
H=oddpart(gcd(X,Y)).                                (2.3)
```

The switched xi hosts are

```text
Z_S=lambda_S^2 W_S,
Z_T=lambda_T^2 W_T.                                (2.4)
```

Put

```text
g_S=oddpart(gcd(Re W_S,Im W_S)),
g_T=oddpart(gcd(Re W_T,Im W_T)).                   (2.5)
```

Merged 4cu proves the matched divisibilities

```text
boxed:
H_S^2 | g_S,
H_T^2 | g_T.                                       (2.6)
```

These are exact integer divisibilities, not exponent inequalities.

---

## 3. New fourth-power transfer to the common xi residual norm

The two switched xi residual norms are equal:

```text
q_S=q_T=:q_xi.                                     (3.1)
```

After the finite 2-primary convention,

```text
oddpart(N(W_S))=q_xi,
oddpart(N(W_T))=q_xi.                              (3.2)
```

For any Gaussian integer `A+iB`,

```text
gcd(A,B)^2 | A^2+B^2.
```

Hence from (2.5),

```text
g_S^2 | q_xi,
g_T^2 | q_xi.                                      (3.3)
```

Combining (2.6) and (3.3),

```text
H_S^4 | q_xi,
H_T^4 | q_xi.                                      (3.4)
```

Because `H_S,H_T` are coprime, their fourth powers multiply:

```text
boxed:
H^4=(H_SH_T)^4 | q_xi.                             (3.5)
```

This is the new exact arithmetic theorem of s7-34.

```text
XI_COMMON_ROOT_GCD_FOURTH_POWER_DIVIDES_QXI=true.
```

It is stronger on the xi side than the older k-side statement

```text
H^2 | q_k.
```

No independence assumption between the two switched hosts is used: the strength comes precisely from their **equal residual norm**.

---

## 4. Fourth-power-divisor one-host count

Dyadically write

```text
H=B^(eta+o(1)).                                     (4.1)
```

Merged s7-32 proves the xi one-host reconstruction theorem:

```text
fixed (q_xi,lambda_S,W_S,finite orientation data)
=> physical collision fiber B^o(1).                (4.2)
```

The raw xi residual norm support is

```text
q_xi <= B^(4phi-1/2+o(1)),                         (4.3)
```

while

```text
#lambda_S <= B^(3/8-phi+o(1)).                     (4.4)
```

By (3.5), write

```text
q_xi=H^4 q_0.                                      (4.5)
```

For a dyadic `H=B^(eta+o(1))`, the number of possible `H` is at most

```text
B^(eta+o(1)),                                      (4.6)
```

and the remaining norm support has exponent

```text
4phi-1/2-4eta.                                     (4.7)
```

Thus the pair `(H,q_0)` costs

```text
eta+(4phi-1/2-4eta)
 =4phi-1/2-3eta.                                   (4.8)
```

For fixed residual norm, the number of Gaussian quotient representations remains divisor-many as in s7-32. Adding the square-divisor norm support (4.4) gives

```text
boxed:
E_xi,H
 <= (3/8-phi)+(4phi-1/2-3eta)
 =3phi-1/8-3eta.                                   (4.9)
```

Therefore

```text
XI_H_DYADIC_COMPLETE_COUNT_EXPONENT=3phi-1/8-3eta.
```

This is a complete alternative count of the same physical block. It is compared by `min`; it is never multiplied into the 4cu residual-gcd saving.

---

## 5. Retain the exact pre-relaxation 4cu joint-core inequality

Choose `star in {S,T}` so that

```text
H_star >= H_other
```

at exponent scale. Write

```text
H_star =B^(eta_star+o(1)),
H_other=B^(eta_other+o(1)),
g_star =B^(rho+o(1)).                              (5.1)
```

Then

```text
eta_star>=eta_other,
eta=eta_star+eta_other,                             (5.2)
```

and merged 4cu gives

```text
rho>=2eta_star.                                    (5.3)
```

Before 4cu relaxed everything to `chi-3rho`, its exact bad-support estimate is

```text
J_star >= B^(chi-2rho-2eta_other-o(1)).            (5.4)
```

On the nonproportional branch, `J_star|L_-L_+` and (1.2), hence

```text
chi-2rho-2eta_other <= 1/4+o(1).                   (5.5)
```

Put

```text
d=max(0,chi-1/4).                                  (5.6)
```

For `d>0`, (5.5) gives

```text
d <= 2rho+2eta_other.                              (5.7)
```

Since `eta_star>=eta_other`,

```text
2eta_other <= eta.                                 (5.8)
```

Therefore

```text
boxed:
d <= 2rho+eta.                                     (5.9)
```

This is the exact interface needed to combine the two complete xi counts.

---

## 6. Forced saving improves from d/3 to 3d/7

Merged 4cu gives the residual-gcd complete count

```text
E_xi,g <= 3phi-1/8-rho.                            (6.1)
```

Section 4 gives

```text
E_xi,H <= 3phi-1/8-3eta.                           (6.2)
```

Hence

```text
E_xi
 <=3phi-1/8-max(rho,3eta).                         (6.3)
```

Define

```text
Delta=max(rho,3eta).                               (6.4)
```

Then

```text
rho<=Delta,
eta<=Delta/3.                                      (6.5)
```

Using (5.9),

```text
d
 <=2rho+eta
 <=2Delta+Delta/3
 =7Delta/3.                                        (6.6)
```

Therefore

```text
boxed:
Delta >= 3d/7.                                     (6.7)
```

Equivalently, whenever `chi>1/4`,

```text
boxed:
E_xi
 <=3phi-1/8
   -3(chi-1/4)/7.                                  (6.8)
```

Thus

```text
NONPROPORTIONAL_FORCED_SAVING=3*(chi-1/4)/7.
```

This is strictly stronger than the `4cu` relaxation

```text
rho >= (chi-1/4)/3
```

because it uses the fourth-power common-root sparsity whenever the endpoint-core pressure is carried by `H_other` rather than by `g_star` alone.

---

## 7. Exact whole-strip minimax

For `chi<=1/4`, no new saving is needed. The existing complete-count envelope satisfies

```text
E<=11/20.                                          (7.1)
```

Now assume `chi>1/4`. Combine

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4,
E_xi<=3phi-1/8-3(chi-1/4)/7.                       (7.2)
```

Since

```text
chi=2theta+2phi-3/4,
```

and `phi<=1/4`,

```text
E_xi
 <= 47/56 - 6theta/7.                              (7.3)
```

In the relevant region `theta>1/4`, the s-count is

```text
E_s=2theta.                                        (7.4)
```

The two active envelopes meet at

```text
2theta=47/56-6theta/7,
```

i.e.

```text
boxed:
theta=47/160,
E=47/80.                                           (7.5)
```

The exact rational strip audit confirms that this is the unique maximum of the proved nonproportional envelope, attained only when

```text
boxed:
theta=47/160,
phi=1/4,
chi=27/80.                                         (7.6)
```

The k one-host count there is larger:

```text
E_k=101/160>47/80.                                 (7.7)
```

Merged 4cu already bounds the proportional branch by

```text
E_prop<=9/16<47/80.                                (7.8)
```

Therefore every physical block satisfies

```text
boxed:
E<=47/80.                                          (7.9)
```

Hence

```text
boxed:
V(B) << B^(47/80+o(1)).                            (7.10)
```

The gain over merged 4cu is

```text
19/32-47/80=1/160.                                 (7.11)
```

---

## 8. Equality profile of the new envelope

At the new possible saturation point

```text
theta=47/160,
phi=1/4,
chi=27/80,                                         (8.1)
```

we have

```text
d=chi-1/4=7/80.                                   (8.2)
```

To attain equality in the forced-saving inequality, both complete xi counts must tie:

```text
rho=3eta=3/80.                                     (8.3)
```

Hence

```text
boxed:
eta=1/80,
rho=3/80.                                         (8.4)
```

Equality in

```text
2eta_other<=eta
```

also requires balanced cross-root cells:

```text
boxed:
eta_S=eta_T=1/160.                                 (8.5)
```

The joint-core exponent is then exactly

```text
chi-2rho-2eta_other
 =27/80-6/80-1/80
 =1/4.                                             (8.6)
```

Thus any packet saturating the new `47/80` envelope must obey

```text
H_S,H_T = B^(1/160+o(1)),
H       = B^(1/80+o(1)),
g_star  = B^(3/80+o(1)),
J_star  = B^(1/4+o(1)).                            (8.7)
```

The matched mandatory root square inside `g_star` has exponent only

```text
2eta_star=1/80,
```

while the selected residual coordinate gcd has exponent `3/80`. Therefore a genuinely extra residual coordinate-gcd factor of exponent

```text
3/80-1/80=1/40                                    (8.8)
```

must remain beyond the cross-root square forced by 4cu.

This is the next exact obstruction.

---

## 9. New minimal receiver

The old 4cu receiver

```text
NineteenThirtySecondsJointCoreCayleyResidualLinearProductIncidence
```

is no longer minimal. Any possible `47/80` saturation must satisfy all of

```text
(theta,phi)=(47/160,1/4),
C=B^(27/80+o(1)),
H_S,H_T=B^(1/160+o(1)),
H=B^(1/80+o(1)),
g_star=B^(3/80+o(1)),
J_star=B^(1/4+o(1)),
J_star|L_-L_+,
|L_-L_+|=B^(1/4+o(1)),
H_star^2|g_star,
log_B(g_star/H_star^2)=1/40+o(1).                  (9.1)
```

Define the new receiver

```text
FortySevenEightiethsExtraXiResidualGcdJointCoreLinearFactorIncidence.   (9.2)
```

Its distinctive feature is that the surviving `g_star` is much larger than the cross-root square that was already explained by `H_star`. The next stage should classify the prime support of this **extra** coordinate-gcd factor and determine whether it must lie in `C`, in `v_res`, in switched-cell support, or in a small overlap of those sets.

---

## 10. H / tH decision

No auxiliary H/tH theorem is needed at s7-34.

The reason is now especially concrete: the live `1/40` extra residual-coordinate-gcd factor has not yet been primewise decomposed. This is still an exact valuation/gcd problem, not a stable averaged-incidence theorem.

Therefore

```text
S7_34_AUXILIARY_H_NEEDED=false
TH18_CROSS_PROMOTED_TO_S7_34=false
T72_CROSS_PROMOTED_TO_S7_34=false
T73_CROSS_PROMOTED_TO_S7_34=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

A new s-specific H target should be considered only if s7-35 peels the extra gcd support completely and leaves a genuinely averaged incidence problem.

---

## 11. Next stage

`Stage14-s7-35` should start from the equality profile (8.7) and write

```text
g_star = H_star^2 * G_extra
```

up to the already-known `B^o(1)` overlap decoration, with

```text
G_extra=B^(1/40+o(1)).                              (11.1)
```

The first task is primewise classification of `G_extra` against

```text
C,
v_res,
S*T,
T_C,
E_S,
L_-,L_+,
```

using the common-core-cancelled s7-33 transfer equation and the 4cu joint-core sign allocation.

Do not invoke a large sieve or H theorem before this support classification is exhausted.

---

## Stage boundary

```text
STAGE14_S7_34=COMPLETE_XI_FOURTH_POWER_ROOT_GCD_TRANSFER_AND_47_80_PROMOTION
MERGED_S7_33_IMPORTED=true
MERGED_4CU_IMPORTED=true
XI_COMMON_ROOT_GCD_FOURTH_POWER_DIVIDES_QXI=true
XI_H_DYADIC_COMPLETE_COUNT_EXPONENT=3phi-1/8-3eta
FOUR_CU_RESIDUAL_GCD_COMPLETE_COUNT_REUSED=true
FOUR_CU_PRE_RELAXATION_JOINT_CORE_INEQUALITY_RETAINED=true
NONPROPORTIONAL_FORCED_SAVING=3*(chi-1/4)/7
LOW_CORE_REGION_UPPER_BOUND_EXPONENT=11/20
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=47/80
IMPROVEMENT_OVER_PREVIOUS_19_32=1/160
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
FORTY_SEVEN_EIGHTIETHS_SATURATION_THETA=47/160
FORTY_SEVEN_EIGHTIETHS_SATURATION_PHI=1/4
FORTY_SEVEN_EIGHTIETHS_SATURATION_COMMON_CORE_EXPONENT=27/80
FORTY_SEVEN_EIGHTIETHS_SATURATION_H_EXPONENT=1/80
FORTY_SEVEN_EIGHTIETHS_SATURATION_CROSS_HS_EXPONENT=1/160
FORTY_SEVEN_EIGHTIETHS_SATURATION_CROSS_HT_EXPONENT=1/160
FORTY_SEVEN_EIGHTIETHS_SATURATION_SELECTED_XI_GCD_EXPONENT=3/80
FORTY_SEVEN_EIGHTIETHS_SATURATION_JOINT_CORE_EXPONENT=1/4
FORTY_SEVEN_EIGHTIETHS_EXTRA_XI_GCD_EXPONENT=1/40
REMAINING_RECEIVER=FortySevenEightiethsExtraXiResidualGcdJointCoreLinearFactorIncidence
S7_34_AUXILIARY_H_NEEDED=false
TH18_CROSS_PROMOTED_TO_S7_34=false
T72_CROSS_PROMOTED_TO_S7_34=false
T73_CROSS_PROMOTED_TO_S7_34=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-35
```
