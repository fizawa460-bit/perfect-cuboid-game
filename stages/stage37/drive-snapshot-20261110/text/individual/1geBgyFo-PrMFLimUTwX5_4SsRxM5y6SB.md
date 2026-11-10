# M3-ETA-002 — Stage15-6ao degree-four adapter

CARD_ID: M3-ETA-002
CANONICAL_CARD_KEY: M3-ETA-002
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-ETA-002
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: Fix nonzero delta, positive squarefree eta, and one Gaussian orientation K=A+iB with Norm(K)=eta. The equation f^4+delta^2 e^4=eta r^2 reduces, after primitive Gaussian factorizati
主張の抜粋: Fix nonzero delta, positive squarefree eta, and one Gaussian orientation K=A+iB with Norm(K)=eta. The equation f^4+delta^2 e^4=eta r^2 reduces, after primitive Gaussian factorization, to a smooth degree-4 genus-one intersection of two quadrics: A(u^2-v^2)-2Buv-f^2=0, B(u^2-v^2)+2Auv-delta e^2=0. On a dyadic block r~R, 
対象・測度: fixed-(delta,eta,Gaussian orientation) endpoint packets.
依存関係: M3-ETA-001 and primitive Gaussian factorization.
再開条件の抜粋: a summation theorem over the moving base and allowed delta/eta supports.
旧詳細位置: LEGACY-COLD route-audit Section33.5.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 377044
SOURCE_END: 378497
SOURCE_SHA256: 93263db422e4c64bc9c669b3b20705d88f8dba20d26cba5f438bd13136e34054

## M3-ETA-002
TYPE: THEOREM
STATUS: PROVED_EXACT


CLAIM:
Fix nonzero delta, positive squarefree eta, and one Gaussian orientation
K=A+iB with Norm(K)=eta.
The equation
f^4+delta^2 e^4=eta r^2
reduces, after primitive Gaussian factorization, to a smooth degree-4 genus-one intersection of two quadrics:
A(u^2-v^2)-2Buv-f^2=0,
B(u^2-v^2)+2Auv-delta e^2=0.
On a dyadic block r~R, its projective height satisfies
H << eta^(1/4)*R^(1/2).
Applying the uniform degree-four projective-curve bound retained from the Stage15-6ao method gives
N_{delta,eta}(R)
<<_epsilon
B^epsilon * eta^(1/8) * R^(1/4),
with theorem constant depending only on epsilon and degree 4, not on delta or eta.


POPULATION:
fixed-(delta,eta,Gaussian orientation) endpoint packets.


HEIGHT:
dyadic r-height with the stated projective-height adapter.


DEPENDS_ON:
M3-ETA-001 and primitive Gaussian factorization.


IMPLIES:
each fixed second-core packet has a quantitative degree-four genus-one upper bound.


ALIASES:
Stage15-6ao degree-four adapter;
fixed delta-eta quartic count;
second-core degree-four bound.


DUPLICATE_OF:
none.


SUPERSEDES:
purely qualitative finiteness on a fixed eta packet.


DO_NOT_REPEAT:
This fixed-packet estimate does not sum the moving Pythagorean bases and gives no standalone global P/M3 theorem.


REOPEN_CONDITION:
a summation theorem over the moving base and allowed delta/eta supports.


DETAIL_DOC:
LEGACY-COLD route-audit Section33.5.


---
