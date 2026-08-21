# Stage29-02a fresh audit

```text
AUDITED_PR=1287
AUDITED_MATHEMATICAL_SUBMISSION_HEAD=82595de724e6f1d8e980b9190945cedd454e700b
AUDIT_VERDICT=PASS
REPAIR_CLASS=MECHANICAL_SOURCE_LOCATOR_COMPLETION
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

## Audit scope

Fresh audit covered the full-endpoint Testa--Stoll import, the positive-physical-chamber low-degree filter, the Euler-K3 bridge candidate, the genus-5 / elliptic-fibration locks, the reuse firewalls, and the route contract.

## Primary source verification

Primary source: Damiano Testa and Michael Stoll, `Curves on the surface of cuboids`, *Mathematics of Computation*, DOI `10.1090/mcom/4238`, arXiv `1009.0388`; current author PDF `Cuboidi.pdf`.

Independently checked against the current source:

```text
ENDPOINT_COMPLETE_INTERSECTION_2_2_2_2_AUDIT=PASS
SINGULARITIES_48_A1_AUDIT=PASS
CANONICAL_MODEL_GENERAL_TYPE_K2_16_AUDIT=PASS
GEOMETRIC_PICARD_RANK_64_AUDIT=PASS
AUTOMORPHISM_GROUP_ORDER_1536_AUDIT=PASS
LOW_DEGREE_CLASSIFICATION_THROUGH_6_AUDIT=PASS
NO_INTEGRAL_DEGREE6_CURVE_AUDIT=PASS
FULL_SURFACE_28_GENUS5_FIBRATIONS_AUDIT=PASS
EULER_K3_QUOTIENT_AUDIT=PASS
EULER_K3_15_ELLIPTIC_FIBRATIONS_AUDIT=PASS
```

The exact locators are now completed in `stages/stage29/29-02a/source-lock.md`.

## Positive physical chamber audit

Testa--Stoll Corollary 18 identifies all integral curves with canonical degree at most six with the explicit set `G`. Each component class fails the positive nondegenerate rational-box chamber for an elementary reason: zero side/diagonal, imaginary relation, or the equal-side `sqrt(2)` obstruction; exceptional curves lie over the singular/degenerate locus.

Accepted consequence:

```text
POSITIVE_NONDEGENERATE_ENDPOINT_CURVE_DEGREE_LE_6=ABSENT
FIRST_POSSIBLE_CANONICAL_CURVE_DEGREE_FOR_PHYSICAL_FAMILY>=8
```

This is strictly a **curve-family carrier** statement. It does not exclude isolated rational points, higher-degree curves, or perfect cuboids globally.

## K3 / fibration audit

The published `K_c` quotient is indeed obtained by forgetting the long diagonal sign and is explicitly an Euler-brick K3 after minimal desingularization. The paper supplies 15 elliptic fibrations there. Stage20's `X_face` describes the same Euler-brick moduli on a dense physical open, but the repo has not yet written the global birational/polarization/height adapter.

Therefore the following receiver is correctly retained rather than silently identifying degrees:

```text
R29-K1=Stage20ToricK3ToTestaStollEulerK3BirationalPolarizationAdapter
```

The full endpoint's 28 genus-5 fibrations and the Euler K3's 15 elliptic fibrations are valid structural inputs, but no counting exponent or uniform-rank theorem follows automatically.

## Firewalls

```text
GENERAL_TYPE_IMPLIES_FINITE_RATIONAL_POINTS=false
NO_DEGREE6_CURVE_IMPLIES_NO_PERFECT_CUBOID=false
ENDPOINT_CANONICAL_DEGREE_EQUALS_STAGE20_M_FACE_DEGREE=false
TESTA_STOLL_KC_EQUALS_STAGE20_XFACE_GLOBALLY_WITHOUT_ADAPTER=false
FIBRATION_IMPLIES_COUNTING_EXPONENT=false
OLD_GATE_REPLAY=false
OLD_STAGE_REENTRY_REQUIRED=false
KEEP_STAGE29_NATIVE=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Audit verdict

The mathematical submission is accepted. The only audit repair was completing the referenced source-lock with the Section 5/6 fibration and K3 locators; no mathematical claim was weakened or changed.

```text
CHECKPOINT29_02A_AUDIT=PASS
SOURCE_LOCK_AUDIT=PASS
PHYSICAL_CHAMBER_FILTER_AUDIT=PASS
EULER_K3_BRIDGE_AUDIT=PASS_WITH_R29_K1_RETAINED
FIBRATION_LOCK_AUDIT=PASS
NEW_TO_REPO_WEAPON_CANDIDATE=true
NEW_TO_MATHEMATICS=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
PARENT_PR_AUDIT_INHERITED=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```
