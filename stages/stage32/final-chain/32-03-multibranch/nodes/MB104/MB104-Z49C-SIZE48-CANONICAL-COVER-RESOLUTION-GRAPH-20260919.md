# MB104 Z49C — size48 canonical-cover resolved exceptional graph — 2026-09-19

Status: **PRE-AUDIT EXACT CANONICAL-COVER RESOLUTION GRAPH / NO CREDIT**

## Input

Use one connected size-48 exceptional fiber

```text
Q_1(-4,g=1) -- B(-2,g=0) -- Q_2(-4,g=1)
```

and the Z49B unique degree-three canonical cover.

Near a smooth exceptional point the cover is

```text
x=t^3.
```

At each of the two plumbing nodes the normalized cover is

```text
xy=t^3,
```

an A_2 singularity.

## 1. Q-self-intersections before resolving the A_2 points

Let `Q'_1,B',Q'_2` denote the reduced inverse-image curves on the normal branched cover before
resolving the two A_2 points.

The cover has degree three and is totally ramified along each original component, so

```text
pi^*Q_i = 3Q'_i,
pi^*B   = 3B'.
```

Therefore, in the Q-intersection form on the normal cover,

```text
(Q'_i)^2 = Q_i^2/3 = -4/3,
(B')^2   = B^2/3   = -2/3.                     (Q-SELF)
```

## 2. Local A_2 resolution correction

At a node write the cover as

```text
xy=t^3.
```

Its minimal resolution inserts a chain

```text
F_1(-2) -- F_2(-2).
```

Let `L` and `R` be the two boundary Weil divisors meeting the A_2 point.  If their strict
transforms are `\widetilde L,\widetilde R`, then

```text
f^*L = \widetilde L + (2/3)F_1 + (1/3)F_2,
f^*R = \widetilde R + (1/3)F_1 + (2/3)F_2.
```

This is forced by orthogonality to the exceptional chain:

```text
(f^*L).F_1=(f^*L).F_2=0,
(f^*R).F_1=(f^*R).F_2=0.
```

Hence resolving one A_2 point lowers the self-intersection of each adjacent boundary strict
transform by

```text
2/3.
```

## 3. Global strict-transform self-intersections

Each elliptic component meets exactly one plumbing node, so

```text
\widetilde Q_i^2
 = -4/3 - 2/3
 = -2.
```

The bridge meets two plumbing nodes, so

```text
\widetilde B^2
 = -2/3 - 2/3 - 2/3
 = -2.
```

Therefore after resolving both A_2 points the complete exceptional fiber of the canonical cover is

```text
E_1(-2,g=1)
 -- R_1(-2)
 -- R_2(-2)
 -- R_3(-2)
 -- R_4(-2)
 -- R_5(-2)
 -- E_2(-2,g=1),                                  (COVER-GRAPH)
```

where the two end components are the strict transforms of the elliptic quartics and the five
interior components are rational: four come from the two A_2 resolutions and the middle one is the
strict transform of the original bridge.

Thus the canonical-cover resolution graph is a length-seven chain with every self-intersection
equal to -2 and genera

```text
(1,0,0,0,0,0,1).
```

## 4. Canonical discrepancy on the cover

Let `M` be the 7x7 chain intersection matrix with diagonal -2 and adjacent entries 1.

Adjunction gives

```text
K. E_1 = K. E_2 = 2
```

for the elliptic ends and

```text
K.R_j=0
```

for each rational -2 interior component.

Solving

```text
M a = (2,0,0,0,0,0,2)^T
```

gives

```text
a=(-2,-2,-2,-2,-2,-2,-2).
```

So the canonical index-one cover is Gorenstein, but still strongly non-log-canonical.

## 5. Fundamental cycle

For the reduced full chain

```text
Z = E_1+R_1+...+R_5+E_2,
```

one has

```text
Z.E_1=Z.E_2=-1,
Z.R_j=0
```

for interior components.  Hence Z is anti-nef and is the fundamental cycle.

Its numerical invariants are

```text
Z^2=-2,
K.Z=4,
p_a(Z)=1+(Z^2+K.Z)/2=2.
```

Thus the canonical cover does not turn the size-48 contraction into a rational or minimally
elliptic singularity; the fundamental genus remains two.

## Consequence

Z49B left the next task as:

```text
resolve the two A_2 points,
compute the cover exceptional graph,
then contract and identify the Gorenstein germ.
```

The first two steps are now exact.

The remaining identification problem is narrower:

```text
Gorenstein normal surface germ
with good resolution graph
E(g=1,-2) -- five P1(-2) -- E(g=1,-2),
all discrepancies -2,
fundamental genus 2.
```

No quotient, lc, klt, rational, or minimally-elliptic identification is made.

## Firewalls

```text
size48_cover_resolution_graph_exact=true
all_cover_exceptional_self_intersections_minus2=true
cover_discrepancy_all_minus2=true
cover_fundamental_genus=2
cover_gorenstein=true
cover_log_canonical=false
explicit_affine_cover_equation_known=false
local_symmetric_euler_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
