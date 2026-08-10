# Stage14-4cw — full Cayley-row CRT after joint-core column reconstruction and the 11/20 bound

## Status

`COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION`

Stage14-4cw consumes merged `4cv`, `s7-35`, `s7-36`, `X11`, and `s7-37` on current main. The entering whole-family theorem is

```text
V(B) << B^(19/34+o(1)).
```

Merged s7-37 has already made the proportional family subcritical:

```text
E_prop <= 7/16.
```

The remaining global receiver is the nonproportional twin-short row/column packet. The new point is a quantifier-order correction: the endpoint-linear column reconstruction genuinely needs the residual/Cayley intersection `J`, but after it fixes `M`, the Cayley row CRT may use the entire already-fixed Cayley-good core `C_Cayley`, not only `J`.

This removes the second fixed-power short support and yields

```text
V(B) << B^(11/20+o(1)).
```

No external H/tH theorem is used.

---

## 1. Imported packet and complete counts

Use

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

On a nonproportional packet choose the larger cross-root cell and write

```text
H_star = B^(a+o(1)),
H_other= B^(b+o(1)),
a>=b>=0.
```

Merged s7-35 gives

```text
g_star/H_star^2 | oddpart(omega_1*omega_2)=B^o(1),
```

hence at exponent scale

```text
rho=log_B(g_star)=2a.
```

Merged s7-34/s7-35 give the fourth-power-root complete count

```text
E_H <= 3phi-1/8-3a-3b.                              (1.1)
```

The always-available complete counts remain

```text
E_s <= max(2theta,1-2theta),
E_k <= 3theta-1/4.                                  (1.2)
```

---

## 2. Cayley-good core versus joint residual/Cayley core

Let `C_Cayley|C` denote the Cayley-good core. Merged 4cu gives

```text
C/C_Cayley | B^o(1)*(H_star*H_other)^2.
```

If

```text
C_Cayley=B^(c_y+o(1)),
```

then

```text
c_y >= chi-2a-2b.                                  (2.1)
```

The selected residual host is primitive only after its coordinate-gcd square is removed. Intersecting its residual-good core with `C_Cayley` gives the joint core

```text
J=B^(j+o(1)).
```

The exact pre-relaxation lower bound retained in merged 4cu/s7-36 is

```text
j >= chi-4a-2b.                                    (2.2)
```

Thus

```text
J | C_Cayley | C.
```

The difference between (2.1) and (2.2) is the selected residual coordinate-gcd square. It is not a second independently charged modulus.

---

## 3. Column reconstruction still uses `J`

Set

```text
L_- = z1*r2*s2-z2*r1*s1,
L_+ = z1*r2*s2+z2*r1*s1.
```

On the nonproportional branch

```text
L_-L_+ != 0,
|L_-L_+| <= B^(1/4+o(1)).                          (3.1)
```

The residual/Cayley orientation comparison is available on `J`. Write the column allocation

```text
J_L- | L_-,
J_L+ | L_+,
J_L-*J_L+=J,

L_-=J_L-*h_-,
L_+=J_L+*h_+.
```

Since `J|L_-L_+`, every physical nonproportional packet satisfies `j<=1/4+o(1)`. Put

```text
d:=chi-1/4.
```

Then (2.2) and `j<=1/4` force

```text
4a+2b-d >= -o(1).
```

The total column-cofactor support therefore has exponent

```text
ell_col <= 1/4-j
        <= 4a+2b-d.                                (3.2)
```

Once the column allocation and `(h_-,h_+)` are fixed,

```text
z1*r2*s2=(L_++L_-)/2,
z2*r1*s1=(L_+-L_-)/2.
```

Because `r_i,s_i=B^o(1)`, this reconstructs `(z1,z2)` with divisor-many multiplicity, hence fixes

```text
M=4rsXY*epsilon_x*epsilon_k
```

up to the already-fixed finite 2-primary decoration.

---

## 4. After `M` is fixed, use the full Cayley row

Merged 4cr allocates the entire Cayley-good core into coprime row factors

```text
C_Cayley=C_-*C_+,
gcd(C_-,C_+)=1,

C_- | M-N,
C_+ | M+N,
N=abcd.                                             (4.1)
```

These row congruences are Cayley statements; they do not require the selected residual host to be primitive. Therefore after the `J`-column step fixes `M`, CRT may be run modulo the full `C_Cayley`:

```text
N == N_0(M,C_-,C_+)  (mod C_Cayley).               (4.2)
```

Since

```text
N<=B^(1/4+o(1)),
```

the number of row lifts has exponent

```text
ell_row <= max(0,1/4-c_y)
        <= max(0,2a+2b-d).                          (4.3)
```

Once `N` is fixed, `(a,b,c,d)` is divisor-many, so `u_res` and `v_res` are not charged separately.

The legal charged-once order is

```text
choose C once
-> primitive common-core pair
-> choose divisor-many nested sign/core allocations
-> J-column reconstructs z1,z2 and M
-> full C_Cayley-row fixes N modulo C_Cayley
-> divisor-many quotient/reciprocal reconstruction.
```

No factor `J*C_Cayley` is introduced.

```text
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false.
```

---

## 5. Full-row reconstruction count

The already-charged outer support is

```text
C:                     B^chi,
primitive (U,V) fiber: B^(2phi-chi).
```

Adding only the two sequential short supports gives

```text
E_FR
 <= 2phi
    +(4a+2b-d)
    +max(0,2a+2b-d).                               (5.1)
```

This is a complete count of the same nonproportional block as (1.1).

### Case A: full row reaches the N-range

Assume

```text
2a+2b<=d.
```

Then

```text
E_FR <= 2phi+4a+2b-d.
```

Taking the weighted average of the two complete counts,

```text
min(E_H,E_FR) <= (4E_H+3E_FR)/7,
```

cancels `a` and leaves a favorable `b` term:

```text
E <= (12phi-6theta+5/2)/7 -(6/7)b
  <= (12phi-6theta+5/2)/7.                         (5.2)
```

Using `phi<=1/4`,

```text
E <= 11/14-(6/7)theta.                             (5.3)
```

### Case B: a row lift remains

Assume

```text
2a+2b>=d.
```

Then

```text
E_FR <= 2phi+6a+4b-2d.
```

Now

```text
min(E_H,E_FR) <= (2E_H+E_FR)/3
```

gives

```text
E <= (4phi-4theta+7/4)/3 -(2/3)b
  <= (4phi-4theta+7/4)/3.                          (5.4)
```

Using `phi<=1/4`,

```text
E <= 11/12-(4/3)theta.                             (5.5)
```

---

## 6. Whole-strip minimax

If `theta<=1/4`, then

```text
E_k<=1/2<11/20.
```

If

```text
1/4<=theta<=11/40,
```

then `E_s=2theta<=11/20`.

Finally suppose `theta>=11/40`. In Case A, (5.3) gives

```text
E<=11/14-(6/7)(11/40)=11/20.
```

In Case B, (5.5) gives

```text
E<=11/12-(4/3)(11/40)=11/20.
```

Both decrease strictly with theta after `11/40`. Therefore

```text
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20.  (6.1)
```

Merged s7-37 gives

```text
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16.      (6.2)
```

Hence

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20
IMPROVEMENT_OVER_MERGED_X11_19_34=3/340
CURRENT_GAP_TO_SQRT=1/20
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.          (6.3)
```

---

## 7. Unique equality profile

Equality at `11/20` requires

```text
theta=11/40,
phi=1/4.
```

Then

```text
chi=3/10,
d=1/20.
```

Equality in either weighted cancellation occurs at the Case A/B boundary with

```text
a=1/40,
b=0.
```

Thus

```text
rho=2a=1/20,
j=chi-4a-2b=1/5,
c_y=chi-2a-2b=1/4.
```

Consequently

```text
column cofactor support exponent = 1/4-j = 1/20,
full Cayley row N-lift exponent  = max(0,1/4-c_y)=0.
```

The equality ledger is

```text
C + primitive pair:          1/2,
linear-column short support: 1/20,
full-row N lift:             0,
---------------------------------
total:                       11/20.
```

The previous twin `1/34` short supports collapse to one `1/20` column support at a new unique point.

---

## 8. Remaining receiver

The new minimal receiver is

```text
ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence.
```

Any possible saturation packet must satisfy

```text
theta=11/40,
phi=1/4,
chi=3/10,
H_star=B^(1/40+o(1)),
H_other=B^o(1),
g_star=B^(1/20+o(1)),
J=B^(1/5+o(1)),
C_Cayley=B^(1/4+o(1)),
|h_-h_+|<=B^(1/20+o(1)),
# {N lifts modulo C_Cayley}=B^o(1).
```

The next exact task is to substitute the now divisor-many reconstructed `N=abcd` back into the signed reciprocal equations and compare it directly with

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
M=M(L_-,L_+).
```

The question is whether the single remaining `B^(1/20)` column-cofactor support is divisor-locked before any averaged theorem is requested.

---

## 9. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T75_CROSS_PROMOTED_TO_MAINLINE=false
```

The live obstruction is still an exact quotient/factorization problem. `t75/tH20` remain in the fixed-U coefficient space and are not used for this theorem.

If the next stage exhausts the signed reciprocal substitution and leaves a genuine average over the one `B^(1/20)` cofactor, then an H line may be opened for that exact minimized receiver only.

---

## Stage boundary

```text
STAGE14_4CW=COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION
MERGED_X11_IMPORTED=true
MERGED_S7_37_IMPORTED=true
MERGED_4CV_COLUMN_RECONSTRUCTION_IMPORTED=true
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_PROVED=true
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false
CAYLEY_GOOD_CORE_LOWER_EXPONENT=chi-2a-2b
JOINT_COLUMN_CORE_LOWER_EXPONENT=chi-4a-2b
FULL_ROW_N_LIFT_EXPONENT=max(0,2a+2b-d)
COLUMN_COFACTOR_EXPONENT=4a+2b-d
NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=4:3
NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=2:1
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20
IMPROVEMENT_OVER_MERGED_X11_19_34=3/340
CURRENT_GAP_TO_SQRT=1/20
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
ELEVEN_TWENTIETHS_SATURATION_THETA=11/40
ELEVEN_TWENTIETHS_SATURATION_PHI=1/4
ELEVEN_TWENTIETHS_COMMON_CORE_EXPONENT=3/10
ELEVEN_TWENTIETHS_SELECTED_CROSS_ROOT_EXPONENT=1/40
ELEVEN_TWENTIETHS_OTHER_CROSS_ROOT_EXPONENT=0
ELEVEN_TWENTIETHS_SELECTED_RESIDUAL_GCD_EXPONENT=1/20
ELEVEN_TWENTIETHS_JOINT_COLUMN_CORE_EXPONENT=1/5
ELEVEN_TWENTIETHS_CAYLEY_GOOD_CORE_EXPONENT=1/4
ELEVEN_TWENTIETHS_COLUMN_SHORT_SUPPORT_EXPONENT=1/20
ELEVEN_TWENTIETHS_FULL_ROW_LIFT_EXPONENT=0
REMAINING_RECEIVER=ElevenTwentiethsFullCayleyRowUniqueNLinearShortCofactorIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T75_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4cx
```
