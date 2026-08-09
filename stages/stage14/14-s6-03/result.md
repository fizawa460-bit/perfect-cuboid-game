# Stage14-s6-03 — centered quartic auxiliary sieve and small-denominator reduction

## Purpose

Stage14-s6-02 proves a genuine post-local incidence gain when the canonical odd edge-kernel prime is large and its incident square-variable pair is long.  The two apparent complements were

```text
A. tiny/smooth odd kernel,
B. short incident square variables.
```

Stage14-s6-03 removes the dependence on the kernel size altogether.

The key observation is that the two-quadrics witness has **three exact binary-quartic square projections**, one centered at each square variable.  Good auxiliary primes, chosen away from the moving bad support, act on these quartics even when

```text
abc=1.
```

Thus the auxiliary-prime square sieve is not a replacement for the s6-02 edge-prime incidence; it is a complementary global-point mechanism which also sees the tiny-kernel branch.

The stage proves a uniform fixed-packet rectangle saving

```text
min(U,D)^(-1/3+epsilon)
```

for each centered projection.  It also proves an anisotropic forcing lemma

```text
D <= 2 max(|u1|,|u2|),
```

so every witness with large denominator automatically has a long centered square variable.  Consequently the two s6-02 coordinate-level complements collapse to one:

```text
small denominator D.
```

This still does **not** prove a full post-local exponent `delta_post>0` for the number of locally-soluble base/classes.  The reason is a quantifier issue: s5u counts each admissible packet once, whereas the square sieve bounds the density of witness coordinates inside a packet box.  Multiplying those two bounds is not justified without a moving-packet weighted correlation theorem or a canonical-witness incidence count.

No new external analytic input is introduced.  The one-variable quartic Weil bound used below is the same good-auxiliary-prime input already frozen in merged Stage14-t30.

---

## 1. Starting two-quadrics packet

Fix a primitive Pythagorean base

```text
S^2+X^2=H^2
```

and one signed squarefree packet from s6-01:

```text
d0 u0^2 - d1 u1^2 = S^2 D^2,
d2 u2^2 - d0 u0^2 = X^2 D^2.
```

The packet satisfies

```text
d0*d1*d2 = k^2 > 0
```

for an integer `k>0`.

Adding the equations also gives

```text
d2 u2^2 - d1 u1^2 = H^2 D^2.
```

All `di` are nonzero signed squarefree integers supported on the Stage14 bad-prime set and refined by s6-01 to the same five Euclid columns as s5.

---

## 2. Three exact centered quartic projections

### 2.1 Center at `u0`

The two equations give

```text
d1 u1^2 = d0 u0^2 - S^2 D^2,
d2 u2^2 = d0 u0^2 + X^2 D^2.
```

Multiply and use `d0*d1*d2=k^2`:

```text
(k u1 u2)^2
 = d0 (d0 u0^2 - S^2 D^2)(d0 u0^2 + X^2 D^2).
```

Define

```text
Phi0(U,V)
 = d0 (d0 U^2 - S^2 V^2)(d0 U^2 + X^2 V^2).
```

Every witness satisfies

```text
Phi0(u0,D) = square.
```

### 2.2 Center at `u1`

Similarly,

```text
d0 u0^2 = d1 u1^2 + S^2 D^2,
d2 u2^2 = d1 u1^2 + H^2 D^2,
```

so

```text
(k u0 u2)^2
 = d1 (d1 u1^2 + S^2 D^2)(d1 u1^2 + H^2 D^2).
```

Define

```text
Phi1(U,V)
 = d1 (d1 U^2 + S^2 V^2)(d1 U^2 + H^2 V^2).
```

Every witness satisfies `Phi1(u1,D)=square`.

### 2.3 Center at `u2`

Finally,

```text
d0 u0^2 = d2 u2^2 - X^2 D^2,
d1 u1^2 = d2 u2^2 - H^2 D^2,
```

and therefore

```text
(k u0 u1)^2
 = d2 (d2 u2^2 - X^2 D^2)(d2 u2^2 - H^2 D^2).
```

Define

```text
Phi2(U,V)
 = d2 (d2 U^2 - X^2 V^2)(d2 U^2 - H^2 V^2).
```

Every witness satisfies `Phi2(u2,D)=square`.

Hence

```text
THREE_CENTERED_QUARTIC_PROJECTIONS_EXACT=true.
```

This projection is safe for upper bounds: imposing only one centered quartic square condition enlarges the full witness set.

---

## 3. Exact discriminants and good auxiliary primes

For

```text
F(T)=d(d T^2+b)(d T^2+c)
```

the quartic discriminant is

```text
disc_T(F)=16 d^12 b c (b-c)^4.
```

Applying this to the three centered forms gives

```text
disc Phi0(T,1) = -16 d0^12 S^2 X^2 H^8,
disc Phi1(T,1) =  16 d1^12 S^2 H^2 X^8,
disc Phi2(T,1) =  16 d2^12 X^2 H^2 S^8.
```

Therefore every odd prime

```text
lambda not dividing 2*d_i*S*X*H
```

is a good auxiliary prime for the `i`-th centered quartic: the dehomogenized quartic is squarefree modulo `lambda`.

This is the exact analogue of the good-prime/bad-direction-prime separation already frozen in Stage14-t30.

```text
CENTERED_QUARTIC_DISCRIMINANTS_EXACT=true
CENTERED_QUARTIC_GOOD_PRIME_SUPPORT_EXACT=true.
```

The crucial point is that the auxiliary prime need not divide any selected kernel.  Thus

```text
abc=1
```

causes no loss of the auxiliary sieve.

---

## 4. Complete good-prime character correlation

Let `chi_lambda` be the quadratic character modulo a good odd prime `lambda`.

Merged Stage14-t30 already freezes the standard squarefree-quartic Weil estimate

```text
| sum_{t mod lambda} chi_lambda(f(t)) |
 <= 3 sqrt(lambda)
```

for a squarefree quartic `f`.

Apply it to `Phi_i(T,1)`.  The projective point at infinity contributes at most one additional unit, hence

```text
| sum_[U:V] in P1(F_lambda) chi_lambda(Phi_i(U,V)) |
 <= 3 sqrt(lambda)+1.
```

Because `Phi_i` is homogeneous of degree four,

```text
chi_lambda(Phi_i(rU,rV))
 = chi_lambda(r^4) chi_lambda(Phi_i(U,V))
 = chi_lambda(Phi_i(U,V))
```

for `r!=0`.

Therefore the complete affine two-variable sum satisfies

```text
| sum_{U,V mod lambda} chi_lambda(Phi_i(U,V)) |
 <= (lambda-1)(3 sqrt(lambda)+1)
 << lambda^(3/2).
```

For two distinct good primes `lambda,mu`, CRT factorization gives

```text
| sum_{U,V mod lambda*mu}
    chi_{lambda*mu}(Phi_i(U,V)) |
 << (lambda*mu)^(3/2).
```

Relative to the `(lambda*mu)^2` ambient residue pairs, this is a square-root saving.

```text
GOOD_AUXILIARY_HOMOGENEOUS_COMPLETE_CORRELATION=true
GOOD_AUXILIARY_TWO_PRIME_CRT_CORRELATION=true.
```

---

## 5. Incomplete rectangle correlation by complete blocks

Let

```text
|U| ~ Ubox,
V ~ Vbox,
```

be a dyadic rectangle and put `q=lambda*mu` for two good auxiliary primes.

The Jacobi-symbol weight

```text
chi_q(Phi_i(U,V))
```

is periodic modulo `q` in both variables.  Tile the rectangle by complete `q x q` blocks and bound the two boundary strips trivially.  The complete correlation from Section 4 gives

```text
S_q(Ubox,Vbox)
 << Ubox*Vbox*q^(-1/2)
    + (Ubox+Vbox)*q
    + q^2.
```

No incomplete character-sum theorem is required for this bound.

The same block decomposition shows that, for a good prime `lambda`, the number of rectangle pairs with

```text
lambda | Phi_i(U,V)
```

is

```text
<< Ubox*Vbox/lambda
   + Ubox+Vbox+lambda,
```

because a squarefree homogeneous quartic has only `O(lambda)` zero residue pairs modulo `lambda`.

---

## 6. Fixed-packet rectangle square sieve

Let

```text
M = min(Ubox,Vbox).
```

Choose good auxiliary primes in a dyadic prime interval

```text
lambda ~ L,
L = M^(1/3),
```

up to harmless integer rounding.  When `M` is a fixed positive power of `B`, only `O(log B/log L)=O(1)` primes in the interval can divide the bad product

```text
2*d_i*S*X*H,
```

whereas the interval contains `>> L/log L` primes.  Thus deleting the bad primes does not change exponent bookkeeping.

Use the elementary square-sieve expansion over these good primes.  The diagonal term, zero-value term, and the off-diagonal `lambda*mu` correlations from Section 5 give

```text
N_i(Ubox,Vbox)
 <<_epsilon B^epsilon
    [ Ubox*Vbox/L
      + (Ubox+Vbox)L^2
      + L^4 ],
```

where `N_i` counts rectangle pairs for which `Phi_i(U,V)` is an integer square.

With `L=M^(1/3)` and, say, `Ubox>=Vbox=M`, every displayed term is bounded by

```text
B^epsilon Ubox*Vbox*M^(-1/3).
```

Hence

```text
boxed:
N_i(Ubox,Vbox)
 <<_epsilon
 B^epsilon Ubox*Vbox*min(Ubox,Vbox)^(-1/3).
```

This is the fixed-packet auxiliary square-sieve theorem of s6-03.

```text
FIXED_PACKET_RECTANGLE_SQUARE_SIEVE_PROVED=true
FIXED_PACKET_RECTANGLE_SAVING=min(U,D)^(-1/3+epsilon).
```

It applies equally to large, tiny, smooth, or trivial odd kernel packets.

---

## 7. Tiny-kernel complement disappears at coordinate level

The s6-02 edge-prime incidence required a selected prime

```text
ell=P^+(abc)
```

and therefore left `abc=1` or `P^+(abc)<B^eta` as a separate complement.

The centered quartic sieve does not use `ell` at all.  It uses primes outside

```text
2*d_i*S*X*H.
```

Consequently, whenever one centered coordinate and `D` are both long, the same `min(U,D)^(-1/3)` saving holds even for

```text
abc=1.
```

Thus

```text
TINY_KERNEL_COMPLEMENT_CLOSED_AT_COORDINATE_LEVEL=true.
```

This statement is deliberately qualified by `AT_COORDINATE_LEVEL`; Section 10 explains the remaining packet-count quantifier issue.

---

## 8. Anisotropic size forcing: large denominator forces a long square coordinate

Use the eliminated `H`-edge equation

```text
d2 u2^2 - d1 u1^2 = H^2 D^2.
```

From s6-01,

```text
|d1| = |tau1| a c <= 2 S H,
|d2| = |tau2| b c <= 2 X H.
```

Let

```text
Umax=max(|u1|,|u2|).
```

Then

```text
H^2 D^2
 <= |d2| u2^2 + |d1| u1^2
 <= 2H(S+X) Umax^2
 <= 2 sqrt(2) H^2 Umax^2
 < 4 H^2 Umax^2.
```

Therefore

```text
boxed:
D <= 2 max(|u1|,|u2|).
```

In particular, for any fixed `eta>0`,

```text
D >= 2 B^eta
```

forces at least one of `u1,u2` to have size `>=B^eta`.

Choose the corresponding centered quartic `Phi1` or `Phi2`.  On its dyadic box,

```text
min(U_i,D) >= B^eta
```

up to an absolute dyadic constant, so the fixed-packet square sieve gives

```text
B^(-eta/3+epsilon)
```

coordinate-density saving.

Thus the s6-02 short-variable complement is not independent:

```text
SHORT_VARIABLE_COMPLEMENT_REDUCED_TO_SMALL_DENOMINATOR=true.
```

---

## 9. Coordinate-level partition after s6-03

Fix `eta>0`.

Every integral witness packet lies in one of two sectors.

### Sector A — large denominator

```text
D >= 2 B^eta.
```

Then one of `u1,u2` is also `>=B^eta`, and the corresponding centered quartic gives

```text
coordinate box saving >= B^(-eta/3+epsilon).
```

This includes the entire tiny/smooth-kernel branch.

### Sector B — small denominator

```text
D < 2 B^eta.
```

No coordinate-density power saving follows merely from the centered rectangle theorem, because `min(U_i,D)` may be small for every centered projection.

Hence the only remaining **coordinate-level** complement is the small-denominator sector.

```text
ONLY_COORDINATE_LEVEL_COMPLEMENT=SMALL_DENOMINATOR.
```

This is a substantial simplification over the three-way s6-02 complement ledger.

---

## 10. Why this still does not prove a global `delta_post`

It is tempting, but incorrect, to multiply

```text
N_local(B) << B^(41/42+epsilon)
```

by the centered-box factor

```text
B^(-eta/3).
```

The two statements have different quantifiers.

- `N_local(B)` counts each locally-admissible base/state packet **once**.
- the centered square sieve bounds the number of coordinate pairs `(u_i,D)` inside a fixed packet rectangle.

A packet which has one global small point contributes `1` to the existence count even if its ambient coordinate rectangle contains a very small proportion of square values.

Thus

```text
UNWEIGHTED_LOCAL_TO_COORDINATE_SAVING_MULTIPLICATION_JUSTIFIED=false.
```

Equivalently, the inequality

```text
1_{packet has a witness}
 <= number of witness coordinate pairs
```

is safe, but after summing packets the right side carries coordinate-volume weights not present in the s5u unweighted theorem.

This is the exact remaining quantifier gap:

```text
EXISTENCE_VS_COORDINATE_DENSITY_QUANTIFIER_GAP=true.
```

The stage therefore does not claim

```text
J_C(B) << B^(41/42-delta_post+epsilon)
```

for any fixed positive `delta_post`.

---

## 11. Exact moving-family theorem now required

For a dyadic locally-admissible packet family `L` and a centered index `i`, define the joint auxiliary correlation

```text
C_q(L;U,V)
 = sum_{(F,sigma) in L}
   sum_{u~U, D~V}
   w(F,sigma;u,D)
   chi_q(Phi_{i,F,sigma}(u,D)),
```

where `w` retains the full two-quadrics incidence / canonical witness selection needed for the existence problem.

A theorem of the schematic form

```text
C_q
 << ( #L * U * V ) q^(-kappa)
    + controlled boundary
```

uniformly for auxiliary squarefree `q` would allow the square sieve to act **after summing packets**, and would convert the coordinate saving into a genuine post-local class saving.

Because the auxiliary primes are coprime to the five s5 support columns, this is the natural point at which the s5p/s5q auxiliary-progression/Hilbert machinery may be reusable.  However that weighted theorem is not yet proved.

For the small-denominator sector, the next stage must additionally exploit

```text
D < B^eta
```

directly, rather than paying the full generic polynomial denominator box from s6-01.

---

## 12. Status and next stage

Stage14-s6-03 proves:

1. three exact centered binary-quartic square projections;
2. exact quartic discriminants and good-prime set;
3. complete one- and two-prime auxiliary correlations;
4. a fixed-packet rectangle square-sieve saving `min(U,D)^(-1/3+epsilon)`;
5. kernel-size independence of that sieve;
6. the anisotropic inequality `D<=2 max(|u1|,|u2|)`;
7. reduction of all coordinate-level complements to small denominator;
8. the precise existence-vs-coordinate-density quantifier gap preventing a false global exponent claim.

The required square-root budget remains

```text
10/21.
```

No new physical upper-bound exponent is claimed in this stage.

```text
STAGE14_S6_03=COMPLETE_CENTERED_QUARTIC_AUXILIARY_SIEVE_AND_SMALL_DENOMINATOR_REDUCTION
THREE_CENTERED_QUARTIC_PROJECTIONS_EXACT=true
CENTERED_QUARTIC_DISCRIMINANTS_EXACT=true
GOOD_AUXILIARY_PRIME_WEIL_IMPORTED_FROM_T30=true
GOOD_AUXILIARY_HOMOGENEOUS_COMPLETE_CORRELATION=true
GOOD_AUXILIARY_TWO_PRIME_CRT_CORRELATION=true
FIXED_PACKET_RECTANGLE_SQUARE_SIEVE_PROVED=true
FIXED_PACKET_RECTANGLE_SAVING=min(U,D)^(-1/3+epsilon)
KERNEL_SIZE_REQUIRED_FOR_AUXILIARY_SIEVE=false
TINY_KERNEL_COMPLEMENT_CLOSED_AT_COORDINATE_LEVEL=true
D_LARGE_FORCES_LONG_U1_OR_U2=true
SHORT_VARIABLE_COMPLEMENT_REDUCED_TO_SMALL_DENOMINATOR=true
ONLY_COORDINATE_LEVEL_COMPLEMENT=SMALL_DENOMINATOR
UNWEIGHTED_LOCAL_TO_COORDINATE_SAVING_MULTIPLICATION_JUSTIFIED=false
EXISTENCE_VS_COORDINATE_DENSITY_QUANTIFIER_GAP=true
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND=10/21
NEXT=Stage14-s6-04 prove a moving-packet auxiliary-character correlation compatible with the s5u unweighted packet count, while exploiting D<B^eta as the sole coordinate-level exceptional sector
```
