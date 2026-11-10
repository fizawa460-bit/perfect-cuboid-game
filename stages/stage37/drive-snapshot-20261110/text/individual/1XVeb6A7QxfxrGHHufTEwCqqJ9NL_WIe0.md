# M3-T11-065 — Exact split-5 factor-7-bit router and pointwise delta determination

CARD_ID: M3-T11-065
CANONICAL_CARD_KEY: M3-T11-065
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-065
現行一覧の状態: PROVED_EXACT_LOCAL_STRUCTURE / GLOBAL CLASSIFICATION OPEN
種別: EXACT_LOCAL_STRUCTURE / THEOREM_GATE REFINEMENT
要点: Retain M3-T11-048, M3-T11-057, and M3-T11-059 through M3-T11-064. In K=Q(s), s^2=-14, put Z=-R+I*s, R=b*(124*a^2+9*b^2), I=a*(100*a^2+7*b^2). By M3-T11-058, N(Z)=R^2+14*I^2=Y_h^2 i
主張の抜粋: Retain M3-T11-048, M3-T11-057, and M3-T11-059 through M3-T11-064. In K=Q(s), s^2=-14, put
対象・測度: Exact x=27/40 translated-lift carrier restricted to the canonical M3-T11-048 three-packet survivor locus.
依存関係: M3-T11-048; M3-T11-057; M3-T11-058; M3-T11-059; M3-T11-062; M3-T11-063; M3-T11-064.
再開条件の抜粋: Intersect the uniquely determined delta packet with the exact u*v=H*K factorization and the M3-T11-057 Mordell-Weil residue classes. A productive route should transport the required denominator/numerator characters onto nQ+epsilon*T (for ex
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 72.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 707052
SOURCE_END: 707079
SOURCE_SHA256: f7b2020008d4380356266c4a0f3a01c5767a6926edcafb4aefcdae4b549c731e

RESEARCH_CARD=M3-T11-065

## Retained LEDGER source 2
SOURCE_START: 733671
SOURCE_END: 737478
SOURCE_SHA256: 56fb1ca2b2b56236ed2acdd63cf930823824ccb7fddcfb493adb1d31ac2c731e

## M3-T11-065
ID:
M3-T11-065
TYPE:
EXACT_LOCAL_STRUCTURE / THEOREM_GATE REFINEMENT
TITLE:
Exact split-5 factor-7-bit router and pointwise delta determination
STATUS:
PROVED_EXACT_LOCAL_STRUCTURE / GLOBAL CLASSIFICATION OPEN
CLAIM:
Retain M3-T11-048, M3-T11-057, and M3-T11-059 through M3-T11-064. In K=Q(s), s^2=-14, put
Z=-R+I*s,
R=b*(124*a^2+9*b^2),
I=a*(100*a^2+7*b^2).
By M3-T11-058, N(Z)=R^2+14*I^2=Y_h^2 is a rational square. Since 5 splits in K, the two local Q_5 squareclasses of Z are equal. Reducing at the two split roots s==+1 and s==-1 modulo 5 gives exactly
Z_+ == b*(a+b)^2 (mod 5),
Z_- == b*(a-b)^2 (mod 5).
Hence whenever 5 does not divide b, at least one of a+b,a-b is a 5-adic unit and therefore both split-place classes satisfy [Z]=[b].


M3-T11-063 already gives 5 does not divide b on Packets I/II, so
Packets I/II: [-delta]=[b] in Q_5^x/Q_5^x2.


For Packet III:
- if d=9, then 5 does not divide b and again [-delta]=[b];
- if d=225, then 5 divides b. The previous v_5(b)>=2 sharpens to v_5(b)>=3. Indeed v_5(b)=2, b=25c with 5 not dividing a*c, would make
F-/25 == 4*a*(a-c) (mod 5),
F+/25 == 4*a*(a+c) (mod 5),
and for c/a in F_5^x one of these two unit residues is nonsquare (the cases c/a=+/-1 leave the other residue nonsquare), contradicting that Packet III has both F- and F+ rational squares. For v_5(b)>=3, v_5(R)>=3 and v_5(I)=2, so at s==+/-1
Z/25 == +/-4*a^3 (mod 5),
whose squareclass is [a] because -1 and 4 are squares in Q_5. Thus Packet III,d=225 has [-delta]=[a].


Because the M3-T11-064 split-3 router leaves exactly two delta values differing by a factor 7, and 7 is a nonsquare modulo 5, the split-5 class selects exactly one. Explicitly, with chi5 the Legendre symbol modulo 5:
Packets I/II:
 b==1 (mod 3): chi5(b)=+1 => delta=14; chi5(b)=-1 => delta=2.
 b==2 (mod 3): chi5(b)=+1 => delta=1;  chi5(b)=-1 => delta=7.
Packet III:
 b==1 (mod 3): chi5(beta)=+1 => delta=1;  chi5(beta)=-1 => delta=7.
 b==2 (mod 3): chi5(beta)=+1 => delta=14; chi5(beta)=-1 => delta=2,
where beta=b on d=9 and beta=a on d=225.


This closes the local delta ambiguity but does not classify rational points. The M3-T11-057 infinite Mordell-Weil progressions remain.
POPULATION:
Exact x=27/40 translated-lift carrier restricted to the canonical M3-T11-048 three-packet survivor locus.
DEPENDS_ON:
M3-T11-048;
M3-T11-057;
M3-T11-058;
M3-T11-059;
M3-T11-062;
M3-T11-063;
M3-T11-064.
NEW_RECEIVERS:
X27Over40Split5DeltaSevenBitRouter;
X27Over40DeltaPointwiseUnique;
X27Over40PacketIIID225V5BGe3.
DO_NOT_REPEAT:
Do not reopen two delta candidates after the 3-adic and 5-adic characters are known. Do not treat d=225 Packet III as merely v_5(b)>=2; the exact surviving branch has v_5(b)>=3. Do not infer rational-point classification from local delta uniqueness.
REOPEN_CONDITION:
Intersect the uniquely determined delta packet with the exact u*v=H*K factorization and the M3-T11-057 Mordell-Weil residue classes. A productive route should transport the required denominator/numerator characters onto nQ+epsilon*T (for example through division-polynomial or elliptic-denominator characters) or produce a lower-genus global packet; another unconstrained finite-prime sieve is not sufficient.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 72.
FLAGS:
M3_T11_X_27_OVER_40_SPLIT5_DELTA_SEVEN_BIT_ROUTER=true
M3_T11_X_27_OVER_40_DELTA_POINTWISE_UNIQUE=true
M3_T11_X_27_OVER_40_PACKET_III_D225_V5B_GE3=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40DeltaResolvedHKFactorDistributionWithMWIntersection
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-065
