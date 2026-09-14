# Stage32 MB104 — `000707000f0f` e=2 exact residual node-orbit table

Status: **RETAINED EXACT `R x R` NODE-ORBIT REFINEMENT / BRANCH ALLOCATION AND CONDUCTOR TRANSITION STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP
```

for the dangerous equality packet

```text
Sigma=000707000f0f,
node-type counts=(7,7,0),
8*l normalization branches at every supported node.
```

The retained residual coordinate on one level-eight factor is

```text
r = theta10(z)/theta10(2z),
R=C8/H ~= P1_r,
T H : r -> -r.
```

This leaf materializes the exact residual `R x R` orbit of every supported box node. It does **not** choose, for an individual normalization branch, one member of that two-point simultaneous-sign orbit.

## 1. Inverting the box theta products to residual coordinates

For the two level-eight factors write

```text
x=theta00(2z), y=theta10(2z), e_z=theta10(z),
X=theta00(2w), Y=theta10(2w), e_w=theta10(w).
```

The retained theta source gives

```text
e_z^2=2*x*y,
e_w^2=2*X*Y,
```

and the box coordinates

```text
C  = xX+yY,
W1 = yX+xY,
W2 = i*(yX-xY),
W3 = xX-yY,
Z3 = e_z*e_w.
```

Put

```text
r_z=e_z/y,
r_w=e_w/Y.
```

On the finite chart containing all fourteen supported nodes, direct elimination gives

```text
r_z^2   = 2*(C+W3)/(W1-i*W2),
r_w^2   = 2*(C+W3)/(W1+i*W2),
r_z*r_w = 2*Z3/(C-W3).                         (INV)
```

The three invariants in `(INV)` determine the pair `(r_z,r_w)` up to the simultaneous residual deck action

```text
(r_z,r_w) -> (-r_z,-r_w).
```

Thus they determine the exact point of `(R x R)/(G/H)_diag` lying above a box node without assigning a residual sheet to a normalization branch.

## 2. Exact `000707` support in the retained 48-node ordering

Decoding the retained mask in the exact 48-node ordering gives

```text
Sigma = {P0,P1,P2,P3,P8,P9,P10,P11,P24,P25,P26,P32,P33,P34}.
```

The two supported zero-quartic/node types are

```text
Q0 / b1=0 : P0,P1,P2,P3,P24,P25,P26,   omitted P27,
Q1 / b2=0 : P8,P9,P10,P11,P32,P33,P34, omitted P35.
```

Substitution of the exact node coordinates into `(INV)` gives:

| nodes | `r_z^2` | `r_w^2` | `r_z*r_w` |
|---|---:|---:|---:|
| `P0,P2` | `2` | `2` | `2` |
| `P1,P3` | `2` | `2` | `-2` |
| `P24,P26` | `-2` | `2` | `-2i` |
| `P25` | `-2` | `2` | `2i` |
| `P8,P10` | `2i` | `-2i` | `2` |
| `P9,P11` | `2i` | `-2i` | `-2` |
| `P32,P34` | `2i` | `2i` | `-2i` |
| `P33` | `2i` | `2i` | `2i` |

The omitted nodes satisfy

```text
P27 : (-2, 2,  2i),   the same residual orbit as P25,
P35 : (2i,2i, 2i),    the same residual orbit as P33.
```

These coincidences are orbit coincidences only; they do not identify box nodes or conductor branches.

## 3. Representative form and the two exact saturation equations

Choose square roots

```text
a^2=2,
b=i*a,
u^2=2i,
v=2/u  (so v^2=-2i and u*v=2).
```

Choose one representative in each simultaneous-sign orbit:

```text
P0,P2   -> (a,a)
P1,P3   -> (a,-a)
P24,P26 -> (b,-a)
P25     -> (b,a)

P8,P10  -> (u,v)
P9,P11  -> (u,-v)
P32,P34 -> (u,-u)
P33     -> (u,u).
```

For a supported node `Pj`, let `x_j` be the number of its `8*l` normalization branches whose residual lift uses the displayed representative; the remaining `8*l-x_j` use its simultaneous negative.

The retained boundary-fiber saturation says that the two fixed-factor fibres on each zero quartic contain exactly `28*l` branches each in the `e=2` case.

For `Q0`, the exact orbit table shows that the fixed factor is `r_w` with values `+a,-a`. Hence

```text
x0-x1+x2-x3-x24+x25-x26 = -4*l.              (Q0)
```

For `Q1`, the fixed factor is `r_z` with values `+u,-u`. Hence

```text
x8+x9+x10+x11+x32+x33+x34 = 28*l.            (Q1)
```

Equivalently, with centered variables

```text
d_j=2*x_j-8*l,
```

the equations are

```text
d0-d1+d2-d3-d24+d25-d26 = 0,
d8+d9+d10+d11+d32+d33+d34 = 0.                (CENTERED)
```

## 4. What the exact table does and does not determine

The equations `(Q0)` and `(Q1)` do not determine the branchwise binary lift allocation.

For example, as formal integer allocations in units of `l`, both

```text
x_j=4*l for every supported j
```

and

```text
x0=5*l, x2=3*l,
x8=5*l, x9=3*l,
x_j=4*l for every other supported j
```

satisfy the exact saturation equations and the bounds `0<=x_j<=8*l`.

These are **formal allocation witnesses only**. They are not asserted to come from actual curves. Their role is to prove that the currently retained node-orbit and two-fibre saturation data alone cannot recover the branchwise residual sheet label.

Therefore the active missing datum is narrower than before:

```text
exact node -> residual simultaneous-sign orbit     MATERIALIZED,
per-normalization-branch choice inside that orbit  MISSING,
conductor pairing / transition M_(u,v)              MISSING,
chi_res(M_(u,v)) and weighted opposite-sheet cut    MISSING.
```

A successful continuation must impose a global relation on these branch allocations or directly construct the conductor descent/transition map. Only then may `chi_res` be evaluated and compared with the retained `84*l^2` threshold.

## Firewalls

- No conductor sign is assigned.
- No branch allocation is claimed geometrically realizable.
- No weighted-cut upper bound is proved.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- No finite degree window is released.
- MB104/span5/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
