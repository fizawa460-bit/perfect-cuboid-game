# Stage14-t90 — open the bounded canonical-Q weight and isolate the genuine Gaussian-orientation correlation

## Status

`COMPLETE_BOUNDED_Q_WEIGHT_OPENING_LOCAL_SELECTOR_PEEL_AND_GAUSSIAN_ORIENTATION_CORE`

Stage14-t90 consumes merged Stage14-t89, merged Stage14-t87/t88, and the completed immutable Stage14-tH25 snapshot.  The tH25 target is not reopened.

The entering whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

No new whole-family exponent is claimed here.

The purpose of t90 is exactly the task left by t89: open

```text
omega_U(Q)
```

once, separate deterministic/divisor-local selectors from the genuinely moving arithmetic, and decide whether a new immutable H snapshot is now justified.

---

## 1. Imported one-dimensional packet

Fix

```text
(U,epsilon,k,h,kappa,beta),
eta in {1,2},
k0=eta*k,
```

and the already-fixed reciprocal/inversion orientation.  Merged t89 gives

```text
Q=ell*delta0,
ell=LPF(Q),
v_ell(Q)=1,
delta0=Q/ell,
ell^2>4B,
ell^2>2*h*k0*Q,
h*k0*Q<=2B,
```

with all odd prime factors of `Q` split in `Z[i]` and endpoint selector conductor

```text
d=B^o(1).
```

Choose

```text
a in Z[i], N(a)=k0,
gamma in Z[i], N(gamma)=delta0,
pi_ell in Z[i], N(pi_ell)=ell
```

with the canonical orientation for `pi_ell`.  Then

```text
w=gamma*pi_ell,
z=a*w,
W_sigma=a*gamma=p-i*sigma*q.
```

Merged t89 defines `omega_U(Q)` as the number of such Gaussian labels surviving every remaining physical selector.

```text
MERGED_T89_IMPORTED=true
MERGED_TH25_CONSUMED=true
TH25_TARGET_REOPENED=false
```

---

## 2. Exact opening of omega_U(Q)

Let `A(k0)` be the finite set of Gaussian factors of norm `k0` allowed by the frozen unit/orientation convention.  For fixed `Q`, write

```text
R(delta0)={gamma in Z[i]: N(gamma)=delta0}.
```

Then the physical weight can be written exactly as

```text
omega_U(Q)
 = sum_{a in A(k0)}
   sum_{gamma in R(delta0)}
     P_prim(a,gamma)
     P_tag(U,kappa,beta;a,gamma)
     P_cell(U;a,gamma)
     P_proj(d;a,gamma,pi_ell)
     P_sign(U;a,gamma),                              (2.1)
```

where every factor is a `0/1` selector.  No new variable is introduced in (2.1): it only names the masks already retained by t89.

The divisor envelope remains

```text
#A(k0)<=r_2(k0)=B^o(1),
#R(delta0)<=r_2(delta0)=B^o(1).
```

Hence (2.1) reproduces

```text
0<=omega_U(Q)<=B^o(1).
```

```text
PHYSICAL_Q_WEIGHT_EXACT_SELECTOR_EXPANSION_PROVED=true
```

---

## 3. Primitive-cover mask is an exact Möbius-local selector

From

```text
W_sigma=a*gamma=p-i*sigma*q
```

the primitive-cover condition is

```text
gcd(p,q)=1.
```

It has the exact identity

```text
P_prim(a,gamma)
 = sum_{e|p, e|q} mu(e).                            (3.1)
```

Every divisor in (3.1) satisfies

```text
e^2 | p^2+q^2 = k0*delta0.
```

Thus for one fixed Gaussian label the number of Möbius terms is divisor-many:

```text
B^o(1).
```

The primitive condition is therefore a local/divisor switch, not an additional polynomial coordinate.

Moreover any physical primitive product forces `gamma` itself to be primitive: if a rational prime divided both coordinates of `gamma`, it would divide both coordinates of `a*gamma`.

```text
PRIMITIVE_COVER_MOBIUS_EXPANSION_EXACT=true
PRIMITIVE_SELECTOR_POINTWISE_MULTIPLICITY=Bo1
PHYSICAL_PRODUCT_PRIMITIVE_IMPLIES_GAMMA_PRIMITIVE=true
```

---

## 4. Denominator tag and reciprocal orientation carry no moving allocation entropy

The packet already fixes

```text
(kappa,beta),
beta=gcd(kappa,v_scale),
```

and merged t73 proves that a fixed denominator tag determines the signed Cayley orientation uniquely.  Therefore the old `2^omega(kappa)` sign allocation is not a moving choice inside `omega_U(Q)`.

Likewise the reciprocal/inversion branch and canonical Gaussian unit convention were fixed before t89.

Consequently

```text
P_tag * P_sign
```

is a fixed-coefficient representation-local predicate.  It may remove Gaussian labels, but it contributes no new independent sum.

```text
FIXED_TAG_SIGN_ALLOCATION_MULTIPLICITY=1
RECIPROCAL_ORIENTATION_MOVING_MULTIPLICITY=O1
TAG_AND_SIGN_SELECTORS_CREATE_NEW_POLYNOMIAL_VARIABLE=false
```

This statement does not declare the tag predicate automatic; it only removes the false entropy of re-summing its already-fixed orientation choices.

---

## 5. Angular gcd and four-cell labels are deterministic functions of the reconstructed cover

Let the fixed direction odd columns be

```text
A0=odd(b-a),
B0=odd(b+a),
```

and reconstruct

```text
r=q-p,
t=q+p,
R=odd(r),
T=odd(t).
```

Merged t78 defines

```text
d_AR=gcd(A0,R),
d_AT=gcd(A0,T),
d_BR=gcd(B0,R),
d_BT=gcd(B0,T).
```

For a primitive physical cover,

```text
gcd(A0,B0)=1,
gcd(R,T)=1,
```

so these four cells are pairwise coprime and satisfy exactly

```text
g=d_AR*d_AT*d_BR*d_BT
 =gcd(A0*B0,R*T).                                  (5.1)
```

Thus after `(a,gamma)` is fixed, `(p,q)`, `(r,t)`, `g`, all four cells, and the residual cofactor `c` are functions, not choices.

If one wants a tensor form, merged t78 supplies an exact Möbius/divisor-switch expansion with only `B^o(1)` pointwise terms.  Therefore `P_cell` is a divisor-local selector and cannot be charged as a second analytic dimension.

```text
FOUR_CELL_LABELS_DETERMINED_BY_GAUSSIAN_LABEL=true
ANGULAR_GCD_MOVING_ALLOCATION_MULTIPLICITY=1
FOUR_CELL_MOBIUS_EXPANSION_AVAILABLE=true
FOUR_CELL_SELECTOR_POINTWISE_MULTIPLICITY=Bo1
```

---

## 6. Endpoint-small projective selector has an exact subpolynomial character expansion

Merged t87 gives the endpoint selector divisor

```text
d | D_Ubeta | |R_U*S_U|,
d=B^o(1),
gcd(d,ell*k0*delta0)=1,
```

and the exact projective condition

```text
[gamma]*[a]*[pi_ell]=1 in
G(d)=(Z[i]/dZ[i])^x/(Z/dZ)^x.                     (6.1)
```

Equivalently

```text
P_proj
 = 1/|G(d)| * sum_{chi in G(d)^}
     chi(gamma) chi(a) chi(pi_ell).                 (6.2)
```

On the only unsaved branch

```text
|G(d)|=B^o(1).
```

Hence the full projective selector is an exact `B^o(1)`-term finite-character expansion.  It is not a growing ring-class family anymore.

The canonical prime enters only through the bounded phase

```text
chi(pi_ell),
```

while the cofactor representation enters through

```text
chi(gamma).
```

```text
ENDPOINT_PROJECTIVE_SELECTOR_CHARACTER_EXPANSION_EXACT=true
ENDPOINT_PROJECTIVE_CHARACTER_FAMILY_SIZE=Bo1
RING_CLASS_FAMILY_REINTRODUCED=false
```

---

## 7. Canonical reduced weight

After Sections 3--6, every selector except the Gaussian representation itself is either

```text
O(1) fixed orientation,
B^o(1) divisor/Mobius localization,
or B^o(1) endpoint-projective character expansion.
```

Therefore `omega_U(Q)` is a `B^o(1)` linear combination of weights of the form

```text
chi(pi_ell)
*
Sum_U,chi(delta0),                                  (7.1)
```

where

```text
Sum_U,chi(delta0)
 := sum_{N(gamma)=delta0}^{primitive}
      c_U(gamma) chi(gamma),                        (7.2)
```

and `c_U(gamma)` is a product of fixed tag/sign selectors and divisor-local primitive/four-cell selectors.

Uniformly

```text
|Sum_U,chi(delta0)| <= r_2(delta0)*B^o(1)=B^o(1).
```

This is the first t89 descendant in which the hidden weight has been opened far enough to identify a genuine moving arithmetic object.

```text
Q_WEIGHT_REDUCED_TO_GAUSSIAN_ORIENTATION_SUM=true
CANONICAL_PRIME_DEPENDENCE_ONLY_THROUGH_LPF_AND_ENDPOINT_CHARACTER=true
COFACTOR_MOVING_CORE_IS_PRIMITIVE_GAUSSIAN_REPRESENTATION_SUM=true
```

No multiplicativity of the full coefficient `c_U` is asserted.  The fixed tag/four-cell masks may correlate prime orientations, so treating (7.2) as a completely multiplicative function would be unjustified.

```text
FULL_REDUCED_WEIGHT_MULTIPLICATIVE_PROVED=false
```

---

## 8. Final one-dimensional correlation

The fixed-packet survivor is reduced to `B^o(1)` many sums dominated by

```text
sum_{Q~X}
  1_{ell=LPF(Q), v_ell(Q)=1}
  1_{ell^2>4B}
  1_{ell^2>2*h*k0*Q}
  1_{h*k0*Q<=2B}
  chi(pi_ell)
  Sum_U,chi(Q/ell),                                 (8.1)
```

with all odd prime factors of `Q` split in `Z[i]`.

The principal endpoint character gives the positive representation weight; nonprincipal characters give signed Gaussian-orientation correlations.  The principal term cannot simply be discarded, and the split-prime support by itself is only logarithmically sparse at fixed-power scale.

Therefore t90 still proves no packet power saving.

```text
ONE_DIMENSIONAL_CANONICAL_LPF_GAUSSIAN_ORIENTATION_CORRELATION_PROVED=true
PRINCIPAL_GAUSSIAN_REPRESENTATION_TERM_REMAINS=true
NONPRINCIPAL_ENDPOINT_CHARACTER_TERMS_REMAIN=true
SPLIT_PRIME_SUPPORT_ALONE_FIXED_POWER_SAVING=false
T90_FIXED_U_PACKET_POWER_SAVING_PROVED=false
```

---

## 9. tH26 decision

Unlike t89, the residual object is now sufficiently explicit to justify a new immutable theorem audit.

Stage14-tH26 should audit the exact frozen t90 receiver:

```text
FixedPacketCanonicalLargestPrime
PrimitiveGaussianCofactorRepresentationCharacterWeightedSieve
```

with the canonical-LPF gap, split-prime support, principal/nonprincipal endpoint-character decomposition, fixed tag/four-cell masks, and all physical inequalities retained.

The audit must answer whether any existing theorem gives a **uniform fixed positive B-power saving** for (8.1), not merely a logarithmic density gain or a bound after dropping the physical masks.

```text
TH25_COMPLETE=true
TH25_TARGET_REOPENED=false
TH26_NEEDED=true
TH26_DISPATCHED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH26=false
```

The t-route may proceed to t91 while tH26 runs; under `H-PROTOCOL.md`, later stages must not mutate the t90 snapshot request.

---

## 10. Preferred receiver and global ledger

```text
PREFERRED_RECEIVER=SharedUCanonicalLPFPrimitiveGaussianCofactorRepresentationCharacterWeightedPhysicalSieve
```

No fixed-U result is cross-promoted to the whole family.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T90_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
NEXT=Stage14-t91
```

---

## Locked boundary

```text
STAGE14_T90=COMPLETE_BOUNDED_Q_WEIGHT_OPENING_LOCAL_SELECTOR_PEEL_AND_GAUSSIAN_ORIENTATION_CORE
MERGED_T89_IMPORTED=true
MERGED_TH25_CONSUMED=true
PHYSICAL_Q_WEIGHT_EXACT_SELECTOR_EXPANSION_PROVED=true
PRIMITIVE_COVER_MOBIUS_EXPANSION_EXACT=true
PRIMITIVE_SELECTOR_POINTWISE_MULTIPLICITY=Bo1
PHYSICAL_PRODUCT_PRIMITIVE_IMPLIES_GAMMA_PRIMITIVE=true
FIXED_TAG_SIGN_ALLOCATION_MULTIPLICITY=1
RECIPROCAL_ORIENTATION_MOVING_MULTIPLICITY=O1
FOUR_CELL_LABELS_DETERMINED_BY_GAUSSIAN_LABEL=true
ANGULAR_GCD_MOVING_ALLOCATION_MULTIPLICITY=1
FOUR_CELL_MOBIUS_EXPANSION_AVAILABLE=true
ENDPOINT_PROJECTIVE_SELECTOR_CHARACTER_EXPANSION_EXACT=true
ENDPOINT_PROJECTIVE_CHARACTER_FAMILY_SIZE=Bo1
Q_WEIGHT_REDUCED_TO_GAUSSIAN_ORIENTATION_SUM=true
CANONICAL_PRIME_DEPENDENCE_ONLY_THROUGH_LPF_AND_ENDPOINT_CHARACTER=true
COFACTOR_MOVING_CORE_IS_PRIMITIVE_GAUSSIAN_REPRESENTATION_SUM=true
FULL_REDUCED_WEIGHT_MULTIPLICATIVE_PROVED=false
ONE_DIMENSIONAL_CANONICAL_LPF_GAUSSIAN_ORIENTATION_CORRELATION_PROVED=true
PRINCIPAL_GAUSSIAN_REPRESENTATION_TERM_REMAINS=true
NONPRINCIPAL_ENDPOINT_CHARACTER_TERMS_REMAIN=true
T90_FIXED_U_PACKET_POWER_SAVING_PROVED=false
TH25_COMPLETE=true
TH25_TARGET_REOPENED=false
TH26_NEEDED=true
TH26_DISPATCHED=false
T_ROUTE_BLOCKED_WAITING_FOR_TH26=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T90_PROVES_ADDITIONAL_WHOLE_FAMILY_POWER_SAVING=false
FIXED_U_TO_WHOLE_FAMILY_CROSS_PROMOTION_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFPrimitiveGaussianCofactorRepresentationCharacterWeightedPhysicalSieve
NEXT=Stage14-t91
```
