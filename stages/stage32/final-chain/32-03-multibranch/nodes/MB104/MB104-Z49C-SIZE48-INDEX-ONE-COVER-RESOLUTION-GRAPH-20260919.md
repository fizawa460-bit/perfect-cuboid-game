# MB104 Z49C — size48 index-one cover resolution graph — 2026-09-19

Status: **PRE-AUDIT EXACT CANONICAL-COVER RESOLUTION GRAPH / NO CREDIT**

## Input

Z49B gives the unique holomorphic degree-three canonical cover over one size48 plumbing component.

On the resolution plumbing

```text
Q_1(-4,g=1) -- B(-2,g=0) -- Q_2(-4,g=1)
```

the cover is totally ramified of order three along every component.  At each transverse Q--B
attachment the normalized local cover is

```text
xy=t^3,
```

an A_2 rational double point.

Z49C resolves those two A_2 points and computes the exceptional graph of the index-one cover.

## 1. Self-intersection before resolving the A2 nodes

Let

```text
pi:X' -> S
```

be the normal degree-three cyclic cover of the plumbing neighborhood.

For a branch component R downstairs and its reduced ramification curve R' upstairs,

```text
pi^*R = 3R'.
```

Intersection projection gives

```text
(pi^*R)^2 = 3 R^2,
```

hence, as Q-Cartier intersection numbers on X',

```text
(R')^2 = R^2/3.
```

Therefore

```text
Q_i'{}^2 = -4/3,
B'{}^2   = -2/3.
```

The only singularities of X' along this configuration are the two A_2 points over the two
plumbing nodes.

## 2. Local A2 correction

At one node the cover is

```text
xy=t^3.
```

Its minimal resolution inserts a chain

```text
A_1(-2)--A_2(-2).
```

The strict transforms of the two coordinate-axis ramification curves attach to opposite ends.

For one axis curve R through the A2 point, write its Mumford pullback as

```text
f^*R = R_tilde + a A_1 + b A_2,
```

with R_tilde meeting A_1 once and not A_2.  Orthogonality to the exceptional curves gives

```text
1-2a+b=0,
a-2b=0.
```

Hence

```text
a=2/3,
b=1/3.
```

Thus

```text
R^2 = R_tilde^2 + 2/3,
R_tilde^2 = R^2 - 2/3.                         (A2-CORR)
```

## 3. Strict-transform self-intersections

Each elliptic ramification curve meets one A2 point.  Hence

```text
Q_i_tilde^2
 = -4/3 - 2/3
 = -2.
```

The rational bridge meets both A2 points, so it receives the correction twice:

```text
B_tilde^2
 = -2/3 - 2/3 - 2/3
 = -2.
```

Therefore after resolving both A2 points the complete exceptional configuration is the seven-term
chain

```text
Q_1~(-2,g=1)
-- A_1(-2)
-- A_2(-2)
-- B~(-2,g=0)
-- A_3(-2)
-- A_4(-2)
-- Q_2~(-2,g=1).                                (COVER-GRAPH)
```

All intersections are transverse and consecutive.

## 4. Discrepancies on the index-one cover resolution

Let

```text
psi:X_tilde -> Y^#
```

be the resulting resolution of the canonical index-one cover germ.

Because Y^# is Gorenstein, write

```text
K_Xtilde = psi^*K_Y# + sum a_i E_i.
```

Adjunction gives

```text
K_Xtilde.Q_i_tilde = 2
```

for each elliptic endpoint of self-intersection -2, and

```text
K_Xtilde.E = 0
```

for every rational (-2) interior component.

For the seven-chain intersection matrix, the unique solution is

```text
a_i=-2
```

for all seven components.

Indeed at an endpoint

```text
-2(-2)+(-2)=2,
```

and at every interior vertex

```text
(-2)-2(-2)+(-2)=0.
```

Thus the canonical cover germ is Gorenstein but still non-log-canonical:

```text
all discrepancies = -2.
```

This is compatible with the fact that taking the index-one cover removes the denominator but does
not repair the non-lc nature of the original contraction.

## 5. Fundamental cycle checksum

Let Z be the reduced sum of all seven exceptional components.

The seven-chain has six edges, so

```text
Z^2 = 7*(-2)+2*6 = -2.
```

Also

```text
K_Xtilde.Z = 2+2 = 4.
```

Hence

```text
p_a(Z)
 = 1 + (Z^2+K.Z)/2
 = 1 + (-2+4)/2
 = 2.
```

The reduced exceptional divisor is already anti-nef:

```text
Z.Q_endpoint=-1,
Z.E_interior=0.
```

So it is the fundamental cycle.

## 6. Consequence

The size48 canonical cover is no longer an unspecified Gorenstein cover.

Its minimal good-resolution data are exact:

```text
graph: seven consecutive (-2) vertices,
endpoint genera: 1,1,
interior genera: 0,
discrepancy vector: (-2,-2,-2,-2,-2,-2,-2),
fundamental genus: 2.
```

This is materially stronger than the original Z43 wall.

The remaining local problem is now:

```text
identify/classify Gorenstein surface germs with this exact resolved marked plumbing,
or compute the needed local symmetric-Euler/Chern invariant from this source-complete cover data.
```

No quotient, lc, or rational-double-point classification of the contracted germ is asserted.

## Firewalls

```text
size48_cover_resolution_graph_exact=true
cover_A2_nodes_resolved=true
cover_discrepancy_vector_exact=true
cover_fundamental_genus=2
cover_gorenstein=true
cover_log_canonical=false
cover_analytic_equation_global_known=false
local_symmetric_euler_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
