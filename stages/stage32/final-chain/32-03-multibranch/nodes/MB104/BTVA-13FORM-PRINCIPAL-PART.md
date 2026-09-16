# Stage32 MB104 — BTVA 13-form A1 principal-part interface

Status: **RETAINED BRANCH-SENSITIVE LOCAL RESULT / MB104 INCOMPLETE / NO CREDIT**

## Purpose

The previous MB104 preflight identified the 13-dimensional order-two reflexive symmetric-differential space used by Bruin--Thomas--Varilly-Alvarado (BTVA) as the next concrete branch-sensitive object. This checkpoint materializes the local principal-part map at representatives of the two classical 24-node coordinate families, proves maximal rank three, and identifies exactly what one minimal cusp branch asks of that map.

This is useful both positively and negatively: it gives an exact landing-direction condition for a minimal branch, but it also shows that order-two principal parts saturate after three distinct landing directions at one node. Therefore this 13-form portfolio, by itself, cannot count arbitrary branch multiplicity `R8` at a fixed node.

## Immutable external inputs

BTVA:

- Nils Bruin, Jordan Thomas, Anthony Varilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Algebra & Number Theory 16 (2022), 1377--1405, arXiv:1912.08908v3.
- immutable ancillary output: `https://arxiv.org/src/1912.08908v3/anc/perfectcuboid.out`.
- the ancillary computation constructs the degree-zero part of `hat S^2 Omega_X`, verifies that it has 13 displayed affine generators `forms[1]...forms[13]`, and writes them in the `x1=1`, local-parameter basis `(dx2^2, dx2*dx3, dx3^2)`.

Stoll source lock already used by MB103:

- repository `MichaelStollBayreuth/Verification`
- commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`
- file `Cuboids/cuboids.magma`
- blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`

Its nine displayed coordinate substitutions generate the order-1536 geometric automorphism action used below.

## Local A1 principal-part lemma

Write the A1 cone as

```text
xz = y^2,
x = u^2,
y = u v,
z = v^2.
```

On the resolution chart

```text
s = u^2,
t = v/u,
```

a constant order-two tensor on the double cover

```text
Q = a du^2 + b du dv + c dv^2
```

has exceptional principal part

```text
Q = (a + b t + c t^2) ds^2/(4s) + regular terms.
```

Thus its pole polynomial is the homogeneous binary quadratic represented in this chart by

```text
P_Q(t)=a+b t+c t^2.
```

For an FSM-minimal branch `(A,B)=(1,1)`, MB101 gives exceptional multiplicity one. In resolution coordinates it has

```text
s = tau,
t = lambda + O(tau).
```

Therefore the pullback of `Q` to that normalization branch is regular at the exceptional point iff

```text
P_Q(lambda)=0.
```

The homogeneous formulation on `P^1` includes the landing direction at infinity.

Consequences at one node:

- one distinct minimal landing direction imposes at most one linear condition on a space of order-two forms;
- two distinct landing directions impose at most two;
- three distinct landing directions force the whole binary quadratic principal part to vanish, i.e. full regularity at that node;
- any additional distinct landing directions impose no new order-two principal-part condition;
- repeated branches with the same landing direction impose the same principal pole-cancellation condition.

This saturation statement concerns only the order-two exceptional principal part. It does not claim that repeated branches are globally unconstrained.

## Representative R1

Use

```text
R1=[1:0:0:0:1:1:1].
```

On `x1=1`, the local equations give

```text
y1^2=x2^2+x3^2,
y2^2=1+x3^2,
y3^2=1+x2^2,
z^2=1+x2^2+x3^2.
```

A double-cover parametrization of the tangent A1 cone is

```text
x2=(u^2-v^2)/2,
x3=u v,
y1=(u^2+v^2)/2.
```

Substituting the 13 BTVA affine forms and taking the constant tensor on the double cover gives the following rows in basis `(du^2,du dv,dv^2)`:

```text
omega01  ( 0,  0,  0)
omega02  ( 0, -2,  0)
omega03  ( 1,  0, -1)
omega04  ( 0,  0,  0)
omega05  ( 1,  0, -1)
omega06  ( 0,  2,  0)
omega07  ( 1,  0,  1)
omega08  ( 0,  0,  0)
omega09  ( 0,  0,  0)
omega10  ( 0,  0,  0)
omega11  ( 1,  0,  1)
omega12  ( 1,  0,  1)
omega13  ( 1,  0,  1)
```

Hence the local principal-part image is all of `Sym^2(C^2)`: rank `3`.

Equivalently, the portfolio already contains pole polynomials proportional to

```text
t,
1-t^2,
1+t^2,
```

which span the full quadratic space.

## Representative R2

Use

```text
R2=[1:i:0:i:1:0:0].
```

Here a convenient tangent-cone model is obtained from

```text
b=x3,
e=y3,
f=z,
b^2+e^2=f^2,
```

with double-cover parametrization

```text
b=(u^2-v^2)/2,
e=u v,
f=(u^2+v^2)/2.
```

Using `x2^2=e^2-1`, `y1^2=f^2-1`, and `y2^2=1+b^2`, the same 13 ancillary forms give

```text
omega01  (-i,  0,  i)
omega02  ( 1,  0, -1)
omega03  ( i,  0,  i)
omega04  (-1,  0, -1)
omega05  ( 0,  0,  0)
omega06  ( 0,  0,  0)
omega07  ( 0, 2i,  0)
omega08  ( 0, -2,  0)
omega09  ( 0,  0,  0)
omega10  ( 0, -2,  0)
omega11  ( 0, 2i,  0)
omega12  ( 0,  0,  0)
omega13  ( 0,  0,  0)
```

Again the rank is `3`.

## All 48 nodes

The 48 nodes are the six eight-point coordinate families

```text
[1:0:0:0:+/-1:+/-1:+/-1],
[0:1:0:+/-1:0:+/-1:+/-1],
[0:0:1:+/-1:+/-1:0:+/-1],
[1:+/-i:0:+/-i:+/-1:0:0],
[0:1:+/-i:0:+/-i:+/-1:0],
[+/-i:0:1:+/-1:0:+/-i:0].
```

A direct replay using the nine Stoll coordinate substitutions from the fixed `cuboids.magma` source sends `R1` through a single orbit of size `48`. Pullback by a surface automorphism identifies the intrinsic 13-dimensional reflexive order-two space and carries the A1 principal-part map equivariantly. Therefore maximal rank `3` holds at every one of the 48 nodes.

This does **not** materialize a chosen 3-by-13 coefficient matrix in a fixed local basis at all 48 labels. It materializes the intrinsic rank-three map at every node and exact representative matrices sufficient for the branch-direction conclusion.

## MB104 consequence

Let `s_i` be the number of **distinct exceptional landing directions** among FSM-minimal `(1,1)` branches over node `i`. For the BTVA order-two space `V_13`, the subspace whose principal pole cancels on every such minimal branch has codimension at node `i` at most

```text
min(3,s_i).
```

Hence globally the order-two portfolio sees at most

```text
sum_i min(3,s_i)
```

linear principal-part conditions, not the branch multiplicity

```text
R8=sum_i r8_i.
```

In particular, arbitrarily many minimal branches concentrated in already-used landing directions do not create additional order-two principal-part conditions. Even with many distinct directions, the local contribution saturates at three per node.

Therefore the BTVA 13-form order-two principal-part portfolio **cannot by itself provide the missing linear upper bound on `R8`** required by

```text
d <= 16g-16+4R8.
```

A successful continuation must use information that does not saturate at order two: e.g. higher-order principal parts/jets, a conductor or intersection mechanism that charges repeated branches, or another global constraint coupling branch multiplicity to degree.

## Firewalls

- `MB104_complete=false`.
- no absolute `R8` upper bound is proved.
- no finite degree window is released.
- no finite Picard enumeration is released.
- no receiver/effectivity/theorem/endpoint credit.
- no Perfect Cuboid existence or nonexistence claim.
- no merge authorization.
