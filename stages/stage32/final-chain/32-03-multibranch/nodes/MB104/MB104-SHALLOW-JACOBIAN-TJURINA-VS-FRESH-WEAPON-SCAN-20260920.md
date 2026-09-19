# MB104 — shallow Jacobian/Tjurina versus fresh-weapon scan — 2026-09-20

Status: **PRE-AUDIT SHALLOW TOP-DOWN SCAN / NEW LOG-TANGENT INTERFACE / NO CREDIT**

## Scope

The previous six-map jet route is not deepened.

This pass compares:

A. a global Jacobian/Tjurina route for the hypothetical carrier C in |lP|;
B. an unrelated secant/self-intersection / normalization-image route.

The sole dangerous support remains

```
Sigma=000707000f0f.
```

## 1. Exact surface invariants

The resolved cuboid surface is the crepant resolution of the (2,2,2,2) complete-intersection
surface in P6.

Hence

```
H^2=16,
K_S=H,
K_S^2=16.
```

Rational double points preserve chi(O) and K^2 under the crepant resolution.  Since

```
p_g=h0(K_S)=7,
q=0,
chi(O_S)=8,
```

Noether gives

```
c2(S)=12*8-16=80.
```

For the hostile ray

```
C=lP,
C^2=336l^2,
K_S.C=112l.
```

## 2. A — local Tjurina lower bound

At every singular point p of the reduced Cartier curve C, the germ is a reduced plane-curve
singularity in smooth surface coordinates.

Let

```
delta_p = local delta invariant,
mu_p    = local Milnor number,
tau_p   = local Tjurina number,
r_p     = number of analytic branches.
```

In characteristic zero,

```
mu_p = 2 delta_p - r_p + 1.
```

Almiron's theorem gives for every isolated reduced plane-curve singularity

```
mu_p / tau_p < 4/3,
```

equivalently

```
4 tau_p > 3 mu_p.
```

Put

```
delta = sum delta_p = 168l^2+56l,
B = sum_p (r_p-1).
```

Then

```
sum mu_p = 2 delta - B
```

and therefore

```
4 tau(C)
 > 6 delta - 3B
 = 1008l^2 + 336l - 3B.                    (TJ-LOW)
```

This is source-valid for arbitrary reduced plane-curve germs, not only branches or nodes.

## 3. Globalize tau through the logarithmic tangent bundle

Let

```
Tlog := T_S(-log C).
```

Because S is smooth and C is reduced with isolated singularities, Tlog is reflexive of rank two,
hence locally free on the smooth surface.

The logarithmic tangent exact sequence gives

```
c1(Tlog)=-(K_S+C),
c2(Tlog)=c2(S)+K_S.C+C^2-tau(C).
```

Thus

```
c1(Tlog)^2
 = (K_S+C)^2
 = 16+224l+336l^2,
```

and

```
4c2(Tlog)-c1(Tlog)^2
 = 304+224l+1008l^2-4tau(C).                (LOG-DISC)
```

Insert (TJ-LOW):

```
Delta_log
 :=4c2(Tlog)-c1(Tlog)^2
 < 304 - 112l + 3B.                         (LOG-CANCEL)
```

The entire l^2 term cancels.

This is the strongest new top-down identity found in this shallow pass.

## 4. What LOG-CANCEL does and does not prove

No stability or semistability of Tlog is currently retained.

Therefore a negative right-hand side is not itself a contradiction; it would imply Bogomolov
instability, which would require a further geometric exploitation.

More importantly, the branch-excess term

```
B=sum(r_p-1)
```

is not currently bounded linearly.

The six-fibration common ramification bound does not control B: several smooth branches may collide
at one singular point while each branch has multiplicity one and hence contributes zero to the
common ramification gcd.

Thus LOG-CANCEL yields a precise two-gate weapon:

```
Gate A1: control B with coefficient <112/3 per l,
or otherwise control the destabilizing geometry;

Gate A2: source-lock semistability/stability or exploit the Bogomolov destabilizing divisor.
```

It is not yet a finite-l theorem.

## 5. Why the naive global-Tjurina upper route is not selected

Plane-curve global Tjurina bounds of du Plessis--Wall type are powerful in P2, but a generic
projection of the present carrier has degree proportional to

```
H.C=112l.
```

Their natural quadratic scale is therefore on the order of

```
(112l)^2,
```

far above the intrinsic coefficient 168l^2 of delta.

No surface-specific Tjurina upper theorem with a favorable coefficient was found in the shallow
search.

The log-tangent formula is materially sharper because it uses the fixed surface Chern classes and
causes exact l^2 cancellation.

## 6. B — secant/self-intersection fresh weapon

Achilles--Manaresi--Schenzel provide degree formulas for secant varieties of singular projective
curves in terms of degree, normalization genus, local self-intersection multiplicities and branch
data.

This is genuinely relevant in shape because it packages genus defect into a projective
self-intersection invariant.

However the retained embedding has degree

```
d=H.C=112l.
```

The standard positivity terms in secant/projection formulas are quadratic in d.  The shallow
source pass did not produce a cuboid-surface specialization whose leading coefficient approaches
the intrinsic 168l^2 scale.

Therefore there is no visible finite-l coefficient in this route at present.

Disposition:

```
SECANT/SELF-INTERSECTION = interesting invariant package,
but NO DEEP ALLOCATION from this scan.
```

## 7. Shallow verdict

```
A1 log-tangent/Tjurina cancellation : NEW and LIVE
A2 generic global Tjurina upper       : coefficient too large
B  secant/self-intersection           : no favorable coefficient found
```

The log-tangent route earns only one additional shallow round, not an open-ended depth allocation.

That round must compare, at equal depth:

1. whether B=sum(r_p-1) has any source-valid O(l) upper bound from existing MB geometry;
2. whether T_S(-log C) has a source-valid semistability/stability theorem in this fixed
   general-type surface setting, or whether Bogomolov instability itself forces a divisor class
   already excluded by the P-null/Picard arsenal;
3. one unrelated fresh weapon, so this route is not allowed to monopolize MB.

If neither log-tangent gate closes shallowly, park it.

## Firewalls

```
log_tangent_c2_formula_exact=true
almiron_mu_tau_bound_applicable=true
quadratic_term_cancels=true
branch_excess_linear_bound_known=false
log_tangent_semistability_known=false
finite_degree_window_proved=false
dangerous_000707_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
