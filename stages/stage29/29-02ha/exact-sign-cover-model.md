# Stage29-02ha — exact 64-fold sign/Kummer cover

Set homogeneous coordinates on the base plane

\[
[x:y:z]=[a_1^2:a_2^2:a_3^2]\in \mathbf P^2.
\]

There is no base point: if `a1=a2=a3=0`, the four cuboid equations force all seven canonical coordinates to vanish, impossible in projective space. Hence

\[
\pi:\bar S\longrightarrow \mathbf P^2,
\qquad
[a_1:a_2:a_3:b_1:b_2:b_3:c]
\mapsto [a_1^2:a_2^2:a_3^2]
\]

is a morphism.

Define the seven linear forms

\[
L_{a1}=x,\quad L_{a2}=y,\quad L_{a3}=z,
\]
\[
L_{b3}=x+y,\quad L_{b2}=x+z,\quad L_{b1}=y+z,\quad L_c=x+y+z.
\]

The cuboid equations say exactly that the seven canonical coordinates are simultaneous square roots of these seven forms. Over the generic point of `P^2`, there are `2^7` sign choices, modulo simultaneous projective sign, hence

\[
\deg(\pi)=2^6=64.
\]

The deck group is

\[
G_{\rm sign}\cong (\mathbf Z/2)^7/\langle(1,1,1,1,1,1,1)\rangle
\cong (\mathbf Z/2)^6.
\]

The branch divisor is the seven-line arrangement

\[
D=V\bigl(xyz(x+y)(x+z)(y+z)(x+y+z)\bigr).
\]

Thus `Sbar` is the normal `(Z/2)^6` Kummer/sign cover of `P^2` obtained by adjoining the square roots of the seven forms, modulo the common projective sign.

## Canonical-class consistency check

For a uniform order-two abelian cover branched on seven lines,

\[
K_{\bar S}=\pi^*\left(K_{\mathbf P^2}+\frac12D\right)
=\pi^*\left(-3H+\frac72H\right)
=\pi^*(H/2).
\]

Since `pi^*H=2 O_Sbar(1)`, this recovers

\[
K_{\bar S}=O_{\bar S}(1),
\]

the canonical embedding used by Testa–Stoll. Numerically,

\[
K^2=64(1/2)^2=16,
\]

matching the audited smooth-resolution invariant. The 48 singularities are `A1`, hence crepant, so this numerical value survives minimal resolution.

## Exact arithmetic lifting criterion

Let

\[
A=\mathbf P^2\setminus D.
\]

Over `A`, `pi` is an etale `G_sign`-torsor. Choose `L_c` as reference. For

\[
q\in A(\mathbf Q),
\]

the fiber torsor is represented by the six square classes

\[
\delta(q)=\left(
\frac{x}{L_c},
\frac{y}{L_c},
\frac{z}{L_c},
\frac{x+y}{L_c},
\frac{x+z}{L_c},
\frac{y+z}{L_c}
\right)
\in (\mathbf Q^*/\mathbf Q^{*2})^6.
\]

Then

\[
q\text{ lifts to }\bar S(\mathbf Q)
\iff \delta(q)=1.
\]

Equivalently, the seven values `L_i(q)` have a common square class. Scaling the projective representative so that `L_c=1` then makes all seven values rational squares.

For a physical perfect cuboid one further requires the positive real chamber and nonzero edge coordinates. Clearing denominators converts a positive rational lift into an integral cuboid candidate, so this is an exact existence adapter rather than a thin-family parameterization.

```text
R29-KUM0=FullEndpointAsSevenLineZ2^6KummerCover
STATUS=PASS_CANDIDATE_DIRECT_FROM_ENDPOINT_EQUATIONS
R29-KUM1=ExactBasePlaneSquareclassTorsorCriterion
STATUS=PASS_CANDIDATE_DIRECT
```
