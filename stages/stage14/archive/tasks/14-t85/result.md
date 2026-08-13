# Stage14-t85 — selector/cofactor coprimality, modulus-square root lift, and exact square-quotient reduction

## Status

`COMPLETE_SELECTOR_DELTA_COPRIMALITY_MODULUS_SQUARE_ROOT_LIFT_AND_SQUARE_QUOTIENT_REDUCTION`

Stage14-t85 consumes merged Stage14-t84.  The Stage14-tH24 request emitted by t84 is treated under the immutable H-snapshot protocol: this stage does **not** edit, refine, or reopen `stages/stage14/14-t84/th24-target.md`.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.

The purpose of t85 is to expose the exact arithmetic content of the t84 vertical divisor condition.  Once the primitive switched norm is written as

```text
N=T^2+D^2=ell*k*delta,
D=d*j,
```

the selector divisor `d` and the short cofactor `delta` are automatically coprime, the norm acquires a square-root lift modulo `d^2`, and the residual condition is exactly that a normalized difference is a positive square.

---

## 1. Imported t84 packet

Fix

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
m=N(U)=R^2+S^2,
h*k=epsilon*m.
```

Merged t84 gives one primitive switched point

```text
N=T^2+D^2,
gcd(T,D)=1,
D=d*j,
```

with

```text
d | D_Ubeta | |R*S|,
# {d for fixed U}=B^o(1),
d odd and squarefree,
ell=LPF(N),
v_ell(N)=1,
ell^2>2N,
N=ell*k*delta,
```

and the retained physical masks include

```text
epsilon*ell*m*delta/2 <= B,
ell^2>4B,
ell*delta <= Y_U.
```

From the first two inequalities one recovers the sharp t65 separation

```text
ell>2*epsilon*m*delta.                              (1.1)
```

Also

```text
2*|R*S|<=m,
```

hence

```text
d<=m/2.                                            (1.2)
```

---

## 2. The whole vertical coordinate is coprime to the binary norm

Because

```text
gcd(T,D)=1,
N=T^2+D^2,
```

one has exactly

```text
gcd(D,N)
 = gcd(D,T^2)
 = 1.                                               (2.1)
```

Since

```text
D=d*j,
N=ell*k*delta,
```

this implies

```text
boxed:
gcd(d*j,ell*k*delta)=1.                            (2.2)
```

In particular

```text
gcd(d,delta)=1,
gcd(d,k)=1,
gcd(d,ell)=1,
gcd(j,delta)=1,
gcd(j,k)=1,
gcd(j,ell)=1.                                      (2.3)
```

Thus selector support and short norm-cofactor support are disjoint for a purely primitive reason; no separate squareclass argument is needed at this stage.

Moreover every odd prime divisor of `delta` divides the primitive sum-of-two-squares norm `N`, so merged t84 gives

```text
p|delta, p odd  => p==1 mod 4.                     (2.4)
```

```text
VERTICAL_COORDINATE_COPRIME_TO_BINARY_NORM=true
SELECTOR_DIVISOR_COPRIME_TO_DELTA=true
SELECTOR_DIVISOR_COPRIME_TO_K=true
DETERMINANT_QUOTIENT_COPRIME_TO_DELTA=true
ODD_DELTA_SUPPORT_ONLY_1_MOD_4=true
```

---

## 3. Exact square-root lift modulo d^2

Substitute `D=d*j` into the binary norm:

```text
ell*k*delta
 = T^2+d^2*j^2.                                    (3.1)
```

Hence

```text
boxed:
T^2 == ell*k*delta (mod d^2).                      (3.2)
```

By (2.2), both sides are units modulo `d`.  Since `d` is odd and squarefree, a unit modulo `d^2` is a square if and only if it is a quadratic residue modulo every prime `p|d`.  The physical point itself supplies one root, so

```text
(ell*k*delta / p)=+1 for every p|d.                (3.3)
```

For fixed `(ell,k,delta,d)`, whenever the condition is soluble, the number of roots modulo `d^2` is exactly

```text
boxed:
2^omega(d)=B^o(1).                                 (3.4)
```

Thus the vertical selector does not create a polynomial root-orientation family after the switch.

```text
BINARY_NORM_SQUARE_ROOT_LIFT_MOD_D2=true
ROOT_LIFT_UNIT_CONDITION=true
ROOT_CLASSES_MOD_D2=2^omega(d)
ROOT_CLASS_MULTIPLICITY=Bo1
```

---

## 4. Quadratic-character tensorization of the lifted selector

For a unit `a mod d`, with `d` odd squarefree,

```text
1_{a square mod d^2}
 = product_{p|d} (1+(a/p))/2
 = 2^(-omega(d)) * sum_{s|d} (a/s).                (4.1)
```

Apply this to

```text
a=ell*k*delta.
```

Then exactly

```text
boxed:
1_{ell*k*delta square mod d^2}
 = 2^(-omega(d))
   * sum_{s|d} (ell/s)*(k*delta/s).                 (4.2)
```

The selector congruence therefore tensorizes into a prime-side quadratic character and a short-cofactor-side quadratic character with only

```text
tau(d)=2^omega(d)=B^o(1)
```

terms.

This is only the congruence part of the physical condition.  Equation (4.2) must **not** be confused with the full equality `D=d*j`; a fixed-power saving does not follow merely from the index of the square subgroup.

```text
SELECTOR_ROOT_LIFT_QUADRATIC_CHARACTER_EXPANSION_PROVED=true
SELECTOR_ROOT_LIFT_CHARACTER_FAMILY_SIZE=Bo1
PRIME_COFACTOR_QUADRATIC_CHARACTER_TENSORIZATION_PROVED=true
ROOT_LIFT_ALONE_PROVES_FIXED_POWER_SAVING=false
```

---

## 5. The remaining vertical condition is exactly a square quotient

Equation (3.1) is equivalent to

```text
boxed:
J := (ell*k*delta-T^2)/d^2 = j^2 > 0.              (5.1)
```

together with the divisibility in (3.2).  Conversely, if the right-hand side of (5.1) is a positive integral square, then

```text
D=+/-d*sqrt(J)
```

recovers the two sign choices for the vertical coordinate; the fixed reciprocal/orientation convention reduces this to `O(1)` multiplicity.

Thus t85 separates the post-t84 receiver into

```text
quadratic-residue/root-lift condition mod d^2
+
positive square-quotient condition.                (5.2)
```

The first part has the exact `B^o(1)` character tensorization of Section 4.  The second part is the genuine remaining nonlinear arithmetic constraint.

```text
VERTICAL_DIVISOR_CONDITION_EQUIVALENT_TO_ROOT_LIFT_PLUS_SQUARE_QUOTIENT=true
SQUARE_QUOTIENT_VARIABLE=j^2
SQUARE_QUOTIENT_PHYSICAL_ENERGY_PROVED=false
```

---

## 6. New selector/cofactor hyperbolas

From (1.1) and `d<=m/2`,

```text
ell>4*epsilon*d*delta.                              (6.1)
```

The physical budget and super-square-root branch give

```text
epsilon*m*delta < sqrt(B).                         (6.2)
```

Therefore

```text
boxed:
2*epsilon*d*delta < sqrt(B),                        (6.3)
```

or

```text
d*delta < sqrt(B)/(2*epsilon).                     (6.4)
```

Consequently

```text
boxed:
min(d,delta)
 < B^(1/4)/sqrt(2*epsilon).                         (6.5)
```

This is independent of the earlier t83 dichotomy between `d` and `j`.

Combining (6.1) with the retained hyperbola

```text
ell*delta<=Y_U
```

gives the sharper mixed inequality

```text
boxed:
4*epsilon*d*delta^2 < Y_U.                         (6.6)
```

Hence also

```text
min(d,delta)
 < (Y_U/(4*epsilon))^(1/3).                         (6.7)
```

The hard packet therefore carries two simultaneous short-variable switches:

```text
min(d,|j|) <= (2B/h)^(1/4)     [t83],
min(d,delta) < B^(1/4)/sqrt(2epsilon) [t85],
4epsilon*d*delta^2<Y_U.                             (6.8)
```

```text
SELECTOR_DELTA_PRODUCT_HYPERBOLA_PROVED=true
SELECTOR_DELTA_PRODUCT_BOUND=sqrt(B)/(2epsilon)
SELECTOR_DELTA_QUARTER_DICHOTOMY_PROVED=true
SELECTOR_DELTA_SQUARED_HYPERBOLA_PROVED=true
SELECTOR_DELTA_SQUARED_BOUND=Y_U/(4epsilon)
```

---

## 7. Refined internal receiver

The live object after t85 is

```text
SharedUFixedSelectorPrimitiveBinaryNorm
CoprimeShortDeltaRootLiftSquareQuotient
SuperSqrtPrimeCofactorPhysicalEnergy.
```

Mandatory exact kernel:

```text
N=ell*k*delta=T^2+d^2*j^2,
gcd(T,d*j)=1,
gcd(d*j,ell*k*delta)=1,
d|D_Ubeta|R*S,
d odd squarefree,
#d=B^o(1),
ell=LPF(N),
v_ell(N)=1,
ell^2>2N,
T^2==ell*k*delta mod d^2,
(ell*k*delta-T^2)/d^2=j^2>0,
2epsilon*d*delta<sqrt(B),
4epsilon*d*delta^2<Y_U,
```

with all reconstructed-cover masks from t84 retained.

The square-root congruence may be expanded by (4.2), but the square-quotient condition and the reconstructed balanced-cover/hyperbola filters remain live.  No sieve theorem is claimed here.

```text
ROOT_LIFT_SQUARE_QUOTIENT_PHYSICAL_ENERGY_PROVED=false
```

---

## 8. tH24 / tH25 decision under H-PROTOCOL

The t84 auxiliary request remains

```text
Stage14-tH24:
FixedUPrimitiveBinaryNormSuperSqrtLargestPrimeShortCofactorVerticalDivisorSieve.
```

At the start of t85 no tH24 PR/branch was present.  Regardless of when tH24 is dispatched, this stage does not mutate its target:

```text
TH24_NEEDED=true
TH24_TARGET_REOPENED=false
TH24_REFINEMENT_REQUESTED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH24=false
```

The t85 root-lift/square-quotient decomposition is still internal algebra of the same t84 physical set.  It should be exploited once more before asking for a materially different external theorem audit.

```text
TH25_NEEDED=false
```

If a later stage converts the square-quotient receiver into a genuinely new standard theorem object, that later stage may dispatch `tH25`; the running/completed tH24 snapshot must remain unchanged.

---

## 9. Global ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T85_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t86
```

---

## Locked boundary

```text
STAGE14_T85=COMPLETE_SELECTOR_DELTA_COPRIMALITY_MODULUS_SQUARE_ROOT_LIFT_AND_SQUARE_QUOTIENT_REDUCTION
MERGED_T84_IMPORTED=true
VERTICAL_COORDINATE_COPRIME_TO_BINARY_NORM=true
SELECTOR_DIVISOR_COPRIME_TO_DELTA=true
SELECTOR_DIVISOR_COPRIME_TO_K=true
DETERMINANT_QUOTIENT_COPRIME_TO_DELTA=true
ODD_DELTA_SUPPORT_ONLY_1_MOD_4=true
BINARY_NORM_SQUARE_ROOT_LIFT_MOD_D2=true
ROOT_LIFT_UNIT_CONDITION=true
ROOT_CLASSES_MOD_D2=2^omega(d)
ROOT_CLASS_MULTIPLICITY=Bo1
SELECTOR_ROOT_LIFT_QUADRATIC_CHARACTER_EXPANSION_PROVED=true
SELECTOR_ROOT_LIFT_CHARACTER_FAMILY_SIZE=Bo1
PRIME_COFACTOR_QUADRATIC_CHARACTER_TENSORIZATION_PROVED=true
ROOT_LIFT_ALONE_PROVES_FIXED_POWER_SAVING=false
VERTICAL_DIVISOR_CONDITION_EQUIVALENT_TO_ROOT_LIFT_PLUS_SQUARE_QUOTIENT=true
SQUARE_QUOTIENT_PHYSICAL_ENERGY_PROVED=false
SELECTOR_DELTA_PRODUCT_HYPERBOLA_PROVED=true
SELECTOR_DELTA_PRODUCT_BOUND=sqrt(B)/(2epsilon)
SELECTOR_DELTA_QUARTER_DICHOTOMY_PROVED=true
SELECTOR_DELTA_SQUARED_HYPERBOLA_PROVED=true
SELECTOR_DELTA_SQUARED_BOUND=Y_U/(4epsilon)
ROOT_LIFT_SQUARE_QUOTIENT_PHYSICAL_ENERGY_PROVED=false
TH24_NEEDED=true
TH24_TARGET_REOPENED=false
TH24_REFINEMENT_REQUESTED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH24=false
TH25_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T85_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
PREFERRED_RECEIVER=SharedUFixedSelectorPrimitiveBinaryNormCoprimeShortDeltaRootLiftSquareQuotientSuperSqrtPrimeCofactorPhysicalEnergy
NEXT=Stage14-t86
```
