# M3-HIST17-DOMINANCE-FW-001 — Stage17 exactly-one dominance

CARD_ID: M3-HIST17-DOMINANCE-FW-001
CANONICAL_CARD_KEY: M3-HIST17-DOMINANCE-FW-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-HIST17-DOMINANCE-FW-001
現行一覧の状態: PROVED_AUDITED
種別: THEOREM_RESULT / FIREWALL
要点: Let H_{1,d}(B) count primitive canonical cuboids with integral space diagonal and at least one integral face. Every object in H_{1,d}(B)-N_1(B) has at least two integral faces, so 
主張の抜粋: Let H_{1,d}(B) count primitive canonical cuboids with integral space diagonal and at least one integral face. Every object in H_{1,d}(B)-N_1(B) has at least two integral faces, so it contributes to at least one Stage13 pair-overlap term. Writing P(B)=A_ab,ac+A_ab,bc+A_ac,bc, the frozen Stage13 overlap theorem gives P(B
対象・測度: primitive canonical integral-space-diagonal cuboids with at least one integral face versus exactly one integral face.
依存関係: M3-HIST17-N1-ASYMPTOTIC-001; frozen Stage13 pair-overlap little-o theorem.
再開条件の抜粋: an effective overlap theorem or finer asymptotic for the at-least-one correction.
旧詳細位置: Stage17 final R01, Exactly-one dominance after imposing the space diagonal.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 517220
SOURCE_END: 519260
SOURCE_SHA256: 76cd35a425cab25509d2d7d3c2d949160714526b6c4c73eec25e6fe493eef254

## M3-HIST17-DOMINANCE-FW-001
TYPE: THEOREM_RESULT / FIREWALL
STATUS: PROVED_AUDITED
CLAIM:
Let H_{1,d}(B) count primitive canonical cuboids with integral space diagonal and at least one integral face.
Every object in H_{1,d}(B)-N_1(B) has at least two integral faces, so it contributes to at least one Stage13 pair-overlap term.
Writing
P(B)=A_ab,ac+A_ab,bc+A_ac,bc,
the frozen Stage13 overlap theorem gives
P(B)=o(B(log B)^3).
Hence
0 <= H_{1,d}(B)-N_1(B) <= P(B),
so
H_{1,d}(B)=N_1(B)+o(B(log B)^3),
therefore
H_{1,d}(B) ~ N_1(B)
and
N_1(B)/H_{1,d}(B) -> 1.
This conclusion does not assume perfect cuboids are absent; three-face objects are contained in the lower-order overlap correction.
AR-039 remains only a lower-order constructive subfamily and is not the mechanism for this dominance theorem.
POPULATION:
primitive canonical integral-space-diagonal cuboids with at least one integral face versus exactly one integral face.
HEIGHT:
exact d=R<=B.
DEPENDS_ON:
M3-HIST17-N1-ASYMPTOTIC-001; frozen Stage13 pair-overlap little-o theorem.
IMPLIES:
after imposing integral space diagonal, exactly-one-face objects asymptotically dominate the at-least-one-face host at the B(log B)^3 scale.
ALIASES:
Stage17 exactly-one dominance;
H1d asymptotic equivalence;
pair-overlap subtraction theorem.
DUPLICATE_OF:
none; Stage16 overlap card explicitly lacked this little-o conclusion, while Stage17 gains it from the Stage13 space-integral overlap theorem.
SUPERSEDES:
Stage16-era same-order-only comparison between exactly-one and at-least-one populations once the space condition is imposed.
DO_NOT_REPEAT:
Do not transfer this dominance result back to Stage16 without the space condition.
Do not infer effective convergence rate.
Do not use perfect-cuboid nonexistence as an assumption.
Do not interpret the result as independence of face conditions.
REOPEN_CONDITION:
an effective overlap theorem or finer asymptotic for the at-least-one correction.
DETAIL_DOC:
Stage17 final R01, Exactly-one dominance after imposing the space diagonal.
---
