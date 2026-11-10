# M3-T11-105 — FixedSquareclassGenus2S4Quartic

CARD_ID: M3-T11-105
CANONICAL_CARD_KEY: M3-T11-105
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-105
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / GENERIC_S4_ETALE / NORM_ONLY_NO_GO / GENERIC_QUADRATIC_SPLIT_NO_GO / NO POWER SAVING
種別: EXACT_STRUCTURE / GENERIC_GALOIS_PREFLIGHT / SAME_MEASURE_DESCENT_PREFLIGHT / NEGATIVE_RESULT / ANTI_LOOP_FIREWALL
要点: After exact normalization, the residual genus-2 quartic is generically S4 over Q(u). The norm of the physical quartic étale class is always [-1], so norm-only descent and generic two-quadratic splitting give no new support saving.
主張の抜粋: With z=(1+u^2)x/(16u^2), Q_u(z)=(1+u^2)z^4-8uz^3+(11u^2-1)z^2+6uz-u^2 and Disc=-2^4*u^2*(1+u^2)^2*(25u^2-2)^3. Q_u and its cubic resolvent are irreducible over Q(u), while the discriminant squareclass [2-25u^2] is nonsquare, hence generic Gal=S4. For theta a root of monic Q_u/(1+u^2), physical points satisfy N(z-theta)=-(T/(2^8*u^4*(1+u^2)))^2, so the norm class is [-1]. Full non-norm S4 étale/Selmer information remains open.
対象・測度: Exact same Stage37 physical endpoint population with R<=B; same measure; no exceptional-specialization or power-saving credit.
依存関係: M3-T11-101/102 HOSTILE_AUDIT_PASS; M3-T11-103/104 PROVISIONAL.
再開条件の抜粋: Reopen if hostile audit rejects M3-T11-103/104/105, the generic Galois calculation fails, or an exact same-measure theorem turns the full S4 étale class or exceptional-specialization locus into a quantitative saving.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 118.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 941408
SOURCE_END: 948611
SOURCE_SHA256: fe79f66f33622ea22329f1c9bf572774ff5a808a6cf4f3c8621c129f46d8599e

M3-T11-105
STATUS:
PROVISIONAL GENERIC_S4_ETALE / NORM_ONLY_NO_GO / GENERIC_QUADRATIC_SPLIT_NO_GO / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING


TYPE:
EXACT_STRUCTURE / GENERIC_GALOIS_PREFLIGHT / SAME_MEASURE_DESCENT_PREFLIGHT / NEGATIVE_RESULT / ANTI_LOOP_FIREWALL


SUMMARY:
After z=(1+u^2)x/(16u^2), the residual quartic in M3-T11-103 becomes
Q_u(z)=(1+u^2)z^4-8uz^3+(11u^2-1)z^2+6uz-u^2.
Generically over Q(u) it has Galois group S4. For the physical residual étale element z-theta, the norm to Q(u) has constant squareclass [-1].


CLAIM:
Disc(Q_u)=-2^4*u^2*(1+u^2)^2*(25u^2-2)^3.
Q_u and its standard cubic resolvent are irreducible over Q(u), certified by the irreducible specialization u=1:
Q_1=2z^4-8z^3+10z^2+6z-1,
resolvent proportional to y^3-5y^2-10y-11.
The discriminant squareclass is [2-25u^2], nonsquare in Q(u). Hence Gal(Q_u/Q(u))=S4.


With theta a root of the monic quartic Q_u/A and A=1+u^2,
N(z-theta)=Q_u(z)/A=-(T/(2^8*u^4*A))^2
on every physical point, so the norm squareclass is exactly [-1]. Norm-only descent therefore contains no d/q support information.


SCOPE:
Generic S4 is a function-field statement and does not assert S4 for every rational u. The full element z-theta in the quartic étale algebra remains open; only its norm and generic quadratic-split shortcuts are frozen.


POPULATION:
Exact same fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B; same measure. No exceptional-specialization counting theorem is asserted.


HEIGHT:
Exact physical R<=B inherited from M3-T11-102. Structural/generic Galois and no-double-charge result only.


DEPENDS_ON:
M3-T11-101/102 HOSTILE_AUDIT_PASS; M3-T11-103/104 PROVISIONAL; standard quartic resolvent/Galois criterion.


IMPLIES:
Sharpen the interior route to Interior2PiSquareclassGenus2S4EtaleSelmerSupport. The remaining genus-2 information must use the non-norm S4 étale class, exceptional-specialization control with a physical adapter, a non-reciprocal correspondence, or global cross-u support.


ALIASES:
FixedSquareclassGenus2S4Quartic;
ResidualEtaleNormMinusOneFirewall;
Interior2PiS4EtaleSelmer.


DUPLICATE_OF:
NONE. M3-T11-104 freezes the rational x-factor; M3-T11-105 treats the distinct quartic étale factor and its generic Galois structure.


SUPERSEDES:
The generic hope that the residual quartic will split into two quadratic norm problems, and any norm-only use of the residual quartic class.


DO_NOT_REPEAT:
Do not use only N(z-theta), search again for generic two-quadratic factorization, promote generic S4 to every specialization, or infer a thin-set/fixed-power saving without a same-physical-measure theorem.


REOPEN_CONDITION:
Hostile audit rejects M3-T11-103/104/105, the generic Galois calculation fails, or an exact physical theorem converts the full S4 étale class or exceptional-specialization locus into a quantitative saving.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 118.


CREDIT:
No fixed-power saving. No fixed-squareclass B^o(1). No thin-set physical saving. No primary-gate/endpoint/P-over-M3/Perfect-Cuboid credit.


FLAGS:
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_QUARTIC_NORMAL_FORM=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_QUARTIC_GENERIC_GALOIS_S4=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_ETALE_NORM_CLASS_MINUS_ONE=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_NORM_ONLY_NEW_SAVING=false
M3_T11_FIXED_SQUARECLASS_GENUS2_GENERIC_TWO_QUADRATIC_SPLIT=false
M3_T11_FIXED_SQUARECLASS_FULL_GENUS2_SELMER_COLLAPSE_PROVED=false
M3_T11_FIXED_SQUARECLASS_BO1_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


LATEST_RESEARCH_CARD=M3-T11-105
LATEST_AUDITED_RESEARCH_CARD=M3-T11-102
PROVISIONAL_FRONTIER_CARD=M3-T11-105
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
PROVISIONAL_DEPENDS_ON=M3-T11-103,M3-T11-104
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|Interior2PiSquareclassGenus2S4EtaleSelmerSupport
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|Interior2PiSquareclassGenus2S4EtaleSelmerSupport
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-103, then 104, then 105. Mainbatch may continue only with non-norm information in the S4 quartic étale class, an exact physical exceptional-specialization theorem, a non-reciprocal correspondence with physical adapter, genuinely global cross-u support, or the independent theta route.
NEXT_RESEARCH_CARD_ID=M3-T11-106


## AUDIT PROMOTION — M3-T11-103 through M3-T11-105
AUDIT_DOC_ID=1TLW9ndcDO5o6HodeD314X77Ch-5gOMjUSzdYy2Y3nBU
HOSTILE_AUDIT=PASS
AUDITED_CARDS=M3-T11-103,M3-T11-104,M3-T11-105
LATEST_AUDITED_RESEARCH_CARD=M3-T11-105


M3-T11-103 STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_V4_DECOMPOSITION / GENUS2_QUADRATIC_TWIST_RECEIVER / RECIPROCAL_SPLIT_NO_GO / NO POWER SAVING
M3-T11-104 STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_KUMMER_COLLAPSE / RATIONAL_2TORSION_NO_GO / NO POWER SAVING
M3-T11-105 STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / GENERIC_S4_ETALE / NORM_ONLY_NO_GO / GENERIC_QUADRATIC_SPLIT_NO_GO / NO POWER SAVING


CANONICAL_AUDIT_CONSEQUENCES:
- The fixed-squareclass genus-3 cover has complementary smooth genus-2 quotient H_{d,u}; Jac(C_{d,u}) is Q-isogenous to the already-consumed E_u factor times Jac(H_{d,u}).
- The reciprocal M3-T11-044 second-elliptic mechanism is uniformly absent.
- The visible rational-Weierstrass Kummer class on physical points is [x]=[d], exactly the previously consumed interior splitting receiver.
- The residual normalized quartic is generically S4 over Q(u); generic quadratic/two-norm splitting is absent.
- After physical specialization or scalar extension so z lies in the base field, Norm(z-theta) has squareclass [-1]. Norm-only descent contains no d/q support information.


M3_T11_FIXED_SQUARECLASS_GENUS3_COMPLEMENTARY_GENUS2_QUOTIENT=true
M3_T11_FIXED_SQUARECLASS_GENUS2_IS_D_TWIST=true
M3_T11_FIXED_SQUARECLASS_GENUS3_JAC_SPLIT_E_PLUS_GENUS2=true
M3_T11_FIXED_SQUARECLASS_GENUS2_RATIONAL_2TORSION=true
M3_T11_FIXED_SQUARECLASS_GENUS2_RECIPROCAL_SECOND_ELLIPTIC=false
M3_T11_FIXED_SQUARECLASS_GENUS2_PHYSICAL_X_KUMMER_CLASS_D=true
M3_T11_FIXED_SQUARECLASS_GENUS2_COMPLEMENTARY_FACTOR_CLASS_D=true
M3_T11_FIXED_SQUARECLASS_GENUS2_RATIONAL_WEIERSTRASS_DESCENT_NEW_SAVING=false
M3_T11_101_INTERIOR_SPLITTING_AND_GENUS2_X_KUMMER_INDEPENDENT=false
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_QUARTIC_NORMAL_FORM=true
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_QUARTIC_GENERIC_GALOIS_S4=true
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_ETALE_NORM_CLASS_MINUS_ONE=true
M3_T11_FIXED_SQUARECLASS_GENUS2_RESIDUAL_NORM_ONLY_NEW_SAVING=false
M3_T11_FIXED_SQUARECLASS_GENUS2_GENERIC_TWO_QUADRATIC_SPLIT=false
M3_T11_FIXED_SQUARECLASS_FULL_GENUS2_SELMER_COLLAPSE_PROVED=false
M3_T11_FIXED_SQUARECLASS_BO1_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
SURVIVING_FRONTIER=ThetaFourthPowerMovingSupportBeyondKummer|Interior2PiSquareclassGenus2S4EtaleSelmerSupport
NEXT_RESEARCH_CARD_ID=M3-T11-106
