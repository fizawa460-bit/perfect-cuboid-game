# MB104 Z48 — explicit negative-elliptic neighborhood model — 2026-09-19

Status: **PRE-AUDIT EXACT ANALYTIC-INPUT COMPRESSION / NEW ADAPTER / NO CREDIT**

## Purpose

Z43 stopped because the weighted resolution graph and discrepancy vector do not determine the analytic
canonical index-one cover.

Z48 does not infer an analytic type from the graph.  Instead it uses the **actual cuboid elliptic
quartics** and their exact embeddings to reduce the missing analytic input.

The result is a genuine new adapter: every elliptic (-4) component occurring in the three surviving
balanced contractions has an explicit j-invariant, explicit normal bundle and explicit marked
intersection points.

It does **not** yet classify the complete connected contracted germ.

## 1. Representative quartic and its j-invariant

Z33E gives an exact representative

```
Q:
y^2=x^2+t^2,
z^2=x^2-t^2
```

as the complete intersection of two quadrics in P3.

For the pencil `lambda Q1 + mu Q2`, in coordinates `(x,t,y,z)` the diagonal determinant is,
up to a nonzero scalar,

```
lambda * mu * (lambda^2-mu^2).
```

Hence the four singular members of the pencil occur at

```
[lambda:mu] = 0, infinity, 1, -1.
```

The associated double-cover branch cross-ratio may be taken as `-1`.  The Legendre formula gives

```
j(-1)
 = 256(1-(-1)+(-1)^2)^3 / ((-1)^2(1-(-1))^2)
 = 1728.
```

Therefore every retained elliptic quartic, being an Aut(S)-translate of the source family, has

```
j(Q)=1728.
```

## 2. Exact normal bundle

Each retained quartic satisfies

```
Q^2=-4,
K_S=H,
K_Q~=O_Q.
```

Adjunction gives

```
O_Q(Q)
 ~= K_Q tensor (K_S|Q)^(-1)
 ~= O_Q(-H).
```

Z33E proves that every retained box-node point p on Q is a hyperflex:

```
H|Q ~ 4p.
```

Thus, for any such retained node p,

```
N_(Q/S)
 = O_Q(Q)
 ~= O_Q(-H)
 ~= O_Q(-4p).                                  (Z48-NORMAL)
```

In particular the normal bundle is not merely known by degree: its Picard class is exact.

## 3. Analytic neighborhood compression

A smooth elliptic curve with negative normal bundle is in the negative-neighborhood regime of
Grauert's formal/analytic principle.  For the present component

```
deg N_(Q/S)=-4<0.
```

Accordingly the germ of the surface along an individual Q is analytically linearizable to the germ
of the zero section in its normal bundle.

For the retained quartics this reduces the individual component-neighborhood input to

```
(E_1728, O_E(-4p)).
```

Translation may move the single marked point p to the origin; because multiplication by four on
the complex elliptic curve is surjective, the degree -4 normal-bundle class introduces no further
uncontrolled continuous parameter at the one-marked-component level.

This statement is only componentwise.  It does not identify the analytic type of a connected
multi-component contraction without checking the plumbing/gluing.

## 4. Size-48 contraction input

Each nonrational connected exceptional fiber is

```
Q1(-4,g=1) -- E(-2) -- Q2(-4,g=1).
```

The bridge meets each elliptic quartic at the retained omitted box node.  Hence each elliptic side is
of the exact marked form

```
(E_1728,p,N=O(-4p)).
```

The rational bridge has self-intersection -2 and one transverse attachment at each end.

Therefore the previous Z43 phrase "unknown analytic germ with this graph" can be sharpened:

```
unknown data =
  gluing/plumbing of two standard negative E_1728 neighborhoods
  to the (-2) bridge at the two exact transverse attachment points,
not arbitrary deformations of the elliptic component neighborhoods.
```

There are two disconnected copies of this connected fiber on each size-48 support.

## 5. Size-768 contraction input

The connected nonrational fiber has

```
A^2=B^2=-4,
A.B=2,
one (-2) leaf on each component.
```

Z33G gives the two smooth intersection points exactly:

```
r_+ = (1,1,i,0,0,+sqrt(2),1),
r_- = (1,1,i,0,0,-sqrt(2),1).
```

Both A and B are retained elliptic quartics, hence each has j=1728 and normal bundle O(-H).
Their omitted-node leaf attachments and the pair (r_+,r_-) are explicit marked points in the
source equations.

Thus the size-768 local problem also has a finite explicit marked-plumbing input; the remaining
analytic uncertainty is the compatibility of the standard negative neighborhoods across those
specified transverse gluings.

## 6. What Z48 changes

Z43 correctly forbids:

```
graph -> analytic type
```

by itself.

Z48 provides additional source geometry:

```
graph
+ exact elliptic equations
+ j=1728
+ exact normal bundles O(-H)=O(-4p)
+ exact attachment/intersection points.
```

So a future local canonical-cover computation need not start from an arbitrary normal surface
singularity with the same graph.  It may start from an explicit plumbing problem.

This is the new adapter required by the Class-3 boundary.

## 7. Next leaf

```
MB104-Z49-EXPLICIT-PLUMBING-CANONICAL-COVER-PREFLIGHT
```

First work on one size-48 Q-E-Q component because it has no dual-graph cycle and only one marked
point on each elliptic component.

Target:

1. construct transition coordinates from the linearized models
   `Tot(O_E(-4p))` and the `(-2)) bridge;
2. use the exact canonical divisor/discrepancy relation to identify the local index-three canonical
   algebra on the punctured plumbing;
3. determine whether the degree-three index-one cover is forced into an explicit hypersurface,
   complete-intersection, or other source-complete analytic model;
4. only then return to local Chern/Euler theory.

If the plumbing still contains an uncontrolled modulus after the exact marked data are imposed,
record that modulus explicitly instead of reverting to the generic Z43 wall.

## Sources

Repository source locks:

- Z33E exact quartic/hyperflex note;
- Z33G exact size-768 intersection-point note;
- Z41/Z43 exact contraction/index-three notes.

External analytic input:

- Grauert negative-neighborhood/formal principle for curves with negative normal bundle.
  The theorem is used only to linearize each individual negative elliptic component neighborhood,
  not to classify the complete reducible exceptional fiber.

## Firewalls

```
elliptic_component_j_exact=1728
elliptic_component_normal_bundle_exact=true
individual_negative_neighborhood_linearized=true
connected_plumbing_analytic_type_classified=false
canonical_cover_equation_known=false
local_symmetric_euler_coefficient_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
