# Stage29-02b — joint V4 endpoint geometry preflight

```text
TASK_ID=Stage29-02b
ROLE=JOINT_V4_COVER_GEOMETRY_PREFLIGHT
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT=Stage29-02
OLD_GATE_REPLAY=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## 1. Main result

Stage29-02 found the simultaneous completion field

\[
K_{joint}=K(Y)(\sqrt{f_{face}},\sqrt{f_{sp}}),
\]

with

```text
f_face=t1^2+t2^2,
f_sp=1+t1^2+t2^2,
Y=Bl_4(P1xP1).
```

29-02b proves at dense-open/function-field level that this is exactly the full labeled perfect-cuboid endpoint:

```text
K_endpoint=K_joint.
```

The two square roots reconstruct the third face diagonal and the long diagonal with zero height-power loss.  The generic deck group is `V4=(Z/2)^2`.

## 2. Exact quotient diamond

The joint surface has the three nontrivial quadratic quotients

```text
X_face  = K(sqrt(f_face))       # Stage20 Euler/third-face K3
X_sp    = K(sqrt(f_sp))         # Stage19 space K3
X_cross = K(sqrt(f_face*f_sp))  # new Stage29 cross quotient.
```

The third quotient is the geometric carrier of the exact local covariance character `chi(f_face*f_sp)`.

## 3. Canonical classes and invariants

Using the Stage28 branch classes

```text
D_face ~ -2K_Y,
D_sp   ~ -2K_Y,
(-K_Y)^2=4,
```

and the standard abelian-cover Hurwitz formula, the joint cover has

\[
K_{joint}\sim\pi^*(-K_Y),
\qquad K_{joint}^2=16
\]

at the normal/canonical-cover level.

Its V4 eigensheaf decomposition gives

```text
pg_joint=7,
q_joint=0,
chi(O_joint)=8.
```

These independently reproduce the known full cuboid-surface invariants `K^2=16, pg=7, q=0`.

For the cross quotient the preflight predicts

```text
K_cross ~ pi_cross^*(-K_Y),
K_cross^2=8,
pg_cross=5,
q_cross=0,
chi(O_cross)=6,
```

with the full minimal-resolution/general-type promotion still subject to the complete singularity audit.

## 4. Canonical projective model

The two-face host in physical coordinates

```text
[e:x:y:p:q]
```

satisfies

```text
e^2+x^2=p^2,
e^2+y^2=q^2.
```

Adding the two joint square-root coordinates gives

```text
x^2+y^2=z^2,
e^2+x^2+y^2=d^2.
```

Thus the seven canonical coordinates reproduce the full four-quadric cuboid surface in `P6`.  The V4 eigensheaf decomposition also gives exactly seven canonical sections: five base `-K_Y` sections plus the two square-root eigensections.

Therefore the broad F1/F2 adapter is reduced from a vague birational comparison to a concrete canonical-model/boundary problem.

```text
GLOBAL_ENDPOINT_CANONICAL_MODEL_IDENTIFICATION=PASS_CANDIDATE
REMAINING_BOUNDARY_RECEIVER=R29-G1b
R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger
```

## 5. Exact Stage28 physical-polarization bridge

Let

```text
M_face=pi_face^*(-K_Y),
M_sp=pi_sp^*(-K_Y).
```

For the two quotient maps from the joint cover,

\[
\boxed{K_{endpoint}=q_{sp}^*M_{face}=q_{face}^*M_{sp}.}
\]

Hence for an endpoint curve `C` mapping generically with degree `delta` to a marginal curve `C_face`,

\[
\boxed{K_{endpoint}.C=\delta\,M_{face}.C_{face}}
\]

and analogously on the Stage19 side.

This is a zero-loss degree adapter between the Stage28 fixed-curve spectrum and the full endpoint canonical geometry.

### Saunderson rematch

The Stage20 Saunderson curve has audited `M_face` degree 6.  A split degree-one endpoint lift would therefore give an endpoint degree-6 curve, forbidden by Testa--Stoll.  Thus the lift is nonsplit and has endpoint canonical degree 12.

This **does not create a new nonsplitting theorem**: audited Stage27-19-r9 already proves directly that the Saunderson space lift is the smooth genus-3 curve

\[
y^2=t^8+68t^6-122t^4+68t^2+1.
\]

Stage29 supplies the new global canonical-degree explanation and generalizes the adapter to arbitrary marginal curves.

On the Stage19 side, even if a physical `M_sp=6` curve exists, it cannot lift trivially to a degree-6 endpoint family.  Thus the old optional M6 spectrum question is not a direct low-degree perfect-cuboid-family route.

## 6. Local singularity preflight

The exact Stage28 branch factors were checked locally.

- same-colour transverse branch crossings give `A1` singularities;
- different-colour transverse crossings are smooth on the total V4 cover and `A1` on the cross quotient;
- a representative toric-boundary tangency gives `A1` on the joint cover and `A3` on the cross quotient.

These visible corrections are rational double points / crepant.  A complete global singularity enumeration is still reserved for 29-07; it is no longer a conceptual blocker to the canonical model.

## 7. Exact finite-field V4 identity

At every compatible good odd finite field,

\[
\boxed{
\#X_{joint}
=
\#X_{face}+\#X_{sp}+\#X_{cross}-2\#Y.
}
\]

Equivalently the new joint local contribution beyond the two marginal characters is exactly the cross trace

```text
S_fg=sum chi(f_face*f_sp).
```

This creates the later cohomological receiver

```text
R29-L2=V4CohomologyDecompositionAndCrossQuotientLFunctionAdapter.
```

It should be compared with the Horie--Yamauchi endpoint L-function rather than attacked by a fresh broad local search.

## 8. New reusable Stage29 structures

```text
S29-J01_CANDIDATE=FULL_ENDPOINT_AS_JOINT_V4_COVER
S29-J02_CANDIDATE=CROSS_QUOTIENT_GENERAL_TYPE_SIGNAL
S29-J03_CANDIDATE=ENDPOINT_CANONICAL_TO_MARGINAL_PHYSICAL_DEGREE_ADAPTER
S29-J04_CANDIDATE=EXACT_V4_FINITE_FIELD_POINT_COUNT_DECOMPOSITION
```

These are structural/adaptor weapons, not counting savings.

## 9. Remaining exact receivers

```text
R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger
R29-X1=CrossQuotientCompleteADESingularityAndMinimalModelAudit
R29-L2=V4CohomologyDecompositionAndCrossQuotientLFunctionAdapter
```

The first two are bounded geometry refinements for later 29-07.  `R29-L2` belongs naturally to the 29-02e / 29-09 local-cohomological route.

## 10. Backflow / stop verdict

Nothing found requires reopening Stage16--28.  In fact the new polarization adapter *reuses* Stage28 and the audited Stage27 Saunderson no-go rather than repeating them.

```text
NEW_FOUNDATION_CONFIRMED=true
GLOBAL_ENDPOINT_BIRATIONAL_TO_JOINT_V4=true
CANONICAL_MODEL_ADAPTER_MOSTLY_CLOSED=true
OLD_STAGE_REENTRY_REQUIRED=false
OLD_SAUNDERSON_GATE_REPLAY=false
KEEP_STAGE29_NATIVE=true
FURTHER_BROAD_SEARCH_REQUIRED=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```
