# Stage32 MB104 — explicit BTVA span/degree reduction

Status: **RETAINED PARTIAL EXPLICIT REDUCTION / MB104 INCOMPLETE / NO CREDIT**

## Source theorem

Bruin--Thomas--Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasi-hyperbolicity*, Theorem 1.2 and Corollary 6.5, give explicit support/span restrictions for curves of geometric genus `0` or `1` on the perfect cuboid surface `X_pc subset P^6`.

For genus zero they prove:

```text
every genus-0 curve passes through at least six distinct nodes;
every genus-0 curve other than van Luijk's 32 plane conics
passes through at least seven nodes that span P^6.
```

For genus one they prove that the curve lies in a linear subspace of dimension at most one larger than the span of the singular points it passes through. Corollary 6.5 gives in particular:

```text
if span(C intersect Sing(X_pc)) has dimension <= 4 (=6-2),
then degree(C) <= degree(X_pc)=16.
```

They further state the convenient perfect-cuboid specialization that a genus-one curve is a component of a hyperplane section or passes through at least six singularities spanning a hyperplane.

## Adapter to the multibranch receiver

Let

```text
Sigma(D)={box nodes met by the image curve D},
N=#Sigma(D),
s=dim span(Sigma(D)) in P^6.
```

Then the MB104 population splits as follows.

### Geometric genus 0

If `D` is not one of the known 32 plane conics, then

```text
N>=7 and s=6.
```

The known 32 plane conics are smooth rational curves in the retained cuboid configuration. Their normalization is the curve itself, so they do not acquire two distinct normalization branches over a surface node merely from passing through that node. Consequently they are not a new generic source of the `r_i>=2` multibranch phenomenon; any use of this observation as an exact receiver exclusion must still source-lock the nodewise branch map of the known conics.

Thus the **unknown** genus-zero multibranch sector is forced into full node-span `P^6`.

### Geometric genus 1

If

```text
s<=4,
```

then BTVA gives the explicit degree bound

```text
d<=16.
```

This sector already has a genuine finite degree window. It may be routed to finite Picard/effectivity handling only after the mission decides whether to split MB104 population-wise; it does not release MB105 globally because the sectors `s=5` and `s=6` remain open.

For `s=5`, the node support spans a hyperplane; for `s=6`, it spans all of `P^6`. No population-wide degree bound for those sectors follows from BTVA Theorem 1.2 alone.

## Relation to the `R8` bottleneck

The branchwise FSM inequality remains

```text
d<=16g-16+4R8.
```

BTVA's span theorem controls **where distinct surface nodes lie**, not the number of normalization branches above one node. Therefore it does not itself upper-bound `R8` in the hard sectors.

The sharpened residual sectors are now:

```text
g=0: unknown multibranch carrier => node support spans P^6;
g=1: only support-span dimensions 5 or 6 can evade the explicit d<=16 window.
```

This is stronger than the non-effective `N<=13` finiteness result because it gives an actual degree cap on the low-span genus-one sector and an exact full-span requirement on unknown rational curves.

## Firewalls

- The known conic multibranch exclusion is not promoted without an explicit nodewise normalization/source lock.
- No degree bound is claimed for genus-zero full-span carriers.
- No degree bound is claimed for genus-one `s=5` or `s=6` carriers.
- MB104 remains incomplete; global MB105 enumeration is not released.
- No receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit is granted.
