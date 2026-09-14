# Stage32 MB104 — `000707000f0f` e=2 supported inertia versus residual sheet

Status: **RETAINED SEMANTIC CORRECTION / SUPPORTED A1 INVOLUTION DIES IN THE `H` QUOTIENT / RESIDUAL SHEET REQUIRES `G/H` DATA / NO CREDIT**

## Scope

Work only with the retained dangerous equality packet

```text
Sigma = 000707000f0f,
node-type counts = (7,7,0),
e in {2,4}.
```

Let the two occurring singular stabilizer involutions be `s1,s2` and set

```text
H=<s1,s2> ~= (Z/2)^2,
G ~= (Z/2)^3,
R=C8/H,
S=C8/G,
q:R -> S.
```

The third singular stabilizer `s3` is absent from the support and satisfies `s3 notin H`. The residual deck group is

```text
G/H ~= Z/2,
```

with nontrivial class represented by `s3 H`.

Source locks: `BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md`, `GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER.md`.

## 1. The local A1 involution at a supported node belongs to `H`

At a supported box node of type `s_j`, with `j in {1,2}`, the retained theta/product local model has a smooth product germ with node stabilizer

```text
s_j:(p,q) -> (-p,-q),
```

and downstairs invariant A1 germ

```text
C[[p,q]]^{<s_j>} = C[[x,y,z]]/(xz-y^2),
x=p^2,
y=pq,
z=q^2.
```

The two local product lifts of one invariant branch therefore differ by the supported-node involution `s_j`.

But by definition

```text
s_j in H.
```

Hence the two points have the same `H`-orbit:

```text
[r]_H = [s_j r]_H in R=C8/H.
```

So the supported-node simultaneous-sign involution is already killed before the residual quotient `q:R->S` is formed.

## 2. The supported-node sign is not the residual `G/H` sheet variable

The two residual sheets of `q` differ by the nontrivial class in `G/H`, represented by `s3 H`, not by either `s1` or `s2`.

Therefore the binary test

```text
identity versus (p,q)->(-p,-q)
```

at a supported A1 node does **not** exchange the two residual `q`-sheets. It only changes a representative inside one `H`-orbit.

This sharpens the earlier local-normalization boundary. Even if an exact invariant carrier equation, normalization parameter, tangent, and all local jets were known, deciding which of the two supported-node product lifts is used would still not evaluate the residual conductor character.

Source locks: `GENUS1-SPAN5-BALANCED16-000707-E2-LOCAL-THETA-PRODUCT-LIFT.md`, `GENUS1-SPAN5-BALANCED16-000707-E2-INVARIANT-NODE-BRANCH-NORMALIZATION.md`.

## 3. What remains genuinely load-bearing

The `e=2` conductor sign is the descent sign of the residual cover

```text
q:R=C8/H -> S=C8/G.
```

Thus the required datum at a normalization preimage is not a representative in the local product doublet modulo `s_j`. It is its actual `H`-orbit point in `R`, or any equivalent coordinate/trivialization that detects the nontrivial `G/H` action.

A sufficient next asset is one of:

- an explicit branch-preimage map into `R=C8/H` together with the `s3 H` action;
- theta/modular coordinates whose quotient by `H` is explicit and whose residual involution is source-locked;
- an equivalent evaluation of the pulled-back residual-cover square root `sqrt(h o phi)` at both conductor preimages;
- a conductor descent isomorphism stated directly at the `G/H` level.

This is exactly the semantic level fixed by the retained square-root/base-change note.

Source lock: `GENUS1-SPAN5-BALANCED16-000707-E2-SQRT-FACTOR-BASECHANGE-SEMANTICS.md`.

## 4. What is *not* concluded

This correction does **not** imply that every conductor pair is same-sheet. Two distinct normalization preimages can map to different `H`-orbits in the same residual fibre for global reasons, and their conductor gluing can still be deck-twisted.

It also does not alter the exact weighted-cut identity or the Hodge requirement. In the `e=2` case one still needs the opposite-sheet weighted sum to satisfy

```text
y/2 >= 84 l^2.
```

The correction only retires one proposed way of reading that sheet bit: the supported-node local involution cannot supply it.

## Routing consequence

Do not continue the route

```text
exact supported A1 branch jet
 -> choose between (p,q) and (-p,-q)
 -> infer residual G/H sheet.
```

The load-bearing continuation is instead

```text
normalization preimage
 -> H-orbit coordinate in R=C8/H
 -> residual s3H action / sqrt(h o phi)
 -> conductor pair sign.
```

This remains within the active retained leaf `MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP`, but narrows its admissible input semantics.

## Firewalls

- No conductor sign is assigned.
- No upper bound for the cross-sheet weighted sum is proved.
- `e=2` remains open.
- `e=4` remains open.
- `000707000f0f` remains open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- No finite degree window is released.
- MB104/span5/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No heavy-compute authorization.
- No merge authorization.
