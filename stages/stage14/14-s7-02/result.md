# Stage14-s7-02 — specialization torsion growth and physical positive-rank gate

## Purpose

Merged Stage14-s7-01 proves that the generic fourth-power Jacobi family

```text
C_r: v^2=(1-u^2)(1-r^4 u^2)
```

has no rational nonboundary section over `Q(r)`.  The generic Legendre quotient has geometric Mordell-Weil rank zero, and the generic Jacobi rational points are exactly eight boundary points.

For a rational physical specialization `0<r<1`, a new rational nonboundary point could still arise in two logically different ways:

1. specialization torsion growth;
2. specialization positive rank.

This stage closes the first branch.

The conclusion is uniform on every nonsingular rational physical specialization:

```text
C_r(Q)_tors = Z/2Z x Z/4Z,
```

and its eight torsion points are exactly the eight boundary points already present generically.  Therefore every physical nonboundary rational point has infinite order.  In particular every active physical direction is a positive-rank specialization.

No counting exponent is improved here.  The small-height / physical-cutoff requirement remains essential.

---

## 1. Merged input and physical range

From merged s7-00 and s7-01 we use

```text
C_r: v^2=(1-u^2)(1-r^4u^2),
0<r<1,
```

and the degree-two map

```text
pi: C_r -> E_r,
X=r^4 u^2,
Y=r^4 u v,
```

where

```text
E_r: Y^2=X(X-1)(X-r^4).
```

A physical transferred partner has positive half-angle slopes

```text
r=a/b,
x=c/d,
0<a<b,
0<c<d,
```

with positive cross-square detector.  The factor `ad-bc` is then positive, so

```text
x<r.
```

Since `u=x/r`, every physical point satisfies

```text
0<u<1.                                      (1.1)
```

Thus it is automatically distinct from all boundary points listed below.

---

## 2. The eight boundary points form a rational torsion subgroup of order 8

For every nonsingular rational `r` the eight boundary points are

```text
u=0                    : (0,+1),(0,-1),
u=+1,-1               : v=0,
u=+r^(-2),-r^(-2)   : v=0,
the two points at infinity.
```

Their images under `pi` are the four rational 2-torsion points of `E_r`:

```text
(0,0),
(r^4,0),
(1,0),
O.
```

Choose any boundary point as the origin on `C_r`, and translate the target by the torsion point `pi(O_C)` so that the resulting degree-two morphism

```text
phi:C_r -> E_r
```

sends origin to origin.  A nonconstant morphism of elliptic curves sending origin to origin is an isogeny, so `phi` is a rational 2-isogeny.

Translation by a 2-torsion point only permutes `E_r[2]`.  Hence the eight boundary points are exactly

```text
phi^(-1)(E_r[2]).                            (2.1)
```

This is a subgroup of order `2*4=8`.

For a point `P` in (2.1),

```text
phi(2P)=2phi(P)=0,
```

so `2P` lies in the order-two kernel of `phi`; therefore

```text
4P=0.
```

The subgroup has order eight and cannot be elementary `2`-torsion, since an elliptic curve has only four geometric points killed by `2`.  Consequently

```text
boxed:
B_r := boundary subgroup ~= Z/2Z x Z/4Z.    (2.2)
```

This identification is uniform for every physical `0<r<1`: the eight boundary points stay distinct because `r` is nonzero and `r^4 != 1`.

---

## 3. Mazur leaves only one possible torsion-growth group

We now use Mazur's rational torsion theorem.  The only noncyclic torsion groups over `Q` are

```text
Z/2Z x Z/(2m)Z,  1<=m<=4.
```

Since `C_r(Q)_tors` already contains the subgroup

```text
Z/2Z x Z/4Z,
```

there are only two possibilities:

```text
C_r(Q)_tors ~= Z/2Z x Z/4Z,
```

or

```text
C_r(Q)_tors ~= Z/2Z x Z/8Z.                 (3.1)
```

Thus specialization torsion growth is equivalent to the existence of a rational point of order `8` on `C_r`.

No odd-torsion branch remains after (2.2) and Mazur: a rational torsion group containing `Z/2 x Z/4` cannot simultaneously acquire rational 3-, 5-, or 7-torsion.

---

## 4. A rational order-8 point on C_r would force order >=4 on E_r

Suppose `P in C_r(Q)` has order `8`.

Because `phi` is a degree-two isogeny, its kernel has order `2`.  The image of the cyclic subgroup `<P>` therefore has order either

```text
8
```

or

```text
4.
```

Hence

```text
C_r(Q) has order-8 torsion
  => E_r(Q) has a rational torsion point of order divisible by 4.  (4.1)
```

It remains to prove that no physical fourth-power Legendre specialization has rational 4-torsion.

---

## 5. Uniform exclusion of rational order 4 on the Legendre quotient

Put

```text
lambda=r^4,
0<lambda<1.
```

Then

```text
E_lambda: y^2=x(x-1)(x-lambda)
```

has the three nonzero rational 2-torsion points

```text
T0=(0,0),
T1=(1,0),
Tl=(lambda,0).
```

Any rational point of order `4` must halve one of these three points.

For a split cubic

```text
y^2=(x-e1)(x-e2)(x-e3),
```

a rational 2-torsion point `(e1,0)` is divisible by `2` over `Q` only if both differences

```text
e1-e2,
e1-e3
```

are rational squares.  Equivalently, direct duplication gives the same three conditions below.

### 5.1 T0 cannot be halved

For `T0=(0,0)` the required differences include

```text
-1.
```

This is not a rational square, so `T0` is not divisible by `2`.

### 5.2 Tl cannot be halved in the physical interval

For `Tl=(lambda,0)` the required differences are

```text
lambda=r^4,
lambda-1.
```

The first is a square, but

```text
lambda-1<0,
```

so the second is not a rational square.  Thus `Tl` is not divisible by `2`.

### 5.3 T1 would require the Fermat quartic equation

For `T1=(1,0)` the required differences are

```text
1,
1-lambda=1-r^4.
```

Therefore a rational half would require

```text
s^2=1-r^4                                  (5.1)
```

with rational `0<r<1`.

The classical Fermat quartic descent states that

```text
y^2=1-x^4
```

has no rational points with `0<|x|<1`; its rational points are the trivial boundary points `x=0,+/-1` with the corresponding `y` values.  Applying this to (5.1) excludes every physical `0<r<1`.

Thus none of the three rational 2-torsion points of `E_r` is divisible by `2`, and hence

```text
boxed:
E_r(Q) has no rational point of order 4
for every rational physical 0<r<1.          (5.2)
```

This step uses only the classical Fermat quartic descent, not a rank computation for each specialization.

---

## 6. Specialization torsion growth is impossible

Combine (4.1) and (5.2).

If `C_r(Q)` had torsion `Z/2 x Z/8`, it would contain an order-8 point; its image under the rational 2-isogeny would give order `4` or `8` torsion on `E_r`, contradicting (5.2).

Therefore the second case in (3.1) never occurs in the physical rational interval.

Hence

```text
boxed:
C_r(Q)_tors = Z/2Z x Z/4Z
for every rational 0<r<1.                   (6.1)
```

Since the boundary subgroup `B_r` already has order eight,

```text
boxed:
C_r(Q)_tors = B_r.                          (6.2)
```

Thus the torsion points are exactly the eight boundary points.

---

## 7. Every physical nonboundary point has infinite order

By (1.1), a physical transferred point satisfies

```text
0<u<1.
```

The finite boundary `u`-coordinates are

```text
0,
+/-1,
+/-r^(-2).
```

Because `0<r<1`,

```text
r^(-2)>1.
```

So a physical point is not any finite boundary point, and it is not at infinity.

Using (6.2), every physical point is therefore non-torsion:

```text
boxed:
physical nonboundary rational point
  => infinite order on C_r(Q).              (7.1)
```

The 2-isogeny has finite kernel, so the image of an infinite-order point remains infinite order.  Hence

```text
boxed:
physical active direction
  => rank C_r(Q) >=1
  => rank E_r(Q) >=1.                       (7.2)
```

This removes the torsion-growth branch left open in s7-01.

---

## 8. What this does and does not buy quantitatively

The new implication is a genuine structural reduction:

```text
active physical directions
  subset
positive-rank specializations of the extremal K3 family E_r.
```

However the converse is false and is not claimed.

A positive-rank specialization can have its first nonboundary rational point far outside the Stage14 physical height/cutoff window.  Therefore the next problem remains a **small first point among rank-jump specializations**, not plain positive-rank density.

In particular, the following are still insufficient by themselves:

- average rank;
- root-number density;
- existence of any non-torsion point without height control;
- Selmer rank without a rational small-point transfer.

The current active-direction exponent remains

```text
T^(41/21+epsilon)
```

with `T~sqrt(B)`.

The next ceiling still requires a `T^(-1/63)` family-level saving, and square-root scale still requires total `T^(-20/21)` saving relative to the current active-direction exponent.

---

## 9. Next route

Stage14-s7-03 should now work on the positive-rank branch only.

The correct object is the first nonboundary specialization height

```text
h_min(r)
 = min{ h(P): P in C_r(Q) nonboundary, infinite order },
```

with the physical square-lift / primitive / reconstructed-cutoff constraints retained.

The first task is to derive a specialization-height receiver that separates

```text
rank jump
```

from

```text
rank jump with a point in the Stage14 polynomial/physical window.
```

Only the latter can reduce `A_res(B)`.

---

## External standard inputs

Two classical inputs are used explicitly.

1. **Mazur's rational torsion theorem** for elliptic curves over `Q`, only in the restricted consequence that a torsion group containing `Z/2 x Z/4` is either `Z/2 x Z/4` or `Z/2 x Z/8`.
2. **Fermat's quartic descent** for `y^2=1-x^4`, only in the consequence that there is no rational solution with `0<|x|<1`.

Everything else is an exact algebraic consequence of the merged Stage14 Jacobi/Legendre model.

---

## Boundary

```text
STAGE14_S7_02=COMPLETE_SPECIALIZATION_TORSION_GROWTH_EXCLUSION_AND_POSITIVE_RANK_GATE
MERGED_S7_01_GENERIC_CLASSIFICATION_IMPORTED=true
PHYSICAL_NORMALIZED_U_RANGE=0<u<1
BOUNDARY_SUBGROUP_ORDER=8
BOUNDARY_SUBGROUP_STRUCTURE=(Z/2Z)x(Z/4Z)
MAZUR_ONLY_TORSION_GROWTH_CANDIDATE=(Z/2Z)x(Z/8Z)
LEGENDRE_PHYSICAL_ORDER4_TORSION_EXISTS=false
FERMAT_QUARTIC_NONTRIVIAL_PHYSICAL_SOLUTION_EXISTS=false
JACOBI_PHYSICAL_TORSION_GROWTH_EXISTS=false
SPECIALIZED_JACOBI_TORSION=(Z/2Z)x(Z/4Z)
SPECIALIZED_JACOBI_TORSION_POINTS_ALL_BOUNDARY=true
PHYSICAL_NONBOUNDARY_POINT_HAS_INFINITE_ORDER=true
PHYSICAL_ACTIVATION_IMPLIES_POSITIVE_RANK_UNCONDITIONALLY=true
POSITIVE_RANK_IMPLIES_PHYSICAL_ACTIVATION=false
SMALL_POINT_HEIGHT_GATE_REMAINS=true
CURRENT_ACTIVE_DIRECTION_EXPONENT_T=41/21
ACTIVE_DIRECTION_SAVING_TO_CROSS_CEILING_T=1/63
ACTIVE_DIRECTION_SAVING_TO_SQRT_T=20/21
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
NEXT=Stage14-s7-03
```
