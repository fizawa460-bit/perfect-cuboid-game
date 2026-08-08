# Stage14-e roadmap — two-face ambient control population

## Purpose

Stage14-e is an independent **front-side control track** for the exactly-two integral-face problem.

The main Stage14 track keeps the integer-space-diagonal condition. Stage14-e deliberately removes it. The point is not to solve an easier copy of the same problem, but to measure what the integer-space-diagonal square condition itself removes from the natural two-face ambient family.

The e-track must not replace or renumber the existing Stage14-4 / Stage14-5 roadmap.

## Locked ambient object

Let `e,x,y` be positive integer edges with `x<y` and

\[
\gcd(e,x,y)=1.
\]

Require two Pythagorean faces sharing `e`:

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2.
\]

Define the ordinary real Euclidean space diagonal only as a height

\[
D_{\mathbf R}:=\sqrt{e^2+x^2+y^2}.
\]

The cutoff is

\[
D_{\mathbf R}\le B.
\]

**No condition whatsoever is imposed that `D_R` be an integer or rational.**

The raw ambient population allows the third face to be either square or nonsquare. The exactly-two ambient population additionally imposes

\[
x^2+y^2\ne\square.
\]

The three directions are the position of the shared edge:

```text
a-ambient: e < x < y
b-ambient: x < e < y
c-ambient: x < y < e
```

Write the corresponding exactly-two ambient counts as

\[
E_a(B),\qquad E_b(B),\qquad E_c(B),
\]

and

\[
E_2(B)=E_a(B)+E_b(B)+E_c(B).
\]

These are **not** the main Stage14 counts `N_a^(2),N_b^(2),N_c^(2),N_2`; the latter also require an integer space diagonal.

## Structural link to the main Stage14 track

For two oriented primitive face data

\[
F_1=(S_1,X_1,H_1),
\qquad
F_2=(S_2,X_2,H_2),
\]

put

\[
g=(S_1,S_2),\qquad
\alpha=S_1/g,\qquad
\beta=S_2/g.
\]

The Stage14-4ab minimal gluing, which does not use the integer-space-diagonal condition, gives

\[
\boxed{
 e=\operatorname{lcm}(S_1,S_2)=g\alpha\beta,
 \quad x=\beta X_1,
 \quad y=\alpha X_2.
}
\]

With

\[
t_1=X_1/S_1,\qquad t_2=X_2/S_2,
\qquad L=\operatorname{lcm}(S_1,S_2),
\]

this is exactly

\[
(e,x,y)=L(1,t_1,t_2)
\]

and the e-track height is

\[
\boxed{D_{\mathbf R}=L\sqrt{1+t_1^2+t_2^2}.}
\]

Thus Stage14-e studies the full primitive two-face gluing family before the main-track filter

\[
1+t_1^2+t_2^2\in(\mathbf Q^\times)^2
\]

is imposed.

## 14-e1 — definition, bijection, and independent finite audit

Status: [>] Active.

Targets:

1. lock the raw and exactly-two ambient counting conventions;
2. prove that the Stage14-4ab two-face gluing is still a bijection after the space-diagonal square condition is removed;
3. prove that the real-height formula above is exact and direction-neutral;
4. implement two materially different finite enumerators:
   - edge-first ambient enumeration;
   - oriented-face-pair ambient enumeration;
5. require exact agreement of directional counts and third-face-square counts at several small cutoffs;
6. record finite data only as a diagnostic, not as an asymptotic theorem.

## 14-e2 — finite ambient reconnaissance

Status: pending 14-e1.

Targets:

- extend `E_a,E_b,E_c,E_2` to substantially larger `B`;
- record raw ambient versus exactly-two ambient populations;
- measure the third-face-square thinning separately;
- compare coarse growth candidates without promoting a finite fit to a theorem;
- compare the ambient direction vector with the main Stage14 finite direction vector.

## 14-e3 — total ambient growth

Status: pending 14-e2.

Targets:

- determine the true order of `E_2(B)`;
- exploit the exact lcm / Pythagorean-slope parametrization without any space-diagonal square condition;
- isolate the contribution of the shared-leg representation multiplicity
  \[
  a(S)=2^{\omega(S)-1}
  \]
  on its valid support;
- derive a rigorous asymptotic or matching upper/lower order before introducing any comparison with the main Stage14 square filter.

## 14-e4 — directionwise ambient asymptotic

Status: pending 14-e3.

Targets:

- determine whether
  \[
  E_a(B),E_b(B),E_c(B)
  \]
  have a common arithmetic factor times three chamber integrals;
- derive any limiting ambient direction vector from proof, not from finite ratios;
- identify whether the chamber geometry alone creates directional bias before the integer-space-diagonal condition is imposed.

## 14-e5 — space-diagonal filter comparison

Status: pending 14-e4 and sufficient progress in main Stage14.

This is the bridge back to the main problem.

Compare

\[
N_2(B)\subset E_2(B)
\]

and directionwise

\[
N_a^{(2)}(B)\subset E_a(B),\qquad
N_b^{(2)}(B)\subset E_b(B),\qquad
N_c^{(2)}(B)\subset E_c(B).
\]

Targets:

- quantify the thinning caused specifically by
  \[
  e^2+x^2+y^2=\square;
  \]
- study the ratio `N_2(B)/E_2(B)` only after both numerator and denominator have rigorous scales;
- determine whether the integer-space-diagonal filter is asymptotically direction-neutral or direction-biased;
- separate geometry/chamber bias from arithmetic square-filter bias.

## Scope boundary

Stage14-e does not assume a perfect cuboid exists or does not exist. It does not infer the main Stage14 growth order from the ambient family. It does not reuse a finite directional fit as an asymptotic law.

The e-track is intentionally a control population with one major condition removed.

```text
STAGE14_E_TRACK=DEFINED
INTEGER_SPACE_DIAGONAL_CONDITION=REMOVED_FROM_E_TRACK
REAL_SPACE_DIAGONAL_USED_AS_HEIGHT_ONLY=true
MAIN_STAGE14_NUMBERING_UNCHANGED=true
NEXT_E_TASK=Stage14-e1 definition bijection and independent finite audit
```
