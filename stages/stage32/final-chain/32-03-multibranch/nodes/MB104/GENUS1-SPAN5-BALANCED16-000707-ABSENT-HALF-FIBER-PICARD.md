# Stage32 MB104 — `000707000f0f` absent half-fiber Picard adapter

Status: **RETAINED EXACT SURFACE-PICARD ADAPTER FOR THE RESIDUAL CHARACTER / NO CLOSURE / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue the hostile-audited dangerous equality packet on

```text
Sigma=000707000f0f,
node-type counts=(7,7,0),
D_l=7lH-4l sum_(p in Sigma)E_p,
l>=1.
```

The residual-sheet leaf gives, for each product factor, a degree-`56l` map

```text
phi:E->P1
```

from the normalization `E` of a hypothetical carrier and a two-torsion class

```text
eta=O_E(A-B) in Pic^0(E)[2],
```

where `2A` and `2B` are the two completely ramified fibers belonging to the singular stabilizer type absent from `Sigma`.

This leaf identifies `A-B` as the restriction of an explicit difference of known `G2` elliptic quartics on the cuboid resolution.

## 1. The absent branch values are doubled `G2` bad fibers

The two factor maps arise from the two complementary product-induced isotrivial genus-five fibrations of the cuboid surface.

For either fibration, the Stoll--Testa source adapter gives six bad fibers.  Each bad fiber has on the canonical model one known `G2` elliptic curve with multiplicity two.  The `G2` curves are precisely the twelve genus-one quartics contained in

```text
b1=0, b2=0, b3=0.
```

Fix one factor fibration.  Let

```text
Q_a,Q_b
```

be the two reduced `G2` components corresponding to the two residual branch values of the third/absent stabilizer type.

Each `Q_x` contains exactly eight box nodes, all of that absent type.  Because the current support has type counts `(7,7,0)`, none of these sixteen exceptional curves belongs to the support of `D_l`.

## 2. Full fiber classes on the minimal resolution

Let `T_x` be the eight-node set of `Q_x`.  Pulling the doubled bad fiber through the A1 resolution gives

```text
F_x = 2 Q_x + sum_(p in T_x) E_p.
```

The two divisors `F_a,F_b` are fibers of the same morphism, hence

```text
F_a ~ F_b.
```

Therefore in `Pic(S)`

```text
2(Q_a-Q_b)
  ~ sum_(p in T_b)E_p - sum_(p in T_a)E_p.       (HF)
```

The exceptional correction is essential.  In particular `(HF)` does not make `Q_a-Q_b` a two-torsion class of `Pic(S)`.

## 3. The hypothetical carrier misses all absent-type exceptional curves

For any absent-type node `p`, the class `D_l` has coefficient zero at `E_p`, so

```text
D_l.E_p=0.
```

If an integral carrier `C_l in |D_l|` exists, it is distinct from `E_p`; effectivity and nonnegative local intersection then imply

```text
C_l cap E_p = emptyset
```

for every absent-type exceptional curve.

Restricting `(HF)` to the normalization `E` of `C_l` therefore gives

```text
2 (Q_a-Q_b)|_E ~ 0.
```

Moreover

```text
D_l.Q_a=D_l.Q_b=7l*(H.Q_x)=28l,
```

because `H.Q_x=4` and no supported exceptional point lies on either absent half-fiber.

Thus the intersection divisors

```text
A = Q_a|_E,
B = Q_b|_E
```

have degree `28l`, and the residual character of the previous leaf is exactly

```text
eta = O_E((Q_a-Q_b)|_E).
```

## 4. Two factors give two explicit Picard64 differences

Apply the construction to the two complementary product fibrations.  This gives two surface divisor classes

```text
Delta_1 = Q_(1,a)-Q_(1,b),
Delta_2 = Q_(2,a)-Q_(2,b)
```

built entirely from the known `G2` library, with

```text
eta_j = O_E(Delta_j|_E).
```

The residual-sheet leaf requires

```text
eta_1=eta_2.
```

Hence every remaining dangerous-packet realization must satisfy the concrete restriction condition

```text
O_E((Delta_1-Delta_2)|_E) ~= O_E.
```

The `e` cases are distinguished by the common value:

```text
e=2  => eta_1=eta_2=0,
e=4  => eta_1=eta_2 is one common nonzero element of Pic^0(E)[2].
```

This replaces the previous abstract sheet/character problem by a restriction problem for two explicit classes in the known rank-64 Picard lattice.

## 5. Why Picard torsion-freeness does not close `e=4`

Stoll--Testa prove `Pic(S)` is torsion-free.  That fact alone does not force `eta=0`.

Indeed `(HF)` says

```text
2 Delta_j = exceptional difference,
```

not `2 Delta_j=0` in `Pic(S)`.  The right-hand side vanishes only after restriction to a carrier that avoids the absent exceptional curves.  A non-torsion surface line bundle may restrict to a nontrivial two-torsion line bundle on a genus-one curve.

Therefore the correct next problem is not surface torsion.  It is the exact restriction of

```text
Delta_1, Delta_2, Delta_1-Delta_2
```

to a hypothetical carrier in `|D_l|`.

## Next lever

Use the explicit `G2` equations / Picard64 coordinates to determine whether

```text
(Delta_1-Delta_2)|_E = 0
```

is compatible with the birational joint factor map and the saturated boundary fibers.  An exact result should either

- force the common character `eta` to be zero, excluding `e=4`;
- force it nonzero, excluding `e=2`; or
- show `eta_1!=eta_2`, excluding both cases.

Absent such a calculation, both cases remain open.

## Firewalls

- No `e=2` or `e=4` closure is claimed.
- No claim that `Delta_j` is torsion in `Pic(S)`.
- No claim that torsion-freeness of `Pic(S)` implies trivial restriction.
- No arbitrary-branch closure for the Picard class.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104, span5, receiver, theorem, endpoint, and Perfect-Cuboid credit remain zero.
- No merge authorization.
