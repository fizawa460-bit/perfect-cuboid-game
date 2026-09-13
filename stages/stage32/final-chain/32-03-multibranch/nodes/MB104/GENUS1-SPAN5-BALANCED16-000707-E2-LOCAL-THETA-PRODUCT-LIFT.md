# Stage32 MB104 — `000707000f0f` e=2 local theta/product lift

Status: **RETAINED AMBIENT LOCAL-LIFT MATERIALIZATION / CARRIER JET STILL MISSING / NO CONDUCTOR SIGN / NO CREDIT**

## 1. Local ambient model is now explicit

Freitag--Salvati Manni give the product modular parametrization of the box surface and, at the typical singular cusp `(infinity,infinity)`, the level-eight uniformizers

```text
p=exp(2*pi*i*z/8),
q=exp(2*pi*i*w/8).
```

The node stabilizer acts by

```text
(p,q) -> (-p,-q).
```

Therefore the completed local box germ is

```text
Spec C[[p,q]] / {+-1},
```

while the corresponding Beauville/local double-cover germ is the smooth product germ

```text
Spec C[[p,q]] -> Spec C[[p,q]]/{+-1}.          (LOCAL)
```

Thus the two local lifts of a generic downstairs point are represented by

```text
(p,q) and (-p,-q).                             (SHEET)
```

This is the first explicit local product-lift map retained on the MB104 route.

Source lock: `FREITAG-SALVATI-MANNI-LOCAL-NODE-THETA-SOURCE-NOTE.md`.

## 2. What a carrier branch would require

A normalization branch through the node must lift locally to a parametrized germ

```text
p=p(s),
q=q(s).
```

Its downstairs image forgets the simultaneous sign. Two normalization branches over the same singular carrier point are same-sheet/opposite-sheet only after one knows whether their lifted germs are related by the identity or by

```text
(p,q) -> (-p,-q)
```

at the relevant conductor identification.

Hence the residual-sheet problem has been reduced from an unspecified theta map to a concrete local involution test.

## 3. Minimal contact does not determine the involution test

The dangerous equality packet has FSM-minimal branch data `(1,1)`. This fixes contact/multiplicity information, but it does not determine the leading tangent ratio

```text
lambda = lim_(s->0) q(s)/p(s)
```

or any equivalent first nonzero pair of coefficients.

Distinct lifted germs can have the same multiplicity/contact pair and different tangent directions. The simultaneous-sign quotient also identifies `lambda` with itself, so the tangent ratio alone does not label the Beauville sheet unless a lift/orientation datum is supplied.

Therefore the retained `(1,1)` branch type plus node label still cannot assign a conductor sign.

## 4. Exact remaining datum

For one supported node, it is sufficient to materialize the leading lifted branch coefficients

```text
p(s)=a*s+O(s^2),
q(s)=b*s+O(s^2),
(a,b)!=(0,0),
```

together with the identification of the normalization parameter at the other conductor preimage.

The sheet test is then whether the two lifted coefficient pairs agree under the identity or simultaneous negation, after the allowed local reparametrization has been fixed by the normalization/conductor map.

Equivalently, an actual local carrier equation in the invariant coordinates

```text
x=p^2, y=pq, z=q^2,  xz=y^2
```

plus its normalized branches would permit this lift to be computed directly.

## 5. Next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-INVARIANT-NODE-BRANCH-NORMALIZATION
```

Target: derive or source-lock the local carrier branch in the A1 node coordinates `x=p^2,y=pq,z=q^2`, normalize it, and recover the two product lifts. First test one of the two supported node types; only after a verified group-action transport may the result be propagated to the other thirteen supported nodes.

## Firewalls

- The ambient local quotient is explicit; the hypothetical carrier germ is not.
- `(1,1)` contact does not determine a tangent or sheet.
- No conductor sign or weighted cut is computed.
- `e=2` and `e=4` remain open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
