# MB104 Z56 — maximal-ideal generators split into exceptional and first-normal parts — 2026-09-19

Status: **PRE-AUDIT EXACT GENERATOR DECOMPOSITION / ONE SCALAR TANGENT RECEIVER / NO CREDIT**

## Input

Use the size48 canonical-cover resolution

```
D=E_L-C1-C2-C3-C4-C5-E_R
```

with all self-intersections -2, elliptic endpoints, and maximal ideal cycle

```
F=Z+Gamma=(1,2,2,2,2,2,1).
```

Z53 gives

```
-F.(E_L,C1,C2,C3,C4,C5,E_R)
=(0,1,0,0,0,1,0).
```

Konno type-(II), m=1 gives

```
m O_X = O_X(-F),
embdim=4.
```

## 1. Exact restriction of O(-F) to D

Put

```
L=O_D(-F).
```

On the elliptic endpoints, F=Z+Gamma and the unique attachment point is p.  Since

```
O_E(-Z) ~= O_E(p),
O_E(-Gamma) ~= O_E(-p),
```

we get

```
L|E_L ~= O_E,
L|E_R ~= O_E.
```

On the rational chain the degrees are

```
deg L|C1=1,
deg L|C2=deg L|C3=deg L|C4=0,
deg L|C5=1.
```

Hence the normalization components contribute dimensions

```
1+2+1+1+1+2+1=9.
```

The dual graph is a tree with six nodes.  Evaluation at every node is surjective because O(1) on
C1,C5 is globally generated and all degree-zero component bundles are trivial.  Therefore

```
h0(D,L)=9-6=3,
h1(D,L)=0.
```

The complete linear system |L| maps the reduced exceptional divisor onto two distinct intersecting
lines, as retained in Z54.

## 2. The fourth tangent generator vanishes on D

The singularity has embedding dimension four, so

```
dim_C m/m^2=4.
```

The three independent restrictions above account for only three tangent generators.

Use the exact sequence

```
0 -> O_X(-F-D)
  -> O_X(-F)
  -> O_D(-F)
  -> 0.
```

The missing tangent direction can therefore be represented by a section

```
x in H0(O_X(-F-D))
```

whose class is nonzero modulo m^2.

Thus choose tangent generators

```
x,y,z,w
```

so that

```
x|D=0,
(y,z,w)|D span H0(D,L).
```

This identifies the Z54 coordinate x intrinsically as the unique tangent direction invisible on the
reduced exceptional cycle.

Cycle comparison explains why such a direction is possible:

```
F+D = (2,3,3,3,3,3,2),
2F  = (2,4,4,4,4,4,2).
```

So the strip

```
O_X(-F-D) / O_X(-2F)
```

is supported exactly on the central A5 chain.

## 3. Quadratic relations

On the reduced exceptional image, the three visible sections can be chosen so that its two-line
equation is

```
yz=0.
```

Because x restricts to zero on D, the lift of this reduced relation to gr_m degree two may differ
from zero only by a quadratic term containing x.

After the Z54 projective normalizations, x^2 is one quadratic relation and all remaining inessential
x-linear terms can be removed except xw.  Therefore the degree-two multiplication is controlled by
a single scalar c:

```
q1=x^2,
q2=yz + c xw.                                  (Z56-SCALAR)
```

Projectively only

```
c=0
or
c!=0
```

matters.

Thus

```
c=0   <=> T0,
c!=0  <=> T1.
```

## 4. Cohomological meaning of c

The scalar c is not an arbitrary tangent-pencil modulus.  It is the obstruction to the reduced
relation yz=0 lifting one order further while keeping the first-normal generator x separated.

Equivalently it is the image of the product yz in the one-dimensional quotient of the
first-normal strip that survives in degree two after modding out by coordinate changes and m^3.

This is the precise algebraic interface between

```
explicit plumbing / first-normal transition
```

and

```
quadratic tangent pencil.
```

No identification with the earlier Picard H1 class is asserted without an adapter.

## 5. Bounded reconstruction target

To decide c, it is enough to materialize:

1. one section x with cycle >=F+D but not >=2F;
2. arm sections y,z whose restrictions generate the two degree-one arms;
3. one common section w nonzero at the central contracted image;
4. the coefficient of xw in yz modulo m^3.

No complete local equation is needed.

## 6. Next leaf

```
MB104-Z57-CENTRAL-A5-FIRST-NORMAL-MULTIPLICATION
```

Compute the one-dimensional quotient

```
Q = H0(O_X(-2F))? / filtration
```

in a source-correct Rees formulation and evaluate whether the class of yz along the central A5
strip is zero or nonzero.

If direct contraction sections remain unavailable, use the explicit A1/cyclic-cover plumbing charts
to compute transition functions only on the five central rational components.

## Firewalls

```
fourth_generator_first_normal=true
h0_exceptional_visible_generators=3
single_tangent_scalar_receiver=true
actual_scalar_zero_or_nonzero_known=false
actual_tangent_type_selected=false
equivariant_smoothing_known=false
downstairs_local_correction_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
