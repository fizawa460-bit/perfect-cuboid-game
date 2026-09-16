# Stage32 MB104 — `000707000f0f` e=2 zero-quartic-union residual monodromy

Status: **RETAINED EXACT AMBIENT GENERATOR MATERIALIZATION / ZERO-QUARTIC UNION HAS NONTRIVIAL RESIDUAL GRAPH MONODROMY / CONDUCTOR EDGES STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

The integral complement leaf gives

```text
U=S\B_abs,
H_1(U,Z) ~= Z/2,
alpha_abs = unique nonzero character.
```

This note materializes one explicit geometric loop carrying the nonzero class. It does not identify any carrier conductor loop with that generator.

## 1. The two zero quartics and their two smooth intersections

The retained two-quartic gluing computation for `000707000f0f` fixes

```text
Q0: b1=0,  i*a2-a3=0,  a1-c=0,
Q1: b2=0,  i*a3+a1=0,  a2-c=0.
```

They meet transversely at exactly two smooth points

```text
R_+=[1:1:i:0:0:+sqrt(2):1],
R_-=[1:1:i:0:0:-sqrt(2):1].
```

The box-node sets of `Q0,Q1` contain only the two supported node types, so their strict transforms are disjoint from the absent divisor `B_abs`. Thus

```text
Q0 union Q1 subset U.
```

The dual graph of the union has two vertices and two edges, hence one graph cycle.

## 2. Evaluate the residual `R x R` invariants at the intersections

Use the retained inverse formulas

```text
r_z^2   = 2*(C+W3)/(W1-i*W2),
r_w^2   = 2*(C+W3)/(W1+i*W2),
r_z*r_w = 2*Z3/(C-W3).
```

Under the Stage32 coordinate convention

```text
(W1,W2,W3,Z1,Z2,Z3,C)=(a1,a2,a3,b1,b2,b3,c).
```

At `R_±` all denominators above are nonzero. Exact substitution gives

```text
r_z^2 = 2i,
r_w^2 = 2,
r_z*r_w = ±sqrt(2)*(1+i).                      (INT-R)
```

Choose

```text
u=1+i,  u^2=2i,
a=sqrt(2), a^2=2.
```

Then the two simultaneous-sign residual orbits are

```text
R_+ : {(u,a),(-u,-a)},
R_- : {(u,-a),(-u,a)}.                          (ORB-R)
```

This is an exact field calculation in `Q(i,sqrt(2))`; no numerical square-root choice is used beyond the displayed normalization.

## 3. Component gluing in the residual double cover

The retained zero-quartic splitting convention labels

```text
Q0^+ : r_w=+a,
Q1^+ : r_z=+u,
```

with deck conjugates `Q0^-`,`Q1^-` obtained by simultaneous sign change.

Equation `(ORB-R)` therefore gives the lifted intersection pattern

```text
above R_+:
  Q0^+ meets Q1^+,
  Q0^- meets Q1^-,

above R_-:
  Q0^+ meets Q1^-,
  Q0^- meets Q1^+.                              (GLUE-R)
```

Thus the degree-two cover restricted to the union has lifted dual graph

```text
Q0+ --R+-- Q1+ --R--- Q0- --R+-- Q1- --R--- Q0+,
```

which is connected. Equivalently, transport around the unique downstairs graph cycle exchanges the two residual sheets:

```text
alpha_abs(gamma_Q)=1.                           (Q-MONO)
```

Here `gamma_Q` is any loop that goes from `R_+` to `R_-` along `Q0` and returns from `R_-` to `R_+` along `Q1`.

## 4. `gamma_Q` is the unique ambient generator

Because `Q0 union Q1 subset U`, `gamma_Q` defines a class in `H_1(U,Z)`. The integral complement certificate gives

```text
H_1(U,Z) ~= Z/2
```

and identifies `alpha_abs` as its unique nonzero character. Since `(Q-MONO)` is nonzero,

```text
[gamma_Q] = the unique nonzero class in H_1(U,Z).   (GEN)
```

The canonical linking evaluator therefore also gives

```text
link_abs(gamma_Q)=1.
```

So the previously abstract ambient meridian generator now has a source-locked representative supported entirely on the explicit zero-quartic union.

## 5. Consequence for the active conductor problem

For every conductor-identification loop `lambda_(p;i,j)`, the remaining bit can now be phrased as the exact dichotomy

```text
same residual sheet
  <=> [lambda_(p;i,j)] = 0,

opposite residual sheet
  <=> [lambda_(p;i,j)] = [gamma_Q].             (EDGE-v-GEN)
```

Equivalently, a bounding two-chain for `lambda_(p;i,j)` has even/odd total intersection with `B_abs`.

This fixes a concrete reference generator and the relative orientation of the two zero-quartic split components. It still does not construct the conductor loop itself or determine any branch allocation `x_j`.

## Firewalls

- No conductor edge is identified with `gamma_Q`.
- No branch allocation `x_j` is evaluated.
- No weighted-cut upper bound is claimed.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
