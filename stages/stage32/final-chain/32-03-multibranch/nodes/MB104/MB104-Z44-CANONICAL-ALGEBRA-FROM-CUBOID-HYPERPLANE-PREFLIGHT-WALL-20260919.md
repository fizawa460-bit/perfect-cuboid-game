# MB104 Z44 — canonical algebra from cuboid hyperplane preflight wall — 2026-09-19

Status: **PRE-AUDIT EXACT CANONICAL-ALGEBRA INTERFACE WALL / NO CREDIT**

## Input

Z41B proves exact local canonical index three at every nonrational contraction point and exact
line-bundle descent

```text
O_S(P) ~= phi^* O_Y(3K_Y).
```

Z43 therefore gives the degree-three canonical index-one cover

```text
Y# = Spec_Y( O_Y + O_Y(-K_Y) + O_Y(-2K_Y) )
```

locally at those points.

## 1. What the cuboid data actually materialize

The retained Z33G package gives an explicit rational section of `O_S(P)`,

```text
sigma,
div(sigma)=7(c=0)-4 sum_(i in Sigma) E_i,
```

and explicit componentwise trivializations on the zero elliptic quartics.

Z37/Z38 and the size-48 formal-null calculation then prove that the restriction of `O_S(P)`
is trivial on every finite thickening of each complete exceptional fiber.

Thus the repository proves existence of a compatible formal generator of the pullback of
`O_Y(3K_Y)`.

## 2. Missing datum for the canonical algebra

To write the index-one cover analytically, one needs a local generator of `O_Y(3K_Y)` on a
punctured contraction neighborhood together with the multiplication maps

```text
O_Y(-K) tensor O_Y(-K) -> O_Y(-2K),
O_Y(-K) tensor O_Y(-2K) -> O_Y(-3K) ~= O_Y.
```

Equivalently one needs a single local cubic relation for a degree-one canonical generator.

The retained data do not materialize:

```text
a punctured-neighborhood generator downstairs,
a single rational function whose cube defines the cover,
the multiplication constants of the local canonical algebra,
a mu_3-equivariant defining equation upstairs.
```

The explicit Z33G functions are sufficient for restriction/gluing calculations on the null curves,
but they are not a source-locked analytic presentation of the contracted germ.

## 3. Why the graph cannot fill this gap

The cyclic-cover literature explicitly warns that covering resolution data are not in general
recoverable from the embedded resolution graph alone.

In particular, Némethi's work on resolution graphs of cyclic coverings gives examples showing that
an embedded resolution graph does not by itself determine the resolution graph of the cyclic cover;
additional covering/monodromy data are required.

This is exactly the missing datum here. The retained weighted graph plus discrepancies determine
the canonical index, but not the canonical algebra multiplication.

Therefore it is not valid to guess that the index-one cover is:

```text
weighted homogeneous,
a hypersurface,
a complete intersection,
splice type,
or determined uniquely by the Z41 graph.
```

## 4. Disposition

The canonical-cover route has reached a clean interface:

```text
EXACT:
  index = 3,
  degree-three canonical cover exists,
  upstairs canonical divisor is Cartier.

MISSING:
  local canonical algebra / analytic cover equation.

NOT RECOVERABLE FROM:
  resolution graph + discrepancy vector alone.
```

No local symmetric-Euler coefficient is extracted.

## Next route

Return to a theorem that only needs the exact contraction/null divisor data:

```text
MB104-Z45-FULL-NULL-BOUNDARY-SABATINO-REOPTIMIZATION
```

Use the complete null divisor as the SNC boundary on S. Since a hypothetical carrier is disjoint
from the null locus, this replaces the earlier arbitrary-exceptional-boundary Z35 calculation by the
actual contraction boundary. Compute the exact Sabatino Theorem 1.1(i) minimum separately for the
size-48 and size-768 null graphs.

## Literature anchors

- Némethi, *Resolution Graphs of Some Surface Singularities, I. (Cyclic Coverings)*,
  arXiv:math/0003084.
- standard index-one/canonical cover construction for Q-Gorenstein singularities.

## Firewalls

```text
canonical_algebra_materialized=false
canonical_cover_equation_materialized=false
local_symmetric_euler_coefficient_computed=false
surviving_orbits_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
