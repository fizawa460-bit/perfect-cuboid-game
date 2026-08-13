# Stage14-4cy — cross-root-square reduction of the Cayley row and unique 23/44 saturation

## Status

`COMPLETE_CROSS_ROOT_SQUARE_ROW_REDUCTION_AND_UNIQUE_23_44_SATURATION`

Stage14-4cy consumes latest merged main through `4cx`, merged `s7-39`, merged `s7-31`, and the signed reciprocal/Cayley reconstruction chain.

The entering canonical whole-family theorem is

```text
V(B) << B^(23/44+o(1)).
```

Stage14-4cx proved the exponent and left a one-parameter equality segment

```text
theta=23/88,
19/88<=phi<=21/88,
H=B^(s+o(1)),
s=phi-19/88.
```

The new point is that `H^2` is not merely a column divisor.  It divides both Cayley variables `M` and `N=abcd`.  Since the Cayley-good core is coprime to `H`, the row congruence may be divided by `H^2` without changing its modulus.  The row lift therefore loses the same `2s` exponent as the endpoint-linear column cofactor product.

This does not lower the global exponent below `23/44`, because the old segment has a genuine endpoint at `s=0`.  It does, however, eliminate every other equality packet and reduces the mainline obstruction to one unique cross-root-free point with two equal `B^(1/22)` short coordinates.

No external incidence theorem, sieve theorem, determinant theorem, genus-one theorem, or auxiliary H/tH theorem is used.

---

## 1. Imported balanced packet and current theorem

Use

```text
3/16 <= theta <= 5/16,
1/8  <= phi   <= 1/4,
0 <= theta-phi <= 1/8,
theta+phi >= 3/8,

C=B^(chi+o(1)),
chi=2theta+2phi-3/4.
```

Merged 4cx proves on the nonproportional branch

```text
chi<=1/4+o(1),
C_Cayley/J=B^o(1),
gcd(C_Cayley,H)=1,
D=C/J | B^o(1)*H^2,
H|h_-,
H|h_+.
```

It also gives the whole-family theorem

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44.
```

The proportional branch is already

```text
E_prop<=7/16<1/2
```

by merged s7-37 and remains irrelevant for the present equality analysis.

Retain the always-available complete counts

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4.
```

For the total cross-root gcd write

```text
H=B^(s+o(1)).
```

Merged s7-34/s7-39 gives the complete root-gcd count

```text
E_H<=3phi-1/8-3s.                                  (1.1)
```

---

## 2. The same `H^2` divides both Cayley numerator and quotient product

Use the exact Cayley notation

```text
M=4*r*s*X*Y*epsilon_x*epsilon_k,
N=a*b*c*d.
```

Merged 4cs/s7-39 identifies

```text
H=oddpart(gcd(X,Y))
 =oddpart(gcd(c,d)).                                (2.1)
```

Hence

```text
H|X,
H|Y,
```

so

```text
boxed:
H^2|M.                                             (2.2)
```

Likewise

```text
H|c,
H|d,
```

and therefore

```text
boxed:
H^2|N.                                             (2.3)
```

Define the reduced positive integers

```text
M_H:=M/H^2,
N_H:=N/H^2.                                        (2.4)
```

The reduction is exact because `H` is odd and is an actual integer divisor in both factors; no exponent-only relaxation is being used.

Since

```text
N<=B^(1/4+o(1)),
```

we have

```text
boxed:
N_H<=B^(1/4-2s+o(1)).                              (2.5)
```

---

## 3. Cayley-row congruences survive division by `H^2`

Let the full Cayley-good sign split be

```text
C_Cayley=C_-*C_+,
gcd(C_-,C_+)=1,

C_- | M-N,
C_+ | M+N.                                         (3.1)
```

Merged s7-39/4cx proves

```text
gcd(C_Cayley,H)=1.                                (3.2)
```

Thus every prime power of `C_-` and `C_+` is a unit on `H^2`.  From

```text
M-N=H^2(M_H-N_H),
M+N=H^2(M_H+N_H),
```

we may cancel `H^2` modulo the same Cayley factors:

```text
boxed:
C_- | M_H-N_H,
C_+ | M_H+N_H.                                     (3.3)
```

Therefore, after the column reconstruction fixes `M_H`, the same full Cayley-row CRT fixes one residue class

```text
N_H == N_{H,0} (mod C_Cayley).                    (3.4)
```

If

```text
C_Cayley=B^(c_C+o(1)),
```

the number of possible reduced row lifts is

```text
boxed:
E_row,H<=max(0,1/4-2s-c_C).                        (3.5)
```

Because 4cx gives

```text
C_Cayley/J=B^o(1),
```

we may replace `c_C` by the joint-core exponent `j` at fixed-power scale:

```text
boxed:
E_row,H<=max(0,1/4-j-2s).                          (3.6)
```

This is the row analogue of removing the common cross-root divisor from both endpoint-linear columns.

---

## 4. The column has the same reduced support

The endpoint-linear allocation is

```text
L_-=J_L-*h_-,
L_+=J_L+*h_+,
J_L-*J_L+=J.
```

Merged 4cx proves

```text
H|h_-,
H|h_+.
```

Define

```text
h_-^0=h_-/H,
h_+^0=h_+/H.                                       (4.1)
```

On the nonproportional branch

```text
0<|L_-L_+|<=B^(1/4+o(1)).
```

Consequently

```text
|h_-^0 h_+^0|
 <=B^(1/4-j-2s+o(1)).                              (4.2)
```

After fixing the product, its ordered split is divisor-many, so

```text
boxed:
E_col,H<=max(0,1/4-j-2s).                          (4.3)
```

The row and column short supports are therefore the same exponent after the cross-root square is removed.

```text
CROSS_ROOT_SQUARE_REMOVED_FROM_BOTH_COLUMN_AND_ROW=true.
```

---

## 5. Replace `j` by the common-core exponent

Merged 4cx/s7-39 gives

```text
C/C_Cayley | B^o(1)*H^2,
C_Cayley/J=B^o(1).
```

Therefore

```text
boxed:
j>=chi-2s-o(1).                                    (5.1)
```

Insert this into (3.6) and (4.3):

```text
1/4-j-2s
 <=1/4-(chi-2s)-2s+o(1)
 =1/4-chi+o(1).
```

Hence on the surviving low-core region

```text
boxed:
E_row,H<=max(0,1/4-chi),
E_col,H<=max(0,1/4-chi).                           (5.2)
```

Since merged 4cx already removes every fixed-power `chi>1/4` nonproportional block, we may henceforth assume

```text
chi<=1/4.
```

Thus both short supports have the common upper exponent

```text
1/4-chi.                                           (5.3)
```

---

## 6. New cross-root-reduced reconstruction count

The common-core plus first primitive root-line cost remains

```text
C:                  chi,
primitive pair:      2phi-chi,
```

hence `2phi` total.

Add the two reduced short supports (5.2):

```text
boxed:
E_R2
 <=2phi+2*(1/4-chi)
 =2phi+1/2-2chi.                                   (6.1)
```

Using

```text
chi=2theta+2phi-3/4,
```

this becomes

```text
boxed:
E_R2<=2-4theta-2phi.                               (6.2)
```

This is an alternative complete count of exactly the same physical block as (1.1).  No common-core divisor is charged twice.

The previous 4cx count was

```text
2phi+1/2-2chi+2s.
```

Stage14-4cy removes precisely the final `+2s` row penalty.

```text
CROSS_ROOT_REDUCED_ROW_SAVING_EXPONENT=2s.
```

---

## 7. Whole-strip bound remains `23/44`

We now combine

```text
E_s<=max(2theta,1-2theta),
E_k<=3theta-1/4,
E_H<=3phi-1/8-3s,
E_R2<=2-4theta-2phi.                               (7.1)
```

### 7.1. `theta<=1/4`

Then

```text
E<=E_k<=1/2<23/44.                                 (7.2)
```

### 7.2. `1/4<=theta<=23/88`

Here

```text
E<=E_s=2theta<=23/44.                              (7.3)
```

### 7.3. `theta>=23/88` and `phi<=19/88`

From (1.1), dropping only the favorable `-3s`,

```text
E<=E_H
 <=3phi-1/8
 <=3*(19/88)-1/8
 =23/44.                                           (7.4)
```

### 7.4. `theta>=23/88` and `phi>=19/88`

From (6.2),

```text
E<=E_R2
 <=2-4*(23/88)-2*(19/88)
 =23/44.                                           (7.5)
```

These cases cover the whole physical strip.  Together with the proportional `7/16` branch,

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44.       (7.6)
```

Therefore

```text
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false.
```

The value of Stage14-4cy is not a new exponent but the collapse of the equality geometry.

---

## 8. Equality is now a unique point

Suppose a sequence saturates `23/44` in the Stage14-4cy envelope.

- Section 7.2 forces
  ```text
  theta=23/88.
  ```
- Section 7.3 requires
  ```text
  phi>=19/88
  ```
  for the `E_H` bound not to be strict.
- Section 7.4 requires
  ```text
  phi<=19/88
  ```
  for the reconstruction bound not to be strict.

Hence

```text
boxed:
theta=23/88,
phi=19/88.                                         (8.1)
```

Then

```text
chi
 =2*(23/88)+2*(19/88)-3/4
 =9/44.                                            (8.2)
```

At this point

```text
E_H<=23/44-3s.
```

Thus equality additionally forces

```text
boxed:
s=0,
H=B^o(1).                                          (8.3)
```

Merged s7-35 then gives

```text
g_star=B^o(1).                                     (8.4)
```

Since

```text
C/C_Cayley | B^o(1)*H^2,
C_Cayley/J=B^o(1),
```

we get

```text
boxed:
C=J=C_Cayley=B^(9/44+o(1))                        (8.5)
```

at fixed-power scale, and

```text
D=C/J=B^o(1).                                      (8.6)
```

Thus the old 4cx saturation segment

```text
19/88<=phi<=21/88
```

has collapsed to its left endpoint only.

```text
TWENTYTHREE_44_SATURATION_SEGMENT_COLLAPSED_TO_POINT=true.
```

---

## 9. Exact remaining short ledger

At (8.1)--(8.5),

```text
1/4-chi
 =1/4-9/44
 =1/22.                                            (9.1)
```

Therefore

```text
boxed:
column residual support <= B^(1/22+o(1)),
reduced row lift        <= B^(1/22+o(1)).           (9.2)
```

The common-core/primitive-pair base is

```text
2phi=19/44.                                        (9.3)
```

Hence the equality ledger is

```text
C + primitive pair:       19/44,
column residual:           1/22,
reduced row lift:          1/22,
--------------------------------
total:                     23/44.                  (9.4)
```

There is no fixed-power cross-root gcd, residual coordinate gcd, Cayley-only annulus, or lost core left.

---

## 10. Compatibility with merged s7-31

At the unique point,

```text
mu<=2theta-2phi=1/11,
nu<=1/4+2phi-2theta=7/44,
chi=9/44.                                          (10.1)
```

Therefore

```text
nu-chi<=-1/22.                                     (10.2)
```

Merged s7-31 gives

```text
# {(c,d)}
 <=B^(max(0,nu-chi)+o(1))
 =B^o(1)                                           (10.3)
```

once its outer data are fixed.

Also

```text
H=oddpart(gcd(c,d))=B^o(1),                        (10.4)
```

consistent with (8.3).

Thus the remaining obstruction is not a moving common gcd or a large opposite signed quotient pair.  It is the exact compatibility between two short coordinates attached to an essentially primitive reciprocal packet.

---

## 11. New minimal receiver

The new mainline receiver is

```text
TwentyThreeFortyFourthsCrossRootFreeEqualCoreTwinOneTwentySecondLiftIncidence.
```

Every possible saturation sequence satisfies

```text
theta=23/88,
phi=19/88,
chi=9/44,
H=B^o(1),
g_star=B^o(1),
D=C/J=B^o(1),
C_Cayley/J=B^o(1),
C=J=C_Cayley=B^(9/44+o(1)),
column residual<=B^(1/22+o(1)),
reduced row lift<=B^(1/22+o(1)),
# opposite signed quotient pairs on a fixed outer fiber = B^o(1).
```

The next exact task is to substitute the divisor-many opposite quotient pair and the reconstructed column data into the two signed reciprocal equations and determine whether the two `1/22` short coordinates are independent.  A single algebraic relation reducing their joint support by `B^(1/44)` would already reach the square-root exponent.

---

## 12. H / tH decision

No mainline auxiliary theorem is needed at Stage14-4cy.

```text
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH21_CROSS_PROMOTED_TO_MAINLINE=false
T77_CROSS_PROMOTED_TO_MAINLINE=false.
```

The merged s7-39 theorem is used only through exact Cayley/cross-root coprimality and square support.  The fixed-U `t77` projective ray-character kernel is a different coefficient space and is not cross-promoted.

The current receiver still has unexhausted exact signed-reciprocal arithmetic.  Reconsider an H line only after Stage14-4cz tests the two surviving `1/22` coordinates for direct algebraic dependence.

---

## Stage boundary

```text
STAGE14_4CY=COMPLETE_CROSS_ROOT_SQUARE_ROW_REDUCTION_AND_UNIQUE_23_44_SATURATION
MERGED_4CX_IMPORTED=true
MERGED_S7_39_IMPORTED=true
MERGED_S7_31_COMPATIBILITY_CHECKED=true
CROSS_ROOT_SQUARE_DIVIDES_CAYLEY_NUMERATOR=true
CROSS_ROOT_SQUARE_DIVIDES_SIGNED_QUOTIENT_PRODUCT=true
CAYLEY_ROW_DESCENDS_AFTER_CROSS_ROOT_SQUARE_DIVISION=true
CROSS_ROOT_SQUARE_REMOVED_FROM_COLUMN_SUPPORT=true
CROSS_ROOT_SQUARE_REMOVED_FROM_ROW_SUPPORT=true
CROSS_ROOT_REDUCED_COLUMN_SUPPORT=max(0,1/4-j-2s)
CROSS_ROOT_REDUCED_ROW_SUPPORT=max(0,1/4-j-2s)
JOINT_CORE_LOWER_EXPONENT=chi-2s
CROSS_ROOT_REDUCED_RECONSTRUCTION_EXPONENT=2phi+2*max(0,1/4-chi)
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
TWENTYTHREE_44_SATURATION_SEGMENT_COLLAPSED_TO_POINT=true
TWENTYTHREE_44_UNIQUE_SATURATION_THETA=23/88
TWENTYTHREE_44_UNIQUE_SATURATION_PHI=19/88
TWENTYTHREE_44_COMMON_CORE_EXPONENT=9/44
TWENTYTHREE_44_TOTAL_CROSS_ROOT_EXPONENT=0
TWENTYTHREE_44_SELECTED_RESIDUAL_GCD_EXPONENT=0
TWENTYTHREE_44_LOST_CORE_EXPONENT=0
TWENTYTHREE_44_CAYLEY_ANNULUS_EXPONENT=0
TWENTYTHREE_44_COLUMN_RESIDUAL_EXPONENT=1/22
TWENTYTHREE_44_REDUCED_ROW_LIFT_EXPONENT=1/22
TWENTYTHREE_44_OPPOSITE_SIGNED_QUOTIENT_PAIR_EXPONENT=0
CURRENT_GAP_TO_SQRT=1/44
REMAINING_RECEIVER=TwentyThreeFortyFourthsCrossRootFreeEqualCoreTwinOneTwentySecondLiftIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH21_CROSS_PROMOTED_TO_MAINLINE=false
T77_CROSS_PROMOTED_TO_MAINLINE=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4cz
```
