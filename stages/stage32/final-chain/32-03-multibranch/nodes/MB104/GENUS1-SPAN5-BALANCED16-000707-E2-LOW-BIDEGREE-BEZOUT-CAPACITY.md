# Stage32 MB104 — `000707000f0f` e=2 complete low-bidegree Bezout capacity

Status: **RETAINED EXACT GLOBAL CAPACITY REFINEMENT / ALL RAW SPECIAL-GRID BEZOUT DIVISORS EXHAUSTED / FORMAL ENDPOINT SURVIVES / e=2 OPEN / NO CREDIT**

## Scope

Continue only

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The retained joint-pair leaf gives a birational normalization map

```text
Psi:E -> C=Psi(E) subset R x R = P1 x P1
```

with

```text
[C]=(28l,28l),
g(E)=1.
```

The retained residual-node table gives sixteen exact special points, arranged in eight simultaneous-sign pairs.  Write them

```text
A+,(A-),...,H+,(H-)
```

with representatives

```text
A+=( a, a), A-=(-a,-a), B+=( a,-a), B-=(-a, a),
C+=(ia,-a), C-=(-ia, a), D+=(ia, a), D-=(-ia,-a),
E+=(u,v), E-=(-u,-v), F+=(u,-v), F-=(-u, v),
G+=(u,-u), G-=(-u, u), H+=(u,u), H-=(-u,-u),

a^2=2, u=1+i, v=1-i.
```

Their branch masses are

```text
w(A+) = x0+x2,           w(A-) = 16l-x0-x2,
w(B+) = x1+x3,           w(B-) = 16l-x1-x3,
w(C+) = x24+x26,         w(C-) = 16l-x24-x26,
w(D+) = x25,             w(D-) = 8l-x25,
w(E+) = x8+x10,          w(E-) = 16l-x8-x10,
w(F+) = x9+x11,          w(F-) = 16l-x9-x11,
w(G+) = x32+x34,         w(G-) = 16l-x32-x34,
w(H+) = x33,             w(H-) = 8l-x33.
```

The total special mass is exactly `112l`.

## 1. Bezout capacity rule

For any effective divisor `D` of bidegree `(a,b)` on `P1 x P1` not containing `C`,

```text
C.D = 28l(a+b).
```

Every normalization branch of `C` through a special point lying on `D` contributes local intersection at least one.  Therefore

```text
sum_(P special on D) w(P) <= 28l(a+b).          (CAP)
```

Since `C` has bidegree `(28l,28l)` with `l>=1`, no divisor of the low bidegrees used below can contain `C`.

## 2. Fibres: all `(1,0)` and `(0,1)` special capacities

The sixteen points lie on the following special coordinate fibres.

Vertical:

```text
{A+,B+}, {A-,B-}, {C+,D+}, {C-,D-},
{E+,F+,G+,H+}, {E-,F-,G-,H-}.
```

Horizontal:

```text
{A+,B-,C-,D+}, {A-,B+,C+,D-},
{E+,F-}, {E-,F+}, {G+,H-}, {G-,H+}.
```

Each listed fibre has capacity `28l`.  The two four-point Q0 fibres and the two four-point Q1 fibres reproduce the retained zero-quartic saturation equalities; the remaining fibre inequalities are additional exact degree constraints that must also be obeyed.

## 3. Irreducible `(1,1)` graphs

An exact enumeration over `Q(i,sqrt(2))` uses rows

```text
(xy,x,y,1).
```

There are exactly **32** irreducible `(1,1)` curves containing four special points, and no irreducible `(1,1)` curve contains five or more.  Every such four-point set obeys

```text
sum w(P) <= 56l.                                (11-CAP)
```

If an irreducible `(1,1)` curve contains at most three special points, the inequality is automatic because every single special mass is at most `16l`, so the left side is at most `48l`.

The 32 four-point supports are retained machine-readably in the companion certificate and recomputed by the verifier.

## 4. Irreducible `(1,2)` and `(2,1)` curves

For `(1,2)` use rows

```text
(x y^2, x y, x, y^2, y, 1).
```

Exact enumeration gives `262` unique curves through at least six special points before reducibility is removed, with support-size census

```text
6:116,
7:128,
9:16,
12:2.
```

Exactly **16** of these are irreducible, and every irreducible one contains exactly six special points.  Hence each supplies

```text
sum_(six points) w(P) <= 84l.                  (12-CAP)
```

The transpose `(2,1)` enumeration has the identical census and again exactly **16** irreducible six-point supports.

All reducible `(1,2)/(2,1)` divisors give no stronger inequality than the sum of their lower-bidegree component capacities.  An irreducible `(1,2)/(2,1)` curve through at most five special points is automatic because `5*16l < 84l`.

## 5. Why this exhausts raw supported-point Bezout capacity

If `a+b>=4`, then

```text
28l(a+b) >= 112l,
```

which is already at least the total mass of all sixteen special points.  Thus no raw supported-point capacity inequality of bidegree total at least four can improve the constraints.

Pure `(a,0)` or `(0,b)` divisors are sums of fibres and are likewise covered componentwise.  Therefore the fibre, `(1,1)`, irreducible `(1,2)`, and irreducible `(2,1)` lists above exhaust every nontrivial inequality obtainable solely from `(CAP)` and the sixteen special-point masses.

## 6. The route does not close e=2

The capacity package is nontrivial.  For example, the earlier `m=4` formal endpoint witness recorded in the thin-shell wall violates the irreducible `(1,1)` support

```text
{A-,C-,E-,G+}.
```

However, raw Bezout capacity still does not close the formal endpoint.  For

```text
m=5, l=10
```

take, in node order

```text
(0,1,2,3,8,9,10,11,24,25,26,32,33,34),

x = (8,0,0,48,42,76,2,80,0,0,0,0,2,78).
```

Equivalently

```text
b_j=x_j/2-4m
 =(-16,-20,-20,4,1,18,-19,20,-20,-20,-20,-20,-19,19).
```

It satisfies:

```text
0<=x_j<=8l,
Q0 and Q1 saturation,
all x_j even,
x24+x25+x26 == 0 mod 4,
x32+x33+x34 == 0 mod 4,
Q=sum b_j^2 = 4480 = 168m^2+56m,
delta_same = 336m^2+112m-2Q = 0,
```

and every retained fibre / `(1,1)` / irreducible `(1,2)` / irreducible `(2,1)` capacity inequality.

This is formal allocation data only; no geometric realization is claimed.

## Routing consequence

The special-grid geometry now supplies a finite exact package of useful global linear inequalities, but **raw Bezout counting on the sixteen residual special points is exhausted and cannot close e=2 by itself**.

The load-bearing continuation remains one of:

```text
actual conductor loop -> 0 or gamma_Q in H1(U,Z),
```

or a stronger global condition using tangencies, singularity delta, monodromy/Nielsen data, or the product/Jacobian correspondence beyond raw point capacity.

## Firewalls

- A capacity inequality is necessary, not a realization theorem.
- The `m=5` survivor is formal and does not assert an actual carrier.
- Reducible low-bidegree divisors are used only through componentwise Bezout.
- No conductor loop is evaluated.
- No weighted-cut upper bound or e=2 closure is claimed.
- `e=4`, `000707000f0f`, MB104, span5, receiver, effectivity, theorem, endpoint and Perfect-Cuboid credit remain open/zero.
- No heavy compute is armed.
- No merge or rebase authorization.
