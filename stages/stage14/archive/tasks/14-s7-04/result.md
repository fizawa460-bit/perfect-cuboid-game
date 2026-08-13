# Stage14-s7-04 — separate small-denominator projection audit and joint two-denominator receiver

## Purpose

Stage14-s7-03 replaces the first physical small-point height by the exact multiplicative coordinate height

```text
H_mult = D_u D_x,
```

where, for primitive half-angle pairs `(a,b)` and `(c,d)`,

```text
u = bc/(ad),
w = ac/(bd),
D_u = denom(u),
D_x = denom(w).
```

A physical hit below `B` implies `D_u D_x <= 2B`.  The natural first attempt is therefore a hyperbola split:

```text
D_u <= L
or
D_x <= 2B/L.
```

This stage tests that strategy exactly.

The result is a useful negative/redirecting theorem:

> each **fixed coordinate** fiber is indeed a smooth genus-one quartic and has only `B^o(1)` bounded-height directions, but there are quadratically many reduced rational coordinates of denominator at most `L`.  The two separate projection estimates therefore optimize only at `B^(1+o(1))` and cannot reproduce the already-merged Stage14-4bq bound `B^(61/63+o(1))`.

The correct receiver must keep the two denominators together.  In reduced coordinates

```text
u=P/Q,
w=R/S,
```

the physical first-point problem becomes the joint system

```text
0 < R/S < P/Q < 1,
PR/(QS) is a rational square,
(Q^2-P^2)(S^2-R^2) is an integer square,
QS <= O(B).
```

Equivalently, the two difference-of-squares have the same squarefree kernel.  This joint collision, not either one-coordinate projection by itself, is the next s7 counting object.

No new whole-family exponent is claimed here.

---

## 1. Merged inputs

### 1.1 s7-03 multiplicative first-point height

For a physical pair, s7-03 proves

```text
u = bc/(ad),
w = ac/(bd),
H_mult = D_u D_x,
(1/2) H_mult <= d_rec <= 4 H_mult.
```

Hence, directionwise, first physical height and first multiplicative height have the same power exponent.  In particular

```text
physical hit d_rec <= B
=> D_u D_x <= 2B.
```

### 1.2 s7-02 positive-rank gate

Every physical nonboundary point has infinite order.  Thus

```text
physical activation => positive rank specialization.
```

The converse remains false: positive rank alone does not force a point in the multiplicative-height window.

### 1.3 merged 4bq current whole-family baseline

Merged Stage14-4bq proves

```text
V(B) << B^(61/63+o(1)).
```

Therefore an s7 counting device is useful only if it can ultimately beat an exponent strictly below `1`; in particular, a projection estimate of order `B^(1+o(1))` is not competitive with the current merged theorem.

---

## 2. Cross-gcd coordinates behind the two denominators

Define the four cross cells

```text
q_ac = gcd(a,c),
q_ad = gcd(a,d),
q_bc = gcd(b,c),
q_bd = gcd(b,d).
```

Because

```text
gcd(a,b)=gcd(c,d)=1,
```

the four cross cells are pairwise coprime.  Write the residual cores

```text
a = q_ac q_ad a0,
b = q_bc q_bd b0,
c = q_ac q_bc c0,
d = q_ad q_bd d0.
```

The reduced-coordinate gcds are

```text
gcd(bc,ad) = q_ac q_bd,
gcd(ac,bd) = q_ad q_bc.
```

Therefore the two denominators from s7-03 simplify exactly to

```text
boxed:
D_u = q_ad^2 a0 d0,
D_x = q_bd^2 b0 d0.                       (2.1)
```

This is useful structurally: a small coordinate denominator is a small **one-cell-square times normalized-core product**.  But it is not a direction-only rarity statement; the relevant cell contains partner data.

The product is

```text
D_u D_x
 = q_ad^2 q_bd^2 a0 b0 d0^2
 = ab d^2 / gcd(ab,cd),
```

agreeing with s7-03.

---

## 3. Fixing `u`: an exact genus-one direction fiber

Let

```text
u=P/Q,
0<P<Q,
gcd(P,Q)=1.
```

For a direction

```text
r=a/b,
gcd(a,b)=1,
0<a<b,
```

the second coordinate is

```text
w=r^2 u = P a^2/(Q b^2).
```

The Jacobi equation is

```text
v^2=(1-u^2)(1-w^2).
```

After clearing denominators,

```text
boxed:
Y^2=(Q^2-P^2)(Q^2 b^4-P^2 a^4),          (3.1)
```

with

```text
Y=Q^2 b^2 v.
```

For `0<P<Q`, the binary quartic

```text
(Q^2-P^2)(Q^2 b^4-P^2 a^4)
```

has four distinct geometric roots.  Its smooth projective model is genus one.

The merged Stage14 bounded-height genus-one mechanism used in t22/4bq therefore gives, for fixed reduced `u`, only

```text
B^o(1)
```

primitive direction slopes `a/b` in the Stage14 polynomial height range.

This is the strongest fixed-`u` conclusion needed here.

---

## 4. Fixing `w`: the symmetric genus-one direction fiber

Now let

```text
w=R/S,
0<R<S,
gcd(R,S)=1.
```

Since

```text
u=w/r^2 = R b^2/(S a^2),
```

the same Jacobi equation becomes

```text
boxed:
Z^2=(S^2-R^2)(S^2 a^4-R^2 b^4),          (4.1)
```

where

```text
Z=S^2 a^2 v.
```

Again the quartic is smooth of genus one for `0<R<S`.  Thus a fixed reduced `w` also supports at most

```text
B^o(1)
```

bounded-height primitive directions.

So **both separate fibers are analytically thin**.  The failure below comes entirely from the number of possible projection values.

---

## 5. Quadratic size of each rational projection space

The number of reduced fractions in `(0,1)` with denominator at most `L` is

```text
sum_{q<=L} phi(q) < L^2.
```

Combining this with the fixed-fiber genus-one bound gives the separate projection estimates

```text
N_u(L) << L^(2+o(1)),
N_w(M) << M^(2+o(1)).                       (5.1)
```

Here `N_u(L)` counts directions which possess an admissible nonboundary point with `D_u<=L`; `N_w(M)` is the analogous count with `D_x<=M`.

These estimates deliberately retain no joint relation between `u` and `w` beyond the existence of a point in the corresponding one-coordinate fiber.

---

## 6. The naive hyperbola split has exponent ceiling `1`

From s7-03,

```text
D_u D_x <= 2B.
```

For any `L>=1`, every physical hit lies in

```text
D_u<=L
or
D_x<=2B/L.
```

Applying (5.1),

```text
A_phys(B)
 << B^o(1) [ L^2 + (B/L)^2 ].              (6.1)
```

Constants such as `2` are irrelevant at power scale.

Put

```text
L=B^alpha.
```

The exponent delivered by (6.1) is

```text
max(2 alpha, 2-2 alpha).
```

It is minimized at

```text
alpha=1/2,
```

where the exponent is exactly

```text
boxed: 1.                                      (6.2)
```

Thus the route

```text
separate rational projection count
+ fixed-coordinate genus-one multiplicity
+ hyperbola split
```

only proves

```text
A_phys(B) << B^(1+o(1)).
```

This does **not** improve the merged `61/63` whole-family exponent.  It is also weaker than the older `41/42` bound.

This is a method boundary, not a lower bound on the true count: a stronger theorem may certainly use additional arithmetic structure.  The point is that the additional structure must couple the two coordinates; it cannot be discarded before the count.

---

## 7. Exact joint reduced-coordinate receiver

Write the two physical rational coordinates in lowest terms:

```text
u=P/Q,
w=R/S,
```

with

```text
0<R/S<P/Q<1,
gcd(P,Q)=gcd(R,S)=1.
```

The multiplicative height is exactly

```text
boxed:
H_mult=Q S.                                    (7.1)
```

### 7.1 Rational direction and partner slope

Recall

```text
u=x/r,
w=rx.
```

Therefore

```text
uw=x^2,
w/u=r^2.
```

But

```text
(w/u)/(uw)=1/u^2
```

is automatically a rational square.  Hence the two rational-square conditions are equivalent: it is enough to require

```text
boxed:
PR/(QS) in Q^{x2}.                            (7.2)
```

Then

```text
x = sqrt(PR/(QS)),
r = sqrt(RQ/(SP))
```

are rational.  The ordering `0<w<u<1` gives

```text
0<x<r<1,
```

which is exactly the positive physical slope orientation.

### 7.2 The remaining Jacobi square condition

The Jacobi equation gives

```text
v^2
 = (Q^2-P^2)(S^2-R^2)/(Q^2 S^2).
```

Since the denominator is already a square, rational `v` is equivalent to

```text
boxed:
(Q^2-P^2)(S^2-R^2)=T^2                    (7.3)
```

for an integer `T>0`.

Equivalently,

```text
boxed:
ker(Q^2-P^2)=ker(S^2-R^2),                    (7.4)
```

where `ker` denotes the positive squarefree kernel.

Thus the full first-point receiver on the rational-coordinate side is

```text
0<R/S<P/Q<1,
PR/(QS) rational square,
ker(Q^2-P^2)=ker(S^2-R^2),
QS <= O(B).                                    (7.5)
```

This keeps precisely the two arithmetic couplings lost by the separate projection count.

---

## 8. Relation to the physical cutoff

Let `A_joint(X)` count primitive directions admitting a nonboundary joint tuple (7.5) with

```text
QS<=X
```

and with the Stage14 primitive/orientation conditions inherited after reconstructing `r` and `x`.

The s7-03 absolute comparison gives

```text
A_joint(B/4)
 <= A_phys(B)
 <= A_joint(2B),                               (8.1)
```

up to the already-frozen finite orientation convention.

Therefore `A_joint` and the physical active-direction count have the same power exponent.

The s7 problem is now a **joint denominator hyperbola plus squareclass collision** problem, not a pair of one-dimensional small-denominator problems.

---

## 9. Updated exponent ledger

At branch creation the latest merged whole-family theorem is 4bq:

```text
CURRENT_MERGED_PHYSICAL_EXPONENT = 61/63.
```

The separate-projection route of Sections 3--6 yields exponent

```text
1,
```

so it is discarded as a primary power-saving route.

The square-root target remains

```text
1/2.
```

No exponent improvement is claimed in s7-04.

An independently running 4br branch may improve the main-line baseline further; s7-04 does not use an open PR as theorem input.  Any such improvement only strengthens the conclusion that exponent `1` is noncompetitive.

---

## 10. Next theorem target

Stage14-s7-05 should keep `Q` and `S` simultaneously and dyadically study

```text
Q~U,
S~V,
UV<=B,
```

with the two exact constraints

```text
PR/(QS) rational square,
ker(Q^2-P^2)=ker(S^2-R^2).
```

The main choices to audit are:

1. parameterize the rational-square product condition before Cauchy;
2. retain the common squarefree kernel as a shared modulus/character family;
3. measure the principal same-kernel collision energy;
4. test whether the moving `Q,S` hyperbola supplies a genuine average saving;
5. do not split into independent `u` and `w` counts before exploiting the collision.

The first target remains any theorem beating the then-current merged physical exponent; the square-root asymptotic is not claimed.

---

## Boundary

```text
STAGE14_S7_04=COMPLETE_SEPARATE_PROJECTION_GENUS_ONE_AUDIT_AND_JOINT_DENOMINATOR_RECEIVER
S7_03_MULTIPLICATIVE_HEIGHT_IMPORTED=true
FIXED_U_DIRECTION_FIBER_GENUS_ONE=true
FIXED_W_DIRECTION_FIBER_GENUS_ONE=true
FIXED_REDUCED_COORDINATE_FIBER_MULTIPLICITY=B^o(1)
REDUCED_COORDINATE_VALUES_DENOM_LE_L=O(L^2)
SEPARATE_U_PROJECTION_BOUND=L^(2+o(1))
SEPARATE_W_PROJECTION_BOUND=M^(2+o(1))
SEPARATE_PROJECTION_HYPERBOLA_OPTIMAL_EXPONENT=1
SEPARATE_PROJECTION_METHOD_BEATS_MERGED_61_63=false
JOINT_REDUCED_COORDINATE_RECEIVER_EXACT=true
JOINT_MULTIPLICATIVE_HEIGHT=Q*S
JOINT_PRODUCT_SQUARE_CONDITION=PR/(QS)_IS_RATIONAL_SQUARE
JOINT_DIFFERENCE_SQUARE_CONDITION=(Q^2-P^2)*(S^2-R^2)_IS_SQUARE
JOINT_DIFFERENCE_SQUAREFREE_KERNEL_COLLISION=true
CURRENT_MERGED_PHYSICAL_UPPER_BOUND_EXPONENT=61/63
FAMILY_SMALL_FIRST_POINT_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-s7-05
```
