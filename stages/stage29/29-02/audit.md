# Stage29-02 fresh audit

```text
AUDITED_PR=1286
AUDITED_MATHEMATICAL_SUBMISSION_HEAD=4635653be2d0944a1d5bfa4dfa998db4b5ea3d70
AUDIT_VERDICT=PASS
CHECKPOINT29_02_AUDIT=PASS_AFTER_BOUNDED_FIELD_OF_DEFINITION_REPAIR
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## 1. Scope

This audit covers the Stage29-02 **screening parent** only. It verifies that the parent has genuinely found materially new Stage29-native foundations and exact receivers. It does **not** audit the deeper mathematical claims in stacked child PRs `#1287` / `29-02a` or `#1288` / `29-02b`; those remain independently auditable candidate surfaces until their own fresh audits pass.

## 2. F1 global endpoint model

The four projective quadrics

\[
a^2+b^2=x^2,\quad a^2+c^2=y^2,\quad b^2+c^2=z^2,\quad a^2+b^2+c^2=d^2
\]

are the standard perfect-cuboid endpoint surface in `P^6`. The face-diagonal rewrite in the submission is exact:

\[
2a^2=x^2+y^2-z^2,\quad 2b^2=x^2+z^2-y^2,
\]
\[
2c^2=y^2+z^2-x^2,\quad 2d^2=x^2+y^2+z^2.
\]

The submission correctly treats this as an endpoint model/coordinate foundation rather than an existence or nonexistence theorem.

```text
F1_GLOBAL_ENDPOINT_MODEL_AUDIT=PASS
F1_FACE_DIAGONAL_REWRITE_AUDIT=PASS
F1_EXISTENCE_INFERENCE_FIREWALL=PASS
```

## 3. F2 joint V4 cover and bounded repair

The algebraic core is correct. With the two Stage28 radicands

\[
f=t_1^2+t_2^2,\qquad g=1+t_1^2+t_2^2,
\]

Stage28's geometric squareclass separation implies that the two quadratic extensions are distinct. Hence their compositum has degree four with generic Galois group `(Z/2)^2`, and the forced third quadratic subfield is

\[
K(\sqrt{fg}).
\]

The submission mixed two field layers by writing `K=Qbar(Y)` and then using a rational-lift endpoint criterion. A bounded audit repair has been added at

`stages/stage29/29-02/field-of-definition-adapter.md`.

The corrected statement is:

```text
ARITHMETIC_FIELD=Q(Y)
GEOMETRIC_FIELD=Qbar(Y)
```

The covers and cross quotient descend to `Q`. Since the squareclasses are still distinct after geometric base change, they are distinct over `Q(Y)` as well. For any field `F` of characteristic not two and an `F`-rational base point away from branch/pole loci, an **F-rational** joint lift exists iff both radicands are squares in `F`. Over `Qbar`, geometric lifting is not an arithmetic endpoint criterion.

This repair changes no V4/cross-quotient conclusion.

```text
F2_DEGREE_FOUR_COMPOSITUM_AUDIT=PASS
F2_GENERIC_GALOIS_GROUP_AUDIT=PASS_V4
F2_CROSS_QUADRATIC_SUBFIELD_AUDIT=PASS
F2_FIELD_OF_DEFINITION_AUDIT=PASS_AFTER_REPAIR
F2_RATIONAL_LIFT_QUANTIFIER_AUDIT=PASS_AFTER_REPAIR
```

## 4. Cross branch and canonical firewall

Stage28 gives the two reduced geometric branch profiles `4 x genus0` and `2 x genus1`, each of total class `-2K_Y`. No geometric irreducible component can occur in both supports, because geometric genus is an invariant of the irreducible curve. Therefore the odd branch support of `fg` is their union, with six components and total class `-4K_Y`.

For a normal double-cover package with branch class `2L=-4K_Y`, the formal line bundle is `L=-2K_Y` and the pre-resolution canonical signal is

\[
K_X\sim\pi^*(K_Y+L)=\pi^*(-K_Y).
\]

The submission correctly refuses to infer the minimal-resolution Kodaira type or general type before singularity/resolution analysis.

```text
F2_CROSS_BRANCH_UNION_AUDIT=PASS
F2_CROSS_BRANCH_CLASS_AUDIT=PASS_MINUS_4K_Y
F2_CANONICAL_SIGNAL_AUDIT=PASS_PRE_RESOLUTION_ONLY
F2_GENERAL_TYPE_CLAIM_FIREWALL=PASS
```

## 5. F4 local joint character

Away from branch/zero/pole loci at good odd primes,

\[
1_{\mathrm{both}}=\frac14(1+\chi(f))(1+\chi(g))
=\frac14(1+\chi(f)+\chi(g)+\chi(fg)).
\]

Thus `chi(fg)` is exactly the additional joint character not determined by the two marginal terms alone. The submission correctly forbids converting this local identity into a global Euler-product endpoint count without a same-measure global theorem.

```text
F4_LOCAL_CHARACTER_IDENTITY_AUDIT=PASS
F4_CROSS_CHARACTER_CORRELATION_AUDIT=PASS
F4_GLOBAL_PRODUCT_FIREWALL_AUDIT=PASS
```

## 6. F3/F5/F6 screening status

F3 is a legitimate new **coverage-adapter layer**: it does not assert a new parametrized family, but imposes image-dimension/generic-degree/height/exceptional-locus/coverage bookkeeping before family-specific results can be promoted to endpoint claims.

F5 and F6 are also materially distinct screening lenses. External source rematch confirms:

- Stoll--Testa's cuboid-surface work describes, over `Q(i)`, the quotient of `X(8) x X(8)` by the diagonal kernel `G0 ~= (Z/2)^3`; it also records the `Q`-form via Weil restriction and the geometric split-quadric quotient.
- Horie--Yamauchi `arXiv:2512.22520v3` (24 Mar 2026) computes the L-function of the cuboid surface and gives the degree-two etale-cohomology decomposition into weight-3 modular-form factors plus twisted Tate/Dirichlet-character pieces, together with an explicit Galois-module description of the geometric Picard group.

These are screening-level foundation identifications only; no rational-point conclusion is imported.

```text
F3_COVERAGE_LAYER_AUDIT=PASS
F5_MODULAR_X8_FOUNDATION_AUDIT=PASS_SCREENING_LEVEL
F6_L_FUNCTION_FOUNDATION_AUDIT=PASS_SCREENING_LEVEL
F5_F6_RATIONAL_POINT_INFERENCE_FIREWALL=PASS
```

## 7. Reuse / anti-loop / backflow

The parent correctly reuses Stage28 `S28-W01..W04` only under their firewalls and does not treat the old Stage27/28 open gates as solved. The StructureRadar rematch distinguishes exact receivers and forbids cross-measure promotion.

The new objects are joint/endpoint objects that Stage16--28 deliberately deferred. Therefore `NO_FOUNDATION_BACKFLOW_REQUIRED_CANDIDATE=true` is acceptable at screening level. The formal 29-03 backflow decision should occur only after the already-open materially relevant child routes are independently audited or explicitly deferred.

```text
REUSE_PREFLIGHT_AUDIT=PASS
OLD_GATE_REPLAY_AUDIT=PASS_FALSE
MATERIALLY_NEW_ROUTE_AUDIT=PASS
SCREENING_BACKFLOW_RECOMMENDATION_AUDIT=PASS_NO_IMMEDIATE_BACKFLOW
FORMAL_29_03_DECISION_READY_AFTER_CHILD_AUDITS=true
```

## 8. Child-PR firewall and advancement

The parent is mergeable after this audit. Parent PASS means the screening contract is accepted; it does not promote child-PR theorem claims.

Recommended immediate order after parent merge:

```text
1. retarget/audit 29-02a PR #1287 against main
2. retarget/audit 29-02b PR #1288 against main
3. audit any further suffix only if materially distinct
4. then execute 29-03 foundation-backflow decision
```

Accordingly, `ADVANCE_ALLOWED=true` means Stage29 may advance through the suffix-audit queue; it does not mean the child results are already certified.

```text
CHILD_PR_1287_AUDITED_BY_PARENT=false
CHILD_PR_1288_AUDITED_BY_PARENT=false
CHILD_RESULTS_PROMOTED_BY_PARENT=false
NEXT_ITEM=Stage29-02_SUFFIX_AUDITS_THEN_29-03
NEXT_EXPECTED_COMMAND=Stage29-audit
```

## 9. Final audit state

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02_AUDIT=PASS
BOUNDED_REPAIR=FIELD_OF_DEFINITION_AND_RATIONAL_LIFT_QUANTIFIER
NEW_FOUNDATION_FOUND=true
MATERIALLY_NEW_ROUTE_FOUND=true
STRONGEST_NEW_FOUNDATION=JOINT_V4_COVER_PLUS_CROSS_QUOTIENT
F1_F2_F3_F4_AUDIT=PASS
F5_F6_SCREENING_AUDIT=PASS
OLD_GATE_REPLAY=false
NO_FOUNDATION_BACKFLOW_REQUIRED_CANDIDATE=true
P_FINITE_ZERO_THROUGH_5E8_PRESERVED=true
P_GLOBAL_ZERO_THEOREM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=Stage29-02_SUFFIX_AUDITS_THEN_29-03
NEXT_EXPECTED_COMMAND=Stage29-audit
```