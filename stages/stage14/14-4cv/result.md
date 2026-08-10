# Stage14-4cv — row/column cofactor reconstruction and the 7/12 bound

## Status

`COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION`

Stage14-4cv consumes merged `4cu` and the subsequently merged `s7-33` orientation-identification/no-go result.  The current mainline theorem entering this stage is

```text
V(B) << B^(19/32+o(1)).
```

with the only possible `19/32` equality packet localized by 4cu at

```text
theta=19/64,
phi=1/4,
chi=11/32,
rho=1/32,
J_star=B^(1/4+o(1)).
```

The new observation is that the same joint core `J_star` has two exact, already-proved primewise partitions:

1. the Cayley row sign `C_-/C_+`, and
2. the endpoint-linear column sign `L_-/L_+`.

These do **not** supply two independent moduli.  Instead they give a 2x2 partition of one modulus.  Reading that partition by columns reconstructs the endpoint roots from short cofactors; reading it by rows reconstructs the full signed-quotient product `N=abcd` from one CRT class and a short lift.  The two short supports can then replace the old independent residual-support charge.

The resulting alternative complete count, combined blockwise with the 4cu gcd-stratified xi-host count and the merged s7-32 counts, yields

```text
boxed:
V(B) << B^(7/12+o(1)).
```

No external incidence theorem is used.

---

## 1. Imported notation and 4cu joint core

Keep

```text
C=B^(chi+o(1)),
chi=2theta+2phi-3/4,

3/16<=theta<=5/16,
1/8<=phi<=1/4,
0<=theta-phi<=1/8,
theta+phi>=3/8.
```

Use the signed-quotient notation

```text
a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-,
N=a*b*c*d.
```

Merged s7-27 gives

```text
oddpart(a*b)=oddpart(u_res),
oddpart(c*d)=oddpart(v_res),
```

up to the finite 2-primary decoration.  Consequently

```text
N <= B^(1/4+o(1))
```

because `u_res*v_res<=B^(1/4+o(1))`.

Use

```text
r=r1*r2,
s=s1*s2,
X=x1*x2,
Y=y1*y2,
M=4*r*s*X*Y*epsilon_x*epsilon_k.
```

Since

```text
z_i=2*x_i*y_i/g_i,
```

we have the exact finite-2-primary identity

```text
4*r*s*X*Y
 = g1*g2*r1*r2*s1*s2*z1*z2.
```

Thus, once `(z1,z2)` and the endpoint-small/2-primary decoration are fixed, `M` is fixed exactly.

Merged 4cr gives the Cayley sign allocation on the good core:

```text
C_- | M-N,
C_+ | M+N,
gcd(C_-,C_+)=1.
```

Merged 4cu chooses one xi residual host `star` and proves a joint Cayley/residual core

```text
J=J_star | C,
J >= B^(chi-3rho-o(1)),
```

where

```text
g_star=B^(rho+o(1)).
```

On the nonproportional branch it also proves

```text
J | L_-*L_+,

L_-=z1*r2*s2-z2*r1*s1,
L_+=z1*r2*s2+z2*r1*s1,

0<|L_-*L_+|<=B^(1/4+o(1)).
```

The selected xi-host complete count is

```text
E_xi,star <= 3phi-1/8-rho.                         (1.1)
```

The proportional branch `L_-=0` is already bounded by `9/16` in 4cu and remains strictly below the new barrier.

---

## 2. Exact 2x2 row/column partition of one modulus

Merged 4cu proves that on `J` the three Gaussian root orientations have rank-two relative sign entropy.  Therefore every odd prime power of `J` has exactly one Cayley row sign and exactly one endpoint-linear column sign.

Define the four prime-power cells

```text
J_{--}, J_{-+}, J_{+-}, J_{++},
```

where the first sign is the Cayley row (`C_-` or `C_+`) and the second sign is the linear column (`L_-` or `L_+`).  Then exactly

```text
boxed:
J=J_{--}*J_{-+}*J_{+-}*J_{++},
```

and the four factors are pairwise coprime.

Define row products

```text
J_C- = J_{--}*J_{-+},
J_C+ = J_{+-}*J_{++},
```

and column products

```text
J_L- = J_{--}*J_{+-},
J_L+ = J_{-+}*J_{++}.
```

Then

```text
J_C-*J_C+=J,
gcd(J_C-,J_C+)=1,

J_L-*J_L+=J,
gcd(J_L-,J_L+)=1,
```

with exact divisibilities

```text
J_C- | M-N,
J_C+ | M+N,

J_L- | L_-,
J_L+ | L_+.
```

This is a partition of one already-charged modulus.  No product of row and column moduli is introduced.

Merged s7-33 is compatible with this statement and supplies the necessary warning: the common-core Gaussian orientation is the same orientation already carried by the primitive agreement root line.  Hence none of the four cells may be recharged as an independent Gaussian spacing modulus.

---

## 3. Column reading: short cofactors reconstruct the endpoint roots

On the nonproportional branch define positive/signed integer cofactors by

```text
L_- = J_L-*h_-,
L_+ = J_L+*h_+.
```

Since the row/column cells are pairwise coprime, these are exact integer quotients.  Put

```text
H_L := |h_-*h_+|
     = |L_-*L_+|/J.
```

Write

```text
J=B^(j+o(1)).
```

Then

```text
boxed:
H_L <= B^(1/4-j+o(1)).                             (3.1)
```

The number of ordered cofactor pairs `(h_-,h_+)` with product in this range is

```text
B^(1/4-j+o(1)).                                    (3.2)
```

Once `J_L-,J_L+,h_-,h_+` are fixed,

```text
A_z := z1*r2*s2 = (L_+ + L_-)/2,
B_z := z2*r1*s1 = (L_+ - L_-)/2.
```

The endpoint-small tuple `(r_i,s_i)` is already `B^o(1)`, so every physical lift has only divisor-many possibilities for `(z1,z2)`.  Invalid parity/sign cases are discarded.

Thus the endpoint linear product does not require an independent `B^(1/4)` support once its `J`-column divisibility is retained.

---

## 4. Row reading: CRT reconstructs `N=abcd` up to a short lift

The row congruences are

```text
N == M  (mod J_C-),
N == -M (mod J_C+).
```

Because the two row moduli are coprime, CRT gives one residue class

```text
N == N_0 (mod J).
```

Both `M` and `N` are at most `B^(1/4+o(1))`.  Therefore after the column reading has reconstructed `(z1,z2)` and hence `M`, the number of positive admissible `N` is

```text
boxed:
#N <= B^(1/4-j+o(1)).                              (4.1)
```

Equivalently write

```text
N=N_0+J*h_N,
|h_N|<=B^(1/4-j+o(1)).
```

For fixed `N`, the signed quotient quadruple `(a,b,c,d)` has only divisor-many possibilities:

```text
# {(a,b,c,d): a*b*c*d=N} <= tau_4(N)=B^o(1),
```

with the dyadic, odd-part and 2-primary masks only reducing the count.  In particular the separate residual supports `u_res` and `v_res` are then fixed up to `B^o(1)` through

```text
oddpart(a*b)=oddpart(u_res),
oddpart(c*d)=oddpart(v_res).
```

This is the key quantifier replacement in 4cv.

---

## 5. Complete row/column reconstruction count

Use the legal charged-once order

```text
C
-> one primitive common-core pair (U,V)
-> divisor-many 2x2 cell allocation of J|C
-> short linear cofactors (h_-,h_+)
-> endpoint roots z1,z2 and M
-> short CRT lift h_N and N
-> divisor-many signed quotient quadruple (a,b,c,d)
-> merged reciprocal reconstruction.
```

The support costs are

```text
C:                         B^chi,
primitive (U,V):           B^(2phi-chi),
linear cofactor pair:      B^(1/4-j),
CRT lift for N:            B^(1/4-j),
remaining reconstruction: B^o(1).
```

Hence

```text
boxed:
E_RC(theta,phi,j)
 <= 2phi + 1/2 - 2j.                               (5.1)
```

Merged 4cu gives

```text
j >= chi-3rho-o(1),
```

so uniformly

```text
boxed:
E_RC(theta,phi,rho)
 <= 2phi+1/2-2chi+6rho.                            (5.2)
```

This count does not multiply the common core twice: `C` is charged once, the primitive pair uses the already-merged determinant fiber `B^(2phi-chi)`, and both the row and column readings use divisors of the same chosen `J`.

The strong canonical `S/T` associate split rejected by s7-33 is not used anywhere.

---

## 6. Combine with the xi-host count

For the same nonproportional physical block we now have the two complete alternative bounds

```text
E_xi <= 3phi-1/8-rho,                              (6.1)
E_RC <= 2phi+1/2-2chi+6rho.                        (6.2)
```

For any two real numbers `A,B`,

```text
min(A,B) <= (6A+B)/7.
```

Apply this with (6.1)-(6.2).  The `rho` terms cancel:

```text
E
 <= (6(3phi-1/8-rho)
     +(2phi+1/2-2chi+6rho))/7
 = (20phi-2chi-1/4)/7.
```

Substitute

```text
chi=2theta+2phi-3/4
```

to obtain

```text
boxed:
E <= (16phi-4theta+5/4)/7.                         (6.3)
```

This is used together with the merged complete counts

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.
```

---

## 7. Whole-strip 7/12 minimax

### 7.1. `theta<=1/4`

Merged s7-32 gives

```text
E_k<=3theta-1/4<=1/2<7/12.
```

### 7.2. `1/4<=theta<=7/24`

Here

```text
E_s<=2theta<=7/12.
```

### 7.3. `theta>=7/24`

Since `phi<=1/4`, (6.3) gives

```text
E
 <= (4-4theta+5/4)/7
 = 3/4-(4/7)theta
 <= 3/4-(4/7)(7/24)
 = 7/12.
```

Thus every nonproportional block satisfies

```text
boxed:
E_nonprop<=7/12.                                   (7.1)
```

The proportional branch remains

```text
E_prop<=9/16<7/12.
```

Therefore

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12,
IMPROVEMENT_OVER_PREVIOUS_19_32=1/96,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.         (7.2)
```

---

## 8. Unique 7/12 saturation profile

Equality in the proved envelope requires simultaneous equality in the middle/upper split and in the weighted two-count bound.  Hence

```text
boxed:
theta=7/24,
phi=1/4.                                           (8.1)
```

Then

```text
chi=1/3.
```

Equality of (6.1) and (6.2) forces

```text
rho=1/24.
```

The lower joint-core bound then has exponent

```text
j=chi-3rho
 =1/3-1/8
 =5/24.                                           (8.2)
```

Consequently the two remaining short supports each have total exponent

```text
1/4-j=1/24.
```

Thus the only current saturation profile is

```text
boxed:
theta=7/24,
phi=1/4,
C~B^(1/3),
g_star~B^(1/24),
J~B^(5/24),
H_L=|L_-L_+|/J<=B^(1/24+o(1)),
#CRT_lifts(N mod J)<=B^(1/24+o(1)).                (8.3)
```

At equality the 7/12 ledger is exactly

```text
C + primitive root-line fiber:  1/2,
linear cofactor support:         1/24,
CRT N-lift support:              1/24,
--------------------------------------
total:                           7/12.
```

The old `19/32` point `(19/64,1/4)` is therefore strictly subcritical after row/column reconstruction.

---

## 9. Relation to merged s7-33 and fixed-U t-route

Merged s7-33 proves that the residual-host common-core orientation and the primitive agreement root-line orientation are the same local Gaussian object, and it freezes a physical counterexample to a stronger canonical `S/T` UFD split.

Stage14-4cv respects both facts:

- the common core is charged only once;
- the four `J_{sigma,tau}` are merely a partition of that one core;
- no independent Gaussian-spacing factor is multiplied into the determinant count;
- no associate identity such as `K~lambda_S*conj(lambda_T)` is assumed.

The t73/tH19 fixed-`U` norm-value route remains a distinct coefficient space.  It is not cross-promoted into the 4cv theorem.

---

## 10. Remaining receiver and H decision

The current minimal receiver is

```text
SevenTwelfthsJointCoreRowColumnShortCofactorCRTLiftIncidence.
```

It is localized at (8.3) and retains simultaneously

```text
J=J_{--}J_{-+}J_{+-}J_{++},
L_-=J_L-*h_-,
L_+=J_L+*h_+,
N=N_0(M,J_C-,J_C+)+J*h_N,
H_L<=B^(1/24+o(1)),
|h_N|<=B^(1/24+o(1)),
```

with the full reciprocal reconstruction and physical masks.

There is still exact arithmetic left: the two `1/24` cofactors arise from the same four-cell packet and have not yet been compared by an exact resultant/gcd identity.  Therefore no external H theorem is requested yet.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T73_CROSS_PROMOTED_TO_MAINLINE=false.
```

`Stage14-4cw` should compare the linear cofactor product and the Cayley CRT lift directly before any analytic average is requested.

---

## Stage boundary

```text
STAGE14_4CV=COMPLETE_JOINT_CORE_ROW_COLUMN_COFACTOR_RECONSTRUCTION_AND_SEVEN_TWELFTHS_PROMOTION
MERGED_4CU_IMPORTED=true
MERGED_S7_33_IMPORTED=true
JOINT_CORE_TWO_BY_TWO_ROW_COLUMN_PARTITION_PROVED=true
JOINT_CORE_FOUR_CELLS_PAIRWISE_COPRIME=true
LINEAR_COLUMN_COFACTOR_PRODUCT_MAX_EXPONENT=1/4-j
COLUMN_DATA_RECONSTRUCT_ENDPOINT_ROOTS_BO1=true
CAYLEY_ROW_CRT_DETERMINES_N_MOD_J=true
CAYLEY_ROW_N_LIFT_MAX_EXPONENT=1/4-j
FIXED_N_SIGNED_QUOTIENT_QUADRUPLE_MULTIPLICITY=Bo1
ROW_COLUMN_RECONSTRUCTION_BLOCK_EXPONENT=2phi+1/2-2j
ROW_COLUMN_RECONSTRUCTION_RHO_BOUND=2phi+1/2-2chi+6rho
NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/12
PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12
IMPROVEMENT_OVER_PREVIOUS_19_32=1/96
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
SEVEN_TWELFTHS_SATURATION_THETA=7/24
SEVEN_TWELFTHS_SATURATION_PHI=1/4
SEVEN_TWELFTHS_SATURATION_COMMON_CORE_EXPONENT=1/3
SEVEN_TWELFTHS_SATURATION_SELECTED_XI_GCD_EXPONENT=1/24
SEVEN_TWELFTHS_SATURATION_JOINT_CORE_EXPONENT=5/24
SEVEN_TWELFTHS_LINEAR_COFACTOR_EXPONENT=1/24
SEVEN_TWELFTHS_CRT_LIFT_EXPONENT=1/24
STRONG_CANONICAL_ST_SPLIT_USED=false
COMMON_CORE_ORIENTATION_DOUBLE_CHARGED=false
REMAINING_RECEIVER=SevenTwelfthsJointCoreRowColumnShortCofactorCRTLiftIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T73_CROSS_PROMOTED_TO_MAINLINE=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cw
```