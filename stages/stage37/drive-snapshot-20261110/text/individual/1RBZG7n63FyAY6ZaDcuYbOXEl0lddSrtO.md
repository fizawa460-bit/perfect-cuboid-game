# M3-T11-067 — Bad-prime denominator-order router, zero-coset closure, and Packet III d=225 removal

CARD_ID: M3-T11-067
CANONICAL_CARD_KEY: M3-T11-067
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-067
現行一覧の状態: PROVED_EXACT_STRUCTURE / ONE MW PROGRESSION CLOSED / GLOBAL CLASSIFICATION OPEN
種別: EXACT_LOCAL_STRUCTURE / MORDELL-WEIL SIEVE REFINEMENT
要点: Retain M3-T11-056/057/063/066. On
主張の抜粋: Retain M3-T11-056/057/063/066. On E2: V^2=U*(U^2+1244U+562500), Q=(50,5600), write U(nQ)=d0*(A_n/C_n)^2 with d0=2 for n odd, d0=1 for n even, A_n,C_n>0 and gcd(A_n,C_n)=1. The displayed model has c4=-2239424, a p-adic unit for p=3,5,7, hence is minimal at those primes. For E_1(Q_p), the kernel of reduction to O, p|C_n 
対象・測度: Exact x=27/40 translated-lift carrier restricted to the saturated E2 Mordell-Weil decomposition and the M3-T11-057 sieve certificate.
依存関係: M3-T11-056; M3-T11-057; M3-T11-063; M3-T11-066; exact multiplication on E2 through 12Q; the reduction-kernel criterion p|C_n iff nQ in E_1(Q_p).
再開条件の抜粋: Prove the exact global characters of the positive reduced denominator C(nQ+epsilon*T) at p=3,5,7 on the four live progressions and intersect them with (-1)^e2=(C|3), (-1)^e7=(-1)^n*(C|3)*(C|5), and, when v_7(U-2500)>=3, (C|7)=(-1)^n*(C|3)*(
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 74.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 743585
SOURCE_END: 747604
SOURCE_SHA256: fbea2c0dc95c512cd126910c6875b2ae4b2253be0a671e479fde8c858235bb1c

## M3-T11-067
ID:
M3-T11-067
TYPE:
EXACT_LOCAL_STRUCTURE / MORDELL-WEIL SIEVE REFINEMENT
TITLE:
Bad-prime denominator-order router, zero-coset closure, and Packet III d=225 removal
STATUS:
PROVED_EXACT_STRUCTURE / ONE MW PROGRESSION CLOSED / GLOBAL CLASSIFICATION OPEN
CLAIM:
Retain M3-T11-056/057/063/066. On
E2: V^2=U*(U^2+1244U+562500),
Q=(50,5600),
write
U(nQ)=d0*(A_n/C_n)^2
with d0=2 for n odd, d0=1 for n even, A_n,C_n>0 and gcd(A_n,C_n)=1.
The displayed model has c4=-2239424, a p-adic unit for p=3,5,7, hence is minimal at those primes. For E_1(Q_p), the kernel of reduction to O,
p|C_n iff nQ lies in E_1(Q_p).


Exact reduced root pairs are
(A_1,C_1)=(5,1),
(A_2,C_2)=(50,1),
(A_3,C_3)=(125,7),
(A_4,C_4)=(325,18),
(A_6,C_6)=(374,161),
(A_12,C_12)=(94480798816781,588799889370).
Therefore Q has exact order
4 in E2(Q_3)/E_1(Q_3),
12 in E2(Q_5)/E_1(Q_5),
3 in E2(Q_7)/E_1(Q_7),
and consequently
3|C_n iff 4|n,
5|C_n iff 12|n,
7|C_n iff 3|n.


Since M3-T11-057 has M=2656080 with 12|M, every nonzero n==0 mod M has 3|C_n, contradicting the exact translated-lift three-packet/root dictionary where every finite survivor has 3∤C. The n=0 representative is O and is non-affine. Hence the epsilon=0 zero progression is empty.


The only live M3-T11-057 progressions are therefore
epsilon=0, n==+/-2 mod M,
epsilon=1, n==+/-1 mod M.
For n==+/-2 mod M one has n==+/-2 mod12, so 5∤C_n. M3-T11-066 then forces Packet III common content d=9; the d=225 branch is absent from every live MW survivor. Hence on all four live progressions kappa5=(C|5), and the A-at-5 branch of M3-T11-066 is no longer needed.


POPULATION:
Exact x=27/40 translated-lift carrier restricted to the saturated E2 Mordell-Weil decomposition and the M3-T11-057 sieve certificate.
DEPENDS_ON:
M3-T11-056;
M3-T11-057;
M3-T11-063;
M3-T11-066;
exact multiplication on E2 through 12Q;
the reduction-kernel criterion p|C_n iff nQ in E_1(Q_p).
IMPLIES:
The live MW character intersection has four, not five, infinite progressions.
Packet III,d=225 is removed on the live sieve locus.
The remaining first attack needs only denominator characters C at 3,5,7; no numerator A-character at 5 is needed.
ALIASES:
X27Over40BadPrimeDenominatorOrderRouter;
X27Over40MWZeroCosetClosure;
X27Over40PacketIIID225RemovalOnMWSurvivors;
X27Over40DenominatorCharacterSequencesOnFourMWSurvivorProgressions.
DUPLICATE_OF:
none found under semantic rematch. M3-T11-057 leaves the zero progression live; M3-T11-066 explicitly retains a possible 5|C / d=225 / A-character branch. This card removes both using exact reduction-kernel orders.
DO_NOT_REPEAT:
Do not carry epsilon=0,n==0 mod M as a live progression.
Do not carry Packet III,d=225 into n==+/-2 mod M.
Do not ask for the M3-T11-066 A-at-5 character on the four live progressions.
Do not infer rational-point classification or theorem-gate closure from the four-progression reduction.
REOPEN_CONDITION:
Prove the exact global characters of the positive reduced denominator C(nQ+epsilon*T) at p=3,5,7 on the four live progressions and intersect them with
(-1)^e2=(C|3),
(-1)^e7=(-1)^n*(C|3)*(C|5),
and, when v_7(U-2500)>=3,
(C|7)=(-1)^n*(C|3)*(C|5).
A successful elliptic-log height bound or split-Jacobian quadratic-Chabauty classification remains an independent acceptable closure.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 74.
FLAGS:
M3_T11_X_27_OVER_40_BAD_PRIME_DENOMINATOR_ORDERS_EXACT=true
M3_T11_X_27_OVER_40_MW_ZERO_COSET_CLOSED=true
M3_T11_X_27_OVER_40_MW_LIVE_PROGRESSIONS=4
M3_T11_X_27_OVER_40_PACKET_III_D225_REMOVED_ON_MW_SURVIVORS=true
M3_T11_X_27_OVER_40_KAPPA5_DENOMINATOR_ONLY_ON_MW_SURVIVORS=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40DenominatorCharacterSequencesOnFourMWSurvivorProgressions
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-067
