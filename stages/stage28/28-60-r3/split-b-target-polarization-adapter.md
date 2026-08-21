# Stage28-60-r3 split B — Stage20 target physical-polarization adapter

```text
SPLIT_ID=Stage28-60-r3B
ROLE=TARGET_POLARIZATION_IDENTIFICATION
STATUS=COMPLETE_AS_R3_SUBMISSION_PENDING_FRESH_AUDIT
```

The purpose of this split is to decide whether the Saunderson degree must be read in the same physical polarization normalization used on the Stage19 space cover. The answer is yes, after distinguishing "same line-bundle construction" from "the same divisor on the same K3": the two completion covers are different K3 surfaces, but both pull back the same anticanonical line bundle from the same toric base.

## 1. Common base line bundle

Stage14-e3 / PR #155 proves that the two-face toric host is

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

and that the physical edge-coordinate morphism

\[
\phi:Y\to\mathbf P^2,\qquad [1:t_1:t_2]=[e:x:y]
\]

satisfies

\[
\boxed{\phi^*\mathcal O_{\mathbf P^2}(1)=L=-K_Y},
\qquad L^2=4.
\]

Stage14-e8 / PR #163 and the frozen Stage20 final identify the third-face completion as a degree-two cover

\[
\pi_{face}:X_{face}\to Y
\]

with branch class `2L=-2K_Y`, resolving to the Stage20 K3 surface.

Define its physical quasi-polarization by

\[
M_{face}:=\pi_{face}^*L.
\]

Then automatically

\[
\boxed{M_{face}^2=2L^2=8}
\]

and, with

\[
\Phi_{face}=\phi\circ\pi_{face}:X_{face}\to\mathbf P^2,
\]

one has the exact line-bundle identity

\[
\boxed{M_{face}=\Phi_{face}^*\mathcal O_{\mathbf P^2}(1)}.
\]

Thus on a labeled physical Euler-brick point the `M_face`-height is represented by the same three edge coordinates `[e:x:y]`; under the primitive integral normalization its Euclidean norm is exactly

\[
\sqrt{e^2+x^2+y^2}=R.
\]

Permuting the three physical edges only composes `Phi_face` with a coordinate permutation of `P^2`, so it does not change the line bundle or curve degree.

## 2. Comparison with the Stage19 source

Stage14-4ah gives

\[
M_{sp}=\pi_{sp}^*L=\Phi_{sp}^*\mathcal O_{\mathbf P^2}(1),
\qquad M_{sp}^2=8,
\]

for the distinct space-square K3 cover `X_sp -> Y`.

Therefore the legal Stage28 comparison is

```text
SOURCE_K3=X_sp
TARGET_K3=X_face
COMMON_BASE=Y=Bl_4(P1xP1)
COMMON_BASE_LINE_BUNDLE=L=-K_Y
SOURCE_PHYSICAL_POLARIZATION=M_sp=pi_sp^*L
TARGET_PHYSICAL_POLARIZATION=M_face=pi_face^*L
SOURCE_M_SQUARED=8
TARGET_M_SQUARED=8
COMMON_PHYSICAL_EDGE_HEIGHT_NORMALIZATION=true
LITERAL_SAME_DIVISOR_ON_SAME_SURFACE=false
SAME_PHYSICAL_POLARIZATION_SPECIES=true
```

This is stronger and cleaner than inferring degree from the ambient `P^5` complete-intersection model alone. The Stage20 Saunderson `M_face`-degree must be computed from its three edge-coordinate forms, because those are exactly the pullback of the common `O_{P^2}(1)` physical height.

## Verdict

```text
TARGET_POLARIZATION_ADAPTER=PASS_CANDIDATE
SAUNDERSON_DEGREE_CAN_BE_COMPARED_DIRECTLY_TO_STAGE19_M_DEGREE=true
HEIGHT_ADAPTER_POWER_LOSS=0
FRESH_AUDIT_REQUIRED=true
```
