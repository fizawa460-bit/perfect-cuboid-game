# Stage30-05 — common `Q(i)` modular/cuboid anchor source lock

```text
STAGE=30-05
ROLE=COMMON_QI_GEOMETRIC_OR_MODULI_ANCHOR
STATUS=SUBMITTED_PENDING_AUDIT
```

## Primary common model

The load-bearing source is Damiano Testa and Michael Stoll, *The surface parametrizing cuboids*, current arXiv `1009.0388v2` / published version, Section 4.

It gives the genus-5 model of `X(8)`

```text
u^2 = 2xy
v^2 = x^2-y^2
w^2 = x^2+y^2,
```

with

```text
Aut_geom(X)=PSL2(Z/8),
G0=ker(PSL2(Z/8)->PSL2(Z/4)) ~= (Z/2)^3,
PSL2(Z/4) ~= S4,
```

and the exact quotient coordinates on `(X x X)/Delta G0`

```text
U=u1*u2, V=v1*v2, W=w1*w2,
X=x1*x2, Y=y1*y2, T=x1*y2, Z=x2*y1,
XY=TZ.
```

The cuboid coordinates are identified over `Q(i)` by

```text
U=2*b1
V=2*b2
W=2*b3
X=a1+c
Y=-a1+c
T=a2+i*a3
Z=a2-i*a3.
```

Thus the relevant seven squareclasses on the common quotient are represented, after harmless common square scaling, by

```text
A1=(X-Y)^2        = 4*a1^2
A2=(T+Z)^2        = 4*a2^2
A3=-(T-Z)^2       = 4*a3^2
B1=4*X*Y          = 4*b1^2
B2=X^2+Y^2-T^2-Z^2 = 4*b2^2
B3=X^2+Y^2+T^2+Z^2 = 4*b3^2
C =(X+Y)^2        = 4*c^2.
```

This is the same cuboid surface, not a lookalike model.  The source explicitly states that the isomorphism is over `Q(i)`, not over `Q`.

Stable locator: Testa--Stoll Section 4, especially the displayed equations defining `X`, the invariant coordinates and relations, and the substitution to `a_i,b_i,c`.

## `X(4)` gauge used for the finite action calculation

Since `X/G0 ~= X(4) ~= P1`, Stage30-05 fixes one explicit `Q(i)` Hauptmodul gauge on `[x:y]`.  It uses the standard modular-generator action

```text
S : [x:y] -> [-x+y : x+y]
T : [x:y] -> [i*x : y]
```

(up to irrelevant projective/common scalars).  Equivalently on `t=x/y`,

```text
S(t)=(1-t)/(1+t),
T(t)=i*t.
```

A stable published source for this standard `X(4)` transformation law is Ching-Li Chai, Chang-Shou Lin and Chin-Lung Wang, *Mean field equations, hyperelliptic curves and modular forms: I*, Cambridge J. Math. 3 (2015), Proposition 4.3 and Corollary 4.4, DOI `10.4310/CJM.2015.v3.n1.a3` / arXiv `1502.03297`.

The precise labeling of the six cusps is a gauge choice.  Changing the `X(4)` Hauptmodul by a permitted Möbius relabeling conjugates the resulting subgroup.  Therefore Stage30-05 only treats the kernel size, image size and extension-level relation as invariant; it does **not** claim that the displayed `S3` subgroup is canonically equal to the previously audited `Q`-liftable coordinate-permutation `S3`.

## Exact consequence in the chosen gauge

Applying the diagonal `S,T` transformations to `X,Y,T,Z`, reducing by `XY=TZ`, and comparing the seven squareclasses gives

```text
rho(S_mod)=a06
  = (A1 A2)(B1 B2)

rho(T_mod)=a21
  = (A1 C)(B2 B3).
```

The multipliers are only `+1` or `-1`; `-1=i^2` is a square over `Q(i)`, so the action is legitimate at the squareclass/sign-cover level.

The exact finite checker then extends this generator assignment to all of `PSL2(Z/4)` and finds

```text
|ker rho|=4
ker rho=V_mod=ker(PSL2(Z/4)->PSL2(F2))
|im rho|=6
im rho={a00,a05,a06,a11,a19,a21} ~= S3.
```

This is the key semantic correction to the Stage30-04 abstract comparison:

```text
MODULAR_RESIDUAL_S4 -> ARRANGEMENT_BRANCH_ACTION
```

is not an isomorphism in this common-model realization.  Its `V4` kernel acts below the branch-squareclass quotient and must be accounted for in the endpoint sign-deck lift.  The 24 Stage30-04 `S4<->S4` equivariant bijections remain valid finite relabelings, but they are **not** 24 geometric adapters.

## Remaining wall

Stage30-05 does not yet determine the exact lift of the modular `V4` kernel into the endpoint sign deck, nor its behavior under `Gal(Q(i)/Q)`.  Those data are the finite semilinear/cocycle wall now owned by Stage30-06.

```text
COMMON_QI_MODEL_ANCHOR=SOURCE_LOCKED
MODULAR_TO_BRANCH_KERNEL_EXPECTED=V_mod
MODULAR_TO_BRANCH_IMAGE_ORDER_EXPECTED=6
STAGE30_04_24_CANDIDATES_GEOMETRIC_ADAPTER_CREDIT=false
Q_GALOIS_COCYCLE_VERIFIED=false
DEFECT_ELIMINATION_COUNT=0
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
