# MB104 Z42 — Q-Gorenstein contraction local symmetric-Euler preflight wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-COMPLETE LOCAL-EULER INTERFACE WALL / NO CREDIT**

## Exact geometric input

Z41 upgrades the Birkar contraction to an exact Q-Gorenstein package.

For all three surviving balanced supports,

```text
K_Y ample,
3K_Y ~_Q A_Y,
K_Y^2 = 112/3,
e(Y_reg)=16,
index(K_Y) divides 3.
```

The nonrational contracted points are not quotient A_n points and are not log canonical.

### Size-48 local graph

Two connected points per support, each with exceptional graph

```text
Q1(-4,g=1) -- E(-2,g=0) -- Q2(-4,g=1)
```

and exact discrepancies

```text
(-4/3,-4/3,-4/3).
```

The fundamental cycle has arithmetic genus 2.

### Surviving size-768 local graph

One connected point with exceptional graph

```text
A(-4,g=1) ==two edges== B(-4,g=1),
with one (-2) leaf attached to each elliptic component,
```

and discrepancies

```text
a_A=a_B=-8/3,
a_EA=a_EB=-4/3.
```

The fundamental cycle has arithmetic genus 3.

## Target

The original Z12/BTVA route misses positivity at N=14 by cubic coefficient

```text
5/54.
```

After the actual Z3 contraction, one would need the leading asymptotic local Euler / local Chern
correction for symmetric powers of the cotangent sheaf at the above non-lc Q-Gorenstein
singularities.

A positive source-complete coefficient larger than the missing 5/54 would create a new exclusion
mechanism independent of l.

## Literature audit

The source-complete explicit formulas located by targeted searches are substantially narrower.

### Bruin--Ilten--Xu

*Local Euler characteristics of A_n-singularities and their application to hyperbolicity*
(arXiv:2312.01722) computes Wahl local Euler characteristics of symmetric differentials
explicitly for isolated surface singularities of type A_n, using toric/lattice-point methods.

This is not applicable to the Z41 graph singularities:

```text
not rational double points,
not quotient A_n singularities,
exceptional locus contains elliptic curves,
fundamental genus is 2 or 3,
discrepancies are below -1.
```

### Asega--De Oliveira--Weiss

*Surface quotient singularities and bigness of the cotangent bundle*, Parts I/II, develops
local cotangent-bigness invariants and explicit extension/local terms in the quotient-singularity
setting.

Again, the Z41 contraction points are not source-locked quotient singularities.

### Wahl / Blache / Langer general local theory

General local Euler/local Chern/orbifold-Euler frameworks provide definitions and structural
identities for normal surface singularities, but the targeted search did not locate a theorem that
takes only the present resolution graph, discrepancy vector and Q-Gorenstein index and outputs
the needed leading cubic coefficient for

```text
chi^0_local(Sym^m Omega_Y)
```

or its BTVA-equivalent correction.

In particular, no source-complete rule was found showing that the coefficient is determined purely
by:

```text
intersection matrix,
component genera,
fundamental cycle,
discrepancy vector,
K_Y index.
```

For nonrational/non-lc singularities analytic data may enter, so importing a quotient or A_n
coefficient by graph analogy is not justified.

## Exact disposition

The actual contraction is now much better understood than in the earlier one-quartic thought
experiment, but the local symmetric-Euler route remains blocked at one sharply identified
interface:

```text
INPUT:
  exact Q-Gorenstein singularity resolution graph + discrepancies + index<=3

MISSING:
  source-complete asymptotic local symmetric-differential Euler coefficient

FORBIDDEN:
  A_n / quotient formula substitution by analogy.
```

Therefore no N=14 BTVA sign repair is claimed.

## Next leaf

The index bound from Z41 suggests a more structured local route:

```text
MB104-Z43-INDEX-ONE-CANONICAL-COVER-PREFLIGHT
```

Target:

1. construct or characterize the local index-one cyclic cover of each nonrational contraction point;
2. determine whether the cover has a simpler Gorenstein/complete-intersection/weighted-homogeneous
   model;
3. if so, test whether existing Wahl/local-Chern formulas apply upstairs and descend through the
   order-3 action;
4. otherwise record that the analytic local model is still underdetermined by retained graph data.

Do not assume the index is exactly three where only divisibility by three is proved.

## Literature anchors

- Bruin--Ilten--Xu, arXiv:2312.01722, explicit local Euler quasi-polynomials for A_n.
- Asega--De Oliveira--Weiss, *Surface quotient singularities and bigness of the cotangent bundle*,
  Parts I/II, quotient-singularity framework.
- Wahl's local Euler characteristic framework for normal surface singularities.
- Langer's logarithmic/orbifold Euler framework; no non-lc graph-specific symmetric-power
  coefficient is imported here.

## Firewalls

```text
local_symmetric_euler_coefficient_computed=false
N14_BTVA_repaired=false
size48_orbits_excluded=false
surviving768_excluded=false
analytic_local_type_classified=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
