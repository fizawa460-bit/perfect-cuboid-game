# Stage32 MB104 — population-wide finite-window reduction / member-level barriers

Status: **RETAINED PARTIAL MB104 / FINITE DEGREE WINDOW NOT YET PROVED / NO RECEIVER CREDIT**.

This checkpoint does not complete MB104. It records the strongest population-wide restrictions currently retained and the exact nonclosure walls accumulated so far. The active question has narrowed from numerical Picard/effectivity data to an ambient **box-surface-specific conductor/index bound for actual integral low-genus members**.

Let `D` be the strict transform of a nonexceptional integral curve in `R29-LG2-MB`, with normalization genus `g in {0,1}`. Write `n_i=D.F_i`, `d=K_S.D=n1+n2`, `M=sum M_i`, `R=sum r_i`, and `t=M-R=sum_branches(min(A,B)-1)>=0`. Let `s_min` be the number of node branches of the unique FSM-minimal type `(A,B)=(1,1)`.

## 1. Population-wide special-fibre identity

AM source-locks two factor directions, six Satake-boundary elliptics in each direction, and

`F_E = 2E + sum(8 incident exceptional curves)`.

Summing the six fibres in direction `i`, with `q_i` the total intersection with the six boundary elliptics, gives

`6*n_i = 2*q_i + M`, hence `q_i=3*n_i-M/2>=0`.

Therefore `M` is even, `M<=6*n_i` in both directions, and

`M<=6*min(n1,n2)<=3d`.

## 2. Generalized two-factor slack identity

The AR local ramification calculation is degree-independent. For normalization genus `g`, Riemann--Hurwitz gives

`2g-2+2*n_i-q_i = t+q_i_node+eta_i+rho_i =: sigma_i >=0`.

Substituting the special-fibre identity,

`sigma_i=M/2-n_i+2g-2`.

Adding both factor directions gives

`M-d+4g-4 = sigma_1+sigma_2 >=0`.

Hence

`d<=M+4g-4`.

Specializations:

- `g=0`: `d+4<=M<=3d`;
- `g=1`: `d<=M<=3d`.

Garcia-Fritz--Urzua Theorem 3.1 independently reaches the same coefficient-one wall for an unknown low-genus cuboid curve. Their stronger `d<=4g+44` corollary uses smoothness at the surface singularities and is not imported into the multibranch population.

## 3. Population-wide minimal-branch lower bound

Every nonminimal node branch `(A,B)!=(1,1)` consumes at least one unit from `t`, `q_1_node`, or `q_2_node`. If `U` is the number of nonminimal node branches,

`U<=t+q_1_node+q_2_node <= R-d+4g-4`.

Thus

`s_min=R-U >= d-4g+4`.

So

- `g=0`: `s_min>=d+4`;
- `g=1`: `s_min>=d`.

Therefore an independent upper bound `s_min<=alpha*d+beta` or `M<=alpha*d+beta` with `alpha<1` would close the degree direction directly.

## 4. Picard/Hodge exceptional-mass inequality

Stage29 source-locks `H=K_S`, `H^2=16`, and negative-definiteness of `H^perp`. The 48 exceptional curves are pairwise disjoint rational `(-2)` curves and `H.E_i=0`.

For `x=D-(d/16)H`, projection to the exceptional sublattice gives

`x_E=-sum_i (M_i/2)E_i`,

and hence

`D^2-d^2/16 <= -(1/2)sum_i M_i^2`.

Combining with adjunction and `Delta_strict>=0` gives

`sum_i M_i^2 <= d^2/8+2d-4g+4`.

By Cauchy over 48 exceptional curves,

`M^2 <= 6d^2+96d-192g+192`.

This improves the crude asymptotic coefficient from `3` to `sqrt(6)`, but `sqrt(6)>1`; it is still nonclosing.

## 5. Local lambda-capacity wall

AN gives the exact minimal resolved germ

`gamma_lambda(t)=(t,lambda*t,lambda^2*t)`, `lambda in C^*`,

for `(A,B)=(1,1)`. Arbitrarily many pairwise distinct nonzero `lambda` values can occur in the retained local A1 model over one node. Their strict transforms separate after resolution and the FSM weighted local divisor order does not see `lambda`.

Therefore no uniform local branch-capacity bound follows from the exceptional `P^1` landing coordinate alone. This is a local nonclosure statement only; it does not assert simultaneous global algebraic realization.

## 6. Known-curve cone wall and effective scaling ray

The exact upstream cuboid computation gives 92 nonexceptional known curves plus 48 exceptional curves. Reconstruction yields:

- `G1`: 32 conics, each through 6 nodes; 4 through each node;
- `G2`: 12 boundary elliptics, each through 8 nodes; 2 through each node;
- `G3`: 48 other elliptics, each through 4 nodes; 4 through each node.

For every integer `k>=1`, define

`D_k=6kH-k*sum_i E_i`.

Then

`d=H.D_k=96k`, `M=96k=d`, `D_k^2=480k^2`,

and the intersections with `G1`, `G2`, `G3`, and each exceptional curve are respectively

`6k`, `16k`, `20k`, `2k`.

So the full 140-known-curve nonnegative-intersection system admits an unbounded degree ray.

Riemann--Roch strengthens this from a formal numerical ray to effective divisor classes:

`chi(O(D_k))=240k^2-48k+8>0`,

while `H.(K_S-D_k)=16-96k<0`, so `K_S-D_k` is not effective and `h^2(D_k)=0`. Hence `h^0(D_k)>0` for every `k>=1`.

Critical firewall: this does not imply an integral member and does not imply geometric genus `0` or `1`.

## 7. Exact A1 contraction conductor / delta correction

MB102 measures `Delta_strict` on the smooth resolution. Contracting an exceptional `(-2)` curve back to a box-surface `A1` node creates an additional, exact normalization defect.

For one node with `M_i=D.E_i`, the numerical pullback is

`pi^*C = D + (M_i/2)E_i`.

Using the rational-surface delta formula / Blache correction for the `A1` lattice gives

`p_a(C)-p_a(D)=floor(M_i^2/4)`.

Therefore over all 48 nodes

`Delta_image = Delta_strict + Q_A1`,

where

`Q_A1=sum_i floor(M_i^2/4)`.

This correction is independent of the exceptional landing parameter `lambda`.

The function `floor(m^2/4)` is discretely convex. Writing `M=48q+r`, `0<=r<48`, the exact balanced minimum is

`Q_min(M)=(48-r)floor(q^2/4)+r floor((q+1)^2/4)`.

A convenient population-wide bound is

`Q_A1 >= M^2/192-12`.

Hence

- `g=0`: `Q_A1 >= (d+4)^2/192-12`;
- `g=1`: `Q_A1 >= d^2/192-12`.

This is a genuine quadratic member-level conductor debt on the singular box-surface image. It still does not bound `d` because the image arithmetic genus and projection discriminant degree can also grow quadratically.

The retained effective ray illustrates that nonclosure: there `M_i=2k` at all 48 nodes, so

`Q_A1=48k^2`.

## 8. S32-PW09 discriminant interface

The provisional Arsenal weapon `S32-PW09` supplies the exact normalization/conductor identity for a finite singular curve projection:

`Disc(pi)=Br(f)+2*A`,

with `deg A=delta` for the normalization-index divisor. Thus the A1 contraction debt contributes to the same index/discriminant ledger used by the two factor projections.

This suggested a possible closer: upper-bound the discriminant/index capacity at the six special factor values. Generic finite-map algebra shows that this route does **not** close without additional ambient geometry.

## 9. Generic special-discriminant capacity wall

Let

`A=k[[t]]`,

and let the normalized quadratic order be

`B'=A+uA`, `u^2=t`.

The normalized projection degree is fixed at `2`, and the normalized branch discriminant valuation at `t=0` is `1`.

For every integer `N>=0`, take the finite rank-two integral suborder

`B_N=A+t^N u A`.

Then:

- `Frac(B_N)=Frac(B')`;
- the normalization of `B_N` is `B'`;
- `length_A(B'/B_N)=N`;
- in the trace basis `[1,t^N u]`, the trace matrix is `diag(2,2t^(2N+1))`;
- therefore `v_t(Disc(B_N))=2N+1=1+2N`.

This is exactly the local identity `Disc=Br+2A` with index length `N`.

Consequently, even with **normalized projection degree fixed at 2 and only one special base value**, normalization index and discriminant multiplicity are unbounded. Six special values do not alter this generic conclusion.

Therefore:

`projection degree + number of special values + S32-PW09`

cannot by themselves upper-bound the quadratic `Q_A1` debt.

This wall does **not** assert that the orders `B_N` embed as curve germs in the cuboid surface and does not assert that they arise from the A1 contraction profile. It only proves that a successful bound must use additional ambient box-surface structure.

## 10. Current MB104 boundary

For every fixed `d`, the scalar/discrete search remains finite and can use the factor-slack interval, Hodge quadratic bound, A1 contraction debt, and the exact MB103 `Aut(S)` node-profile quotient. The degree direction remains globally infinite, so finite Picard enumeration remains forbidden.

The active sub-obligation is now

`MB104_AMBIENT_BOX_SURFACE_CONDUCTOR_CAPACITY_BOUND`.

A closing input must use structure absent from a generic finite map, for example:

- an ambient polar/jet/Jacobian restriction on singular curve orders inside the cuboid surface;
- a source-derived restriction on which finite suborders can occur for the two factor projections of embedded box-surface curves;
- a global linear-system theorem bounding normalization-index multiplicity at the six special fibres;
- or an independent subunit-slope upper bound on `M` or `s_min`.

Do not retry local `lambda` cardinality, the standalone known-curve cone, or generic discriminant-degree counting without such new ambient input.

## Source locks / firewalls

This checkpoint source-locks MB101/102/103, Stage29 finite-lattice geometry, AL/AM/AN/AR, the corrected FSM16 interfaces, the lambda wall, the exact known-curve/effective-divisor wall, the A1 contraction conductor certificate, and `S32-PW09` only at its provisional routing ceiling.

No Freitag--Salvati Manni unibranch `176/192` cap is imported into the multibranch population. No generic DVR order is claimed to occur inside the cuboid surface. No integral low-genus member of `D_k` is asserted. No finite degree window, finite Picard release, `R29-LG2-MB` discharge, receiver/effectivity/final-milestone/theorem/endpoint/Stage32/Perfect-Cuboid credit is claimed. Merge remains unauthorized.
