# Stage27-19-r6d — fixed-core representation multiplicity bridge

```text
TASK_ID=Stage27-19-r6d
PARENT_ROUTE=Stage27-19-r6c
ROUTE_KIND=UPPER_BRIDGE_TO_R402
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_MU=1/2
```

## Purpose

The earlier Stage27-19-r402f upper route stopped at the exact arithmetic representation gate

\[
s^2(m^2+n^2)=pg,\qquad n^2(r^2-s^2)=qg,
\]

where `tau=p/q` is reduced and `g` is the common integer core.  It asked for a representation-multiplicity theorem in dyadic `(H(tau),g)` ranges.

This route proves the fixed-`(p,q,g)` multiplicity part exactly.

## Lemma

Fix positive integers `p,q,g` with `(p,q)=1`.  The number of positive integer quadruples `(m,n,r,s)` satisfying

\[
s^2(m^2+n^2)=pg,
\qquad
n^2(r^2-s^2)=qg
\]

is

\[
\boxed{\ll \tau(pg)^2=(pg)^{o(1)}}.
\]

On the Stage27 physical range `pg<2B^2`, this is `B^{o(1)}` uniformly.

## Proof

From the first equation, `s^2|pg`.  The number of possible positive `s` is at most `tau(pg)`.  For each such `s`,

\[
m^2+n^2=\frac{pg}{s^2}.
\]

The number of ordered integer representations by two squares is at most

\[
r_2(pg/s^2)\le4\tau(pg/s^2)\le4\tau(pg).
\]

Thus there are at most `4 tau(pg)^2` triples `(s,m,n)`.

Once `(s,m,n)` is fixed, the second equation gives

\[
r^2=s^2+\frac{qg}{n^2}.
\]

If `n^2` does not divide `qg` there is no solution; if it does, the right side is fixed and there is at most one positive integer `r`.  Hence

\[
\boxed{\#(m,n,r,s)\le4\tau(pg)^2.}
\]

All primitive/canonical/exactly-two conditions only remove solutions, so the same upper bound holds on the physical population.

## Consequence for the tau-core route

For one reduced `tau=p/q`, let

\[
\mathcal G_{p,q}(B)=\{g:\text{at least one physical Stage19 representation occurs at }(p,q,g)\}.
\]

Write `G_{p,q}(B)=#mathcal G_{p,q}(B)` and let `w_B(p/q)` be the physical fiber multiplicity.  The lemma gives

\[
\boxed{
G_{p,q}(B)\le w_B(p/q)\le B^{o(1)}G_{p,q}(B).
}
\]

Therefore the polynomial exponent of a fixed-tau fiber is exactly the exponent of its **realized core support**, not hidden representation multiplicity.

Likewise

\[
w_B(p/q)(w_B(p/q)-1)
\le B^{o(1)}G_{p,q}(B)^2,
\]

so the r402f collision term reduces to a core-support energy problem.

This discharges the representation-multiplicity half of the old r402f restart contract.  It does **not** bound the number or energy of realized `g` values.

```text
FIXED_PQG_REPRESENTATION_BOUND_PROVED=true
FIXED_PQG_REPRESENTATION_BOUND=4*tau(pg)^2
FIXED_PQG_MULTIPLICITY_SUBPOWER=true
TAU_FIBER_EXPONENT_EQUALS_REALIZED_G_SUPPORT_EXPONENT=true
TAU_COLLISION_REDUCED_TO_G_SUPPORT_ENERGY=true
R402F_REPRESENTATION_MULTIPLICITY_GATE_DISCHARGED=true
REALIZED_G_SUPPORT_FIXED_POWER_BOUND_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-19-r6e
```
