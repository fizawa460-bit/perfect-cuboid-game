# Stage14-4cw — full Cayley row + lost-core fourth-root column reduction

## Status

`COMPLETE_FULL_CAYLEY_ROW_LOST_CORE_FOURTH_ROOT_AND_61_112_PROMOTION`

Stage14-4cw consumes merged `X12`, `X11`, `s7-37`, `s7-35`, `4cv`, `4cu`, and `4cr` on current main.

Entering strongest whole-family theorem:

```text
V(B) << B^(71/128+o(1))
```

from merged X12.  Stage14-4cw combines two exact facts which were previously used separately:

1. X12: the fourth root of the lost joint core divides the endpoint-linear column cofactor product;
2. 4cv/4cr: after the column step reconstructs `M`, the Cayley row CRT can use the entire Cayley-good core rather than only the residual/Cayley intersection `J`.

The resulting whole-family theorem is

```text
V(B) << B^(61/112+o(1)).
```

No external H/tH theorem is used.

---

## 1. Imported exponents

Use the balanced strip

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

Choose the larger nonproportional cross-root cell and write

```text
H_star = B^(a+o(1)),
H_other= B^(b+o(1)),
a>=b>=0.
```

Merged s7-35 gives

```text
g_star/H_star^2 | B^o(1),
```

hence

```text
rho=2a.
```

Merged s7-34/X12 supply the fourth-power-root complete count

```text
E_H <= 3phi-1/8-3a-3b.                              (1.1)
```

The baseline complete counts remain

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4.                                  (1.2)
```

Merged s7-37 already gives

```text
E_prop <= 7/16.                                     (1.3)
```

---

## 2. Nested cores

Let `C_Cayley|C` be the full Cayley-good core.  Merged 4cu gives

```text
C/C_Cayley | B^o(1)*(H_star H_other)^2.
```

If

```text
C_Cayley=B^(c_y+o(1)),
```

then

```text
c_y >= chi-2a-2b.                                  (2.1)
```

Let

```text
J=B^(j+o(1))
```

be the residual/Cayley joint core used for the endpoint-linear orientation comparison.  The exact pre-relaxation lower bound is

```text
j >= chi-4a-2b.                                    (2.2)
```

Thus

```text
J | C_Cayley | C.
```

Define the lost joint core

```text
D=C/J.
```

Merged X12 proves, after removing endpoint-small support, that its fourth-root divisor

```text
R4(D0)=prod_p p^ceil(v_p(D0)/4)
```

satisfies

```text
R4(D0) | H_star H_other,
R4(D0) | h_- h_+,
R4(D0) >= B^((chi-j)/4-o(1)).                       (2.3)
```

No shortcut `J*H^2|L_-L_+` is used.

---

## 3. X12-sharpened column support

The endpoint-linear factors satisfy

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
J_L-*J_L+=J,

0<|L_-L_+|<=B^(1/4+o(1)).
```

Before X12 the raw cofactor product has exponent at most

```text
1/4-j.
```

By (2.3), a divisor of exponent at least `(chi-j)/4` is already forced into `h_-h_+`.  Therefore the effective moving column support is

```text
ell_col
 <= 1/4-j-(chi-j)/4
 = 1/4-chi/4-3j/4.                                 (3.1)
```

For a physical packet this quantity is nonnegative.  Using (2.2),

```text
ell_col <= 3a+(3/2)b-d,                             (3.2)
```

where

```text
d:=chi-1/4.
```

Once the column allocation and reduced cofactor are fixed, `L_-,L_+` reconstruct `(z1,z2)` and hence

```text
M=4rsXY epsilon_x epsilon_k
```

with divisor-many multiplicity.

---

## 4. Full Cayley row after `M` is fixed

Merged 4cr gives on the entire Cayley-good core

```text
C_Cayley=C_- C_+,
gcd(C_-,C_+)=1,

C_- | M-N,
C_+ | M+N,
N=abcd.                                             (4.1)
```

The row statement does not require residual primitivity.  Therefore after the `J`-column step fixes `M`, CRT may use all of `C_Cayley`:

```text
N == N0(M,C_-,C_+)  (mod C_Cayley).                (4.2)
```

Since `N<=B^(1/4+o(1))`, its moving lift support has exponent

```text
ell_row
 <= max(0,1/4-c_y)
 <= max(0,2a+2b-d).                                 (4.3)
```

Fixed `N` leaves only divisor-many signed quotient quadruples `(a,b,c,d)`.

The quantifier order is

```text
choose C once
-> primitive common-core pair
-> choose nested sign/core allocation
-> J-column + X12 fourth-root reconstruct M
-> full C_Cayley-row reconstruct N modulo C_Cayley
-> divisor-many signed reciprocal reconstruction.
```

The same common core is never multiplied back as a second spacing modulus.

```text
FULL_CAYLEY_ROW_AFTER_X12_COLUMN_DOUBLE_CHARGE=false.
```

---

## 5. New complete count

The outer common-core plus primitive-root-line cost is still

```text
B^(2phi+o(1)).
```

Hence the new full-row/fourth-root complete count is

```text
E_FR4
 <= 2phi
    +3a+(3/2)b-d
    +max(0,2a+2b-d).                                (5.1)
```

This is an alternative complete count of the same nonproportional physical block as (1.1).

### Case A: full Cayley row has no fixed-power lift

Assume

```text
2a+2b<=d.
```

Then

```text
E_FR4 <= 2phi+3a+(3/2)b-d.
```

Use

```text
min(E_H,E_FR4) <= (E_H+E_FR4)/2.
```

The `a` coefficient cancels and the `b` remainder is favorable:

```text
E
 <= (3/2)phi-theta+7/16-(3/4)b
 <= (3/2)phi-theta+7/16.                           (5.2)
```

With `phi<=1/4`,

```text
E <= 13/16-theta.                                  (5.3)
```

### Case B: a short full-row lift remains

Assume

```text
2a+2b>=d.
```

Then

```text
E_FR4 <= 2phi+5a+(7/2)b-2d.
```

Use

```text
min(E_H,E_FR4) <= (5E_H+3E_FR4)/8.
```

Again `a` cancels and `b` is favorable:

```text
E
 <= (9/8)phi-(3/2)theta+43/64-(9/16)b
 <= (9/8)phi-(3/2)theta+43/64.                     (5.4)
```

With `phi<=1/4`,

```text
E <= 61/64-(3/2)theta.                             (5.5)
```

---

## 6. Whole-strip minimax

For `theta<=1/4`,

```text
E_k<=1/2<61/112.
```

For

```text
1/4<=theta<=61/224,
```

we have

```text
E_s=2theta<=61/112.
```

For `theta>=61/224`:

- Case A gives

```text
E<=13/16-theta
 <=13/16-61/224
 =121/224
 <61/112;
```

- Case B gives

```text
E<=61/64-(3/2)theta
 <=61/64-(3/2)(61/224)
 =61/112.
```

Therefore

```text
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=61/112. (6.1)
```

Merged s7-37 gives `E_prop<=7/16`, hence

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112
IMPROVEMENT_OVER_MERGED_X12_71_128=9/896
IMPROVEMENT_OVER_MERGED_X11_19_34=25/1904
CURRENT_GAP_TO_SQRT=5/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.          (6.2)
```

---

## 7. Unique 61/112 equality profile

Equality in the proved whole-family envelope can occur only in Case B at

```text
theta=61/224,
phi=1/4.                                            (7.1)
```

Then

```text
chi=33/112,
d=5/112.
```

Equality in the `5:3` weighted min and the favorable `b` drop forces

```text
b=0,
a=3/112.                                           (7.2)
```

Thus

```text
rho=2a=3/56,
j=chi-4a=3/16,
c_y=chi-2a=27/112.                                 (7.3)
```

The lost-core and short-support ledger is

```text
C/J exponent:                 3/28,
raw column support:           1/16,
forced X12 fourth-root:       3/112,
effective column support:     1/28,
full Cayley row N-lift:       1/112.                (7.4)
```

Indeed

```text
2phi + 1/28 + 1/112
 =1/2+4/112+1/112
 =61/112.
```

The selected fourth-root exponent equals `a=3/112`: the X12 lost-core fourth root consumes the entire live cross-root scale at equality.

---

## 8. Remaining receiver

The new minimal receiver is

```text
SixtyOneOneHundredTwelfthsFullCayleyRowFourthRootColumnShortLiftIncidence.
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
R4(D0)=B^(3/112+o(1)),
effective column support=B^(1/28+o(1)),
full-row N-lift=B^(1/112+o(1)).
```

The next exact task is to compare the remaining reduced column cofactor and the very short full-row CRT lift after substituting the reconstructed `M,N` into the signed reciprocal identities.  No averaged theorem is yet forced.

---

## 9. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
X12_AUXILIARY_H_CROSS_PROMOTED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T76_CROSS_PROMOTED_TO_MAINLINE=false
```

X12 is used only through its merged exact lost-core fourth-root divisor theorem.  The fixed-U t/tH coefficient space remains separate.

A future H should be opened only if the reduced `1/28` column cofactor and `1/112` row lift survive exact signed-reciprocal substitution as a genuinely averaged incidence problem.

---

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
IMPROVEMENT_OVER_MERGED_X11_19_34=25/1904
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
