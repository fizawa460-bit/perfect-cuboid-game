# Stage32 MB104 — `000707000f0f` e=2 invariant A1-node branch normalization

Status: **RETAINED LOCAL ALGEBRA REDUCTION / SHEET LABEL IS NOT IN THE DOWNSTAIRS BRANCH GERM / DESCENT-GLUING DATUM IS ESSENTIAL / NO CREDIT**

## Scope

Work in the source-locked local product model

```text
A = C[[p,q]],
sigma(p,q)=(-p,-q),
B=A^{<sigma>} = C[[x,y,z]]/(xz-y^2),
x=p^2, y=pq, z=q^2.
```

A dangerous carrier branch through the box node is a reduced one-dimensional germ in `Spec B`. Its normalization is a formal disc `Spec C[[s]]`.

## 1. Generic minimal branch normalization

For an FSM-minimal branch with nonzero first lifted coefficients, an upstairs lift has

```text
p=a*s+O(s^2),
q=b*s+O(s^2),
(a,b)!=(0,0).
```

The induced invariant branch has

```text
x=a^2*s^2+O(s^3),
y=ab*s^2+O(s^3),
z=b^2*s^2+O(s^3).
```

The second product lift is obtained by the deck involution

```text
(p,q) -> (-p,-q).
```

At the level of the normalization parameter this has the same leading effect as

```text
s -> -s
```

on the linear terms.

Thus one downstairs invariant branch germ naturally has two local product lifts differing by simultaneous sign.

## 2. The invariant branch cannot choose between the two lifts

All functions in the invariant local ring `B` are unchanged by `sigma`. Therefore the complete downstairs branch equation, even if known exactly in `x,y,z`, determines the unordered pair of lifts but cannot canonically label one as the residual `+` sheet and the other as the residual `-` sheet.

Equivalently, replacing a lifted parametrization

```text
(p(s),q(s))
```

by

```text
(-p(s),-q(s))
```

does not change the induced map to `Spec B`.

This is not merely a lack of tangent data. It is the local manifestation of the global `mu_2` descent ambiguity.

## 3. Consequence for conductor pairs

Suppose two normalization points `x_i,x_j` are identified by the singular carrier conductor. Their downstairs invariant germs can be fully known while the gluing of their two-element lift fibres still has two possibilities:

```text
identity gluing,
deck-twisted gluing.
```

These are exactly the same-sheet and opposite-sheet alternatives measured by the retained conductor character `kappa` / ambient Kummer character.

Therefore:

```text
local invariant carrier equation alone
  does not determine
conductor residual-sheet sign.                 (BOUNDARY)
```

A local equation plus normalization is useful for identifying branches and intersection multiplicities, but a sign decision additionally requires the descent/gluing map between their lifted fibres.

## 4. Refined missing datum

The previous target asked for the local carrier equation and normalization. The local algebra above shows that this is necessary but not sufficient for the actual e=2 cut.

The load-bearing datum must include one of:

- an explicit lift of the singular carrier map to the residual double cover;
- a conductor gluing isomorphism between the two `mu_2` fibres;
- an equivariant product-cover construction of the carrier that fixes the deck action at the conductor;
- a global rational square root together with its limiting trivializations at both conductor preimages.

In the retained e=2 language, if `g^2=f_t|_E`, one must compare the two fibre trivializations induced by `g` under the conductor identification. The invariant A1 branch alone cannot supply that comparison.

## 5. Next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-CONDUCTOR-DESCENT-GLUING-MAP
```

Target: construct the actual descent isomorphism on the two-element residual-cover fibres at conductor pairs, preferably from the global product/modular quotient square. If unavailable, source-lock a theorem or explicit carrier construction that determines this gluing. Do not continue searching for a sheet label in invariant tangent data alone.

## Firewalls

- No claim that every minimal branch has both `a,b` nonzero; the displayed expansion is the generic local form used to expose the deck ambiguity.
- No conductor sign is assigned.
- No local equation is promoted to a global carrier.
- `e=2` and `e=4` remain open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
