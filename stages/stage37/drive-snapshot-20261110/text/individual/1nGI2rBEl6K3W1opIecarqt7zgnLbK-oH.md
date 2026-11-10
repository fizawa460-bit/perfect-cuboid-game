# M3-T11-016 — Fixed-two relative-core triple-spin fiber is subpolynomial

CARD_ID: M3-T11-016
CANONICAL_CARD_KEY: M3-T11-016
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-016
現行一覧の状態: PROVED_EXACT / FIBER_ANTICONCENTRATION
要点: Fixed-two relative-core triple-spin fiber is subpolynomial
主張の抜粋: Parameterize the norm-one torus by r(t)=(1-t^2+2*i*t)/(1+t^2). For fixed r_1=r(a), r_2=r(b), the moving pairwise trace is lambda_a(t) = 2*Q_a(t)/[(1+a^2)(1+t^2)], Q_a(t) = (1-a^2)(1-t^2)+4*a*t. The exact resultant is Res_t(Q_a,Q_b) = -16*(a-b)^2*(a*b+1)^2. Thus branch degeneration occurs exactly for r_2=+/-r_1. Both degenerate cases are physically empty: - r_2=-r_1 contradicts positivity of the corresponding normalized physical legs; - r_2=r_1 forces, through the triple-spin square relation, lambda_13=0, then the endpoint sphere forces the first two normalized legs to vanish. Hence every positive physical endpoint gives a smooth quartic Y^2=d_{a,b} Q_a(t)Q_b(t) with four distinct rational projective branch points and full rational 2-torsion on the Jacobian. Using the same uniform bounded-height rational-torsion theorem as Stage14-t22/t36/t37, #{G_3 for fixed packet,G_1,G_2 satisfying the triple-spin condition} <= B^o(1). The torus-double-lift and physical reconstruction are post-filters, so the bound remains valid for actual endpoint-compatible G_3.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 18.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 381548
SOURCE_END: 383324
SOURCE_SHA256: ccb702fac9b2ba9cad65b8254ddbc02490d8a212389a5b1ed67045967e806d04

CARD_ID: M3-T11-016
TITLE: Fixed-two relative-core triple-spin fiber is subpolynomial
STATUS: PROVED_EXACT / FIBER_ANTICONCENTRATION
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
Parameterize the norm-one torus by


r(t)=(1-t^2+2*i*t)/(1+t^2).


For fixed r_1=r(a), r_2=r(b), the moving pairwise trace is


lambda_a(t)
=
2*Q_a(t)/[(1+a^2)(1+t^2)],


Q_a(t)
=
(1-a^2)(1-t^2)+4*a*t.


The exact resultant is


Res_t(Q_a,Q_b)
=
-16*(a-b)^2*(a*b+1)^2.


Thus branch degeneration occurs exactly for r_2=+/-r_1.


Both degenerate cases are physically empty:
- r_2=-r_1 contradicts positivity of the corresponding normalized physical legs;
- r_2=r_1 forces, through the triple-spin square relation, lambda_13=0, then the endpoint sphere forces the first two normalized legs to vanish.


Hence every positive physical endpoint gives a smooth quartic


Y^2=d_{a,b} Q_a(t)Q_b(t)


with four distinct rational projective branch points and full rational 2-torsion on the Jacobian.


Using the same uniform bounded-height rational-torsion theorem as Stage14-t22/t36/t37,


#{G_3 for fixed packet,G_1,G_2 satisfying the triple-spin condition}
<=
B^o(1).


The torus-double-lift and physical reconstruction are post-filters, so the bound remains valid for actual endpoint-compatible G_3.


IMPLIES:
The Section-17 fixed-content-triple problem reduces from three moving relative cores to an active ordered-pair count.


NEW_GATE:
CyclicRelativeCorePairIncidenceOneTwelfth.


DO_NOT_REPEAT:
Do not treat the resultant-degenerate pairs as a large exceptional family; they are empty on the positive physical endpoint locus.
Do not claim this fixed-two B^o(1) result alone closes the B^(1/12) fixed-content receiver.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 18.


---
