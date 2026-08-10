# Stage14-s7-30 — reciprocal common-core discriminant and short-cofactor reduction

## Status

`COMPLETE_RECIPROCAL_COMMON_CORE_DISCRIMINANT_DIVISIBILITY_AND_SHORT_COFACTOR_REDUCTION`

Stage14-s7-30 consumes merged `s7-29`, merged `4cp`, and the primitive reconstruction of merged `s7-28`.  The current unconditional whole-family bound is already

```text
V(B) << B^(3/4+o(1)),
```

and merged `4cp` proves that only

```text
theta=5/16,
phi=1/4
```

can saturate it.

The purpose of s7-30 is to use the **second** occurrence of the same common core `C`.  The result is not a second independent determinant modulus.  Instead, eliminating the two reciprocal quadratic equations shows that essentially all of `C` divides a reciprocal coefficient discriminant.  This produces a two-way factor allocation and a short cofactor which reconstructs the moving root product `X*Y`.

No new exponent below `3/4` is promoted in this stage because a fixed-`X*Y` common-core physical fiber theorem is still missing.

---

## 1. Quarter-phi primitive reciprocal packet

Retain the merged s7-28/s7-29 signed data

```text
U=L_x^+,
V=L_x^-,
M=L_k^+,
N=L_k^-,

gcd(U,V)=1,
gcd(M,N)=1,
```

and the signed quotient decoration

```text
a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-.
```

Write

```text
kappa = 4*r*s*epsilon_k,
lambda = 4*X*Y*epsilon_x.
```

The exact reciprocal equations are

```text
(aU)^2-(bV)^2 = kappa*M*N,                      (1.1)
(cM)^2-(dN)^2 = lambda*U*V.                     (1.2)
```

The same odd common core occurs in both plus hosts:

```text
C | (aU)^2+(bV)^2,                              (1.3)
C | (cM)^2+(dN)^2.                              (1.4)
```

Merged 4cg gives

```text
gcd(C,U*V)=1,
gcd(C,M*N)=1.                                   (1.5)
```

The first signed quotient pair also satisfies the s7-29 small-gcd lock

```text
gcd(a,b)=B^o(1),                                (1.6)
```

because its odd part divides `r*s=B^o(1)`.

---

## 2. Eliminate the two common-core root ratios without division

Put

```text
x=aU,
y=bV,
z=cM,
w=dN.
```

Multiplying (1.1)--(1.2) by the opposite coefficient products gives the exact integral equations

```text
c*d*(x^2-y^2) = kappa*z*w,                      (2.1)
a*b*(z^2-w^2) = lambda*x*y.                    (2.2)
```

Modulo `C`, (1.3)--(1.4) give

```text
x^2 == -y^2 (mod C),
z^2 == -w^2 (mod C).                            (2.3)
```

Square (2.1) modulo `C` and use (2.3):

```text
4*c^2*d^2*y^4 + kappa^2*w^4 == 0 (mod C).       (2.4)
```

Likewise (2.2) gives

```text
4*a^2*b^2*w^4 + lambda^2*y^4 == 0 (mod C).      (2.5)
```

Multiply (2.4) by `4*a^2*b^2` and substitute (2.5).  The `w^4` term disappears and one obtains the exact congruence

```text
[(4*a*b*c*d)^2-(kappa*lambda)^2] * y^4
 == 0 (mod C).                                   (2.6)
```

No inversion of `c,d,X,Y` was used.  This is important: the second common-core condition is being consumed in the actual physical quantifier order, not after assuming all moving coefficients are units.

---

## 3. The coefficient defect removed from `C` is only `B^o(1)`

Define

```text
C_bad = gcd(C,b^4),
C_Delta = C/C_bad.                               (3.1)
```

Because `gcd(C,V)=1`, cancellation of `y^4=b^4V^4` in (2.6) gives

```text
boxed:
C_Delta | Delta,                                 (3.2)

Delta := (4abcd)^2-(kappa*lambda)^2.
```

The apparent `b`-defect is harmless.  If an odd prime of `C` divides `b`, then (1.3), together with `gcd(C,U)=1`, forces the same prime into `a`.  Prime-power valuations give the quantitative bound

```text
C_bad <= gcd(a,b)^4.                              (3.3)
```

Hence by (1.6)

```text
boxed:
C/C_Delta = B^o(1),                               (3.4)
```

so essentially the full common core divides the reciprocal discriminant.

```text
RECIPROCAL_COMMON_CORE_DISCRIMINANT_DIVISIBILITY_PROVED=true
RECIPROCAL_DISCRIMINANT_BAD_CORE_MULTIPLICITY=Bo1
```

---

## 4. Two-way reciprocal-discriminant allocation

Factor

```text
Delta = E_- * E_+,

E_- = 4abcd-kappa*lambda,
E_+ = 4abcd+kappa*lambda.                         (4.1)
```

Merged X6, imported by merged 4cp, proves that the physical quarter-phi packet never reaches the singular equality

```text
kappa*lambda = 4abcd.
```

Therefore

```text
E_- != 0,
E_+ > 0                                           (4.2)
```

on every surviving packet.

Since `C_Delta | E_-E_+`, prime-power valuations may be allocated between the two factors.  Thus there exist positive integers

```text
C_- * C_+ = C_Delta,
C_- | |E_-|,
C_+ | E_+.                                       (4.3)
```

For fixed `C_Delta` the number of such labelled allocations is divisor-many, hence `B^o(1)`.  No coprimality of `E_-` and `E_+` is required.

At least one factor is dominant:

```text
boxed:
L := max(C_-,C_+) >= C_Delta^(1/2).              (4.4)
```

This is a genuine two-way allocation of the **outer common core**, not a re-charge of the self-generated agreement or switch moduli.

```text
RECIPROCAL_DISCRIMINANT_TWO_WAY_ALLOCATION_PROVED=true
RECIPROCAL_DISCRIMINANT_DOMINANT_CORE_SQRT_LOWER_BOUND=true
```

---

## 5. Quarter-phi size ledger and the short cofactor

On the unique `3/4` saturation corner,

```text
theta=5/16,
phi=1/4.
```

Merged s7-27/s7-29 give

```text
oddpart(a*b) = oddpart(u_res),
oddpart(c*d) = oddpart(v_res),

u_res <= B^(1/8+o(1)),
v_res <= B^(1/8+o(1)),                           (5.1)
```

with only subpolynomial 2-primary decoration.  Hence

```text
4abcd <= B^(1/4+o(1)).                            (5.2)
```

The endpoint-small factors satisfy `r,s=B^o(1)`, while

```text
X=x_1*x_2,
Y=y_1*y_2,

x_i,y_i <= B^(1/16+o(1)),
```

so

```text
kappa*lambda
 =16*r*s*X*Y*epsilon_x*epsilon_k
 <=B^(1/4+o(1)).                                  (5.3)
```

Consequently

```text
|E_-|, E_+ <= B^(1/4+o(1)).                      (5.4)
```

Write

```text
C = B^(c+o(1)).
```

By (3.4) and (4.4), the dominant allocated common-core factor satisfies

```text
L >= B^(c/2-o(1)).                                (5.5)
```

For the corresponding nonzero discriminant factor write

```text
|E_sigma| = L*h.                                  (5.6)
```

Then

```text
boxed:
h <= B^(1/4-c/2+o(1)).                           (5.7)
```

This is the new short cofactor.

```text
QUARTER_PHI_RECIPROCAL_DISCRIMINANT_COFACTOR_EXPONENT=1/4-c/2
```

---

## 6. The short cofactor reconstructs the moving root product `X*Y`

For the `E_+` branch,

```text
4abcd + kappa*lambda = L*h,
```

so

```text
kappa*lambda = L*h-4abcd.                        (6.1)
```

For the `E_-` branch, retain one sign bit

```text
eta = sign(E_-) in {+1,-1}.
```

Then

```text
4abcd-kappa*lambda = eta*L*h,
```

hence

```text
kappa*lambda = 4abcd-eta*L*h.                    (6.2)
```

All data on the right except `h` and a divisor-many allocation/branch label are already fixed in the outer residual/quotient packet.  Since

```text
kappa*lambda
 =16*r*s*epsilon_x*epsilon_k*X*Y,                (6.3)
```

(6.1)--(6.3) reconstruct `X*Y` exactly whenever the resulting value is positive and integral.

Thus

```text
boxed:
fixed outer packet + dominant discriminant allocation + short cofactor h
=> X*Y is uniquely reconstructed.                (6.4)
```

up to the already retained subpolynomial 2-primary decorations.

```text
RECIPROCAL_DISCRIMINANT_SHORT_COFACTOR_RECONSTRUCTS_XY=true
```

---

## 7. Why this does not yet lower `3/4`

Merged s7-29 gives, for fixed residual/quotient data at `phi=1/4`, the primitive root-line count

```text
#(U,V) <= B^(1/2-c+o(1)).                        (7.1)
```

The outer residual/common-core support is

```text
B^(c+1/4+o(1)).                                  (7.2)
```

which yields the current `3/4` total.

The new cofactor parameterization has support

```text
B^(1/4-c/2+o(1)).                                (7.3)
```

and fixes `X*Y`.  Let a future fixed-`X*Y` common-core physical-fiber estimate be

```text
B^(f(c)+o(1)).                                    (7.4)
```

Then the resulting whole block would have exponent

```text
(c+1/4) + (1/4-c/2) + f(c)
 = 1/2+c/2+f(c).                                  (7.5)
```

Therefore a uniform improvement below `3/4` follows exactly if one proves

```text
boxed:
f(c) < 1/4-c/2                                  (7.6)
```

by a fixed positive margin on the saturation family.

At the maximal common-core scale `c=3/8`, the threshold is `1/16`; at `c=0`, it is `1/4`.

No such fixed-`X*Y` fiber theorem is proved in s7-30.  In particular the completed generic fixed-lambda genus-one audit does not exploit the large common-core residue class and does not certify (7.6).

```text
FIXED_XY_COMMON_CORE_RECIPROCAL_FIBER_THRESHOLD=1/4-c/2
FIXED_XY_COMMON_CORE_RECIPROCAL_FIBER_THRESHOLD_PROVED=false
```

---

## 8. Quantifier guard

The two-way factorization (4.3) is derived from the **same outer `C`** already used by s7-29.  It may be used to reconstruct `X*Y`, but it may not be multiplied by the first Gaussian root-line modulus to claim a fictitious `C^(3/2)` or `C^2` determinant spacing.

Likewise the X6 real/twisted agreement and switch moduli are generated by the quadratic values of `(U,V)` and remain self-generated masks.

```text
SECOND_COMMON_CORE_CHARGED_AS_INDEPENDENT_DETERMINANT_MODULUS=false
COMMON_CORE_DOUBLE_CHARGE_FORBIDDEN=true
SELF_GENERATED_FOUR_ROOT_MODULI_RECHARGED=false
```

The legal new information is the discriminant divisibility and the short `X*Y` cofactor, not a second lattice determinant.

---

## 9. New minimal receiver

The `3/4` barrier is now refined from

```text
QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy
```

to

```text
QuarterPhiFixedXYCommonCoreReciprocalFiber.        (9.1)
```

The exact quantifier order is

```text
fixed (C,u_res,v_res)
+ divisor-many signed quotient / small decorations
+ divisor-many discriminant branch and C allocation
+ short h <= B^(1/4-c/2+o(1))
-> reconstruct X*Y
-> count primitive physical (U,V) lifts on the fixed common-core Gaussian root line
   with the original reciprocal equations, four-root masks, cell splits,
   orientation and reconstruction filters.                         (9.2)
```

The fixed-`X*Y` fiber, rather than a generic fixed-lambda Edwards curve, is the next object to attack.

---

## 10. H / tH decision

No new auxiliary theorem line is opened in s7-30.  The discriminant elimination above is exact arithmetic and materially changes the coefficient space once more.  Stage s7-31 should first test whether the fixed-`X*Y` fiber admits an elementary/p-adic reconstruction or determinant-spacing argument using the common-core residue class.

If that fails and a genuine rational-point/dispersion theorem remains, the precise future H target should be

```text
QuarterPhiFixedXYCommonCoreReciprocalFiber
```

with the common-core modulus and original reciprocal filters retained.  It should **not** revert to generic `PhysicalReciprocalEdwardsGenusOneAverageIncidence`.

The merged fixed-`U` t/tH18 line is a different coefficient space and is not cross-promoted; toolbox-aw also records the old tH18 request as superseded after t68.

```text
S7_30_AUXILIARY_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH18_CROSS_PROMOTED_TO_S7_30=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

---

## Stage boundary

```text
STAGE14_S7_30=COMPLETE_RECIPROCAL_COMMON_CORE_DISCRIMINANT_DIVISIBILITY_AND_SHORT_COFACTOR_REDUCTION
MERGED_S7_29_IMPORTED=true
MERGED_4CP_IMPORTED=true
MERGED_S7_28_PRIMITIVE_RECONSTRUCTION_IMPORTED=true
THREE_QUARTER_SATURATION_REQUIRES_THETA=5/16
THREE_QUARTER_SATURATION_REQUIRES_PHI=1/4
RECIPROCAL_COMMON_CORE_DISCRIMINANT_DIVISIBILITY_PROVED=true
RECIPROCAL_DISCRIMINANT_BAD_CORE_MULTIPLICITY=Bo1
RECIPROCAL_DISCRIMINANT_TWO_WAY_ALLOCATION_PROVED=true
RECIPROCAL_DISCRIMINANT_DOMINANT_CORE_SQRT_LOWER_BOUND=true
QUARTER_PHI_RECIPROCAL_DISCRIMINANT_COFACTOR_EXPONENT=1/4-c/2
RECIPROCAL_DISCRIMINANT_SHORT_COFACTOR_RECONSTRUCTS_XY=true
SECOND_COMMON_CORE_CHARGED_AS_INDEPENDENT_DETERMINANT_MODULUS=false
COMMON_CORE_DOUBLE_CHARGE_FORBIDDEN=true
FIXED_XY_COMMON_CORE_RECIPROCAL_FIBER_THRESHOLD=1/4-c/2
FIXED_XY_COMMON_CORE_RECIPROCAL_FIBER_THRESHOLD_PROVED=false
REMAINING_RECEIVER=QuarterPhiFixedXYCommonCoreReciprocalFiber
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4
NEW_S7_30_WHOLE_FAMILY_POWER_SAVING_PROVED=false
S7_30_AUXILIARY_H_NEEDED=false
GENERIC_GENUS_ONE_H_REOPENED=false
TH18_CROSS_PROMOTED_TO_S7_30=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
NEXT=Stage14-s7-31
```
