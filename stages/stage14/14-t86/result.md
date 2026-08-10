# Stage14-t86 — cofactor root-line quotient form, fixed discriminant, and fixed-cofactor prime-value reduction

## Status

`COMPLETE_COFACTOR_ROOT_LINE_TO_FIXED_DISCRIMINANT_FIXED_COFACTOR_PRIME_VALUE_FORM`

Stage14-t86 consumes merged Stage14-t85 and the merged immutable Stage14-tH24 snapshot verdict.  The completed tH24 audit remains a scoped Stage14-t84 certificate and is not edited, refined, or reopened.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.

The purpose of t86 is to remove the last apparent nonlinear `square quotient` from t85.  The short cofactor `delta` already divides the primitive switched norm.  Using its canonical root of `-1`, the equation

```text
T^2+d^2*j^2=ell*k*delta
```

becomes a primitive positive-definite binary quadratic form whose discriminant is exactly `-4d^2`, independent of the moving cofactor.  After the harmless 2-primary branch is absorbed into the fixed packet coefficient, the right-hand side is `ell*k0` with `k0` fixed.  Thus the moving cofactor has moved from the right-hand side into a form class of one fixed conductor.

---

## 1. Imported t85 packet and the completed tH24 verdict

Fix the physical packet

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
m=N(U),
```

and the fixed reciprocal/inversion orientation.  Merged t85 gives

```text
N=T^2+D^2=ell*k*delta,
gcd(T,D)=1,
D=d*j,
d|D_Ubeta|R*S,
d odd squarefree,
# {d for fixed U}=B^o(1),
```

with

```text
gcd(d*j,ell*k*delta)=1,
ell=LPF(N),
v_ell(N)=1,
ell^2>2N,
ell>2*k*delta,
ell*delta<=Y_U,
2*epsilon*d*delta<sqrt(B),
4*epsilon*d*delta^2<Y_U.
```

Merged tH24 proves only a negative applicability certificate for the t84 snapshot:

```text
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=false,
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=0,
NEXT_H_NEEDED=false
```

for the older primitive-binary-norm / vertical-divisor formulation.  Stage14-t86 consumes that verdict exactly once.

```text
TH24_CONSUMED=true
TH24_TARGET_REOPENED=false
TH24_REAUDIT_REQUESTED=false
```

---

## 2. Absorb the only possible 2-primary cofactor into the fixed packet

Because `(T,D)=1`, merged t84 proves

```text
v_2(T^2+D^2)<=1.
```

The canonical prime `ell` is odd, so

```text
v_2(k*delta)<=1.
```

Write

```text
eta = 2^v_2(delta) in {1,2},
delta = eta*delta0,
delta0 odd,
k0 = eta*k.
```

Then

```text
k0*delta0=k*delta,
N=ell*k0*delta0.                                  (2.1)
```

For each fixed packet there are only two possible `eta` branches, so the replacement `k -> k0` costs `O(1)`.

The t85 coprimality gives

```text
gcd(d*j,delta0)=1,
gcd(T,delta0)=1.                                   (2.2)
```

The second relation follows from

```text
gcd(T,N)=gcd(T,D^2)=1.
```

All odd prime divisors of `delta0` are `1 mod 4`.

```text
DELTA_TWO_PRIMARY_ABSORBED_INTO_FIXED_K=true
ETA_BRANCH_MULTIPLICITY=O1
DELTA0_ODD=true
GCD_T_DJ_DELTA0=1
```

---

## 3. The moving cofactor carries an exact root of -1

Reduce (2.1) modulo `delta0`:

```text
T^2+d^2*j^2 == 0 (mod delta0).                    (3.1)
```

Because `d*j` is a unit modulo `delta0`, define the physical root

```text
rho == T*(d*j)^(-1) (mod delta0).                  (3.2)
```

Then

```text
boxed:
rho^2 == -1 (mod delta0).                         (3.3)
```

For `delta0=1` take `rho=0`.  For `delta0>1`, each odd prime-power divisor is split, so the number of roots is exactly

```text
boxed:
# {rho mod delta0: rho^2==-1} = 2^omega(delta0)=B^o(1).  (3.4)
```

Thus a fixed cofactor has only subpolynomial local orientation entropy.

```text
DELTA_ROOT_OF_MINUS_ONE_PROVED=true
DELTA_ROOT_CLASS_MULTIPLICITY=2^omega(delta0)
DELTA_ROOT_CLASS_COST=Bo1
```

---

## 4. Exact quotient form

Choose the representative `0<=rho<delta0` and define

```text
s = (T-rho*d*j)/delta0,                            (4.1)
c = (rho^2+1)/delta0.                              (4.2)
```

Both are integers.  Hence

```text
T=rho*d*j+delta0*s.                                (4.3)
```

Expanding the switched norm gives

```text
T^2+d^2*j^2
 = delta0 * F_{d,delta0,rho}(s,j),                 (4.4)
```

where

```text
boxed:
F_{d,delta0,rho}(s,j)
 = delta0*s^2
   + 2*rho*d*s*j
   + c*d^2*j^2.                                    (4.5)
```

Combining with `N=ell*k0*delta0` yields

```text
boxed:
F_{d,delta0,rho}(s,j)=ell*k0.                      (4.6)
```

This is an exact equivalence, not an upper-bound relaxation.  Conversely, (4.3) and `D=d*j` reconstruct the switched pair `(T,D)`.

The t85 positive square quotient

```text
(ell*k*delta-T^2)/d^2=j^2
```

has therefore become an ordinary coordinate of a binary quadratic form.  It is no longer a separate nonlinear square condition.

```text
COFACTOR_ROOT_LINE_QUOTIENT_FORM_PROVED=true
SQUARE_QUOTIENT_NONLINEARITY_ELIMINATED=true
SWITCHED_POINT_RECONSTRUCTED_FROM_FORM_COORDINATES=true
```

---

## 5. The discriminant is fixed by the selector divisor alone

The coefficients of (4.5) are

```text
a=delta0,
b=2*rho*d,
c_form=c*d^2.
```

Its discriminant is exactly

```text
b^2-4*a*c_form
 = 4*rho^2*d^2 - 4*delta0*c*d^2
 = -4*d^2.                                         (5.1)
```

Hence

```text
boxed:
Disc(F)=-4*d^2.                                    (5.2)
```

The moving cofactor `delta0` changes only the representative/form class.  It does **not** change the discriminant or conductor.

The form is primitive.  Indeed

```text
gcd(delta0,2*rho*d)=1
```

because `delta0` is odd, `rho` is a unit modulo `delta0`, and `gcd(d,delta0)=1`.  Therefore the gcd of all three coefficients is one.

Since `a=delta0>0` and the discriminant is negative, the form is positive definite.

```text
FIXED_DISCRIMINANT_REDUCTION_PROVED=true
FORM_DISCRIMINANT=-4*d^2
MOVING_FORM_DISCRIMINANT_ELIMINATED=true
PRIMITIVE_POSITIVE_DEFINITE_FORM_PROVED=true
FIXED_U_SELECTOR_IS_FORM_CONDUCTOR=true
```

No claim is made that the number of proper form classes of discriminant `-4d^2` is `B^o(1)`.  That class-family issue remains analytic and must not be silently discarded.

---

## 6. Primitive transformed coordinates

Equation (4.3) and the t85 coprimality imply

```text
boxed:
gcd(s,d*j)=1.                                      (6.1)
```

Indeed any common divisor of `s` and `d*j` divides `T`, contradicting `gcd(T,d*j)=1`.

Thus the quotient-form point is primitive relative to the entire vertical coordinate.

```text
TRANSFORMED_COORDINATE_PRIMITIVITY_PROVED=true
GCD_S_DJ=1
```

This is stronger than merely asking for a primitive form: it is a physical-point condition that must be retained in any theorem adapter.

---

## 7. The form value has a fixed cofactor and one canonical prime

Equation (4.6) has fixed packet cofactor `k0`.  The original separation becomes

```text
ell>2*k*delta
   =2*k0*delta0.                                   (7.1)
```

Consequently

```text
ell>2*k0,
gcd(ell,k0)=1,
ell=LPF(F),
v_ell(F)=1,                                       (7.2)
```

and, more sharply,

```text
boxed:
ell^2 > 2*delta0*F.                               (7.3)
```

Thus the post-t86 arithmetic target is not a form with a moving short cofactor on the value side.  It is a primitive form of discriminant `-4d^2` taking a **fixed-cofactor prime value**:

```text
F(s,j)=k0*ell,
ell prime,
k0 fixed on the packet.                           (7.4)
```

```text
FIXED_COFACTOR_PRIME_VALUE_FORM_PROVED=true
FORM_VALUE_COFACTOR=k0
FORM_VALUE_CANONICAL_PRIME=ell
FORM_VALUE_LPF_EXPONENT_ONE=true
MOVING_DELTA_REMOVED_FROM_VALUE_SIDE=true
```

The canonical prime remains intrinsic to the form value; it must not be counted as a second independent choice if a prime-value theorem already counts `(s,j)`.

---

## 8. Gaussian ideal interpretation and fixed-k peel

Let

```text
z=T+iD=T+i*d*j.
```

The root condition `T==rho*D (mod delta0)` says

```text
z in I_{delta0,rho}:=(delta0,rho+i) subset Z[i].    (8.1)
```

The quotient `Z[i]/I_{delta0,rho}` has size `delta0`, so

```text
N(I_{delta0,rho})=delta0.                           (8.2)
```

Since `Z[i]` is a PID, choose a generator `gamma` with

```text
I_{delta0,rho}=(gamma),
N(gamma)=delta0.
```

Then

```text
boxed:
z=gamma*w,
N(w)=ell*k0.                                       (8.3)
```

The primitive condition `gcd(T,D)=1` implies that no rational prime divides the Gaussian integer `w`; otherwise that rational prime would divide both coordinates of `z`.

For each split prime-power in the fixed integer `k0`, primitiveness forces all Gaussian valuation onto one of the two conjugate primes.  Hence `w` has a Gaussian divisor `a` with

```text
N(a)=k0,
```

and after conditioning the divisor orientation,

```text
boxed:
w=a*pi',
N(pi')=ell,
pi' Gaussian prime.                                (8.4)
```

The number of possible fixed-norm factors is bounded by

```text
r_2(k0)<=4*tau(k0)=B^o(1).                         (8.5)
```

Therefore the exact factorization can also be written

```text
boxed:
T+iD = gamma * a * pi',
N(gamma)=delta0,
N(a)=k0,
N(pi')=ell.                                        (8.6)
```

This is a bijective/reconstruction reparameterization of the switched point up to Gaussian units and the already-fixed orientation.  It does not reopen the forbidden independent `pi x V` counting multiplicity from t84/tH24.

```text
DELTA_GAUSSIAN_IDEAL_EXTRACTION_PROVED=true
FIXED_K_GAUSSIAN_FACTOR_PEEL_PROVED=true
FIXED_K_GAUSSIAN_FACTOR_MULTIPLICITY=Bo1
GAUSSIAN_PRIME_SHORT_COFACTOR_FACTORIZATION_PROVED=true
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
```

---

## 9. Physical hyperbolas in the new variables

The original `delta=eta*delta0` inequalities become

```text
ell*eta*delta0 <= Y_U,                              (9.1)
2*epsilon*eta*d*delta0 < sqrt(B),                   (9.2)
4*epsilon*eta^2*d*delta0^2 < Y_U,                  (9.3)
ell>2*k0*delta0.                                   (9.4)
```

The t83 vertical quotient also remains

```text
D=d*j,
0<d*|j|<=sqrt(2B/h),
min(d,|j|)<=(2B/h)^(1/4).                          (9.5)
```

All reconstructed-cover masks from t84 remain filters after

```text
T=rho*d*j+delta0*s,
D=d*j,
```

followed by the canonical inverse reconstruction of the original cover.

```text
ELL_DELTA_HYPERBOLA_RETAINED=true
SELECTOR_DELTA_HYPERBOLAS_RETAINED=true
VERTICAL_QUARTER_SWITCH_RETAINED=true
RECONSTRUCTED_PHYSICAL_MASKS_RETAINED=true
```

---

## 10. What t86 has and has not closed

The following obstacles from tH24 are now strictly refined:

```text
moving cofactor on value side
    -> removed;

positive square quotient
    -> ordinary form coordinate;

moving form discriminant
    -> removed;

pi x full-cover multiplicity
    -> not reopened;

fixed packet k factor
    -> Gaussian-divisor-many, B^o(1).
```

The live analytic cost is now the distribution of prime values across a family of primitive form classes of one conductor `d`, with the moving leading coefficient/root pair `(delta0,rho)` and all physical masks retained.

No t86 theorem proves that this form-class family is power sparse, and no prime-value theorem is imported here.

```text
FIXED_DISCRIMINANT_PRIME_VALUE_PHYSICAL_ENERGY_PROVED=false
T86_FIXED_U_PACKET_POWER_SAVING_PROVED=false
```

---

## 11. New receiver and tH25 decision

The preferred receiver is

```text
SharedUFixedSelectorFixedDiscriminantPrimitive
FixedCofactorPrimeValueFormShortGaussianCofactorPhysicalEnergy.
```

This is materially different from the frozen tH24 object.  tH24 audited a moving-short-cofactor primitive norm with a vertical product-coordinate condition.  t86 has converted it to a fixed-discriminant form-class / ring-class prime-value problem with fixed value cofactor.

A new external audit is therefore justified:

```text
TH24_CONSUMED=true
TH24_TARGET_REOPENED=false
TH25_NEEDED=true
TH25_REQUESTED_OBJECT=FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve
TH25_DISPATCHED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH25=false
```

The immutable request is stored in

```text
stages/stage14/14-t86/th25-target.md
```

Once dispatched, tH25 audits this t86 snapshot only.  Stage14-t87+ may continue and must not refine a running tH25 request; a materially later receiver uses tH26.

---

## 12. Global ledger

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T86_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
NEXT=Stage14-t87
```

---

## Locked boundary

```text
STAGE14_T86=COMPLETE_COFACTOR_ROOT_LINE_TO_FIXED_DISCRIMINANT_FIXED_COFACTOR_PRIME_VALUE_FORM
MERGED_T85_IMPORTED=true
MERGED_TH24_SNAPSHOT_CONSUMED=true
TH24_CONSUMED=true
TH24_TARGET_REOPENED=false
DELTA_TWO_PRIMARY_ABSORBED_INTO_FIXED_K=true
ETA_BRANCH_MULTIPLICITY=O1
DELTA_ROOT_OF_MINUS_ONE_PROVED=true
DELTA_ROOT_CLASS_MULTIPLICITY=2^omega(delta0)
DELTA_ROOT_CLASS_COST=Bo1
COFACTOR_ROOT_LINE_QUOTIENT_FORM_PROVED=true
SQUARE_QUOTIENT_NONLINEARITY_ELIMINATED=true
FIXED_DISCRIMINANT_REDUCTION_PROVED=true
FORM_DISCRIMINANT=-4*d^2
MOVING_FORM_DISCRIMINANT_ELIMINATED=true
PRIMITIVE_POSITIVE_DEFINITE_FORM_PROVED=true
TRANSFORMED_COORDINATE_PRIMITIVITY_PROVED=true
FIXED_COFACTOR_PRIME_VALUE_FORM_PROVED=true
MOVING_DELTA_REMOVED_FROM_VALUE_SIDE=true
DELTA_GAUSSIAN_IDEAL_EXTRACTION_PROVED=true
FIXED_K_GAUSSIAN_FACTOR_PEEL_PROVED=true
FIXED_K_GAUSSIAN_FACTOR_MULTIPLICITY=Bo1
GAUSSIAN_PRIME_SHORT_COFACTOR_FACTORIZATION_PROVED=true
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
ELL_DELTA_HYPERBOLA_RETAINED=true
SELECTOR_DELTA_HYPERBOLAS_RETAINED=true
VERTICAL_QUARTER_SWITCH_RETAINED=true
RECONSTRUCTED_PHYSICAL_MASKS_RETAINED=true
FIXED_DISCRIMINANT_PRIME_VALUE_PHYSICAL_ENERGY_PROVED=false
T86_FIXED_U_PACKET_POWER_SAVING_PROVED=false
TH25_NEEDED=true
TH25_REQUESTED_OBJECT=FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve
TH25_DISPATCHED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH25=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T86_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
PREFERRED_RECEIVER=SharedUFixedSelectorFixedDiscriminantPrimitiveFixedCofactorPrimeValueFormShortGaussianCofactorPhysicalEnergy
NEXT=Stage14-t87
```