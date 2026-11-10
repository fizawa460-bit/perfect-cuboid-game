# M3-T11-032 — Let the corrected distinct anti-roots be v_i=A_i/B_i in lowest terms, with A_i==rho_i B_i mod m_i^2, rho_i^2==-1 mod m_i^2, m_i=tau_i^sharp. Set M_rel=m_1*m_2*m_3 and F_v(X)=product_i(B_i X-A_i). CRT gives one rho_rel mod M_rel^2 with rho_rel==rho_i mod m_i^2, rho_rel^2==-1 mod M_rel^2. Then exactly F_v(rho_rel)==0 mod M_rel^2. Writing F_v(X)=D X^3-T_1 X^2+T_2 X-T_3, the relation rho_rel^2=-1 reduces the cubic congruence to (T_1-T_3)+(T_2-D)rho_rel==0 mod M_rel^2. Hence M_rel^2 | (T_1-T_3)^2+(T_

CARD_ID: M3-T11-032
CANONICAL_CARD_KEY: M3-T11-032
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-032
現行一覧の状態: PROVED_EXACT_WITH_OPEN_FRESH_CONTENT_AUDIT
種別: EXACT_STRUCTURE / SAME_MEASURE_ADAPTER / JOINT_MODULUS
要点: Let the corrected distinct anti-roots be v_i=A_i/B_i in lowest terms, with A_i==rho_i B_i mod m_i^2, rho_i^2==-1 mod m_i^2, m_i=tau_i^sharp. Set M_rel=m_1*m_2*m_3 and F_v(X)=product_i(B_i X-A_i). CRT gives one rho_rel mod M_rel^2 with rho_rel==rho_i mod m_i^2, rho_rel^2==-1 mod M_rel^2. Then exactly F_v(rho_rel)==0 mod M_rel^2. Writing F_v(X)=D X^3-T_1 X^2+T_2 X-T_3, the relation rho_rel^2=-1 reduces the cubic congruence to (T_1-T_3)+(T_2-D)rho_rel==0 mod M_rel^2. Hence M_rel^2 | (T_1-T_3)^2+(T_
主張の抜粋: Let the corrected distinct anti-roots be v_i=A_i/B_i in lowest terms, with A_i==rho_i B_i mod m_i^2, rho_i^2==-1 mod m_i^2, m_i=tau_i^sharp. Set M_rel=m_1*m_2*m_3 and F_v(X)=product_i(B_i X-A_i). CRT gives one rho_rel mod M_rel^2 with rho_rel==rho_i mod m_i^2, rho_rel^2==-1 mod M_rel^2. Then exactly F_v(rho_rel)==0 mod M_rel^2. Writing F_v(X)=D X^3-T_1 X^2+T_2 X-T_3, the relation rho_rel^2=-1 reduces the cubic congruence to (T_1-T_3)+(T_2-D)rho_rel==0 mod M_rel^2. Hence M_rel^2 | (T_1-T_3)^2+(T_2-D)^2.
対象・測度: Exact fixed-content relative-fresh endpoint packets on the M3 principal/double-lift measure.
依存関係: M3-T11-029; corrected M3-T11-030; pairwise coprimality of fresh relative cores.
再開条件の抜粋: A primewise valuation theorem controlling gcd(T_1-T_3,T_2-D,M_rel), strong enough to expose a polynomial part of the M_rel^2 modulus on a primitive coefficient pair.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 36.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 622107
SOURCE_END: 623878
SOURCE_SHA256: 5137800e1fd1247c4d39d72948f342f6f4c46099f071b0b137c138641de58600

CARD_ID: M3-T11-032


TYPE: EXACT_STRUCTURE / SAME_MEASURE_ADAPTER / JOINT_MODULUS
STATUS: PROVED_EXACT_WITH_OPEN_FRESH_CONTENT_AUDIT


CLAIM:
Let the corrected distinct anti-roots be v_i=A_i/B_i in lowest terms, with
A_i==rho_i B_i mod m_i^2,
rho_i^2==-1 mod m_i^2,
m_i=tau_i^sharp.


Set M_rel=m_1*m_2*m_3 and
F_v(X)=product_i(B_i X-A_i).


CRT gives one rho_rel mod M_rel^2 with
rho_rel==rho_i mod m_i^2,
rho_rel^2==-1 mod M_rel^2.


Then exactly
F_v(rho_rel)==0 mod M_rel^2.


Writing
F_v(X)=D X^3-T_1 X^2+T_2 X-T_3,
the relation rho_rel^2=-1 reduces the cubic congruence to
(T_1-T_3)+(T_2-D)rho_rel==0 mod M_rel^2.


Hence
M_rel^2 | (T_1-T_3)^2+(T_2-D)^2.


NOVELTY:
This is not the retracted same-v CRT. It retains three distinct rational anti-roots and combines their separate fresh root lines through the product cubic. The joint modulus lives on one common integer coefficient pair.


POPULATION:
Exact fixed-content relative-fresh endpoint packets on the M3 principal/double-lift measure.


DEPENDS_ON:
M3-T11-029;
corrected M3-T11-030;
pairwise coprimality of fresh relative cores.


DOES_NOT_IMPLY:
No primitive AR-009 saving yet. The coefficient pair may have common fresh content because complementary denominators B_j can carry m_i-primes for j!=i.


REOPEN_CONDITION:
A primewise valuation theorem controlling gcd(T_1-T_3,T_2-D,M_rel), strong enough to expose a polynomial part of the M_rel^2 modulus on a primitive coefficient pair.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 36.


M3_T11_DISTINCT_ANTIROOT_CUBIC_CRT=true
M3_T11_CUBIC_COEFFICIENT_JOINT_ROOTLINE=true
M3_T11_CUBIC_COEFFICIENT_PRIMITIVE_AT_FRESH_PRIMES_PROVED=false
CURRENT_SUPPORTING_ATTACK=ThreeAntiRootCubicCoefficientFreshContentAudit
P_OVER_M3_LIMIT_PROVED=false


---
