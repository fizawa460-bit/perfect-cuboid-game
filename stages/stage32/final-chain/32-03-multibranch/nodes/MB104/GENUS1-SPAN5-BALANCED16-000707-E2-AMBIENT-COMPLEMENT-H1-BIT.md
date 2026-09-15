# Stage32 MB104 — `000707000f0f` e=2 ambient-complement H1 bit

Status: **RETAINED EXACT TOPOLOGICAL REDUCTION / `H_1(U,F_2)=F_2` / CONDUCTOR LOOP CLASS STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Let `S` be the smooth cuboid resolution, let

```text
B_abs = E_16+...+E_23+E_40+...+E_47,
U = S \ B_abs,
```

and let `alpha_abs` be the ambient Kummer character of the absent half-branch double cover over `U`.

## 1. Exact complement homology

The retained one-factor half-branch adapter gives

```text
2 L_abs ~ B_abs,
```

so the sixteen absent exceptional classes satisfy the all-ones relation modulo two. The retained Picard64 certificate computes their span in `Pic(S)/2Pic(S)` to have rank exactly `15`.

The source-locked cuboid Picard input says `Pic(S)` is torsion-free. Kummer over `C`, finite-coefficient comparison, excision, Thom, Poincare duality, and the long exact sequence for `(S,U)` then give

```text
H_1(S,F_2)=0,
H_2(S,U;F_2) ~= F_2^16,
rank(H_2(S,F_2) -> H_2(S,U;F_2)) = 15,
H_1(U,F_2) ~= F_2.
```

The intersection-map image is the even-weight hyperplane

```text
{(z_1,...,z_16) in F_2^16 : sum z_i = 0},
```

because the all-ones relation annihilates the image and both spaces have dimension `15`. Hence every absent meridian maps to the same nonzero generator of `H_1(U,F_2)`.

## 2. The ambient character is the unique nonzero bit

The half-branch cover has local monodromy `1` around each deleted absent exceptional component. Therefore

```text
alpha_abs : H_1(U,F_2) -> F_2
```

is nonzero. Since the source is one-dimensional,

```text
alpha_abs is an isomorphism.
```

Thus for every conductor-identification loop `lambda_(p;i,j)`,

```text
alpha_abs(lambda_(p;i,j)) = 0
  <=> [lambda_(p;i,j)] = 0 in H_1(U,F_2),

alpha_abs(lambda_(p;i,j)) = 1
  <=> [lambda_(p;i,j)] is the unique nonzero class.
```

The retained conductor formula therefore becomes

```text
epsilon_(p,i) + epsilon_(p,j)
  = [lambda_(p;i,j)] in H_1(U,F_2) ~= F_2.
```

So the same/opposite residual-sheet question is exactly a mod-two null-homology test in the fixed complement `U`; there is no larger ambient character space left to classify.

## 3. Extra consequence in the active e=2 leaf

The active `e=2` assumption says the pulled-back absent Kummer character is trivial on the normalization `E`:

```text
alpha_abs o nu_* = 0 on H_1(E,F_2).
```

Because `alpha_abs` is injective, this strengthens to

```text
nu_* : H_1(E,F_2) -> H_1(U,F_2)
is the zero map.
```

Hence changing the normalization path used to form a conductor loop changes it by a class whose image in `H_1(U,F_2)` is zero. The remaining sheet bit is carried only by the conductor/dual-graph gluing cycle, not by ordinary genus-one cycles on `E`.

This is a genuine reduction of the missing datum, but it still does not evaluate an individual conductor edge.

## 4. What remains

For each supported conductor pair, compute one of the equivalent exact data:

- `[lambda_(p;i,j)]` in the one-dimensional group `H_1(U,F_2)`;
- its mod-two linking parity with the absent divisor `B_abs`;
- an explicit two-chain in `S` bounding `lambda_(p;i,j)` together with its intersection parity with `B_abs`;
- the equivalent source-locked `sqrt(h o phi)` branch-identification sign.

Once this bit is known, the retained weighted local intersection table immediately determines the same/opposite-sheet cut.

## Firewalls

- No conductor loop class is assigned here.
- No same/opposite residual sheet is assigned to any node.
- No weighted-cut upper bound is claimed.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
