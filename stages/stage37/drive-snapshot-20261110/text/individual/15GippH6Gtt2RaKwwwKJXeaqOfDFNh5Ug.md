# M3-T11-038 — For the scaled symmetric parameter w=u/S=P/(S*E+P) use the unreduced integer pair N_w=T_3*D, D_w=T_1*T_2+T_3*D. Let C_w be the collision content from M3-T11-037: C_w=product_i gcd(

CARD_ID: M3-T11-038
CANONICAL_CARD_KEY: M3-T11-038
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-038
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE / SAME_MEASURE_RECEIVER / PROJECTIVE_GCD_ROUTER
要点: For the scaled symmetric parameter w=u/S=P/(S*E+P) use the unreduced integer pair N_w=T_3*D, D_w=T_1*T_2+T_3*D. Let C_w be the collision content from M3-T11-037: C_w=product_i gcd(
主張の抜粋: For the scaled symmetric parameter w=u/S=P/(S*E+P) use the unreduced integer pair N_w=T_3*D, D_w=T_1*T_2+T_3*D. Let C_w be the collision content from M3-T11-037: C_w=product_i gcd(m_i^2,H_i). Then primewise on the fresh conductor and hence globally, boxed: gcd(N_w,D_w,M_rel^4)=M_rel^2*C_w. Therefore the M3-T11-037 dich
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet.
依存関係: M3-T11-033, M3-T11-037.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 45.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 637542
SOURCE_END: 639137
SOURCE_SHA256: 74961fd128721bc0a385e8f0853bbfeec0b6b8caf7a9b81358d7ba02518ba0b8

## M3-T11-038
TYPE: EXACT_STRUCTURE / SAME_MEASURE_RECEIVER / PROJECTIVE_GCD_ROUTER
STATUS: PROVED_EXACT


CLAIM:
For the scaled symmetric parameter
w=u/S=P/(S*E+P)
use the unreduced integer pair
N_w=T_3*D,
D_w=T_1*T_2+T_3*D.
Let C_w be the collision content from M3-T11-037:
C_w=product_i gcd(m_i^2,H_i).
Then primewise on the fresh conductor and hence globally,
boxed:
gcd(N_w,D_w,M_rel^4)=M_rel^2*C_w.
Therefore the M3-T11-037 dichotomy
Q_w*C_w=M_rel^2
becomes:
A. Q_w>=M_rel -> a divisor >=M_rel survives in Num(w);
B. C_w>=M_rel -> gcd(N_w,D_w,M_rel^4)>=M_rel^3.


INTERPRETATION:
C_w is exactly the extra fresh projective content canceled when the rational value w is reduced.
It is not visible from reduced w alone.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet.
HEIGHT:
Exact R<=B retained.
DEPENDS_ON:
M3-T11-033, M3-T11-037.
IMPLIES:
The large-collision branch has a concrete raw projective-gcd receiver
ScaledSymmetricWProjectiveContentTail.
DOES_NOT_IMPLY:
No fixed-power tail bound.
No direct AR-014 application: no fixed outer W with square-divisor lock has yet been proved.
No active-u or active-w support theorem.
NO_DOUBLE_CHARGE:
Do not count baseline M_rel^2 projective content as a new saving; only the extra factor C_w is new collision data.
FLAGS:
M3_T11_W_COLLISION_EQUALS_EXTRA_PROJECTIVE_CONTENT=true
M3_T11_W_FRESH_GCD_IDENTITY=true
M3_T11_W_LARGE_COLLISION_IMPLIES_MREL3_GCD=true
M3_T11_W_PROJECTIVE_CONTENT_TAIL_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 45.




---
