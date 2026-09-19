# MB104 Z52 — size48 canonical cover: quadratic complete intersection and Milnor number 31 — 2026-09-19

Status: **PRE-AUDIT EXACT LOCAL-CI NUMERICS / NO CREDIT**

## Input

Z51 gives for the size48 canonical index-one cover germ

```
dim = 2,
Gorenstein = true,
complete intersection codimension = 2,
embedding dimension = 4,
multiplicity = 4,
p_g = 3.
```

Z50 gives on the minimal good resolution

```
Z_K = 2Z,
Z^2=-2,
Z_K^2=-8,
e(E_red)=4.
```

Here the reduced exceptional divisor is the seven-component chain with two elliptic endpoints and five rational components.

## 1. Initial orders are exactly (2,2)

Write the completed local ring as

```
R ~= C[[x1,x2,x3,x4]]/(f,g)
```

with f,g a minimal regular sequence.

Because the embedding dimension is four, neither f nor g has a linear term. Hence

```
ord(f)>=2,
ord(g)>=2.
```

For a codimension-two complete intersection, local intersection multiplicity satisfies

```
e(R) >= ord(f) ord(g).
```

Since e(R)=4, we get

```
4 >= ord(f)ord(g) >=4.
```

Therefore

```
ord(f)=ord(g)=2.
```

Equality in the complete-intersection multiplicity bound means the quadratic initial forms form a regular sequence. Thus

```
gr_m(R) ~= C[x1,x2,x3,x4]/(q1,q2)
```

for a regular sequence of two quadrics q1,q2.

Equivalently the projectivized tangent cone is a degree-four (2,2) complete-intersection curve in P3, with arithmetic genus one as a scheme.

No smoothness or irreducibility of that tangent-cone curve is asserted.

## 2. Laufer-Steenbrink Milnor number

The germ is a local complete intersection, hence smoothable.

For a smoothable Gorenstein normal surface singularity, the Laufer-Steenbrink formula is

```
mu + 1 = e(X_tilde) + K^2 + 12 p_g.
```

A sufficiently small good-resolution neighborhood retracts onto its exceptional divisor, so here

```
e(X_tilde)=e(E_red).
```

For the seven-component chain:

- the two elliptic endpoints contribute Euler number 0;
- the five rational components contribute 5*2=10;
- the six transverse intersection points are counted twice before gluing.

Hence

```
e(E_red)=10-6=4.
```

Also

```
K^2 = Z_K^2 = (2Z)^2 = 4(-2) = -8,
p_g=3.
```

Therefore

```
mu+1 = 4-8+36 = 32,
mu = 31.
```

So every smoothing of this Gorenstein complete-intersection germ has Milnor number 31.

## 3. Exact analytic package

The size48 canonical cover now has:

```
ICIS in C4,
two defining equations of order two,
quadratic tangent cone = (2,2) complete intersection,
p_g=3,
mu=31,
resolution type = type (ii.a),
j=1728 elliptic endpoint neighborhoods,
central fixed A5 chain.
```

This is substantially narrower than the Z43 "unknown index-one cover".

## 4. What remains

The pair of tangent quadrics is not yet source-identified.

In particular, the cuboid j=1728 endpoint data do not automatically imply that the projectivized tangent-cone quartic is the same elliptic quartic as either exceptional endpoint.

That semantic identification requires a new adapter.

Likewise, mu=31 by itself does not supply the local symmetric-Euler coefficient needed downstairs.

## 5. Next leaf

```
MB104-Z53-SIZE48-QUADRATIC-PENCIL-AND-EQUIVARIANT-MILNOR-PREFLIGHT
```

Two shallow targets:

1. determine the degeneration type of the tangent quadratic pencil from Konno type (ii.a), the maximal ideal cycle F=Z+A5, and the marked j=1728 endpoints;
2. determine whether the canonical deck mu_3 action on the Milnor fiber can be recovered from the explicit branched plumbing strongly enough to compute the downstairs equivariant/local correction.

Do not identify the tangent-cone elliptic curve with a cuboid quartic without proof.

## Literature anchors

- K. Konno, *Certain normal surface singularities of general type*, for the even-Gorenstein type-(ii.a), p_g, multiplicity and embedding dimension package.
- Laufer-Steenbrink formula for smoothable Gorenstein normal surface singularities:
  `mu+1=e(X_tilde)+K^2+12p_g`.

## Firewalls

```
tangent_quadratic_pencil_explicit=false
projectivized_tangent_cone_smooth=false
projectivized_tangent_cone_identified_with_cuboid_quartic=false
deck_action_on_vanishing_cohomology_known=false
downstairs_local_correction_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
