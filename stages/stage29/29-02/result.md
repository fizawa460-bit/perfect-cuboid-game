# Stage29-02 — new-foundation screening

```text
TASK_ID=Stage29-02
ROLE=NEW_FOUNDATION_SCREENING
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
OLD_FROZEN_GATE_REPLAY=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Screening question

Stage29-02 asks a narrower question than “which old bound can be sharpened?”  It asks whether the certified Stage16–28 surface supports a materially different global object, coordinate system, coverage adapter, or joint invariant that was not the main object of the earlier population stages.

The standing preflight is the audited Stage29-01 map plus Stage28 closeout, Stage19 exact shared-edge/toric interface, StageA2 closeout, and the Stage28 branch/local/fixed-curve weapons.  No old OPEN_GATE is counted as progress merely because it is restated here.

## 2. F1 — global perfect-cuboid geometry

Let

\[
S_0\subset \mathbf P^6_{[a:b:c:x:y:z:d]}
\]

be the projective endpoint model cut out by

\[
a^2+b^2=x^2,\qquad
a^2+c^2=y^2,\qquad
b^2+c^2=z^2,\qquad
a^2+b^2+c^2=d^2.
\]

On the positive nondegenerate chamber, primitive integral perfect cuboids are exactly primitive integral representatives of rational points of this model satisfying the physical ordering and height condition `d=R<=B`.  This is an endpoint model, not an existence theorem.

A symmetric face-diagonal rewrite is immediate:

\[
2a^2=x^2+y^2-z^2,\qquad
2b^2=x^2+z^2-y^2,
\]
\[
2c^2=y^2+z^2-x^2,\qquad
2d^2=x^2+y^2+z^2.
\]

Thus the endpoint may also be viewed as a multiquadratic lift over the face-diagonal projective plane.  This coordinate layer was not needed by the Stage16–28 population interfaces and is materially different from asking for another marginal upper/lower bound.

Screening verdict:

```text
F1_NEW_FOUNDATION_FOUND=true
F1_KIND=GLOBAL_ENDPOINT_COMPLETE_INTERSECTION_PLUS_FACE_DIAGONAL_MULTIQUADRATIC_MODEL
F1_AFFECTED_STAGES=19,20,28,29
F1_OLD_GATE_REPLAY=false
F1_BACKFLOW_RECOMMENDED=false
F1_NEXT_NATIVE_ITEM=29-06_GLOBAL_ENDPOINT_GEOMETRY
```

The missing theorem is not “prove this surface has no rational points.”  The first exact receiver is the adapter between this global model and the common Stage18/19/20 toric/joint-cover model, with exceptional loci, symmetry quotient, physical chamber, height and multiplicity preserved.

## 3. F2 — simultaneous completion cover

Stage28 gives a common two-face base

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

with function field `K=Qbar(Y)` and two distinct quadratic extensions

\[
K_{face}=K(\sqrt{f_{face}}),\qquad f_{face}=t_1^2+t_2^2,
\]
\[
K_{sp}=K(\sqrt{f_{sp}}),\qquad f_{sp}=1+t_1^2+t_2^2.
\]

The audited Stage28 squareclass-separation certificate proves that these quadratic extensions are distinct over the fixed base.  Therefore their compositum has degree four:

\[
K_{joint}=K(\sqrt{f_{face}},\sqrt{f_{sp}}),
\qquad [K_{joint}:K]=4,
\]

with generic Galois group `(Z/2Z)^2`.

This produces a third, previously unused quadratic subfield

\[
\boxed{
K_{cross}=K\!\left(\sqrt{f_{face}f_{sp}}\right)
}
\]

with

\[
f_{cross}=(t_1^2+t_2^2)(1+t_1^2+t_2^2).
\]

Over the common two-face host, a point lifts to the joint cover exactly when it lifts to both the third-face and space-completion covers.  Thus this is a direct simultaneous endpoint object rather than a comparison of two disjoint marginal populations.

The Stage28 branch decompositions also imply that the two branch divisors have no common geometric irreducible component: one consists of `4 x genus-0` components and the other of `2 x genus-1` components.  Hence the odd branch support of the cross quotient is their union, with profile

```text
CROSS_BRANCH_COMPONENTS=6
CROSS_BRANCH_GENUS_MULTISET={0,0,0,0,1,1}
CROSS_BRANCH_CLASS=-4K_Y
```

at the divisor-class screening level.  The associated line-bundle/canonical calculation suggests a qualitatively different canonical type from either marginal K3 cover, but singularity normalization and resolution effects are deliberately deferred to 29-07 and are **not** promoted here to a proved general-type classification.

Screening verdict:

```text
F2_NEW_FOUNDATION_FOUND=true
F2_KIND=JOINT_V4_COVER_PLUS_CROSS_QUOTIENT
F2_NEW_INVARIANT=CROSS_QUADRATIC_CHARACTER_f_face_times_f_sp
F2_AFFECTED_STAGES=28,29
F2_OLD_GATE_REPLAY=false
F2_BACKFLOW_RECOMMENDED=false
F2_NEXT_NATIVE_ITEM=29-07_JOINT_COVER_ENDPOINT_MODEL
```

This is the strongest new foundation found at 29-02.

## 4. F3 — parametrization coverage atlas

The repo already contains sharply different coverage statuses that were previously used locally rather than placed on one endpoint atlas.

Initial certified rows are:

| source | certified image/coverage status | endpoint firewall |
|---|---|---|
| Stage18/19 shared-edge toric coordinates | zero-loss physical reconstruction for the exactly-two-face host after the frozen chamber convention | does not itself impose the third face |
| Stage20 Saunderson parametrization | generically birational `P^1` onto a physical `M_face`-degree-six rational curve on the Stage20 K3 | curve-level construction, not Euler-population dominance |
| StageA2 equation-(6) `-18` family | family-specific two-cover/descent closure | `GENERAL_COVERAGE_PROVED=false`; no reverse map from arbitrary perfect cuboid |

The new content is not another family.  It is the requirement that every future family/model be classified by image dimension, generic degree, height distortion, exceptional locus and actual coverage before a family-specific closure is used in endpoint reasoning.

Screening verdict:

```text
F3_NEW_FOUNDATION_FOUND=true
F3_KIND=COVERAGE_ADAPTER_LAYER
F3_AFFECTED_STAGES=18,19,20,A2,29
F3_OLD_GATE_REPLAY=false
F3_BACKFLOW_RECOMMENDED=false
F3_NEXT_NATIVE_ITEM=29-08_PARAMETRIZATION_COVERAGE_ATLAS
```

## 5. F4 — joint local arithmetic

The separate Stage19 and Stage20 local densities were already compared in Stage28, and after removing the first-order quadratic-character oscillation their relative good-prime product is only a finite nonzero Euler-product constant.  That result concerns **marginal** acceptance laws.

The joint cover exposes a different local statistic.  For a good odd prime `p`, away from branch/zero loci, let `chi_p` be the quadratic character.  The indicator that both radicands are nonzero squares is exactly

\[
\mathbf 1_{both}
=\frac14(1+\chi_p(f_{face}))(1+\chi_p(f_{sp}))
\]
\[
=\frac14\left(1+\chi_p(f_{face})+\chi_p(f_{sp})+\chi_p(f_{face}f_{sp})\right).
\]

The new term is precisely the character of the cross quotient from F2.  Therefore the local covariance of the two completion predicates is not determined by the two marginal densities alone: its genuinely joint part is carried by

\[
\chi_p(f_{cross})=\chi_p(f_{face}f_{sp}).
\]

Summed over the common base modulo `p`, this is the character-sum / point-count trace associated with the third quadratic quotient.  This gives a single object on which finite-field geometry and local correlation can meet.

Screening verdict:

```text
F4_NEW_FOUNDATION_FOUND=true
F4_KIND=JOINT_LOCAL_CORRELATION_AS_CROSS_QUOTIENT_TRACE
F4_AFFECTED_STAGES=19,20,28,29
F4_OLD_GATE_REPLAY=false
F4_BACKFLOW_RECOMMENDED=false
F4_NEXT_NATIVE_ITEM=29-09_JOINT_LOCAL_ARITHMETIC
```

Firewall: no product of these local correlations is promoted to a global perfect-cuboid count without a same-measure global theorem.

## 6. Cross-lens synthesis

The four lenses do not produce four unrelated projects.  F1, F2 and F4 converge on one new structural object:

```text
NEW_FOUNDATION_NF01=GLOBAL_ENDPOINT_JOINT_V4_COVER
NEW_FOUNDATION_NF02=CROSS_QUOTIENT_CONTROLS_JOINT_LOCAL_CORRELATION
NEW_FOUNDATION_NF03=PARAMETRIZATION_COVERAGE_LAYER
```

In particular, the third quadratic quotient

\[
K(\sqrt{(t_1^2+t_2^2)(1+t_1^2+t_2^2)})
\]

is not present in the Stage28 marginal bridge comparison, because Stage28 was required to keep the perfect-cuboid endpoint deferred.  Its appearance here is therefore a genuinely new Stage29 receiver rather than a renamed Stage28 OPEN_GATE.

## 7. Backflow recommendation for 29-03

No immediate Stage16–28 reentry is recommended by this screen.

Reason: the new objects are endpoint/joint objects that earlier stages deliberately did not own.  The common two-face base, the two marginal covers, the branch decompositions, the physical reconstruction adapter, and the needed firewalls are already certified.  Reopening Stage18, Stage19, Stage20 or Stage28 now would mostly move Stage29 work backward rather than repair a missing old-stage foundation.

The proposed 29-03 decision is therefore

```text
FOUNDATION_BACKFLOW_CANDIDATES=NONE_AT_SCREENING_LEVEL
NO_FOUNDATION_BACKFLOW_REQUIRED_CANDIDATE=true
KEEP_NEW_WORK_STAGE29_NATIVE=true
```

This remains subject to fresh audit of 29-02.  A backflow becomes legal later only if 29-06/07/08/09 exposes an actual missing zero-loss adapter in an earlier stage.

## 8. Exact receivers created by the screen

```text
R29-G1=GlobalEndpointSurfaceToToricJointCoverAdapter
R29-J1=JointV4CoverNormalizationSingularityAndCanonicalModel
R29-J2=CrossQuotientBranchAndHeightModel
R29-C1=ParametrizationCoverageAtlasWithGenericDegreeAndHeight
R29-L1=CrossCharacterJointLocalCorrelationTheorem
```

These receivers are new enough to justify Stage29 continuation without replaying Stage27/28 theorem gates.

## 9. Submission state

```text
NEW_FOUNDATION_FOUND=true
MATERIALLY_NEW_ROUTE_FOUND=true
OLD_GATE_REPLAY=false
NEW_PERFECT_CUBOID_EXISTENCE_CLAIM=false
NEW_PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
P_FINITE_ZERO_THROUGH_5E8_PRESERVED=true
BACKFLOW_DECISION_DEFERRED_TO_29_03=true
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_AFTER_PASS=Stage29-03_FOUNDATION_BACKFLOW_DECISION
NEXT_EXPECTED_COMMAND=Stage29-audit
```
