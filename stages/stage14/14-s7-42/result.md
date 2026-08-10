# Stage14-s7-42 — consume X13 square-root closure and stratify the theta-quarter same-side gcd

## Status

`COMPLETE_X13_SQRT_IMPORT_AND_THETA_QUARTER_SAMESIDE_PRIMITIVE_REDUCTION`

Stage14-s7-42 consumes latest merged `Stage14-X13`, merged `Stage14-4cz`, merged `Stage14-s7-41`, and the independently supplied auxiliary result `Stage14-sH41`.

The canonical whole-family theorem has now advanced to

```text
boxed:
V(B) << B^(1/2+o(1)).
```

by merged X13.  X13 proves the missing post-column reverse reciprocal quantifier bridge uniformly on the full surviving low-core strip:

```text
fixed (U,V,M)
=> #(a,b,c,d,p,q)=B^o(1),
=> #N=B^o(1),
```

and therefore

```text
E_RRF <= 2phi + (1/4-chi) = 1-2theta.
```

This bridge is exactly the kind of reverse difference-of-squares reconstruction independently found by sH41 at the former `23/44` critical packet.  X13 proves the scale-uniform version needed for the global square-root theorem without any reverse reuse of the common-core root-line spacing.

Stage14-s7-42 does not reprove X13.  Its new s-route contribution is to work on the **new square-root saturation band** and show that every fixed-power same-side root gcd is already power-saved there.  Consequently square-root saturation requires the two same-side root-gcd cells to be subpolynomial on the entire theta-quarter band.

No strict sub-square-root whole-family saving is claimed.

---

## 1. Canonical X13 square-root theorem

Merged X13 gives on the nonproportional low-core region

```text
chi=2theta+2phi-3/4<=1/4,
E_RRF<=2phi+1/4-chi=1-2theta.
```

Together with

```text
E_k<=3theta-1/4
```

for `theta<=1/4`, the fixed-power high-core emptiness of merged 4cx, and the proportional bound

```text
E_prop<=7/16,
```

this yields

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Possible square-root saturation is confined by X13 to

```text
boxed:
theta=1/4,
5/24<=phi<=1/4,
0<=s<=phi-5/24,
chi=2phi-1/4,                                      (1.1)
```

where

```text
H=B^(s+o(1)).
```

The old `23/44` receiver and its row CRT lift are closed.

---

## 2. Relation to the supplied sH41 result

The independently supplied sH41 result states

```text
STAGE14_SH41=COMPLETE
FIXED_POWER_SAVING_PROVED=true
SAFE_CRITICAL_FIBER_DELTA=1/22
CRITICAL_FIBER_BOUND=B^(1/22+o(1))
USED_MECHANISM=post-column reverse reciprocal difference-of-squares factorization + divisor-bound reconstruction
PHYSICAL_FILTERS_RETAINED=true
COMMON_CORE_ROOT_LINE_REUSED_IN_REVERSE=false
TWIN_SHORT_DOUBLE_CHARGED=false
TH22_T78_CROSS_PROMOTED=false
```

At the former s7-41 critical packet its common base was `19/44`, so sH41 independently gives

```text
E_old-critical<=19/44+1/22=21/44<1/2.
```

Thus

```text
SH41_OLD_CRITICAL_ENDPOINT_BOUND=21/44
SH41_OLD_CRITICAL_ENDPOINT_STRICTLY_SUBSQRT=true.
```

However this old packet has

```text
theta=23/88>1/4,
```

and is already strictly below the new X13 square-root saturation band.  sH41 is therefore retained as an independent validation of the reverse-reciprocal mechanism, not cross-promoted as a theorem on the new theta-quarter band.

```text
SH41_REQUIRED_FOR_X13_SQRT_BOUND=false
SH41_CROSS_PROMOTED_TO_THETA_QUARTER_BAND=false.
```

---

## 3. First residual and single column have exactly the same scale on the sqrt band

On

```text
theta=1/4,
```

the first signed residual cap is

```text
mu:=2theta-2phi=1/2-2phi.                          (3.1)
```

Thus

```text
u_res<=B^(1/2-2phi+o(1)).                          (3.2)
```

The X13 reduced column support is

```text
1/4-chi
 =1/4-(2phi-1/4)
 =1/2-2phi.                                        (3.3)
```

Hence exactly

```text
boxed:
FIRST_RESIDUAL_EXPONENT
 = SINGLE_COLUMN_EXPONENT
 = A(phi):=1/2-2phi.                               (3.4)
```

Across the square-root band

```text
5/24<=phi<=1/4,
```

we have

```text
0<=A(phi)<=1/12.                                   (3.5)
```

This is the theta-quarter analogue of the s7-41 residual/twin-short scale coincidence, but after X13 there is only one live column support rather than a twin column/row pair.

---

## 4. Opposite signed quotient pair is divisor-many at theta quarter

Merged s7-30 gives the opposite signed-product cap

```text
nu<=1/4+2phi-2theta.
```

At `theta=1/4`,

```text
nu<=2phi-1/4=chi.                                  (4.1)
```

Merged s7-31 counts the opposite signed quotient pair after the first primitive/base data are fixed by

```text
B^o(1)*(1+B^(nu-chi)).
```

Therefore throughout the complete theta-quarter band

```text
boxed:
fixed outer data => #(c,d)=B^o(1).                 (4.2)
```

Consequently the same forward map used in s7-41 remains finite-fiber:

```text
u_res
-> divisor-many (a,b)
-> first reciprocal equation fixes p*q
-> divisor-many (p,q)
-> divisor-many (c,d)
-> physical reconstruction.
```

Conversely, X13 proves

```text
single column
-> z1,z2 and M
-> fixed (U,V,M)
-> reverse reciprocal factorization
-> divisor-many (a,b,c,d,p,q)
-> u_res.
```

Hence after the same common base is conditioned,

```text
boxed:
FIRST_RESIDUAL_AND_SINGLE_COLUMN_POWER_EQUIVALENT=true,
RESIDUAL_TO_SINGLE_COLUMN_FIBER_MULTIPLICITY=Bo1,
SINGLE_COLUMN_TO_RESIDUAL_FIBER_MULTIPLICITY=Bo1.  (4.3)
```

This is a no-double-charge statement, not a new saving by itself.

---

## 5. Same-side root gcd on the theta-quarter band

Define as in merged 4cz

```text
K_x=oddpart(gcd(x1,x2)),
K_y=oddpart(gcd(y1,y2)),
K=K_x*K_y.
```

The primewise support statements proved in 4cz are scale-free:

```text
gcd(K,q_xi)=1,
gcd(K,C)=1,
K^2|u_res,
K^2|X*Y,
K^2|M,
K|h_-,
K|h_+.
```

In particular

```text
boxed:
K^2|u_res,
K^2|h_-h_+.                                        (5.1)
```

The lost-core factor removed from the X13 column divides the once-charged common core, whereas `K` is coprime to `C`.  Therefore the `K^2` valuation survives in the reduced X13 column support.

Write

```text
K=B^(kappa+o(1)).                                  (5.2)
```

From `K^2|u_res` and (3.2),

```text
boxed:
0<=kappa<=A(phi)/2=1/4-phi.                        (5.3)
```

---

## 6. Fixed-K complete count

The common-core plus primitive-pair base in X13 costs

```text
2phi.
```

Fixing a dyadic same-side gcd `K=B^(kappa+o(1))` costs at most

```text
B^(kappa+o(1)).
```

The reduced single-column support has total exponent `A(phi)`.  Since `K^2` divides the column cofactor product and is coprime to the column modulus, the remaining column quotient has exponent at most

```text
A(phi)-2kappa.                                     (6.1)
```

This is nonnegative by (5.3).  X13 then reconstructs the entire row/signed quotient completion with `B^o(1)` multiplicity.

Therefore every fixed-K theta-quarter block satisfies

```text
E_K
 <=2phi+kappa+(A(phi)-2kappa)
 =2phi+A(phi)-kappa
 =1/2-kappa.                                       (6.2)
```

Thus

```text
boxed:
E_K<=1/2-kappa.                                    (6.3)
```

Every fixed-power same-side root-gcd stratum is strictly sub-square-root.

```text
THETA_QUARTER_FIXED_POWER_SAMESIDE_GCD_SAVING_PROVED=true
THETA_QUARTER_FIXED_K_SAVING=kappa.
```

---

## 7. Consequence for square-root saturation

Equation (6.3) shows that any sequence saturating the X13 `1/2` theorem must satisfy

```text
boxed:
kappa=0,
K=B^o(1).                                          (7.1)
```

Hence throughout the full X13 saturation band

```text
theta=1/4,
5/24<=phi<=1/4,
0<=s<=phi-5/24,
```

we additionally have

```text
boxed:
oddpart(gcd(x1,x2))=B^o(1),
oddpart(gcd(y1,y2))=B^o(1).                        (7.2)
```

The cross-root cells encoded by `H` may still carry fixed-power mass subject to the X13 condition on `s`; s7-42 does not remove them.

Thus the current theorem remains

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

The contribution of s7-42 is a strict receiver contraction, not a new global exponent.

---

## 8. New minimal receiver

The X13 receiver

```text
SquareRootThetaQuarterPrimitiveCommonCoreSingleColumnReverseReciprocalIncidence
```

is narrowed to

```text
boxed:
SquareRootThetaQuarterSameSidePrimitiveFirstResidualSingleColumnIncidence.
```

Its mandatory structure is

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
0<=s<=phi-5/24,
K=B^o(1),
A(phi)=1/2-2phi,
u_res<=B^(A(phi)+o(1)),
single column support<=B^(A(phi)+o(1)),
first residual <-> single column has B^o(1) fibers,
post-column row reconstruction=B^o(1).
```

There is now only one fixed-power residual/column degree of freedom after the common base, and no fixed-power same-side root gcd can support saturation.

The next deterministic question is whether the primitive common-core pair `(U,V)` and this single residual/column coordinate are genuinely independent after the `H`-normalization and the full k/xi host identities are imposed.

---

## 9. H / tH decision

No new auxiliary H/tH theorem is requested at s7-42.

Reasons:

1. merged X13 already supplies the scale-uniform reverse reciprocal bridge;
2. s7-42 still exposes unused exact same-side primitivity and first-residual/single-column equivalence;
3. the cross-root `H` normalization and the primitive `(U,V)`/column algebra have not yet been exhausted.

Therefore

```text
S7_42_SH41_CONSUMED=true
S7_42_X13_SQRT_IMPORTED=true
S7_42_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
TH22_CROSS_PROMOTED_TO_S7_42=false.
```

A new H should be considered only if the primitive common-core/single-column coupling survives the next exact audit.

---

## 10. Next

`Stage14-s7-43` should work only on

```text
SquareRootThetaQuarterSameSidePrimitiveFirstResidualSingleColumnIncidence
```

and test the exact coupling between

```text
primitive common-core pair (U,V)
```

and

```text
u_res <-> single column coordinate,
```

after removing the known cross-root/lost-core factors and imposing `K=B^o(1)`.

The target is any fixed saving below `1/2`.  Do not reopen the row CRT lift: X13 proves it is already divisor-reconstructible.

---

## Stage boundary

```text
STAGE14_S7_42=COMPLETE_X13_SQRT_IMPORT_AND_THETA_QUARTER_SAMESIDE_PRIMITIVE_REDUCTION
MERGED_X13_IMPORTED=true
MERGED_4CZ_IMPORTED=true
MERGED_S7_41_IMPORTED=true
SH41_EXTERNAL_AUXILIARY_RESULT_CONSUMED=true
SH41_OLD_CRITICAL_ENDPOINT_BOUND=21/44
SH41_OLD_CRITICAL_ENDPOINT_STRICTLY_SUBSQRT=true
SH41_REQUIRED_FOR_X13_SQRT_BOUND=false
SH41_CROSS_PROMOTED_TO_THETA_QUARTER_BAND=false
X13_REVERSE_RECIPROCAL_NONPROPORTIONAL_COUNT=1-2theta
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
SQRT_SATURATION_THETA=1/4
SQRT_SATURATION_PHI_RANGE=[5/24,1/4]
THETA_QUARTER_FIRST_RESIDUAL_EXPONENT=1/2-2phi
THETA_QUARTER_SINGLE_COLUMN_EXPONENT=1/2-2phi
THETA_QUARTER_OPPOSITE_QUOTIENT_CAP_EQUALS_CHI=true
FIRST_RESIDUAL_AND_SINGLE_COLUMN_POWER_EQUIVALENT=true
RESIDUAL_TO_SINGLE_COLUMN_FIBER_MULTIPLICITY=Bo1
SINGLE_COLUMN_TO_RESIDUAL_FIBER_MULTIPLICITY=Bo1
THETA_QUARTER_SAMESIDE_GCD_SQUARE_DIVIDES_FIRST_RESIDUAL=true
THETA_QUARTER_SAMESIDE_GCD_SQUARE_DIVIDES_SINGLE_COLUMN=true
THETA_QUARTER_FIXED_POWER_SAMESIDE_GCD_SAVING_PROVED=true
THETA_QUARTER_FIXED_K_BLOCK_EXPONENT=1/2-kappa
SQRT_SATURATION_REQUIRES_SAMESIDE_K=Bo1
S7_42_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
TH22_CROSS_PROMOTED_TO_S7_42=false
REMAINING_RECEIVER=SquareRootThetaQuarterSameSidePrimitiveFirstResidualSingleColumnIncidence
NEXT=Stage14-s7-43
```
