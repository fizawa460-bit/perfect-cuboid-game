# M3-T11-034 — symmetric-u conductor transfer

CARD_ID: M3-T11-034
CANONICAL_CARD_KEY: M3-T11-034
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-034
現行一覧の状態: RETRACTED
種別: RETRACTED / ERROR
要点: Retracted symmetric-u fresh-conductor transfer
主張の抜粋: The inverse of the M3-T11-031 conic parameterization was written incorrectly as u=P/(S*E+P). The correct identity is u=P*S/(S*E+P). Therefore the claimed fresh-conductor transfer into Num(u) is invalid and withdrawn; M3_T11_SYMMETRIC_U_FRESH_TRANSFER=false.
対象・測度: Exact fixed-content/coefficient relative-fresh endpoint packet.
依存関係: M3-T11-031.
再開条件の抜粋: Do not reopen the withdrawn transfer without a new exact identity; use the corrected common-u route beginning at M3-T11-035.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 40 retraction / section 41 correction.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 626553
SOURCE_END: 629255
SOURCE_SHA256: 5a95ccd453c78f81fc7117aa7f5b203e540180f8f1a307f60691ceb6c35e29cc

CARD_ID: M3-T11-034


TYPE: EXACT_STRUCTURE / SAME_MEASURE_ROUTER / LOCAL_VALUATION_TRANSFER
STATUS: PROVED_EXACT_WITH_OPEN_COUNTING_GATE


CLAIM:
On the finite symmetric-parameter branch u=P/(S*E+P), fresh relative conductor is conserved primewise between the numerator of u and explicit normalized anti-root collision cross-gcds.


For i=1 define
Bhat_2^(1)=B_2/m_1^2,
Bhat_3^(1)=B_3/m_1^2,
H_1=A_2*Bhat_3^(1)+A_3*Bhat_2^(1),
and cyclically H_2,H_3.


For p^a||m_i, if e=v_p(H_i)<2a then
v_p(u)=2a-e.


Consequently
Q_u=product_i[m_i^2/gcd(m_i^2,H_i)]
divides Num(u).


With
C_u=product_i gcd(m_i^2,H_i),
one has exactly
Q_u*C_u=M_rel^2,
hence max(Q_u,C_u)>=M_rel.


POPULATION:
Exact fixed-content/coefficient relative-fresh endpoint packets on the finite-u part of the current M3 principal/double-lift measure.


HEIGHT:
Exact physical R<=B retained.


DEPENDS_ON:
M3-T11-031;
corrected M3-T11-030;
M3-T11-033 local denominator valuations.


IMPLIES:
Every large-M_rel endpoint has either a large realized-u numerator divisor or a large explicit scaled anti-root collision cross-gcd.


ALIASES:
symmetric-u conductor transfer;
fresh-conductor conservation to u;
scaled anti-root collision cross-gcd;
u-transfer/collision dichotomy.


DUPLICATE_OF:
none found in RESULT-LEDGER, NEGATIVE-REGISTER, or current TrivialSplit route semantic sweep.


SUPERSEDES:
ThreeAntiRootCubicCoefficientRootLineRangeAdapter as the live supporting attack.
M3-T11-032/033 remain retained algebraic routers.


DO_NOT_REPEAT:
Do not count Q_u and C_u as independent savings.
Do not infer sparsity solely from a large divisor of Num(u).
Do not treat p|H_i as an auxiliary-prime tH14 collision without an exact adapter.
Do not include the u=infinity branch in the finite-u valuation formula.


REOPEN_CONDITION:
A same-measure theorem for either realized finite-u support with Q_u large, or scaled collision cross-gcd occupancy with C_u large, strong enough to prove the fixed-content B^(1/12-delta) target.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 39.


CURRENT_MINIMAL_TARGET=FreshRelativeConductorMovingRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=SymmetricUFreshTransferVsScaledAntiRootCollision
M3_T11_SYMMETRIC_U_FRESH_TRANSFER=true
M3_T11_SYMMETRIC_U_MOVING_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false




---
RETRACTION: M3-T11-034


STATUS: RETRACTED


ERROR:
The inverse of the M3-T11-031 conic parameterization was written as
u=P/(S*E+P).


The correct identity is
u=P*S/(S*E+P).


Therefore the claimed fresh-conductor transfer into Num(u) is invalid and is withdrawn.


M3_T11_034_RETRACTED=true
M3_T11_SYMMETRIC_U_FRESH_TRANSFER=false
P_OVER_M3_LIMIT_PROVED=false


---
