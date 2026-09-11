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
- pure powers of BTVA `omega_7`: available hyperplane vanishing and A1 regularization cost both have ratio `1/2`, leaving no multi-hyperplane slack.

## BTVA 13-form principal-part computation completed

The preflight for the 13-dimensional order-two BTVA space has now been pushed to an exact local computation. The ancillary file `arXiv:1912.08908v3/anc/perfectcuboid.out` gives 13 affine generators in the basis `(dx2^2,dx2*dx3,dx3^2)`.

For the A1 cone

```text
xz=y^2,
x=u^2,
y=uv,
z=v^2,
```

and resolution chart `s=u^2, t=v/u`, a constant tensor

```text
a du^2+b du dv+c dv^2
```

has exceptional pole polynomial

```text
P(t)=a+b*t+c*t^2,
```

via the principal part `P(t) ds^2/(4s)`. An FSM-minimal branch has `s=tau, t=lambda+O(tau)`, hence the order-two form is regular on that normalization branch iff `P(lambda)=0`.

At `R1=[1:0:0:0:1:1:1]`, direct substitution of the 13 BTVA forms gives principal tensors spanning

```text
t,
1-t^2,
1+t^2,
```

so the local principal-part map has rank `3`, the maximum possible. A second representative `R2=[1:i:0:i:1:0:0]` independently gives rank `3`.

The fixed nine Stoll coordinate substitutions send `R1` through a single orbit of all 48 nodes. Therefore every node has an intrinsic rank-three order-two principal-part map.

Detailed artifacts:

- `BTVA-13FORM-PRINCIPAL-PART.md`
- `BTVA-13FORM-PRINCIPAL-PART-CERTIFICATE.json`
- `verify_mb104_btva_13form_principal_part.py`

## Structural consequence: order two cannot count R8 multiplicity

Let `s_i` be the number of distinct exceptional landing directions among minimal `(1,1)` branches over node `i`. Requiring one order-two form to cancel its principal pole on all those branches gives at most

```text
min(3,s_i)
```

independent conditions at node `i`, because a binary quadratic is determined by three distinct landing directions. Repeated branches at the same landing direction impose the same principal pole-cancellation condition; after three distinct directions the condition has already saturated to full regularity at that node.

Thus the complete 13-form order-two portfolio sees at most

```text
sum_i min(3,s_i)
```

principal-part conditions. It does **not** count

```text
R8=sum_i r8_i
```

with multiplicity. Consequently, even fully materializing a fixed-basis `3x13` matrix at all 48 labels would not supply the missing `R8` upper bound: the limitation is structural, not missing matrix bookkeeping.

This closes the order-two BTVA principal-part portfolio as a standalone MB104 route.

## Current hard sectors and next live input

The unresolved population is concentrated in

```text
g=0: multibranch carriers with node support spanning P^6;
g=1: carriers with node-support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

The next successful input must charge **branch multiplicity**, including multiple minimal branches at one node, rather than only node support or finitely many landing-direction conditions. The live route classes are therefore narrowed to:

1. a global conductor/intersection inequality that charges every normalization branch or total exceptional mass with coefficient strong enough to imply `R8<=alpha*d+beta`, `alpha<1/4`;
2. a genuinely higher-jet/global constraint whose independent conditions grow with branch multiplicity rather than saturating at the order-two landing polynomial;
3. a new global symmetric differential architecture with stronger exceptional regularity/vanishing than the retained BTVA/GFU portfolios.

## Firewalls

No population-wide finite degree window is claimed. MB104 remains incomplete; finite Picard enumeration is unreleased. There is no receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit.
