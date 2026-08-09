# Stage14-s6-01 — integral global-small-point witness packetization

## Purpose

Stage14-s6-00 selects the direct post-local global-small-point route.  The starting upper bound is

```text
V(B) <<_epsilon B^(41/42+epsilon),
```

and reaching a square-root upper bound from this input would require a further post-local saving `10/21` on the physical `B` scale.

Stage14-s6-01 does not yet try to prove that saving.  Its task is structural and exact:

> replace the abstract event "a locally-soluble supported class contains a globally rational logarithmically small non-torsion point" by a primitive integral incidence packet with explicit squarefree state, exact gcd support, and polynomial height box.

The result is stronger than a generic denominator-clearing statement.  The three signed squarefree kernels are forced into an edge-packet factorization

```text
d0 = tau0 * a * b,
d1 = tau1 * a * c,
d2 = tau2 * b * c,
```

where

```text
a | rad(S),
b | rad(X),
c | rad(H),
```

and `(tau0,tau1,tau2)` belongs to only sixteen sign/2-adic patterns.  In Euclid coordinates this packet refines exactly to the same five odd support columns used throughout s5:

```text
m, n, m-n, m+n, m^2+n^2.
```

Thus s6 keeps the global point variables without creating a new uncontrolled local state space.

No new external theorem is used.  The only height input is the already-merged Stage14-s3 fixed-degree canonical/naive height comparison.

---

## 1. Direct post-local witness majorant

Fix a primitive oriented Pythagorean first-face base

```text
F=(S,X,H),
S^2+X^2=H^2,
gcd(S,X)=gcd(S,H)=gcd(X,H)=1,
```

with one of `S,X` even and `H` odd.  The integral full-2-torsion model is

```text
E_F : W^2 = Z(Z-S^2)(Z+X^2).
```

Let `C` be a fixed admissible constant in the Stage14-s3 logarithmic canonical-height window.

Define `J_C(B)` to be the number of pairs `(F,xi)` such that

1. `H<=B`;
2. `xi` is a nonzero class in `E_F(Q)/2E_F(Q)` supported on the actual Stage14 bad-prime set;
3. `xi` is globally soluble;
4. `xi` has a non-torsion rational representative `Q` satisfying

```text
hat_h(Q) <= C(log B + log H).
```

The physical reconstruction condition is **not** imposed on `Q`.  This is deliberate: `J_C` is an upper majorant, not an exact physical count.

Every globally soluble class is locally soluble, so the s5u count gives

```text
J_C(B) <= N_local(B).
```

Conversely, a physical hit below `B` gives by s3 a non-torsion point `P` in the same logarithmic height window.  If `P` is 2-divisible, repeatedly halve it until reaching a non-torsion `Q` which is not in `2E_F(Q)`.  Finite generation of `E_F(Q)` makes the process terminate, and

```text
hat_h(2R)=4 hat_h(R)
```

shows that halving never increases canonical height.

Hence each physical active base supplies at least one pair counted by `J_C`, and

```text
boxed: V(B) <= J_C(B) <= N_local(B).
```

This one-sided relaxation is the correct s6 object for upper bounds.

```text
PHYSICAL_RECONSTRUCTION_DROPPED_ONLY_FOR_UPPER_MAJORANT=true.
```

---

## 2. Polynomial rational-coordinate box

Stage14-s3 gives the fixed-family comparison

```text
hat_h(Q) = O(log B + log H)
  => h_Z(Q) = O(log B)
```

uniformly for `H<=B`.  Therefore there is a fixed constant `K_C` such that a representative counted by `J_C(B)` has

```text
H_Z(Q) <= B^K_C.
```

We next prove the exact denominator shape directly from the monic cubic.

Write `Z=A/C0` in lowest terms.  If a prime `p|C0`, then `v_p(Z)<0`, while `S^2,X^2` are integral, so

```text
v_p(Z-S^2)=v_p(Z+X^2)=v_p(Z).
```

Thus

```text
v_p(Z(Z-S^2)(Z+X^2)) = 3 v_p(Z) = -3 v_p(C0).
```

The left side is `W^2`, so it has even valuation.  Therefore every `v_p(C0)` is even.  Hence

```text
C0=D^2,
D>0,
gcd(A,D)=1.
```

The same valuation identity gives

```text
W=Y/D^3
```

with `Y in Z`.  Therefore every witness admits primitive integral coordinates

```text
Z=A/D^2,
W=Y/D^3,
D>0,
gcd(A,D)=1.
```

The height bound gives

```text
|A| <= B^K_C,
D^2 <= B^K_C.
```

Since `S,X,H<=B`, all remaining variables produced below lie in a fixed polynomial box as well.

```text
MONIC_WEIERSTRASS_DENOMINATOR_SQUARE_CUBE_PROVED=true.
```

---

## 3. Exact integral witness equation

Substituting and clearing the denominator `D^6` gives

```text
boxed:
Y^2 = A(A-S^2 D^2)(A+X^2 D^2).
```

Put

```text
G0=A,
G1=A-S^2 D^2,
G2=A+X^2 D^2.
```

Then exactly

```text
G0-G1 = S^2 D^2,
G2-G0 = X^2 D^2,
G2-G1 = H^2 D^2.
```

Because `Q` is non-torsion, none of the three `G_i` is zero; a zero factor would give `W=0`, hence a rational 2-torsion point.

The non-torsion condition itself is retained as part of the witness packet.  s6-01 does not yet classify every additional torsion component which may occur inside later algebraic relaxations.

---

## 4. Pairwise gcd support is exactly on the three Pythagorean edges

Since `gcd(A,D)=1`, every prime dividing `D` is coprime to all three `G_i`: modulo such a prime all `G_i` are congruent to `A`, which is a unit.

Therefore

```text
gcd(G0,G1) | S^2,
gcd(G0,G2) | X^2,
gcd(G1,G2) | H^2.
```

In particular, for odd primes,

```text
supp_odd gcd(G0,G1) subset supp_odd(S),
supp_odd gcd(G0,G2) subset supp_odd(X),
supp_odd gcd(G1,G2) subset supp_odd(H).
```

Because the primitive Pythagorean triple is pairwise coprime, the three odd overlap supports are disjoint.

More precisely, for an odd prime `p`:

- if `p|S`, then `p` can divide `G0,G1` together, but cannot divide `G2`;
- if `p|X`, then `p` can divide `G0,G2` together, but cannot divide `G1`;
- if `p|H`, then `p` can divide `G1,G2` together, but cannot divide `G0`.

This is the exact three-edge support geometry of the global witness.

---

## 5. Signed squarefree kernels

For each nonzero integer factor write uniquely

```text
Gi = di * ui^2,
ui>0,
di signed squarefree.
```

Since

```text
G0 G1 G2 = Y^2,
```

the product

```text
d0 d1 d2
```

is a positive square.

Take an odd prime `p` dividing one of the `d_i`.  The parity of its valuation in the product forces it to divide exactly one other `d_j`.  It cannot occur in all three because the three pairwise gcd supports are disjoint.

Thus every odd prime appearing in the signed kernel triple lies in one of the three pair packets:

```text
01 packet: p|S,
02 packet: p|X,
12 packet: p|H.
```

Consequently the complete odd squarefree kernel is supported on `SXH`, and including the prime `2` gives

```text
boxed:
rad(d0 d1 d2) | 2 S X H.
```

This proves the exact global analogue of the s5 bad-prime support restriction; it is not merely a local necessary condition.

---

## 6. Exact odd edge-packet factorization

Define positive odd squarefree integers

```text
a = product of odd p occurring in both d0,d1,
b = product of odd p occurring in both d0,d2,
c = product of odd p occurring in both d1,d2.
```

Then

```text
a | rad(S),
b | rad(X),
c | rad(H),
gcd(a,b)=gcd(a,c)=gcd(b,c)=1.
```

Remove these odd parts from the signed kernels.  The remaining factors are supported only at the sign and prime `2`, so there are unique

```text
taui in {+1,-1,+2,-2}
```

such that

```text
boxed:
d0 = tau0 * a * b,
d1 = tau1 * a * c,
d2 = tau2 * b * c.
```

The condition that `d0d1d2` is a positive square is equivalent to

```text
tau0 tau1 tau2 is a positive square.
```

Among the `4^3=64` raw triples in `{+-1,+-2}^3`, this means

- the product of the three signs is positive;
- the number of even `tau_i` is even.

Hence there are exactly

```text
4 sign patterns * 4 even-2-support patterns = 16
```

admissible `(tau0,tau1,tau2)` patterns.

Therefore the entire signed squarefree state of a global small-point witness consists of

```text
one of 16 finite 2/sign packets
+ a|rad(S)
+ b|rad(X)
+ c|rad(H).
```

No uncontrolled new state family appears.

---

## 7. Exact refinement to the five s5 Euclid columns

Write the primitive Pythagorean base in Euclid form

```text
S=2mn,
X=m^2-n^2=(m-n)(m+n),
H=m^2+n^2,
```

with

```text
m>n>0,
gcd(m,n)=1,
m,n opposite parity.
```

At odd primes the five factors

```text
m,
n,
m-n,
m+n,
m^2+n^2
```

have pairwise disjoint support.

Therefore the packet divisors split uniquely as

```text
a = a_A a_B,
a_A | rad(m),
a_B | rad(n),

b = b_C b_D,
b_C | rad(m-n),
b_D | rad(m+n),

c = c_E,
c_E | rad(m^2+n^2).
```

These are exactly the five moving odd support columns of s5:

```text
A=m,
B=n,
C=m-n,
D=m+n,
E=m^2+n^2.
```

Thus s6-01 proves a precise handoff:

```text
closed s5 local state
  -> same five-column squarefree support
  + actual global square variables (u0,u1,u2,D).
```

The global point variables, not a new local state explosion, are the new analytic content of s6.

---

## 8. Fixed packet is an explicit intersection of two quadrics

Substitute the packet factorization into the three factor differences.  A fixed packet

```text
sigma=(tau0,tau1,tau2,a,b,c)
```

satisfies

```text
boxed:
tau0*a*b*u0^2 - tau1*a*c*u1^2 = S^2 D^2,
```

```text
boxed:
tau2*b*c*u2^2 - tau0*a*b*u0^2 = X^2 D^2.
```

The third equation

```text
tau2*b*c*u2^2 - tau1*a*c*u1^2 = H^2 D^2
```

follows by addition and `S^2+X^2=H^2`.

For fixed `(S,X,H,sigma)` this is a complete intersection of two diagonal quadrics in the four square variables

```text
(u0,u1,u2,D).
```

The exact primitive denominator condition also gives

```text
gcd(D, d_i u_i)=1
```

for each `i`; in particular

```text
gcd(D,abc*u0*u1*u2)=1.
```

If any `tau_i` is even, then `D` is automatically odd.

This is the first fully integral s6 incidence object.

---

## 9. Polynomial witness box

From Section 2,

```text
|A| <= B^K_C,
D^2 <= B^K_C.
```

Also

```text
|Gi|
 <= |A| + B^2 D^2
 << B^(K_C+2).
```

Since `|di|>=1`,

```text
ui^2 <= |Gi| << B^(K_C+2),
ui << B^((K_C+2)/2).
```

And trivially

```text
a,b,c <= B.
```

Hence all variables of the fixed-packet two-quadrics system lie in a fixed polynomial box in `B`.  Dyadic decomposition therefore costs only a power of `log B`, absorbable into `B^epsilon`.

The exact exponent `K_C` is not optimized because s6-01 only needs polynomial boundedness before choosing the incidence theorem.

---

## 10. Counting interface and multiplicity

Let `I_C(B)` be the set of tuples

```text
(S,X,H;
 tau0,tau1,tau2;
 a,b,c;
 u0,u1,u2,D)
```

satisfying

- primitive Pythagorean base conditions;
- the sixteen-state sign/2-adic rule;
- `a|rad(S), b|rad(X), c|rad(H)`;
- the two exact quadratic equations;
- primitive denominator coprimality;
- polynomial height box;
- nonzero/non-torsion witness condition corresponding to a nonzero mod-2 class.

Then every pair counted by `J_C(B)` maps to at least one tuple in `I_C(B)`.  Conversely the raw two-quadrics equations alone may contain nonphysical or torsion algebraic components, so s6 keeps the inclusion in the safe direction:

```text
V(B) <= J_C(B) <= #I_C(B).
```

The sign of `Y` and the signs of square roots create only a fixed multiplicity.  The squarefree support refinements along the five Euclid columns are divisor-many, hence `B^epsilon` on exponent scale.

Therefore proving any bound

```text
#I_C(B) << B^(41/42-delta+epsilon)
```

with `delta>0` gives the first genuine s6 post-local saving.

---

## 11. What s6-01 closes and what remains

Closed here:

1. direct post-local witness majorant;
2. maximal-halving injection to a nonzero mod-2 small point;
3. exact square/cube denominator form;
4. primitive integral cubic witness equation;
5. exact pairwise bad-prime support;
6. exact signed squarefree kernel edge packets;
7. finite sixteen-state sign/2-adic classification;
8. exact refinement to the five s5 Euclid columns;
9. fixed-packet intersection-of-two-quadrics form;
10. polynomial height box.

Not closed here:

- algebraic classification/removal of every torsion and boundary component of the relaxed incidence variety;
- dyadic determinant geometry after eliminating one square variable;
- a canonical large-prime visible/invisible/smooth split for this exact witness system;
- any positive post-local exponent;
- the `10/21` saving required for a square-root upper bound.

Those are the tasks of s6-02 and later stages.

---

## Boundary

```text
STAGE14_S6_01=COMPLETE_INTEGRAL_GLOBAL_SMALL_POINT_WITNESS_PACKETIZATION
S6_DIRECT_WITNESS_MAJORANT_JC_DEFINED=true
PHYSICAL_BASE_TO_NONZERO_MOD2_SMALL_WITNESS_INJECTION=true
PHYSICAL_RECONSTRUCTION_DROPPED_ONLY_FOR_UPPER_MAJORANT=true
MONIC_WEIERSTRASS_DENOMINATOR_SQUARE_CUBE_PROVED=true
INTEGRAL_WITNESS_EQUATION_EXACT=true
WITNESS_FACTOR_DIFFERENCE_IDENTITIES_EXACT=true
PAIRWISE_ODD_GCD_SUPPORT_EXACT=true
SIGNED_SQUAREFREE_KERNEL_SUPPORTED_ON_2SXH=true
ODD_KERNEL_EDGE_PACKET_FACTORIZATION=true
KERNEL_PACKET_FORM=d0=tau0*a*b,d1=tau1*a*c,d2=tau2*b*c
TWO_ADIC_SIGN_PACKET_COUNT=16
FIVE_EUCLID_COLUMN_REFINEMENT_EXACT=true
FIXED_PACKET_TWO_QUADRIC_SYSTEM_EXACT=true
PRIMITIVE_DENOMINATOR_COPRIMALITY_EXACT=true
POLYNOMIAL_WITNESS_BOX_PROVED=true
GLOBAL_POINT_VARIABLES_RETAINED=true
NON_TORSION_PREDICATE_RETAINED=true
ALGEBRAIC_TORSION_COMPONENT_CLASSIFICATION_PROVED=false
DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
S6_01_SUBSTAGE_SPLIT_REQUIRED=false
NEXT=Stage14-s6-02 dyadically decompose the fixed-packet two-quadrics system, classify/remove torsion and boundary components, eliminate one square variable, and isolate the determinant geometry for the canonical large-prime incidence attack
```
