# Stage29-02b fresh audit

```text
AUDITED_PR=1288
AUDITED_MATHEMATICAL_SUBMISSION_HEAD=e9aecd9f9a8ffc65f85ddbbe0209979f3cd1258d
AUDIT_VERDICT=PASS_AFTER_BOUNDED_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## Audit scope

Fresh audit covered the dense-open endpoint/joint-cover adapter, the exact `V4` quotient diamond, abelian-cover canonical class, eigensheaf invariants, canonical `P^6` model, endpoint/marginal degree adapter, Saunderson rematch, local ADE preflight, and finite-field `V4` point-count identity.

The Testa--Stoll low-degree theorem used by the degree argument was independently audited in Stage29-02a / PR #1287 immediately before this audit.

## Bounded audit repairs

Two local corrections were required; neither changes the core V4 conclusions.

### 1. Arithmetic / geometric field separation

The child inherited the pre-repair parent convention in which `Q(Y)` and `Qbar(Y)` were not always separated. `function-field-adapter.md` now fixes

```text
ARITHMETIC_FIELD=Q(Y)
GEOMETRIC_FIELD=Qbar(Y)
```

The covers descend to `Q`. Geometric branch and divisor calculations may be made after base change to `Qbar`; rational endpoint semantics require an `F`-rational lift over the arithmetic field. The two squareclasses are geometrically distinct, hence also distinct over `Q(Y)`, so the arithmetic joint extension has generic degree four.

### 2. Weak-del-Pezzo vanishing

`invariant-decomposition.md` called the Stage28 base an ordinary degree-4 del Pezzo and invoked Kodaira vanishing with `-2K_Y` ample. The same branch correctly treats anticanonical-degree-zero boundary curves, so the precise object is the rational degree-4 **weak del Pezzo** with `-K_Y` nef and big.

The needed vanishing remains true: by Serre duality `H^1(2K_Y)` is dual to `H^1(-K_Y)`, and Kawamata--Viehweg applies to

```text
-K_Y = K_Y + (-2K_Y)
```

because `-2K_Y` is nef and big in characteristic zero. Hence the computed `q=0` conclusions are unchanged.

## Exact function-field / quotient audit

On the labeled dense two-face chart,

```text
f_face=t1^2+t2^2
f_sp=1+t1^2+t2^2
K_endpoint=Q(Y)(sqrt(f_face),sqrt(f_sp))
```

and the two quadratic squareclasses are independent. Therefore

```text
[K_endpoint:Q(Y)]=4
GENERIC_GROUP=(Z/2)^2
```

with exactly the three quadratic quotients

```text
X_face  : sqrt(f_face)
X_sp    : sqrt(f_sp)
X_cross : sqrt(f_face*f_sp).
```

This is a genuine Stage29 joint object and not a replay of the Stage28 marginal comparison.

```text
ENDPOINT_FUNCTION_FIELD_ADAPTER_AUDIT=PASS
V4_QUOTIENT_DIAMOND_AUDIT=PASS
CROSS_QUOTIENT_AUDIT=PASS
ALGEBRAIC_COVER_DEGREE_IS_PHYSICAL_MULTIPLICITY=false
```

## Canonical class / invariant audit

Using the audited Stage28 divisor classes

```text
D_face ~ -2K_Y
D_sp   ~ -2K_Y
(-K_Y)^2=4,
```

Pardini/Hurwitz gives on the normal joint cover

```text
K_joint ~ pi_joint^*(-K_Y)
K_joint^2=16.
```

The exact eigensheaf algebra is

```text
pi_*O_joint = O_Y + O_Y(K_Y) + O_Y(K_Y) + O_Y(2K_Y),
```

which yields

```text
pg_joint=7
q_joint=0
chi_joint=8.
```

This matches the independently known full cuboid-surface package `K^2=16, pg=7, q=0`.

For the cross double cover,

```text
D_cross ~ -4K_Y
K_cross ~ pi_cross^*(-K_Y)
formal K_cross^2=8
pg_cross=5
q_cross=0
```

on the normal-cover level. Promotion of the same `K^2=8, pg=5, q=0` package to the minimal resolution remains conditional on the complete global canonical/ADE singularity audit.

```text
JOINT_CANONICAL_CLASS_AUDIT=PASS
JOINT_K2_PG_Q_AUDIT=PASS
CROSS_NORMAL_COVER_INVARIANT_AUDIT=PASS
CROSS_MINIMAL_GENERAL_TYPE_AUDITED=false
```

## Canonical projective model / degree adapter audit

The five anticanonical base sections `[e:x:y:p:q]` plus the two square-root eigensections `[z:d]` give seven canonical sections satisfying exactly the four cuboid quadrics in `P^6`. Together with the function-field equality this identifies the canonical image with the full cuboid endpoint model; the exact exceptional-curve/contraction ledger remains `R29-G1b`.

On the normal/canonical joint model,

```text
K_joint = q_sp^* M_face = q_face^* M_sp
```

as line-bundle classes. Therefore for any integral noncontracted curve mapping generically with degree `delta`, projection formula gives

```text
K_joint.C = delta * M_marginal.C_marginal.
```

This is an exact degree adapter, not a rational-point count.

The audited Stage20 Saunderson curve has `M_face.C=6`. A generically split degree-one endpoint lift would therefore yield a degree-six endpoint curve, forbidden by the freshly audited Testa--Stoll theorem. The lift is thus nonsplit; the connected degree-two lift has canonical degree `12`. This nonsplitting is **not new**: Stage27-r9 already proves the explicit smooth genus-3 hyperelliptic restricted cover. Stage29-02b contributes the global degree explanation and general adapter.

```text
CANONICAL_P6_MODEL_AUDIT=PASS_WITH_BOUNDARY_LEDGER_RETAINED
CANONICAL_TO_MARGINAL_DEGREE_ADAPTER_AUDIT=PASS
SAUNDERSON_NONSPLIT_AUDIT=PASS_REUSED_STAGE27
SAUNDERSON_ENDPOINT_CANONICAL_DEGREE_AUDIT=PASS_12
STAGE19_M6_TRIVIAL_ENDPOINT_LIFT_FORBIDDEN_AUDIT=PASS
COUNTING_EXPONENT_FROM_CANONICAL_DEGREE=false
```

## Local singularity preflight audit

The submitted local calculations were independently checked on the exact Stage28 branch factors:

- the four face same-colour intersections `(±1,±1)` are transverse;
- representative non-boundary space-component intersections are transverse;
- different-colour transverse crossings give local joint equations `u^2=r, v^2=s`, hence are smooth on the total V4 cover and `A1` on the cross quotient;
- at the representative blown-up boundary corner the strict transforms have contact order two; the joint quadratic leading form is nondegenerate (`A1`) and the cross double cover is analytically `A3`.

These representative corrections are ADE/crepant. The audit does **not** upgrade this to a complete global singularity inventory.

```text
REPRESENTATIVE_ADE_PREFLIGHT_AUDIT=PASS
FULL_GLOBAL_SINGULARITY_ENUMERATION_COMPLETE=false
```

## Finite-field V4 identity audit

For compatible good odd finite-field cover models, the fiber identity

```text
(1+chi(f))(1+chi(g))
 = 1+chi(f)+chi(g)+chi(fg)
```

holds also at branch points with `chi(0)=0`. Summing gives

```text
#X_joint=#X_face+#X_sp+#X_cross-2#Y.
```

Thus the cross trace is exactly the additional joint character contribution beyond the two marginals. No Euler product or global physical rational-point count follows from this identity.

```text
FINITE_FIELD_V4_IDENTITY_AUDIT=PASS
CROSS_TRACE_JOINT_TERM_AUDIT=PASS
GLOBAL_COUNT_FROM_LOCAL_TRACE=false
```

## Remaining receivers / verdict

```text
R29-G1b=JointCoverBoundaryContractionAndExceptionalCurveLedger
R29-X1=CrossQuotientCompleteADESingularityAndMinimalModelAudit
R29-L2=V4CohomologyDecompositionAndCrossQuotientLFunctionAdapter
```

These are genuinely narrower follow-ups. Nothing in the audit requires reopening Stage16--28.

```text
CHECKPOINT29_02B_AUDIT=PASS
NEW_FOUNDATION_CONFIRMED=true
OLD_STAGE_REENTRY_REQUIRED=false
OLD_SAUNDERSON_GATE_REPLAY=false
KEEP_STAGE29_NATIVE=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
PARENT_PR_AUDIT_INHERITED=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```
