# MB104 Z50 — exact resolution graph of the size48 canonical index-one cover — 2026-09-19

Status: **PRE-AUDIT EXACT GORENSTEIN-COVER RESOLUTION GRAPH / NO CREDIT**

## Input

Use one size48 nonrational contraction component

```
Q1(-4,g=1) -- B(-2,g=0) -- Q2(-4,g=1)
```

on the smooth cuboid resolution.

Z49 fixes the canonical order-three character.
Z49B proves that its unique holomorphic lift has local models

```
generic exceptional point: x=t^3,
plumbing node:             xy=t^3.
```

Each plumbing node is therefore an A2 singularity on the normalized branched cover.

## 1. Resolve one A2 plumbing node

At a Q--B crossing, write the normalized cover as

```
xy=t^3.
```

Its minimal resolution inserts two rational (-2)-curves

```
Q' -- R1(-2) -- R2(-2) -- B'.
```

For the map to the base plumbing, the Cartier pullbacks of the coordinate divisors have the
standard A2 valuations

```
f^*(x=0)=3Q' + 2R1 + R2,
f^*(y=0)=3B' + R1 + 2R2.
```

This is the toric valuation pattern for xy=t^3.

## 2. Self-intersection of the lifted elliptic component

Projection formula gives

```
f^*Q . Q' = Q . f_*Q' = Q^2 = -4.
```

Since Q' meets only R1,

```
3(Q')^2 + 2 = -4,
```

hence

```
(Q')^2=-2.
```

The same holds for Q2'.

Thus each elliptic (-4) component downstairs becomes an elliptic (-2) component on the resolved
canonical cover.

## 3. Self-intersection of the lifted bridge

The bridge B meets two plumbing nodes.

At each node the A2 pullback of B carries coefficient 2 on the exceptional curve adjacent to B'.
Therefore

```
f^*B . B'
 = 3(B')^2 + 2 + 2
 = B^2
 = -2.
```

Hence

```
(B')^2=-2.
```

## 4. Complete exceptional graph upstairs

Resolving the two A2 points produces the chain

```
E1(-2,g=1)
 -- R1(-2)
 -- R2(-2)
 -- B'(-2,g=0)
 -- R3(-2)
 -- R4(-2)
 -- E2(-2,g=1).
```

All seven components have self-intersection -2.
Only the two endpoints have genus one.

The intersection matrix is the negative A7 Cartan matrix:

```
M50 =
[-2  1  0  0  0  0  0
  1 -2  1  0  0  0  0
  0  1 -2  1  0  0  0
  0  0  1 -2  1  0  0
  0  0  0  1 -2  1  0
  0  0  0  0  1 -2  1
  0  0  0  0  0  1 -2].
```

Its determinant is -8 and its Smith form is

```
diag(1,1,1,1,1,1,8).
```

## 5. Fundamental cycle

Let

```
Z=E1+R1+R2+B'+R3+R4+E2.
```

Then

```
Z.E1=Z.E2=-1,
Z.Ri=0,
Z.B'=0.
```

Thus Z is anti-nef and is the fundamental positive cycle.

Its square is

```
Z^2 = 7(-2)+2*6 = -2.
```

Adjunction gives

```
K.E1=K.E2=2,
K.Ri=K.B'=0.
```

Therefore

```
K.Z=4
```

and

```
p_a(Z)
 = 1 + (Z^2+K.Z)/2
 = 2.
```

The canonical-cover singularity is therefore not rational and not minimally elliptic.

## 6. Gorenstein discrepancy / canonical cycle

Because this is the canonical index-one cover, the contracted germ is Gorenstein.

Solve

```
M50 * a = (2,0,0,0,0,0,2)^T.
```

The unique solution is

```
a=(-2,-2,-2,-2,-2,-2,-2).
```

So every exceptional component has discrepancy -2.

Equivalently the canonical cycle on the resolution is

```
Z_K = -sum a_i E_i = 2Z.
```

This gives an exact numerical Gorenstein model:

```
fundamental cycle Z,
p_a(Z)=2,
canonical cycle Z_K=2Z,
discrepancies all -2.
```

The cover remains non-log-canonical; passing to the index-one cover does not move it into the lc
range.

## 7. Consequence for the analytic-classification route

The size48 canonical cover is no longer an unspecified Gorenstein germ.
Its minimal good resolution graph and canonical cycle are exact:

```
(g=1,-2)--(-2)--(-2)--(g=0,-2)--(-2)--(-2)--(g=1,-2),
Z_K=2Z.
```

A future classification search must target Gorenstein surface singularities with exactly this
marked resolution data, not arbitrary index-one covers.

This is sufficiently narrow to reopen a bounded literature/explicit-equation classification pass.

## 8. Next leaf

```
MB104-Z51-SIZE48-GORENSTEIN-GERM-CLASSIFICATION-PREFLIGHT
```

Target:

1. search for classifications or normal forms of Gorenstein surface singularities with
   `Z_K=2Z`, `p_a(Z)=2`, and the above two-elliptic-end A7-shaped graph;
2. if a source-complete analytic normal form exists, materialize it and compute the local symmetric
   Euler/Chern correction;
3. if classification has moduli, identify the exact moduli and test whether Z48 cuboid
   `j=1728`/marked-point data selects finitely many values.

Do not call the graph rational A7: only the intersection matrix is A7; the endpoint components are
elliptic.

## Firewalls

```
cover_resolution_graph_exact=true
all_upstairs_self_intersections_minus2=true
fundamental_cycle_genus=2
canonical_cycle_equals_2Z=true
upstairs_discrepancies_all_minus2=true
upstairs_log_canonical=false
explicit_affine_equation_known=false
local_symmetric_euler_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
