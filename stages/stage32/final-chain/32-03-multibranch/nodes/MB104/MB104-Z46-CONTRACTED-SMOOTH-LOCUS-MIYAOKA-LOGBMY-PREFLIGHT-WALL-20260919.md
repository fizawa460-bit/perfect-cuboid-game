# MB104 Z46 — contracted smooth-locus Miyaoka/log-BMY preflight wall — 2026-09-19

Status: **PARALLEL PRE-AUDIT SOURCE-VALID THEOREM-SHAPE NO-GO / NO CREDIT**

## Motivation

The original Z16/Miyaoka route is weak on the smooth cuboid resolution because

```text
K_S^2=16 < c2(S)=80.
```

After the exact Z3 contraction, however, the numerical package becomes

```text
K_Y ample,
K_Y^2=112/3,
e(Y_reg)=16.
```

Numerically,

```text
K_Y^2 > e(Y_reg).
```

This suggests trying to rerun a canonical-degree bound directly on the singular contracted model or
its smooth locus.

## 1. The singular model is outside the log-canonical BMY hypotheses

The exact Z41 discrepancies are:

size-48 nonrational contraction point
```text
(-4/3,-4/3,-4/3);
```

size-768 nonrational contraction point
```text
(-8/3,-8/3,-4/3,-4/3).
```

Hence these points are strictly worse than log canonical.

Langer's logarithmic/orbifold BMY theorem for normal surfaces with boundary proves the BMY-type
inequality in the **log canonical** case.  Its local orbifold-Euler formalism therefore cannot be
applied to the Z41 contraction by simply inserting the exact graph or index-three data.

Likewise, klt/canonical `Q`-Chern class inequalities do not apply to these non-lc points.

Thus the attractive numerical comparison

```text
K_Y^2=112/3 > 16=e(Y_reg)
```

is not itself a theorem hypothesis available for the present singular surface.

## 2. Returning to the smooth compactification does not recover the sign

The canonical smooth compactification of

```text
Y_reg ~= S \ Null(P)
```

is the smooth cuboid resolution with complete null boundary D.

The exact Z45 calculation gives

size-48
```text
(K_S+D)^2=-28,
e(S\D)=16;
```

size-768
```text
(K_S+D)^2=-36,
e(S\D)=16.
```

Sabatino's explicit boundedness corollary for curves on open surfaces requires

```text
(K_S+D)^2 > e(S\D)
```

in addition to big-nef hypotheses.

Here the left side is negative.  Therefore the post-contraction positivity of `K_Y` does not
translate into positivity of the log-canonical divisor `K_S+D` on the smooth compactification.

This is exactly the discrepancy cost of resolving the non-lc contraction points.

## 3. Existing source-valid inequalities already consumed

Sabatino Theorem 1.1(i) itself does remain applicable on the smooth pair and was optimized exactly
in Z45.  It gives strictly positive minima

```text
size48:       >4/3,
surviving768: >28/3
```

for every l>=1.

No additional local correction with a source-valid sign is supplied by the normal-surface
log-BMY literature for the present non-lc singularities.

Langer's local orbifold Euler corrections are designed for the log-canonical framework; treating
the present worse-than-lc points as if they were quotient/orbifold points would be invalid.

## 4. Disposition

The contraction changes the raw numerical ratio dramatically but not in a theorem-compatible way:

```text
numerical:
  K_Y^2 > e(Y_reg)       YES

source-valid normal BMY hypothesis:
  Y log canonical        NO

source-valid smooth-log boundedness hypothesis:
  (K_S+D)^2 > e(S\D)    NO
```

Therefore the original Z16/Z2 idea cannot currently be revived solely from the contracted
smooth-locus invariants.

A future revival requires a canonical-degree/BMY theorem explicitly valid for the present
index-three **non-log-canonical** surface singularities, not a quotient/lc substitution.

## Literature anchors

- A. Langer, *The Bogomolov--Miyaoka--Yau inequality for log canonical surfaces*,
  J. London Math. Soc. 64 (2001), 327--343.
- A. Langer, *Logarithmic orbifold Euler numbers of surfaces with applications*,
  Proc. London Math. Soc. 86 (2003), 358--396.
- P. Sabatino, *An Explicit Bound for the Log-Canonical Degree of Curves on Open Surfaces*,
  PRIMS 58 (2022), Theorem 1.1.

## Firewalls

```text
contracted_K2_gt_e_reg=true
normal_logBMY_applicable=false
smooth_log_boundedness_corollary_applicable=false
new_canonical_degree_bound=false
surviving_orbits_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
