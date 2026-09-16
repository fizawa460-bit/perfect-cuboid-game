# Stage32 MB104 — balanced16 two-zero-quartic gluing obstruction

Status: **RETAINED EXACT FIXED-COMPONENT OBSTRUCTION / ONE 768 SUPPORT ORBIT CLOSED FOR UNIFORM P5 RAY / BALANCED16 STILL OPEN / NO CREDIT**

## Scope

Let

```text
A = 7H - 4 sum_{i in Sigma} E_i,
D_l = lA, l>=1,
```

for one of the two balanced support representatives

```text
000707000f0f,
00070b000f0f.
```

Both representatives have the same two zero-pairing retained elliptic quartics, but differ in one omitted box node. The previous leaves prove `O_Q(D_l)` is trivial on each zero quartic separately. The present leaf computes the gluing across the **two smooth intersection points** of the quartics.

## The two zero quartics

Write the surface equations as

```text
q1=a1^2+a2^2-b3^2,
q2=a2^2+a3^2-b1^2,
q3=a1^2+a3^2-b2^2,
q4=a1^2+a2^2+a3^2-c^2.
```

The two zero quartics are

```text
Q0: b1=0,  i*a2-a3=0,  a1-c=0,
Q1: b2=0,  i*a3+a1=0,  a2-c=0.
```

Combining the linear equations gives

```text
a1=a2=c=t,
a3=i*t,
b1=b2=0.
```

Then `q1=0` gives `b3^2=2t^2`. Projectively `t!=0`, so

```text
Q0 cap Q1 = {R_+,R_-},
R_±=[1:1:i:0:0:±sqrt(2):1].
```

The intersection scheme is reduced: the remaining equation is `b3^2-2t^2`, with two distinct roots in characteristic zero. A direct Jacobian minor on columns `(a1,a2,a3,c)` has determinant `-32i`, so both points are smooth on the cuboid surface. Hence the strict transforms meet transversely in exactly these two smooth points.

## Explicit component trivializations

On `Q0`, use coordinates

```text
x=a1, y=a2, z=b2, w=b3,
z^2=x^2-y^2,
w^2=x^2+y^2.
```

Its eight box nodes are the divisor of `x*y`, so `B_Q0=div(xy)`. On `Q1`, use

```text
x=a2, y=a3, z=b3, w=b1,
z^2=x^2-y^2,
w^2=x^2+y^2,
```

and again `B_Q1=div(xy)`, now represented by the ambient form `a2*a3`.

For a zero quartic with omitted box node `P`, the previous Pic^0 leaf gives a hyperflex linear form `L_P` with `div_Q(L_P)=4P`. Choosing the common ambient hyperplane `M=c`, a rational trivialization of `A|_Q` away from its divisor is

```text
tau_Q = c^7 * L_P / G_Q^4,
```

where `G_Q` is `a1*a2` on `Q0` and `a2*a3` on `Q1`.

At `R_±`, `c=1`, `(a1*a2)^4=1` and `(a2*a3)^4=i^4=1`, so the gluing multipliers are controlled only by the hyperflex forms.

## Representative `000707000f0f`: gluing is trivial

Here the omitted nodes are

```text
Q0: P27,
Q1: P35.
```

Exact hyperflex forms are

```text
L27 = -2*a2 + b3 + i*b2,
L35 = -2*a3 - b1 + i*b3.
```

On `R_±`, with `s=sqrt(2)`,

```text
L27(R_±) = -2 ± s,
L35(R_±) = i(-2 ± s).
```

Thus

```text
tau_Q0/tau_Q1 = -i
```

at both intersection points. After rescaling one component trivialization the two gluing constants agree, so `A` restricts trivially to the connected union `Q0 union Q1`. The same is true for every `D_l=lA`. This route does not close `000707000f0f`.

## Representative `00070b000f0f`: nontrivial gluing for every l

Here the omitted nodes are

```text
Q0: P26,
Q1: P35.
```

The hyperflex forms are

```text
L26 = -2*a2 - b3 + i*b2,
L35 = -2*a3 - b1 + i*b3.
```

Hence

```text
lambda_+ = (-2-s)/(i(-2+s)),
lambda_- = (-2+s)/(i(-2-s)).
```

The cycle monodromy of `A` is

```text
mu = lambda_+/lambda_-
   = ((2+s)/(2-s))^2
   = 17+12s.
```

This is a positive real algebraic number strictly greater than `1`, so `mu^l != 1` for every integer `l>=1`.

For two smooth components meeting at two reduced points, a multidegree-zero line bundle that is trivial on each component has a nonzero global section iff its two gluing constants agree. Therefore

```text
H^0(Q0 union Q1, O(D_l)) = 0
```

for `00070b000f0f` and every `l>=1`.

Every global section of `O_S(D_l)` therefore restricts to zero on the union. Both zero quartics are fixed components of every effective divisor in the class, so **no irreducible effective divisor in the displayed uniform P5 ray exists on this support orbit**.

By `Aut(S)` transport, the entire support orbit of size `768` represented by `00070b000f0f` is closed for the displayed uniform ray.

## Updated uniform-P5 hard core

The previous four support orbits

```text
48, 48, 768, 768
```

are reduced to

```text
48, 48, 768
```

with canonical masks

```text
0000770000ff,
00007b0000ff,
000707000f0f.
```

Thus the surviving balanced support population drops from `1632` to `864` for this ray.

This does not close arbitrary unequal Picard classes, support-span five as a whole, genus-one P6, genus-zero P6, MB104, or any receiver/theorem/endpoint claim. No merge authorization.
