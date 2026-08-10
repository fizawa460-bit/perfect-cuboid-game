# Stage14-tH25 target — fixed-discriminant fixed-cofactor prime-value form with physical masks

## Snapshot protocol

This target is prepared by Stage14-t86 under `stages/stage14/H-PROTOCOL.md`.

```text
H_STAGE=Stage14-tH25
SOURCE_STAGE=Stage14-t86
TARGET_FILE=stages/stage14/14-t86/th25-target.md
TARGET_FREEZES_AT_DISPATCH=true
RUNNING_TH25_MAY_CHASE_T87_PLUS=false
TH25_DISPATCHED_BY_T86=false
```

When tH25 is dispatched, audit the merged t86 snapshot only.  Later t87+ reductions do not modify this request.  A materially different later receiver uses tH26.

## Requested object

```text
FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve
```

## Exact input from t86

Fix a physical packet

```text
(U,epsilon,k,h,kappa,beta),
U=R+iS,
```

and the reciprocal/inversion orientation.  Fix one of the `O(1)` 2-primary branches

```text
eta in {1,2},
delta=eta*delta0,
delta0 odd,
k0=eta*k.
```

The fixed-U selector divisor satisfies

```text
d|D_Ubeta|R*S,
d odd squarefree,
# {d for fixed U}=B^o(1),
gcd(d,k0*delta0)=1.
```

For each physical point there is a root

```text
rho^2 == -1 (mod delta0),
#rho=2^omega(delta0)=B^o(1),
```

and transformed coordinates `(s,j)` with

```text
T=rho*d*j+delta0*s,
D=d*j,
gcd(s,d*j)=1.
```

Define

```text
c=(rho^2+1)/delta0
```

and the primitive positive-definite binary quadratic form

```text
F_{d,delta0,rho}(s,j)
 = delta0*s^2
   + 2*rho*d*s*j
   + c*d^2*j^2.
```

Then exactly

```text
Disc(F)=-4*d^2,
F(s,j)=k0*ell,
ell prime,
ell=LPF(F),
v_ell(F)=1,
ell>2*k0*delta0,
ell^2>2*delta0*F.
```

The key structural change relative to tH24 is:

```text
moving delta on the VALUE side = eliminated,
form discriminant moving with delta = eliminated,
value cofactor = fixed k0,
form-class/leading-coefficient pair (delta0,rho) = still moving,
selector conductor d = fixed after the B^o(1) fixed-U divisor choice.
```

Do not revert to the tH24 moving-short-cofactor norm receiver.

## Equivalent Gaussian ideal factorization

Let

```text
z=T+iD.
```

The root condition gives the Gaussian ideal

```text
I_{delta0,rho}=(delta0,rho+i),
N(I)=delta0,
z in I.
```

Since `Z[i]` is principal, choose `gamma` with

```text
I=(gamma),
N(gamma)=delta0.
```

Then

```text
z=gamma*w,
N(w)=k0*ell.
```

After conditioning one fixed-norm Gaussian divisor `a` of norm `k0`, at only

```text
r_2(k0)<=4*tau(k0)=B^o(1)
```

cost,

```text
w=a*pi',
N(pi')=ell,
pi' Gaussian prime,
```

hence

```text
T+iD=gamma*a*pi'.
```

This is a reparameterization of one switched point.  It does not reopen an independent `pi x V` multiplicity.

## Mandatory physical ranges and masks

Retain all of the following, directly or as coefficient/mask restrictions with only certified `B^o(1)` loss:

```text
fixed U,epsilon,k,h,kappa,beta,
fixed reciprocal/inversion orientation,
eta in {1,2},
k0=eta*k,
d|D_Ubeta|R*S,
#d=B^o(1),
d odd squarefree,
delta0 odd,
rho^2=-1 mod delta0,
#rho=B^o(1),
gcd(s,d*j)=1,
F(s,j)=k0*ell,
ell prime,
ell>2*k0*delta0,
ell=LPF(F),
v_ell(F)=1,
Disc(F)=-4d^2,
ell*eta*delta0<=Y_U,
2*epsilon*eta*d*delta0<sqrt(B),
4*epsilon*eta^2*d*delta0^2<Y_U,
0<d*|j|<=sqrt(2B/h),
min(d,|j|)<=(2B/h)^(1/4),
canonical Gaussian direction convention,
reconstructed primitive balanced cover,
small angular-g four-cell weights,
short ellipse,
sharp ell*odd(h)*odd(r)*odd(t) hyperbola,
fixed beta-tag rules.
```

The t78 four-cell Möbius tensorization and tH23 coefficient `L2` bookkeeping remain available at `B^o(1)` loss.

## Closed branches — do not reopen

```text
TH24_TARGET_REOPENED=false
MOVING_SHORT_COFACTOR_ON_FORM_VALUE_REOPENED=false
MOVING_FORM_DISCRIMINANT_REOPENED=false
POSITIVE_SQUARE_QUOTIENT_REOPENED=false
CANONICAL_PRIME_INDEPENDENT_CHOICE_REOPENED=false
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
MOVING_MODULUS_FAMILY_REOPENED=false
TWO_FREQUENCY_LENGTH_REOPENED=false
HECKE_CONDUCTOR_D2_REOPENED=false
```

Do not charge a separate sum over `ell` if the invoked prime-value theorem already counts form points with `F/k0` prime.

## Main analytic questions

Audit whether the t86 receiver is now covered, directly or after one standard adapter, by any of the following kinds of results.

1. Primes represented by primitive positive-definite binary quadratic forms with **growing discriminant** `-4d^2`, uniformly in the conductor `d`.
2. Prime ideals in ring classes / ring class characters of the order of conductor `d` in `Q(i)`.
3. Uniform PNT / Bombieri--Vinogradov / Barban--Davenport--Halberstam for ring-class or Hecke characters as `d` grows through the physical range.
4. Prime values of a family of equivalent/proper form classes of one fixed discriminant, with the class indexed by `(delta0,rho)`.
5. Whether the fixed value factor `k0` can be peeled by ideal composition at `B^o(1)` cost uniformly in `d`, leaving a genuine prime-representation theorem.
6. Gaussian prime distribution for

   ```text
   gamma*a*pi'
   ```

   with `N(gamma)=delta0`, `N(a)=k0`, and `d|Im(gamma*a*pi')`, without reintroducing an independent full-cover variable.
7. Bilinear/dispersion estimates for a short Gaussian cofactor `gamma` against a Gaussian prime, in the simultaneous ranges

   ```text
   ell*eta*delta0<=Y_U,
   d*delta0^2 << Y_U,
   d*delta0 << sqrt(B).
   ```

8. Spectral / class-group large sieve for ring-class characters if the moving form-class family can be diagonalized without polynomial class-number loss.
9. Fouvry--Iwaniec / Iwaniec-type prime-value results or modern uniform variants, but only if the variable dictionary and growing-discriminant uniformity are explicit.
10. Any fixed-conductor determinant/geometry-of-numbers estimate that proves power sparsity of the physical subfamily before invoking prime distribution.

## Class-family issue that must be audited explicitly

The statement

```text
Disc(F)=-4d^2
```

does **not** imply that the number of relevant proper form classes is `B^o(1)`.  The t86 proof intentionally leaves this open.

Any applicability claim must account for the family indexed by

```text
(delta0,rho),
rho^2=-1 mod delta0,
```

inside the order of conductor `d`.

Determine whether these physical forms occupy:

```text
one class,
a B^o(1) subfamily,
a genus,
a ray/ring-class character coset,
or a genuinely polynomial-size class family.
```

Do not assume the strongest outcome without proof.

## Range ledger required for APPLICABLE=true

At minimum identify explicitly:

```text
d range and conductor norm,
delta0 range,
rho multiplicity,
form coefficient sizes,
proper-equivalence/reduction cost,
class number / genus number cost,
(s,j) region after physical reconstruction,
prime ell range,
fixed cofactor k0 dependence,
level of distribution,
exceptional character / Siegel-zero dependence,
angular/sector restrictions,
coefficient L2 norm,
vertical coordinate range,
physical hyperbola localization cost,
quantifier order.
```

A logarithmic prime-density gain is not a certified fixed `B`-power saving.

## Questions to answer

A. Does the fixed discriminant `-4d^2` and fixed value cofactor `k0` make an off-the-shelf prime-representation theorem directly applicable with all physical masks retained?

B. If not, can one standard ideal-composition / ring-class-character step produce a theorem-ready family with a uniform fixed-power gain?

C. For a fixed U packet, can one certify

```text
packet contribution
 <= B^(-delta0_save) * current packet trivial scale
```

for an explicit `delta0_save>0`?

D. If C holds, is there a legal summation bridge over U and the fixed packet data that cross-promotes it to the whole-family square-root ledger?

Do not update the global exponent unless D is proved.

## Required boundary

Emit at minimum

```text
STAGE14_TH25=COMPLETE_...
AUDITED_THROUGH=Stage14-t86
TARGET_FROZEN=true
T86_FIXED_DISCRIMINANT_RETAINED=true
T86_FORM_DISCRIMINANT=-4*d^2
T86_FIXED_VALUE_COFACTOR_RETAINED=true
T86_MOVING_DELTA_VALUE_SIDE_ELIMINATED=true
T86_FORM_CLASS_FAMILY_RETAINED=true
T86_GAUSSIAN_IDEAL_FACTORIZATION_RETAINED=true
T86_FIXED_K_PEEL_RETAINED=true
BILINEAR_PI_V_MULTIPLICITY_REOPENED=false
FULL_PHYSICAL_MASKS_RETAINED=...
RING_CLASS_PRIME_THEOREM_APPLICABLE=...
GROWING_DISCRIMINANT_FORM_PRIME_THEOREM_APPLICABLE=...
RING_CLASS_LARGE_SIEVE_APPLICABLE=...
GAUSSIAN_SHORT_COFACTOR_PRIME_BILINEAR_APPLICABLE=...
FIXED_K_IDEAL_COMPOSITION_ADAPTER_PROVED=...
FORM_CLASS_FAMILY_POWER_COST_CONTROLLED=...
OFF_THE_SHELF_FIXED_POWER_SAVING_PROVED=...
CERTIFIED_FIXED_U_PACKET_B_POWER_SAVING_EXPONENT=...
FIXED_U_SAVING_LEGALLY_CROSS_PROMOTES_TO_WHOLE_FAMILY=...
STRICT_SUBSQRT_POWER_SAVING_PROVED=...
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
NEXT_H_NEEDED=...
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=[latest main context only]
```

If the verdict is negative, isolate one exact obstruction that t87+ can attack internally.  The negative result should still merge as the scoped t86 snapshot certificate.

## GitHub deliverables

Record Stage14-tH25 under

```text
stages/stage14/14-tH25/
```

with at least

```text
result.md
literature/applicability note
deterministic range/form-class audit
frozen boundary
dedicated CI workflow
```

Create branch, commits, Draft PR, run dedicated CI, and mark Ready when internally consistent.  Once dispatched, do not update the mathematical target merely because t87+ advances.