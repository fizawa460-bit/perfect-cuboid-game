# Stage32 MAIN scratch — residual-G tangent-capacity nonclosure

Status: scratch exact local-feasibility witness only. No MAIN/Q602/O210/theorem/receiver/endpoint/Perfect-Cuboid credit.

## Inputs

This leaf uses only the exact AQ/AR local semantics already retained on current main.

AQ gives the residual deck group `H ~= (Z/2)^3`, 12 target cusp points, target cusp multiplicities

`[35,24,18,19,28,21,25,34,20,5,5,32]`,

total multiplicity `266`, first-blowup delta lower bound `3350`, and total target-curve delta `8319`.

AR gives `N>=238` normalization branches over surface nodes and at least `186` FSM-minimal `(A,B)=(1,1)` branches. AQ separately gives at least `210` exceptional-contact-one branches.

## Local residual action

At the standard source cusp, Freitag--Salvati Manni use `p,q` with diagonal node stabilizer `(p,q)->(-p,-q)`. The box node has invariant coordinates

`x=p^2, y=pq, z=q^2`, `xz=y^2`.

For the residual quotient to the two factor bases use

`u=x=p^2`, `v=z=q^2`.

The nontrivial residual node stabilizer is represented by changing sign in one source factor, e.g. `(p,q)->(-p,q)`. Hence

`(x,y,z)->(x,-y,z)`.

On the A1 resolution chart `y=xw`, `z=xw^2`, this sends `w->-w`. Therefore a nonboundary landing `w=lambda in C*` maps to target tangent parameter

`c=v/u=lambda^2`.

Thus the stabilizer quotient identifies only `lambda` and `-lambda`; the target tangent parameter set remains `C*`, not a finite set.

## Explicit collision-free local witness

Take the extremal AR slack choice `t=28`, hence `N=266-t=238`.

Use 28 contact-two branches of type `(A,B)=(2,2)` and 210 contact-one minimal branches `(A,B)=(1,1)`. Distribute the 28 extra contact units among the first four target cusps as

`d=[10,8,5,5,0,0,0,0,0,0,0,0]`.

The resulting branch counts are

`r=[25,16,13,14,28,21,25,34,20,5,5,32]`,

so `sum r=238` and `sum(r+d)=266`.

Because every chosen node branch has `A=B`, both node-boundary ledgers have `q_node=0`. The exact AR slack identities are satisfied by

- factor 81: `52 = 28 + 0 + 24 + 0`;
- factor 105: `28 = 28 + 0 + 0 + 0`.

The corresponding smooth-boundary point counts are `86` and `182`, and the Riemann--Hurwitz totals replay to `162` and `210`.

At each target cusp choose pairwise distinct nonzero tangent values `c_{j,k}` and choose `lambda_{j,k}` with `lambda^2=c`. For contact one use the local model

`u=s`, `v=c s`.

For contact two use

`u=s^2`, `v=s^2(lambda+s)^2`.

The latter has multiplicity two at the target cusp, but after the first blowup its strict transform is smooth. Distinct `c` values separate all strict transforms on the first exceptional line. Consequently the current branch/multiplicity budgets admit a local configuration with no forced tangent collision and cusp delta equal to the existing first-blowup bound `3350`; the remaining target delta budget is `8319-3350=4969`.

This is only a formal local compatibility witness. It does not construct one global algebraic V6 carrier or prove that all twelve germs can occur simultaneously on one member.

## Decision

The route

`large node-branch count -> finite tangent capacity -> forced collision -> extra delta contradiction`

is nonpruning with the currently retained AQ/AR data. The residual involution `lambda->-lambda` does not create a finite tangent-slot bound because the invariant tangent coordinate is `lambda^2 in C*`.

A useful re-entry now requires genuinely new member-level information: a finite/algebraically constrained landing set, a global relation coupling the twelve cusp landing ratios, a source-bound discriminant/polar restriction, or another condition that forces two target tangents to coincide.

No current Stage32 authority changes.
