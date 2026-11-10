# M3-T11-071 — The p=5 denominator character is +1 on all four live Mordell-Weil progressions, including the torsion-shifted branches

CARD_ID: M3-T11-071
CANONICAL_CARD_KEY: M3-T11-071
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-071
現行一覧の状態: PROVED_EXACT_P5_CHARACTER / ACTIVE CONTINUATION
種別: EXACT_LOCAL_STRUCTURE / MORDELL-WEIL CHARACTER INTERSECTION / THEOREM-GATE REFINEMENT
要点: Retain M3-T11-066 through M3-T11-070. Let M=2656080 and let the four live translated-lift progressions be epsilon=0, n==+/-2 mod M, epsilon=1, n==+/-1 mod M. For the base points nQ
主張の抜粋: Retain M3-T11-066 through M3-T11-070. Let M=2656080 and let the four live translated-lift progressions be epsilon=0, n==+/-2 mod M, epsilon=1, n==+/-1 mod M. For the base points nQ, use the split multiplicative Tate model at p=5. The reduction is the split nodal cubic V^2=U^2(U-1), v_5(Delta)=12, and the Tate parameter
対象・測度: The exact x=27/40 translated-lift carrier restricted to the four M3-T11-067 live Mordell-Weil progressions.
依存関係: M3-T11-066; M3-T11-067; M3-T11-069; M3-T11-070; Stange 2016, Tate theta identity (9.3) and split multiplicative parametrization; exact E2 invariants and W_2=11200.
再開条件の抜粋: Only if the split multiplicative Tate identification at p=5, the M3-T11-070 normalization, or the M3-T11-066 torsion-root reciprocity is retracted. Otherwise continue with p=3 and ramified-7 compatibility, or either retained global closure 
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 78.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 759805
SOURCE_END: 764547
SOURCE_SHA256: 95d92f3c3b95d920492fa3dfc4fdcefdb9b0d592795ee01b88e5ce4f5fdcab47

## M3-T11-071
ID:
M3-T11-071
TYPE:
EXACT_LOCAL_STRUCTURE / MORDELL-WEIL CHARACTER INTERSECTION / THEOREM-GATE REFINEMENT
TITLE:
The p=5 denominator character is +1 on all four live Mordell-Weil progressions, including the torsion-shifted branches
STATUS:
PROVED_EXACT_P5_CHARACTER / ACTIVE CONTINUATION
CLAIM:
Retain M3-T11-066 through M3-T11-070. Let M=2656080 and let the four live translated-lift progressions be
epsilon=0, n==+/-2 mod M,
epsilon=1, n==+/-1 mod M.
For the base points nQ, use the split multiplicative Tate model at p=5. The reduction is the split nodal cubic V^2=U^2(U-1), v_5(Delta)=12, and the Tate parameter q=5^12*q0 has q0==1 mod5. Choosing component valuation a=2 and applying Stange's Tate theta identity, the normalized EDS unit satisfies, for 6 not dividing n,
( W_n/5^R_n(2,12) | 5 )
=
L^(n^2-1)*U0^[n(n-1)/2-n*floor(n/6)],
where L and U0 are the two unit squareclasses coming from the minimal Tate isomorphism and the Tate point parameter. The exact value W_2/5^2=448==3 mod5 gives L*U0=-1. Hence the normalized EDS unit has character +1 on n==+/-1 mod M and -1 on n==+/-2 mod M.
Combining this with M3-T11-070,
|W_n|=C_n*2^e2(n)*5^R_n(2,12)*7^R_n(1,3),
with e2 even on all four live classes and R_n(1,3) even on +/-1 but odd on +/-2, gives
boxed:
(C_n|5)=+1
for the canonical denominator of U(nQ) on all n==+/-1,+/-2 mod M.
For epsilon=1 the actual translated-lift point is nQ+T, so the M3-T11-066 reciprocal root transform must still be applied. On n==+/-1 mod M, Tate continuity and 5|(M/12) give
U(nQ)/25 == U(+/-Q)/25 ==2 mod5.
Thus v_5(A_n)=1 and
(A_n/5)^2*C_n^(-2)==1 mod5,
so (A_n/5|5)=(C_n|5)=+1. At p=3, n==+/-1 mod4 has the same nonsingular reduction as +/-Q with x==2 mod3, so 3 does not divide A_n. Therefore gcd(A_n,375)=5 and the torsion-shifted canonical denominator is exactly A_n/5. It also has character +1.
Consequently, on the actual four translated-lift progressions,
boxed:
kappa5=(C|5)=+1.
The M3-T11-066 delta router collapses to
(-1)^e2=(C|3),
(-1)^e7=(-1)^n*(C|3).
Thus:
- epsilon=0, n even, Packet III,d=9: (C|3)=+1 gives delta=1, while (C|3)=-1 gives delta=14;
- epsilon=1, n odd, Packets I/II: (C|3)=+1 gives delta=7, while (C|3)=-1 gives delta=2.
POPULATION:
The exact x=27/40 translated-lift carrier restricted to the four M3-T11-067 live Mordell-Weil progressions.
DEPENDS_ON:
M3-T11-066;
M3-T11-067;
M3-T11-069;
M3-T11-070;
Stange 2016, Tate theta identity (9.3) and split multiplicative parametrization;
exact E2 invariants and W_2=11200.
IMPLIES:
The p=5 unit-character branch is closed, including epsilon=1 torsion reciprocity. The local delta packet is now determined entirely by the p=3 denominator character. The first attack reduces to the p=3 denominator character on the four live progressions and the retained ramified-7 compatibility condition.
ALIASES:
X27Over40P5DenominatorCharacterAllLivePlus;
X27Over40TateThetaP5CharacterClosure;
X27Over40P5TorsionShiftCharacterClosure;
X27Over40DeltaReducedToP3Character.
DUPLICATE_OF:
none found under semantic rematch. M3-T11-068 explicitly leaves global denominator-unit characters open, while M3-T11-069/070 close valuation normalization only. This card uses the split Tate theta unit, not reduction-kernel periodicity, and separately transports the result through the epsilon=1 reciprocal root map.
DO_NOT_REPEAT:
Do not reopen the p=5 denominator character on any of the four live progressions.
Do not confuse the base denominator C_n of U(nQ) with the epsilon=1 translated denominator; the latter is covered by the exact gcd=5 reciprocal step above.
Do not infer the p=3 character or the ramified-7 condition from this p=5 closure.
Do not promote rational-point classification, fixed-power saving, primary theorem-gate closure, or P/M3 credit.
REOPEN_CONDITION:
Only if the split multiplicative Tate identification at p=5, the M3-T11-070 normalization, or the M3-T11-066 torsion-root reciprocity is retracted. Otherwise continue with p=3 and ramified-7 compatibility, or either retained global closure route.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 78.
FLAGS:
M3_T11_X_27_OVER_40_P5_DENOMINATOR_CHARACTER_ALL_LIVE_PLUS=true
M3_T11_X_27_OVER_40_P5_TORSION_SHIFT_CHARACTER_CLOSED=true
M3_T11_X_27_OVER_40_DELTA_REDUCED_TO_P3_CHARACTER=true
M3_T11_X_27_OVER_40_NORMALIZED_UNIT_RECURRENCE_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40P3DenominatorCharacterThenRamified7CompatibilityOnFourMWSurvivorProgressions
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-071
