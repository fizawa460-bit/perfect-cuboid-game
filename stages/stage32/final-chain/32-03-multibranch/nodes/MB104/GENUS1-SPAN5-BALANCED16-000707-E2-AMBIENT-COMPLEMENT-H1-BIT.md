# Stage32 MB104 — `000707000f0f` e=2 ambient-complement H1 bit

Status: **RETAINED EXACT TOPOLOGICAL REDUCTION / `H_1(U,Z)=Z/2` / CONDUCTOR LOOP CLASS STILL OPEN / NO CREDIT**

## Scope

Continue only the active leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP.
```

Let `S` be the smooth cuboid resolution,

```text
B_abs = E_16+...+E_23+E_40+...+E_47,
U = S \ B_abs,
```

and let `alpha_abs` be the ambient Kummer character of the absent half-branch double cover over `U`.

## 1. Exact complement homology

The retained one-factor half-branch adapter gives `2L_abs~B_abs`; the retained Picard64 certificate computes the span of the sixteen absent exceptional classes modulo two to have rank exactly `15`. The source-locked cuboid Picard input gives `H_1(S,Z)=0` and torsion-free `Pic(S)`.

For `(S,U)`, integral excision and Thom give

```text
H_2(S,U;Z) ~= Z^16.
```

The intersection map has full rational rank because the sixteen exceptional classes have intersection matrix `-2I_16`. Each `E_p` maps to `-2e_p`, so its cokernel is finite of exponent at most two. Modulo two the intersection-map image has rank `15`, hence the cokernel has exactly one `F_2` dimension. Therefore

```text
H_1(U,Z) ~= Z/2,
H_1(U,F_2) ~= F_2.
```

All sixteen absent meridians represent the unique nonzero class.

## 2. The ambient character is the unique nonzero bit

The half-branch cover has local monodromy `1` around every deleted absent exceptional component. Hence

```text
alpha_abs : H_1(U,Z) -> F_2
```

is the unique nonzero character and an isomorphism after identifying `Z/2` with `F_2`.

Since `H_1(S,Z)=0`, any loop `lambda` in `U` bounds an integral singular 2-chain `Gamma` in `S`. The parity

```text
Gamma . B_abs mod 2
```

is independent of `Gamma`, because changing `Gamma` by a closed 2-cycle changes the intersection by an even number (`B_abs~2L_abs`). Therefore

```text
alpha_abs(lambda) = Gamma.B_abs mod 2.          (LINK)
```

For a conductor-identification loop this gives

```text
epsilon_(p,i)+epsilon_(p,j)
 = alpha_abs(lambda_(p;i,j))
 = Gamma_(p;i,j).B_abs mod 2.                   (COND)
```

Thus the residual sheet problem is exactly one integral meridian/linking bit; no larger ambient character space remains.

## 3. Extra consequence in the active e=2 leaf

The `e=2` assumption says the pulled-back absent Kummer character is trivial on the normalization `E`. Since `alpha_abs` is injective,

```text
nu_* : H_1(E,F_2) -> H_1(U,F_2)
is the zero map.
```

Changing the normalization path used to form a conductor loop therefore cannot change `(COND)`. The surviving bit belongs to the conductor/dual-graph gluing cycle, not to an ordinary genus-one cycle of `E`.

## 4. What remains

For each supported conductor pair, it now suffices to construct one ambient bounding 2-chain `Gamma_(p;i,j)` and compute

```text
Gamma_(p;i,j).B_abs mod 2.
```

Equivalent inputs are the class `[lambda_(p;i,j)]` in `H_1(U,Z)=Z/2`, its absent-divisor linking parity, or a source-locked `sqrt(h o phi)` branch-identification sign. Once these bits are known, the retained weighted local intersection table determines the same/opposite-sheet cut.

## Firewalls

- No conductor loop class is assigned here.
- No same/opposite residual sheet is assigned to any node.
- No weighted-cut upper bound is claimed.
- `e=2`, `e=4`, and `000707000f0f` remain open.
- MB104/span5/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy compute is armed.
- No merge or rebase authorization.
