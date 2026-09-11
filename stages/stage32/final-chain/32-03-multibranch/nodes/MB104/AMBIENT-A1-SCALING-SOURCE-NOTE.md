# Stage32 MB104 — ambient A1 scaling wall

Status: **RETAINED ANALYTIC/NORMALIZATION NONCLOSURE / NO GLOBAL MEMBER / NO FINITE-DEGREE CREDIT**.

This note strengthens the earlier generic discriminant-capacity wall. The high-index quadratic order used there is not merely an abstract DVR construction: it occurs inside the actual local `A1` box-surface equation. Moreover, the retained effective Picard scaling ray admits a simultaneous local analytic profile satisfying the current node, factor-fibre, ramification, conductor, and genus-defect ledgers for every positive integer scale.

## 1. The generic order family embeds in the box node

The box-node germ is

`xz=y^2`.

For every integer `m>=1`, consider the irreducible parametrized curve germ

`gamma_m(s)=(x,y,z)=(s^2,s^(2m+1),s^(4m))`.

Then `xz=y^2` identically. In the FSM notation of post1648AN,

`ord(x)=A=2`,
`ord(y)=(A+B)/2=2m+1`,
`ord(z)=B=4m`,

so `(A,B)=(2,4m)` satisfies `A,B>0` and `A+B` even.

For the first factor base `x`, put `A0=k[[x]]=k[[s^2]]`. The curve image ring is

`R_m=k[[s^2,s^(2m+1)]]=A0+x^m*s*A0`.

Its normalization is `k[[s]]`, the projection degree over `A0` is exactly `2`, and

`length_A0(k[[s]]/R_m)=m`.

The trace discriminant valuation is

`2m+1=1+2m`,

exactly the `Br+2A` split from `S32-PW09`.

Thus the earlier generic family `B_N=A+t^N u A`, `u^2=t`, is realized inside the actual `A1` box-node equation by taking `N=m`, `t=x`, `u=s`.

The exceptional mass is fixed:

`min(A,B)=2`.

On the `x`-chart of the resolution, `u=y/x=s^(2m-1)`, so the strict transform has plane semigroup `<2,2m-1>` and delta `m-1`. The A1 contraction formula adds

`floor(2^2/4)=1`.

Hence the singular box-surface image has delta

`(m-1)+1=m`,

matching the normalization-index computation exactly.

Therefore **A1 ambient geometry + one factor degree + fixed exceptional mass do not bound normalization index**.

## 2. Simultaneous scaling witness on the retained Picard ray

The retained known-curve wall gives, for every `k>=1`, the effective divisor class

`D_k=6kH-k*sum_i E_i`,

with

`d=H.D_k=96k`,
`D_k.E_i=2k` for all 48 nodes,
`M=96k=d`,
`D_k^2=480k^2`.

The two source-locked factor fibre classes satisfy `F1+F2=H`, `F1^2=F2^2=0`, `F1.F2=8`, and every exceptional curve has zero intersection with a fibre class. Therefore

`n1=D_k.F1=48k`,
`n2=D_k.F2=48k`.

At every box node choose `2k` distinct nonzero landing parameters `lambda` and the FSM-minimal branches

`gamma_lambda(t)=(t,lambda*t,lambda^2*t)`.

Then at each node:

- `M_i=2k`;
- the normalization has `2k` local branches;
- all branches are minimal `(A,B)=(1,1)`;
- the strict transforms are separated on the exceptional curve;
- forced strict-transform delta on the exceptional locus is zero.

Globally this gives

`R=M=s_min=96k=d`,
`t=M-R=0`,
`q1_node=q2_node=0`.

For the retained Picard class, each of the 12 Satake-boundary elliptics has intersection `16k`. Taking those contacts simple and away from box nodes gives, in each factor direction,

`q_i=6*16k=96k`,
`eta_i=0`.

For genus one,

`sigma_i=M/2-n_i=48k-48k=0`.

Thus the factor-slack decomposition is compatible with `rho_i=0`. The normalized factor map has degree `48k`, so Riemann--Hurwitz requires total ramification `96k`; exactly `96k` simple smooth-boundary contacts, each with special-fibre order two, supply that ramification.

## 3. Conductor and genus-defect budgets also scale consistently

The exact A1 contraction debt is

`Q_A1=48*floor((2k)^2/4)=48k^2=d^2/192`.

Adjunction gives

`p_a(D_k)=1+(D_k^2+d)/2=1+240k^2+48k`.

A hypothetical integral member of geometric genus one would therefore require

`Delta_strict=240k^2+48k`.

As an analytic singularity budget at a smooth point of the resolved surface, this can be realized by the irreducible plane branch

`v^2=u^(480k^2+96k+1)`,

whose delta is exactly `240k^2+48k`.

The singular box-surface image would then have total normalization defect

`Delta_image=Delta_strict+Q_A1=288k^2+48k`.

This is only a simultaneous **local analytic/scalar feasibility witness**. It does not show that the class `D_k` has an integral member, that the prescribed germs globalize, or that a genus-one curve exists.

## 4. Consequence for MB104 routing

The following standalone routes are now nonclosing:

- local exceptional landing cardinality;
- known-curve nonnegative intersection cone;
- divisor-class effectivity;
- A1 contraction conductor debt by itself;
- generic `Disc=Br+2A` degree accounting;
- local A1 ambient equation plus exact factor-fibre/ramification scalar bookkeeping.

The remaining useful interface must be genuinely global at the member level. The next obligation is

`MB104_GLOBAL_LINEAR_SYSTEM_JET_OR_MEMBER_EXISTENCE_BOUND`.

A productive input must constrain which analytic profiles can occur in the actual complete linear systems of the surviving Picard classes, for example through jet/interpolation codimension, global polar/Jacobian conditions, irreducibility/member theorems, or another source-locked global result.

## Firewalls

- No global algebraic curve with these germs is constructed.
- Effectivity of `D_k` is not promoted to existence of an integral or genus-one member.
- The analytic scaling witness is not receiver discharge.
- Finite degree window remains open.
- Finite Picard enumeration remains unreleased.
- No receiver, effectivity, theorem, endpoint, or Perfect-Cuboid credit.
- Merge remains unauthorized.
