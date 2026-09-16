# Stage32 MB104 — `000707000f0f` e=2 residual-lift information boundary

Status: **RETAINED INFORMATION-BOUNDARY DIAGNOSIS / CURRENT ASSETS DO NOT DETERMINE CONDUCTOR PAIR SHEET / NEXT INPUT IS LOCAL NORMALIZATION-TO-PRODUCT INCIDENCE / NO CREDIT**

## Scope

The active target is to assign, for each pair of normalization preimages identified in the singular carrier, whether their lifts through

```text
q:R=C8/H -> S=C8/G
```

lie on the same or opposite residual sheet.

The retained data currently available are:

1. the joint quotient pair map `Psi:Q->R x R` is birational onto its image;
2. for each of the two zero quartics, the relevant two marked fibers of `psi_j:Q->R` are completely saturated;
3. in `e=2`, the residual base change over the normalization is split, equivalently `eta=0`;
4. the ambient/residual Kummer square class is explicit up to the verified square-class match.

## 1. What birationality supplies

For `e=2` one has

```text
Q=E,
Psi=(psi_1,psi_2):E -> R x R
```

birational onto a bidegree `(28l,28l)` genus-one correspondence.

Thus a **normalization point** is generically determined by its ordered pair of factor-quotient coordinates.

This does not identify two distinct normalization points that map to the same singular point downstairs. The conductor relation is an additional equivalence relation imposed by the singular carrier map

```text
nu:E -> C.
```

No retained leaf gives this relation as an explicit relation on `R x R`.

## 2. What two-fiber saturation supplies

For each zero quartic, seven supported nodes contribute `56l` distinct normalization points and exactly fill two degree-`28l` fibers of the relevant factor map.

Therefore the retained data determine the **multiset of factor values** occupied by those normalization points and the exact `28l/28l` total split.

They do not determine which of the `8l` branches over a fixed box node land in which of the two marked values, and they do not pair one branch with another branch through the conductor.

Hence saturation alone cannot recover the residual sheet comparison.

## 3. What eta=0 supplies

The equality

```text
eta=0
```

says that the normalized pullback

```text
Norm(E x_S R)
```

is the disjoint union of two copies of `E`. Equivalently, a global sheet section exists over the normalization.

This fixes sheet transport **along E**, but it does not specify how the two values of that section are identified when distinct points of `E` are glued by `nu:E->C`.

That missing identification is exactly the conductor/gluing character `kappa`.

Therefore the implication

```text
eta=0  =>  all conductor pairs are same-sheet
```

is invalid without an additional descent statement.

## 4. Exact missing datum

To evaluate a conductor pair `(x_i,x_j)`, one needs both:

```text
nu(x_i)=nu(x_j)
```

and the images of `x_i,x_j` in the residual product-cover fibre.

A sufficient explicit asset would be any one of:

- a local normalization parametrization of every dangerous minimal branch together with its lift to `C8 x C8`;
- an exact table mapping the branch landing key at each supported node to the two `H`-orbit factor values and residual `G/H` sheet;
- an equation for the singular carrier image in quotient coordinates whose normalization map records the two preimages at every conductor identification;
- an equivariant local model proving that a specified class of conductor identifications is forced same-sheet or forced opposite-sheet.

The current retained MB104 assets provide none of these maps.

## 5. Consequence for the mainbatch route

The active problem is therefore not presently a numerical optimization over the known `28l/28l` fiber totals. Such an optimization would silently treat unknown branch-to-sheet incidence as free data.

The correct next leaf is

```text
MB104-GENUS1-SPAN5-BALANCED16-000707-E2-LOCAL-NORMALIZATION-PRODUCT-LIFT
```

with target:

```text
construct or source-lock the local map
(branch / normalization preimage)
 -> (C8 x C8 product lift)
 -> (R x R residual quotient coordinates)
 -> G/H sheet.
```

Only after that map is available can the conductor weighted cut be evaluated or bounded.

## Firewalls

- This is an information-boundary result, not a nonexistence result.
- No conductor sign is inferred from `28l/28l` saturation.
- No per-node even split is inferred.
- `eta=0` is not promoted to descent through the singular carrier.
- `e=2` and `e=4` remain open.
- Geometric support core remains `864`; dangerous equality-packet core remains `768`.
- MB104/span5/receiver/theorem/endpoint/Perfect-Cuboid credit remains zero.
- No merge authorization.
