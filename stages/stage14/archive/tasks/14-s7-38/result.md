# Stage14-s7-38 — lost-core column divisor + full Cayley-row CRT and the 61/112 bound

## Status

`COMPLETE_X12_COLUMN_DIVISOR_FULL_CAYLEY_ROW_CORE_RECONSTRUCTION_AND_61_112_PROMOTION`

Stage14-s7-38 consumes latest merged main through `X12`, together with merged `s7-37`, `X11`, `s7-36`, `s7-35`, `4cu`, and `4cv`.

The entering canonical theorem is now

```text
V(B) << B^(71/128+o(1)).
```

Merged X12 improves the column cofactor by forcing a fourth-root divisor of the lost core `C/J` into `h_-h_+`, but still uses the joint core `J` for the Cayley-row CRT lift. The new s7-38 observation is orthogonal: the row CRT is valid on the larger full Cayley-good core `C_Cayley`, not merely on `J`.

Combining both exact refinements gives

```text
boxed:
V(B) << B^(61/112+o(1)).
```

No external incidence theorem is used.

---

## 1. Imported strip and current exact data

Use

```text
3/16 <= theta <= 5/16,
1/8 <= phi <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

The proportional branch is already

```text
E_prop<=7/16<1/2
```

by merged s7-37, hence only the nonproportional branch matters here.

Retain the complete counts

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4,
E_xi,raw<=3phi-1/8,
```

and the older merged s7-36 nonproportional bound

```text
E_old<=(18phi-12theta+5)/11.                       (1.1)
```

---

## 2. Cross-root exponents and selected residual gcd

Write

```text
H_star=B^(eta_star+o(1)),
H_other=B^(eta_other+o(1)),
eta_star>=eta_other>=0,
s_H=eta_star+eta_other.
```

Merged s7-35 proves

```text
g_star/H_star^2 | oddpart(omega1*omega2),
omega1*omega2=B^o(1),
```

so

```text
rho=2eta_star.                                     (2.1)
```

Merged s7-34 gives the fourth-power-root complete count

```text
boxed:
E_H<=3phi-1/8-3s_H.                                (2.2)
```

---

## 3. Joint core and full Cayley-good core

Merged 4cu defines

```text
C_Cayley|C,
C/C_Cayley | B^o(1)*H_star^2 H_other^2.
```

Thus if

```text
C_Cayley=B^(c_C+o(1)),
```

then

```text
boxed:
c_C>=chi-2eta_star-2eta_other
    =chi-2s_H.                                     (3.1)
```

The selected residual good core is

```text
C_res=C/gcd(C,g_star^2),
```

and

```text
J=gcd(C_Cayley,C_res)=B^(j+o(1)).
```

Merged s7-36/X12 retain the exact lower bound

```text
boxed:
j>=chi-4eta_star-2eta_other.                       (3.2)
```

For a uniform upper envelope we may weaken this to

```text
boxed:
j>=chi-4s_H.                                       (3.3)
```

---

## 4. Import X12: lost-core fourth root saves the column

Define the lost core

```text
D=C/J.
```

Merged X12 proves, after removing endpoint-small decoration, that

```text
R_4(D_0)|h_-h_+,
R_4(D_0)>=B^((chi-j)/4-o(1)),
```

where

```text
L_-=J_L- h_-,
L_+=J_L+ h_+,
J_L-J_L+=J.
```

Therefore the effective column cofactor support is

```text
boxed:
E_col
 <=max(0,1/4-j-(chi-j)/4).                         (4.1)
```

Equivalently,

```text
E_col
 <=max(0,1/4-chi/4-3j/4).                          (4.2)
```

Using `(3.2)`,

```text
E_col
 <=max(0,1/4-chi+3eta_star+(3/2)eta_other).         (4.3)
```

Since `eta_star<=s_H`,

```text
boxed:
E_col<=max(0,3s_H-d),                              (4.4)
```

where

```text
d=chi-1/4=2theta+2phi-1.                          (4.5)
```

---

## 5. New s7-38 lever: row CRT uses `C_Cayley`, not `J`

The Cayley row congruences are valid before intersecting with the residual good core. Write the full Cayley sign allocation

```text
C_Cayley=C_C- C_C+,
gcd(C_C-,C_C+)=1,

C_C-|M-N,
C_C+|M+N.
```

The column reconstruction fixes `(z1,z2)` and hence

```text
M=4rsXY epsilon_x epsilon_k
```

with divisor-many ambiguity.

Once `M` is fixed, CRT on the full Cayley core fixes

```text
N == N_C (mod C_Cayley).
```

Since

```text
N=a*b*c*d<=B^(1/4+o(1)),
```

the row-lift support is

```text
boxed:
E_row<=max(0,1/4-c_C).                              (5.1)
```

Using `(3.1)`,

```text
boxed:
E_row<=max(0,2s_H-d).                               (5.2)
```

This does not double-charge the common core. `J` and `C_Cayley` are already chosen divisors of the same once-charged `C`; the row merely uses arithmetic which 4cv/X12 had left unused.

```text
FULL_CAYLEY_CORE_USED_FOR_ROW_CRT=true
JOINT_CORE_ONLY_USED_FOR_COLUMN=true
X12_COLUMN_SAVING_RETAINED=true
ROW_AND_COLUMN_REFINEMENTS_COMPATIBLE=true.
```

---

## 6. Combined complete count

The common-core and primitive-pair cost is still exactly

```text
C:               chi,
primitive (U,V): 2phi-chi,
```

hence `2phi` total.

Combining `(4.4)` and `(5.2)`,

```text
boxed:
E_CRC
 <=2phi
   +max(0,3s_H-d)
   +max(0,2s_H-d).                                 (6.1)
```

If `d>0`, nonproportionality and `J|L_-L_+` imply `j<=1/4`. Together with `(3.3)`,

```text
chi-4s_H<=1/4,
```

so

```text
boxed:
s_H>=d/4.                                         (6.2)
```

This is the only lower bound on `s_H` needed below.

---

## 7. Uniform `61/112` bound

### 7.1. `theta<=61/224`

If `theta<=1/4`,

```text
E<=E_k<=1/2.
```

If

```text
1/4<=theta<=61/224,
```

then

```text
E<=E_s=2theta<=61/112.                             (7.1)
```

Thus assume

```text
theta>=61/224.                                     (7.2)
```

### 7.2. Low-core region `d<=0`

Then `phi<=1/2-theta`. Instead of the coarse raw xi count, retain the merged s7-36 estimate `(1.1)`:

```text
E_old
 <=(18(1/2-theta)-12theta+5)/11
 =(14-30theta)/11.
```

At `(7.2)`,

```text
(14-30theta)/11<61/112.                            (7.3)
```

Thus low core is strictly subcritical.

### 7.3. High core and `3s_H<=d`

Both positive parts in `(6.1)` vanish, so

```text
E_CRC<=2phi<=1/2<61/112.                           (7.4)
```

### 7.4. High core and `d<=3s_H`, `2s_H<=d`

Here only the column term is active:

```text
E_CRC<=2phi+3s_H-d.
```

Together with `(2.2)`,

```text
min(E_H,E_CRC)
 <=(E_H+E_CRC)/2
 <=(3phi-2theta+7/8)/2.                            (7.5)
```

Using `phi<=1/4`,

```text
E<=13/16-theta.
```

At `(7.2)`,

```text
13/16-theta<61/112.                                (7.6)
```

So this middle regime is also strict.

### 7.5. High core and `2s_H>=d`

Both short terms may be active:

```text
E_CRC<=2phi+5s_H-2d.
```

Combine with `(2.2)` using weights `5:3`:

```text
min(E_H,E_CRC)
 <=(5E_H+3E_CRC)/8.
```

The `s_H` terms cancel:

```text
5*(-3)+3*5=0.
```

Hence

```text
E
 <=(9/8)phi-(3/2)theta+43/64.                      (7.7)
```

Since `phi<=1/4`,

```text
E<=61/64-(3/2)theta.
```

At `(7.2)`,

```text
61/64-(3/2)theta<=61/112.                          (7.8)
```

Sections 7.1--7.5 cover the whole strip. The proportional branch is already `<=7/16`. Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112.
```

Relative to latest merged X12,

```text
71/128-61/112=9/896.
```

The gap to square-root scale is

```text
61/112-1/2=5/112.
```

Thus

```text
IMPROVEMENT_OVER_PREVIOUS_71_128=9/896
CURRENT_GAP_TO_SQRT=5/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.
```

---

## 8. Unique equality profile

Equality can occur only in Section 7.5, and requires equality in the `s`-count and in `(7.7)--(7.8)`:

```text
boxed:
theta=61/224,
phi=1/4.                                           (8.1)
```

Then

```text
chi=33/112,
d=chi-1/4=5/112.                                  (8.2)
```

Equality of the two complete counts in Section 7.5 gives

```text
s_H=3/112.                                         (8.3)
```

Equality in the selected-core relaxations forces

```text
eta_star=3/112,
eta_other=0.                                       (8.4)
```

Hence

```text
rho=2eta_star=3/56.                                (8.5)
```

The joint and Cayley core exponents are

```text
j=chi-4eta_star=3/16,
c_C=chi-2s_H=27/112.                               (8.6)
```

The lost core and short supports are

```text
chi-j=3/28,
raw column support       =1/4-j      =1/16,
forced X12 fourth root   =(chi-j)/4  =3/112,
effective column support =1/28,
row CRT lift support     =1/4-c_C    =1/112.       (8.7)
```

The Cayley-only annulus has exponent

```text
c_C-j=3/56=rho.                                    (8.8)
```

Thus the equality ledger is

```text
C + primitive pair:       1/2,
effective column quotient:1/28,
full-Cayley row lift:      1/112,
--------------------------------
total:                     61/112.
```

---

## 9. New minimal receiver

```text
SixtyOneOneHundredTwelfthsSingleCrossRootCayleyAnnulusEffectiveColumnTinyRowLiftIncidence
```

with equality data

```text
theta=61/224,
phi=1/4,
chi=33/112,
eta_star=3/112,
eta_other=0,
rho=3/56,
j=3/16,
c_C=27/112,
C/J=B^(3/28+o(1)),
R_4(D_0)=B^(3/112+o(1)),
C_Cayley/J=B^(3/56+o(1)),
effective column quotient<=B^(1/28+o(1)),
row CRT lift<=B^(1/112+o(1)).
```

The old symmetric twin-short receiver is gone. The remaining fixed-power obstruction is highly asymmetric.

---

## 10. H / tH decision

No auxiliary H/tH theorem is needed at s7-38.

At equality the Cayley-only annulus and selected residual gcd have the same exponent

```text
c_C-j=rho=3/56,
```

while the effective column quotient and row lift are much shorter. This exposes a new exact prime-support question before any averaged theorem is justified.

`Stage14-s7-39` should classify

```text
A_C=C_Cayley/J
```

primewise inside the residual bad quotient, compare it to `g_star`, and determine how its Cayley sign constrains the effective column quotient and the tiny full-Cayley row lift.

```text
S7_38_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.
```

`t75/tH20` are not cross-promoted.

---

## Stage boundary

```text
STAGE14_S7_38=COMPLETE_X12_COLUMN_DIVISOR_FULL_CAYLEY_ROW_CORE_RECONSTRUCTION_AND_61_112_PROMOTION
MERGED_X12_71_128_IMPORTED=true
MERGED_S7_37_IMPORTED=true
MERGED_X11_IMPORTED=true
MERGED_S7_36_NONPROPORTIONAL_BOUND_RETAINED=true
X12_LOST_CORE_FOURTH_ROOT_COLUMN_SAVING_RETAINED=true
FULL_CAYLEY_CORE_USED_FOR_ROW_CRT=true
JOINT_CORE_ONLY_USED_FOR_COLUMN=true
ROW_AND_COLUMN_REFINEMENTS_COMPATIBLE=true
COMBINED_ROW_COLUMN_COUNT_PROVED=true
COMBINED_ROW_COLUMN_COUNT=2phi+max(0,3s_H-d)+max(0,2s_H-d)
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=61/112
IMPROVEMENT_OVER_PREVIOUS_71_128=9/896
CURRENT_GAP_TO_SQRT=5/112
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SIXTYONE_112_SATURATION_THETA=61/224
SIXTYONE_112_SATURATION_PHI=1/4
SIXTYONE_112_COMMON_CORE_EXPONENT=33/112
SIXTYONE_112_SINGLE_CROSS_ROOT_EXPONENT=3/112
SIXTYONE_112_RESIDUAL_GCD_EXPONENT=3/56
SIXTYONE_112_JOINT_CORE_EXPONENT=3/16
SIXTYONE_112_CAYLEY_CORE_EXPONENT=27/112
SIXTYONE_112_LOST_CORE_EXPONENT=3/28
SIXTYONE_112_FORCED_FOURTH_ROOT_EXPONENT=3/112
SIXTYONE_112_RAW_COLUMN_SUPPORT_EXPONENT=1/16
SIXTYONE_112_EFFECTIVE_COLUMN_SUPPORT_EXPONENT=1/28
SIXTYONE_112_ROW_CRT_LIFT_EXPONENT=1/112
SIXTYONE_112_CAYLEY_ONLY_ANNULUS_EXPONENT=3/56
REMAINING_RECEIVER=SixtyOneOneHundredTwelfthsSingleCrossRootCayleyAnnulusEffectiveColumnTinyRowLiftIncidence
S7_38_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
T75_CROSS_PROMOTED_TO_S7_38=false
TH20_CROSS_PROMOTED_TO_S7_38=false
NEXT=Stage14-s7-39
```
