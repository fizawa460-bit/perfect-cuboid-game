# Stage29-02b — canonical projective model from the joint cover

```text
ROLE=JOINT_COVER_TO_FULL_P6_CANONICAL_MODEL
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

This note sharpens the dense-open function-field adapter to the canonical projective model.

## 1. The two-face base in physical anticanonical coordinates

Choose the unique shared edge `e`, the other edges `x,y`, and the two already-integral face diagonals `p,q`.  The two-face host satisfies

\[
e^2+x^2=p^2,
\qquad
e^2+y^2=q^2.
\]

Thus its physical projective model lies in

```text
[e:x:y:p:q] in P4
```

as an intersection of two quadrics.  Stage28 identifies the corresponding quasi-polarization on the smooth toric resolution

```text
Y=Bl_4(P1xP1)
```

as

```text
L=-K_Y,
h^0(Y,L)=5,
L^2=4.
```

The physical five-coordinate morphism is the anticanonical/quasi-anticanonical map associated with `L`; the special boundary curves on the weak del Pezzo may be contracted in the singular P4 image, which is why the smooth `Y` model remains the safe resolution-level base.

## 2. Add the two missing square roots

The joint cover adds

```text
z^2=x^2+y^2              # third face diagonal
d^2=e^2+x^2+y^2          # long/space diagonal.
```

Therefore its seven physical coordinates satisfy exactly

\[
\boxed{
\begin{aligned}
e^2+x^2&=p^2,\\
e^2+y^2&=q^2,\\
x^2+y^2&=z^2,\\
e^2+x^2+y^2&=d^2.
\end{aligned}}
\]

These are the four defining quadrics of the full cuboid/perfect-cuboid projective endpoint surface in `P6` after relabeling the three edges.

## 3. Canonical-section count

The V4 eigensheaf calculation gives

\[
h^0(K_{X_{joint}})=7.
\]

Five canonical sections come from

```text
H^0(Y,L)
```

and the two remaining one-dimensional character eigenspaces correspond to the two adjoined square-root coordinates.  Thus, up to a change of basis in the seven-dimensional canonical space, the canonical map of the joint cover is precisely

```text
[e:x:y:p:q:z:d].
```

Since

```text
K_joint=pi_joint^*L
```

and the image is the `(2,2,2,2)` complete intersection above, this recovers the known full endpoint canonical model directly from the Stage18/20/28 common-base architecture.

```text
JOINT_CANONICAL_H0_DIMENSION=7
CANONICAL_COORDINATES=5_BASE_SECTIONS_PLUS_2_SQRT_EIGENSECTIONS
P6_IMAGE_EQUATIONS=FOUR_CUBOID_QUADRICS
GLOBAL_ENDPOINT_CANONICAL_MODEL_IDENTIFICATION=PASS_CANDIDATE
```

## 4. What remains on the boundary

The smooth toric `Y` and the singular two-face P4 image differ by contractions of anticanonical-degree-zero boundary curves.  Likewise the normal joint cover and the canonical P6 endpoint model may differ by the corresponding lifted contractions / ADE resolutions.

These do not change the dense-open physical population and are compatible with the canonical-model interpretation, but the exact exceptional-curve matching should be tabulated before calling the two presentations globally isomorphic as resolved surfaces.

The former broad receiver

```text
R29-G1=GlobalEndpointSurfaceToToricJointCoverAdapter
```

is therefore reduced to the narrower boundary ledger

```text
R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger.
```

No separate height-power adapter remains: on a physical endpoint point the coordinate `d` is exactly the Euclidean space diagonal `R`, and the canonical physical chamber uses the same projective endpoint coordinates.

```text
HEIGHT_POWER_LOSS=0
PHYSICAL_ENDPOINT_CUTOFF=d=R<=B
GLOBAL_RESOLVED_SURFACE_ISOMORPHISM_AUDITED=false
```
