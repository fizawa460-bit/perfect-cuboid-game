# Stage32 MB104 checkpoint — finite window reduced to a high-span minimal-cusp branch problem

Status: **ACTIVE RETAINED CHECKPOINT / MB104 NOT COMPLETE / NO CREDIT**

## Core inequality

Reopening Freitag--Salvati Manni Theorem 3.1 at the exact bijective-normalization step gives the retained branchwise necessary inequality

```text
d <= 16g - 16 + 4R8,
```

where `R8` is the number of normalization branches over box nodes with minimal cusp type `(A,B)=(1,1)`. In the bijective case `R8<=48`, recovering `d<=176+16g`. Thus an explicit finite degree window follows from `R8<=constant` or `R8<=alpha*d+beta` with `alpha<1/4`.

## Positive population reductions now retained

BTVA low-support finiteness gives: any potentially infinite genus-0/1 multibranch family lies in `N=#{i:r_i>0}>=14`. The known 32 plane conics are smooth and therefore not in the multibranch receiver, so every genus-zero multibranch carrier is in the full-span sector. For genus one, BTVA gives `dim span(Sigma(D))<=4 => d<=16`; only span dimensions 5 and 6 remain outside an explicit BTVA window.

## Exact negative-route walls

The following routes are now retained as insufficient by themselves:

- local A1 landing/delta data: arbitrarily many minimal branches can use distinct exceptional landing points;
- published Garcia-Fritz--Urzua correction: exactly `-d+M+4g-4`, with no hidden branch-excess or delta cancellation;
- six rank-3 fibrations: only `R8<=M<=6d`;
- Hodge projection: only `R8<=sqrt(6d^2+96d-192g+192)`;
- minimal cusp plus one fibration: first tangential jet is free, so ramification is not automatic;
- all 28 genus-5 fibrations with unit charging: even impossible-best-case charging gives only `R8<=d+2g-2`; slope `<1/4` would require aggregate charge `q>112` per minimal branch;
- pure powers of BTVA `omega_7`: available hyperplane vanishing and A1 regularization cost both have ratio `1/2`, leaving no multi-hyperplane slack;
- Beauville two-fold cover: exact global Riemann--Hurwitz gives `r_odd>=d-4g+4`, a lower bound on odd contacts, not an `R8` upper bound.

## BTVA 13-form principal-part computation completed

The preflight for the 13-dimensional order-two BTVA space has now been pushed to an exact local computation. The ancillary file `arXiv:1912.08908v3/anc/perfectcuboid.out` gives 13 affine generators in the basis `(dx2^2,dx2*dx3,dx3^2)`.

For the A1 cone `xz=y^2`, double cover `x=u^2,y=uv,z=v^2`, and resolution chart `s=u^2,t=v/u`, a constant tensor

```text
a du^2+b du dv+c dv^2
```

has exceptional principal part

```text
(a+b*t+c*t^2) ds^2/(4s).
```

An FSM-minimal branch has `s=tau,t=lambda+O(tau)`, so the form is regular on that branch iff the binary quadratic vanishes at `lambda`.

At `R1=[1:0:0:0:1:1:1]`, direct substitution of the 13 BTVA forms gives principal tensors spanning `t`, `1-t^2`, `1+t^2`, so the local principal-part map has rank `3`, the maximum possible. A second representative `R2=[1:i:0:i:1:0:0]` independently gives rank `3`. The fixed nine Stoll coordinate substitutions send `R1` through a single orbit of all 48 nodes, hence every node has intrinsic rank three.

Detailed artifacts:

- `BTVA-13FORM-PRINCIPAL-PART.md`
- `BTVA-13FORM-PRINCIPAL-PART-CERTIFICATE.json`
- `verify_mb104_btva_13form_principal_part.py`

## Structural consequence: order two cannot count R8 multiplicity

Let `s_i` be the number of distinct exceptional landing directions among minimal `(1,1)` branches over node `i`. A binary quadratic is determined by three distinct landing directions, so the order-two portfolio imposes at most

```text
min(3,s_i)
```

independent principal-part conditions at node `i`. Repeated branches at the same landing direction impose the same condition, and after three distinct directions the condition has saturated to full regularity at that node.

Thus the complete 13-form order-two portfolio sees at most `sum_i min(3,s_i)`, not `R8=sum_i r8_i` with multiplicity. Even a full fixed-basis `3x13` table for all 48 labels would not repair this structural limitation. This closes the order-two BTVA principal-part portfolio as a standalone MB104 route.

## Sharp A1 conductor / downstairs-delta wall

Repeated branches **can** be charged by the delta invariant after contracting the exceptional curve. For every reduced curve germ with `r` normalization branches,

```text
Delta >= r-1.
```

Hence for the downstairs cuboid curve

```text
Delta_nodes_down >= R-N,
Delta_nodes_down >= R8-N8 >= R8-48,
R8 <= p_a(C)-g+48.
```

This is genuinely multiplicity-sensitive. However, the coefficient is sharp on an `A1` surface singularity. The `A1=1/2(1,1)` rational double point has reduced fundamental cycle, and collections of smooth transversal curvettes realize `Delta=r-1`. Therefore no universal stronger local coefficient can be obtained from branch count alone.

Combining this sharp local inequality with the classical Castelnuovo bound for a nondegenerate degree-`d` curve in `P^6` gives only

```text
R8 <= pi_6(d)-g+48,
pi_6(d) ~ d^2/10,
```

which is quadratic and cannot meet the required linear slope `<1/4`. Thus the local conductor route is useful as an exact interface but is also insufficient by itself.

Artifacts:

- `A1-CONDUCTOR-BRANCH-DELTA-WALL.md`
- `A1-CONDUCTOR-BRANCH-DELTA-CERTIFICATE.json`
- `verify_mb104_a1_conductor_branch_delta.py`

## Beauville odd-branch double-cover wall

The canonical two-fold Beauville cover gives a global parity-sensitive constraint. Let

```text
r_odd = #{normalization branches through box nodes with odd m},
```

where `m=min(A,B)` is the exceptional contact multiplicity. Every FSM-minimal `(1,1)` branch has `m=1`, hence

```text
R8 <= r_odd <= M.
```

For `R8>0`, the restricted double cover of the carrier normalization is connected and Riemann--Hurwitz gives

```text
2h-2 = 4g-4+r_odd.
```

The Beauville surface has a finite etale cover by a product of two curves of genus greater than one. Applying Riemann--Hurwitz to the two projections of the lifted curve gives

```text
K_X.Y <= 4h-4.
```

The quasi-etale canonical pullback gives `K_X.Y=2d`, therefore

```text
d <= 4g-4+r_odd,
r_odd >= d-4g+4,
r_odd is even.
```

This is a genuine global constraint but has the wrong direction for MB104: it lower-bounds odd contact instead of upper-bounding `R8`. Using `r_odd<=M` recovers `d<=4g-4+M`, i.e. the same direction as the retained GFU exceptional-mass inequality.

Artifacts:

- `BEAUVILLE-ODD-BRANCH-COVER-WALL.md`
- `BEAUVILLE-ODD-BRANCH-COVER-CERTIFICATE.json`
- `verify_mb104_beauville_odd_branch_cover.py`

## Current hard sectors and next live input

The unresolved population is concentrated in

```text
g=0: multibranch carriers with node support spanning P^6;
g=1: carriers with node-support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

The next successful input must charge branch multiplicity with a **global linear degree control**, not merely local branch count or odd-contact parity. The live route classes are narrowed to:

1. a cuboid-specific conductor/arithmetic-genus inequality linear in `d`, strong enough to combine with `R8<=p_a(C)-g+48`;
2. a genuinely higher-jet/global constraint whose independent conditions grow with branch multiplicity rather than saturating at order two;
3. a new global symmetric-differential architecture with stronger exceptional regularity/vanishing than the retained BTVA/GFU portfolios;
4. a high-span geometric restriction that directly bounds the remaining genus-zero full-span or genus-one span-5/6 sectors.

## Firewalls

No population-wide finite degree window is claimed. MB104 remains incomplete; finite Picard enumeration is unreleased. There is no receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit.
