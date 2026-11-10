# M3-T11-017 — Fixed-content endpoint count is active-tau count at power scale

CARD_ID: M3-T11-017
CANONICAL_CARD_KEY: M3-T11-017
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-017
現行一覧の状態: PROVED_EXACT / RECEIVER_SIMPLIFICATION
要点: Fixed-content endpoint count is active-tau count at power scale
主張の抜粋: Fix a labeled content triple (h_1,h_2,h_3) and tau. Then
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 19.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 383324
SOURCE_END: 384803
SOURCE_SHA256: 5ea7551f32fcf6eab8f52579c71f7193a47a700cb7fb8a016c0f2bdaeb3422d2

CARD_ID: M3-T11-017
TITLE: Fixed-content endpoint count is active-tau count at power scale
STATUS: PROVED_EXACT / RECEIVER_SIMPLIFICATION
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
Fix a labeled content triple (h_1,h_2,h_3) and tau.


Then


D_1=tau*h_2*h_3,
D_2=tau*h_1*h_3,
D_3=tau*h_1*h_2


are fixed primitive Pythagorean hypotenuses.


For each fixed D_i the number of primitive oriented Pythagorean directions is D_i^o(1). Therefore the total number of exact endpoint candidates above fixed (h_1,h_2,h_3,tau) is B^o(1); all cyclic, sphere, triple-spin and reconstruction conditions only reduce this set.


Hence for fixed content triple,


endpoint count
<=
B^o(1) * active-tau count,


and the two counts have the same power exponent.


Combined with the Section-17 outer budget


#content triples
<=
B^(1/4+(3/2)xi+o(1)),


it is sufficient to prove uniformly


A_tau(B;h_1,h_2,h_3)
<<
B^(1/12-delta)


for some fixed delta>0, with xi small enough.


NEW_GATE:
CyclicFixedContentActiveTauOneTwelfth.


The triple-spin and torus-double-lift structures from M3-T11-015/016 are retained as arithmetic selectors for which tau are active.


DO_NOT_REPEAT:
Do not demand B^o(1) multiplicity for a moving tau family; fixed tau is already B^o(1).
Do not count all split-prime-supported tau as active.
Do not discard the triple-spin structure merely because the minimal counting object is now tau.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 19.


---
