# MB104 Z36 / Z4' — forced ordinary-singularity localization preflight wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-COMPLETE COUNT-ONLY / LOCALIZATION-INTERFACE WALL / NO CREDIT**

## Target

The retained Lu--Miyaoka adapter gives, for a hypothetical integral genus-one carrier

```text
C_l in |lP|,  l>=1,
```

the necessary lower bound

```text
n_ord(C_l) >= max(0,112l-224),
```

where `n_ord` counts ordinary nodes and ordinary triple points on the smooth resolution.

P6F independently proves that any such carrier is equigenerically isolated.

Z36 asks whether the forced ordinary singularities can be upgraded from a count to a
source-complete projective/postulation constraint strong enough to contradict the isolated carrier.

## 1. Exact scale comparison

For the hostile genus-one ray,

```text
delta_total = 168l^2+56l.
```

The Lu--Miyaoka theorem forces only

```text
n_ord >= 112(l-2)  for l>=3.
```

Thus the theorem controls only a linear number of ordinary singularities while the total genus defect is quadratic.

No retained statement says that the remaining

```text
delta_total - n_ord
```

is also ordinary, has bounded analytic type, or lies on a controlled zero-dimensional subscheme.

## 2. T-smoothness theorems require the missing data

Thomas Keilen, *Smoothness of Equisingular Families of Curves*,
arXiv:math/0308247, studies families in `|D|` with precisely specified singularity types

```text
S_1,...,S_r
```

and gives sufficient T-smoothness criteria of the form

```text
sum gamma_a(S_i) < c (D-K)^2.
```

The input is the complete equisingular singularity package (equivalently the associated local
zero-dimensional equisingularity schemes/invariants), not merely a lower bound on how many
members of the package happen to be ordinary nodes or triples.

The current Stage32 packet does not source-lock:

- the positions of the forced ordinary singularities;
- the split between nodes and triples;
- the analytic types of the remaining quadratic delta mass;
- the equisingularity zero-scheme;
- independence of the corresponding conditions on `|lP|`.

Therefore no source-valid T-smoothness/postulation theorem can presently be evaluated on the
actual carrier singularity package.

## 3. The linear ordinary count is not asymptotically strong enough by itself

Even if one pessimistically assigned a bounded number of linear conditions to each of the
forced ordinary nodes/triples, the resulting controlled condition count is only

```text
O(l).
```

By contrast,

```text
(lP-K)^2 = 336l^2 - 224l + 16
```

has quadratic growth.

Hence the known ordinary-singularity subpackage alone is not an asymptotic source of
overdetermination. Any successful T-smoothness contradiction must also classify/charge a
quadratic portion of the remaining singularity mass.

This is the same missing interface seen from a different angle in P6M and P6R.

## 4. Interaction with P6F

P6F gives

```text
equigeneric reduced tangent cone = 0.
```

This does not locate the singularities and does not imply that their local equations impose
independent ambient conditions.

Indeed an isolated obstructed/superabundant equigeneric point is compatible with negative
expected dimension. Thus combining P6F with the Lu--Miyaoka count still does not produce a
postulation theorem.

## Disposition

```text
forced ordinary node/triple count       = exact and linear in l,
ordinary singularity positions          = unknown,
full singularity-type package           = unknown,
quadratic delta localization            = unknown,
equisingularity scheme                  = not source-locked,
T-smoothness/postulation theorem usable = false.
```

Z36 is parked.

## Next route

The most concrete unresolved global calculation remains the first-normal-neighborhood class on
the surviving size-768 balanced orbit:

```text
MB104-Z37-SURVIVING-768-FIRST-NORMAL-EXACT-TRANSITION-REOPEN-PREFLIGHT
```

Unlike Z36, this has explicit equations for the two null elliptic quartics and two intersection
points. Reopen only to determine whether the normal-direction transition can be normalized and
computed exactly from those equations. Stop if the class depends on an unretained formal
trivialization choice.

## Source locks

Historical archive head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `LU-MIYAOKA-GENUS1-SINGULARITY-COUNT-SOURCE-NOTE.md`
  blob `82e247159d736f92aa1382a469fa1d46a81dbae0`;
- `MIYAOKA2008-ORBIBUNDLE-GENUS1-WALL.md`
  blob `f59898039325b8a919f195ed9b0a491885e8232d`.

Current compact branch:

- P6F note blob `e89426128010ae97a10fbd908346f6cf07fff109`;
- P6M note blob `f1b0037a7207c6bb137a72ab1f337f2f2eb52e18`;
- P6R note blob `8629902c454ae81221b7b0f610e3c621c3943f04`.

External theorem anchor:

- Thomas Keilen, *Smoothness of Equisingular Families of Curves*,
  arXiv:math/0308247.

## Firewalls

```text
ordinary_singularity_positions_localized=false
full_singularity_package_classified=false
T_smoothness_applied=false
finite_degree_window_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
