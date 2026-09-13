# Stage32 MB104 — `000707000f0f` e=2 O210 local-lift precedent boundary

Status: **RETAINED CROSS-LANE PRECEDENT AUDIT / NODE-ACTION REUSABLE, BRANCH-LIFT NOT RETAINED / NEXT INPUT LOCAL THETA EXPANSION / NO CREDIT**

## Scope

The active MB104 leaf needs an explicit map

```text
dangerous minimal branch / normalization preimage
 -> C8 x C8 product lift
 -> R x R
 -> residual G/H sheet.
```

A bounded repository lookup found the closest Stage32 precedent in the post-1490 O210 chain.

The relevant retained O210 source notes are:

```text
post1490-o210-q4-bolza-x-relative-h-marked-node-action-source-note.md
post1490-o210-q4-bolza-x-local-multiplicity-adapter-source-note.md
post1490-o210-q4-bolza-marked-tangent-information-boundary-source-note.md
post1490-o210-q4-equivariant-beauville-deck-cross-exclusion-source-note.md
```

under `stages/stage32/residual-32-01-production/`.

## 1. Reusable part: marked-node relative-H action

The O210 relative-H note identifies

```text
P=X(8)xX(8),
X=P/H_diag,
q:X->P/(HxH),
```

and source-locks the three nonidentity relative-H translations on the 48 marked X node lifts.

The key reusable semantic fact is narrow:

```text
a named first-factor H translation induces a definite permutation
of the marked node lifts.
```

This is sufficient for transporting data that are already attached to marked points, such as multiplicities.

It is **not** a branch-lift adapter.

## 2. Reusable part: multiplicity transport

The O210 local-multiplicity adapter proves that, once the local multiplicity at each marked lift is independently identified, the relative-H permutation can transport those multiplicities and support bounds such as

```text
I_x(D,t(D)) >= mult_x(D) mult_x(t(D)).
```

Again, the finite node permutation acts only after the local numerical datum is already attached to the marked point.

For MB104, the unknown datum is finer: which local normalization branch maps to which residual sheet. Node multiplicity or total branch count does not encode that information.

## 3. O210 itself records the missing tangent/branch boundary

The O210 marked-tangent information-boundary note explicitly states that the retained numerical class, marked multiplicities, and node permutations do not serialize:

- a local equation;
- tangent cone;
- branch jet;
- strict-transform point on the exceptional `P1`;
- infinitely-near cluster.

It concludes that these finer local data cannot be reconstructed from the retained Picard/node/multiplicity evidence.

The MB104 residual-sheet problem is at least this fine: distinct normalization branches over one box node must be distinguished before one can decide their product-cover/residual-sheet lift.

Therefore the O210 precedent does **not** supply the active MB104 map.

## 4. Why the final O210 deck-cross exclusion does not transfer directly

The O210 deck-cross closure eventually succeeds because an exact fixed Picard class, exact equivariant Picard action, exact exceptional multiplicities, and an independent global defect identity determine both sides of an intersection formula.

MB104 currently has no analogous exact effective-carrier local branch record. The active problem asks for branch-level sheet incidence, not merely divisor-class intersection transport.

Thus importing the final O210 numerical contradiction into MB104 would be a population/object mismatch.

## 5. Exact next missing input

The remaining missing object is local modular geometry at a supported box node.

A sufficient next asset is an explicit local expansion of the quotient/product map near a node-stabilizer fixed point, for example:

```text
(local carrier branch parameter)
 -> local X(8)xX(8) coordinates
 -> H-orbit factor coordinates in C8/H
 -> residual G/H sheet.
```

Equivalently, a theta-coordinate local model must distinguish the several normalization branches with the same downstairs box-node label.

This can be supplied by:

- a source-locked local theta expansion at the 48 box nodes;
- an explicit completed-local-ring quotient model with the H/G actions;
- a retained branch tangent/jet record together with the modular quotient map;
- an actual carrier equation permitting the local lift to be computed.

## Next leaf

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-LOCAL-THETA-PRODUCT-LIFT
```

Target: materialize the completed-local modular/product map at one supported node type and determine which local branch/tangent datum controls the residual sheet. Then use symmetry to test transport across all fourteen supported nodes.

## Firewalls

- O210 marked-node permutations are not promoted to branch permutations.
- O210 multiplicity transport is not promoted to residual-sheet transport.
- No tangent or branch jet is inferred from Picard64 or multiplicity data.
- No conductor sign is assigned.
- `e=2` and `e=4` remain open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
