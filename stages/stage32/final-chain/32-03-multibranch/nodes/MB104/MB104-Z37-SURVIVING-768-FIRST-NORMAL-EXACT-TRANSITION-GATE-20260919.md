# MB104 Z37 — surviving-768 first-normal exact transition gate — 2026-09-19

Status: **PRE-AUDIT EXACT FIRST-NORMAL VANISHING / NO CREDIT**

## Target

The surviving balanced size-768 support is

```text
000707000f0f.
```

Z33G gives its two zero-pairing elliptic quartics

```text
QA:
  b1=0,
  i*a2-a3=0,
  a1-c=0

QB:
  b2=0,
  i*a3+a1=0,
  a2-c=0
```

meeting at the two smooth points

```text
r_s=(1,1,i,0,0,s,1),  s=+sqrt(2),-sqrt(2).
```

The ordinary gluing holonomy of `O(P)` on `U=QA union QB` is exactly one. Z33H parked the first-normal class because a normalized normal-direction transition had not been computed.

Z37 computes that transition directly from the exact local equations.

## 1. Exact local coordinates

Work in the affine chart `c=1` near either `r_s`. Put

```text
u=b1,
v=b2.
```

The four cuboid equations give exact analytic branches

```text
a1^2 = 1-u^2,
a2^2 = 1-v^2,
a3^2 = u^2+v^2-1,
b3^2 = 2-u^2-v^2,
```

with the branches selected by

```text
a1(0,0)=1,
a2(0,0)=1,
a3(0,0)=i,
b3(0,0)=s.
```

Thus `u,v` are regular parameters and locally

```text
QA=(u=0),
QB=(v=0),
U=(uv=0).
```

In particular `I_U/I_U^2` is generated locally by `uv`.

All four functions `a1,a2,a3,b3` have zero first derivatives in both `u,v` at the origin, and zero mixed derivative there.

## 2. Exact transition

For the surviving support, Z33G uses

```text
LA = b3+i*b2-2*a2,
LB = -b1+i*b3-2*a3,

fA = LA/a2^4,
fB = LB/a3^4
```

(the common `c^3` factor is one on this affine chart), and

```text
g=fB/fA.
```

Let

```text
D=s-2.
```

At `u=v=0`,

```text
LA=D,
LB=iD,
(a2/a3)^4=1,
g=i.
```

The exact first jet is

```text
LA_u=0,  LA_v=i,  LA_uv=0,
LB_u=-1, LB_v=0,  LB_uv=0,
((a2/a3)^4)_u=((a2/a3)^4)_v=((a2/a3)^4)_uv=0.
```

Hence

```text
g_u   = -1/D,
g_v   =  1/D,
g_uv  =  i/D^2.
```

The branchwise-normalized transition is obtained by dividing out the restrictions to the two branches:

```text
G(u,v)
 = g(u,v) g(0,0) / (g(u,0) g(0,v)).
```

It satisfies

```text
G(u,0)=G(0,v)=1.
```

Its fiber coefficient in `I_U/I_U^2` at the node is

```text
kappa_s
 = partial_u partial_v log(g)(0,0)
 = g_uv/g - (g_u g_v)/g^2.
```

Substituting the exact jet gives

```text
kappa_s
 = (i/D^2)/i
   - [(-1/D)(1/D)]/i^2
 = 1/D^2 - 1/D^2
 = 0.
```

This holds for both `s=+sqrt(2)` and `s=-sqrt(2)`.

## 3. From local coefficients to the first-normal Picard class

Z33H source-locks

```text
L = O_U(-U),
deg L|QA = deg L|QB = 2,
H^1(QA,L|QA)=H^1(QB,L|QB)=0.
```

The normalization exact sequence therefore identifies any possible first-neighborhood obstruction with the quotient of the two intersection-point fiber data. After the branch restrictions have been normalized, the only local fiber data are the two coefficients

```text
(kappa_+,kappa_-).
```

Both are zero. Hence the class of `O(P)|_{2U}` in

```text
ker(Pic(2U)->Pic(U))
  ~= H^1(U,O_U(-U))
```

is zero.

Therefore

```text
O_{2U}(P) ~= O_{2U}.
```

Consequently every multiple also restricts trivially:

```text
O_{2U}(lP) ~= O_{2U}
```

for every `l>=1`.

## Disposition

The reopened first-normal interface closes negatively but exactly:

```text
ordinary holonomy on U         = 1,
first-normal coefficients      = (0,0),
first-neighborhood obstruction = 0,
surviving size-768 orbit        = not excluded.
```

This does not prove formal triviality to all orders and does not construct an effective carrier.

## Next route

The exact local coordinates are now available, so one more bounded formal step is legitimate:

```text
MB104-Z38-SURVIVING-768-SECOND-NORMAL-EXACT-TRANSITION-PREFLIGHT
```

Target: compute the next nonzero term of the branchwise-normalized transition `G` and place it in the exact second formal Picard obstruction group. Stop if the obstruction requires global component data not determined by the local jets.

## Source locks

Current compact branch:

- Z33G note blob `14c1661c5a3b1975474c1f983ed08b29c2150731`;
- Z33G certificate blob `62374fbb19092a2a4a5630fb86b37ddb4924ca29`;
- Z33H note blob `a52a101290c9b2b7024be03858eebd69f67d206d`;
- Z33H certificate blob `9bdd24030ba069e54afccdaa8952400bfa41844b`.

## Firewalls

```text
first_normal_obstruction_computed=true
first_normal_obstruction_nonzero=false
surviving_768_excluded=false
remaining_balanced_support_count=864
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
