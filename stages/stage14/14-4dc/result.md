# Stage14-4dc — Gaussian product root line, transverse resultant no-go, and refined mainline H gate

## Status

`COMPLETE_GAUSSIAN_PRODUCT_ROOT_LINE_COMPRESSION_TRANSVERSE_RESULTANT_NOGO_AND_MAINLINE_H_GATE`

Stage14-4dc consumes merged `Stage14-4db`, merged `Stage14-s7-44`, merged `Stage14-s7-42`, and the exact signed-quotient / primitive-root-line identities of merged `Stage14-s7-27` and `Stage14-s7-29` on latest main.

The entering canonical theorem is

```text
V(B) << B^(1/2+o(1)).
```

No strict sub-square-root whole-family saving is proved here.  The purpose of 4dc is to sharpen the coefficient space of the genuine average-incidence obstruction identified by s7-44 and to prove that the most obvious cross-resultant shortcut cannot supply a second copy of the full common core.

The new minimal receiver is

```text
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy.
```

The s7-44 H gate is therefore promoted to the mainline, with a narrower target.

---

## 1. Imported square-root saturation band

Merged X13 gives

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged 4db and s7-44 reduce every possible equality sequence to

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,
H=B^o(1),
K=B^o(1),
C/J=B^o(1),
C_Cayley/J=B^o(1).                                (1.1)
```

Hence at fixed-power scale

```text
C=J=C_Cayley.                                     (1.2)
```

All four odd cross-state root-gcd cells are subpolynomial, so the surviving four-root packet is globally odd-primitive at fixed-power scale.

Merged s7-44 expresses the remaining `1/2` ledger as

```text
C choice:                    chi,
primitive Gaussian (U,V):    2phi-chi=1/4,
primitive endpoint column:   1/4-chi=1/2-2phi,
post-column reciprocal fiber: 0.                  (1.3)
```

The last two supports are not independent after the first residual is reinserted.

---

## 2. Signed first residual and Gaussian product coordinates

Use the merged s7-27/s7-29 notation

```text
a=c_x^+,
b=c_x^-,
D+A=aU,
D-A=bV,
gcd(U,V)=1.                                      (2.1)
```

Write

```text
g=gcd(a,b),
a=g*a0,
b=g*b0,
gcd(a0,b0)=1.                                    (2.2)
```

Merged s7-29 proves

```text
oddpart(g) | r*s,
r,s=B^o(1),                                       (2.3)
```

so `g=B^o(1)` at exponent scale.

Define the Gaussian product coordinates

```text
boxed:
P:=a0*U,
Q:=b0*V.                                          (2.4)
```

Equivalently,

```text
P=(D+A)/g,
Q=(D-A)/g.                                        (2.5)
```

Merged s7-27 gives

```text
oddpart(a*b)=oddpart(u_res).                       (2.6)
```

On the theta-quarter band merged s7-42 gives

```text
u_res<=B^(A(phi)+o(1)),
A(phi):=1/2-2phi,                                 (2.7)
```

while merged s7-29 gives

```text
U*V=B^(2phi+o(1)).                                 (2.8)
```

Because `g=B^o(1)`, (2.6)--(2.8) yield

```text
boxed:
P*Q<=B^(A(phi)+2phi+o(1))
    =B^(1/2+o(1)).                                 (2.9)
```

Thus the first residual support and the primitive `(U,V)` support naturally combine into one product pair of total hyperbolic size `B^(1/2+o(1))`.

---

## 3. The common-core equation becomes coefficient-free

Merged s7-29 peels the endpoint-small coefficient defect and produces

```text
C0=C/B^o(1),
gcd(C0,a0*b0*U*V)=1,
C0 | a0^2 U^2+b0^2 V^2.                           (3.1)
```

Using (2.4), this is exactly

```text
boxed:
C0 | P^2+Q^2.                                     (3.2)
```

Hence for every odd prime power `p^e||C0`,

```text
(P/Q)^2 == -1 (mod p^e).                          (3.3)
```

The product-pair Gaussian orientation has only `2^omega(C0)=B^o(1)` choices.

The pair `(P,Q)` is primitive after an endpoint-small gcd peel.  Indeed from (2.5)

```text
gcd(P,Q) | 2*gcd(A,D)/g.                          (3.4)
```

and, since

```text
A=alpha*r,
D=delta*s,
gcd(alpha,delta)=1,
r,s=B^o(1),                                        (3.5)
```

the odd part of `gcd(P,Q)` is `B^o(1)`.  Dividing this harmless gcd leaves a primitive pair without changing the fixed-power common-core modulus because `C0` is coprime to `P*Q`.

Therefore the primitive root-line lattice lemma of merged s7-29 applies directly to `(P,Q)`.

---

## 4. One Gaussian product root line absorbs residual plus `(U,V)` support

Dyadically localize the primitive reduction of `(P,Q)`.  By (2.9), its box product is at most `B^(1/2+o(1))`.

For each fixed Gaussian CRT orientation modulo `C0`, the s7-29 determinant-spacing lemma gives

```text
#(P,Q)
 <= B^o(1)*(1+P0*Q0/C0).                          (4.1)
```

On the square-root band

```text
chi<=1/4,                                         (4.2)
```

so the polynomial contribution is bounded by

```text
boxed:
E_PQ<=1/2-chi.                                    (4.3)
```

This exponent is exactly the sum of the two old supports:

```text
A(phi)+(2phi-chi)
 =(1/2-2phi)+(2phi-chi)
 =1/2-chi.                                        (4.4)
```

Thus the product-pair line does not create a new saving; it proves that the first residual and primitive Gaussian root line are one charged-once support in a more economical coordinate system.

---

## 5. Product-pair splitting has divisor-many fibers

Fix `(P,Q)`.  Any physical preimage satisfies

```text
P=a0*U,
Q=b0*V.                                           (5.1)
```

The number of positive divisor splittings is at most

```text
tau(P)*tau(Q)=B^o(1).                             (5.2)
```

The restrictions

```text
gcd(a0,b0)=1,
gcd(U,V)=1,
physical dyadic ranges,
squarefree-cell masks,
statewise reducedness,
2-primary decorations                                  (5.3)
```

only filter these splittings.

After a split is fixed, `u_res` is determined up to its `B^o(1)` 2-primary decoration by (2.6).  Merged s7-42 proves

```text
RESIDUAL_TO_SINGLE_COLUMN_FIBER_MULTIPLICITY=Bo1. (5.4)
```

Hence the endpoint-linear column compatible with a fixed product-pair split has only `B^o(1)` possibilities.

Together with merged X13 post-column reverse reciprocal reconstruction,

```text
boxed:
fixed (C,P,Q)
=> full physical endpoint / reciprocal completion
   has at most B^o(1) multiplicity after divisor splitting.   (5.5)
```

This is a reparameterization of the physical receiver, not a claim that every Gaussian product-pair has a completion.

---

## 6. The compressed square-root ledger

The charged-once count may now be written as

```text
C choice:                     chi,
Gaussian product root line:   1/2-chi,
product split + endpoint completion: 0.            (6.1)
```

Therefore

```text
boxed:
E_4dc<=chi+(1/2-chi)=1/2.                         (6.2)
```

The whole-family exponent remains exactly the merged X13 square-root exponent.

The value of the reparameterization is that the analytic obstruction is no longer a formal Cartesian product of two independently counted root-line point sets.  It is a single Gaussian product root line together with the sparse subset of divisor splittings that admit the full physical endpoint/reciprocal completion.

```text
DUAL_ROOT_LINE_CARTESIAN_PRODUCT_REPARAMETERIZED=true.        (6.3)
```

---

## 7. Exact transverse resultant no-go

Merged s7-44 also gives the endpoint primitive root line.  Put

```text
A_z=z1*r2*s2,
B_z=z2*r1*s1.                                     (7.1)
```

After its endpoint-small peel, for every odd `p^e||C0`,

```text
A_z/B_z == sigma_p (mod p^e),
sigma_p^2 == 1.                                   (7.2)
```

From (3.3), write

```text
P/Q == rho_p (mod p^e),
rho_p^2 == -1.                                    (7.3)
```

The two root polynomials are transverse over every odd prime:

```text
Res(t^2+1,t^2-1)=4.                               (7.4)
```

If an odd prime `p|C0` divided

```text
P*B_z-Q*A_z,                                      (7.5)
```

then (because `Q,B_z` are units modulo `p`) we would have

```text
rho_p == sigma_p (mod p).                         (7.6)
```

Squaring gives `-1==1 (mod p)`, impossible for odd `p`.  The same argument with the plus sign gives `rho_p==-sigma_p`, again impossible.

Therefore

```text
boxed:
gcd(C0,P*B_z-Q*A_z)=1,                           (7.7)

boxed:
gcd(C0,P*B_z+Q*A_z)=1.                           (7.8)
```

So the obvious rational cross determinant and cross sum do **not** contain a second copy of `C`; they are units on the full good core.

This is stronger than merely saying that a second determinant modulus has not been found.

---

## 8. Gaussian cross norms do not provide a fresh modulus

There are quadratic cross expressions which are divisible by `C0`; for example, modulo `C0`,

```text
P^2*B_z^2+Q^2*A_z^2
 ==Q^2*B_z^2*(rho^2+sigma^2)
 ==0,                                             (8.1)
```

and similarly

```text
P^2*A_z^2+Q^2*B_z^2 ==0 (mod C0).                 (8.2)
```

But these divisibilities are algebraic consequences of the two already charged equations

```text
P^2+Q^2 ==0 (mod C0),
A_z^2-B_z^2==0 (mod C0).                          (8.3)
```

They supply no fresh independent common-core modulus.  Charging them as a second spacing gain would reproduce the double-charge prohibited by merged s7-33/4cv/s7-44.

```text
GAUSSIAN_CROSS_NORM_SECOND_MODULUS_ALLOWED=false.  (8.4)
```

---

## 9. Minimal remaining physical energy receiver

After conditioning all `B^o(1)` decorations, the square-root obstruction can be stated using one Gaussian product root line.

For

```text
theta=1/4,
5/24<=phi<=1/4,
chi=2phi-1/4,                                     (9.1)
```

sum over odd common cores

```text
C~B^chi                                            (9.2)
```

and primitive product pairs `(P,Q)` satisfying

```text
P*Q<=B^(1/2+o(1)),
C/B^o(1) | P^2+Q^2,                               (9.3)
```

with one of the `B^o(1)` Gaussian orientations.

For each product pair, retain only divisor splittings

```text
P=a0*U,
Q=b0*V                                            (9.4)
```

that satisfy all original physical conditions and whose s7-42/X13 reconstruction produces a legal endpoint pair, row/column sign allocation, Cayley filter and reciprocal completion.

The trivial charged-once bound is

```text
sum_C I_C^phys <= B^(1/2+o(1)).                   (9.5)
```

Define

```text
boxed:
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy.
```

A strict sub-square-root theorem is precisely a uniform bound

```text
sum_C I_C^phys
 << B^(1/2-delta+o(1))                            (9.6)
```

for some fixed `delta>0` throughout the full phi band.

---

## 10. Mainline H decision

Merged s7-44 already proves that the local determinant/orientation bookkeeping is exhausted and opens an s-specific H gate.

Stage14-4dc does not close that gate.  It sharpens the theorem input by replacing the dual-root-line Cartesian product with the coefficient-free Gaussian product line plus physical completion fiber, and proves the transverse rational determinant cannot be used as an internal substitute.

Therefore the H gate is now promoted to the mainline:

```text
boxed:
MAINLINE_H_NEEDED=true,
MAINLINE_BLOCKED_BY_H=true.                        (10.1)
```

The refined target is

```text
boxed:
SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving.    (10.2)
```

Required output:

```text
sum_C I_C^phys
 << B^(1/2-delta+o(1))                             (10.3)
```

for any fixed `delta>0`, uniformly in `5/24<=phi<=1/4`, with all physical masks retained and without reusing `C` as a second determinant modulus.

Suitable mechanisms may include a genuine dispersion/large-sieve estimate, Gaussian integer energy theorem, or determinant method on the **physical completion subset**.  Any candidate theorem must be mapped to this exact coefficient space.

The generic genus-one H is not reopened, and the fixed-U projective-ray t/tH route is not cross-promoted:

```text
GENERIC_GENUS_ONE_H_REOPENED=false,
T80_CROSS_PROMOTED_TO_MAINLINE=false,
TH23_CROSS_PROMOTED_TO_MAINLINE=false.             (10.4)
```

---

## 11. Whole-family theorem and next step

No new exponent is claimed:

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.          (11.1)
```

Next:

```text
Stage14-4dd_after_H.
```

Do not reopen the row CRT lift, root-gcd peels, Cayley annulus, dual independent root-line charge, or a second full-core determinant spacing.

---

## Stage boundary

```text
STAGE14_4DC=COMPLETE_GAUSSIAN_PRODUCT_ROOT_LINE_COMPRESSION_TRANSVERSE_RESULTANT_NOGO_AND_MAINLINE_H_GATE
MERGED_4DB_IMPORTED=true
MERGED_S7_44_IMPORTED=true
MERGED_S7_42_IMPORTED=true
MERGED_S7_29_IMPORTED=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
SQRT_SATURATION_THETA=1/4
SQRT_SATURATION_PHI_RANGE=[5/24,1/4]
SQRT_SATURATION_COMMON_CORE_EXPONENT=chi=2phi-1/4
SQRT_SATURATION_GLOBAL_ODD_ROOT_PRIMITIVITY=true
SIGNED_QUOTIENT_FIRST_RESIDUAL_PRODUCT_IMPORTED=true
GAUSSIAN_PRODUCT_COORDINATES=P=a0*U,Q=b0*V
GAUSSIAN_PRODUCT_PAIR_SIZE_EXPONENT_AT_MOST=1/2
GAUSSIAN_PRODUCT_ROOT_EQUATION=P^2+Q^2=0_mod_C0
GAUSSIAN_PRODUCT_ROOT_LINE_EXPONENT=1/2-chi
PRODUCT_PAIR_TO_RESIDUAL_PRIMITIVE_SPLIT_MULTIPLICITY=Bo1
PRODUCT_PAIR_TO_SINGLE_COLUMN_MULTIPLICITY=Bo1
DUAL_ROOT_LINE_CARTESIAN_PRODUCT_REPARAMETERIZED=true
PRODUCT_ROOT_LINE_PLUS_CORE_TRIVIAL_COMPLETE_COUNT=1/2
TRANSVERSE_ROOT_POLYNOMIAL_RESULTANT=4
RATIONAL_CROSS_DETERMINANT_COPRIME_TO_FULL_GOOD_CORE=true
RATIONAL_CROSS_SUM_COPRIME_TO_FULL_GOOD_CORE=true
GAUSSIAN_CROSS_NORM_SECOND_MODULUS_ALLOWED=false
SECOND_FULL_CORE_DETERMINANT_SPACING_LEGAL=false
REMAINING_RECEIVER=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergy
S7_44_H_GATE_IMPORTED=true
S7_44_DUAL_ROOT_LINE_H_TARGET_REFINED=true
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=true
MAINLINE_H_TARGET=SquareRootThetaQuarterGloballyOddPrimitiveFullCoreGaussianProductRootLinePhysicalCompletionEnergyPowerSaving
MAINLINE_H_REQUIRED_OUTPUT=sum_C_I_C_phys<=B^(1/2-delta+o(1))_for_some_fixed_delta>0
GENERIC_GENUS_ONE_H_REOPENED=false
T80_CROSS_PROMOTED_TO_MAINLINE=false
TH23_CROSS_PROMOTED_TO_MAINLINE=false
NEXT=Stage14-4dd_after_H
```