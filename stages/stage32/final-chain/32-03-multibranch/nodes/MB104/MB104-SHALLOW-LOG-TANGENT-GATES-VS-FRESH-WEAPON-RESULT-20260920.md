# MB104 — shallow log-tangent gates versus fresh weapon — 2026-09-20

Status: **PRE-AUDIT SHALLOW GATE CHECK / LOG-TANGENT PARKED / NO CREDIT**

## Scope

The previous scan produced the exact cancellation

```
Delta_log < 304 - 112l + 3B,
B=sum_p(r_p-1).
```

This pass tests exactly one shallow round:

A. can retained MB geometry force B=O(l) with coefficient <112/3?
B. is T_S(-log C) semistable/stable in the exact hostile setting, or does instability itself close?
C. does the contraction Y provide an unrelated Bogomolov/quasi-hyperbolicity weapon?

No route is deepened.

## A. Branch excess gate does not close

The retained six-fibration common ramification divisor controls

```
sum_q(m_q-1)<=80l
```

on 000707, where q runs over normalization branches and m_q is branch multiplicity.

This does not control

```
B=sum_p(r_p-1).
```

Ordinary nodes exhibit the separation sharply:

```
two smooth branches,
m_q=1 on both branches,
local common-ramification contribution=0,
r_p-1=1.
```

Thus an arbitrarily large collection of nodal collisions is compatible with zero branch-multiplicity
defect at every branch.  The current equality packet and conductor localization do not contain a
separate bound on the number of such smooth-branch collisions.

Therefore no retained MB theorem gives

```
B <= beta*l+O(1)
```

with beta<112/3, or even B=O(l).

This is a missing theorem, not a numerical calculation left undone.

Disposition:

```
LOG-TANGENT GATE A = FAIL SHALLOW.
```

## B. Semistability gate is not source-valid in the hostile setting

There are strong polystability/semistability theorems for logarithmic tangent/cotangent sheaves:

- Guenancia: logarithmic tangent polystability for log-canonical pairs with K_X+D ample;
- Chintapalli--Iyer: logarithmic cotangent semistability under normal-crossing / related hypotheses.

The hostile carrier is only known to be a reduced integral Cartier curve with arbitrary isolated
plane-curve singularities.

The pair

```
(S,C)
```

is not retained as log canonical, normal crossing, or in any other hypothesis class covered by
those theorems.

In fact the research problem explicitly allows singularities severe enough to account for

```
delta(C)=168l^2+56l.
```

Therefore semistability cannot be imported.

If Delta_log becomes negative, Bogomolov instability by itself only produces a destabilizing line
subsheaf/divisor.  No retained theorem converts that divisor into the already-classified P-null
locus, and without a bound on B even negativity is not uniform in l.

Disposition:

```
LOG-TANGENT GATE B = FAIL SHALLOW.
Do not build a destabilizing-divisor classification without a new bridge theorem.
```

## C. Fresh weapon: Bogomolov quasi-hyperbolicity after the P-contraction

The exact contraction Y is numerically tempting:

```
K_Y ample,
K_Y^2=112/3,
e(Y_reg)=16,
C_Y subset Y_reg,
C_Y in |3lK_Y|,
normalization genus=1.
```

Formally,

```
K_Y^2 - e(Y_reg)=64/3>0.
```

For a smooth compact surface of general type, positive second Segre number

```
c1^2-c2>0
```

is the classical Bogomolov regime yielding quasi-hyperbolicity/finiteness of rational and elliptic
curves.

However this theorem does **not** directly apply here.

The contraction Y has a non-log-canonical canonical-index-three singular point on the 000707
frontier.  The number e(Y_reg) is not, by itself, the second Chern number of a smooth compact
surface or a source-valid orbifold c2 for this non-lc singularity.

On the actual smooth resolution S,

```
c1(S)^2-c2(S)=16-80=-64<0,
```

so the ordinary smooth Bogomolov criterion goes in the wrong direction.

To use the attractive Y-numerics one would need a singular/orbifold/quasi-projective
quasi-hyperbolicity theorem whose local correction explicitly includes the retained non-lc
index-three contraction type.  This is exactly the local-correction hypothesis wall already seen in
Z42--Z46.

Disposition:

```
CONTRACTION QUASI-HYPERBOLICITY = HIGH-UPSIDE SOURCE WALL,
not an executable fresh closer.
```

## Round verdict

All three shallow gates fail to produce a visible finite-l return:

```
A branch excess B: no O(l) control;
B log tangent stability: theorem hypotheses unavailable;
C contraction hyperbolicity: non-lc local correction unavailable.
```

Therefore the log-tangent route is PARKED now, as required by the startup gate.

No destabilizing-divisor classification is launched.
No return is made to size48 local analytic work.

## Fresh portfolio for the next round

Rotate to three materially different top-down shapes:

1. **elliptic linear-series / syzygy receiver**
   - use the seven canonical-coordinate sections on the genus-one normalization,
   - the four ambient quadratic cuboid equations,
   - the exact support-hyperplane divisor and e=4 factorization when available,
   - ask whether the resulting special g^6_(112l) can exist for arbitrary l.

2. **singular pluricanonical low-genus theorem search**
   - search specifically for effective bounds on genus-one normalizations in |mK| on fixed
     Q-Gorenstein canonical/general-type models,
   - require hypotheses that actually tolerate the index-three non-lc point or work entirely on
     Y_reg.

3. **finite-receiver / elimination geometry**
   - seek an exact map from every hostile carrier to bounded discrete data (monodromy, branch
     partition, low-degree residual divisor, or finite Picard shell) whose size does not grow with l,
   - without duplicating the active 32-01 fibration classification.

All three must be scanned shallowly before any depth allocation.

## Firewalls

```
branch_excess_linear_bound_known=false
log_tangent_semistability_source_valid=false
contraction_bogomolov_directly_applicable=false
log_tangent_route_parked=true
finite_degree_window_proved=false
dangerous_000707_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
