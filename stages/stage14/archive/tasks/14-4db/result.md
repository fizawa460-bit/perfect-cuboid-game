# Stage14-4db — cross-root-first lost-core enumeration and globally odd-primitive square-root saturation

## Status

`COMPLETE_CROSS_ROOT_FIRST_LOST_CORE_ENUMERATION_AND_GLOBALLY_ODD_PRIMITIVE_SQRT_SATURATION`

Stage14-4db consumes merged `Stage14-X13`, merged `Stage14-4da`, merged `Stage14-s7-42`, merged `Stage14-4cx`, merged `Stage14-4cz`, and the exact signed reciprocal infrastructure from `s7-27/s7-28`.

The entering canonical whole-family theorem is already

```text
V(B) << B^(1/2+o(1)).
```

Stage14-4db does not improve the whole-family exponent below `1/2`.  Its new result is a quantifier-order refinement: choose the cross-root gcd before the lost core.  Since the lost core is a divisor of the cross-root square, this removes an artificial fixed-power choice and proves a strict saving on every fixed-power cross-root-gcd stratum.

No external theorem is used.

---

## 1. Imported square-root band

Merged X13 proves

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUB_SQRT_POWER_SAVING_PROVED=false.
```

Every possible square-root-saturating nonproportional packet lies in

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=B^(s+o(1)),
0<=s<=phi-5/24.                                    (1.1)
```

The X13 charged-once count has

```text
fixed common-core/primitive-pair base + one reduced column,
post-column reciprocal completion=B^o(1).
```

Put

```text
a_col:=1/4-chi=1/2-2phi.                           (1.2)
```

Then exactly

```text
2phi+a_col=1/2.                                    (1.3)
```

---

## 2. Imported lost-core and root-gcd data

Use the 4cx/4da notation

```text
C=B^(chi+o(1)),
J=B^(j+o(1)),
D=C/J,
D0=D/gcd(D,Omega_0),
Omega_0=B^o(1).                                    (2.1)
```

Set

```text
d:=chi-j.                                          (2.2)
```

Merged 4cx proves

```text
D0|H^2,                                             (2.3)
gcd(J,H)=1.                                        (2.4)
```

Thus

```text
0<=d<=2s.                                          (2.5)
```

Define

```text
G:=H^2/D0=B^(e+o(1)).                              (2.6)
```

Then at exponent scale

```text
e=2s-d.                                            (2.7)
```

Use the same-side root gcd

```text
K=K_x*K_y=B^(kappa+o(1)),                          (2.8)
```

where

```text
K_x=oddpart(gcd(x1,x2)),
K_y=oddpart(gcd(y1,y2)).
```

Merged 4da gives for the reduced single-column product

```text
R_col=(h_-h_+)/D0,
|R_col|<=B^(a_col+o(1)),                            (2.9)

K^2*G | R_col.                                     (2.10)
```

Hence every nonempty fixed-power stratum obeys

```text
2kappa+e<=a_col.                                   (2.11)
```

---

## 3. Reverse the quantifier order: choose `H` before `D0`

Stage14-4da fixed `C,J,D0` first and then counted the possible cross-root excess `G`.  That order is valid and gives its bound

```text
E_4da<=1/2-kappa-e/2.
```

For the square-root saturation problem there is a stronger legal order.

Fix the integer `H`.  Equation (2.3) says

```text
D0|H^2.
```

Therefore

```text
# {D0 : D0|H^2} <= tau(H^2)=B^o(1).                (3.1)
```

For each such `D0`, the quotient

```text
G=H^2/D0                                            (3.2)
```

is already fixed; it is not another polynomially-sized support.

Likewise the cross-root split

```text
H=H_S*H_T,
gcd(H_S,H_T)=1                                    (3.3)
```

has only divisor-many possibilities for fixed `H`.

The endpoint-small factor removed in the definition of `D0` has `B^o(1)` possibilities.  Hence fixed `(J,H)` determine

```text
D=C/J
```

and therefore `C` up to `B^o(1)` possibilities.

Consequently the common-core support can be enumerated by

```text
J choices: B^(j+o(1)),
H choices: B^(s+o(1)),
D0 and endpoint-small decoration: B^o(1),          (3.4)
```

rather than by the crude `B^(chi+o(1))` support for `C`.

This is an alternative complete enumeration, not an extra saving multiplied onto the old `C` count.

---

## 4. Fixed-`C` primitive pair count is unchanged

Once `(J,H,D0)` fix `C` up to `B^o(1)`, use the merged X13/common-core root-line count for the primitive xi-agreement pair `(U,V)`:

```text
fixed C
=> # {(U,V)} <= B^(2phi-chi+o(1)).                 (4.1)
```

The new quantifier order does not reuse the common-core root line and does not alter its modulus.  It only reduces the number of possible common-core values presented to that fixed-`C` count.

---

## 5. The forced column divisor is already fixed

For fixed `H,D0,K`, both factors in

```text
K^2*G | R_col,
G=H^2/D0
```

are fixed.

Therefore the remaining column quotient has support

```text
<=B^(a_col-2kappa-e+o(1))                          (5.1)
```

on a nonempty stratum.  If the exponent on the right is negative, the stratum is empty by (2.11).

The choice of `K=B^(kappa+o(1))` costs at most

```text
B^(kappa+o(1)).                                    (5.2)
```

For fixed `K`, the split `K=K_x K_y` is divisor-many because the two same-side cells are coprime.

---

## 6. Cross-root-first complete count

Charge each moving object once in the order

```text
J
-> H
-> D0|H^2 and endpoint-small decoration
-> C
-> primitive (U,V)
-> K
-> reduced column quotient after K^2*G
-> X13 reverse reciprocal completion.
```

The fixed-power exponents are

```text
J:                              j,
H:                              s,
D0 / C decoration:              0,
primitive (U,V) for fixed C:    2phi-chi,
K:                              kappa,
remaining column:               a_col-2kappa-e,
post-column completion:         0.                 (6.1)
```

Therefore

```text
E_4db
 <= j+s+kappa
    +(2phi-chi)
    +(a_col-2kappa-e).                             (6.2)
```

Using

```text
2phi+a_col=1/2,
d=chi-j,
e=2s-d,
```

we obtain exactly

```text
boxed:
E_4db(s,kappa)<=1/2-kappa-s.                       (6.3)
```

The lost-core exponent `d` cancels completely.

This is stronger than the 4da fixed-`D0` count on every stratum with `d>0`; for `d=0` they agree after using the exact forced divisor.

---

## 7. Consequences for square-root saturation

Equation (6.3) gives

```text
s>0 fixed power
=> E_4db<1/2,                                      (7.1)

kappa>0 fixed power
=> E_4db<1/2.                                      (7.2)
```

Hence every sequence that can still saturate the square-root envelope must satisfy

```text
boxed:
s=0,                                               (7.3)

boxed:
kappa=0.                                           (7.4)
```

Equivalently,

```text
boxed:
H=B^o(1),                                          (7.5)

boxed:
K=B^o(1).                                          (7.6)
```

Since `d<=2s`, (7.3) forces

```text
boxed:
d=0,                                               (7.7)

boxed:
j=chi.                                             (7.8)
```

Thus

```text
boxed:
C/J=B^o(1),                                        (7.9)

boxed:
D0=B^o(1),                                         (7.10)

boxed:
G=B^o(1).                                          (7.11)
```

Merged 4cx already gives

```text
C_Cayley/J=B^o(1),                                 (7.12)
```

so at any square-root saturation sequence the common core, joint core, and Cayley-good core coincide at exponent scale.

---

## 8. Global odd primitivity of the four physical roots

Recall the four pairwise-coprime odd cross-state gcd cells

```text
K_x,
K_y,
H_S,
H_T,
```

with

```text
K=K_x*K_y,
H=H_S*H_T.
```

From (7.5)-(7.6),

```text
boxed:
K_x=K_y=H_S=H_T=B^o(1).                            (8.1)
```

Hence

```text
boxed:
oddpart(gcd(z1,z2))=B^o(1).                        (8.2)
```

More strongly, every odd cross-state root-gcd cell is subpolynomial.  The remaining fixed-power square-root obstruction is therefore globally odd-primitive.

This strengthens the merged s7-42 saturation requirement, which had already forced the same-side product `K` to be subpolynomial but still allowed fixed-power cross-root mass `H`.

---

## 9. Refined square-root band

The remaining possible equality packets satisfy

```text
boxed:
theta=1/4,
5/24<=phi<=1/4,
chi=j=2phi-1/4,
H=B^o(1),
K=B^o(1),
C/J=B^o(1),
C_Cayley/J=B^o(1).                                 (9.1)
```

The only fixed-power residual support still visible in the X13 order is the single primitive column

```text
boxed:
a_col=1/2-2phi.                                    (9.2)
```

The reverse reciprocal completion remains

```text
B^o(1).                                            (9.3)
```

At `phi=1/4`, the column support is already subpolynomial.  At `phi=5/24`, it has maximal exponent `1/12`.

---

## 10. New minimal receiver

The Stage14-4da receiver

```text
SquareRootThetaQuarterCrossRootSquareMatchedLostCorePrimitiveSingleColumnIncidence
```

is replaced by

```text
boxed:
SquareRootThetaQuarterGloballyOddPrimitiveFullJointCoreSingleColumnIncidence.
```

Its mandatory fixed-power data are

```text
theta=1/4,
5/24<=phi<=1/4,
chi=j=2phi-1/4,
H_S=H_T=K_x=K_y=B^o(1),
C/J=B^o(1),
C_Cayley/J=B^o(1),
column support<=B^(1/2-2phi+o(1)),
post-column reciprocal completion=B^o(1).
```

The next deterministic target is the reduced endpoint-linear pair after all fixed-power common root-gcd and lost-core factors are absent.  In particular one should compare the two primitive signed column factors through

```text
L_- = z1*r2*s2-z2*r1*s1,
L_+ = z1*r2*s2+z2*r1*s1
```

after removing only endpoint-small gcds, and test whether their product support can still vary independently of the primitive common-core pair `(U,V)`.

---

## 11. Whole-family theorem

The strongest whole-family theorem remains

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2.         (11.1)
```

Stage14-4db proves strict sub-square-root bounds on every fixed-power `H` or `K` stratum, but `H=K=B^o(1)` is still permitted uniformly.  Therefore

```text
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false,
STRICT_SUB_SQRT_POWER_SAVING_PROVED=false,
SQRT_B_UPPER_BOUND_PROVED=true.                    (11.2)
```

---

## 12. H/tH decision

No mainline H theorem is needed at Stage14-4db.

The remaining receiver still has unused exact structure:

1. all four odd root-gcd cells are subpolynomial;
2. `C/J` is subpolynomial;
3. the post-column reciprocal fiber is divisor-many;
4. the two endpoint-linear signs are explicit sums/differences of a globally odd-primitive root pair.

Therefore the next step should first exploit the reduced two-sign determinant/resultant identities.  A generic genus-one or ray-character theorem is not the current mainline object.

The fixed-U `t80/tH23` coefficient space is not cross-promoted.

---

## Locked boundary

```text
STAGE14_4DB=COMPLETE_CROSS_ROOT_FIRST_LOST_CORE_ENUMERATION_AND_GLOBALLY_ODD_PRIMITIVE_SQRT_SATURATION
MERGED_X13_SQRT_IMPORTED=true
MERGED_4DA_IMPORTED=true
MERGED_S7_42_IMPORTED=true
CROSS_ROOT_FIRST_QUANTIFIER_ORDER_PROVED=true
FIXED_H_LOST_CORE_DIVISOR_MULTIPLICITY=Bo1
CROSS_ROOT_FIRST_COMPLETE_COUNT=1/2-kappa-s
FIXED_POWER_CROSS_ROOT_GCD_STRICTLY_SUBSQRT=true
FIXED_POWER_SAMESIDE_ROOT_GCD_STRICTLY_SUBSQRT=true
SQRT_SATURATION_CROSS_ROOT_GCD=Bo1
SQRT_SATURATION_SAMESIDE_ROOT_GCD=Bo1
SQRT_SATURATION_LOST_CORE=Bo1
SQRT_SATURATION_JOINT_CORE_EXPONENT=chi
SQRT_SATURATION_ALL_FOUR_ODD_ROOT_GCD_CELLS=Bo1
GLOBAL_ODD_FOUR_ROOT_PRIMITIVITY_AT_SQRT_SATURATION=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUB_SQRT_POWER_SAVING_PROVED=false
REMAINING_RECEIVER=SquareRootThetaQuarterGloballyOddPrimitiveFullJointCoreSingleColumnIncidence
MAINLINE_H_NEEDED=false
MAINLINE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_REOPENED=false
T80_CROSS_PROMOTED_TO_MAINLINE=false
TH23_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4dc
```
