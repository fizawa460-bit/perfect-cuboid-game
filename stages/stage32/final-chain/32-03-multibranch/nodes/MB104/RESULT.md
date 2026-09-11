# Stage32 MB104 — population-wide finite-window reduction / coefficient barriers

Status: **RETAINED PARTIAL MB104 / FINITE DEGREE WINDOW NOT YET PROVED / NO RECEIVER CREDIT**.

This checkpoint does not complete MB104. It records the strongest population-wide restrictions currently retained and, crucially, two exact nonclosure walls showing that neither purely local exceptional-landings nor the full known-curve numerical/effective-divisor cone can by themselves produce the required finite degree window.

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

These are genuine population-wide restrictions, but they do not bound `d` absolutely.

## 3. Population-wide minimal-branch lower bound

Every nonminimal node branch `(A,B)!=(1,1)` consumes at least one unit from `t`, `q_1_node`, or `q_2_node`. If `U` is the number of nonminimal node branches,

`U<=t+q_1_node+q_2_node`.

Since `q_i_node<=sigma_i-t`,

`U<=sigma_1+sigma_2-t = R-d+4g-4`.

Thus

`s_min=R-U >= d-4g+4`.

So

- `g=0`: `s_min>=d+4`;
- `g=1`: `s_min>=d`.

Therefore an independent upper bound

`s_min <= alpha*d+beta`

with `alpha<1` closes the degree direction directly. The same sharp threshold applies to an upper bound `M<=alpha*d+beta` because the factor slack already gives `M>=d-4g+4`.

The older threshold `alpha<1/4` is only a sufficient threshold if one insists on using the FSM tensor inequality `d<=16g-16+4*s_min` alone; it is not the sharp threshold after this direct lower bound.

## 4. Picard/Hodge exceptional-mass inequality

Stage29 source-locks `H=K_S`, `H^2=16`, and negative-definiteness of `H^perp`. The 48 exceptional curves are pairwise disjoint rational `(-2)` curves and `H.E_i=0`.

Set

`x=D-(d/16)H in H^perp`.

Since `x.E_i=M_i`, its exceptional projection is

`x_E=-sum_i (M_i/2)E_i`,

with

`x_E^2=-(1/2)sum_i M_i^2`.

Negative definiteness gives

`D^2-d^2/16 <= -(1/2)sum_i M_i^2`.

Adjunction and `Delta_total>=0` give

`D^2=2g-2+2Delta_total-d >= 2g-2-d`.

Therefore

`sum_i M_i^2 <= d^2/8+2d-4g+4`.

By Cauchy over 48 exceptional curves,

`M^2 <= 6d^2+96d-192g+192`.

This improves the crude asymptotic coefficient from `3` to `sqrt(6)`, but `sqrt(6)>1`; it is still nonclosing.

## 5. Local lambda-capacity wall

AN gives the exact minimal resolved germ

`gamma_lambda(t)=(t,lambda*t,lambda^2*t)`, `lambda in C^*`,

for the FSM-minimal type `(A,B)=(1,1)`. For every finite `N`, the retained local A1 model permits `N` pairwise distinct nonzero landing values over one node. The corresponding strict transforms are separated after resolution and have zero forced pairwise exceptional delta.

The retained FSM weighted local divisor order depends on `(A,B)` but not on `lambda`.

Therefore no uniform local constant capacity bound on the number of minimal branches at a node follows from this local model. A purely local exceptional-`P^1` landing-count route cannot yield the needed subunit coefficient. This is a local nonclosure statement only; it does not assert that arbitrary such germs occur simultaneously on a global algebraic curve.

## 6. Exact known-curve incidence reconstruction

The source-locked upstream `Cuboids/cuboids.magma` defines 92 nonexceptional known curves and the 48 exceptional curves, for 140 known curves in total. Reconstructing the 48 singular points and evaluating the exact defining equations of the three nonexceptional families gives:

- `G1`: 32 conics, each through 6 nodes; every node lies on 4 `G1` curves;
- `G2`: 12 boundary elliptics, each through 8 nodes; every node lies on 2 `G2` curves;
- `G3`: 48 other elliptics, each through 4 nodes; every node lies on 4 `G3` curves.

At a listed singular point the strict transform of a known nonexceptional curve meets the corresponding exceptional curve once, exactly as encoded by the upstream pairing matrix.

## 7. Infinite Picard ray defeating the standalone known-curve cone

Let

`E_total=sum_{i=1}^{48} E_i`

and for every integer `k>=1` define the integral Picard class

`D_k=6kH-kE_total`.

Then

`H.D_k=96k`,

so `d=96k`, while

`D_k.E_i=2k`

for every exceptional curve and therefore

`M=sum_i D_k.E_i=96k=d`.

Its self-intersection is

`D_k^2 = 36k^2 H^2 + k^2 E_total^2 = 576k^2-96k^2 = 480k^2`.

Using the exact incidence counts above:

- for every `G1` conic, `D_k.C=6k`;
- for every `G2` boundary elliptic, `D_k.C=16k`;
- for every `G3` other elliptic, `D_k.C=20k`;
- for every exceptional curve, `D_k.E_i=2k`.

Thus `D_k` has **strictly positive intersection with all 140 known curves for every `k>=1`**. It also satisfies the retained Hodge mass inequality.

Consequently the full system of nonnegative intersection inequalities coming from the 140 known curves cannot, by itself, bound the degree.

## 8. The ray consists of effective divisor classes

This wall is stronger than a merely formal numerical ray. On the cuboid resolution, `chi(O_S)=8`. Riemann--Roch gives

`chi(O(D_k)) = 8 + (D_k.(D_k-K_S))/2`

and hence

`chi(O(D_k))=240k^2-48k+8>0`.

Moreover

`H.(K_S-D_k)=16-96k<0` for `k>=1`.

Since `H` is nef, an effective divisor linearly equivalent to `K_S-D_k` is impossible. Therefore

`h^2(D_k)=h^0(K_S-D_k)=0`.

Riemann--Roch then gives

`h^0(D_k)=chi(O(D_k))+h^1(D_k) >= chi(O(D_k)) > 0`.

Hence every `D_k` is represented by an **effective divisor**.

This still does **not** imply that `D_k` has an integral member, and it certainly does not imply a member of geometric genus `0` or `1`. This distinction is load-bearing.

If an integral genus-one member existed in class `D_k`, MB102 adjunction would require

`Delta_total=(D_k^2+d)/2=240k^2+48k`.

The presently retained local/scalar interfaces do not give an upper bound contradicting that quadratic singularity budget. The local AN feasibility wall is not a global existence theorem.

Therefore even

`known-curve nonnegative cone + divisor-class effectivity`

is insufficient to close MB104.

## 9. What remains finite and what remains open

For every fixed `d`, the scalar discrete search is finite and can use:

- `n1+n2=d`;
- the factor-slack interval for `M`;
- the Hodge quadratic mass bound;
- `R<=M`;
- the exact MB103 `Aut(S)` canonicalizer on 48-entry intrinsic profiles.

But the degree direction remains globally infinite. Finite Picard enumeration is therefore still forbidden.

The next MB104 obligation is no longer a numerical/effectivity-cone problem. It is:

`MB104_GLOBAL_LOW_GENUS_MEMBER_SINGULARITY_BOUND`.

A closing input must control actual integral low-geometric-genus members, for example by one of:

- a global jet/polar/contact/conductor bound on `Delta_total`;
- a multi-fibration ramification inequality that charges the multibranch node data across sufficiently many independent fibrations;
- another theorem giving an absolute or subunit-slope bound for integral genus `<=1` members.

Do not retry local `lambda` cardinality or the standalone known-curve nonnegative cone without a new member-level coupling.

## Source locks / firewalls

This checkpoint source-locks MB101/102/103, Stage29 finite-lattice geometry, AL/AM/AN/AR, the corrected FSM16 interfaces, the lambda wall, and the exact upstream `MichaelStollBayreuth/Verification@51233ed...:Cuboids/cuboids.magma` blob `0422b698...`.

No Freitag--Salvati Manni unibranch `176/192` cap is imported into the multibranch population. No integral low-genus member of `D_k` is asserted. No finite degree window, finite Picard release, R29-LG2-MB discharge, receiver/effectivity/final-milestone/theorem/endpoint/Stage32/Perfect-Cuboid credit is claimed. Merge remains unauthorized.
