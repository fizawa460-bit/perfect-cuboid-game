# Stage14-4cw — full Cayley row plus X12 lost-core fourth root

## Status

`COMPLETE_FULL_CAYLEY_ROW_LOST_CORE_FOURTH_ROOT_AND_61_112_PROMOTION`

Stage14-4cw consumes merged `X12`, `X11`, `s7-37`, `s7-35`, `4cv`, `4cu`, and `4cr` on current main. The entering theorem is

```text
V(B) << B^(71/128+o(1)).
```

The new step combines X12's lost-core fourth-root divisor on the column cofactor with a stronger quantifier order for the Cayley row: the column must use the residual/Cayley joint core `J`, but after it reconstructs `M`, the row CRT can use the entire Cayley-good core `C_Cayley`.

This gives

```text
V(B) << B^(61/112+o(1)).
```

No external H/tH theorem is used.

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

On a nonproportional packet choose

```text
H_star=B^(a+o(1)),
H_other=B^(b+o(1)),
a>=b>=0.
```

Merged s7-35 gives `g_star=H_star^2 B^o(1)`, so `rho=2a`. Merged X12/s7-34 give the complete count

```text
E_H<=3phi-1/8-3a-3b.                               (1.1)
```

Retain

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.                                    (1.2)
```

Merged s7-37 gives the proportional bound

```text
E_prop<=7/16.                                       (1.3)
```

## 2. Nested good cores

Let

```text
C_Cayley=B^(c_y+o(1)),
J=B^(j+o(1)),
J | C_Cayley | C.
```

Merged 4cu/s7-35 give

```text
c_y>=chi-2a-2b,                                    (2.1)
j>=chi-4a-2b.                                      (2.2)
```

Put `D=C/J`. Merged X12 defines the fourth-root divisor `R4(D0)` after endpoint-small support is removed and proves

```text
R4(D0)|H_star H_other,
R4(D0)|h_-h_+,
R4(D0)>=B^((chi-j)/4-o(1)).                        (2.3)
```

No coprime shortcut such as `J*H^2|L_-L_+` is used.

## 3. Fourth-root sharpened column

The endpoint-linear column is

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
J_L-*J_L+=J,
0<|L_-L_+|<=B^(1/4+o(1)).
```

The raw cofactor support is `1/4-j`. By (2.3), a fixed divisor of exponent at least `(chi-j)/4` is already present. Thus the effective moving support is

```text
ell_col
 <=1/4-j-(chi-j)/4
 =1/4-chi/4-3j/4.                                  (3.1)
```

For a physical packet this is nonnegative. With

```text
d:=chi-1/4,
```

(2.2) yields

```text
ell_col<=3a+(3/2)b-d.                              (3.2)
```

After fixing the reduced column cofactor, `(L_-,L_+)` reconstruct `(z1,z2)` and hence

```text
M=4rsXY epsilon_x epsilon_k
```

with divisor-many multiplicity.

## 4. Full Cayley row

Merged 4cr gives on all of `C_Cayley`

```text
C_Cayley=C_-C_+,
gcd(C_-,C_+)=1,
C_-|M-N,
C_+|M+N,
N=abcd.                                             (4.1)
```

These congruences do not require residual primitivity. Therefore, after the `J`-column step has fixed `M`, CRT may use the full row:

```text
N == N0(M,C_-,C_+) (mod C_Cayley).                 (4.2)
```

Since `N<=B^(1/4+o(1))`, the row-lift support satisfies

```text
ell_row
 <=max(0,1/4-c_y)
 <=max(0,2a+2b-d).                                  (4.3)
```

Fixed `N` leaves only divisor-many signed quotient quadruples. The legal order is

```text
choose C once
-> primitive common-core pair
-> nested sign/core allocation
-> J-column + X12 fourth-root reconstruct M
-> full C_Cayley row reconstruct N
-> divisor-many reciprocal lift.
```

Thus

```text
FULL_CAYLEY_ROW_AFTER_X12_COLUMN_DOUBLE_CHARGE=false.
```

## 5. Complete count

The common-core plus primitive-root-line cost is `B^(2phi+o(1))`. Hence

```text
E_FR4
 <=2phi
   +3a+(3/2)b-d
   +max(0,2a+2b-d).                                (5.1)
```

This is an alternative complete count of the same block as (1.1).

### Case A: `2a+2b<=d`

Then

```text
E_FR4<=2phi+3a+(3/2)b-d.
```

Using `min(A,B)<=(A+B)/2`,

```text
E<= (3/2)phi-theta+7/16-(3/4)b
 <= (3/2)phi-theta+7/16
 <=13/16-theta.                                    (5.2)
```

### Case B: `2a+2b>=d`

Then

```text
E_FR4<=2phi+5a+(7/2)b-2d.
```

Using

```text
min(E_H,E_FR4)<=(5E_H+3E_FR4)/8,
```

we obtain

```text
E<= (9/8)phi-(3/2)theta+43/64-(9/16)b
 <=61/64-(3/2)theta.                               (5.3)
```

## 6. Whole-strip minimax

For `theta<=1/4`, `E_k<=1/2`.

For

```text
1/4<=theta<=61/224,
```

`E_s=2theta<=61/112`.

For `theta>=61/224`, Case A gives

```text
E<=13/16-theta<=121/224<61/112,
```

while Case B gives

```text
E<=61/64-(3/2)theta<=61/112.
```

Therefore

```text
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=61/112.
```

Together with the merged proportional `7/16` bound,

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112
IMPROVEMENT_OVER_MERGED_X12_71_128=9/896
IMPROVEMENT_OVER_MERGED_X11_19_34=27/1904
CURRENT_GAP_TO_SQRT=5/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

## 7. Unique equality profile

Equality is possible only in Case B at

```text
theta=61/224,
phi=1/4,
chi=33/112,
d=5/112.
```

Equality in the `5:3` weighted min forces

```text
a=3/112,
b=0.
```

Hence

```text
rho=3/56,
j=3/16,
c_y=27/112.
```

The remaining ledger is

```text
lost core C/J:             3/28,
raw column support:        1/16,
forced X12 fourth root:    3/112,
effective column support:  1/28,
full Cayley row N-lift:    1/112.
```

Thus

```text
1/2+1/28+1/112=61/112.
```

At equality the forced fourth-root exponent `3/112` equals the full live cross-root exponent `a`; X12 consumes the entire selected cross-root scale.

## 8. Remaining receiver

```text
SixtyOneOneHundredTwelfthsFullCayleyRowFourthRootColumnShortLiftIncidence
```

with equality data

```text
theta=61/224,
phi=1/4,
C=B^(33/112+o(1)),
H_star=B^(3/112+o(1)),
H_other=B^o(1),
g_star=B^(3/56+o(1)),
J=B^(3/16+o(1)),
C_Cayley=B^(27/112+o(1)),
R4(D0)=B^(3/112+o(1)),
effective column support=B^(1/28+o(1)),
full row lift=B^(1/112+o(1)).
```

The next exact task is to substitute the reconstructed `M,N` into the signed reciprocal identities and compare the reduced column cofactor directly with the very short full-row lift.

## 9. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T76_CROSS_PROMOTED_TO_MAINLINE=false
```

X12 is used only through its merged exact lost-core fourth-root theorem. The fixed-U t/tH coefficient space remains separate. An auxiliary H should be considered only if the remaining exact `1/28`/`1/112` coupling survives Stage14-4cx.

## Stage boundary

```text
STAGE14_4CW=COMPLETE_FULL_CAYLEY_ROW_LOST_CORE_FOURTH_ROOT_AND_61_112_PROMOTION
MERGED_X12_IMPORTED=true
MERGED_S7_37_IMPORTED=true
LOST_CORE_FOURTH_ROOT_COLUMN_SAVING_IMPORTED=true
FULL_CAYLEY_ROW_AFTER_X12_COLUMN_PROVED=true
FULL_CAYLEY_ROW_AFTER_X12_COLUMN_DOUBLE_CHARGE=false
EFFECTIVE_COLUMN_SUPPORT_EXPONENT=3a+(3/2)b-d
FULL_ROW_LIFT_EXPONENT=max(0,2a+2b-d)
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
SIXTYONE_112_JOINT_COLUMN_CORE_EXPONENT=3/16
SIXTYONE_112_CAYLEY_GOOD_CORE_EXPONENT=27/112
SIXTYONE_112_LOST_CORE_EXPONENT=3/28
SIXTYONE_112_FORCED_FOURTH_ROOT_EXPONENT=3/112
SIXTYONE_112_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=1/28
SIXTYONE_112_FULL_ROW_LIFT_EXPONENT=1/112
REMAINING_RECEIVER=SixtyOneOneHundredTwelfthsFullCayleyRowFourthRootColumnShortLiftIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T76_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cx
```
