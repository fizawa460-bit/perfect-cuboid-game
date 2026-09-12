# Stage32 MB104 — `000707000f0f` one-factor absent half-branch class

Status: **RETAINED ONE-FACTOR CHARACTER REDUCTION / NUMERICAL-PICARD WALL / e=2,e=4 OPEN / NO CREDIT**

## Scope

Continue only the dangerous MB104 equality packet on

```text
Sigma=000707000f0f,
node-type counts=(7,7,0),
D_l=7lH-4l sum_(p in Sigma)E_p,
l>=1.
```

The retained residual-character leaf associates to the absent stabilizer type a class

```text
eta in Pic^0(E)[2]
```

on the normalization `E` of a hypothetical carrier and proves

```text
e=2 <=> eta=0,
e=4 <=> eta!=0.
```

The retained half-fiber adapter identifies `eta` as the restriction of the difference of the two absent-type `G2` half-fibers in one product-induced genus-five fibration.

## 1. Canonical half-branch class on the surface

Fix one factor fibration and let

```text
Q_a,Q_b
```

be its two reduced bad `G2` components of the absent node type.  Let `T_a,T_b` be their eight-node sets.

Distinct fibers on the minimal resolution are disjoint.  Since every absent-type node lies on exactly two of the four `G2` curves in the hyperplane `b3=0`, the two components belonging to one fibration have disjoint eight-node sets.  Hence

```text
T_a disjoint T_b,
|T_a|=|T_b|=8,
T_a union T_b = all 16 box nodes of the absent type.
```

The retained A1 fiber relation is

```text
2(Q_a-Q_b)
  ~ sum_(p in T_b) E_p - sum_(p in T_a) E_p.
```

Define

```text
Delta := Q_a-Q_b,
L_abs := Delta + sum_(p in T_a) E_p.
```

Then exactly in `Pic(S)`

```text
2 L_abs
  ~ sum_(p in T_a union T_b) E_p
  =: B_abs.                                      (HB)
```

Thus `L_abs` is the integral half-class of the complete 16-exceptional divisor of the absent node type.

## 2. Restriction to a dangerous-packet carrier

The class `D_l` has coefficient zero at every absent-type exceptional curve.  For an integral effective carrier `C_l in |D_l|`,

```text
D_l.E_p=0
```

at such a curve.  Since `C_l` is distinct from `E_p`, nonnegative local intersection gives

```text
C_l cap E_p = emptyset
```

for all `p in T_a union T_b`.

Therefore every absent exceptional divisor restricts trivially to the normalization `E`, and

```text
L_abs|_E = Delta|_E.
```

Consequently the residual character is exactly

```text
eta = O_E(L_abs|_E).
```

The two component-degree cases are therefore

```text
e=2 <=> O_E(L_abs|_E) is trivial,
e=4 <=> O_E(L_abs|_E) is the nonzero two-torsion class.
```

This is the one-factor problem; no comparison between the two product factors is needed.

## 3. Exact numerical data

The sixteen curves in `B_abs` are pairwise disjoint exceptional `(-2)`-curves.  From `(HB)`,

```text
B_abs^2 = 16*(-2) = -32,
L_abs^2 = -8.
```

The exceptional curves are orthogonal to the hyperplane/canonical class, so

```text
H.L_abs = K_S.L_abs = 0.
```

The dangerous ray has zero coefficient at all absent exceptionals; hence

```text
D_l.L_abs = (1/2) D_l.B_abs = 0.
```

For an absent exceptional curve `E_p`,

```text
2 L_abs.E_p = B_abs.E_p = -2,
L_abs.E_p = -1.
```

Thus the numerical package is

```text
L_abs^2=-8,
K.L_abs=0,
H.L_abs=0,
D_l.L_abs=0,
L_abs.E_p=-1  (p absent type).
```

## 4. Numerical Picard pairings alone cannot decide the case

After restriction to the normalization, both the trivial class and every nonzero element of

```text
Pic^0(E)[2]
```

have degree zero and first Chern class zero.  Therefore intersection numbers in `NS(S)` / the rank-64 Picard lattice can establish the half-branch relation and degree-zero property, but **numerical pairings alone do not distinguish**

```text
eta=0
```

from

```text
eta!=0.
```

A successful continuation must compute the actual restriction class, equivalently one of:

- the Abel--Jacobi class of the two half-fiber intersection divisors;
- the square/non-square class of the residual double-cover function in `k(E)^*/k(E)^{*2}`;
- the connected/split status of the induced intermediate double cover of the normalization;
- an equivalent monodromy/commensurator invariant.

This is a wall only for **purely numerical Picard-pairing** attacks.  It does not say that the explicit Picard64 geometry plus additional restriction data is useless.

## 5. Cohomology caveat

One might try to decide `eta` from the restriction of `O_S(L_abs)` to the singular carrier by a surface exact sequence.  That is not sufficient by itself: the Stage32 carrier has normalization genus one but very large arithmetic genus, so a line bundle may become trivial on the normalization while retaining nontrivial conductor/gluing data on the singular curve.

Therefore a vanishing statement for `H^0(C_l,O_{C_l}(L_abs))` does not, without an explicit normalization/conductor adapter, prove `eta!=0`.

This prevents an unsupported shortcut from a surface-cohomology calculation to the required normalization square class.

## Next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-HALF-BRANCH-ABEL-JACOBI-OR-MONODROMY
```

Target: compute the actual class `L_abs|_E in Pic^0(E)[2]`, not merely its numerical degree.

## Firewalls

- `eta` is not evaluated in this leaf.
- `e=2` and `e=4` both remain open.
- `000707000f0f` remains in the dangerous equality-packet frontier.
- The geometric arbitrary-branch support core remains `864`; the dangerous equality-packet core remains `768`.
- No arbitrary-branch closure, MB104 completion, receiver, theorem, endpoint, or Perfect-Cuboid credit.
- No merge authorization.
