# Stage27-20-r301t — occupied q1 support embeds into Stage14 active-face support by an exact Möbius adapter

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301s
SOURCE_STAGE=Stage20

## 1. Exact coordinate adapter

For a primitive oriented Stage14 face
\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]
use the frozen rational-circle coordinate
\[
q_0=u/v\in(0,1),\qquad
(S,X,H)=\delta^{-1}(v^2-u^2,2uv,v^2+u^2),\quad \delta\in\{1,2\}.
\]
The Stage20/27 torus coordinate attached to the same oriented face is
\[
q_1=\frac{H+X}{S}.
\]
Substitution gives
\[
\boxed{q_1=\frac{v+u}{v-u}=\frac{1+q_0}{1-q_0}},\qquad
\boxed{q_0=\frac{q_1-1}{q_1+1}}.
\]
Thus physical `q1>1` and Stage14 `q0 in (0,1)` determine each other uniquely. The primitive oriented face is reconstructed from reduced `u/v`; the parity factor `delta` is fixed by primitiveness.

## 2. Support injection

Let `Q(B)` be the occupied first-coordinate support from r301s. Every Stage27 survivor contributing an occupied `q1` contains the corresponding oriented primitive integral face, hence that face is an active Stage14 vertex at the same space-diagonal cutoff. Therefore
\[
\boxed{Q(B)\hookrightarrow V(B)}.
\]
Forgetting first-face orientation introduces at most an absolute face-swap multiplicity. No fixed power is lost.

This is deliberately only an injection. Stage14 `V(B)` also contains the other endpoint of each raw two-face edge and vertices from triple objects; equality with all active vertices is not asserted.

## 3. Packet transfer

The Stage14 complete packet decomposition can therefore be restricted to occupied `q1` support with at most its audited `B^o(1)` cell/decorative multiplicity. This reproduces the half-power ceiling but does not improve it by itself.

```text
STAGE27_20_R301T_STATUS=AUDITED_PASS_MERGED
Q1_TO_STAGE14_FACE_MOBIUS_ADAPTER_PROVED=true
Q1_TO_ACTIVE_FACE_SUPPORT_INJECTION_PROVED=true
Q1_EQUALS_ALL_STAGE14_ACTIVE_VERTICES_CLAIMED=false
FIXED_POWER_LOSS_IN_ADAPTER=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301u
```
