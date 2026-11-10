# M3-T11-074 — X27Over40ShiftedEDSGenerator

CARD_ID: M3-T11-074
CANONICAL_CARD_KEY: M3-T11-074
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-074
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE / FIREWALL
要点: torsion-shifted p=3 EDS normalization closes the epsilon=1 reciprocal-root character
主張の抜粋: Let Q_T=Q+T=(11250,-1260000) on E2: V^2=U*(U^2+1244U+562500). On the epsilon=1 live Mordell-Weil classes n==+/-1 mod M, M=2656080, n is odd and nQ+T=nQ_T. The canonical positive root denominator C_n^T of U(nQ_T) is exactly the formerly open reciprocal denominator A_n/5. For W_n^T=psi_n(Q_T), the exact all-prime normali
対象・測度: Exact x=27/40 translated-lift carrier restricted to epsilon=1, n==+/-1 mod 2656080, together with the ambient rank-one Mordell-Weil progressions used by the retained sieve.
依存関係: M3-T11-066; M3-T11-067; M3-T11-069; M3-T11-070; M3-T11-071; M3-T11-072; M3-T11-073; the exact torsion identity U(P+T)=562500/U(P); the retained Silverman-Stephens EDS sign theorem.
再開条件の抜粋: Only reopen if the exact torsion-shift identity/root reduction, the shifted EDS normalization, or the retained EDS sign theorem application is retracted. Otherwise continue at the delta-resolved H*K/global packet.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 81.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 774160
SOURCE_END: 778496
SOURCE_SHA256: 4d62289910b1ef57faa4fb8d758e39b30760e035db700549e27ba719a19a1409

## M3-T11-074 — torsion-shifted p=3 EDS normalization closes the epsilon=1 reciprocal-root character
ID:
M3-T11-074


TYPE:
EXACT_STRUCTURE / FIREWALL


STATUS:
PROVED_EXACT


CLAIM:
Let Q_T=Q+T=(11250,-1260000) on
E2: V^2=U*(U^2+1244U+562500).
On the epsilon=1 live Mordell-Weil classes n==+/-1 mod M, M=2656080, n is odd and
nQ+T=nQ_T.
The canonical positive root denominator C_n^T of U(nQ_T) is exactly the formerly open reciprocal denominator A_n/5.


For W_n^T=psi_n(Q_T), the exact all-prime normalization is
|W_n^T|
=
C_n^T
*2^(5*R_n(1,2)+R_n(1,4))
*3^R_n(2,4)
*5^R_n(4,12)
*7^R_n(1,3).


At p=3, after unramified splitting of the nonsplit I_4 reduction and exact Tate-theta normalization,
W_n^T/3^R_n(2,4)
==(-1)^((n-1)/2) mod3
for every odd n.


Hence on n==n0 modM, n0 in {+1,-1},
(C_n^T|3)
=
rho_T(n0)*sign(W_n^T),
rho_T(+1)=+1,
rho_T(-1)=-1.


Because E2(R) is connected and Q_T is non-torsion, there are fixed sigma_T in {+1,-1} and irrational beta_T such that
sign(W_n^T)=sigma_T^(n-1)*(-1)^floor(n*beta_T).
Therefore
(A_n/5|3)
=
rho_T(n0)*sigma_T^(n-1)*(-1)^floor(n*beta_T)
on the epsilon=1 live classes.


Both p=3 character values occur infinitely often on each ambient epsilon=1 progression. The pointwise delta is
(C_n^T|3)=+1 => delta=7,
(C_n^T|3)=-1 => delta=2.


POPULATION:
Exact x=27/40 translated-lift carrier restricted to epsilon=1, n==+/-1 mod 2656080, together with the ambient rank-one Mordell-Weil progressions used by the retained sieve.


HEIGHT:
Inherited exact physical Stage37 height/reconstruction conditions. This card changes no height measure and gives no counting exponent by itself.


DEPENDS_ON:
M3-T11-066;
M3-T11-067;
M3-T11-069;
M3-T11-070;
M3-T11-071;
M3-T11-072;
M3-T11-073;
the exact torsion identity U(P+T)=562500/U(P);
the retained Silverman-Stephens EDS sign theorem.


IMPLIES:
The epsilon=1 reciprocal-root p=3 character gap is closed exactly.
Together with M3-T11-072 and M3-T11-073, all local character gaps on the four live MW progressions are closed.
The active first attack becomes the global intersection of the two exact Sturmian delta laws with the retained u*v=H*K, gcd(H,K)|7, principal-factor/squareclass packet.


ALIASES:
X27Over40ShiftedEDSGenerator;
X27Over40Epsilon1P3SturmianRootCharacter;
X27Over40ReciprocalRootP3Closure;
X27Over40TwoSturmianDeltaHKGlobalPacketIntersection.


DUPLICATE_OF:
none found under semantic rematch. M3-T11-072 controls the base-Q denominator only and explicitly leaves the epsilon=1 reciprocal-root sign open. M3-T11-066 supplies only the reciprocal coordinate transform. M3-T11-073 closes ramified-7 but leaves this p=3 gap open.


SUPERSEDES:
the unresolved epsilon=1 reciprocal-root p=3 subtask in M3-T11-072 and M3-T11-073.


DO_NOT_REPEAT:
Do not treat A_n/5 as an unresolved positive-numerator sign problem on the live epsilon=1 classes; it is the ordinary denominator C_n^T of n(Q+T).
Do not reopen p=2, p=5, p=7, or shifted p=3 valuation normalization.
Do not search for a constant p=3 character or constant delta on an ambient epsilon=1 M-progression; the exact Sturmian law takes both signs infinitely often.
Do not infer rational-point classification, fixed-power saving, theorem-gate closure, or P/M3 credit.


REOPEN_CONDITION:
Only reopen if the exact torsion-shift identity/root reduction, the shifted EDS normalization, or the retained EDS sign theorem application is retracted. Otherwise continue at the delta-resolved H*K/global packet.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 81.


FLAGS:
M3_T11_X_27_OVER_40_EPSILON1_SHIFTED_EDS_GENERATOR_EXACT=true
M3_T11_X_27_OVER_40_EPSILON1_SHIFTED_EDS_NORMALIZATION_EXACT=true
M3_T11_X_27_OVER_40_EPSILON1_P3_TROUBLEMAKER_R_2_4=true
M3_T11_X_27_OVER_40_EPSILON1_P3_NORMALIZED_UNIT_RESIDUE_EXACT=true
M3_T11_X_27_OVER_40_EPSILON1_ACTUAL_P3_ROOT_CHARACTER_PROVED=true
M3_T11_X_27_OVER_40_EPSILON1_P3_CHARACTER_STURMIAN=true
M3_T11_X_27_OVER_40_EPSILON1_P3_CHARACTER_NONCONSTANT_EACH_LIVE_PROGRESSION=true
M3_T11_X_27_OVER_40_LOCAL_CHARACTER_GAPS_CLOSED=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40TwoSturmianDeltaHKGlobalPacketIntersection
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_
---

## Retained LEDGER source 2
SOURCE_START: 790078
SOURCE_END: 790107
SOURCE_SHA256: 56d130aa5adf68f35f7e1b1fe7713bf250c73c3a78efd415d9bee38377d63813

RESEARCH_CARD=M3-T11-074
