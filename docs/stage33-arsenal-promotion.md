# Stage33 arsenal promotion — provisional harvest

```text
REGISTRY=STAGE33-ARSENAL-PROVISIONAL-R01
STATUS=PROVISIONAL_ACTIVE_STAGE_HARVEST
SOURCE_STAGE=Stage33
SOURCE_PR=1476
SOURCE_BRANCH=stage33-post1475-j2-v4-generator-adapter
SOURCE_HEAD=1ac7767da2add7765a085fcca13d01e38c927ce9
FORMAL_PROMOTION_AUDIT=NOT_YET_RUN
THEOREM_CREDIT=false
```

This file harvests reusable Stage33 mathematics and exact adapters before Stage33 closes. These cards are for candidate discovery and source lookup only until a final promotion audit. Stage33 has had hostile reopenings, so every card states explicitly which part survived and which promotion is forbidden.

## S33-PW01 — exact zero-survival classifier for the locked K3 Brauer 2-block

**Type:** `ARITHMETIC_HS_CLASSIFIER`

Source lock:

```text
path=stages/stage33/33-05/result.md
blob_sha=d72bbaf1d7f3200754e0cf2791f53c94c25ad417
primary_certificate=stage33-05-br2-zero-q-survival-after-j2-nogo.json
primary_canonical_sha256=a48386c523e8c98b1d2b22a7dc3d789e4cea1bfa4557e658fb150e3c6b85a585
hostile_replay_canonical_sha256=4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9
```

For the locked cuboid K3 block,

```text
Br(Kc_bar)[2]^G_Q = span_F2{J2,q1}
dim=2
rank_F2(d2|_<ct>)=2
ker(global d2 on the invariant block)=0
Q_RELEVANT_SURVIVING_DIM=0
```

The useful reusable pattern is: identify the entire finite invariant block, compute obstruction signatures on enough fixed tests to prove full rank, and allow **exact zero survival** as a valid downstream interface rather than forcing an explicit descended representative.

```text
ID=S33-PW01
SAME_KC_SOURCE_LOCK_REQUIRED=true
ZERO_SURVIVAL_IS_VALID_INTERFACE=true
CORRECTED_J2_Q_DEFINED_PREIMAGE=false
DO_NOT_GENERALIZE_TO_OTHER_K3S_WITHOUT_ADAPTER=true
```

## S33-PW02 — two-primary residue module -> invariant-factor reduction

**Type:** `FINITE_MODULE_REDUCTION`

Primary source: `stages/stage33/33-07/result.md` (current reopened unit; only the retained exact prefix below is harvested).

The arithmetic repair was reduced exactly to

```text
FINITE_RAMIFIED_BOUNDARY_MODULE=(Z/2)^49 direct_sum (Z/4)^12
KNOWN_GLOBAL_U44=(Z/2)^44
BOUNDARY_QUOTIENT_AFTER_U44=(Z/2)^23 direct_sum (Z/4)^3
PRESENTATION_INPUT_GENERATORS=29
MINIMAL_INVARIANT_FACTOR_GENERATORS=26
PROPER_GEOMETRIC_BR2_DIMENSION_F2=14
PROPER_GEOMETRIC_BR2_V4_FIXED_DIMENSION_F2=10
FINITE_V4_H1_PROPER_BR2_DIMENSION_F2=16
TWO_PRIMARY_RESIDUE_INVARIANT_BASIS_SHA256=f18a54717b2327f7abc8ee87859b5c0537bffc062a1d5c1e36a5763c46faa939
```

An explicit unimodular Smith decomposition gives mutually inverse integer coordinate maps between the 29 presentation generators and the 26 invariant-factor generators.

Use when a large residue presentation should be compressed to a canonical finite abelian basis before localization/descent calculations.

```text
ID=S33-PW02
EXACT_FINITE_RESIDUE_MODULE_ONLY=true
GLOBAL_Q_LIFT_NOT_IMPLIED=true
ABSOLUTE_H1_NOT_IDENTIFIED_WITH_FINITE_V4_H1=true
UNIT_33_07_REMAINS_REOPENED=true
```

## S33-PW03 — quotient-order2 vs raw-order4 Bockstein adapter

**Type:** `EXTENSION_WARNING_ADAPTER`

Primary source: `stages/stage33/33-07/result.md`.

The quotient `A[2]=(Z/2)^26` cannot be treated as 26 raw squareclass directions. Exact raw-residue analysis gives

```text
QUOTIENT_A2_DIMENSION_F2=26
RAW_ORDER2_FIRST_RESIDUE_FUNCTION_LIFTABLE=17
QUOTIENT_ONLY_ORDER2_WITH_RAW_ORDER4_RESIDUE=9
QUOTIENT_TO_RAW_DOUBLE_OBSTRUCTION_RANK_F2=9
ORDER2_FIRST_RESIDUE_LIFTABILITY_CERTIFICATE_SHA256=85e219932a47322f6283c650e7c39386c0f6a03ab7a47ff93ac9afd0115d0312
```

The nine remaining directions must stay order four until the Bockstein/extension is resolved; forcing them into order-two Kummer squareclasses is invalid.

Use as a general warning/adapter pattern whenever a quotient has exponent two but the raw extension may retain order-four representatives.

```text
ID=S33-PW03
QUOTIENT_ORDER2_DOES_NOT_IMPLY_RAW_ORDER2=true
CHECK_DOUBLE_OBSTRUCTION_BEFORE_SQUARECLASS_MODEL=true
PROJECT_SPECIFIC_NUMBERS_REQUIRE_SOURCE_MATCH=true
```

## S33-PW04 — Picard-adjoint -> proper Brauer source-coordinate adapter

**Type:** `EXACT_SOURCE_ADAPTER`

Current active-source lock:

```text
path=stages/stage33/33-12/j2-picard-adjoint-proper-br2.json
canonical_sha256=066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8
proper14_coordinate=[1,0,0,1,1,0,0,0,0,0,0,0,0,0]
retained10_coordinate=[0,1,1,0,0,0,0,0,0,0]
source_ref=stage33-post1475-j2-v4-generator-adapter@1ac7767da2add7765a085fcca13d01e38c927ce9
```

The exact Picard-adjoint map supplies the corrected J2 coordinate in the proper geometric Brauer module and its retained 10-dimensional invariant basis. This source coordinate is reusable independently of the revoked historical direct order-four pullback route.

```text
ID=S33-PW04
SOURCE_COORDINATE_EXACT=true
TARGET_75D_BINDING_NOT_IMPLIED=true
OLD_C2_PLUS_C3_RELATION_NOT_AUTHORIZED=true
REQUIRES_LOCKED_PICARD_ADJOINT_BASIS=true
```

## S33-PW05 — finite module-extension source/target reachability audit

**Type:** `COMPATIBILITY_AUDIT_METHOD`

Current active-source lock:

```text
path=stages/stage33/33-12/j2-kummer-source-target-module-compatibility-audit.json
canonical_sha256=463aae0d34980bb9f04171430872e59094a8e0f5ee14592e7f8e957393358229
locked_source_reachable_H1_dimension_f2=13
compatible=false
source_ref=stage33-post1475-j2-v4-generator-adapter@1ac7767da2add7765a085fcca13d01e38c927ce9
```

Instead of accepting a source/target relation because the two sides have plausible dimensions or labels, enumerate/test every module extension compatible with the locked source and target group actions, compute the reachable cohomology subspace, and verify that the named target is actually reachable. In the locked J2 case, the source reaches only a 13-dimensional H1 subspace and the named 75D target lies outside it, revoking the old relation.

Use this method before promoting an explicit Kummer/descent source-target identity assembled from independently computed coordinate systems.

```text
ID=S33-PW05
TEST_EXTENSION_COMPATIBILITY_BEFORE_BINDING=true
DIMENSION_MATCH_ALONE_INSUFFICIENT=true
GAUGE_SANITY_REQUIRED=true
CURRENT_J2_BINDING_REPAIR_OPEN=true
```

## S33-PW06 — finite-quotient cohomology is not the absolute arithmetic obstruction

**Type:** `DESCENT_WARNING_RECIPE`

Primary source: `stages/stage33/33-07/result.md`.

When the coefficient action factors through

```text
L=Q(i,sqrt(2)), Gal(L/Q)=V4,
```

inflation--restriction leaves a genuine `G_L` restriction term. The corrected decision order is

```text
Stage A: F2^26 -> ((L*/L*2) tensor_F2 Br(Sbar)[2])^V4
Stage B: ker(Stage A) -> H^1(V4,Br(Sbar)[2]).
```

The finite `V4` H1 receiver alone does not determine the absolute obstruction; genuine geometric lift/squareclass data are required.

```text
ID=S33-PW06
FINITE_QUOTIENT_H1_IS_NOT_ABSOLUTE_H1=true
INFLATION_RESTRICTION_TERM_MUST_BE_CHECKED=true
ABSTRACT_ENDPOINT_MODULES_DO_NOT_DETERMINE_GEOMETRIC_LIFT=true
```

## Promotion firewalls

- These are provisional active-Stage cards and are not formal `selectors`.
- Stage33 hostile reopenings override older successful-looking relations. Only the exact surviving interface stated in a card may be reused.
- `S33-PW01` is a result for the locked K3 block, not a general K3 theorem.
- `S33-PW02/PW03/PW06` explicitly do not promote finite residue/cohomology data to global Q-defined classes.
- `S33-PW04` gives a source coordinate only. `S33-PW05` currently says the old J2 source-target binding is incompatible; it does not supply the replacement binding.
- At Stage33 close, rerun hostile promotion review and activate/revise/retire each card.

```text
PROVISIONAL_WEAPONS=S33-PW01,S33-PW02,S33-PW03,S33-PW04,S33-PW05,S33-PW06
ROUTEABLE_FOR_CANDIDATE_DISCOVERY=true
FORMAL_PROMOTION_ACTIVE=false
PERFECT_CUBOID_CONCLUSION=NONE
```
