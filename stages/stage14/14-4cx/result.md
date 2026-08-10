# Stage14-4cx — Cayley-annulus collapse, full lost-core column divisor, and the 23/44 bound

## Status

`COMPLETE_CAYLEY_ANNULUS_COLLAPSE_FULL_LOST_CORE_COLUMN_DIVISOR_AND_23_44_PROMOTION`

Stage14-4cx consumes merged `4cw`, merged `s7-38`, merged `X12`, merged `s7-35`, and the Cayley-good-core construction of `4cq/4cs`.

The entering canonical theorem is

```text
V(B) << B^(61/112+o(1)).
```

The `61/112` equality packet retained an apparent Cayley-only annulus

```text
A_C=C_Cayley/J
```

of exponent `3/56`.  The first result of 4cx is that this fixed-power annulus is impossible.  The annulus is a quotient of the selected residual-bad support, but the Cayley-good core is coprime to the Cayley numerator.  Since the selected cross-root gcd divides that numerator, only endpoint-small support can remain in `A_C`.

This strengthens the X12 fourth-root lost-core transfer to a full lost-core divisor of the endpoint-linear column cofactor product.  In particular every fixed-power nonproportional block with

```text
chi>1/4
```

is empty.  On the surviving `chi<=1/4` region the entire lost core is removed from the column support, and the new charged-once ledger gives

```text
boxed:
V(B) << B^(23/44+o(1)).
```

No external incidence theorem, sieve theorem, determinant theorem, genus-one theorem, or auxiliary H/tH theorem is used.

---

## 1. Imported balanced packet

Use the balanced strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Write

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4.                               (1.1)
```

The proportional branch is already strictly subcritical by merged `s7-37`:

```text
E_prop<=7/16.                                      (1.2)
```

Hence only the nonproportional branch

```text
L_-L_+ != 0
```

needs to be treated.

Retain the complete counts

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.                                   (1.3)
```

Let the two cross-root cells be

```text
H_star,
H_other,
H=H_star*H_other,
gcd(H_star,H_other)=1,
```

and write

```text
H=B^(s+o(1)).                                      (1.4)
```

Merged `s7-34/s7-35` gives the fourth-power-root complete count

```text
boxed:
E_H<=3phi-1/8-3s.                                  (1.5)
```

---

## 2. Cayley-good core and selected residual-good core

Let

```text
C_Cayley | C
```

be the Cayley-good core of merged `4cq/4cs/4cu`.

Let the selected residual coordinate gcd be `g_star`.  Merged `s7-35` proves an exact endpoint-small quotient relation

```text
g_star/H_star^2 | Omega_1,
Omega_1=B^o(1).                                    (2.1)
```

The selected residual-good core is

```text
C_res=C/gcd(C,g_star^2).                            (2.2)
```

The joint core is

```text
J=gcd(C_Cayley,C_res).                             (2.3)
```

Define

```text
A_C:=C_Cayley/J.                                   (2.4)
```

Merged `s7-38/4cw` treated `A_C` as potentially fixed-power.  Stage14-4cx now eliminates that possibility.

---

## 3. The Cayley-good core is coprime to the Cayley numerator

Use the 4cq notation

```text
M=4*r*s*X*Y*epsilon_x*epsilon_k,
N=a*b*c*d.
```

The Cayley-good core is exactly the modulus on which the two Cayley ratios are units and satisfy

```text
lambda*x*y == 4 (mod C_Cayley),
```

with

```text
lambda=4*M/N.                                      (3.1)
```

Merged 4cq already proves that `N` is a unit modulo `C_Cayley`.  The two Cayley ratios are also units there.  Therefore (3.1) forces `lambda`, and hence `M`, to be a unit modulo `C_Cayley`:

```text
boxed:
gcd(C_Cayley,M*N)=1.                              (3.2)
```

The cross-root gcd satisfies

```text
H=oddpart(gcd(X,Y)).                               (3.3)
```

Hence `H|M`, and therefore

```text
boxed:
gcd(C_Cayley,H)=1.                                (3.4)
```

In particular

```text
boxed:
gcd(C_Cayley,H_star)=1.                           (3.5)
```

This is the prime-support fact that was not yet fed back into the `61/112` annulus ledger.

---

## 4. Exact collapse of the Cayley-only annulus

We first use an elementary divisor identity.

If `A,B|C`, then

```text
A/gcd(A,B) | C/B.                                  (4.1)
```

Apply (4.1) with

```text
A=C_Cayley,
B=C_res.
```

Using (2.2)--(2.4),

```text
A_C
 = C_Cayley/gcd(C_Cayley,C_res)
 | C/C_res
 = gcd(C,g_star^2)
 | g_star^2.                                       (4.2)
```

By (2.1), write

```text
g_star=H_star^2*e,
e|Omega_1.                                         (4.3)
```

Therefore

```text
A_C | H_star^4*Omega_1^2.                          (4.4)
```

But `A_C|C_Cayley`, so (3.5) gives

```text
gcd(A_C,H_star)=1.                                 (4.5)
```

Cancelling the `H_star`-supported prime powers from (4.4),

```text
boxed:
A_C | Omega_1^2.                                   (4.6)
```

Since `Omega_1=B^o(1)`, we obtain

```text
boxed:
A_C=B^o(1).                                        (4.7)
```

Thus

```text
boxed:
C_Cayley/J=B^o(1).                                 (4.8)
```

Equivalently, at exponent scale

```text
log_B C_Cayley = log_B J + o(1).                  (4.9)
```

The old `61/112` saturation condition

```text
C_Cayley/J=B^(3/56+o(1))
```

is therefore impossible.

```text
CAYLEY_ONLY_ANNULUS_FIXED_POWER_EMPTY=true.
```

---

## 5. The whole lost core is supported on the cross-root gcd

Define the lost core

```text
D:=C/J.                                             (5.1)
```

Factor it as

```text
D=(C/C_Cayley)*(C_Cayley/J).                       (5.2)
```

Merged `4cs/4cu/X12` gives an endpoint-small integer `Omega_2=B^o(1)` such that

```text
C/C_Cayley | Omega_2*H^2.                          (5.3)
```

Together with (4.6), there is an endpoint-small

```text
Omega_0=B^o(1)
```

for which

```text
boxed:
D | Omega_0*H^2.                                   (5.4)
```

Remove the endpoint-small valuation contribution by

```text
D_0:=D/gcd(D,Omega_0).                              (5.5)
```

Primewise, (5.4) implies

```text
boxed:
D_0 | H^2.                                         (5.6)
```

Also

```text
D_0=B^(chi-j+o(1))                                 (5.7)
```

when

```text
J=B^(j+o(1)),                                      (5.8)
```

because `Omega_0=B^o(1)`.

This replaces the X12 fourth-root inclusion

```text
R_4(D_0)|H
```

by the stronger full square-support statement

```text
D_0|H^2.
```

---

## 6. The full lost core divides the column cofactor product

Merged X12 proves

```text
boxed:
H | gcd(L_-,L_+).                                  (6.1)
```

The joint core satisfies

```text
J|C_Cayley.
```

By (3.4),

```text
boxed:
gcd(J,H)=1.                                        (6.2)
```

Write the column allocation

```text
J_L-*J_L+=J,
J_L- | L_-,
J_L+ | L_+,

L_-=J_L-*h_-,
L_+=J_L+*h_+.                                      (6.3)
```

Because every prime of `J_L- J_L+` is coprime to `H`, (6.1) survives the division in both columns:

```text
boxed:
H|h_-,
H|h_+.                                             (6.4)
```

Hence

```text
H^2|h_-h_+.                                        (6.5)
```

Together with (5.6),

```text
boxed:
D_0 | h_-h_+.                                      (6.6)
```

This is strictly stronger than the X12 theorem

```text
R_4(D_0)|h_-h_+.
```

The strengthening is legal because 4cx first proves that the Cayley-only annulus is endpoint-small; this is what makes the whole fixed-power lost core cross-root supported.

```text
FULL_LOST_CORE_DIVIDES_COLUMN_COFACTOR_PRODUCT=true.
```

---

## 7. Fixed-power high-core nonproportional blocks are empty

On the nonproportional branch,

```text
0<|L_-L_+|<=B^(1/4+o(1)).                          (7.1)
```

Since `J_L-J_L+=J`,

```text
|h_-h_+|
 = |L_-L_+|/J
 <= B^(1/4-j+o(1)).                                (7.2)
```

But (5.7) and (6.6) give a forced divisor

```text
D_0=B^(chi-j+o(1))
```

inside the nonzero integer `h_-h_+`.  Therefore every physical nonproportional packet satisfies

```text
chi-j <= 1/4-j+o(1),
```

hence

```text
boxed:
chi<=1/4+o(1).                                     (7.3)
```

Thus for every fixed `delta>0`,

```text
chi>=1/4+delta
```

contains no asymptotic nonproportional packets.

```text
FIXED_POWER_HIGH_CORE_NONPROPORTIONAL_BRANCH_EMPTY=true.
```

The `61/112` equality point had

```text
chi=33/112>1/4,
```

so it is eliminated completely.

---

## 8. Low-core column support after removing the lost core

It remains to count

```text
chi<=1/4.                                          (8.1)
```

Fix `C,J,D_0` and the divisor-many allocation of `D_0` between `h_-` and `h_+`.  Dividing the product by the forced divisor (6.6), the remaining ordered column-cofactor support has exponent

```text
(1/4-j)-(chi-j)=1/4-chi.                           (8.2)
```

Thus

```text
boxed:
E_col,res<=1/4-chi.                                (8.3)
```

No separate `J` or `D_0` support is charged: both are divisors of the once-charged common core and are fixed before the cofactor count.

---

## 9. Row lift after annulus collapse

By (4.8), the full Cayley row and the joint core have the same exponent:

```text
C_Cayley=J*B^o(1).                                 (9.1)
```

Merged 4cs/4cu gives

```text
C/C_Cayley | B^o(1)*H^2.
```

Hence, with `H=B^(s+o(1))`,

```text
j>=chi-2s-o(1).                                    (9.2)
```

Once the column reconstructs `M`, the full Cayley-row CRT determines

```text
N=abcd
```

modulo `C_Cayley`.  Since `N<=B^(1/4+o(1))`, the row-lift support is

```text
E_row<=max(0,1/4-j).                               (9.3)
```

On the low-core region (8.1), (9.2) gives

```text
boxed:
E_row<=1/4-chi+2s.                                 (9.4)
```

---

## 10. New charged-once low-core complete count

The common-core and first primitive-pair cost remains

```text
C:                     chi,
primitive root-line:    2phi-chi,
```

hence exactly `2phi`.

Add only the residual column quotient (8.3) and the row lift (9.4):

```text
boxed:
E_DRC
 <=2phi
   +(1/4-chi)
   +(1/4-chi+2s)
 =2phi+1/2-2chi+2s.                                (10.1)
```

For the same physical block, (1.5) gives

```text
E_H<=3phi-1/8-3s.                                  (10.2)
```

These are alternative complete counts, so

```text
E<=min(E_H,E_DRC).                                 (10.3)
```

Use

```text
min(E_H,E_DRC)
 <=(2E_H+3E_DRC)/5.                                (10.4)
```

The `s` coefficient cancels exactly:

```text
2*(-3)+3*2=0.
```

Therefore

```text
E
 <=(12phi+5/4-6chi)/5
 =23/20-(12/5)theta.                               (10.5)
```

The right side is independent of `phi`.

```text
LOW_CORE_WEIGHTED_COMPLETE_COUNT_COMBINATION=2:3.
```

---

## 11. Whole-strip minimax and the 23/44 bound

### 11.1. `theta<=1/4`

From (1.3),

```text
E<=E_k<=1/2<23/44.                                 (11.1)
```

### 11.2. `1/4<=theta<=23/88`

Here

```text
E_s=2theta,
```

so

```text
E<=2theta<=23/44.                                  (11.2)
```

### 11.3. `theta>=23/88` and `chi<=1/4`

Use (10.5):

```text
E
 <=23/20-(12/5)theta
 <=23/44.                                          (11.3)
```

### 11.4. `chi>1/4`

This fixed-power nonproportional region is empty by Section 7.

### 11.5. Proportional branch

Merged s7-37 gives

```text
E_prop<=7/16<23/44.                                (11.4)
```

Therefore the whole physical family satisfies

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44.
```

Relative to merged 4cw,

```text
61/112-23/44=27/1232.                              (11.5)
```

The gap to square-root scale is

```text
23/44-1/2=1/44.                                    (11.6)
```

Thus

```text
IMPROVEMENT_OVER_MERGED_4CW_61_112=27/1232
CURRENT_GAP_TO_SQRT=1/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

---

## 12. Exact saturation segment

The whole-family bound can be saturated only when

```text
theta=23/88.                                       (12.1)
```

For the weighted minimum in Section 10 to be sharp, the intersection of (10.1) and (10.2) must occur at nonnegative `s`.

Solving

```text
E_H=E_DRC
```

gives

```text
s=(4theta+5phi-17/8)/5.                            (12.2)
```

At `theta=23/88`,

```text
boxed:
s=phi-19/88.                                      (12.3)
```

Hence `s>=0` requires

```text
phi>=19/88.                                        (12.4)
```

The low-core condition `chi<=1/4` gives

```text
phi<=21/88.                                        (12.5)
```

Therefore the exact saturation segment is

```text
boxed:
theta=23/88,
19/88<=phi<=21/88.                                 (12.6)
```

Along this segment,

```text
s=phi-19/88,
0<=s<=1/44.                                        (12.7)
```

The common-core exponent is

```text
chi=2phi-5/22,
9/44<=chi<=1/4.                                    (12.8)
```

Equality in the Cayley-good-core lower bound gives

```text
j=chi-2s=9/44,                                     (12.9)
```

independent of `phi`.  By the annulus collapse,

```text
C_Cayley=J*B^o(1)=B^(9/44+o(1)).                  (12.10)
```

The lost core has exponent

```text
chi-j=2s.                                          (12.11)
```

Thus at saturation

```text
D_0=B^(2s+o(1)),
D_0~H^2 at exponent scale.                         (12.12)
```

The row lift is constant:

```text
1/4-j=1/22.                                       (12.13)
```

The remaining column quotient decreases linearly:

```text
1/4-chi
 =1/22-2s
 =21/44-2phi.                                      (12.14)
```

Hence the equality ledger is

```text
C + primitive pair:          2phi,
forced lost-core divisor:    2s,
residual column support:      1/22-2s,
full Cayley row lift:         1/22,
--------------------------------------
total charged count:          23/44.
```

The forced divisor itself is not charged as a free parameter; (12.15) is a structural ledger showing how the raw column support is consumed.

---

## 13. New minimal receiver

The previous receiver

```text
SixtyOneOneHundredTwelfthsFullCayleyRowFourthRootColumnShortLiftIncidence
```

is superseded.

The new receiver is

```text
TwentyThreeFortyFourthsCayleyAnnulusCollapseLostCoreColumnRowLiftTradeoff.
```

Any possible saturation packet lies on

```text
theta=23/88,
19/88<=phi<=21/88,
H=B^(phi-19/88+o(1)),
C=B^(2phi-5/22+o(1)),
J=C_Cayley=B^(9/44+o(1)),
D_0=B^(2phi-19/44+o(1)),
residual column quotient<=B^(21/44-2phi+o(1)),
row CRT lift<=B^(1/22+o(1)).                       (13.1)
```

The next exact task is to substitute

```text
D_0 | h_-h_+,
N=N_0(M)+C_Cayley*m,
|m|<=B^(1/22+o(1))
```

back into the reciprocal signed-quotient equations, preserving the `phi`-segment tradeoff.  In particular, 4cy should determine whether the constant `1/22` row lift is actually independent of the shrinking residual column quotient after the full lost-core factor has been removed.

---

## 14. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH21_CROSS_PROMOTED_TO_MAINLINE=false
T76_CROSS_PROMOTED_TO_MAINLINE=false
```

The improvement is entirely internal arithmetic: divisor identities, Cayley unit support, cross-root support, and charged-once reconstruction.

Merged `tH21` remains a fixed-U coefficient-space applicability result and is not an input to this theorem.  A new H line should be considered only if Stage14-4cy exhausts the exact row-lift/column-quotient coupling and leaves a genuine averaged incidence problem on the minimized `23/44` packet.

---

## Stage boundary

```text
STAGE14_4CX=COMPLETE_CAYLEY_ANNULUS_COLLAPSE_FULL_LOST_CORE_COLUMN_DIVISOR_AND_23_44_PROMOTION
MERGED_4CW_61_112_IMPORTED=true
MERGED_S7_38_COMPATIBILITY_CHECKED=true
MERGED_X12_IMPORTED=true
CAYLEY_GOOD_CORE_COPRIME_TO_MN=true
CAYLEY_GOOD_CORE_COPRIME_TO_CROSS_ROOT_GCD=true
CAYLEY_ONLY_ANNULUS_DIVIDES_ENDPOINT_SMALL_SQUARE=true
CAYLEY_ONLY_ANNULUS_FIXED_POWER_EMPTY=true
CAYLEY_ONLY_ANNULUS_EXPONENT=0
LOST_CORE_ENDPOINT_PEELED_DIVIDES_H_SQUARE=true
JOINT_CORE_COPRIME_TO_CROSS_ROOT_GCD=true
CROSS_ROOT_GCD_DIVIDES_BOTH_COLUMN_COFACTORS=true
FULL_LOST_CORE_DIVIDES_COLUMN_COFACTOR_PRODUCT=true
FIXED_POWER_HIGH_CORE_NONPROPORTIONAL_BRANCH_EMPTY=true
LOW_CORE_RESIDUAL_COLUMN_SUPPORT_EXPONENT=1/4-chi
LOW_CORE_ROW_LIFT_EXPONENT=1/4-chi+2s
LOW_CORE_COMPLETE_COUNT=2phi+1/2-2chi+2s
LOW_CORE_WEIGHTED_COMPLETE_COUNT_COMBINATION=2:3
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=23/44
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44
IMPROVEMENT_OVER_MERGED_4CW_61_112=27/1232
CURRENT_GAP_TO_SQRT=1/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
TWENTYTHREE_44_SATURATION_THETA=23/88
TWENTYTHREE_44_SATURATION_PHI_MIN=19/88
TWENTYTHREE_44_SATURATION_PHI_MAX=21/88
TWENTYTHREE_44_CROSS_ROOT_EXPONENT=s=phi-19/88
TWENTYTHREE_44_COMMON_CORE_EXPONENT=2phi-5/22
TWENTYTHREE_44_JOINT_CORE_EXPONENT=9/44
TWENTYTHREE_44_CAYLEY_GOOD_CORE_EXPONENT=9/44
TWENTYTHREE_44_CAYLEY_ANNULUS_EXPONENT=0
TWENTYTHREE_44_LOST_CORE_EXPONENT=2s
TWENTYTHREE_44_RESIDUAL_COLUMN_SUPPORT_EXPONENT=1/22-2s
TWENTYTHREE_44_ROW_LIFT_EXPONENT=1/22
REMAINING_RECEIVER=TwentyThreeFortyFourthsCayleyAnnulusCollapseLostCoreColumnRowLiftTradeoff
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH21_CROSS_PROMOTED_TO_MAINLINE=false
T76_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cy
```
