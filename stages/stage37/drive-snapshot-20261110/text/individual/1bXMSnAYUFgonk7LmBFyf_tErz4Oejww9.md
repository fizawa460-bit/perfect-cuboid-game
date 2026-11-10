# M3-T11-013 — Cross-gcd cycle amplifies the residual tau threshold

CARD_ID: M3-T11-013
CANONICAL_CARD_KEY: M3-T11-013
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-013
現行一覧の状態: EXACT_CONDITIONAL_REDUCTION / PRIMARY_ROUTE_PROGRESS
要点: Cross-gcd cycle amplifies the residual tau threshold
主張の抜粋: On every cyclic endpoint, c1*c2*c3=(R/tau)^2. If max_i c_i<=C, then tau>=R/C^(3/2). On the retained large-R branch R>B^(2/3-eta), taking C=B^(1/6+xi) gives tau>B^(5/12-eta-(3/2)xi). Therefore, once the existing same-measure raw-edge cross-gcd tail controls endpoints with some c_i>B^(1/6+xi), the complementary cyclic endpoint family is forced into the much stronger residual regime tau>B^(5/12-o(1)).
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 15.3-15.4.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 264893
SOURCE_END: 266063
SOURCE_SHA256: bbd49e9ab45e280fac919b62d1d58a9bea2dbf0cb81b02211d5c26be4d125ff5

CARD_ID: M3-T11-013
TITLE: Cross-gcd cycle amplifies the residual tau threshold
STATUS: EXACT_CONDITIONAL_REDUCTION / PRIMARY_ROUTE_PROGRESS
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
On every cyclic endpoint,


c1*c2*c3=(R/tau)^2.


If


max_i c_i<=C,


then


tau>=R/C^(3/2).


On the retained large-R branch


R>B^(2/3-eta),


taking


C=B^(1/6+xi)


gives


tau>B^(5/12-eta-(3/2)xi).


Therefore, once the existing same-measure raw-edge cross-gcd tail controls endpoints with some c_i>B^(1/6+xi), the complementary cyclic endpoint family is forced into the much stronger residual regime


tau>B^(5/12-o(1)).


IMPLIES:
The original B^(1/6-o(1)) four-factor pigeonhole threshold is not the final residual threshold after the cross-gcd cycle is used.


COUPLED_GATE:
Step A = Stage14CrossGcdStratifiedRawEdgeTail.
Step B = CyclicHugeResidualTauAfterCrossGcdTail.


CREDIT:
Exact exponent amplification only.
Neither Step A nor Step B is closed by this card.


DO_NOT_REPEAT:
Do not treat the h_i/c_i appearances as independent; this result uses only the exact product identity.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 15.3-15.4.


---
