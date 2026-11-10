# M3-T11-072 — The p=3 base denominator character is a Sturmian real-sign law, not a constant Mordell-Weil progression character

CARD_ID: M3-T11-072
CANONICAL_CARD_KEY: M3-T11-072
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-072
現行一覧の状態: PROVED_EXACT_BASE_CHARACTER_LAW / EPSILON1 TORSION-ROOT CHARACTER OPEN
種別: EXACT_CHARACTER_LAW / NEGATIVE_RESULT / FIREWALL / THEOREM-GATE REFINEMENT
要点: Retain M3-T11-067 through M3-T11-071. For W_n=psi_n(Q), exact residues modulo3 give rank of apparition 4 and Ward symmetry constants a_3=1, b_3=2, hence W_(n+4h)==W_n*(-1)^h mod3. 
主張の抜粋: Retain M3-T11-067 through M3-T11-071. For W_n=psi_n(Q), exact residues modulo3 give rank of apparition 4 and Ward symmetry constants a_3=1, b_3=2, hence W_(n+4h)==W_n*(-1)^h mod3. Since M=2656080 has M/4=664020 even, W_(n+M)==W_n mod3. Thus on n==n0 modM the signed residue is fixed as rho(+1)=rho(+2)=+1, rho(-1)=rho(-2
対象・測度: The rank-one E2 Mordell-Weil sequence on the four M3-T11-067 live residue classes; translated-lift interpretation is exact for epsilon=0 and is a base-coordinate statement only for
依存関係: M3-T11-056; M3-T11-067; M3-T11-069; M3-T11-070; M3-T11-071; Ward's finite-field EDS symmetry formula; Silverman-Stephens, The Sign of an Elliptic Divisibility Sequence, Theorem 4.
再開条件の抜粋: Only if the retained rank-one EDS, Ward mod-3 symmetry, or Silverman-Stephens sign theorem is inapplicable. Otherwise continue by controlling the epsilon=1 positive-root sign and/or intersecting the exact Sturmian p=3 law with ramified-7/gl
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 79.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 764547
SOURCE_END: 769408
SOURCE_SHA256: 9fbf9f10039e0cec8c70091c96a89992008f83d525a2dda8953e5937cd2fb292

## M3-T11-072
ID:
M3-T11-072
TYPE:
EXACT_CHARACTER_LAW / NEGATIVE_RESULT / FIREWALL / THEOREM-GATE REFINEMENT
TITLE:
The p=3 base denominator character is a Sturmian real-sign law, not a constant Mordell-Weil progression character
STATUS:
PROVED_EXACT_BASE_CHARACTER_LAW / EPSILON1 TORSION-ROOT CHARACTER OPEN
CLAIM:
Retain M3-T11-067 through M3-T11-071. For W_n=psi_n(Q), exact residues modulo3 give rank of apparition 4 and Ward symmetry constants a_3=1, b_3=2, hence
W_(n+4h)==W_n*(-1)^h mod3.
Since M=2656080 has M/4=664020 even,
W_(n+M)==W_n mod3.
Thus on n==n0 modM the signed residue is fixed as
rho(+1)=rho(+2)=+1,
rho(-1)=rho(-2)=-1.
By M3-T11-069/070 all explicit normalization factors have square character modulo3 on the live classes: e2 is even, R_n(2,12) is even, and 7==1 mod3. Hence
(C_n|3)=(|W_n||3)
for the canonical denominator of U(nQ).
The real curve E2(R) is connected because U^2+1244U+562500 has discriminant -702464<0, and Q is non-torsion. Silverman-Stephens' EDS sign theorem therefore supplies a fixed sigma in {+1,-1} and an irrational beta such that
sign(W_n)=sigma^(n-1)*(-1)^floor(n*beta).
Consequently the exact base denominator law on every live class is
boxed:
(C_n|3)=rho(n0)*sigma^(n-1)*(-1)^floor(n*beta),
for n==n0 modM, n0 in {+1,-1,+2,-2}.
Since M is even and M*beta is irrational, floor((n0+kM)*beta) mod2 takes both parities infinitely often. Therefore (C_n|3) takes both +1 and -1 infinitely often on every ambient live MW progression.
For epsilon=0 this is already the actual translated-root denominator character. It proves that no constant p=3 character, and hence no constant delta in {1,14}, can be assigned to an entire even progression before the translated-lift condition is imposed.
For epsilon=1 this theorem controls the base denominator C_n of U(nQ), not the reciprocal translated denominator A_n/g. The additional positive-root sign in the torsion transform remains open.
POPULATION:
The rank-one E2 Mordell-Weil sequence on the four M3-T11-067 live residue classes; translated-lift interpretation is exact for epsilon=0 and is a base-coordinate statement only for epsilon=1.
DEPENDS_ON:
M3-T11-056;
M3-T11-067;
M3-T11-069;
M3-T11-070;
M3-T11-071;
Ward's finite-field EDS symmetry formula;
Silverman-Stephens, The Sign of an Elliptic Divisibility Sequence, Theorem 4.
IMPLIES:
The remaining p=3 obstruction is not signed-EDS periodicity: that part is already closed. It is the archimedean sign required by the positive denominator normalization, together with the epsilon=1 positive-root sign after torsion reciprocity. A legal continuation must keep the Sturmian sign law and intersect it with torsion-root sign, ramified-7 compatibility, or the global delta-resolved packet. Pure p-adic reduction-class or finite signed-EDS periodicity cannot close the branch.
ALIASES:
X27Over40P3BaseDenominatorSturmianLaw;
X27Over40P3SignedEDSPeriodM;
X27Over40P3ConstantProgressionFirewall;
X27Over40ArchimedeanSignNormalizationObstruction.
DUPLICATE_OF:
none found. M3-T11-068 rejects bad-prime quotient-order determination of denominator unit characters, but does not identify the missing global bit. This card identifies that bit at p=3 as the real EDS sign and proves nonconstancy on each M-progression.
DO_NOT_REPEAT:
Do not seek a constant value of (C_n|3) on n==n0 modM.
Do not infer the positive denominator character from the signed residue W_n mod3 alone.
Do not apply the base C_n law directly to epsilon=1 after adding T; its denominator is A_n/g and the root-sign transfer remains open.
Do not claim that both delta values occur among translated-lift solutions; only the ambient MW progression has both p=3 character values infinitely often.
Do not promote rational-point classification, fixed-power saving, primary theorem-gate closure, or P/M3 credit.
REOPEN_CONDITION:
Only if the retained rank-one EDS, Ward mod-3 symmetry, or Silverman-Stephens sign theorem is inapplicable. Otherwise continue by controlling the epsilon=1 positive-root sign and/or intersecting the exact Sturmian p=3 law with ramified-7/global packet conditions.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 79.
FLAGS:
M3_T11_X_27_OVER_40_P3_SIGNED_EDS_PERIOD_M=true
M3_T11_X_27_OVER_40_P3_BASE_DENOMINATOR_STURMIAN_LAW=true
M3_T11_X_27_OVER_40_P3_BASE_CHARACTER_NONCONSTANT_EACH_LIVE_PROGRESSION=true
M3_T11_X_27_OVER_40_P3_CONSTANT_PROGRESSION_SHORTCUT_REJECTED=true
M3_T11_X_27_OVER_40_EPSILON1_ACTUAL_P3_ROOT_CHARACTER_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40P3SturmianTorsionRootSignAndRamified7Compatibility
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-072
