# Stage14-X6 — top-theta singular elimination and primitive four-root CRT reduction

## Status

`COMPLETE_TOP_THETA_SINGULAR_ELIMINATION_AND_PRIMITIVE_FOUR_ROOT_CRT_REDUCTION`

Stage14-X6 consumes merged `X5`, merged `s7-28`, merged `4cg`, and the compatible algebraic part of merged `4cn`.

There are two new conclusions.

1. The only positive singular ratio specialization found in X5/4cn/s7-28, namely `lambda=4`, is **empty on the actual top-theta physical collision packet**.  The proof uses the old common-core plus-factor coupling and squarefree-kernel parity, not a finite search.
2. After the primitive-pair reconstruction of s7-28, the remaining one-pair receiver admits an exact primewise four-root description.  Away from fixed coefficient support, primes from the reconstructed `k`-agreement quadratic value lie on the two real projective roots, while primes from the `xi`-switch plus value lie on the two square-roots of `-1` twists.  The two moving supports are disjoint outside fixed bad primes.

No whole-family power saving is claimed.  The unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

No canonical index or global exponent ledger is modified.

---

## 1. Imported charged-once packet

Keep the balanced common-core packet

```text
xi cells: R,S,T,J,
k cells:  alpha,beta,gamma,delta,
```

with

```text
Xi_switch = S*T,
Xi_agree  = R*J,
K_switch  = beta*gamma,
K_agree   = alpha*delta.
```

The four cells on each side are pairwise-coprime squarefree cells, and

```text
gcd(xi,k)=1.
```

Put, as in s7-28,

```text
r=r_1*r_2,
s=s_1*s_2,
X=x_1*x_2,
Y=y_1*y_2,

A=alpha*r,
D=delta*s,
P=R*X,
Q=J*Y,
```

so

```text
D>A>0,
Q>P>0.
```

The common-core hosts are

```text
H_k^+  = D^2+A^2,
H_k^-  = D^2-A^2,
H_xi^+ = Q^2+P^2,
H_xi^- = Q^2-P^2.
```

Merged 4cg proves the exact plus-factor coupling

```text
boxed:
(g_1*g_2) K_switch H_k^+
 = 2 Xi_switch H_xi^+,                         (1.1)
```

where `g_i in {1,2}`.  Hence `g_1*g_2` is a power of two.

Merged s7-28 fixes, up to `B^o(1)` residual/quotient/small decoration, one primitive xi-agreement modulus pair

```text
u=L_x^+,
v=L_x^-,
gcd(u,v)=1.                                      (1.2)
```

Write the full xi signed quotients

```text
a=c_x^+,
b=c_x^-.
```

Then

```text
D+A=a*u,
D-A=b*v,                                          (1.3)
```

and

```text
D=(a*u+b*v)/2,
A=(a*u-b*v)/2.                                    (1.4)
```

---

## 2. Imported singular relation

X5, 4cn and s7-28 independently identify the only possible positive singular specialization of the reciprocal `(2,2)` ratio family:

```text
lambda=4.
```

On a physical point this is equivalent to

```text
boxed:
D*(Q-P)=A*(Q+P),                                  (2.1)
```

or

```text
boxed:
Q*(D-A)=P*(D+A).                                  (2.2)
```

X5 left this as a rational singular subreceiver.  X6 now puts (2.2) back into the common-core coupling (1.1).

---

## 3. Singular relation forces a squarefree-kernel square identity

From (2.2),

```text
P*(D+A)=Q*(D-A).                                  (3.1)
```

Therefore

```text
P^2*(D+A)^2=Q^2*(D-A)^2.                         (3.2)
```

Now compute

```text
H_xi^+*(D+A)^2
 = (Q^2+P^2)*(D+A)^2
 = Q^2*(D+A)^2 + Q^2*(D-A)^2
 = 2 Q^2*(D^2+A^2)
 = 2 Q^2*H_k^+.                                   (3.3)
```

Substitute (3.3) into the exact common-core coupling (1.1).  Since `H_k^+>0`, cancellation gives

```text
boxed:
(g_1*g_2) K_switch (D+A)^2
 = 4 Xi_switch Q^2.                               (3.4)
```

Using (3.1) symmetrically also gives

```text
boxed:
(g_1*g_2) K_switch (D-A)^2
 = 4 Xi_switch P^2.                               (3.5)
```

These are exact physical identities on any singular packet.

---

## 4. Odd valuation parity kills both switched kernels

Strip powers of two from (3.4).  Since `g_1*g_2` and `4` are powers of two,

```text
oddpart(K_switch) * square
 = oddpart(Xi_switch) * square.                   (4.1)
```

Both switched products are squarefree.  Moreover

```text
gcd(K_switch,Xi_switch)=1                         (4.2)
```

because `K_switch|k`, `Xi_switch|xi`, and `gcd(k,xi)=1`.

Let an odd prime `p|K_switch`.  In (3.4), its valuation on the left is

```text
1 + an even number,
```

while `p` does not divide `Xi_switch`, so its valuation on the right is even.  Contradiction.

Thus

```text
oddpart(K_switch)=1.                              (4.3)
```

The same argument with the two sides reversed gives

```text
oddpart(Xi_switch)=1.                             (4.4)
```

Hence every singular physical packet would have

```text
boxed:
K_switch in {1,2},
Xi_switch in {1,2}.                               (4.5)
```

This is an exact parity theorem; no size estimate has yet been used.

---

## 5. The top-theta singular branch is empty

The only unsaved edge imported from s7-25/s7-28 is

```text
theta=5/16,
3/16 <= phi <= 1/4.                               (5.1)
```

On this edge the balanced cells have

```text
beta,gamma = B^(3/16+o(1)),
```

so

```text
K_switch=beta*gamma=B^(3/8+o(1)).                 (5.2)
```

Likewise

```text
S,T=B^(3/8-phi+o(1)),
```

hence

```text
Xi_switch=S*T
 = B^(3/4-2phi+o(1))
 >= B^(1/4-o(1)).                                  (5.3)
```

Removing the possible single factor two does not change either exponent.  Therefore (4.5) is incompatible with every top-theta dyadic block for sufficiently large `B`.

Thus

```text
boxed:
TOP_THETA_LAMBDA4_SINGULAR_BRANCH_EMPTY=true.      (5.4)
```

Equivalently,

```text
TopThetaCayleySingularCrossRoleIncidence = 0        (5.5)
```

up to the finite initial range absorbed in the implied constant.

This explains the zero `lambda=4` hits in the finite X5 audit, but the finite observation is not used in the proof.

---

## 6. Cross-route consequence for the smooth genus-one envelope

Merged 4cn calls the remaining nonsingular ratio family a physical reciprocal Edwards genus-one problem and requests an independent H audit.

Merged s7-28 subsequently restores the original reciprocal equations and proves a stronger quantifier statement:

```text
fixed residual + quotient + small decoration
-> choose one primitive pair (u,v)
-> reconstruct the opposite agreement product
-> divisor-many opposite split
-> reconstruct P,Q and X*Y
-> divisor-many physical completion.              (6.1)
```

In particular `X*Y`, and hence the Edwards coefficient `lambda`, is not a legal independent outer coefficient before `(u,v)` is chosen.

Therefore X6 records the cross-route adjudication

```text
FIXED_LAMBDA_GENUS_ONE_SLICE_VALID=true,
FIXED_LAMBDA_GENUS_ONE_SLICE_MINIMAL_FOR_X_ROUTE=false.   (6.2)
```

A genus-one H result may remain useful as an auxiliary corollary if it is proved on the exact physical coefficient family, but X6 does not charge it as the primary receiver and does not wait for it.

---

## 7. Two exact quadratic values on the primitive pair

With (1.3), define

```text
F_-(u,v) := a^2*u^2-b^2*v^2,
F_+(u,v) := a^2*u^2+b^2*v^2.                       (7.1)
```

The first reciprocal equation of s7-28 gives

```text
boxed:
F_-(u,v)
 = 4*r*s*epsilon_k*N_k,                            (7.2)
```

where

```text
N_k=L_k^-L_k^+=oddpart(alpha*delta).                (7.3)
```

Thus `N_k` is squarefree.

For the plus value,

```text
F_+(u,v)=2(D^2+A^2)=2H_k^+.                        (7.4)
```

Merged common-core reconstruction gives

```text
boxed:
oddpart(F_+)
 = C*oddpart(S*T).                                 (7.5)
```

So the remaining primitive-pair problem simultaneously prescribes the moving squarefree kernel of a difference of two squares and the physical `xi`-switch part of a sum of two squares.

---

## 8. The two quadratic values have only fixed common support

Put

```text
U=a*u,
V=b*v.
```

Since `gcd(u,v)=1`,

```text
gcd(U,V) | a*b.                                    (8.1)
```

After dividing by `g=gcd(U,V)`, the two integers `U/g` and `V/g` are coprime.  Hence

```text
gcd((U/g)^2-(V/g)^2,
    (U/g)^2+(V/g)^2) | 2.
```

Multiplying back by `g^2` gives

```text
boxed:
gcd(F_-,F_+) | 2*a^2*b^2.                         (8.2)
```

Therefore every odd prime shared by the two quadratic values lies in the fixed quotient support `a*b`.

In particular, outside

```text
Bad := primes dividing 2*a*b*r*s*C,                (8.3)
```

the moving `k`-agreement support from `N_k` and the moving `xi`-switch support from `S*T` are disjoint.

---

## 9. Primewise real roots for the difference value

Let `p` be an odd prime such that

```text
p | N_k,
p does not divide 2*a*b*r*s*C.                    (9.1)
```

Because `N_k` is squarefree and `p∤r*s`, equation (7.2) gives

```text
v_p(F_-)=1.                                        (9.2)
```

Also `p∤u*v`: if, for example, `p|u`, then primitivity gives `p∤v`, and `p∤b`, so `F_-` is nonzero modulo `p`.

Thus `u/v` is defined modulo `p`, and

```text
(a*u)^2=(b*v)^2 (mod p).
```

Therefore

```text
boxed:
u/v = +b/a or -b/a (mod p).                     (9.3)
```

The valuation-one statement (9.2) says that the physical squarefree kernel uses a simple root rather than an unrestricted `p^2` lift.

---

## 10. Primewise imaginary roots for the plus value

Let `p` be an odd prime such that

```text
p | S*T,
p does not divide 2*a*b*r*s*C.                    (10.1)
```

By (7.5) and `p∤C`,

```text
p | F_+(u,v).                                      (10.2)
```

Again `p∤u*v`.  Hence

```text
(a*u)^2=-(b*v)^2 (mod p).                          (10.3)
```

Consequently `-1` is a quadratic residue modulo `p`, so

```text
boxed:
p=1 (mod 4).                                      (10.4)
```

For either square root `i_p^2=-1 (mod p)`,

```text
boxed:
u/v = +i_p*b/a or -i_p*b/a (mod p).             (10.5)
```

Thus the moving plus-value support occupies the two quadratic-twist roots, distinct from the two real roots in (9.3).

---

## 11. Exact four-root CRT receiver

Outside the fixed bad support, every physical primitive pair is decorated primewise by four disjoint projective root classes:

```text
k-agreement / F_- :  +b/a, -b/a,
xi-switch  / F_+ :  +i*b/a, -i*b/a.               (11.1)
```

The first two occur at the squarefree primes of `oddpart(alpha*delta)` outside `r*s`; the second two occur at `xi`-switch primes outside `C`, necessarily `1 mod 4`.

All original data remain charged once:

```text
- fixed common-core residual triple;
- divisor-many full signed quotient quadruple;
- endpoint-small roots and 2-primary decoration;
- primitive pair gcd(u,v)=1;
- balanced cell windows;
- squarefree/coprime cell masks;
- opposite-product and root reconstruction of s7-28;
- original interval/orientation/reconstruction masks.
```

Define the new minimal X receiver

```text
TopThetaPrimitiveAgreementFourRootCRTQuadraticValueIncidence.  (11.2)
```

It asks for a fixed-power saving in the number of primitive `(u,v)` whose two coupled quadratic values admit these simultaneous physical prime allocations.

This is narrower than the ambient smooth genus-one ratio curve and narrower than an unrestricted pair of binary quadratic forms.

---

## 12. What is not yet proved

X6 does **not** prove that the four-root CRT structure alone yields a fixed-power saving.  In particular the moving prime products `N_k` and `S*T` are reconstructed from `(u,v)` rather than fixed before it, so one may not simply apply a fixed-modulus CRT count and multiply independent modulus savings.

Still open:

```text
- average scarcity of primitive pairs with the simultaneous real/twisted root allocations;
- optimal treatment of primes in the fixed bad support 2*a*b*r*s*C;
- exploitation of valuation-one squarefree roots on F_- and the squarefree xi-switch support on F_+;
- a fixed-power saving on the top-theta edge.
```

The whole-family exponent therefore remains `7/8`.

---

## 13. H / tH decision

No new X6-specific H line is needed.

The singular rational branch is eliminated exactly before any average theorem.  The smooth fixed-`lambda` genus-one family is a valid derived envelope but is not the minimal X coefficient space after merged s7-28.

The next useful step is to attack the primewise four-root receiver directly by squarefree-value / root-sieve / CRT methods while preserving the reconstructed-modulus quantifier order.

```text
X6_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_CROSS_PROMOTED_TO_X6=false.
```

If X7 leaves a genuine average theorem, its object should be the precise primitive four-root quadratic-value incidence, not the generic Edwards family.

---

## Stage boundary

```text
STAGE14_X6=COMPLETE_TOP_THETA_SINGULAR_ELIMINATION_AND_PRIMITIVE_FOUR_ROOT_CRT_REDUCTION
MERGED_X5_IMPORTED=true
MERGED_S7_28_IMPORTED=true
MERGED_4CG_IMPORTED=true
MERGED_4CN_COMPATIBILITY_AUDITED=true
X1_CHARGED_ONCE_QUANTIFIER_ORDER_PRESERVED=true
SINGULAR_CROSS_ROLE_RELATION_IMPORTED=true
SINGULAR_PLUS_COUPLING_SQUARE_IDENTITY_PROVED=true
SINGULAR_MINUS_COUPLING_SQUARE_IDENTITY_PROVED=true
SINGULAR_FORCES_ODDPART_K_SWITCH=1
SINGULAR_FORCES_ODDPART_XI_SWITCH=1
TOP_THETA_LAMBDA4_SINGULAR_BRANCH_EMPTY=true
TOP_THETA_CAYLEY_SINGULAR_CROSS_ROLE_INCIDENCE_PROVED_ZERO=true
FIXED_LAMBDA_GENUS_ONE_SLICE_VALID=true
FIXED_LAMBDA_GENUS_ONE_SLICE_MINIMAL_FOR_X_ROUTE=false
PRIMITIVE_DIFFERENCE_QUADRATIC_VALUE_EXACT=true
PRIMITIVE_PLUS_QUADRATIC_VALUE_EXACT=true
PRIMITIVE_PLUS_MINUS_GCD_DIVIDES=2*a^2*b^2
OUTSIDE_FIXED_BAD_SUPPORT_MOVING_KERNELS_DISJOINT=true
K_AGREEMENT_GOOD_PRIME_ROOTS=+b/a,-b/a
XI_SWITCH_GOOD_PRIME_ROOTS=+i*b/a,-i*b/a
XI_SWITCH_GOOD_PRIMES_ARE_1_MOD_4=true
TOP_THETA_PRIMITIVE_AGREEMENT_FOUR_ROOT_CRT_QUADRATIC_VALUE_INCIDENCE_PROVED=false
REMAINING_RECEIVER=TopThetaPrimitiveAgreementFourRootCRTQuadraticValueIncidence
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
X6_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
GENERIC_GENUS_ONE_H_CROSS_PROMOTED_TO_X6=false
NEXT_RECOMMENDED=Stage14-X7
```
