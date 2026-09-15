# Stage32 MB104 — `000707000f0f` e=2 anti-invariant class decomposition

Status: **RETAINED EXACT NUMERICAL ANTI-INVARIANT REDUCTION / ALL UNKNOWN NUMERICAL ENERGY LIVES ON THE FOURTEEN SPLIT A1 EXCEPTIONALS / e=2 STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Assume conditionally that the retained dangerous packet is realized in the `e=2` case. Use the retained smooth residual double cover

```text
pi:Y->S
```

from the absent half-branch class, and write

```text
pi^*C=C_1+C_2
```

for the two deck-exchanged irreducible components. At each of the fourteen supported box nodes keep the retained branch allocation

```text
x_j + (8l-x_j)=8l,
d_j=2x_j-8l.
```

This leaf determines the **numerical anti-invariant divisor class** `C_1-C_2`. It does not determine an individual conductor transition.

## 1. Split exceptional curves over the supported A1 nodes

The branch divisor of `pi` consists only of the sixteen exceptional curves of the absent node type. Every supported node is of one of the other two types, so `pi` is etale over its exceptional curve

```text
E_j ~= P1.
```

A connected nontrivial etale double cover of `P1` does not exist. Hence

```text
pi^{-1}(E_j)=E_j^+ disjoint_union E_j^-
```

with the deck involution exchanging the two components. Since `pi` is etale there,

```text
(E_j^+)^2=(E_j^-)^2=-2,
E_j^+.E_j^-=0.
```

Define the anti-invariant exceptional difference

```text
F_j=E_j^+-E_j^-.
```

Then

```text
F_j^2=-4,
F_i.F_j=0  (i!=j).
```

Choose the `+` labeling so that the displayed representative in the retained residual-node orbit table is the `E_j^+` residual lift.

## 2. The centered branch allocation is an intersection coordinate

For the first component `C_1`, the displayed residual representative occurs `x_j` times and the simultaneous-negative representative occurs `8l-x_j` times. The deck translate `C_2` reverses the two counts. Therefore

```text
C_1.E_j^+ = x_j,
C_1.E_j^- = 8l-x_j,
C_2.E_j^+ = 8l-x_j,
C_2.E_j^- = x_j.
```

Put

```text
v=C_1-C_2.
```

Then exactly

```text
v.E_j^+ = d_j,
v.E_j^- = -d_j,
v.F_j = 2d_j.                                  (PAIRING)
```

Thus the fourteen centered allocation variables are not merely combinatorial counts: they are the intersection coordinates of the anti-invariant divisor class `v` against the fourteen orthogonal roots `F_j`.

## 3. The lift-energy identity computes the complete norm

The retained split-Hodge identities give

```text
(C_1-C_2)^2=2C^2-4(C_1.C_2).
```

The retained A1 lift-energy identity gives

```text
C^2=336l^2,
C_1.C_2=168l^2+(1/4)sum_j d_j^2.
```

Hence

```text
v^2 = - sum_j d_j^2.                           (NORM)
```

On the other hand, the orthogonal projection of `v` to the span of the `F_j` is

```text
v_exc = - sum_j (d_j/2) F_j,
```

because `F_j^2=-4` and `(PAIRING)` gives `v.F_j=2d_j`. Since every `d_j` is even, the displayed coefficients are integral.

Its square is

```text
v_exc^2 = - sum_j d_j^2.
```

Therefore the exceptional projection already accounts for the **entire** square of `v`.

## 4. No hidden anti-invariant numerical component

Set

```text
w = v-v_exc
  = v + sum_j (d_j/2)F_j.
```

By construction

```text
w.F_j=0
```

for all fourteen supported nodes, and from `(NORM)`

```text
w^2=0.
```

Both `v` and every `F_j` are anti-invariant under the deck involution. Hence `w` is anti-invariant. For any ample divisor `A` on `S`, the pullback `pi^*A` is invariant, so

```text
w.pi^*A=0.
```

The Hodge index theorem makes the intersection form negative definite on the numerical orthogonal complement of an ample class. Since `w^2=0`, it follows that

```text
w == 0 numerically.
```

Consequently the exact numerical class identity is

```text
C_1-C_2 == - sum_(j in Sigma) (d_j/2)(E_j^+-E_j^-).   (ANTI-NS)
```

Here `==` means numerical equivalence on `Y`.

## 5. Consequence for the active route

There is no additional unknown **numerical** anti-invariant direction left after the fourteen branch allocations are specified. For every anti-invariant divisor class `G` on `Y`, numerical intersection with the component difference is forced by

```text
(C_1-C_2).G
 = - sum_j (d_j/2) (E_j^+-E_j^-).G.            (TEST)
```

Thus a future numerical obstruction must come from one of the following:

1. an additional geometric anti-invariant test class whose intersections with the split exceptionals are source-locked and whose left side is independently known;
2. an integral/divisibility constraint stronger than numerical equivalence;
3. torsion/linear-equivalence information for the numerically trivial remainder;
4. the actual conductor transition / residual `G/H` sheet map.

The two retained zero-quartic saturation equations are compatible with `(ANTI-NS)` and with the balanced vector `d_j=0`; this leaf does not exclude `e=2`.

## Cusp-width re-entry check

The previously rejected compact-etale cusp-width route required

```text
f1^{-1}(Cusps)=f2^{-1}(Cusps).
```

The later boundary saturation controls the two zero-pairing boundary components, but the other Satake boundary components have positive `D_l` intersection and are not removed by that argument. Therefore the missing common-puncture equality is still not proved here, and the rejected cusp-width route remains non-consumable.

## Firewalls

- Numerical equivalence `(ANTI-NS)` is not promoted to linear equivalence.
- No torsion statement for `Pic(Y)` is asserted.
- No individual conductor pair receives a residual sign.
- No new upper bound on the weighted cut is claimed.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge authorization.
