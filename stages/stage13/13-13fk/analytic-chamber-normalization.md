# Stage13-13fk — analytic chamber normalization

> STATUS: `R06_GATE_A_ANALYTIC_CHAMBER_NORMALIZATION`
>
> PURPOSE: close the R05 review objection that `I_ab+I_ac+I_bc=pi^2/8` was asserted without a symbolic derivation.

Let

\[
\mathcal R=\{(x,y,z)\in S^2:0<x<y<z\}
\]

and

\[
w_{xy}=\frac1{\sqrt{x^2+y^2}},\qquad
w_{xz}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{yz}=\frac1{\sqrt{y^2+z^2}}.
\]

Write

\[
I_{ab}=\int_{\mathcal R}w_{xy}\,d\omega,\qquad
I_{ac}=\int_{\mathcal R}w_{xz}\,d\omega,\qquad
I_{bc}=\int_{\mathcal R}w_{yz}\,d\omega.
\]

We prove analytically that

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}}.
\]

## 1. Pass from the ordered chamber to the positive octant

Let

\[
\mathcal O=\{(x,y,z)\in S^2:x>0,y>0,z>0\}
\]

be the positive spherical octant and set

\[
W(x,y,z)=w_{xy}+w_{xz}+w_{yz}.
\]

The function `W` is invariant under all permutations of `(x,y,z)`. Apart from the measure-zero walls where two coordinates coincide, `\mathcal O` is the disjoint union of the six order chambers obtained by permuting

\[
0<x<y<z.
\]

Therefore permutation invariance gives

\[
\int_{\mathcal O}W\,d\omega
=6\int_{\mathcal R}W\,d\omega
=6(I_{ab}+I_{ac}+I_{bc}).
\]

Hence it remains to evaluate the octant integral of `W`.

## 2. Evaluate one pair-weight integral exactly

By permutation symmetry on `\mathcal O`,

\[
\int_{\mathcal O}w_{xy}\,d\omega
=
\int_{\mathcal O}w_{xz}\,d\omega
=
\int_{\mathcal O}w_{yz}\,d\omega.
\]

Use spherical coordinates with the positive `z` axis as polar axis:

\[
x=\sin\phi\cos\theta,\qquad
y=\sin\phi\sin\theta,\qquad
z=\cos\phi,
\]

where

\[
0<\phi<\frac\pi2,\qquad 0<\theta<\frac\pi2,
\]

and

\[
d\omega=\sin\phi\,d\phi\,d\theta.
\]

Since

\[
\sqrt{x^2+y^2}=\sin\phi,
\]

we obtain the exact cancellation

\[
w_{xy}\,d\omega
=\frac1{\sin\phi}\sin\phi\,d\phi\,d\theta
=d\phi\,d\theta.
\]

Thus

\[
\int_{\mathcal O}w_{xy}\,d\omega
=
\int_0^{\pi/2}\int_0^{\pi/2}d\phi\,d\theta
=\frac{\pi^2}{4}.
\]

Consequently

\[
\int_{\mathcal O}W\,d\omega
=3\frac{\pi^2}{4}.
\]

Combining with the six-chamber decomposition,

\[
6(I_{ab}+I_{ac}+I_{bc})=\frac{3\pi^2}{4},
\]

so

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}}.
\]

This is an exact analytic identity. Numerical quadrature is not used as proof.

## 3. Consequences for the Stage13 normalization

Since

\[
J_q=\frac{2I_q}{\pi},
\]

we also get

\[
\sum_qJ_q=\frac{2}{\pi}\frac{\pi^2}{8}=\frac\pi4.
\]

And since

\[
P_q=\frac{8I_q}{\pi^2},
\]

we have

\[
\sum_qP_q=1.
\]

Therefore the directional normalization and the total exactly-one constant are symbolically compatible with the Stage12 calibration.

```text
STAGE13_13FK=COMPLETE_ANALYTIC_CHAMBER_NORMALIZATION
SUM_IQ_ANALYTIC_PROOF_COMPLETE=true
POSITIVE_OCTANT_SIX_CHAMBER_PARTITION_USED=true
PAIR_WEIGHT_OCTANT_INTEGRAL=pi^2/4
SUM_IQ=pi^2/8
SUM_JQ=pi/4
SUM_PQ=1
NUMERICAL_QUADRATURE_USED_AS_PROOF=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
NEXT=13-13fl
```
