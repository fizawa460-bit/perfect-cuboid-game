# Stage14-4cw — full Cayley-row CRT after joint-core column reconstruction and the 11/20 bound

## Status

`COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION`

Stage14-4cw consumes merged `X11`, merged `s7-36`, merged `s7-35`, merged `4cv`, and the Cayley-good-core sign allocation of merged `4cr/4cu`.

The strongest theorem on current main entering this stage is

```text
V(B) << B^(19/34+o(1)).
```

Merged `X11` has already removed the proportional `9/16` obstruction and leaves the nonproportional row/column equality profile as the global barrier.

The new point is a quantifier-order correction inside that nonproportional receiver.

Merged `4cv` used the same joint core `J` for both:

1. the endpoint-linear column divisibility needed to reconstruct `z_1,z_2` and hence `M`, and
2. the Cayley row CRT used to reconstruct `N=abcd`.

The first restriction genuinely requires the residual/Cayley intersection `J`.  The second does not.  **After the column step has fixed `M`, the row CRT may use the entire already-fixed Cayley-good core `C_Cayley`, which is generally larger than `J`.**

This does not charge the common core twice.  `C` is chosen once; `J` and `C_Cayley` are nested divisors of that same chosen core, used sequentially for two different reconstructions.

The resulting row lift vanishes at fixed-power scale at the new equality profile and the whole-family exponent improves to

```text
boxed:
V(B) << B^(11/20+o(1)).
```

No external H/tH theorem is used.

---

## 1. Imported balanced packet

Use

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

On the nonproportional branch choose the larger cross-root cell and write

```text
H_star = B^(a+o(1)),
H_other= B^(b+o(1)),
a>=b>=0.                                             (1.1)
```

Merged `s7-35` proves the exact selected residual-gcd collapse

```text
g_star/H_star^2 | oddpart(omega_1*omega_2)=B^o(1),
```

so

```text
rho:=log_B g_star = 2a.                              (1.2)
```

Merged `s7-34` supplies the fourth-power-root complete count

```text
boxed:
E_H <= 3phi-1/8-3a-3b.                              (1.3)
```

Merged `s7-36` used these facts with the `4cv` joint-core row/column count to prove `19/34`.

---

## 2. Two nested good cores

Merged `4cu` defines a Cayley-good core

```text
C_Cayley | C
```

with

```text
C/C_Cayley | B^o(1)*H^2,
H=H_star*H_other.                                   (2.1)
```

Therefore, if

```text
C_Cayley=B^(c_y+o(1)),
```

then

```text
boxed:
c_y >= chi-2a-2b.                                  (2.2)
```

The selected residual host is primitive only after its coordinate-gcd square has also been removed.  Intersecting that residual-good core with `C_Cayley` gives the joint core

```text
J=B^(j+o(1)).
```

Before the coarse relaxation, merged `4cu/s7-36` give

```text
boxed:
j >= chi-4a-2b.                                    (2.3)
```

Thus

```text
J | C_Cayley | C,
```

and the difference between the two good-core exponents is exactly where the selected residual coordinate-gcd square can appear.

---

## 3. Column step still uses only `J`

Retain the endpoint-linear forms

```text
L_- = z_1*r_2*s_2-z_2*r_1*s_1,
L_+ = z_1*r_2*s_2+z_2*r_1*s_1.
```

On the nonproportional branch

```text
L_-L_+ != 0,
|L_-L_+|<=B^(1/4+o(1)).                             (3.1)
```

The residual/Cayley orientation comparison is available on `J`, giving column factors

```text
J_L- | L_-,
J_L+ | L_+,
J_L-*J_L+=J.
```

Write

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+.
```

Hence the total column-cofactor support has exponent

```text
ell_col
 <= max(0,1/4-j).                                   (3.2)
```

Because `J|L_-L_+` and the product is nonzero of size at most `B^(1/4+o(1))`, any physical packet also forces

```text
j<=1/4+o(1).                                        (3.3)
```

Using (2.3), put

```text
d:=chi-1/4.
```

Then (3.3) implies

```text
4a+2b-d >= -o(1),
```

and therefore

```text
boxed:
ell_col <= 4a+2b-d.                                (3.4)
```

Once the column allocation and `(h_-,h_+)` are fixed,

```text
z_1*r_2*s_2=(L_++L_-)/2,
z_2*r_1*s_1=(L_+-L_-)/2.
```

Since `r_i,s_i=B^o(1)`, the physical `(z_1,z_2)` are recovered divisor-many, and so is

```text
M=4rsXY epsilon_x epsilon_k.
```

This is exactly the legal 4cv column reconstruction.

---

## 4. After `M` is fixed, use the full Cayley-good row

Merged `4cr` partitions the **entire** Cayley-good core into two coprime row factors

```text
C_Cayley=C_-*C_+,
gcd(C_-,C_+)=1,
```

with

```text
C_- | M-N,
C_+ | M+N,
N=abcd.                                             (4.1)
```

These row congruences do not require the selected residual host to be primitive.  They are already proved on `C_Cayley` itself.

Now the column step has fixed `M`.  Hence CRT on the full row gives one class

```text
boxed:
N == N_0(M,C_-,C_+) (mod C_Cayley).                (4.2)
```

Since

```text
N<=B^(1/4+o(1)),
```

the number of row lifts is

```text
#N <= B^(ell_row+o(1)),
```

where, by (2.2),

```text
boxed:
ell_row
 <= max(0,1/4-c_y)
 <= max(0,2a+2b-d).                                 (4.3)
```

Once `N` is fixed, the signed quotient quadruple `(a_q,b_q,c_q,d_q)` with product `N` is divisor-many, exactly as in merged `4cv`; consequently the separate `u_res,v_res` supports are not charged again.

### No double charge

The count order is

```text
choose C once
-> primitive common-core pair
-> choose divisor-many nested cores/sign allocations
-> use J-column to fix M
-> use full C_Cayley-row to fix N modulo C_Cayley
-> divisor-many reciprocal reconstruction.
```

Neither `J` nor `C_Cayley` is summed as a new ambient modulus after `C` has been charged.  The full row is simply unused information in the already-fixed Cayley-good divisor.

Therefore

```text
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false.          (4.4)
```

---

## 5. New complete reconstruction count

The already-charged outer support is

```text
C:                         B^chi,
primitive (U,V) fiber:     B^(2phi-chi).
```

Sections 3-4 add only the two short lifts.  Therefore

```text
boxed:
E_FR
 <= 2phi
    +(4a+2b-d)
    +max(0,2a+2b-d).                                (5.1)
```

This is a complete count of the same nonproportional physical block as (1.3).

Split according to whether the full-row lift has fixed-power length.

---

## 6. Case A: full Cayley row already reaches the `N` range

Assume

```text
2a+2b<=d.                                           (6.1)
```

Then the second short term in (5.1) is zero:

```text
E_FR <= 2phi+4a+2b-d.                               (6.2)
```

Compare with

```text
E_H<=3phi-1/8-3a-3b.
```

Since these are alternative complete counts,

```text
min(E_H,E_FR)
 <= (4E_H+3E_FR)/7.
```

The selected cross exponent `a` cancels and the `b` coefficient is favorable:

```text
4*(-3)+3*4=0,
4*(-3)+3*2=-6.
```

Hence

```text
E
 <= (12phi-6theta+5/2)/7 -(6/7)b
 <= (12phi-6theta+5/2)/7.                           (6.3)
```

Using `phi<=1/4`,

```text
boxed:
E <= 11/14-(6/7)theta.                              (6.4)
```

---

## 7. Case B: a short full-row lift remains

Assume

```text
2a+2b>=d.                                           (7.1)
```

Then (5.1) becomes

```text
E_FR <= 2phi+6a+4b-2d.                              (7.2)
```

Now use

```text
min(E_H,E_FR)
 <= (2E_H+E_FR)/3.
```

Again the selected exponent cancels and `b` is favorable:

```text
2*(-3)+6=0,
2*(-3)+4=-2.
```

Therefore

```text
E
 <= (4phi-4theta+7/4)/3 -(2/3)b
 <= (4phi-4theta+7/4)/3.                            (7.3)
```

With `phi<=1/4`,

```text
boxed:
E <= 11/12-(4/3)theta.                              (7.4)
```

---

## 8. Whole-strip nonproportional bound `11/20`

Retain the merged complete counts

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.
```

### 8.1. `theta<=1/4`

```text
E_k<=1/2<11/20.
```

### 8.2. `1/4<=theta<=11/40`

Here `E_s=2theta`, so

```text
E_s<=11/20.
```

### 8.3. `theta>=11/40`

In Case A, (6.4) gives

```text
E<=11/14-(6/7)(11/40)=11/20.
```

In Case B, (7.4) gives

```text
E<=11/12-(4/3)(11/40)=11/20.
```

Both right sides decrease strictly with `theta` after `11/40`.

Thus

```text
boxed:
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20.  (8.1)
```

---

## 9. Equality profile

The inequalities above show that equality at `11/20` can occur only at

```text
boxed:
theta=11/40,
phi=1/4.                                            (9.1)
```

Then

```text
chi=3/10,
d=chi-1/4=1/20.                                   (9.2)
```

Equality in either weighted cancellation forces the boundary between Cases A and B together with

```text
boxed:
a=1/40,
b=0.                                               (9.3)
```

Hence

```text
rho=2a=1/20,
```

and equality in the two good-core lower bounds requires

```text
boxed:
j=1/5,
c_y=1/4.                                          (9.4)
```

Therefore

```text
column cofactor support exponent = 1/4-j = 1/20,
full Cayley row N-lift exponent = max(0,1/4-c_y)=0. (9.5)
```

At the equality profile the ledger is

```text
C + primitive pair:          1/2,
linear-column short support: 1/20,
full-row N lift:             0,
---------------------------------
total:                       11/20.
```

The two previous `1/34` row/column short supports have therefore collapsed to a **single** `1/20` column support at a new point.

---

## 10. Proportional branch is already subcritical

Merged `X11` proves

```text
boxed:
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24.     (10.1)
```

Since

```text
13/24 < 11/20,
```

the proportional family does not control the new theorem.

Therefore every physical packet satisfies

```text
E<=max(11/20,13/24)=11/20.
```

Hence

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20
IMPROVEMENT_OVER_MERGED_X11_19_34=3/340
CURRENT_GAP_TO_SQRT=1/20
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.          (10.2)
```

---

## 11. New minimal receiver

Define

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
# {N lifts modulo C_Cayley}=B^o(1).                 (11.1)
```

Thus the row lift is no longer a fixed-power degree of freedom.  The only remaining polynomial short parameter in this reconstruction is the linear-column cofactor pair/product.

The next exact task is to substitute the now uniquely reconstructed `N=abcd` back into the reciprocal signed-quotient equations and compare it directly with

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
M=M(L_-,L_+).
```

The objective is to determine whether the single `B^(1/20)` cofactor support is itself divisor-locked by the signed quotient factorization, before requesting any averaged theorem.

---

## 12. H / tH decision

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH20_CROSS_PROMOTED_TO_MAINLINE=false
T75_CROSS_PROMOTED_TO_MAINLINE=false
```

Reason: the remaining receiver contains one explicit short integer cofactor attached to an exact full-row CRT and reciprocal factorization.  Its pointwise arithmetic has not been exhausted.

The fixed-`U` t/tH coefficient space remains separate.

---

## Stage boundary

```text
STAGE14_4CW=COMPLETE_FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_RECONSTRUCTION_AND_11_20_PROMOTION
MERGED_X11_IMPORTED=true
MERGED_S7_36_IMPORTED=true
MERGED_S7_35_IMPORTED=true
MERGED_4CV_IMPORTED=true
FULL_CAYLEY_GOOD_CORE_ROW_REUSED_AFTER_COLUMN_M_RECONSTRUCTION=true
FULL_CAYLEY_ROW_AFTER_JOINT_COLUMN_DOUBLE_CHARGE=false
CAYLEY_GOOD_CORE_LOWER_EXPONENT=chi-2a-2b
JOINT_COLUMN_CORE_LOWER_EXPONENT=chi-4a-2b
FULL_CAYLEY_ROW_N_LIFT_EXPONENT=max(0,1/4-chi+2a+2b)
JOINT_COLUMN_COFACTOR_EXPONENT=1/4-j
NONPROPORTIONAL_CASE_A_WEIGHTED_COMBINATION=4:3
NONPROPORTIONAL_CASE_B_WEIGHTED_COMBINATION=2:1
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=11/20
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=13/24
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/20
IMPROVEMENT_OVER_MERGED_X11_19_34=3/340
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
