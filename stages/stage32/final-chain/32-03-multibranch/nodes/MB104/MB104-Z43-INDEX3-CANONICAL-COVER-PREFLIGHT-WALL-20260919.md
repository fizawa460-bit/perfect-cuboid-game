# MB104 Z43 — exact index-three canonical-cover preflight — 2026-09-19

Status: **PRE-AUDIT EXACT CANONICAL-COVER EXISTENCE / ANALYTIC-TYPE WALL / NO CREDIT**

## Input

Z41B gives, at every nonrational point of the Birkar contraction Y,

```text
local canonical index = 3,
3K_Y Cartier,
K_Y not Cartier.
```

The two local resolution types are:

```text
size-48:
Q(-4,g=1) -- E(-2) -- Q(-4,g=1),
discrepancies (-4/3,-4/3,-4/3);

size-768:
two elliptic (-4) components meeting twice,
one (-2) leaf on each,
discrepancies (-8/3,-8/3,-4/3,-4/3).
```

Both are strictly worse than log canonical.

## 1. Canonical index-one cover

For a normal Q-Gorenstein germ (Y,y) of index three, the standard canonical cover is

```text
pi:(Y#,y#) -> (Y,y)
```

obtained from the local graded algebra

```text
O_Y
 + O_Y(-K_Y)
 + O_Y(-2K_Y)
```

with multiplication closed using the local trivialization of O_Y(-3K_Y).

Therefore, at every nonrational contracted point,

```text
deg(pi)=3,
pi is quasi-etale off the singular point,
K_(Y#) is Cartier.
```

So Z41B upgrades the local problem to a degree-three Gorenstein canonical cover.

## 2. What the retained graph determines

The retained resolution graph and discrepancy vector determine exact numerical/topological data of
the downstairs singularity, including:

```text
intersection matrix,
component genera,
fundamental cycle,
canonical discrepancy cycle,
canonical index = 3.
```

They do not by themselves provide:

```text
the local canonical algebra multiplication,
a defining equation for Y#,
a weighted-homogeneous model,
a complete-intersection presentation,
the action of mu_3 on such a presentation.
```

These are analytic data.

## 3. Literature audit

Targeted searches found standard canonical/index-one-cover technology and substantial classification
results in special classes:

- quotient and log-canonical surface singularities;
- rational/minimally elliptic or splice-quotient situations under additional hypotheses;
- weighted-homogeneous/Gorenstein classes.

No source-complete theorem was located saying that a non-log-canonical index-three normal surface
singularity with the present genus-2/genus-3 exceptional graph is analytically determined by that
graph and discrepancy vector.

Indeed the normal-surface-singularity literature distinguishes topological/numerical Gorenstein
data from analytic Gorenstein realizations; graph data alone generally do not fix the analytic germ.

Therefore neither of the following may be asserted:

```text
Y# is a hypersurface,
Y# is a complete intersection,
Y# is weighted homogeneous,
Y# is splice type,
Y# belongs to a standard simple/minimally elliptic class.
```

## 4. Consequence for the local-Euler route

Upstairs one now has a Gorenstein germ with a degree-three deck action, but without a
source-complete analytic presentation.

Hence no exact symmetric-differential local Euler coefficient can yet be computed upstairs and
descended.

This is stronger than the previous Z42 wall in one respect:

```text
the only remaining local input is analytic classification of the index-one cover;
the canonical index itself is no longer unknown.
```

## 5. Next leaf

The most concrete remaining route is to derive the canonical algebra from the cuboid contraction
itself rather than from graph classification:

```text
MB104-Z44-CANONICAL-ALGEBRA-FROM-CUBOID-HYPERPLANE-PREFLIGHT
```

Target:

1. use the exact identities P=3K_S+F and the explicit support-hyperplane section;
2. identify local generators of O_Y(-K_Y) on the punctured contraction neighborhood;
3. determine whether their cubes/products are explicit rational functions inherited from the cuboid
   coordinates;
4. if this does not determine the local multiplication table, freeze the canonical-cover route.

Do not infer analytic type from the weighted dual graph alone.

## Literature anchors

- standard canonical/index-one cover construction for Q-Gorenstein singularities;
- Neumann--Wahl, splice quotient / end-curve theory, which requires additional analytic end-curve
  conditions;
- Popescu-Pampu, numerically Gorenstein versus Gorenstein surface singularities, emphasizing that
  numerical/topological canonical data do not generally determine the analytic realization.

## Firewalls

```text
canonical_cover_exists=true
canonical_cover_degree=3
canonical_cover_Gorenstein=true
canonical_cover_analytic_type_classified=false
canonical_cover_complete_intersection=false
local_symmetric_euler_coefficient_computed=false
surviving_orbits_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
