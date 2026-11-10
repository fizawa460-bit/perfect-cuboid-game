# M3-T11-018 — Triple-spin active-tau selector is an exact six-bilinear square cover

CARD_ID: M3-T11-018
CANONICAL_CARD_KEY: M3-T11-018
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-018
現行一覧の状態: PROVED_EXACT / POLYNOMIAL_NORMAL_FORM
要点: Triple-spin active-tau selector is an exact six-bilinear square cover
主張の抜粋: For the rational norm-one torus parameters r_i=(1-t_i^2+2*i*t_i)/(1+t_i^2), the pairwise traces satisfy lambda_ij = 2*Q_ij/[(1+t_i^2)(1+t_j^2)], with Q_ij = (1-t_i^2)(1-t_j^2)+4*t_i*t_j = (1+t_i-t_j+t_i*t_j) (1-t_i+t_j+t_i*t_j). Therefore lambda_12*lambda_13*lambda_23 in Q^2 is exactly equivalent to W^2 = 2* prod_{i<j} (1+t_i-t_j+t_i*t_j) (1-t_i+t_j+t_i*t_j). Thus the active-tau triple-spin selector is a six-bilinear square-value cover. If any one of the six factors vanishes, then lambda_ij=0 for some pair, equivalently r_j=+/-i*r_i. The corresponding two normalized physical legs already have squared sum 1, so the endpoint sphere forces the third leg to be zero. Hence all six zero-factor branches are empty on the positive physical endpoint locus.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 20.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 384803
SOURCE_END: 386200
SOURCE_SHA256: 9a26e0d6a5b90d3a1ecb11f5f9dc7a06f3d5e679f44bee340017c5e35d434797

CARD_ID: M3-T11-018
TITLE: Triple-spin active-tau selector is an exact six-bilinear square cover
STATUS: PROVED_EXACT / POLYNOMIAL_NORMAL_FORM
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
For the rational norm-one torus parameters


r_i=(1-t_i^2+2*i*t_i)/(1+t_i^2),


the pairwise traces satisfy


lambda_ij
=
2*Q_ij/[(1+t_i^2)(1+t_j^2)],


with


Q_ij
=
(1-t_i^2)(1-t_j^2)+4*t_i*t_j
=
(1+t_i-t_j+t_i*t_j)
(1-t_i+t_j+t_i*t_j).


Therefore


lambda_12*lambda_13*lambda_23 in Q^2


is exactly equivalent to


W^2
=
2*
prod_{i<j}
(1+t_i-t_j+t_i*t_j)
(1-t_i+t_j+t_i*t_j).


Thus the active-tau triple-spin selector is a six-bilinear square-value cover.


If any one of the six factors vanishes, then lambda_ij=0 for some pair, equivalently r_j=+/-i*r_i. The corresponding two normalized physical legs already have squared sum 1, so the endpoint sphere forces the third leg to be zero. Hence all six zero-factor branches are empty on the positive physical endpoint locus.


IMPLIES:
There is now an explicit nondegenerate three-variable polynomial square selector for testing FI/Hecke/tH dispersion on the fixed-content active-tau gate.


DO_NOT_REPEAT:
Do not count a zero-factor branch as an exceptional physical family.
Do not apply ambient square-sieve density without an exact active-tau height/multiplicity adapter.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 20.


---
