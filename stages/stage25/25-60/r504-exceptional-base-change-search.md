# Stage25-60 R504 exceptional base-change search

STATUS=ACTIVE_RESEARCH
ROUTE=R504
CHECKPOINT=60

## Purpose

The hostile repair-2 audit left exactly one repo-native lane live:

```text
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
```

This artifact executes that search rather than relabeling it as an external gate.

## Exact rank-jump receiver

For
\[
E_F:\ Y^2=X^3-4(k^4+1)^2X
\]
and a rational base change `k=phi(u)`, put
\[
C_\phi:\ y^2=\operatorname{num}(\phi(u)^4+1)\operatorname{den}(\phi(u))^4.
\]
The audited R504 twist-descent implies that a new independent pullback section requires an additional elliptic factor Q-isogenous to
\[
E_0:v^2=u^3-4u
\]
in the anti-invariant part of `J(C_phi)`.

The already audited candidates are

```text
BC1: phi(u)=u^2 -> CLOSED_NO_RANK_JUMP
BC2: phi(u)=(u^2-1)/(2u) -> CLOSED_NO_RANK_JUMP
```

## BC3 — phi_a(u)=(u^2-a)/(2u)

After clearing the square denominator,
\[
C_{3,a}:\ y^2=(u^2-a)^4+16u^4.
\]
The involution `u -> a/u` gives the inherited quotient. The complementary quotient is obtained from
\[
X=u+a/u,
\]
and is
\[
Q_{3,a}:\quad Y^2=X^4-8aX^2+16(a^2+1).
\]
For a binary quartic `AX^4+BX^3+CX^2+DX+E`, use
\[
I=12AE-3BD+C^2,
\]
\[
J=72ACE+9BCD-27AD^2-27B^2E-2C^3.
\]
Here
\[
I_{3}(a)=64(4a^2+3),
\]
\[
\boxed{J_{3}(a)=-1024a(8a^2+9)}.
\]
A residual genus-one quotient has `j=1728` only if `J=0`. Over Q,
\[
a(8a^2+9)=0
\]
has only `a=0`, which degenerates the degree-two map. Hence no nondegenerate rational BC3 member produces the required extra `j=1728` factor.

```text
R504_BC3_J=-1024*a*(8*a^2+9)
R504_BC3_NONDEGENERATE_RATIONAL_J_ZERO=false
R504_BC3_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
```

## BC4 — phi_a(u)=(u^2+a)/(2u)

The same computation gives complementary quotient
\[
Q_{4,a}:\quad Y^2=X^4+8aX^2+16(a^2+1),
\]
with
\[
I_{4}(a)=64(4a^2+3),
\]
\[
\boxed{J_{4}(a)=+1024a(8a^2+9)}.
\]
Again the only rational zero is the degenerate value `a=0`.

```text
R504_BC4_J=1024*a*(8*a^2+9)
R504_BC4_NONDEGENERATE_RATIONAL_J_ZERO=false
R504_BC4_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
```

## BC5 — phi_a(u)=a u^2

The pullback cover is
\[
C_{5,a}:\quad y^2=a^4u^8+1,
\qquad a\in\mathbf Q^*.
\]
Besides `u -> -u`, it has the rational involution
\[
u\mapsto 1/(au).
\]
The three genus-one quotient classes are represented by
\[
Q_0:\ Y^2=a^4X^4+1,
\]
which has `j=1728`, and the two complementary quartics
\[
Q_-:\ Y^2=X^4-4aX^2+2a^2,
\]
\[
Q_+:\ Y^2=X^4+4aX^2+2a^2.
\]
Their invariants are
\[
I_\pm=40a^2,
\qquad
J_\pm=\mp448a^3,
\]
so for every `a != 0`,
\[
\boxed{j(Q_-)=j(Q_+)=8000}.
\]
Thus the only `j=1728` factor is the inherited quotient; BC5 cannot create a second `j=1728` factor in this Klein-four decomposition.

```text
R504_BC5_EXTRA_QUOTIENT_J=8000,8000
R504_BC5_NONDEGENERATE_EXTRA_J1728_FACTOR=false
R504_BC5_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
```

## Status after BC3-BC5

The three fresh one-parameter symmetry-adapted mutation classes are now symbolically closed:

```text
R504_BC3_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
R504_BC4_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
R504_BC5_STATUS=CLOSED_NO_EXTRA_J1728_FACTOR
```

No finite scan in `a` is used. The closures come from exact invariant formulas.

This still does **not** classify an arbitrary degree-two rational base change. The live problem is now the general branch-parameter family: normalize a general quadratic rational map up to source PGL2, compute the genus-three pullback Jacobian decomposition, and solve exactly for the exceptional branch locus where an additional `E0`-isogeny factor appears.

```text
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_GENERAL_DEGREE2_BRANCH_LOCUS
R504_ARBITRARY_DEGREE2_CLASSIFICATION_PROVED=false
R504_NEW_RANK_JUMP_PROVED=false
R504_NEW_STAGE19_FAMILY_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## Next attack

Pass from BC3/BC4/BC5 to a general degree-two branch parameter. The next target is a normalized one-parameter degree-two family modulo source PGL2, followed by exact binary-quartic/Jacobian invariants and the exceptional `E0`-isogeny locus. Do not declare an external gate before that locus has been attacked.
