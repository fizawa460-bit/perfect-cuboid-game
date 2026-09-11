# Stage32 MB104 — special 24-support `m=2` web is a hyperplane pencil

Status: **RETAINED EXACT SPECIAL-RESIDUAL DEGREE CAP / NOT POPULATION-WIDE**.

This note uses the 24-support residual isolated by `BTVA-M2-HYPERPLANE-ORBIT-CLASSIFICATION.json`.  It identifies the representative surviving quadratic differential explicitly and proves that its integral curves are components of a canonical hyperplane pencil.  Consequently this special residual cannot carry unbounded canonical degree.

## Source lock and basis

Use BTVA Table 1 / ancillary `perfectcuboid_script.m` in the basis

`(omega1,...,omega6,x1*eta,x2*eta,x3*eta,y1*eta,y2*eta,y3*eta,z*eta)`.

For the representative 16-node support the exact kernel line is

`omega* = omega1 - i*omega2 - omega3 + i*omega4 + i*omega5 + omega6`.

This is the exact `Q(i)` kernel obtained from the representative survivor `(H,p)=(318849034,5)`; it extends at precisely the representative 16-node support mask `4278538410`.

## Stereographic coordinates on the body-diagonal quadric

On the affine chart `x1=1`, write

`c=x2`, `v=x3`,

so the body-diagonal equation is

`z^2=1+c^2+v^2`.

On the dense open `z+1 != 0`, introduce

`u=c/(z+1)`, `w=v/(z+1)`.

Then

`c=2u/(1-u^2-w^2)`,
`v=2w/(1-u^2-w^2)`,
`z=(1+u^2+w^2)/(1-u^2-w^2)`.

Set

`t=u+i*w=(x2+i*x3)/(z+x1)`.

## Exact differential identity

Substituting the seven BTVA Table-1 formulas and the cuboid relations

`y1^2=c^2+v^2`,
`y2^2=v^2+1`,
`y3^2=c^2+1`,
`z^2=c^2+v^2+1`

into the representative section gives

`omega* = F(u,w) * (du+i*dw)^2`

with

`F(u,w)=(2-2i)/((u+i*w)(u+i*w-1)(u+i*w+i))`.

Equivalently,

`omega* = (2-2i)/(t*(t-1)*(t+i)) * (dt)^2`.

The quadratic discriminant is therefore identically zero in the cuboid function field.  The surviving object is a rank-one symmetric square / foliation, not a genuinely two-valued quadratic web.

This identity is an identity of rational symmetric differentials on a dense open and hence determines the same foliation wherever the reflexive section is defined.  The scalar factor is a nonzero rational function of `t`; it has no divisorial zero that could create a nonconstant extra integral family.

## Integral curves

Let `C` be an irreducible curve on the cuboid surface on which `omega*` pulls back identically to zero.

If `t|_C` is defined and nonconstant at the generic point, then `dt` is nonzero generically and the displayed identity cannot vanish identically.  Hence `t|_C` is constant.

Thus every such integral curve away from the indeterminacy set is contained in a fiber

`x2+i*x3 = lambda*(z+x1)`.

The possible fixed/indeterminacy components where numerator and denominator vanish simultaneously are also contained in members of this same hyperplane pencil, so they do not evade the degree argument.

Therefore every integral curve of the representative special foliation is a component of a hyperplane section of `X_pc`.

## Degree consequence

On the cuboid resolution `S`, the projective hyperplane class is the canonical class `H=K_S`, with

`H^2=16`.

A hyperplane-pencil fiber is an effective divisor linearly equivalent to `H`.  For every nonexceptional irreducible component `D` of such a fiber,

`d=H.D <= H.H = 16`.

Hence the representative special residual has the absolute cap

`d<=16`.

The other 23 special node-supports are obtained by the exact automorphism orbit from the hyperplane-orbit classification.  Surface automorphisms preserve `K_S` and canonical degree, so the same `d<=16` cap holds for all 24 special residuals.

## Consequence for the full-span `m=2` branch

The exhaustive hyperplane/outside classification shows:

- any projective-rank-7 node support has simultaneous `m=2` extension kernel of dimension at most one;
- if that kernel is nonzero, the support is forced into one of the 24 special 16-node supports and the surviving section is the corresponding special foliation.

Combining with the present calculation gives:

> **Any projective-rank-7 carrier for which a nonzero global reflexive `m=2` section extends across every met surface node has canonical degree `d<=16`.**

Thus an unbounded-degree rank-7 carrier, if it exists, must lie in the complementary branch where the simultaneous `m=2` extension space is zero.

For BTVA rational nonconics (`d>2`, node rank 7), this removes the entire nonzero-`m=2` branch from the unbounded-degree problem.  It does not exclude the zero-extension branch.

## Next obligation

`MB104_RANK7_M2_ZERO_EXTENSION_OR_HIGHER_M_GLOBAL_MEMBER_OBSTRUCTION`.

The next weapon must address carriers whose met-node support has rank 7 and for which **no** `m=2` reflexive section extends across all met nodes, using higher symmetric degree, a different sheaf/cover, or actual global-member geometry.

## Firewalls

- The bound `d<=16` applies to the 24 special nonzero-`m=2` residual, not to every multibranch carrier.
- `m=2` extension kernel zero is not a contradiction and is not a curve-existence obstruction by itself.
- No unibranch `176/192` cap is imported.
- No finite Picard enumeration release.
- No `R29-LG2-MB` discharge or receiver/effectivity/theorem/endpoint credit.
- Merge remains unauthorized.
