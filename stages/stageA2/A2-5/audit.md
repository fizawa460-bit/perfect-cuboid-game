# StageA2 independent audit — A2-5

```text
AUDIT_VERDICT=PASS_WITH_CONTROLLER_HISTORY_REPAIR
AUDITED_TASK=STAGEA2-A2-5-R01
AUDITED_SUBMISSION_HEAD=0565532d19e7e436b180b7286c1365326d3bec4b
BASE_MAIN_AUDIT=PASS
BASE_MAIN=9a3d32598acc8f288fb562254da84d5f59eda9e8
BASE_MAIN_IS_A2_4_MERGE=PASS
SOURCE_MINUS18_FIREWALL_AUDIT=PASS
CPLUS_BIRATIONAL_QUARTIC_AUDIT=PASS
CMINUS_BIRATIONAL_QUARTIC_AUDIT=PASS
QUARTIC_SMOOTHNESS_AUDIT=PASS
COMMON_BINARY_QUARTIC_INVARIANTS_AUDIT=PASS_I481_J9758
COMMON_JACOBIAN_AUDIT=PASS
EXPLICIT_15_A5_ISOMORPHISM_AUDIT=PASS
LMFDB_15_A5_RANK_AUDIT=PASS_RANK0
LMFDB_15_A5_TORSION_AUDIT=PASS_Z2_x_Z4
LMFDB_15_A5_POINT_COUNT_AUDIT=PASS_8
LPS_SHORT_MODEL_AUDIT=PASS
LPS_EIGHT_POINT_LIST_AUDIT=PASS
LPS_GROUP_NOTATION_USED_FOR_STRUCTURE=false
QPLUS_EIGHT_POINTS_AUDIT=PASS_COMPLETE
QMINUS_EIGHT_POINTS_AUDIT=PASS_COMPLETE
QPLUS_IMAGE_AUDIT=PASS_t_MINUS1_OR_INFINITY
QMINUS_IMAGE_AUDIT=PASS_t_1_OR_MINUS1_OVER2
E18_INFINITY_AND_K1_WALL_AUDIT=PASS
COMPLETE_E18_NONDEGENERATE_RATIONAL_POINT_CLOSURE=true
PUBLISHED_EQUATION6_ANCHOR_NONDEGENERATE_POINTS=0
FAMILY_SPECIFIC_EXCLUSION_COMPLETE=true
GENERAL_COVERAGE_PROVED=false
ARBITRARY_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
PERFECT_CUBOID_FOUND=false
A1_MINUS8_IMPORT_FIREWALL_AUDIT=PASS
CONTROLLER_HISTORY_PRESERVATION_AUDIT=FAIL_THEN_REPAIRED
EXACT_HEAD_STAGEA2_CI=NOT_CONFIGURED
AUDIT_REPAIR_PERFORMED=true
REPAIR=restore previously audited A2-3/A2-4 controller ledger fields while retaining A2-5 closure state
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
NEXT_TARGET=A2_CLOSE_PUBLISHED_MINUS18_FAMILY_EXCLUSION
NEXT_EXPECTED_COMMAND=StageA2-main-batch
```

## Independent algebra audit

The two submitted parameterizations were recomputed symbolically.

For `Cplus`,

`R=1+m(t+1)`

gives the second intersection

`t=-(m^2+2m+6)/(m^2-1)`,

`R=-(m^2+7m+1)/(m^2-1)`,

and substitution into `S^2=t^2-t-1` gives exactly

`y^2=m^4+6m^3+23m^2+22m+29`

with `S=y/(m^2-1)`.

For `Cminus`, the line `R=3+m(t-1)` gives exactly

`t=(m^2-6m+4)/(m^2+1)`,

`R=-3(m^2-m-1)/(m^2+1)`,

and

`y^2=m^4+6m^3-37m^2+42m-11`

with `S=y/(m^2+1)`.

Both quartic polynomial discriminants are exactly `12960000`, so both genus-one models are smooth.

Using the classical binary-quartic invariants

`I=12ae-3bd+c^2`,

`J=72ace+9bcd-27ad^2-27b^2e-2c^3`,

both quartics give

`I=481`, `J=9758`.

Therefore both have Jacobian

`E: Y^2=X^3-12987X-263466=(X+102)(X+21)(X-123)`.

## Exact external Mordell-Weil audit

LMFDB label `15.a5` records the minimal model

`y^2+xy+y=x^3+x^2-10x-10`,

Mordell-Weil rank `0`, and torsion `Z/2Z x Z/4Z`, hence exactly eight rational points.

The submitted c-invariant scaling is correct. The audit also gives an explicit rational isomorphism, removing any same-j ambiguity. If `(x,y)` is on the LMFDB minimal model, set

`X=36x+15`,

`Y=108(2y+x+1)`.

Then exactly

`Y^2=X^3-12987X-263466`.

The inverse is rational, so the short model is genuinely `Q`-isomorphic to `15.a5`.

Leprévost–Pohst–Schöpp, Acta Arith. 127 (2007), proof of Theorem 2.5, uses this same short model and lists the eight rational points explicitly. The paper text/OCR renders the group notation as `Z/8Z`, but the displayed curve has the three nonzero rational 2-torsion points `(-21,0)`, `(-102,0)`, `(123,0)`, and current LMFDB gives `Z/2Z x Z/4Z`. The audit therefore uses the paper only for the identical short model and complete eight-point list, and uses LMFDB for the group structure. This source-notation discrepancy does not affect the cardinality-eight closure.

## Cover point-set audit

`Qplus` contains the six finite points

`m=-7/2, y=+/-45/4`,

`m=1, y=+/-9`,

`m=-1, y=+/-5`,

plus its two rational quartic points at infinity. Since `Qplus(Q)` is a torsor with a rational point under an eight-element Jacobian, these eight points are the complete rational point set.

The finite ordinary chart sends `m=-7/2` to `t=-1,R=1`; the quartic infinities limit to `t=-1,R=-1`; and `m=+/-1` are the four projective `t=infinity` points. Hence `Cplus(Q)` has only `t=-1` and `t=infinity`.

Likewise `Qminus` contains exactly

`m=1/2, y=+/-5/4`,

`m=1, y=+/-1`,

`m=3, y=+/-5`,

and the two quartic infinities. Their images give only `t=1` and `t=-1/2` on `Cminus`.

The audited A2-4 map

`z=(2t^2-8t-6)/(t^2-1)`

has poles at `t=+/-1`, while `t=infinity` and `t=-1/2` both map to `z=2`. Thus every rational point on the two covers lands either at an `E18` projective infinity or at `z=2 -> k=1 -> c^2=d^2`, the already excluded source wall.

Therefore the published equation-(6) `-18` anchor boundary has no nondegenerate rational point. This closes only that published family boundary. Equation (6) is not proved universal, so no conclusion about existence or nonexistence of arbitrary perfect cuboids follows.

## Controller repair

The submitted A2-5 controller update removed several already-audited ledger fields from the A2-3 and A2-4 receiver records. This does not affect the A2-5 mathematics, but it violates the stage's history-preservation convention. The audit restores those fields while appending the A2-5 audited closure state.

No StageA2-specific GitHub Actions workflow run exists on the exact submitted head, so CI is recorded as not configured rather than inferred from unrelated workflows.
