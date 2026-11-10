# M3-T11-031 — For the corrected distinct anti-roots v_1,v_2,v_3 of M3-T11-030, define S=v_1+v_2+v_3, E=v_1*v_2+v_1*v_3+v_2*v_3, P=v_1*v_2*v_3. Exact elimination from the principal endpoint surface gives (S*E+P)^2=S^2*P*(4*S-P). For S!=0 this rationally parameterizes by u in Q: P/S=4*u^2/(1+u^2), (E+P/S)/S=4*u/(1+u^2). Thus v_1,v_2,v_3 are roots of a cubic whose coefficients depend only on (S,u). Rational splitting forces the discriminant-square curve Y^2=-(1+u^2)Q(S,u), Q=-4*S^2+S^4+48*S*u-16*S^3*u-16*u^2+44*

CARD_ID: M3-T11-031
CANONICAL_CARD_KEY: M3-T11-031
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-031
現行一覧の状態: PROVED_EXACT_WITH_OPEN_MOVING_SUPPORT_GATE
種別: EXACT_STRUCTURE / SAME_MEASURE_ADAPTER / THEOREM_GATE_SUPPORT
要点: For the corrected distinct anti-roots v_1,v_2,v_3 of M3-T11-030, define S=v_1+v_2+v_3, E=v_1*v_2+v_1*v_3+v_2*v_3, P=v_1*v_2*v_3. Exact elimination from the principal endpoint surface gives (S*E+P)^2=S^2*P*(4*S-P). For S!=0 this rationally parameterizes by u in Q: P/S=4*u^2/(1+u^2), (E+P/S)/S=4*u/(1+u^2). Thus v_1,v_2,v_3 are roots of a cubic whose coefficients depend only on (S,u). Rational splitting forces the discriminant-square curve Y^2=-(1+u^2)Q(S,u), Q=-4*S^2+S^4+48*S*u-16*S^3*u-16*u^2+44*
主張の抜粋: For the corrected distinct anti-roots v_1,v_2,v_3 of M3-T11-030, define S=v_1+v_2+v_3, E=v_1*v_2+v_1*v_3+v_2*v_3, P=v_1*v_2*v_3. Exact elimination from the principal endpoint surface gives (S*E+P)^2=S^2*P*(4*S-P). For S!=0 this rationally parameterizes by u in Q: P/S=4*u^2/(1+u^2), (E+P/S)/S=4*u/(1+u^2). Thus v_1,v_2,v_3 are roots of a cubic whose coefficients depend only on (S,u). Rational splitting forces the discriminant-square curve Y^2=-(1+u^2)Q(S,u), Q=-4*S^2+S^4+48*S*u-16*S^3*u-16*u^2+44*S^2*u^2+S^4*u^2. For fixed u the quartic discriminant is -65536*u^2*(1+u^2)^2*(-2+25*u^2)^3. Hence every rational nonzero u gives a smooth genus-one fixed-u fiber.
対象・測度: Exact fixed-content relative-fresh endpoint packets on the current M3 principal/double-lift measure.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 35.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 619893
SOURCE_END: 622107
SOURCE_SHA256: 62bfc4af14bab7bb566275ffb52191d17558b5e1e207f0d8b5d39cee29f17d5e

CARD_ID: M3-T11-031


TYPE: EXACT_STRUCTURE / SAME_MEASURE_ADAPTER / THEOREM_GATE_SUPPORT
STATUS: PROVED_EXACT_WITH_OPEN_MOVING_SUPPORT_GATE


CLAIM:
For the corrected distinct anti-roots v_1,v_2,v_3 of M3-T11-030, define
S=v_1+v_2+v_3,
E=v_1*v_2+v_1*v_3+v_2*v_3,
P=v_1*v_2*v_3.


Exact elimination from the principal endpoint surface gives
(S*E+P)^2=S^2*P*(4*S-P).


For S!=0 this rationally parameterizes by u in Q:
P/S=4*u^2/(1+u^2),
(E+P/S)/S=4*u/(1+u^2).


Thus v_1,v_2,v_3 are roots of a cubic whose coefficients depend only on (S,u).
Rational splitting forces the discriminant-square curve
Y^2=-(1+u^2)Q(S,u),
Q=-4*S^2+S^4+48*S*u-16*S^3*u-16*u^2+44*S^2*u^2+S^4*u^2.


For fixed u the quartic discriminant is
-65536*u^2*(1+u^2)^2*(-2+25*u^2)^3.
Hence every rational nonzero u gives a smooth genus-one fixed-u fiber.


POPULATION:
Exact fixed-content relative-fresh endpoint packets on the current M3 principal/double-lift measure.


NOVELTY:
This is not a variable rename of one anti-root and not the retracted same-v CRT. It is a new load-bearing algebraic relation simultaneously coupling the three distinct anti-root coordinates that carry the separate m_i^2 Gaussian root-line congruences.


IMPLIES:
The corrected three-root system lies on one explicit rational symmetric incidence surface; fixed rational u reduces its split-cubic condition to genus one.


DOES_NOT_IMPLY:
No uniform fixed-u B^o(1) theorem is claimed.
No moving-u support saving is proved.
No product of the three root-line densities is legal.
The cubic discriminant square is not an independent probability after conditioning on rational v_i.


DUPLICATE_OF:
none found in RESULT-LEDGER/ROUTE semantic sweep.
Section 17.4 supplies the older triple-spin discriminant but not this three-corrected-anti-root symmetric incidence relation.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 35.


CURRENT_MINIMAL_TARGET=FreshRelativeConductorMovingRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=ThreeAntiRootSymmetricIncidenceMovingSupport
M3_T11_THREE_ANTIROOT_SYMMETRIC_INCIDENCE=true
M3_T11_THREE_ANTIROOT_FIXED_U_GENUS_ONE=true
M3_T11_THREE_ANTIROOT_MOVING_U_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


---
