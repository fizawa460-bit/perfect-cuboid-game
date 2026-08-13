# Stage14-t6 — moving triple gate after the fixed-curve void

## Purpose

Stage14-4ak eliminates the last fixed physical `M`-degree-4 bisection mechanism. Therefore the Stage14-t triple correction can no longer be controlled by auditing finitely many minimal accumulating curves. This stage isolates the exact moving arithmetic condition that remains.

The triple identity is still

\[
E(B)=N_2(B)+3T(B).
\]

No bound `T(B)=o(sqrt(B))` is asserted here.

## Mirror structure of the two relevant elliptic quotients

Stage14-t4 identified the raw-pair quotient `E_R` with geometric j-type

\[
j_+(s)=256\frac{(s^2+s+1)^3}{s^2(s+1)^2},
\]

and the third-face quotient `E_W` with

\[
j_-(s)=256\frac{(s^2-s+1)^3}{s^2(s-1)^2},
\]

where `s=t^2` is the physical Pythagorean base parameter.

There is an exact identity

\[
\boxed{j_-(s)=j_+(-s)}.
\]

Thus the two elliptic gates needed for a triple point form a base-reflection pair. A physical triple point at `s>0` requires simultaneous rational lifting on the raw family at `s` and its reflected j-family at `-s`.

At the same physical rational base, the two j-invariants are never equal. Indeed

\[
j_+(s)-j_-(s)=
512\frac{(s^2+1)(s^2-s-1)(s^2+s-1)}{s(s-1)^2(s+1)^2}.
\]

For rational physical `s>0`, `s!=1`, none of the numerator factors vanishes over `Q`: `s^2+1` has no rational real root and the other two quadratics have discriminant `5`, not a rational square. Therefore `E_R(s)` and `E_W(s)` are not geometrically isomorphic at any physical rational base. This does **not** prove that they are non-isogenous.

## Double small-point gate

A physical triple point projects to rational points on both quotient factors `E_R(s)` and `E_W(s)` coming from the same genus-5 Humbert--Edge point. The raw projection is the Stage14 raw-pair point, so by the already frozen main/t4 interface it lies on a positive-rank specialization of `E_R`.

The physical cuboid height bound supplies bounded rational coordinates on both quotient maps. Because the quotient/birational maps have fixed degree, the same Weil-height versus canonical-height comparison used in Stage14-s3 gives the necessary moving condition

\[
\text{triple with }d\le B
\Longrightarrow
\begin{cases}
P_R(s)\in E_R(s)(\mathbf Q),\\
P_W(s)\in E_W(s)(\mathbf Q),
\end{cases}
\]

with both induced points lying in logarithmic canonical-height windows of shape

\[
\hat h(P_\ast)=O(\log B+\log H),
\]

for the relevant first-face hypotenuse/base height `H`. This statement is a necessary height gate, not a distribution theorem.

Accordingly, after 4ak the triple problem at `sqrt(B)` scale is a **simultaneous moving small-point problem on the reflected pair**

\[
E_+(s),\qquad E_+(-s),
\]

with an additional compatibility constraint because the two points must lift to the same Humbert--Edge genus-5 point / same physical `q`.

## Consequence of Stage14-4ak

Stage14-4ak proves

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

for the raw-pair Kummer problem. Hence the t5 branch-degree-8 root audit has zero actual roots to process. Any hypothetical `sqrt(B)`-scale contribution to `T(B)` must therefore come from a moving/higher-degree mechanism; it cannot be inherited from a fixed minimal `M`-degree-4 accumulating rational curve.

This removes one contamination mechanism but is not itself an estimate for `T(B)`.

## What is still missing

To prove

\[
T(B)=o(\sqrt B),
\]

one still needs a quantitative theorem showing that simultaneous compatible logarithmic small points on the reflected pair occur on `o(sqrt(B))` physical bases/objects. The current Stage14-s finite evidence that rank/Selmer type is concentrated while actual small-point fingerprints are dispersed is consistent with such sparsity, but it is not an asymptotic proof.

The next useful attack should therefore target one of the following equivalent interfaces:

1. a simultaneous first-small-point sieve for `E_+(s)` and `E_+(-s)`;
2. a uniform rational-point bound on the corresponding moving genus-5 fiber product that retains the physical height;
3. an arithmetic incompatibility/local sieve exploiting the shared `q` lift between the two reflected elliptic factors.

## Locked boundary

```text
STAGE14_T6=COMPLETE_MIRROR_DOUBLE_SMALL_POINT_GATE
FIXED_M4_TRIPLE_ROOT_AUDIT_CASES=0
RAW_TRIPLE_ELLIPTIC_PAIR=E_R(s),E_W(s)
J_W_S_EQUALS_J_R_MINUS_S=true
PHYSICAL_RATIONAL_BASE_J_INVARIANTS_EQUAL=false
GEOMETRIC_ISOMORPHISM_AT_SAME_PHYSICAL_BASE=false
NONISOGENY_PROVED=false
TRIPLE_REQUIRES_SIMULTANEOUS_RATIONAL_LIFT=true
TRIPLE_REQUIRES_DOUBLE_LOG_HEIGHT_WINDOW=true
MOVING_COMPATIBLE_SMALL_POINT_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t7 simultaneous reflected-pair small-point/local-compatibility sieve
```
