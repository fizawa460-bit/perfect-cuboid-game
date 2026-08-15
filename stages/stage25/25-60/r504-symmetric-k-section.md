# Stage25-r504 — generic non-torsion section on the symmetric-k quartic surface

STATUS=PROVED_STRUCTURAL_SUBMITTED_WITH_CHECKPOINT60
QUANTITATIVE_LOWER_UPGRADE=NO

The Stage24 symmetric-multiplier family leads to the moving quartic

\[
C_k:\quad t^4+1=(k^4+1)z^2.
\]

It has the obvious rational section

\[
P_C(k)=(t,z)=(k,1).
\]

This section gives a degenerate cuboid (`k^2p^2-q^2=0`) and therefore is not itself a Stage19 construction, but it carries non-torsion information on the genus-one surface.

## Elliptic model

The standard quartic map used already at `k=2` is

\[
X=-\frac{4t^2}{z^2},\qquad
Y=\frac{4t(t^4-1)}{z^3},
\]
which sends `C_k` to

\[
E_k:\quad Y^2=X^3-4(k^4+1)^2X.
\]

The section `P_C(k)` maps to

\[
\boxed{P(k)=(-4k^2,\;4k(k^4-1)).}
\]

At `k=2` this is exactly

\[
P(2)=(-16,120),
\]
the Stage24-50 point already audited to have infinite order. The fiber at `k=2` is smooth. Therefore `P(k)` cannot be torsion in `E_k(Q(k))`: a torsion section would specialize to torsion at every good specialization, contradicting the audited `k=2` specialization.

Hence

\[
\boxed{P(k)\text{ is non-torsion over }\mathbb Q(k).}
\]

## Explicit nondegenerate odd multiple

Using the elliptic doubling/addition formulas and mapping `3P(k)` back to the quartic gives

\[
\boxed{
t_3(k)=\frac{k(k^8-6k^4-3)}{3k^8+6k^4-1}
}
\]

and

\[
\boxed{
z_3(k)=
\frac{k^{16}+28k^{12}+6k^8+28k^4+1}
{(3k^8+6k^4-1)^2}.
}
\]

Direct substitution gives the identity

\[
t_3(k)^4+1=(k^4+1)z_3(k)^2.
\]

For reference, the `X`-coordinate obtained from the elliptic group law is

\[
X(3P)=
-\frac{4k^2(k^8-6k^4-3)^2(3k^8+6k^4-1)^2}
{(k^{16}+28k^{12}+6k^8+28k^4+1)^2},
\]
which is exactly `-4t_3^2/z_3^2`.

Unlike the original degenerate section, `t_3` is not identically `k` or `1/k`; it supplies a genuine moving nondegenerate rational point away from finitely many parameter values.

## Why this does not yet beat the quarter-power lane

This is structural progress, not a new global Stage19 lower theorem. After substituting this section into

\[
e=2kpq,\quad x=k^2p^2-q^2,\quad y=k^2q^2-p^2,
\]
the available cleared rational-height formulas are substantially higher degree than the degree-eight r501 family. For integer `k`, the direct representative has raw space height of degree 20. No theorem is proved that primitive reduction removes a growing factor large enough to reverse this disadvantage, and no uniform two-parameter aggregation over `k` and elliptic multiples is available.

Thus r504 establishes a **generic non-torsion moving section** and removes the earlier uncertainty that only `k=2` might be active, while leaving the quantitative lower upgrade open.

```text
R504_GENERIC_SECTION=P(k)=(-4k^2,4k(k^4-1))
R504_GENERIC_NONTORSION_SECTION_PROVED=true
R504_SPECIALIZATION_CERTIFICATE=k=2_to_audited_infinite_order_point
R504_EXPLICIT_3P_SECTION_PROVED=true
R504_3P_RAW_INTEGER_K_SPACE_DEGREE=20
R504_GLOBAL_STAGE19_LOWER_UPGRADE_PROVED=false
R504_UNIFORM_AGGREGATION_OPEN=true
```
