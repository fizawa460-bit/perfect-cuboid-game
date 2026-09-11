# Stage32 MB104 checkpoint — finite window reduced to a high-span minimal-cusp branch problem

Status: **ACTIVE RETAINED CHECKPOINT / MB104 NOT COMPLETE / NO CREDIT**

## Core inequality

Reopening Freitag--Salvati Manni Theorem 3.1 at the exact bijective-normalization step gives the retained branchwise necessary inequality

```text
d <= 16g - 16 + 4R8,
```

where `R8` is the number of normalization branches over box nodes with minimal cusp type `(A,B)=(1,1)`. In the bijective case `R8<=48`, recovering `d<=176+16g`. Thus an explicit finite degree window follows from `R8<=constant` or `R8<=alpha*d+beta` with `alpha<1/4`.

## Positive population reductions now retained

### BTVA low-support finiteness

Bruin--Thomas--Várilly-Alvarado prove that only finitely many genus-0/1 curves on the perfect cuboid surface pass through at most 13 singularities. Therefore any potentially infinite multibranch family lies in

```text
N=#{i:r_i>0} >= 14.
```

This theorem is non-effective for Stage32 production: it does not list the finite exceptional curves or give their maximum degree.

### Genus-zero multibranch sector is full-span

BTVA prove that every genus-zero curve other than the known 32 plane conics passes through at least seven nodes spanning `P^6`. The Stoll source model shows each of the 32 conics is a smooth plane conic; normalization is therefore an isomorphism and every met node has `r_i=1`. Hence none is in `R29-LG2-MB`.

Consequently every genus-zero multibranch carrier satisfies

```text
N>=7,
dim span(Sigma(D))=6.
```

There is no remaining conic exception inside the multibranch receiver.

### Genus-one low-span sector has an explicit degree window

BTVA Corollary 6.5 gives

```text
dim span(Sigma(D)) <= 4  =>  d <= 16.
```

Thus only genus-one node-support span dimensions `5` and `6` remain outside an explicit BTVA degree window. This is a real finite-window subpopulation, but global MB105 remains gated because the high-span sectors are still open.

## Exact negative-route walls

### Local A1 geometry

Distinct minimal `(1,1)` branches can land at distinct nonzero points of the exceptional line and separate after resolution. The retained local packet gives no bounded number of minimal branches per node and does not force exceptional delta.

### Published GFU correction

Garcia-Fritz--Urzua Theorem 3.1 has exact degree

```text
-d + M + 4g - 4,
M=sum_i D.E_i.
```

There is no hidden negative branch-excess or delta correction. Their smooth-at-node bound `d<=4g+44` is the special case `M<=48`; the multibranch formula only gives `d<=M+4g-4` outside the integral locus. Their multiple-differential refinement gives lower exceptional-incidence bounds. Published GFU therefore does not upper-bound `R8`.

### Six rank-3 fibrations and Hodge

The six rank-3 genus-5 fibrations give only

```text
R8 <= M <= 6d.
```

Direct projection to `H` plus the 48 exceptional classes gives

```text
R8 <= sqrt(6d^2+96d-192g+192),
```

with asymptotic slope `sqrt(6)`. Both are far above the required `<1/4`.

### Local fibration jet wall

A minimal branch has local strict-transform germ

```text
x=t,
u=lambda+c*t+O(t^2),
```

with the first tangential coefficient `c` free in the retained packet. Even when the incident exceptional curve is a local section of a genus-5 fibration, a generic first jet makes the induced map unramified. Minimal cusp type alone therefore does not force even one ramification unit.

### Full 28-fibration Riemann--Hurwitz capacity wall

The 22 rank-4 fibrations occur in 11 complementary pairs with pair class sum `H`; their total restricted map degree is at most `11d`. The six rank-3 maps have total degree at most `3d`. Hence all 28 together satisfy

```text
sum_j n_j <= 14d,
B_total <= 28d+56(g-1).
```

Even under the impossible-best-case assumption that every minimal branch contributes one ramification unit to all 28 maps,

```text
R8 <= d+2g-2,
```

so the asymptotic slope is still `1`. More generally, aggregate forced ramification charge `q` per minimal branch gives slope `28/q`; MB104 needs

```text
q>112.
```

Thus ordinary unit-charging Riemann--Hurwitz architecture is structurally insufficient.

### Pure powers of the BTVA hyperplane-vanishing form

For BTVA `omega_7^k`, symmetric order is `2k`, total movable hyperplane vanishing is `k`, and Corollary 3.4 requires `k` vanishing units to regularize one selected `A1` exceptional component. Available and required ratios are both exactly `1/2`; there is zero slack. Splitting the hyperplane divisor among different node subsets cannot bypass the common-hyperplane span barrier.

## Concrete next computation: BTVA 13-form exceptional-valuation portfolio

BTVA compute

```text
dim H^0(X, SymHat^2 Omega_X^1)=13
```

with explicit generators. Their forms have nonuniform exceptional behavior: for example `omega_1` is already regular over a specified singular subset, while `omega_7` carries a hyperplane zero. For an `A1` node the order-two local Euler characteristic is `chi^0=3`, so regular extension is governed by at most three local principal-part conditions on this 13-dimensional space.

The next exact object is therefore the family of 48 linear maps

```text
L_i: V_13 -> W_i,  dim W_i<=3,
```

whose kernels are the order-two forms intrinsically regular at node `i`. The required computation is to source-lock the 13 forms and 48 nodes, calculate all `L_i`, quotient them by the retained `Aut(S)` action, and optimize products plus hyperplane twists. A positive result matters only if the resulting branchwise inequality reaches `R8<=alpha*d+beta` with `alpha<1/4` or otherwise gives a finite window on the remaining high-span sectors.

This route is recorded in `BTVA-13FORM-PORTFOLIO-PREFLIGHT.*`. No matrix or global regular section is claimed yet.

## Current hard sectors

After all retained reductions, the unresolved population is concentrated in:

```text
g=0: multibranch carriers with node support spanning all P^6;
g=1: carriers with node-support span dimension 5 or 6;
and in either case the potentially infinite sector has N>=14.
```

The exact numerical bottleneck remains the multiplicity-sensitive quantity `R8`, not merely distinct node support.

## Firewalls

No population-wide finite degree window is claimed. MB104 remains incomplete; finite Picard enumeration is unreleased. There is no receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit.
