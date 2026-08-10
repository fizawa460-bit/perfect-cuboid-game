# Stage14-4cw — lost-core fourth root plus full Cayley-row CRT and the 61/112 bound

## Status

`COMPLETE_LOST_CORE_FOURTH_ROOT_FULL_CAYLEY_ROW_AND_61_112_PROMOTION`

Stage14-4cw consumes merged `X12`, `X11`, `s7-37`, `s7-35`, `4cv`, and the Cayley-good-core structure of `4cr/4cu`.

Current main enters with X12's

```text
V(B) << B^(71/128+o(1)).
```

X12 strengthens the nonproportional column by proving that a fourth root of the lost core `C/J` divides the column cofactor product.  Independently, the 4cw quantifier order observes that after the `J`-column has fixed `M`, the Cayley row CRT can use the entire already-fixed Cayley-good core `C_Cayley`, not only `J`.

Combining both exact facts removes more of the two short supports and yields

```text
boxed:
V(B) << B^(61/112+o(1)).
```

No external H/tH theorem is used.

---

## 1. Imported exponents

Use

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4,
3/16<=theta<=5/16,
1/8<=phi<=1/4,
0<=theta-phi<=1/8,
theta+phi>=3/8.
```

On a nonproportional packet write

```text
H_star=B^(a+o(1)),
H_other=B^(b+o(1)),
a>=b>=0.
```

Merged s7-35 gives

```text
g_star=H_star^2*B^o(1),
```

and merged s7-34/X12 give the complete fourth-power-root count

```text
boxed:E_H<=3phi-1/8-3a-3b.                         (1.1)
```

Let

```text
J=B^(j+o(1))
```

be the residual/Cayley joint core.  The pre-relaxation lower bound is

```text
boxed:j>=chi-4a-2b.                                 (1.2)
```

Let the full Cayley-good core be

```text
C_Cayley=B^(c_y+o(1)).
```

Merged 4cu gives

```text
C/C_Cayley | B^o(1)*(H_star H_other)^2,
```

hence

```text
boxed:c_y>=chi-2a-2b.                               (1.3)
```

Thus

```text
J | C_Cayley | C.
```

---

## 2. X12 fourth root removes part of the column cofactor

The nonproportional endpoint-linear forms are

```text
L_-=z1*r2*s2-z2*r1*s1,
L_+=z1*r2*s2+z2*r1*s1,
0<|L_-L_+|<=B^(1/4+o(1)).
```

On `J`, write

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
J_L-*J_L+=J.
```

The raw cofactor-product exponent is

```text
1/4-j.
```

Merged X12 sets

```text
D=C/J
```

and proves, after only endpoint-small support is peeled, that

```text
R4(D) | h_-h_+,
log_B R4(D) >= (chi-j)/4-o(1).                     (2.1)
```

Therefore the **effective** moving column support has exponent

```text
ell_col
 <= max(0, 1/4-j-(chi-j)/4)
 =  max(0, 1/4-chi/4-3j/4).                        (2.2)
```

Using (1.2),

```text
boxed:
ell_col<=max(0,3a+(3/2)b-d),
d:=chi-1/4.                                         (2.3)
```

Fixing the remaining column cofactor reconstructs `(z1,z2)` and hence

```text
M=4rsXY*epsilon_x*epsilon_k
```

with divisor-many multiplicity.

---

## 3. Full Cayley row after `M` is fixed

Merged 4cr allocates the entire Cayley-good core as

```text
C_Cayley=C_-*C_+,
gcd(C_-,C_+)=1,
C_-|M-N,
C_+|M+N,
N=abcd.
```

These are Cayley row congruences and do not require the selected residual host to remain primitive.  Once the column has fixed `M`, CRT therefore gives

```text
boxed:N=N_0(M) mod C_Cayley.                        (3.1)
```

Since `N<=B^(1/4+o(1))`, the full-row lift exponent is

```text
ell_row<=max(0,1/4-c_y)
        <=max(0,2a+2b-d).                           (3.2)
```

Fixed `N` leaves only divisor-many signed quotient quadruples.

This uses one already-fixed common core sequentially:

```text
C charged once
-> J-column fixes M
-> full C_Cayley-row fixes N mod C_Cayley.
```

No modulus product `J*C_Cayley` is charged.

```text
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false.          (3.3)
```

---

## 4. New complete reconstruction count

The outer common-core plus primitive-pair cost is exactly

```text
B^(2phi+o(1)).
```

Hence the X12+full-row reconstruction count is

```text
boxed:
E_F4<=2phi
     +max(0,3a+(3/2)b-d)
     +max(0,2a+2b-d).                               (4.1)
```

Compare (4.1) with the complete fourth-power count (1.1).

There are three cases.

### Case 0: effective column support is zero

If

```text
3a+(3/2)b<=d,
```

then also `2a+2b<=d` because `a>=b`.  Thus

```text
E_F4<=2phi<=1/2.
```

This branch is already below the square-root scale.

### Case A: column positive, full-row lift zero

Assume

```text
3a+(3/2)b>=d,
2a+2b<=d.
```

Then

```text
E_F4<=2phi+3a+(3/2)b-d.
```

The equal-weight average cancels `a`:

```text
min(E_H,E_F4)<=(E_H+E_F4)/2
```

and leaves a favorable `-3b/4`.  Hence

```text
E<= (3phi-2theta+7/8)/2-(3/4)b
 <= (3phi-2theta+7/8)/2.                            (4.2)
```

With `phi<=1/4`,

```text
boxed:E<=13/16-theta.                               (4.3)
```

### Case B: both column and full-row lift positive

Assume

```text
2a+2b>=d.
```

Then automatically the column term is positive and

```text
E_F4<=2phi+5a+(7/2)b-2d.                            (4.4)
```

Use

```text
min(E_H,E_F4)<=(5E_H+3E_F4)/8.
```

The selected exponent cancels:

```text
5*(-3)+3*5=0,
```

while the `b` coefficient is negative.  Therefore

```text
E<= (9phi-12theta+43/8)/8-(9/16)b
 <= (9phi-12theta+43/8)/8.                          (4.5)
```

Using `phi<=1/4`,

```text
boxed:E<=61/64-(3/2)theta.                          (4.6)
```

---

## 5. Whole-strip minimax

Retain merged complete counts

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.
```

If `theta<=1/4`, then

```text
E_k<=1/2<61/112.
```

If

```text
1/4<=theta<=61/224,
```

then

```text
E_s=2theta<=61/112.
```

Now let `theta>=61/224`.

Case 0 is `<=1/2`.

Case A gives, using (4.3),

```text
E<=13/16-61/224=121/224<61/112.
```

Case B gives

```text
E<=61/64-(3/2)(61/224)=61/112.
```

and decreases strictly for larger theta.

Thus

```text
boxed:NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=61/112.       (5.1)
```

Merged s7-37 gives

```text
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16<61/112.
```

Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112
IMPROVEMENT_OVER_MERGED_X12_71_128=9/896
IMPROVEMENT_OVER_MERGED_X11_19_34=27/1904
CURRENT_GAP_TO_SQRT=5/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.          (5.2)
```

---

## 6. Unique saturation profile

Equality can occur only in Case B and requires

```text
boxed:
theta=61/224,
phi=1/4.                                            (6.1)
```

Then

```text
chi=33/112,
d=5/112.
```

Equality in the `5:3` comparison forces

```text
boxed:a=3/112,
b=0.                                                (6.2)
```

Hence

```text
rho=2a=3/56,
j=chi-4a=3/16,
c_y=chi-2a=27/112.                                 (6.3)
```

The lost-core exponent is

```text
chi-j=3/28,
```

so the X12 forced fourth-root exponent is

```text
(chi-j)/4=3/112.                                   (6.4)
```

The short-support ledger becomes

```text
raw column support:          1/4-j = 1/16,
forced lost-core fourth root:          3/112,
effective column support:               1/28,
full Cayley row N-lift:                  1/112.
```

Thus

```text
1/2 + 1/28 + 1/112 = 61/112.
```

The fourth-power count also equals `61/112` at this profile.

---

## 7. Remaining receiver

The new minimal receiver is

```text
SixtyOneOneHundredTwelfthsLostCoreFourthRootFullCayleyRowAsymmetricShortLiftIncidence.
```

Any possible saturation packet must satisfy

```text
theta=61/224,
phi=1/4,
chi=33/112,
H_star=B^(3/112+o(1)),
H_other=B^o(1),
g_star=B^(3/56+o(1)),
J=B^(3/16+o(1)),
C_Cayley=B^(27/112+o(1)),
C/J=B^(3/28+o(1)),
R4(C/J)=B^(3/112+o(1)),
effective column cofactor support=B^(1/28+o(1)),
full-row N-lift support=B^(1/112+o(1)).             (7.1)
```

The next exact task is to compare the small full-row lift with the effective column cofactor after substituting the unique row residue

```text
N=N_0(M)+C_Cayley*m,
```

into the reciprocal signed-quotient system.  No external average is yet required.

---

## 8. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T76_CROSS_PROMOTED_TO_MAINLINE=false
```

Reason: the remaining receiver is still two explicit short integer lifts tied to one exact CRT/factorization system.  Pointwise arithmetic remains unexhausted.

---

## Stage boundary

```text
STAGE14_4CW=COMPLETE_LOST_CORE_FOURTH_ROOT_FULL_CAYLEY_ROW_AND_61_112_PROMOTION
MERGED_X12_IMPORTED=true
MERGED_X11_IMPORTED=true
MERGED_S7_37_IMPORTED=true
X12_LOST_CORE_FOURTH_ROOT_COLUMN_SAVING_IMPORTED=true
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_PROVED=true
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false
EFFECTIVE_COLUMN_COFACTOR_EXPONENT=max(0,1/4-chi/4-3j/4)
FULL_ROW_N_LIFT_EXPONENT=max(0,1/4-chi+2a+2b)
NONPROPORTIONAL_CASE_ZERO_BOUND_EXPONENT=1/2
NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=1:1
NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=5:3
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=61/112
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112
IMPROVEMENT_OVER_MERGED_X12_71_128=9/896
IMPROVEMENT_OVER_MERGED_X11_19_34=27/1904
CURRENT_GAP_TO_SQRT=5/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SIXTYONE_112_SATURATION_THETA=61/224
SIXTYONE_112_SATURATION_PHI=1/4
SIXTYONE_112_COMMON_CORE_EXPONENT=33/112
SIXTYONE_112_SELECTED_CROSS_ROOT_EXPONENT=3/112
SIXTYONE_112_OTHER_CROSS_ROOT_EXPONENT=0
SIXTYONE_112_SELECTED_RESIDUAL_GCD_EXPONENT=3/56
SIXTYONE_112_JOINT_CORE_EXPONENT=3/16
SIXTYONE_112_CAYLEY_GOOD_CORE_EXPONENT=27/112
SIXTYONE_112_LOST_CORE_EXPONENT=3/28
SIXTYONE_112_FORCED_FOURTH_ROOT_EXPONENT=3/112
SIXTYONE_112_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=1/28
SIXTYONE_112_FULL_ROW_LIFT_EXPONENT=1/112
REMAINING_RECEIVER=SixtyOneOneHundredTwelfthsLostCoreFourthRootFullCayleyRowAsymmetricShortLiftIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T76_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cx
```
