# M3-T11-068 — Reduction-kernel classes do not determine the normalized denominator characters

CARD_ID: M3-T11-068
CANONICAL_CARD_KEY: M3-T11-068
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-068
現行一覧の状態: PROVED_EXACT_NEGATIVE / ACTIVE FIREWALL
種別: NEGATIVE_RESULT / FIREWALL / THEOREM_GATE REFINEMENT
要点: Retain M3-T11-067. Let U(nQ)=d0*(A_n/C_n)^2 with positive reduced C_n. The exact bad-prime reduction-kernel orders are 4 at p=3, 12 at p=5, and 3 at p=7, but the Legendre character
主張の抜粋: Retain M3-T11-067. Let U(nQ)=d0*(A_n/C_n)^2 with positive reduced C_n. The exact bad-prime reduction-kernel orders are 4 at p=3, 12 at p=5, and 3 at p=7, but the Legendre character of C_n is not a function of n modulo those orders. Exact counterexamples from the rational group law on E2 are: - p=3: n=1 and n=9 are cong
対象・測度: The rank-one E2 Mordell-Weil sequence attached to Q=(50,5600), with the active M3-T11-067 translated-lift application on the four surviving progressions.
依存関係: M3-T11-066; M3-T11-067; exact rational multiplication on E2 at n=9,10,13.
再開条件の抜粋: Produce an exact normalized division-polynomial, EDS, sigma/formal-group-plus-global-normalization, or equivalent recurrence that computes the unit squareclass of C(nQ+epsilon*T) on the four live M3-T11-067 progressions. The proof must cont
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 75.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 747604
SOURCE_END: 751482
SOURCE_SHA256: 69c3139053f3b24463a406a37c26bd7cfdf00e524726f7485bf5d56b5f22658b

## M3-T11-068
ID:
M3-T11-068
TYPE:
NEGATIVE_RESULT / FIREWALL / THEOREM_GATE REFINEMENT
TITLE:
Reduction-kernel classes do not determine the normalized denominator characters
STATUS:
PROVED_EXACT_NEGATIVE / ACTIVE FIREWALL
CLAIM:
Retain M3-T11-067. Let U(nQ)=d0*(A_n/C_n)^2 with positive reduced C_n. The exact bad-prime reduction-kernel orders are 4 at p=3, 12 at p=5, and 3 at p=7, but the Legendre character of C_n is not a function of n modulo those orders.
Exact counterexamples from the rational group law on E2 are:
- p=3: n=1 and n=9 are congruent modulo 4 and both have 3 not dividing C_n, but C_1=1 gives (C_1|3)=+1 while C_9=57369809 is 2 modulo 3 and gives (C_9|3)=-1.
- p=5: n=1 and n=13 are congruent modulo 12 and both have 5 not dividing C_n, but C_1=1 gives (C_1|5)=+1 while C_13=21024997727248007 is 2 modulo 5 and gives (C_13|5)=-1.
- p=7: n=1 and n=10 are congruent modulo 3 and both have 7 not dividing C_n, but C_1=1 gives (C_1|7)=+1 while C_10=2692585801 is 3 modulo 7 and gives (C_10|7)=-1.
Therefore the M3-T11-067 reduction-kernel data p|C_n iff ord_p(Q)|n controls denominator divisibility only. It cannot by itself be upgraded to the unit squareclass characters required by M3-T11-066/067.
This does not rule out an exact character law on the four much thinner residue classes modulo M=2656080. It rules out only the shortcut that tries to derive those characters from the bad-prime reduction class or quotient order alone.
POPULATION:
The rank-one E2 Mordell-Weil sequence attached to Q=(50,5600), with the active M3-T11-067 translated-lift application on the four surviving progressions.
DEPENDS_ON:
M3-T11-066;
M3-T11-067;
exact rational multiplication on E2 at n=9,10,13.
IMPLIES:
The current first attack must retain globally normalized denominator-unit information. A legal continuation is a normalized division-polynomial / elliptic-divisibility-sequence unit law, or an equivalent global recurrence, specialized to the four M-progressions and then transported through the epsilon=1 torsion shift. Pure reduction-kernel periodicity is RED.
ALIASES:
X27Over40ReductionKernelCharacterFirewall;
X27Over40NormalizedDenominatorUnitRequired;
X27Over40BadPrimeQuotientOrderInsufficient.
DUPLICATE_OF:
none found under semantic rematch. M3-T11-066 warned not to infer global periodicity without a division-polynomial/EDS/formal-group proof; M3-T11-067 proved only divisibility orders. This card supplies explicit counterexamples showing why quotient-order data alone cannot prove the needed unit characters.
DO_NOT_REPEAT:
Do not infer (C_n|p) from n modulo 4,12,3 at p=3,5,7 respectively.
Do not treat p|C_n periodicity as equivalent to denominator-unit character periodicity.
Do not use p-adic reduction continuity alone as a substitute for globally normalized denominator-unit control.
Do not infer that no character law exists on n=n0+kM; that narrower question remains open.
REOPEN_CONDITION:
Produce an exact normalized division-polynomial, EDS, sigma/formal-group-plus-global-normalization, or equivalent recurrence that computes the unit squareclass of C(nQ+epsilon*T) on the four live M3-T11-067 progressions. The proof must control normalization/cancellation, not only the local point in E2(Q_p)/E_1(Q_p).
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 75.
FLAGS:
M3_T11_X_27_OVER_40_REDUCTION_KERNEL_CHARACTER_SHORTCUT_REJECTED=true
M3_T11_X_27_OVER_40_NORMALIZED_DENOMINATOR_UNIT_REQUIRED=true
M3_T11_X_27_OVER_40_MW_LIVE_PROGRESSIONS=4
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40NormalizedDenominatorUnitRecurrenceOnFourMWSurvivorProgressions
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-068
