# Stage14-s7-30 — two-sided common-core root counting and the 11/16 bound

## Status

`COMPLETE_TWO_SIDED_COMMON_CORE_QUADRATIC_ROOT_PAIR_COUNT_AND_11_16_BOUND`

Stage14-s7-30 consumes merged `s7-29` and the mainline promotion `4cp`.

Merged `s7-29/4cp` prove the current whole-family estimate

```text
V(B) << B^(3/4+o(1)),
```

by fixing the full residual triple `(C,u_res,v_res)`, turning the xi-agreement primitive pair into a Gaussian root line modulo the common core, and applying primitive determinant spacing.

The new point is that fixing `v_res` is unnecessary.  After the first primitive xi-agreement pair is chosen, the opposite k-agreement product is reconstructed exactly.  The *moving* opposite signed quotients themselves satisfy a second quadratic congruence modulo the same common core `C`.  Although this second quotient pair need not be primitive, an elementary gcd decomposition plus the primitive root-line lemma gives a uniform count

```text
# opposite signed quotient pairs with product <= M
  << B^o(1) * (M^(1/2) + M/C).
```

This replaces the raw `v_res` support by a square-root/common-core quotient count.  A second exact point is needed for the exponent ledger: on the balanced common-core strip the exponent of `C` is not merely upper bounded.  Positivity and the squarefree switched cells pin it to

```text
C = B^(2*theta+2*phi-3/4+o(1)).
```

Combining the first primitive root line, the second nonprimitive quotient root line, and the residual support gives

```text
E(theta,phi)
 <= max(theta+phi+1/8, 1-2*theta)
 <= 11/16.
```

Hence the merged whole-family `3/4` bound improves unconditionally to

```text
boxed:
V(B) << B^(11/16+o(1)).
```

The unique possible `11/16` saturation remains the old quarter-phi corner

```text
theta=5/16,
phi=1/4.
```

No external determinant method, genus-one theorem, large sieve, or H/tH theorem is used.

---

## 1. Imported charged-once packet

Keep the merged 4cg balanced variables

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
theta+phi >= 3/8.                                  (1.1)
```

The common-core residual norms are

```text
q_k  = C*u_res,
q_xi = C*v_res,                                    (1.2)
```

with

```text
u_res <= B^(2*theta-2*phi+o(1)),
v_res <= B^(1/4+2*phi-2*theta+o(1)),
u_res*v_res <= B^(1/4+o(1)).                       (1.3)
```

Use the full signed quotient notation

```text
a = c_x^+,
b = c_x^-,
c = c_k^+,
d = c_k^-.                                        (1.4)
```

Merged s7-27 gives separately

```text
oddpart(a*b)=oddpart(u_res),
oddpart(c*d)=oddpart(v_res).                        (1.5)
```

Thus for fixed `u_res`, the first pair `(a,b)` has only `B^o(1)` possibilities; fixing `v_res` is only needed if one wants to pre-fix `(c,d)`.  Stage s7-30 will not do that.

For the xi-agreement allocation put

```text
U=L_x^+,
V=L_x^-,
gcd(U,V)=1,
U*V=oddpart(R*J)=B^(2*phi+o(1)).                   (1.6)
```

Then

```text
D+A=aU,
D-A=bV,
D=(aU+bV)/2,
A=(aU-bV)/2.                                       (1.7)
```

For the opposite k-agreement allocation later write

```text
p=L_k^+,
q=L_k^-,
gcd(p,q)=1.                                      (1.8)
```

---

## 2. The common-core exponent is scale-pinned

Merged s7-29 used only the upper bound

```text
C <= B^(2*theta+2*phi-3/4+o(1)).                  (2.1)
```

For the two-sided ledger we sharpen this to an equality at exponent scale.

Recall

```text
H_k^+=D^2+A^2,
D=delta*s,
A=alpha*r,                                        (2.2)
```

where the endpoint root factors `r,s=B^o(1)` and

```text
alpha,delta=B^(theta+o(1)).
```

Consequently

```text
H_k^+=B^(2*theta+o(1)).                            (2.3)
```

It remains to check that the 2-primary part cannot remove a fixed power.  Put

```text
g_A=gcd(A,D).
```

Merged 4cl gives

```text
g_A | r*s,
```

hence `g_A=B^o(1)`.  Write `A=g_A A_0`, `D=g_A D_0` with `gcd(A_0,D_0)=1`.  For a primitive integer pair `(A_0,D_0)`, either one entry is even and `A_0^2+D_0^2` is odd, or both are odd and the sum is `2 mod 4`.  Therefore

```text
v_2(A_0^2+D_0^2) <= 1,
```

so

```text
2^v_2(H_k^+) <= 2*g_A^2 = B^o(1).                 (2.4)
```

Hence

```text
boxed:
oddpart(H_k^+)=B^(2*theta+o(1)).                  (2.5)
```

The xi switched cells `S,T` are pairwise-coprime squarefree cells by merged s7-20.  At most one carries the prime `2`, so

```text
oddpart(S*T)=B^(3/4-2*phi+o(1)).                  (2.6)
```

By the exact common-core definition

```text
oddpart(H_k^+)=C*oddpart(S*T),                    (2.7)
```

we obtain

```text
boxed:
C=B^(c+o(1)),
c=2*theta+2*phi-3/4.                              (2.8)
```

The strip condition `theta+phi>=3/8` is precisely `c>=0`.

```text
COMMON_CORE_SCALE_PINNED=true.
```

---

## 3. First common-core root line: the xi-agreement pair

For fixed `(C,u_res)` and one of the divisor-many pairs `(a,b)`, merged s7-29 proves, after peeling only a `B^o(1)` coefficient factor from `C`, that `(U,V)` lies on one of `B^o(1)` Gaussian CRT root lines

```text
U == rho V (mod C_0),
C_0=C/B^o(1),                                      (3.1)
```

and the primitive determinant-spacing lemma gives

```text
# {(U,V)}
 << B^o(1) * (1 + U_0 V_0/C_0).                   (3.2)
```

Since

```text
U_0 V_0=B^(2*phi+o(1))
```

and, using (2.8),

```text
2*phi-c = 3/4-2*theta >= 1/8,                     (3.3)
```

the `1` is lower order.  Thus

```text
boxed:
# first primitive pair (U,V)
 <= B^(2*phi-c+o(1)).                              (3.4)
```

No `S*T` support is charged: it is reconstructed after `(U,V)` is known, exactly as in s7-28/s7-29.

---

## 4. The first pair reconstructs the opposite agreement product

Merged s7-28 gives the first reciprocal equation

```text
(aU)^2-(bV)^2
 =4*r*s*epsilon_k*L_k^-L_k^+.                     (4.1)
```

Therefore

```text
boxed:
N_k:=p*q=L_k^-L_k^+
 = ((aU)^2-(bV)^2)/(4*r*s*epsilon_k).              (4.2)
```

For every physical completion, `N_k` is a positive integer equal to the odd part of the k-agreement product.  Since `gcd(p,q)=1`, its ordered signed split

```text
N_k=p*q
```

has at most divisor-many possibilities:

```text
# {(p,q)} <= tau(N_k)=B^o(1).                     (4.3)
```

Fix one such split.  At this point the first residual `u_res`, first quotient pair `(a,b)`, both agreement modulus pairs `(U,V)` and `(p,q)`, and all endpoint-small decorations are fixed.  The second signed quotient pair `(c,d)` is still allowed to move.

---

## 5. The second signed quotient pair lies on the same common-core quadratic root family

The opposite signed equations are

```text
Q+P=c*p,
Q-P=d*q.                                          (5.1)
```

Hence

```text
H_xi^+=Q^2+P^2
       =(c^2 p^2+d^2 q^2)/2.                      (5.2)
```

The same common core satisfies

```text
C | H_xi^+,
```

and `C` is odd, so

```text
boxed:
C | p^2 c^2+q^2 d^2.                              (5.3)
```

Merged 4cg also proves

```text
gcd(C,oddpart(alpha*delta))=1.
```

Since `p*q=oddpart(alpha*delta)`, this gives

```text
boxed:
gcd(C,p*q)=1.                                     (5.4)
```

Unlike `(U,V)`, the quotient pair `(c,d)` need not be primitive.  Its product nevertheless has the direct size bound

```text
c*d
 = H_xi^- / oddpart(alpha*delta)
 <= B^(nu+o(1)),                                  (5.5)
```

where

```text
nu <= 1/4+2*phi-2*theta.                          (5.6)
```

This is the second root-line problem, with fixed modulus `C`, fixed unit coefficients `(p,q)`, and a moving positive pair of bounded product.

---

## 6. Nonprimitive quadratic-root-pair lemma

We record the elementary lemma used to count `(c,d)` without fixing `v_res`.

### Lemma

Let `Q` be odd, let `A,B` be units modulo `Q`, and let `M>=1`.  Then the number

```text
N_Q(M;A,B)
 = # {(x,y) in Z_{>0}^2:
      x*y <= M,
      A^2 x^2+B^2 y^2 == 0 (mod Q)}
```

satisfies

```text
boxed:
N_Q(M;A,B)
 << tau(Q)^O(1) * log(2M)^O(1)
    * (M^(1/2)+M/Q).                              (6.1)
```

In Stage14 notation the divisor/log factors are `B^o(1)`.

### Proof

Write

```text
h=gcd(x,y),
x=h*x_0,
y=h*y_0,
gcd(x_0,y_0)=1.                                  (6.2)
```

Define

```text
Q_h=Q/gcd(Q,h^2).                                 (6.3)
```

Then

```text
Q_h | A^2 x_0^2+B^2 y_0^2.                       (6.4)
```

Because `gcd(x_0,y_0)=1` and `A,B` are units, every prime dividing `Q_h` is coprime to `x_0y_0`.  Thus `(x_0,y_0)` lies on one of at most

```text
2^omega(Q_h) <= tau(Q)                            (6.5)
```

primitive quadratic root lines modulo `Q_h`.  Applying the s7-29 primitive determinant-spacing lemma in dyadic boxes of product `<=M/h^2` gives, for fixed `h`,

```text
#(x_0,y_0)
 << B^o(1) * (1 + M/(h^2 Q_h))
 =  B^o(1) * (1 + M*gcd(Q,h^2)/(Q*h^2)).          (6.6)
```

There are only `h<=sqrt(M)`, so the sum of the `1` terms is `O(sqrt(M))`.

For the main terms use

```text
gcd(Q,h^2)
 = sum_{e|Q, e|h^2} phi(e).                       (6.7)
```

For `e=prod p^j`, define

```text
t(e)=prod p^ceil(j/2).
```

Then

```text
e|h^2  <=>  t(e)|h,
t(e)^2>=e.                                        (6.8)
```

Hence

```text
sum_{h>=1} gcd(Q,h^2)/h^2
 <= zeta(2) * sum_{e|Q} phi(e)/t(e)^2
 <= zeta(2) * tau(Q),                             (6.9)
```

because `phi(e)<=e<=t(e)^2`.  Multiplying by `M/Q` proves (6.1).

No cancellation theorem is used.

```text
NONPRIMITIVE_QUADRATIC_ROOT_PAIR_LEMMA_PROVED=true.
```

---

## 7. Apply the lemma to the opposite signed quotients

Apply Section 6 with

```text
Q=C,
A=p,
B=q,
M=B^(nu+o(1)).                                    (7.1)
```

Equations (5.3)--(5.4) verify the unit-coefficient hypotheses.  Therefore

```text
boxed:
# {(c,d)}
 <= B^( max(nu/2, nu-c) + o(1)).                  (7.2)
```

Here a negative value of `nu-c` simply means the `M/C` term is `O(1)`; the nonnegative square-root term remains.

Once `(c,d)` is fixed, its odd product determines `v_res` up to the usual `B^o(1)` 2-primary decoration by merged s7-27.  More importantly, merged s7-28 now reconstructs

```text
P,Q,
X*Y,
R,J,
S*T,
beta*gamma,
```

and all labelled cell/root completions with only `B^o(1)` multiplicity.  Thus `v_res` is not separately charged.

```text
OPPOSITE_SIGNED_QUOTIENTS_COUNTED_WITHOUT_FIXING_VRES=true.
```

---

## 8. Two-sided exponent ledger

Dyadically let

```text
C=B^(c+o(1)),
u_res=B^(mu+o(1)),
c*d <= B^(nu+o(1)).                               (8.1)
```

By Sections 2 and 1,

```text
c  = 2*theta+2*phi-3/4,
mu <= 2*theta-2*phi,
nu <= 1/4+2*phi-2*theta.                          (8.2)
```

The charged-once count is now

```text
C support:                         B^c
u_res support:                     B^mu
first primitive pair (U,V):        B^(2phi-c)
opposite signed quotient pair:     B^max(nu/2,nu-c)
all remaining reconstruction:      B^o(1).         (8.3)
```

Therefore

```text
E(theta,phi)
 <= c+mu+(2phi-c)+max(nu/2,nu-c).                 (8.4)
```

Use the largest permitted `mu,nu` to obtain

```text
E(theta,phi)
 <= 2*theta
    + max(1/8+phi-theta, 1-4*theta)

 = max(theta+phi+1/8, 1-2*theta).                 (8.5)
```

On the whole surviving strip (1.1),

```text
theta+phi <= 5/16+1/4=9/16,
```

so

```text
theta+phi+1/8 <= 11/16.                           (8.6)
```

Also `theta>=3/16`, hence

```text
1-2*theta <= 5/8 < 11/16.                         (8.7)
```

Thus

```text
boxed:
E(theta,phi) <= 11/16                              (8.8)
```

uniformly on the entire merged common-core strip.

The first branch in (8.5) reaches `11/16` only at

```text
boxed:
theta=5/16,
phi=1/4.                                          (8.9)
```

The second branch never exceeds `5/8`.

---

## 9. Whole-family promotion

Merged mainline `4cp` explicitly promotes the s7-29 common-core strip count to the whole-family theorem chain and proves that the only `3/4` saturation packet is

```text
theta=5/16,
phi=1/4.
```

Stage14-s7-30 does not introduce a narrower relaxed family.  Sections 2--8 strengthen the same charged-once common-core packet uniformly on the entire strip used by `4cp`:

- the same outer common core `C` is retained;
- `u_res` is retained as outer data;
- the first primitive agreement pair is counted exactly as in s7-29;
- `v_res` is replaced, not supplemented, by the second root-pair count;
- all switch/agreement/root products are reconstructed in the same s7-28 quantifier order.

Therefore the mainline promotion composes directly, with no unaccounted sector and no double charge.  We obtain

```text
boxed:
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/16,
IMPROVEMENT_OVER_3_4=1/16,
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true.         (9.1)
```

Equivalently

```text
V(B) << B^(11/16+o(1)).                            (9.2)
```

The gap to the square-root upper-bound scale is now

```text
11/16-1/2=3/16.                                    (9.3)
```

---

## 10. What saturates 11/16

At the unique corner

```text
theta=5/16,
phi=1/4,                                           (10.1)
```

we have exactly

```text
c=3/8,
mu<=1/8,
nu<=1/8,
2phi-c=1/8.                                       (10.2)
```

The second quotient lemma contributes

```text
max(nu/2,nu-c)=1/16,                               (10.3)
```

because `nu-c=-1/4`.  Thus the `M/C` term is negligible; the entire new boundary is the square-root term coming from summing the common gcd

```text
h=gcd(c_k^+,c_k^-).                               (10.4)
```

Merged s7-27 already proves that the odd support of this gcd is contained in the small root product:

```text
boxed:
oddpart(h) | X*Y.                                 (10.5)
```

Therefore the remaining `B^(1/16)` loss is not a generic density problem.  It is a concrete common-gcd/root-product incidence inside the top corner.

Define the next receiver

```text
TopCornerOppositeSignedQuotientCommonGcdRootProductIncidence.  (10.6)
```

A successful s7-31 should exploit the exact reconstruction of `X*Y` together with (10.5), rather than invoke an unrelated genus-one or generic large-sieve theorem.

---

## 11. Relation to 4cp four-root masks

Merged 4cp/X6 record the self-generated quadratic values

```text
F_- = a^2U^2-b^2V^2,
F_+ = a^2U^2+b^2V^2
```

and their real/twisted prime-root masks.  Stage14-s7-30 respects the 4cp guard that these self-generated moduli cannot simply be multiplied into the first determinant-spacing modulus.

The new saving comes from a different legal quantifier move:

```text
first primitive pair
 -> reconstruct opposite agreement product
 -> count the still-moving opposite signed quotient pair
    against the already-fixed outer common core C.
```

Thus no self-generated `alpha*delta` or `S*T` modulus is recharged.

```text
SELF_GENERATED_FOUR_ROOT_MODULI_RECHARGED=false.
```

---

## 12. H / tH decision

No s-side auxiliary H theorem is needed.

The new ingredient is the elementary nonprimitive quadratic-root-pair lemma of Section 6.  The completed reciprocal-Edwards genus-one H audit remains nonminimal, and the merged `tH18/t68` private-canonical-prime route has a different fixed-U Cayley coefficient space.

Do not cross-promote either theorem family into s7-30.

```text
TH18_CROSS_PROMOTED_TO_S7_30=false
T68_CROSS_PROMOTED_TO_S7_30=false
GENERIC_GENUS_ONE_H_USED_BY_S7_30=false
S7_30_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false.               (12.1)
```

Reconsider an s-specific H only if the exact common-gcd/root-product receiver of (10.6) survives further divisor reconstruction.

---

## Stage boundary

```text
STAGE14_S7_30=COMPLETE_TWO_SIDED_COMMON_CORE_QUADRATIC_ROOT_PAIR_COUNT_AND_11_16_BOUND
MERGED_S7_29_IMPORTED=true
MERGED_4CP_THREE_QUARTER_PROMOTION_IMPORTED=true
MERGED_X6_FOUR_ROOT_GUARD_COMPATIBLE=true
COMMON_CORE_SCALE_PINNED=true
COMMON_CORE_SCALE_EXPONENT=2*theta+2*phi-3/4
HK_PLUS_ODDPART_EXPONENT=2*theta
XI_SWITCH_ODDPART_EXPONENT=3/4-2*phi
FIRST_PRIMITIVE_COMMON_CORE_ROOT_LINE_COUNT_REUSED=true
OPPOSITE_AGREEMENT_PRODUCT_RECONSTRUCTED_BEFORE_VRES=true
SECOND_COMMON_CORE_QUADRATIC_CONGRUENCE_PROVED=true
NONPRIMITIVE_QUADRATIC_ROOT_PAIR_LEMMA_PROVED=true
NONPRIMITIVE_QUADRATIC_ROOT_PAIR_BOUND=M^(1/2)+M/C
OPPOSITE_SIGNED_QUOTIENTS_COUNTED_WITHOUT_FIXING_VRES=true
SELF_GENERATED_FOUR_ROOT_MODULI_RECHARGED=false
DYADIC_TWO_SIDED_BLOCK_EXPONENT=max(theta+phi+1/8,1-2*theta)
TWO_SIDED_COMMON_CORE_STRIP_UPPER_BOUND_EXPONENT=11/16
ELEVEN_SIXTEENTHS_SATURATION_REQUIRES_THETA=5/16
ELEVEN_SIXTEENTHS_SATURATION_REQUIRES_PHI=1/4
TOP_CORNER_COMMON_CORE_EXPONENT=3/8
TOP_CORNER_URES_EXPONENT=1/8
TOP_CORNER_OPPOSITE_QUOTIENT_PRODUCT_EXPONENT=1/8
TOP_CORNER_OPPOSITE_QUOTIENT_SQRT_GCD_BOUNDARY_EXPONENT=1/16
OPPOSITE_QUOTIENT_COMMON_GCD_ODDPART_DIVIDES_XY=true
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/16
IMPROVEMENT_OVER_3_4=1/16
CURRENT_GAP_TO_SQRT=3/16
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true
TH18_CROSS_PROMOTED_TO_S7_30=false
T68_CROSS_PROMOTED_TO_S7_30=false
GENERIC_GENUS_ONE_H_USED_BY_S7_30=false
S7_30_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
SQRT_B_UPPER_BOUND_PROVED=false
REMAINING_RECEIVER=TopCornerOppositeSignedQuotientCommonGcdRootProductIncidence
NEXT=Stage14-s7-31
```