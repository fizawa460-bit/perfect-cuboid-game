# Stage35-EX 35EX-21 — exact global normalized cuboid surface and genus-5 fibration

## Scope

Continue only from hostile-audited and merged 35EX-20/20B. Work conditionally under the normalized full receiver

```text
mu^2 = r^2 + t^2 - 2*r^2*t^2,
nu^2 = r^2 + t^2 - r^2*t^2,
r^2+s1^2 = 1,
t^2+s2^2 = 1,
```

with the Stage35-EX source chamber `r,t,s1,s2>0` and no E1/R29/Stage35/endpoint credit.

The selected question is whether the preserved `E1-GLOBAL-BIQUADRATIC-SURFACE-GEOMETRY` route produces one exact total-surface model with an exact open inverse and a useful intrinsic geometric structure.

It does. The resulting surface is not a smaller fixed curve or a finite squareclass family: it is exactly the rational square surface of a cuboid normalized to one edge `1`, at the normalized-receiver level. This is a useful exact identification, but it is not by itself a closure theorem and it does not establish an endpoint equivalence at the primitive/canonical source-population level.

## 1. Exact global coordinate change

On the receiver open `r*t != 0`, define

```text
x = s1/r,
y = s2/t,
p = 1/r,
q = 1/t,
z = mu/(r*t),
w = nu/(r*t).
```

The source circles give

```text
p^2 = 1+x^2,                                      (PC1)
q^2 = 1+y^2.                                      (PC2)
```

For the Master square,

```text
z^2
 = mu^2/(r^2*t^2)
 = 1/t^2 + 1/r^2 - 2
 = x^2+y^2.                                       (PC3)
```

For the E1 square,

```text
w^2
 = nu^2/(r^2*t^2)
 = 1/t^2 + 1/r^2 - 1
 = 1+x^2+y^2.                                     (PC4)
```

Thus every normalized full-receiver point maps to the affine surface

```text
S_PC:
p^2 = 1+x^2,
q^2 = 1+y^2,
z^2 = x^2+y^2,
w^2 = 1+x^2+y^2.                                 (S-PC)
```

Geometrically, `(1,x,y)` are three rational edge coordinates; `p,q,z` are the three face-diagonal coordinates and `w` is the space-diagonal coordinate. This description is only a coordinate identification of the normalized receiver until a separate primitive/source-population reverse adapter is proved.

## 2. Exact inverse on the algebraic open

Conversely, on `S_PC` with `p*q != 0`, define

```text
r  = 1/p,
s1 = x/p,
t  = 1/q,
s2 = y/q,
mu = z/(p*q),
nu = w/(p*q).
```

Then

```text
r^2+s1^2=(1+x^2)/p^2=1,
t^2+s2^2=(1+y^2)/q^2=1.
```

Moreover

```text
r^2+t^2-2*r^2*t^2
 = (p^2+q^2-2)/(p^2*q^2)
 = (x^2+y^2)/(p^2*q^2)
 = mu^2,
```

and

```text
r^2+t^2-r^2*t^2
 = (p^2+q^2-1)/(p^2*q^2)
 = (1+x^2+y^2)/(p^2*q^2)
 = nu^2.
```

Therefore the two displayed maps are exact rational inverses on the stated open. For rational points, `p^2=1+x^2` and `q^2=1+y^2` already prevent `p=0` or `q=0`; the open condition is retained because it is the exact algebraic inverse-domain condition.

The Stage35-EX positive source chamber maps into

```text
x>0, y>0, p>1, q>1, z>0, w>0.
```

The algebraic surface has additional sign components and geometric boundary points. No claim is made here that every rational point of `S_PC` reconstructs the required primitive Euclid pairs with the designated `U`/`V` parity orientation, gcd channels, or canonical source labels. That reverse population adapter is outside this leaf and is required before any endpoint-equivalence claim.

## 3. Dimension is exactly two

The coordinate ring

```text
Q[x,y,p,q,z,w] /
(p^2-1-x^2,
 q^2-1-y^2,
 z^2-x^2-y^2,
 w^2-1-x^2-y^2)
```

is integral over `Q[x,y]`, because `p,q,z,w` each satisfy a monic quadratic polynomial over `Q[x,y]`. Hence the projection to `(x,y)` is finite and

```text
dim(S_PC)=2.
```

So 35EX-21 has produced a genuine total surface rather than another fixed-source curve.

## 4. Exact genus-5 fibration over the first source conic

Use as base the first source conic

```text
B1: p^2=1+x^2.
```

It is a rational genus-zero curve. The projection

```text
pi_1: S_PC -> B1,
(x,y,p,q,z,w) |-> (x,p)
```

has generic fiber over `K=Q(B1)` given by the three simultaneous quadratic covers of the `y`-line

```text
q^2 = y^2+1,
z^2 = y^2+x^2,
w^2 = y^2+p^2,             p^2=1+x^2.          (FIB)
```

Over an algebraic closure of `K`, the three radicands have generic branch pairs

```text
{+i,-i},
{+i*x,-i*x},
{+i*p,-i*p}.
```

They are pairwise distinct at the generic point. Each radicand has even degree, so infinity is unramified. The three squareclasses are independent generically because each has branch points not occurring in either of the other two radicands. Therefore the normalized generic fiber is a degree-8 `(Z/2)^3` cover of `P^1_y` with six simple branch points, each with inertia order `2`.

Riemann-Hurwitz gives

```text
2*g-2 = 8*(-2) + 6*(8/2)*(2-1)
      = -16 + 24
      = 8,
```

hence

```text
GENERIC_FIBER_GENUS=5.                         (GENUS5)
```

Visible geometric degenerations occur when branch pairs collide, including `x=0` and `x^2=1`; the inverse receiver chart also excludes the geometric divisor `p*q=0`, and a projective compactification adds the corresponding infinity boundary. This leaf does not claim a complete minimal-model or singular-fiber classification.

## 5. What the global model does and does not buy

The exact identification proves

```text
GLOBAL_TOTAL_SURFACE_MODEL_DERIVED=true,
EXACT_OPEN_RECEIVER_SURFACE_ADAPTER_PROVED=true,
GLOBAL_SURFACE_DIMENSION=2,
GENUS5_FIBRATION_PROVED=true.
```

But the model is the normalized rational cuboid square surface itself. Thus the present global-surface route has not replaced the receiver by a strictly smaller fixed arithmetic object, finite branch family, or already-classified surface.

In particular:

- the exact surface model makes global geometric tools legally source-lockable;
- it does **not** classify `S_PC(Q)`;
- it does **not** prove the primitive-source reverse population adapter;
- it does **not** prove a Brauer obstruction, local-global failure, rational-point classification, or general-type theorem;
- it does **not** authorize perfect-cuboid existence/nonexistence credit.

No formal Arsenal card classifies this global surface. Provisional `S33-PW07` is only a `TORSOR_BRAUER_INTEGRAL_KERNEL_ADAPTER`: it requires an already-constructed Brauer representative/common cocycle/intended torsor and cannot manufacture a Brauer class from `S_PC`.

Therefore

```text
CURRENT_GLOBAL_SURFACE_MODEL_ROUTE
 = FROZEN_EXACT_ENDPOINT_SCALE_MODEL_NO_CLOSURE_THEOREM.
```

This is a blocker for the idea that a mere global reparameterization will simplify E1. It is not a blocker for genuinely new global arithmetic on the exact surface.

## 6. Cycle consequence

The identification of the receiver with the exact normalized cuboid square surface and the genus-5 multiquadratic fibration materially changes the geometry, so the Cycle Exploration Safety Protocol requires a fresh `EXHAUSTIVE_VIEW_AUDIT + BLIND_REDISCOVERY` before selecting the next route.

The previously preserved

```text
E1-SURFACE-LOCAL_GLOBAL_OR_BRAUER_LAYER
```

is now dependency-eligible at the object-definition level, but remains unproved and receives no credit merely from this surface construction.

## 7. Credit boundary

```text
CYCLE_ROUTE_STATUS=BLOCKED_NEW_PATTERN_ISOLATED
CYCLE_ACTIVE_RECEIVER=MASTER_HIT_PLUS_FULL_E1_RECEIVER_WITH_TWO_PRIMITIVE_SOURCE_CIRCLES
GLOBAL_TOTAL_SURFACE_MODEL_DERIVED=true
EXACT_OPEN_RECEIVER_SURFACE_ADAPTER_PROVED=true
NORMALIZED_CUBOID_SQUARE_SURFACE_IDENTIFIED=true
GLOBAL_SURFACE_DIMENSION=2
GENUS5_FIBRATION_PROVED=true
GENERIC_FIBER_GENUS=5
PRIMITIVE_SOURCE_POPULATION_REVERSE_ADAPTER_PROVED=false
GLOBAL_SURFACE_RATIONAL_POINTS_CLASSIFIED=false
BRAUER_OBSTRUCTION_PROVED=false
CURRENT_GLOBAL_SURFACE_MODEL_ROUTE=FROZEN_EXACT_ENDPOINT_SCALE_MODEL_NO_CLOSURE_THEOREM
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
