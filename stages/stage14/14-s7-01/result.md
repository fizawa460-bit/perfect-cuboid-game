# Stage14-s7-01 — generic Mordell–Weil and section classification

## Purpose

Stage14-s7-00 rewrote the active-direction problem as the moving Jacobi quartic family

```text
C_r: v^2=(1-u^2)(1-r^4*u^2),
```

with `r=a/b` and `0<r<1` on physical directions.  The mandatory first gate was to determine whether the fourth-power base change `lambda=r^4` creates generic nonboundary sections.  If it did, active-direction sparsity would not be a specialization phenomenon.

This stage closes that gate.

The answer is strong:

```text
the generic geometric Mordell-Weil rank is 0,
E(Q(r)) has only full rational 2-torsion,
and C_r(Q(r)) consists of exactly eight boundary points.
```

Therefore there is **no generic rational nonboundary section**.  A rational specialization carrying a physical nonboundary partner must acquire Mordell-Weil structure not present generically: either torsion growth or positive rank, together with the Stage14 square-lift / primitive / sharp-cutoff conditions.

No counting exponent is improved in this stage.

---

## 1. Merged input from s7-00

We use the exact normalization

```text
C_r: v^2=(1-u^2)(1-r^4*u^2).
```

The affine degree-two map

```text
U=u^2,
V=u*v
```

gives

```text
E'_r: V^2=U(1-U)(1-r^4*U).
```

After

```text
X=r^4*U,
Y=r^4*V,
```

this is the standard fourth-power Legendre base change

```text
E_r: Y^2=X(X-1)(X-r^4).                 (1.1)
```

The map `C_r -> E'_r` extends to a degree-two morphism of smooth projective generic fibers.  Its involution on the affine chart is

```text
(u,v) -> (-u,-v).
```

---

## 2. Weierstrass invariants

Write (1.1) as

```text
Y^2=X^3-(1+r^4)X^2+r^4 X.
```

Thus

```text
a2=-(1+r^4),
a4=r^4,
a6=0.
```

The standard invariants simplify to

```text
c4    = 16*(r^8-r^4+1),
Delta = 16*r^8*(1-r^4)^2.              (2.1)
```

Hence the finite bad places are

```text
r=0,
r^4=1.
```

At `r=0`, `ord(Delta)=8` and `c4(0)=16`, so the fiber is multiplicative of type

```text
I8.
```

At each of the four roots of `r^4=1`, `ord(Delta)=2` and `c4=16`, so each fiber is

```text
I2.
```

---

## 3. The fiber at infinity is another I8

Put

```text
s=1/r,
X=s^(-4)*X_inf,
Y=s^(-6)*Y_inf.
```

Multiplying the equation by `s^12` gives

```text
Y_inf^2
 = X_inf^3-(1+s^4)X_inf^2+s^4 X_inf.
```

This is the same integral local model with `r` replaced by `s`.  Therefore at `s=0`, i.e. `r=infinity`, one again has

```text
ord(Delta)=8,
c4 unit,
```

and the fiber is

```text
I8.
```

The complete geometric singular-fiber configuration is therefore

```text
[I8, I8, I2, I2, I2, I2].              (3.1)
```

Its Euler-number sum is

```text
8+8+4*2=24.
```

The relatively minimal elliptic surface over `P1_r` therefore has `chi(O)=2`; with section and no multiple fibers it is an elliptic K3 surface.

---

## 4. Shioda-Tate forces geometric generic rank zero

For an elliptic surface with section, the trivial lattice has rank

```text
2 + sum_v (m_v-1),
```

where `m_v` is the number of irreducible components of the fiber.

For (3.1),

```text
rank(Triv)
 = 2 + (8-1)+(8-1)+4*(2-1)
 = 20.                                  (4.1)
```

Shioda-Tate gives

```text
rho = rank(Triv) + rank MW_geom.
```

Over characteristic zero a K3 surface has

```text
rho<=20.
```

Combining with (4.1),

```text
20 <= rho <=20,
```

so

```text
rho=20,
rank E_r(Qbar(r))=0.                    (4.2)
```

Thus the fourth-power base change does **not** create a generic non-torsion section.

The surface is extremal in the sense relevant here: maximal Picard rank and geometric Mordell-Weil rank zero.

---

## 5. Rational generic torsion on the Legendre quotient

Equation (1.1) has the obvious rational 2-torsion

```text
O,
(0,0),
(1,0),
(r^4,0).
```

We now show these are all of `E_r(Q(r))`.

### 5.1 Specialize at r=2

The good specialization is

```text
E_2: y^2=x(x-1)(x-16).
```

Direct finite-field counting gives

```text
#E_2(F_7)=8,
#E_2(F_11)=8.
```

The standard good-reduction injection for prime-to-`p` torsion therefore implies that `E_2(Q)_tors` has order dividing `8`.

It already contains full rational 2-torsion, so its order is at least `4`.

### 5.2 There is no rational point of order 4 on E_2

Any point of order `4` must halve one of the three nonzero 2-torsion points.

For

```text
E_lambda: y^2=x(x-1)(x-lambda),
```

direct duplication algebra gives the following x-coordinate equations for a half:

```text
2P=(0,0)      -> x^2=lambda,
2P=(1,0)      -> x^2-2x+lambda=0,
2P=(lambda,0) -> x^2-2lambda*x+lambda=0.
```

At `lambda=16`:

```text
x=+/-4
```
for the first case, but the corresponding right sides are `-144` and `-400`, so no rational `y` exists.

The second quadratic has discriminant

```text
4-64=-60,
```

and the third has discriminant

```text
1024-64=960=64*15,
```

neither a rational square.

Hence `E_2(Q)` has no order-4 point.  Since an elliptic curve cannot have an exponent-2 torsion subgroup of order `8`,

```text
E_2(Q)_tors ~= (Z/2Z)^2.               (5.1)
```

### 5.3 Inject generic torsion into the good specialization

A torsion section on the smooth locus specializes injectively at a good characteristic-zero fiber: the `n`-torsion group scheme is finite etale, so two torsion sections that agree in one connected good fiber agree identically.

Therefore

```text
E_r(Q(r))_tors -> E_2(Q)_tors
```

is injective.

Together with the four obvious generic 2-torsion points and (5.1),

```text
E_r(Q(r)) = E_r(Q(r))_tors ~= (Z/2Z)^2.    (5.2)
```

There are no rational generic non-torsion sections and no extra rational generic torsion sections.

---

## 6. Exact Q(r)-point classification on the Jacobi quartic

Let `K=Q(r)` and let `C_r` denote the smooth projective model of

```text
v^2=(1-u^2)(1-r^4*u^2).
```

The degree-two map

```text
pi:C_r -> E'_r,
pi(u,v)=(u^2,u*v)
```

sends `K`-points to `K`-points.  Since `E'_r` is `K`-isomorphic to `E_r`, (5.2) gives

```text
#E'_r(K)=4.
```

Each fiber of `pi` has at most two `K`-points, hence

```text
#C_r(K)<=8.                              (6.1)
```

But the following eight `K`-points are explicit:

```text
(0,+1),
(0,-1),
(+1,0),
(-1,0),
(+r^(-2),0),
(-r^(-2),0),
P_inf,+,
P_inf,-,
```

where the two projective points at infinity are characterized by

```text
v/u^2 = +r^2,
v/u^2 = -r^2.
```

Thus equality holds in (6.1):

```text
#C_r(Q(r))=8.                            (6.2)
```

Every one of these eight points is a boundary point for the Stage14 physical open set:

- `u=0` is the universal anchor fiber;
- `u=+/-1` and `u=+/-r^(-2)` are branch/zero-factor points;
- the two points at infinity are outside the affine physical slope chart.

Therefore

```text
GENERIC_RATIONAL_NONBOUNDARY_SECTION_EXISTS=false.   (6.3)
```

This is stronger than merely proving generic rank zero: it classifies **all** rational generic sections relevant to the Jacobi family.

---

## 7. Consequence for active directions

A rational physical direction is a specialization

```text
r=a/b in Q,
0<a<b,
gcd(a,b)=1.
```

If such a specialization admits a physical transferred partner, the specialized Jacobi curve has a rational nonboundary point.

By (6.2), that point cannot be the specialization of a generic `Q(r)`-section.  Therefore the specialization has Mordell-Weil structure beyond the generic boundary set.

There are two logically distinct possibilities:

```text
(A) torsion growth at the specialization;
(B) positive Mordell-Weil rank at the specialization.
```

The present stage does **not** discard branch (A).  A nonboundary torsion point at a special rational parameter is possible in principle and must be classified before every physical activation is called a rank jump.

Thus the correct next receiver is

```text
ACTIVE_DIRECTION
 -> SPECIALIZATION_MW_GROWTH
 -> {TORSION_GROWTH or POSITIVE_RANK}
 -> NONBOUNDARY_SMALL_POINT
 -> PHYSICAL_SQUARE_LIFT_AND_SHARP_CUTOFF.
```

---

## 8. Why plain average-rank is still not enough

Even after generic rank zero is known, the Stage14 event remains stronger than

```text
rank(E_r(Q))>0.
```

A physical activation requires an actual nonboundary point satisfying:

- the Jacobi square lift `U=u^2`;
- positive primitive partner slope;
- the exact cross-square reconstruction;
- the sharp physical cutoff from merged 4bn;
- the relevant Stage14 height window.

Therefore a future rank-jump theorem can be a useful first sparsity input, but it still must be combined with a first-small-point / physical-lift theorem unless its proof directly retains those conditions.

---

## 9. Route decision for s7-02

The generic-section gate is now closed in the favorable direction.

The next stage should separate the two specialization-growth mechanisms before launching a family rank sieve.

Primary target for `Stage14-s7-02`:

1. classify rational specializations `r=a/b` for which the Jacobi/Legendre fiber gains rational torsion beyond the generic boundary torsion;
2. determine whether any such extra torsion point can satisfy the Stage14 nonboundary physical lift;
3. isolate the remaining physical active set inside the positive-rank specialization set;
4. only then choose the first quantitative rank-jump / first-small-point family theorem.

The merged t38 moving-prime elliptic-packet result and merged 4bo moving-`Q` compression remain compatible secondary arithmetic receivers, but neither changes the generic section classification proved here.

---

## Standard geometric inputs used

This stage uses the standard Kodaira/Tate multiplicative-fiber criterion, the Shioda-Tate formula, and the characteristic-zero K3 Picard bound `rho<=20`.  The rank-zero conclusion itself is then forced by the explicitly computed fiber configuration, without importing a classification-table value for this particular surface.

---

## Boundary

```text
STAGE14_S7_01=COMPLETE_GENERIC_MORDELL_WEIL_AND_SECTION_CLASSIFICATION
MERGED_S7_00_FAMILY_NORMALIZATION_IMPORTED=true
LEGENDRE_BASE_CHANGE_MODEL=Y^2=X*(X-1)*(X-r^4)
WEIERSTRASS_C4=16*(r^8-r^4+1)
WEIERSTRASS_DISCRIMINANT=16*r^8*(1-r^4)^2
SINGULAR_FIBER_CONFIGURATION=I8,I8,I2,I2,I2,I2
ELLIPTIC_SURFACE_IS_K3=true
TRIVIAL_LATTICE_RANK=20
GEOMETRIC_PICARD_RANK=20
GENERIC_GEOMETRIC_MORDELL_WEIL_RANK=0
GENERIC_LEGENDRE_QR_TORSION=(Z/2Z)^2
GENERIC_LEGENDRE_QR_POINT_COUNT=4
GENERIC_JACOBI_QR_POINT_COUNT=8
GENERIC_JACOBI_POINTS_ALL_BOUNDARY=true
GENERIC_RATIONAL_NONBOUNDARY_SECTION_EXISTS=false
PHYSICAL_ACTIVATION_REQUIRES_SPECIALIZATION_MW_GROWTH=true
SPECIALIZATION_MW_GROWTH_SPLIT=TORSION_GROWTH_OR_POSITIVE_RANK
PHYSICAL_ACTIVATION_IMPLIES_POSITIVE_RANK_UNCONDITIONALLY=false
PLAIN_AVERAGE_RANK_SUFFICIENT_FOR_PHYSICAL_COUNT=false
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=false
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=41/42
NEXT=Stage14-s7-02
```
