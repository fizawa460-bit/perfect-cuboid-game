# M3-T11-022 — Torus double-lift is a genuine second selector inside the triple-spin principal fiber

CARD_ID: M3-T11-022
CANONICAL_CARD_KEY: M3-T11-022
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-022
現行一覧の状態: PROVED_EXACT_STRUCTURE / NARROWER_RECEIVER
要点: Torus double-lift is a genuine second selector inside the triple-spin principal fiber
主張の抜粋: For a rational norm-one phase U=x+i*y, x^2+y^2=1, one has exactly U in T(Q)^2 iff 2*(1+x) in Q^2. Retain A=X+iY=r_1^2+r_2^2+r_3^2, and assume the triple-spin condition s^2=X^2+Y^2-1. Let
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 23.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 420455
SOURCE_END: 422509
SOURCE_SHA256: 454906fb8d2de54d50fd0acef2d74c5534287a6c4b860f113bbc19a9bc2f853b

CARD_ID: M3-T11-022
TITLE: Torus double-lift is a genuine second selector inside the triple-spin principal fiber
STATUS: PROVED_EXACT_STRUCTURE / NARROWER_RECEIVER
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
For a rational norm-one phase


U=x+i*y,
x^2+y^2=1,


one has exactly


U in T(Q)^2
iff
2*(1+x) in Q^2.


Retain


A=X+iY=r_1^2+r_2^2+r_3^2,


and assume the triple-spin condition


s^2=X^2+Y^2-1.


Let


R_A=X^2+Y^2=1+s^2.


The two solutions of


conj(A)U^2+2U+A=0


are


U_+=(-1+i*s)/conj(A),
U_-=(-1-i*s)/conj(A).


Therefore reconstruction of the all-same Gaussian core requires at least one of


E_+
=
2*(R_A-X-sY)/R_A
in Q^2,


or


E_-
=
2*(R_A-X+sY)/R_A
in Q^2.


The branch product satisfies exactly


E_+*E_-
=
4*(X-1)^2/R_A.


Hence the two branch squareclasses differ by [R_A]^{-1}; if R_A is nonsquare, at most one branch can pass.


The double-lift is not implied by the triple-spin square relation. For the positive rational torus parameters


t_1=1,
t_2=5,
t_3=6,


one has


lambda_12=10/13,
lambda_13=24/37,
lambda_23=960/481,


and


lambda_12*lambda_13*lambda_23=(480/481)^2,


but the two double-lift values are


E_+=746^2/(13*37*409),
E_-=314^2/(13*37*1129),


so neither is a rational square.


This example is an algebraic independence certificate, not a physical endpoint example.


IMPLIES:
The six-bilinear principal-squareclass incidence is an enlarged receiver. Actual endpoint packets lie on an additional independent torus-square cover.


NEW_GATE:
CyclicTripleSpinDoubleLiftPrincipalIncidenceOneTwelfth.


REQUIRED_OUTPUT:
For each fixed Step-A content/coefficient packet, prove


# active tau satisfying both square covers and reconstruction
<<
B^(1/12-delta)


for some fixed delta>0.


DO_NOT_REPEAT:
Do not assume probabilistic independence of the two square selectors.
Do not discard the double-lift as automatic after the triple-spin square.
Do not infer a fixed-power saving merely from the algebraic independence example.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 23.


---
