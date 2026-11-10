# M3-T11-103 — Interior2PiSquareclassGenus2TwistSelmerSupport

CARD_ID: M3-T11-103
CANONICAL_CARD_KEY: M3-T11-103
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-103
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_V4_DECOMPOSITION / GENUS2_QUADRATIC_TWIST_RECEIVER / RECIPROCAL_SPLIT_NO_GO / NO POWER SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE_GLOBAL_GEOMETRY / RECEIVER_REFINEMENT / NEGATIVE_RESULT / ANTI_LOOP_FIREWALL
要点: The audited fixed-squareclass genus-3 cover has a complementary genus-2 quotient H_{d,u}; for fixed u the new factor is exactly a quadratic twist by d=[2*Pi]. The old q->-q elliptic quotient remains consumed.
主張の抜粋: With A=1+u^2 and x=d*q^2, write H_u(x)=A^5*x^4-128*u^3*A^3*x^3+256*u^4*A^2*(11*u^2-1)*x^2+24576*u^7*A*x-65536*u^10. The complementary involution gives W^2=-d*A*x*H_u(x), with discriminant -2^84*d^8*u^46*A^22*(25*u^2-2)^3, hence smooth genus 2 for rational physical d,u!=0. The V4 action gives Jac(C_{d,u}) ~ E_u x Jac(H_{d,u}); x=0 and infinity give rational 2-torsion. The reciprocal split obstruction is -2^26*u^14*A^6*(9+25*u^2), so the M3-T11-044 reciprocal second-elliptic mechanism is uniformly absent.
対象・測度: Exact same fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B; same measure; structural result only.
依存関係: M3-T11-102 HOSTILE_AUDIT_PASS; audited Section-35 fixed-u genus-one incidence; standard V4/Kani-Rosen decomposition; audited M3-T11-044 reciprocal criterion.
再開条件の抜粋: Reopen if hostile audit rejects the quotient map, discriminants, V4 decomposition, or reciprocal obstruction; or if a genuine non-reciprocal elliptic factor/correspondence with an exact physical adapter is proved.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 116.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 931555
SOURCE_END: 936936
SOURCE_SHA256: 2ea69f9894d308e76ae387d8b87dde9f79a65a9e7282ec8a203918ded97a5701

M3-T11-103
STATUS:
PROVISIONAL EXACT_V4_DECOMPOSITION / GENUS2_QUADRATIC_TWIST_RECEIVER / RECIPROCAL_SPLIT_NO_GO / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING


TYPE:
EXACT_STRUCTURE / SAME_MEASURE_GLOBAL_GEOMETRY / RECEIVER_REFINEMENT / NEGATIVE_RESULT / ANTI_LOOP_FIREWALL


SUMMARY:
For the audited M3-T11-102 fixed-squareclass cover, put A=1+u^2 and x=d*q^2. Then
C_{d,u}: T^2=-A*H_u(d*q^2),
where
H_u(x)=A^5*x^4-128*u^3*A^3*x^3+256*u^4*A^2*(11*u^2-1)*x^2+24576*u^7*A*x-65536*u^10.
Besides the old sigma:(q,T)->(-q,T) elliptic quotient, the complementary involution tau:(q,T)->(-q,-T) has invariants x=d*q^2 and W=d*q*T and gives
H_{d,u}: W^2=-d*A*x*H_u(x).
Thus, for fixed u, the genuinely new complementary quotient is a genus-2 quadratic twist by d.


CLAIM:
Exactly,
Disc_x(H_u)=-2^52*u^26*(1+u^2)^14*(25*u^2-2)^3,
and
Disc_x(-d*(1+u^2)*x*H_u(x))
=-2^84*d^8*u^46*(1+u^2)^22*(25*u^2-2)^3.
Hence every rational physical d!=0,u!=0 gives a smooth genus-2 quotient. The rational Weierstrass points x=0 and infinity give a rational 2-torsion class on Jac(H_{d,u}).


The Q-defined V4 action yields the standard isogeny decomposition
Jac(C_{d,u}) ~_Q E_u x Jac(H_{d,u}),
where E_u is exactly the already-audited Section-35 fixed-u genus-one quotient. Therefore all newly exposed Jacobian arithmetic lies in the genus-2 d-twist factor after the old elliptic factor is firewalled.


For a reciprocal commuting involution x->lambda/x on the genus-2 branch set, the audited M3-T11-044 reciprocal criterion requires f*b^2-a*e1^2=0 for the quartic H_u coefficients. Here
f*b^2-a*e1^2
=-2^26*u^14*(1+u^2)^6*(9+25*u^2),
which is nonzero for every rational physical u!=0. Thus the reciprocal second-elliptic split mechanism is uniformly absent. This does not exclude non-reciprocal elliptic factors or other correspondences.


POPULATION:
Exact same fixed-content/coefficient nondegenerate Stage37 physical endpoint population with R<=B. The fixed-(d,u) curves are fibers inside the audited M3-T11-102 receiver; no measure or height change.


HEIGHT:
Exact physical R<=B inherited from M3-T11-102. This card is structural and does not prove a global point count.


DEPENDS_ON:
Hostile-audit-passed M3-T11-102; audited Section-35 fixed-u genus-one incidence; standard V4/Kani-Rosen decomposition for the exact Q-defined involutions; audited M3-T11-044 reciprocal criterion as an anti-loop template.


IMPLIES:
The current Interior2PiSquareclassSurfaceQSupport route can be sharpened to a genus-2 quadratic-twist/Selmer-support receiver. Any new arithmetic beyond the old fixed-u elliptic quotient must come from Jac(H_{d,u}), a genuine non-reciprocal correspondence, or global cross-u support. The rational 2-torsion supplies a concrete 2-descent interface but no saving by itself.


ALIASES:
Interior2PiSquareclassGenus2TwistSelmerSupport;
FixedSquareclassGenus3V4Prym;
ComplementaryGenus2DTwist.


DUPLICATE_OF:
NONE. The decomposition method parallels M3-T11-044, but the population and receiver are different: M3-T11-103 concerns the audited d=[2*Pi] fixed-squareclass surface created by M3-T11-102.


SUPERSEDES:
No prior theorem. It sharpens M3-T11-102's generic “global genus-3 square-coordinate cover” continuation into an explicit old-elliptic plus new-genus2-twist decomposition.


DO_NOT_REPEAT:
Do not recharge E_u. Do not infer fixed-power saving from genus 2, rational 2-torsion, or the isogeny decomposition. Do not repeat reciprocal x->lambda/x searches on H_{d,u}. Do not claim absolute simplicity of Jac(H_{d,u}). Do not identify fixed d with fixed Pi or recharge q's M_rel^2 denominator.


REOPEN_CONDITION:
Hostile audit rejects the quotient map, discriminant factors, V4 decomposition applicability, or reciprocal obstruction; or a genuine non-reciprocal elliptic factor / stronger correspondence with an exact physical adapter is proved.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 116.


CREDIT:
No fixed-power support saving. No fixed-squareclass B^o(1) theorem. No denominator-extreme closure. No primary-gate closure. No endpoint theorem. No P(B)/M3(B) limit. No Perfect Cuboid nonexistence credit.


FLAGS:
M3_T11_FIXED_SQUARECLASS_GENUS3_COMPLEMENTARY_GENUS2_QUOTIENT=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_GENUS2_IS_D_TWIST=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_GENUS3_JAC_SPLIT_E_PLUS_GENUS2=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_GENUS2_RATIONAL_2TORSION=PROVISIONAL
M3_T11_FIXED_SQUARECLASS_GENUS2_RECIPROCAL_SECOND_ELLIPTIC=false
M3_T11_FIXED_SQUARECLASS_BO1_PROVED=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


LATEST_RESEARCH_CARD=M3-T11-103
LATEST_AUDITED_RESEARCH_CARD=M3-T11-102
PROVISIONAL_FRONTIER_CARD=M3-T11-103
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|Interior2PiSquareclassGenus2TwistSelmerSupport
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|Interior2PiSquareclassGenus2TwistSelmerSupport
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-103. Mainbatch may continue only on exact same-measure 2-descent/Selmer/support information in Jac(H_{d,u}) across moving u and d=[2*Pi], on a proved non-reciprocal factor/correspondence with a physical adapter, or on the independent theta moving-support route.
NEXT_RESEARCH_CARD_ID=M3-T11-104
