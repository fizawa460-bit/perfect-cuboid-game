# Stage32 MB104 — `000707000f0f` e=2 A1 lift-energy identity

Status: **RETAINED EXACT AGGREGATE CONDUCTOR FORMULA / HODGE THRESHOLD BECOMES SQUARE-ENERGY IDENTITY / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Assume conditionally that the retained dangerous equality packet is realized in the surviving `e=2` case. Keep

```text
Sigma={P0,P1,P2,P3,P8,P9,P10,P11,P24,P25,P26,P32,P33,P34},
D_l=7lH-4l sum_(p in Sigma)E_p,
l>=1.
```

For every supported node `Pj`, the exact residual-node table gives two points of the support-specific intermediate cover `X_H=P/H_diag` above the box node, exchanged by the residual deck involution `tau`. Let

```text
x_j
```

be the number of the `8l` normalization branches using the displayed residual representative and `8l-x_j` the number using its simultaneous negative.

The goal here is only to compute the **aggregate** cross-sheet intersection `y=C_1.C_2` from these fourteen node-level allocation numbers. No individual conductor pair is labeled.

## 1. Intersection of the two component images before A1 resolution

Use the retained equality-rigidity notation

```text
P=C8 x C8,
H=<T',TT'R>, |H|=4,
X_H=P/H_diag.
```

In the `e=2` case the normalized product-cover component `Z` has stabilizer exactly `H` and both projections

```text
Z -> C8
```

have degree

```text
n=28l.
```

The image of `Z` in the product surface has bidegree `(n,n)`. The diagonal residual element `T` sends this component to the other component `TZ`; because the component stabilizer is exactly `H`, `TZ` is distinct from `Z` and has the same bidegree. Hence on the smooth product surface

```text
Z.TZ = 2 n^2 = 1568 l^2.                       (P-INT)
```

Let

```text
Gamma=Z/H_diag subset X_H,
tau Gamma=(TZ)/H_diag.
```

At the generic point of `Gamma` the diagonal `H` action has trivial inertia, so the quotient pullback has coefficient one:

```text
q_H^* Gamma = Z,
q_H^*(tau Gamma)=TZ,
```

for the degree-four quotient `q_H:P->X_H`. Projection formula therefore gives the Mumford intersection on the normal intermediate quotient

```text
Gamma . tau Gamma = (Z.TZ)/4 = 392 l^2.        (XH-INT)
```

This is the intersection **before** resolving the supported A1 points.

## 2. Branch multiplicities at the two A1 lifts of one supported node

The residual quotient `X_H->B` is unramified over a supported node because its local stabilizer is one of the two elements already contained in `H`; the nontrivial residual class is the absent type `T H`. Thus every supported box node has two A1 lifts in `X_H`, exchanged by `tau`.

At node `Pj`, the retained branch packet has exactly `8l` distinct FSM-minimal branches. Since

```text
D_l.E_j=8l,
```

all `8l` branches meet the corresponding exceptional curve with multiplicity one. Therefore the two A1 lifts carry branch multiplicities

```text
Gamma:      x_j,       8l-x_j,
tau Gamma:  8l-x_j,   x_j.                    (MULT)
```

No assumption on the individual exceptional landing points is used.

## 3. Exact A1 resolution correction

For one A1 point let `F` be the exceptional `(-2)`-curve on the minimal resolution. If a reduced curve germ `A` has total strict-transform intersection

```text
Atilde.F=r_A,
```

then its Mumford pullback is

```text
rho^*A=Atilde+(r_A/2)F,
```

because `(rho^*A).F=0`. Hence for two curve germs `A,B`,

```text
A.B = Atilde.Btilde + r_A*r_B/2.              (A1-CORR)
```

Apply `(A1-CORR)` to `Gamma,tau Gamma`. At the first lift of `Pj` the correction is

```text
x_j(8l-x_j)/2,
```

and at the second lift it is the same. Thus the total correction contributed by the supported box node `Pj` is exactly

```text
x_j(8l-x_j).                                  (NODE-CORR)
```

The carrier misses unsupported box nodes: on the cuboid resolution their exceptional curves have coefficient zero in `D_l`, hence intersection zero with an integral carrier distinct from those exceptional curves. Therefore there are no further A1-resolution corrections along this curve.

The smooth residual-cover model used in the retained split-Hodge leaf is obtained after these supported A1 resolutions (and the absent-type branch resolution, which the carrier misses). Its two component strict transforms are the retained `C_1,C_2`. Consequently

```text
y=C_1.C_2
 =392l^2-sum_(j in Sigma) x_j(8l-x_j).         (Y)
```

This is an aggregate conductor identity. It does not identify which branch pairs contribute locally.

## 4. Centered square-energy form

Put, exactly as in the residual-node table,

```text
d_j=2x_j-8l.
```

Then

```text
x_j(8l-x_j)=16l^2-d_j^2/4.
```

There are fourteen supported nodes, so `(Y)` becomes

```text
y
 =392l^2-224l^2+(1/4)sum_j d_j^2
 =168l^2+(1/4)sum_j d_j^2.                    (ENERGY-Y)
```

Equivalently, the weighted opposite-sheet conductor cut from the retained split-Hodge identity is

```text
y/2
 =84l^2+(1/8)sum_j d_j^2.                     (ENERGY-CUT)
```

Thus the retained Hodge inequality

```text
y/2 >= 84l^2
```

is automatic once the support-specific intermediate quotient and the A1 resolution are materialized. Equality holds exactly when

```text
d_j=0 for every supported node,
```

i.e. when every node has the balanced allocation

```text
x_j=4l.
```

The formal balanced allocation is already compatible with the two retained saturation equations, so this identity does not exclude `e=2`.

## 5. Same-sheet defect and the surviving numerical constraint

The retained downstairs total normalization defect is

```text
Delta(C)=168l^2+56l
```

and the split-Hodge decomposition is

```text
Delta(C)=delta_same+y/2.
```

Using `(ENERGY-CUT)` gives the exact aggregate identity

```text
delta_same
 =84l^2+56l-(1/8)sum_j d_j^2.                 (SAME)
```

Therefore actual realizability requires

```text
sum_j d_j^2 <= 672l^2+448l.                   (SAME-NONNEG)
```

This is a genuine restriction on extreme branch allocations, but it leaves the balanced allocation and does not close `e=2`.

## Route consequence

The previous Hodge route sought an independent upper bound below `84l^2` for the opposite-sheet weighted cut. The exact lift-energy identity shows why that target cannot be reached from the node allocation alone:

```text
opposite-sheet cut = 84l^2 + nonnegative square energy.
```

Hence the Hodge lower bound is not an additional filter on the admissible `x_j`; it is the minimum of the exact A1 lift formula.

The useful remaining problem is now sharper. One must obtain a **global constraint on the fourteen centered allocations `d_j`** (or a stronger obstruction not mediated by the Hodge lower bound), using the actual elliptic correspondence / conductor descent geometry. The two retained boundary-fiber equations alone admit `d_j=0` for all `j`.

## Firewalls

- No individual conductor pair receives a residual sign.
- `(ENERGY-CUT)` is an aggregate intersection identity, not a branch-pair transition table.
- No claim is made that an arbitrary formal allocation is geometrically realizable.
- The balanced allocation is only a surviving formal possibility, not an existence construction.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- No finite degree window is released.
- MB104/span5/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
