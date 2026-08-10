# Stage14-4cw — full Cayley-row CRT and the 11/20 bound

## Status

`COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION`

Stage14-4cw consumes merged `X11`, `s7-37`, `s7-36`, `s7-35`, `4cv`, and the Cayley-good-core allocation of `4cr/4cu`.

Current main enters with

```text
V(B) << B^(19/34+o(1)).
```

The proportional family is already strictly subcritical by merged s7-37:

```text
E_prop<=7/16.
```

The remaining `19/34` barrier is nonproportional.  Merged 4cv used the residual/Cayley intersection `J` for both the endpoint-linear column reconstruction and the Cayley-row CRT.  The new observation is that only the column needs the residual-good orientation.  After the column has reconstructed `M`, the row congruence may be read on the full already-fixed Cayley-good core `C_Cayley`.

This reduces the row `N=abcd` lift and gives

```text
boxed:
V(B) << B^(11/20+o(1)).
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

On a nonproportional packet choose the larger cross-root cell and write

```text
H_star=B^(a+o(1)),
H_other=B^(b+o(1)),
a>=b>=0.
```

Merged s7-35 gives

```text
g_star=H_star^2*B^o(1),
log_B g_star=2a.
```

Merged s7-34 gives the complete fourth-power-root count

```text
E_H<=3phi-1/8-3a-3b.                                (1.1)
```

---

## 2. Joint core versus full Cayley-good core

Merged 4cu gives a Cayley-good divisor

```text
C_Cayley|C,
C/C_Cayley | B^o(1)*(H_star*H_other)^2.
```

If `C_Cayley=B^(c_y+o(1))`, then

```text
boxed:c_y>=chi-2a-2b.                               (2.1)
```

The residual/Cayley intersection used for orientation comparison is

```text
J=B^(j+o(1)),
```

and the pre-relaxation lower bound imported through s7-36 is

```text
boxed:j>=chi-4a-2b.                                 (2.2)
```

Thus

```text
J | C_Cayley | C.
```

---

## 3. Column reconstruction on `J`

Keep

```text
L_-=z1*r2*s2-z2*r1*s1,
L_+=z1*r2*s2+z2*r1*s1.
```

On the nonproportional branch,

```text
0<|L_-L_+|<=B^(1/4+o(1)),
J|L_-L_+.
```

Primewise orientation gives

```text
J_L-|L_-,
J_L+|L_+,
J_L-*J_L+=J.
```

Write

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+.
```

The total column-cofactor support is

```text
ell_col<=max(0,1/4-j).                              (3.1)
```

Since the nonzero product is at most `B^(1/4+o(1))`, physical existence forces `j<=1/4+o(1)`.  Put

```text
d=chi-1/4.
```

Using (2.2),

```text
boxed:ell_col<=4a+2b-d.                             (3.2)
```

Once `J_L±,h_±` are fixed,

```text
z1*r2*s2=(L_++L_-)/2,
z2*r1*s1=(L_+-L_-)/2,
```

so `(z1,z2)` and then

```text
M=4rsXY*epsilon_x*epsilon_k
```

are recovered with `B^o(1)` multiplicity.

---

## 4. Full Cayley row after `M` is known

Merged 4cr splits the entire Cayley-good core as

```text
C_Cayley=C_-*C_+,
gcd(C_-,C_+)=1,
C_-|M-N,
C_+|M+N,
N=abcd.
```

These row congruences are valid on `C_Cayley`, not merely on `J`.

After the column reconstruction has fixed `M`, CRT gives one class

```text
boxed:N=N_0(M) mod C_Cayley.                        (4.1)
```

Since `N<=B^(1/4+o(1))`, the row-lift exponent is

```text
ell_row<=max(0,1/4-c_y)
        <=max(0,2a+2b-d).                           (4.2)
```

Fixed `N` leaves only divisor-many signed quotient quadruples, so `u_res,v_res` are not charged separately.

This is a legal charged-once order:

```text
choose C once
-> primitive common-core pair
-> divisor-many nested core/sign allocation
-> J-column fixes M
-> full C_Cayley-row fixes N modulo C_Cayley
-> divisor-many reciprocal reconstruction.
```

Hence

```text
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false.          (4.3)
```

---

## 5. Complete full-row reconstruction count

The first two costs are

```text
C support:                     B^chi,
primitive (U,V) fiber:         B^(2phi-chi).
```

Therefore

```text
boxed:
E_FR<=2phi+(4a+2b-d)+max(0,2a+2b-d).               (5.1)
```

Compare this complete count with (1.1).

### Case A: `2a+2b<=d`

Then the row lift is `B^o(1)` and

```text
E_FR<=2phi+4a+2b-d.
```

Using

```text
min(E_H,E_FR)<=(4E_H+3E_FR)/7
```

cancels `a` and leaves a favorable `-6b/7`:

```text
E<= (12phi-6theta+5/2)/7-(6/7)b
 <= (12phi-6theta+5/2)/7.                           (5.2)
```

Thus, with `phi<=1/4`,

```text
boxed:E<=11/14-(6/7)theta.                          (5.3)
```

### Case B: `2a+2b>=d`

Now

```text
E_FR<=2phi+6a+4b-2d.
```

Using

```text
min(E_H,E_FR)<=(2E_H+E_FR)/3
```

cancels `a` and leaves `-2b/3`:

```text
E<=(4phi-4theta+7/4)/3-(2/3)b
 <=(4phi-4theta+7/4)/3.                              (5.4)
```

Hence

```text
boxed:E<=11/12-(4/3)theta.                          (5.5)
```

---

## 6. Whole-strip minimax

Retain merged complete counts

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.
```

If `theta<=1/4`, then `E_k<=1/2`.

If `1/4<=theta<=11/40`, then `E_s=2theta<=11/20`.

If `theta>=11/40`, Case A gives

```text
11/14-(6/7)theta<=11/20,
```

and Case B gives

```text
11/12-(4/3)theta<=11/20.
```

Therefore

```text
boxed:NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20.         (6.1)
```

Merged s7-37 gives

```text
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16<11/20.
```

Thus

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20
IMPROVEMENT_OVER_MERGED_19_34=3/340
CURRENT_GAP_TO_SQRT=1/20
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.           (6.2)
```

---

## 7. Unique saturation profile

Equality in the proved envelope requires

```text
theta=11/40,
phi=1/4.
```

Then

```text
chi=3/10,
d=1/20.
```

Equality in the complete-count comparison forces

```text
a=1/40,
b=0,
rho=2a=1/20,
j=1/5,
c_y=1/4.
```

Consequently

```text
column short support exponent=1/20,
full Cayley row N-lift exponent=0.
```

The equality ledger is

```text
C + primitive pair:          1/2,
linear-column short support: 1/20,
full-row N lift:             0,
---------------------------------
total:                       11/20.
```

---

## 8. Remaining receiver

The new minimal receiver is

```text
ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence.
```

Its saturation data are

```text
theta=11/40,
phi=1/4,
C=B^(3/10+o(1)),
H_star=B^(1/40+o(1)),
H_other=B^o(1),
g_star=B^(1/20+o(1)),
J=B^(1/5+o(1)),
C_Cayley=B^(1/4+o(1)),
|h_-h_+|<=B^(1/20+o(1)),
#N_lifts=B^o(1).
```

The row lift is no longer a polynomial degree of freedom.  The next exact task is to substitute the uniquely reconstructed `N=abcd` into the reciprocal signed-quotient equations and determine whether the single remaining `B^(1/20)` column cofactor is divisor-locked.

---

## 9. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T75_CROSS_PROMOTED_TO_MAINLINE=false
```

The remaining obstruction is still one explicit short integer cofactor attached to exact CRT/factorization data.  External averaging is premature.

---

## Stage boundary

```text
STAGE14_4CW=COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION
MERGED_X11_IMPORTED=true
MERGED_S7_37_IMPORTED=true
MERGED_S7_36_IMPORTED=true
MERGED_S7_35_IMPORTED=true
MERGED_4CV_IMPORTED=true
FULL_CAYLEY_GOOD_CORE_ROW_REUSED_AFTER_COLUMN_M_RECONSTRUCTION=true
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false
CAYLEY_GOOD_CORE_LOWER_EXPONENT=chi-2a-2b
JOINT_COLUMN_CORE_LOWER_EXPONENT=chi-4a-2b
FULL_CAYLEY_ROW_N_LIFT_EXPONENT=max(0,1/4-chi+2a+2b)
NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=4:3
NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=2:1
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20
IMPROVEMENT_OVER_MERGED_19_34=3/340
CURRENT_GAP_TO_SQRT=1/20
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
ELEVEN_TWENTIETHS_SATURATION_THETA=11/40
ELEVEN_TWENTIETHS_SATURATION_PHI=1/4
ELEVEN_TWENTIETHS_COMMON_CORE_EXPONENT=3/10
ELEVEN_TWENTIETHS_SELECTED_CROSS_ROOT_EXPONENT=1/40
ELEVEN_TWENTIETHS_OTHER_CROSS_ROOT_EXPONENT=0
ELEVEN_TWENTIETHS_SELECTED_XI_GCD_EXPONENT=1/20
ELEVEN_TWENTIETHS_JOINT_COLUMN_CORE_EXPONENT=1/5
ELEVEN_TWENTIETHS_FULL_CAYLEY_CORE_EXPONENT=1/4
ELEVEN_TWENTIETHS_LINEAR_SHORT_SUPPORT_EXPONENT=1/20
ELEVEN_TWENTIETHS_FULL_ROW_N_LIFT_EXPONENT=0
REMAINING_RECEIVER=ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T75_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cx
```
