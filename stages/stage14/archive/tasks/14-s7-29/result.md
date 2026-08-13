# Stage14-s7-29 — common-core Gaussian root lines, primitive lattice count, and the 3/4 bound

## Status

`COMPLETE_COMMON_CORE_GAUSSIAN_ROOT_LINE_PRIMITIVE_LATTICE_COUNT_AND_3_4_BOUND`

Stage14-s7-29 consumes merged `s7-28` on top of the exact common-core strip of merged `4cg`.

The key point is that the primitive xi-agreement pair retained by s7-28 is not an unconstrained pair.  The fixed common core `C` divides the positive plus host

```text
H_k^+=D^2+A^2,
```

while `C` is coprime to the odd xi-agreement product.  In the s7-28 primitive coordinates this becomes a Gaussian root-line congruence modulo essentially all of `C`.

Because the modulus pair is primitive, the usual `+min(U,V)` boundary loss in a crude congruence count is not present.  Two distinct primitive points on the same CRT root line have determinant a nonzero multiple of the modulus.  In a dyadic box this gives

```text
# primitive points on one root line
  << 1 + U*V/C.
```

Combining this with the residual hyperbola `u_res*v_res<=B^(1/4+o(1))` cancels the entire common-core exponent.  Every surviving balanced endpoint block satisfies

```text
V_{theta,phi}(B) << B^(2*phi+1/4+o(1))
                 << B^(3/4+o(1)),
```

because merged 4cg has `phi<=1/4`.

Thus the previous `7/8` endpoint is improved unconditionally to

```text
V(B) << B^(3/4+o(1)).
```

No external genus-one, determinant-method, large-sieve, or H theorem is used.

---

## 1. Imported exact coefficient space

Keep the merged 4cg endpoint variables

```text
alpha,delta = B^(theta+o(1)),
beta,gamma  = B^(1/2-theta+o(1)),
3/16 <= theta <= 5/16,

R,J = B^(phi+o(1)),
S,T = B^(3/8-phi+o(1)),
1/8 <= phi <= 1/4,
```

on the surviving strip

```text
0 <= theta-phi <= 1/8,
theta+phi >= 3/8.
```

Write the reduced residual triple as

```text
q_k=C*u_res,
q_xi=C*v_res,
```

with

```text
C <= B^(2*theta+2*phi-3/4+o(1)),
u_res <= B^(2*theta-2*phi+o(1)),
v_res <= B^(1/4+2*phi-2*theta+o(1)),

u_res*v_res <= B^(1/4+o(1)).                 (1.1)
```

Merged 4cg also gives

```text
gcd(C,oddpart(R*J))=1.                       (1.2)
```

Merged s7-27/s7-28 retain the full signed quotient decoration

```text
a=c_x^+,
b=c_x^-,
c=c_k^+,
d=c_k^-,
```

which has only `B^o(1)` possibilities after fixing `(C,u_res,v_res)`.

For the xi-agreement allocation put

```text
U=L_x^+,
V=L_x^-,
gcd(U,V)=1,
U*V=oddpart(R*J)=B^(2*phi+o(1)).              (1.3)
```

Then s7-28 reconstructs

```text
D+A=a*U,
D-A=b*V,

D=(aU+bV)/2,
A=(aU-bV)/2.                                  (1.4)
```

All identities in Sections 2--7 are scale-free.  Although s7-27/s7-28 were introduced to attack the top-theta saturation set, the exact signed allocation, primitive-ratio reconstruction and common-core identities used below do not require `theta=5/16`.  We therefore apply them on the whole surviving 4cg strip.

---

## 2. The common core is a quadratic congruence on the primitive pair

From (1.4),

```text
H_k^+=D^2+A^2
     =(a^2 U^2+b^2 V^2)/2.                    (2.1)
```

The common-core definition gives

```text
oddpart(H_k^+)=C*oddpart(S*T),
```

so, because `C` is odd,

```text
boxed:
C | a^2 U^2+b^2 V^2.                          (2.2)
```

Together with (1.2),

```text
boxed:
gcd(C,U*V)=1.                                  (2.3)
```

The only possible nonunit coefficient defect comes from `gcd(a,b)`, and that defect is endpoint-small.

Let

```text
g=gcd(a,b),
a=g*a_0,
b=g*b_0,
gcd(a_0,b_0)=1.                               (2.4)
```

If an odd prime power divides `g`, it divides both `D+A` and `D-A`, hence both `D` and `A`.  Since

```text
D=delta*s,
A=alpha*r,
gcd(alpha,delta)=1,
```

we have

```text
boxed:
oddpart(g) | r*s.                               (2.5)
```

At the endpoint `r,s=B^o(1)`, therefore

```text
g=B^o(1).                                       (2.6)
```

Define

```text
C_bad=gcd(C,g^2),
C_0=C/C_bad.                                    (2.7)
```

Then

```text
C_bad <= g^2=B^o(1),
C_0=C*B^o(1)^{-1}.                              (2.8)
```

Since `C | g^2(a_0^2U^2+b_0^2V^2)` and

```text
gcd(C/C_bad,g^2/C_bad)=1,
```

we obtain

```text
boxed:
C_0 | a_0^2 U^2+b_0^2 V^2.                    (2.9)
```

Moreover

```text
boxed:
gcd(C_0,a_0*b_0*U*V)=1.                       (2.10)
```

Indeed, (2.3) gives coprimality with `UV`; if an odd `p|C_0` also divided `a_0`, then (2.9) would force `p|b_0V`, contradicting `gcd(a_0,b_0)=1` and `p∤V`.  The same argument handles `b_0`.

---

## 3. Exact Gaussian CRT root lines

For every odd prime power `p^e || C_0`, (2.9)--(2.10) give

```text
(a_0 U)^2 == -(b_0 V)^2 (mod p^e).             (3.1)
```

Thus

```text
(a_0 U/(b_0 V))^2 == -1 (mod p^e).             (3.2)
```

A solvable odd prime-power congruence `z^2=-1 (mod p^e)` has exactly two roots, and solvability forces

```text
p == 1 (mod 4).                                  (3.3)
```

Therefore, for each fixed `C_0,a_0,b_0`, the primitive pair lies on exactly

```text
boxed:
2^omega(C_0)                                    (3.4)
```

CRT lines

```text
boxed:
U == rho*V (mod C_0),                            (3.5)
```

where `rho` is a unit modulo `C_0`.

Since

```text
2^omega(C_0) <= tau(C_0)=B^o(1),                (3.6)
```

primewise Gaussian allocation itself has zero fixed-power cost.

This is the s-side common-core analogue of a root-line reduction, but it is derived in the actual charged-once s7 coefficient space.  No t66/tH coefficient space is imported.

---

## 4. Primitive root-line lattice lemma

We need one elementary counting lemma.

Fix integers `q>=1` and a unit `rho (mod q)`.  Let

```text
U0 < U <= 2U0,
V0 < V <= 2V0,
gcd(U,V)=1,
U == rho*V (mod q).                              (4.1)
```

Then

```text
boxed:
# {(U,V) satisfying (4.1)}
 <= 1 + 6*U0*V0/q.                              (4.2)
```

Proof: order the distinct primitive points by the rational slope `U/V`.  For two distinct points `(U_i,V_i)` and `(U_j,V_j)` on the same root line,

```text
q | U_i V_j-U_j V_i.                            (4.3)
```

The determinant cannot vanish: two positive primitive integer vectors with the same rational slope are identical.  Hence for adjacent slopes

```text
|U_i/V_i-U_j/V_j|
 = |U_iV_j-U_jV_i|/(V_iV_j)
 >= q/(4V0^2).                                  (4.4)
```

All slopes in the dyadic box lie in

```text
[U0/(2V0), 2U0/V0],
```

whose length is at most `3U0/(2V0)`.  Summing the adjacent spacings gives (4.2).

The primitivity is essential: it removes the entire family of integer multiples of one short lattice vector, which is exactly the boundary term left by the crude count `UV/q+min(U,V)`.

```text
PRIMITIVE_ROOT_LINE_DYADIC_COUNT_PROVED=true.      (4.5)
```

---

## 5. Count the primitive xi-agreement pair for fixed residual data

Dyadically localize

```text
U ~ U0,
V ~ V0.
```

By (1.3),

```text
U0*V0=B^(2*phi+o(1)).                              (5.1)
```

For each of the `B^o(1)` Gaussian CRT roots from Section 3, apply Section 4 with `q=C_0`.  Using (2.8),

```text
# primitive (U,V)
 << B^o(1) * (1 + U0*V0/C_0)
 << B^o(1) * (1 + B^(2phi)/C).                    (5.2)
```

Write

```text
C=B^(c+o(1)).                                      (5.3)
```

Merged 4cg gives

```text
c <= 2theta+2phi-3/4.                              (5.4)
```

Since `theta<=5/16`,

```text
2phi-c >= 3/4-2theta >= 1/8.                      (5.5)
```

Thus the `1` term in (5.2) is uniformly lower order and

```text
boxed:
fixed residual/quotient/small data
=> # primitive (U,V)
   <= B^(2phi-c+o(1)).                             (5.6)
```

Merged s7-28 then gives only `B^o(1)` opposite signed splits, root-product reconstructions, switch-product reconstructions and physical cell/root lifts for each primitive pair.

---

## 6. Residual support and exact exponent cancellation

Dyadically write

```text
u_res=B^(mu+o(1)),
v_res=B^(nu+o(1)).                                (6.1)
```

From (1.1),

```text
mu+nu <= 1/4.                                     (6.2)
```

For fixed `(theta,phi,c,mu,nu)`, the number of residual triples is at most

```text
B^(c+mu+nu+o(1))
 <= B^(c+1/4+o(1)).                               (6.3)
```

For every such triple:

- the full signed quotient quadruple has `B^o(1)` choices by s7-27;
- `(r,s)` and all 2-primary decorations have `B^o(1)` choices;
- the primitive xi-agreement pair has `B^(2phi-c+o(1))` choices by (5.6);
- every primitive pair has only `B^o(1)` physical completions by s7-28.

Therefore the whole dyadic block satisfies

```text
boxed:
V_{theta,phi,c,mu,nu}(B)
 << B^(c+1/4 + 2phi-c + o(1))
 =  B^(2phi+1/4+o(1)).                            (6.4)
```

The common-core exponent cancels **exactly**.

Since merged 4cg has

```text
phi <= 1/4,
```

we get uniformly

```text
boxed:
V_{theta,phi,c,mu,nu}(B)
 << B^(3/4+o(1)).                                 (6.5)
```

There are only `B^o(1)` dyadic blocks, so

```text
boxed:
V(B) << B^(3/4+o(1)).                             (6.6)
```

This is an unconditional fixed-power improvement of

```text
7/8 - 3/4 = 1/8.                                  (6.7)
```

---

## 7. Why this does not double-charge s7-25

Merged s7-25 used the charged-once datum

```text
(C,u_res,v_res,S*T)
```

and proved `B^o(1)` physical fiber after that datum was fixed.

Stage s7-29 does **not** multiply that `S*T` support by the new primitive-pair count.  Instead it uses the alternative exact s7-28 projection

```text
fixed residual + quotient decoration
-> primitive xi-agreement pair (U,V)
-> reconstruct S*T and the rest.                 (7.1)
```

Thus the block count is

```text
residual support
x primitive-pair fiber
x B^o(1) reconstruction,                         (7.2)
```

with no independent switch-product charge.

```text
S7_25_SWITCH_SUPPORT_DOUBLE_CHARGED=false.         (7.3)
```

---

## 8. Relation to merged 4cn and t66

Merged `4cn` puts the s7-27 ratio envelope into reciprocal Edwards/Jacobi form and requests

```text
PhysicalReciprocalEdwardsGenusOneAverageIncidence.
```

That is a valid mainline derived slice, but s7-28/s7-29 use a strictly sharper quantifier order for the s route:

```text
common core C
-> Gaussian root line for one primitive modulus pair
-> primitive determinant spacing
-> divisor/reconstruction completion.             (8.1)
```

No smooth genus-one average is needed to obtain (6.6).

Merged `t66` also obtains primewise root lines, but in a fixed-U Cayley squareclass coefficient space.  Its result is not cross-promoted here.  The s7-29 root line is instead

```text
(a_0 U/(b_0 V))^2 == -1 (mod C_0),                (8.2)
```

with the common core `C` as the modulus and the s7 primitive agreement pair as the moving lift.

```text
MAINLINE_4CN_H_USED_BY_S7_29=false
T66_CROSS_PROMOTED_TO_S7_29=false.                 (8.3)
```

---

## 9. Next receiver

The `7/8` barrier is closed.  The new current exponent is `3/4`.

The next obstruction is no longer the number of primitive lifts on one common-core root line; Section 4 controls that optimally at the level needed here.  To go below `3/4`, one must exploit extra structure in the worst `phi=1/4` blocks after the root-line count, for example the reciprocal opposite-side divisibility and the reconstructed switch/root products.

Define the next receiver

```text
QuarterPhiReciprocalPrimitiveRootLineEnergy.       (9.1)
```

It is the `phi=1/4` saturation of (6.4), retaining

```text
C,
(u_res,v_res),
full signed quotient decoration,
primitive common-core Gaussian root line (U,V),
opposite divisor split,
reciprocal reconstruction of X*Y and both switch products,
all physical masks.                                (9.2)
```

No claim below `3/4` is made in this stage.

---

## 10. H / tH decision

No auxiliary H theorem is needed for s7-29.

The primewise splitting requested by s7-28 closes by exact Gaussian CRT plus the primitive determinant-spacing lemma.  In particular, the genus-one H requested independently by merged 4cn is not needed by the s route for the new `3/4` bound.

```text
TH17_CROSS_PROMOTED_TO_S7_29=false
T66_CROSS_PROMOTED_TO_S7_29=false
GENERIC_GENUS_ONE_H_REQUESTED_BY_S7_29=false
S7_29_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.               (10.1)
```

Reconsider an s-specific H only after the exact `phi=1/4` reciprocal root-line energy has been algebraically reduced further.

---

## Stage boundary

```text
STAGE14_S7_29=COMPLETE_COMMON_CORE_GAUSSIAN_ROOT_LINE_PRIMITIVE_LATTICE_COUNT_AND_3_4_BOUND
MERGED_4CG_IMPORTED=true
MERGED_S7_27_IMPORTED=true
MERGED_S7_28_IMPORTED=true
MERGED_4CN_COMPATIBILITY_CHECKED=true
MERGED_T66_COMPATIBILITY_CHECKED=true
FULL_STRIP_PRIMITIVE_PARAMETERIZATION_VALID=true
COMMON_CORE_DIVIDES_PRIMITIVE_PLUS_QUADRATIC_VALUE=true
COMMON_CORE_COPRIME_TO_PRIMITIVE_AGREEMENT_PRODUCT=true
QUOTIENT_COMMON_GCD_ODDPART_DIVIDES_R_S=true
COMMON_CORE_BAD_COEFFICIENT_PART=Bo1
COMMON_CORE_GOOD_MODULUS=C/B^o(1)
COMMON_CORE_GAUSSIAN_ROOT_LINES_PROVED=true
COMMON_CORE_GAUSSIAN_CRT_ROOT_MULTIPLICITY=Bo1
PRIMITIVE_ROOT_LINE_DYADIC_COUNT_PROVED=true
FIXED_RESIDUAL_PRIMITIVE_AGREEMENT_PAIR_EXPONENT=2*phi-c
DYADIC_RESIDUAL_SUPPORT_EXPONENT=c+1/4
DYADIC_POST_ROOT_LINE_PACKET_EXPONENT=2*phi+1/4
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4
IMPROVEMENT_OVER_7_8=1/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
S7_25_SWITCH_SUPPORT_DOUBLE_CHARGED=false
MAINLINE_4CN_H_USED_BY_S7_29=false
TH17_CROSS_PROMOTED_TO_S7_29=false
T66_CROSS_PROMOTED_TO_S7_29=false
GENERIC_GENUS_ONE_H_REQUESTED_BY_S7_29=false
S7_29_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
REMAINING_RECEIVER=QuarterPhiReciprocalPrimitiveRootLineEnergy
NEXT=Stage14-s7-30
```