# Stage14-X7 — self-generated four-root uncharging, Gaussian quotient, and cross-resultant energy

## Status

`COMPLETE_SELF_GENERATED_FOUR_ROOT_UNCHARGING_AND_GAUSSIAN_QUOTIENT_RESULTANT_REDUCTION`

Stage14-X7 consumes merged `X6`, merged `s7-29`, and merged mainline `4cp`.

The current unconditional whole-family bound is no longer `7/8`.  Merged `s7-29/4cp` prove

```text
V(B) << B^(3/4+o(1)),
```

and `4cp` localizes every block that can still saturate this bound to

```text
theta=5/16,
phi=1/4.
```

X6 supplies two real roots and two Gaussian/twisted roots for the reconstructed quadratic values of the primitive xi-agreement pair.  The purpose of X7 is to determine whether those roots can legally be charged as a second determinant-spacing modulus after the common-core root line has already been charged.

The answer is **no**.  More precisely:

1. the real-root part is exactly the prime factorization of the two already reconstructed linear values `aU-bV` and `aU+bV`;
2. after the fixed common-core Gaussian divisor is removed, the twisted-root part is exactly the prime factorization of the norm of one Gaussian quotient;
3. hence the generated real/twisted moduli are post-images of `(U,V)`, not fixed outer data;
4. for two primitive points, a generated prime transfers to the other point exactly when it divides one of two explicit cross resultants.

This closes the naive strategy

```text
common-core modulus C_0
x reconstructed four-root modulus
=> larger determinant-spacing modulus.
```

That multiplication reverses the charged-once quantifier and double-counts the same quadratic value.

No additional whole-family power saving is proved in X7.  The current exponent remains `3/4`.

---

## 1. Imported quarter-phi primitive root line

Fix the charged-once outer data used in `s7-29/4cp`: residual/common-core data, one full signed quotient decoration, endpoint-small roots, and one of the divisor-many common-core Gaussian root orientations.

Write

```text
U=L_x^+,
V=L_x^-,
gcd(U,V)=1,

D+A=aU,
D-A=bV,
```

with positive integral `a,b`.  Thus

```text
D=(aU+bV)/2,
A=(aU-bV)/2.                                  (1.1)
```

On the unique `3/4` saturation corner,

```text
theta=5/16,
phi=1/4,
UV=B^(1/2+o(1)).                               (1.2)
```

Let

```text
g=gcd(a,b),
a=g*a_0,
b=g*b_0,
gcd(a_0,b_0)=1.                              (1.3)
```

Merged `s7-29` proves

```text
oddpart(g) | r*s,
g=B^o(1),

C_bad=gcd(C,g^2),
C_0=C/C_bad=C*B^o(1)^(-1),                    (1.4)
```

and

```text
C_0 | a_0^2 U^2+b_0^2 V^2,
gcd(C_0,a_0*b_0*U*V)=1.                       (1.5)
```

Every odd prime divisor of `C_0` is `1 mod 4`.  After fixing one CRT orientation, the pair lies on one primitive root line

```text
U == rho*V (mod C_0).                          (1.6)
```

This is the only determinant-spacing modulus currently charged before `(U,V)` is counted.

---

## 2. The real two-root mask is exactly two linear values

X6 defines

```text
F_- := a^2 U^2-b^2 V^2.
```

Using (1.1), factor it before any primewise argument:

```text
F_-
 = (aU-bV)(aU+bV)
 = (2A)(2D)
 = 4*r*s*alpha*delta.                         (2.1)
```

Therefore the two real root branches are not a new quadratic incidence.  They are literally the two linear values

```text
boxed:
aU-bV = 2*r*alpha,

aU+bV = 2*s*delta.                            (2.2)
```

Since `alpha` and `delta` are coprime squarefree agreement cells, every good odd prime outside `2rsab` belongs to exactly one of these two factors:

```text
p|alpha  <=> aU-bV == 0 (mod p),

p|delta  <=> aU+bV == 0 (mod p).              (2.3)
```

Equivalently,

```text
U/V == +b/a (mod p)
```

or

```text
U/V == -b/a (mod p).
```

The common factor of the two linear forms is coefficient-supported.  Indeed

```text
gcd(aU-bV,aU+bV) | 2ab,                        (2.4)
```

because a common divisor divides both `2aU` and `2bV`, while `gcd(U,V)=1`.

Thus the moving real kernels are disjoint outside fixed coefficient support.

Most importantly, after `(U,V)` has been chosen, the real modulus is reconstructed by (2.2).  It is not fixed before `(U,V)`.

```text
REAL_FOUR_ROOT_MASK_REDUCES_TO_TWO_LINEAR_VALUES=true
REAL_GENERATED_MODULUS_IS_OUTER_DATA=false.       (2.5)
```

---

## 3. The common-core root orientation is one Gaussian divisor

Consider the primitive Gaussian host

```text
Z_0 := a_0 U + i*b_0 V in Z[i].                   (3.1)
```

Its norm is

```text
N(Z_0)=a_0^2 U^2+b_0^2 V^2.                      (3.2)
```

By (1.5), `C_0|N(Z_0)` and every prime `p|C_0` splits in `Z[i]`.

For each prime power

```text
p^e || C_0,
```

write

```text
p=pi_p*conj(pi_p),
N(pi_p)=p.
```

The fixed CRT root orientation in (1.6) chooses exactly one of `pi_p` and `conj(pi_p)`.  Because

```text
gcd(C_0,a_0*b_0*U*V)=1,
```

the chosen Gaussian prime power divides `Z_0` rather than both conjugate coordinates.

Multiplying the selected prime powers gives a Gaussian integer

```text
Pi_C := product_{p^e||C_0} pi_p^e               (3.3)
```

with

```text
boxed:
N(Pi_C)=C_0,
Pi_C | Z_0.                                      (3.4)
```

The ambiguity is only multiplication by a Gaussian unit and the already fixed finite root orientation.

Define the exact Gaussian quotient

```text
boxed:
W := Z_0/Pi_C in Z[i].                            (3.5)
```

Then

```text
boxed:
N(W)=(a_0^2U^2+b_0^2V^2)/C_0.                   (3.6)
```

No analytic theorem is used here; this is unique factorization in `Z[i]` plus the merged common-core root-line orientation.

```text
COMMON_CORE_ROOT_LINE_LIFTS_TO_GAUSSIAN_DIVISOR=true
COMMON_CORE_GAUSSIAN_QUOTIENT_DEFINED=true.       (3.7)
```

---

## 4. The twisted two-root mask is the norm factorization of the Gaussian quotient

X6 also defines

```text
F_+ := a^2U^2+b^2V^2 = 2H_k^+.                  (4.1)
```

Merged `4cg` gives

```text
oddpart(H_k^+) = C*oddpart(S*T).                  (4.2)
```

The only difference between `F_+` and `g^2 N(Z_0)` is the fixed 2-primary convention:

```text
F_+ = g^2 N(Z_0).                                (4.3)
```

After removing the common-core divisor `Pi_C`, equation (3.6) shows that the remaining Gaussian norm is precisely the post-common-core plus value, up to factors supported on the endpoint-small coefficient defect.

In particular, for every odd prime

```text
p not | 2*a*b*r*s*C,
```

we have the exact good-support equivalence

```text
boxed:
p | S*T
<=>
p | N(W).                                        (4.4)
```

Moreover `S*T` is squarefree, and because `p not|C`, (4.2) forces

```text
v_p(N(W))=1.                                      (4.5)
```

Every such prime is `1 mod 4`, and its two twisted roots are exactly the choice of one Gaussian prime above `p` dividing `W`:

```text
U/V == +/- i*b/a (mod p).                         (4.6)
```

Therefore the post-common-core twisted-root data are not a second external CRT modulus.  They are exactly the Gaussian prime factorization of the already reconstructed quotient `W`.

```text
TWISTED_FOUR_ROOT_MASK_REDUCES_TO_GAUSSIAN_QUOTIENT_NORM=true
XI_SWITCH_GOOD_SUPPORT_EQUALS_GAUSSIAN_QUOTIENT_NORM_SUPPORT=true
TWISTED_GENERATED_MODULUS_IS_OUTER_DATA=false.     (4.7)
```

---

## 5. Why multiplying `C_0` by the generated four-root modulus is illegal

The legal charged-once order is

```text
fixed residual/common-core data
-> fixed common-core root orientation Pi_C
-> count primitive (U,V) on U=rho V mod C_0
-> reconstruct alpha,delta from aU-bV,aU+bV
-> reconstruct W=(a_0U+i b_0V)/Pi_C
-> reconstruct S*T from N(W)
-> divisor/root/cell completion.                   (5.1)
```

The generated real and twisted moduli occur **after** `(U,V)` in this map.

Consequently a bound of the form

```text
#(U,V) << U_0V_0/(C_0 * alpha*delta * S*T)
```

or any variant obtained by multiplying the common-core spacing modulus by all reconstructed root moduli is a quantifier reversal.  It reuses values which are functions of the point being counted.

The only unconditional spacing already available is the merged primitive common-core bound

```text
#(U,V on one C_0 root line)
 << 1 + U_0V_0/C_0.                               (5.2)
```

X7 does not weaken that theorem.  It proves that the four-root labels cannot be appended to its modulus without a genuine cross-point distribution argument.

```text
SELF_GENERATED_REAL_MODULUS_RECHARGED=false
SELF_GENERATED_TWISTED_MODULUS_RECHARGED=false
SECOND_DETERMINANT_SPACING_FROM_POINTWISE_FOUR_ROOT_DATA=false. (5.3)
```

---

## 6. Exact two-point cross-resultant dictionary

The generated moduli can affect an **energy** only when prime information transfers from one primitive point to another.  X7 identifies exactly when that occurs.

Fix the same outer coefficient data `a,b,C_0,rho`, and take two primitive points

```text
(U_1,V_1),
(U_2,V_2)
```

on the same common-core root line.  Let

```text
F_-j=a^2 U_j^2-b^2 V_j^2,
F_+j=a^2 U_j^2+b^2 V_j^2.                         (6.1)
```

Define the two homogeneous cross resultants

```text
R_12
 := U_1^2 V_2^2-U_2^2 V_1^2
  = (U_1V_2-U_2V_1)(U_1V_2+U_2V_1),               (6.2)

K_12
 := U_1^2 V_2^2+U_2^2 V_1^2.                     (6.3)
```

Let `p` be an odd prime with

```text
p not | a*b*V_1*V_2.
```

Put

```text
t_j=U_j/V_j (mod p),
q=b/a (mod p).                                     (6.4)
```

Then

```text
p|F_-j <=> t_j^2=q^2,
p|F_+j <=> t_j^2=-q^2.                            (6.5)
```

Hence the following implications are exact.

### Same-role transfer

If `p|F_-1`, then

```text
boxed:
p|F_-2 <=> p|R_12.                                (6.6)
```

If `p|F_+1`, then

```text
boxed:
p|F_+2 <=> p|R_12.                                (6.7)
```

Indeed `R_12/(V_1V_2)^2=t_1^2-t_2^2`.

### Cross-role transfer

If `p|F_-1`, then

```text
boxed:
p|F_+2 <=> p|K_12.                                (6.8)
```

If `p|F_+1`, then

```text
boxed:
p|F_-2 <=> p|K_12.                                (6.9)
```

Indeed `K_12/(V_1V_2)^2=t_1^2+t_2^2`.

The finer root sign is encoded by the two linear factors of `R_12`: equal root orientation gives `U_1V_2-U_2V_1`, opposite orientation gives `U_1V_2+U_2V_1`.

Thus every good generated prime from point 1 falls into one of two classes relative to point 2:

```text
cross-shared:
  p | R_12*K_12,

cross-private:
  p not | R_12*K_12.                               (6.10)
```

For a cross-private prime, the root information of point 1 imposes no congruence on point 2.

```text
FOUR_ROOT_CROSS_RESULTANT_DICTIONARY_PROVED=true
PRIVATE_GENERATED_PRIME_FORCES_CROSS_SPACING=false. (6.11)
```

---

## 7. What the dictionary does and does not prove

The dictionary makes the remaining route precise.

If a generated prime is shared across two points, it divides an explicit cross resultant and can potentially be used in a genuine second-moment spacing argument.  If it is private, it cannot be promoted to a modulus for the other point.

However X7 does **not** prove that a fixed-power portion of the generated kernels must be cross-shared.  The reconstructed linear values and Gaussian quotient norms may, in principle, carry mostly private prime support or small shared support.

Accordingly none of the following is claimed:

```text
large shared generated modulus exists uniformly,
mutually private branch is sparse,
smooth generated values have fixed-power density loss,
3/4 is improved.
```

This is a genuine obstruction, not a missing algebraic simplification.

The current whole-family exponent therefore remains

```text
boxed:
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4.       (7.1)
```

and

```text
X7_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false. (7.2)
```

---

## 8. New minimal X-route receiver

The old X6 receiver

```text
TopThetaPrimitiveAgreementFourRootCRTQuadraticValueIncidence
```

and the merged 4cp receiver

```text
QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy
```

can now be sharpened to

```text
QuarterPhiCommonCoreLinearGaussianQuotientCrossResultantEnergy. (8.1)
```

Its data are:

```text
theta=5/16,
phi=1/4,
fixed charged-once residual/common-core data,
fixed full signed quotient decoration,
fixed common-core Gaussian divisor Pi_C,
primitive (U,V) on one C_0 root line,
real linear values aU-bV and aU+bV,
Gaussian quotient W=(a_0U+i b_0V)/Pi_C,
legal squarefree alpha/delta and S/T factorizations,
for energy pairs, exact resultants R_12 and K_12,
all original physical reconstruction/orientation masks.          (8.2)
```

This receiver retains exactly the structure not used by the `3/4` proof without double charging any self-generated modulus.

The next exact split should be:

```text
cross-shared resultant branch
vs
mutually cross-private generated-prime branch,                    (8.3)
```

with a separate smooth/small-prime subcase only if needed.

---

## 9. H decision

No X-specific auxiliary theorem is requested at X7.

The exact Gaussian quotient and cross-resultant dictionary should be exploited first.  A generic genus-one theorem is already known to be nonminimal, and a generic large sieve on the pointwise generated roots would again forget that their moduli are functions of the same primitive point.

If X8 leaves a genuine average obligation after separating cross-shared and mutually-private support, an auxiliary audit should target that precise energy object rather than a generic four-root CRT family.

```text
X7_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_WAITING_FOR_H=false.               (9.1)
```

---

## Stage boundary

```text
STAGE14_X7=COMPLETE_SELF_GENERATED_FOUR_ROOT_UNCHARGING_AND_GAUSSIAN_QUOTIENT_RESULTANT_REDUCTION
MERGED_X6_IMPORTED=true
MERGED_S7_29_IMPORTED=true
MERGED_4CP_IMPORTED=true
MERGED_THREE_QUARTER_BOUND_IMPORTED=true
THREE_QUARTER_SATURATION_REQUIRES_THETA=5/16
THREE_QUARTER_SATURATION_REQUIRES_PHI=1/4
REAL_FOUR_ROOT_MASK_REDUCES_TO_TWO_LINEAR_VALUES=true
REAL_GENERATED_MODULUS_IS_OUTER_DATA=false
COMMON_CORE_ROOT_LINE_LIFTS_TO_GAUSSIAN_DIVISOR=true
COMMON_CORE_GAUSSIAN_QUOTIENT_DEFINED=true
TWISTED_FOUR_ROOT_MASK_REDUCES_TO_GAUSSIAN_QUOTIENT_NORM=true
XI_SWITCH_GOOD_SUPPORT_EQUALS_GAUSSIAN_QUOTIENT_NORM_SUPPORT=true
TWISTED_GENERATED_MODULUS_IS_OUTER_DATA=false
SECOND_DETERMINANT_SPACING_FROM_POINTWISE_FOUR_ROOT_DATA=false
FOUR_ROOT_CROSS_RESULTANT_DICTIONARY_PROVED=true
PRIVATE_GENERATED_PRIME_FORCES_CROSS_SPACING=false
REMAINING_RECEIVER=QuarterPhiCommonCoreLinearGaussianQuotientCrossResultantEnergy
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4
X7_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
X7_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT_RECOMMENDED=Stage14-X8
```
