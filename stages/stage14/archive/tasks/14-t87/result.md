# Stage14-t87 — projective/ring-class bridge and fixed-power conductor endpoint collapse

## Status

`COMPLETE_PROJECTIVE_RING_CLASS_BRIDGE_AND_FIXED_POWER_CONDUCTOR_ENDPOINT_COLLAPSE`

Stage14-t87 consumes merged Stage14-t86.  The Stage14-tH25 request emitted by t86 remains an immutable t86 snapshot under `stages/stage14/H-PROTOCOL.md`; t87 does not edit or refine `stages/stage14/14-t86/th25-target.md`.

The current whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No whole-family exponent is changed here.

The purpose of t87 is to identify the fixed-discriminant form class from t86 with the same finite projective Gaussian geometry that already appeared earlier in the t-route, and then use elementary lattice geometry before invoking any prime-value theorem.  The resulting conclusion is strong: every fixed-power-large selector conductor `d` already has a fixed-power saving without using primality.  Thus a t-route sequence capable of saturating the local trivial exponent must have

```text
d=B^o(1).
```

The surviving ring-class/projective conductor is endpoint-small.

---

## 1. Imported t86 factorization

Fix the physical packet

```text
(U,epsilon,k,h,kappa,beta),
```

together with its reciprocal/inversion orientation and a selector divisor

```text
d | D_Ubeta | |R*S|,
d odd and squarefree,
# {d for fixed U}=B^o(1).
```

Merged t86 gives

```text
delta=eta*delta0,
eta in {1,2},
k0=eta*k,
```

and the exact Gaussian factorization

```text
z:=T+iD=gamma*a*pi',
D=d*j,
N(gamma)=delta0,
N(a)=k0,
N(pi')=ell,
```

where `pi'` is a Gaussian prime above the canonical rational prime `ell`.  The fixed-`k0` factor `a` has only `B^o(1)` choices.

The inherited primitive/coprimality relations include

```text
gcd(d,ell*k0*delta0)=1,
gcd(T,d)=1,
```

and the super-square-root physical branch gives

```text
ell^2>4B.                                           (1.1)
```

The moving cofactor is still constrained by

```text
ell*eta*delta0<=Y_U,
2*epsilon*eta*d*delta0<sqrt(B),
4*epsilon*eta^2*d*delta0^2<Y_U.                    (1.2)
```

All reconstructed-cover masks from t84--t86 remain filters.

---

## 2. Exact projective Gaussian group at the selector conductor

For odd squarefree `d`, define

```text
G(d):=(Z[i]/d Z[i])^x / (Z/d Z)^x.                 (2.1)
```

Because each factor of `z=gamma*a*pi'` has norm coprime to `d`, each determines a class in `G(d)`.

Since

```text
D=Im(z)=d*j,
```

we have

```text
z == T (mod d).
```

The relation `gcd(T,d)=1` makes this a nonzero rational scalar modulo every `p|d`.  Therefore the projective class of `z` is the identity:

```text
boxed:
[gamma]*[a]*[pi'] = 1 in G(d).                     (2.2)
```

Equivalently,

```text
boxed:
[pi']=[gamma*a]^(-1).                              (2.3)
```

This is exact.  No form-class averaging, prime theorem, or character estimate is used.

```text
PROJECTIVE_GAUSSIAN_SELECTOR_GROUP_REENTERED=true
EXACT_GAMMA_A_PRIME_PROJECTIVE_INCIDENCE=true
PROJECTIVE_INCIDENCE=[gamma]*[a]*[pi']=1
```

---

## 3. Local size and the ring-class bridge

For a prime `p|d`,

```text
|G(p)| = p-chi_4(p),
```

because

```text
p==1 mod 4:  Z[i]/p ~= F_p x F_p,  |G(p)|=p-1,
p==3 mod 4:  Z[i]/p ~= F_{p^2},     |G(p)|=p+1.
```

CRT therefore gives

```text
boxed:
|G(d)|=product_{p|d}(p-chi_4(p))=d*B^o(1).         (3.1)
```

Let

```text
O_d=Z+d*i*Z,
Disc(O_d)=-4*d^2.
```

Since `Z[i]` has class number one, the standard ring-class exact sequence identifies, for odd `d>1`,

```text
boxed:
Pic(O_d) ~= G(d)/<[i]>.                            (3.2)
```

The projective class `[i]` has order two, hence

```text
boxed:
h(-4*d^2)=|G(d)|/2
              =(d/2)*product_{p|d}(1-chi_4(p)/p). (3.3)
```

For `d=1`, `h(-4)=1` separately.

Thus the t86 fixed-discriminant quadratic-form classes are not a new unrelated entropy source: they are the ring-class quotient of the same projective Gaussian group in which (2.2) lives.

```text
T86_FORM_DISCRIMINANT_RING_CLASS_IDENTIFIED=true
RING_CLASS_IS_PROJECTIVE_GROUP_MOD_I=true
RING_CLASS_NUMBER_SCALE=d*Bo1
```

The factor two from `[i]` is an orientation/unit issue only and has zero fixed-power cost.

---

## 4. Exact character orthogonality, without charging it yet

Equation (2.2) admits the exact finite expansion

```text
1_{[gamma][a][pi']=1}
 = 1/|G(d)| * sum_{chi in G(d)^}
     chi(gamma)*chi(a)*chi(pi').                   (4.1)
```

The principal term carries the expected projective density

```text
1/|G(d)|=d^(-1)*B^o(1).                            (4.2)
```

However t87 does **not** infer a full power saving from the principal term alone; nonprincipal terms cannot be discarded without a theorem.  Instead, t87 obtains the needed large-`d` saving geometrically, class by class.

```text
PROJECTIVE_CHARACTER_ORTHOGONALITY_EXACT=true
PRINCIPAL_PROJECTIVE_DENSITY=d^-1*Bo1
NONPRINCIPAL_TERMS_DISCARDED=false
```

---

## 5. A projective class is one determinant-d lattice

Fix a class `C in G(d)` and choose a representative

```text
u+iv mod d
```

whose norm is a unit modulo `d`.  An integer Gaussian number

```text
x+i*y
```

has projective class `C` only if

```text
v*x-u*y == 0 (mod d).                              (5.1)
```

Because `(u,v)` is primitive modulo every prime divisor of `d`, the solution set of (5.1) is a rank-two lattice of index exactly `d` in `Z^2`.

Consequently, for any Euclidean annulus

```text
L <= x^2+y^2 < 2L,
```

standard lattice-point geometry gives uniformly in the class

```text
boxed:
# {(x,y): [x+i*y]=C, L<=x^2+y^2<2L}
 << L/d + sqrt(L) + 1.                             (5.2)
```

The same bound remains valid after imposing primality, canonical orientation, angular restrictions, or any other physical filter, because those only remove points.

```text
PROJECTIVE_CLASS_IS_INDEX_D_LATTICE=true
PROJECTIVE_ANNULUS_LATTICE_BOUND=L/d+sqrt(L)+1
PRIMALITY_NOT_USED_FOR_LARGE_D_SAVING=true
```

---

## 6. Apply the lattice bound to the canonical Gaussian prime

Fix `gamma`, a fixed-`k0` Gaussian factor `a`, and a dyadic canonical-prime norm range

```text
ell ~ L.
```

Equation (2.3) forces `pi'` into the single projective class

```text
[pi']=[gamma*a]^(-1).
```

Therefore, even after dropping the condition that `pi'` is prime,

```text
boxed:
# {pi' in this dyadic range compatible with gamma,a,d}
 << L/d + sqrt(L) + 1.                             (6.1)
```

The unrestricted two-dimensional lattice support in the same annulus is `O(L)`.  Thus the projective condition gives the fixed-power ratio

```text
boxed:
B^o(1)*(d^(-1)+L^(-1/2)).                          (6.2)
```

The physical branch (1.1) gives

```text
L >= ell > 2*sqrt(B),
```

up to the harmless dyadic convention, and hence

```text
L^(-1/2) <= B^(-1/4+o(1)).                         (6.3)
```

If

```text
d >= B^theta
```

for any fixed `theta>0`, (6.2) yields

```text
boxed:
saving >= B^(-min(theta,1/4)+o(1)).                (6.4)
```

This is an unconditional lattice saving on the fixed t86 packet.  It does not use a Gaussian prime theorem and therefore retains all physical masks as filters.

```text
FIXED_POWER_D_PROJECTIVE_LATTICE_SAVING_PROVED=true
FIXED_POWER_D_SAVING_EXPONENT=min(theta,1/4)
SUPER_SQRT_PRIME_BRANCH_USED_FOR_UNIFORM_QUARTER_ERROR=true
FULL_PHYSICAL_MASKS_MAY_BE_RETAINED_AS_FILTERS=true
```

---

## 7. The only unsaved conductor scale is endpoint-small

Since every fixed-power `d` is saved by (6.4), a sequence that can remain at the local trivial fixed-power exponent must satisfy

```text
boxed:
d=B^o(1).                                          (7.1)
```

On this survivor,

```text
|G(d)|=B^o(1),
h(-4*d^2)=B^o(1),
Disc(F)=-4*d^2=B^o(1).                              (7.2)
```

Thus the polynomial ring-class/form-class entropy suggested by the raw t86 fixed-discriminant formulation disappears on the only unsaved conductor branch.

This does **not** imply that the moving cofactor `delta0` is `B^o(1)`.  Many cofactor values may lie in the same endpoint-small projective/ring class.  That remaining cofactor/prime interaction must not be dropped.

```text
HARD_SELECTOR_CONDUCTOR_ENDPOINT=d=Bo1
HARD_PROJECTIVE_GROUP_SIZE=Bo1
HARD_RING_CLASS_NUMBER=Bo1
MOVING_DELTA0_ENDPOINT_NOT_PROVED=true
```

---

## 8. Optional cofactor-side symmetric bound

For completeness, fix `pi'` and `a`, and let

```text
N(gamma)=delta0 ~ X.
```

The same projective incidence forces `gamma` onto one index-`d` projective lattice, so

```text
# gamma << X/d + sqrt(X) + 1.                      (8.1)
```

Relative to the unrestricted `O(X)` Gaussian support this gives

```text
d^(-1)+X^(-1/2).                                  (8.2)
```

Thus every stratum on which both `d` and `delta0` are fixed-power large has a fixed-power saving from either side.  The prime-side estimate of Section 6 is stronger for the present purpose because the super-square-root condition supplies a uniform lower bound for `L` and therefore closes **all** fixed-power `d`, even when `delta0` is endpoint-small.

```text
COFACTOR_PROJECTIVE_LATTICE_BOUND=X/d+sqrt(X)+1
PRIME_SIDE_BOUND_DOMINATES_CONDUCTOR_ENDPOINT_COLLAPSE=true
```

---

## 9. Relation to tH25

Stage14-tH25, if/when dispatched, audits the immutable t86 object

```text
FixedUFixedDiscriminantMinus4dSquaredFixedCofactorPrimeValueFormPhysicalSieve.
```

Stage14-t87 does not alter that request.  Its new large-`d` lattice argument is downstream internal work.

```text
TH25_NEEDED=true
TH25_TARGET_REOPENED=false
TH25_REFINEMENT_REQUESTED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH25=false
TH26_NEEDED=false
```

If tH25 is already running, it continues on the t86 snapshot unchanged.  If it has not yet been dispatched, the stored t86 request remains the request to use.  No tH26 object is justified yet because the endpoint-small conductor receiver still has deterministic structure to exploit.

---

## 10. New receiver

After removing fixed-power conductor strata, the live object is

```text
SharedUEndpointSmallSelectorProjectiveRingClass
ShortGaussianCofactorCanonicalPrimePhysicalIncidenceEnergy.
```

Mandatory kernel:

```text
d=B^o(1),
G(d)=B^o(1),
h(-4*d^2)=B^o(1),
[gamma]*[a]*[pi']=1 in G(d),
N(gamma)=delta0,
N(a)=k0 fixed,
N(pi')=ell prime,
ell^2>4B,
ell>2*k0*delta0,
ell*eta*delta0<=Y_U,
2*epsilon*eta*d*delta0<sqrt(B),
4*epsilon*eta^2*d*delta0^2<Y_U,
```

with the original reconstructed-cover masks retained.

The next deterministic question is no longer a large-conductor prime-value-form problem.  It is whether endpoint-small `d` lets the finite projective class be absorbed completely so that the remaining `(delta0,ell)` relation becomes a one-dimensional norm/product or short-interval incidence.

---

## 11. Whole-family ledger

The lattice saving is proved on fixed t-route packets and on fixed-power conductor strata, but no legal summation over all fixed-`U` packets is established here.  Therefore it is not cross-promoted to the global theorem.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T87_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
NEXT=Stage14-t88
```

---

## Locked boundary

```text
STAGE14_T87=COMPLETE_PROJECTIVE_RING_CLASS_BRIDGE_AND_FIXED_POWER_CONDUCTOR_ENDPOINT_COLLAPSE
MERGED_T86_IMPORTED=true
PROJECTIVE_GAUSSIAN_SELECTOR_GROUP_REENTERED=true
EXACT_GAMMA_A_PRIME_PROJECTIVE_INCIDENCE=true
PROJECTIVE_INCIDENCE=[gamma]*[a]*[pi']=1
PROJECTIVE_GROUP_ORDER=product_{p|d}(p-chi4(p))
PROJECTIVE_GROUP_ORDER_SCALE=d*Bo1
T86_FORM_DISCRIMINANT_RING_CLASS_IDENTIFIED=true
RING_CLASS_IS_PROJECTIVE_GROUP_MOD_I=true
RING_CLASS_NUMBER_SCALE=d*Bo1
PROJECTIVE_CHARACTER_ORTHOGONALITY_EXACT=true
NONPRINCIPAL_TERMS_DISCARDED=false
PROJECTIVE_CLASS_IS_INDEX_D_LATTICE=true
PROJECTIVE_ANNULUS_LATTICE_BOUND=L/d+sqrt(L)+1
PRIMALITY_NOT_USED_FOR_LARGE_D_SAVING=true
FIXED_POWER_D_PROJECTIVE_LATTICE_SAVING_PROVED=true
FIXED_POWER_D_SAVING_EXPONENT=min(theta,1/4)
SUPER_SQRT_PRIME_BRANCH_USED_FOR_UNIFORM_QUARTER_ERROR=true
HARD_SELECTOR_CONDUCTOR_ENDPOINT=d=Bo1
HARD_PROJECTIVE_GROUP_SIZE=Bo1
HARD_RING_CLASS_NUMBER=Bo1
MOVING_DELTA0_ENDPOINT_NOT_PROVED=true
TH25_NEEDED=true
TH25_TARGET_REOPENED=false
TH25_REFINEMENT_REQUESTED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH25=false
TH26_NEEDED=false
PREFERRED_RECEIVER=SharedUEndpointSmallSelectorProjectiveRingClassShortGaussianCofactorCanonicalPrimePhysicalIncidenceEnergy
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T87_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
NEXT=Stage14-t88
```
