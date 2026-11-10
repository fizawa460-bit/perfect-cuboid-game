# M3-T11-078 — Finite-S root-denominator squareclasses reduce to finitely many square power-integral elliptic points

CARD_ID: M3-T11-078
CANONICAL_CARD_KEY: M3-T11-078
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-078
現行一覧の状態: PROVED_THEOREM_ADAPTER / HOSTILE_AUDIT_PASS / QUALITATIVE_FINITE_SUPPORT
種別: THEOREM_ADAPTER / POWER_INTEGRAL_FINITE_S_DENOMINATOR / MORDELL_WEIL_FINITE_INDEX
要点: Finite-S root-denominator squareclasses reduce to finitely many square power-integral elliptic points.
主張の抜粋: If sf(C)|210, write C=d*z^2 with squarefree d|210. Scaling E2 by (U,V)->(d^2 U,d^3 V) gives one of 16 fixed Q-isomorphic curves and standard root denominator z^2. Everest-Reynolds-Stevens fixed-f=2 denominator finiteness therefore makes the E2 point set finite. Via M3-T11-077, even one H-neighbor condition forces only finitely many MW indices; the dual-H set is finite a fortiori.
対象・測度: General: finite rational points on fixed E2 with canonical root denominator squarefree kernel supported on {2,3,5,7}. Frontier application: exact x=27/40 translated-lift survivor locus on the four live MW progressions.
依存関係: M3-T11-066; audited M3-T11-077/M3-T11-076; Everest-Reynolds-Stevens BLMS 39 (2007), DOI 10.1112/blms/bdm061.
再開条件の抜粋: Reopen only if the 076/077 denominator router changes, the standard root-denominator scaling fails, or the fixed-f=2 denominator theorem is inapplicable to one of the 16 fixed scaled curves.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 86.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 802086
SOURCE_END: 806578
SOURCE_SHA256: 3f3336e4e8ea096fb0de64817d8475d04d46f7d521be9fb05cc5a5e3e65af0d6

## M3-T11-078
ID:
M3-T11-078
TYPE:
THEOREM_ADAPTER / POWER_INTEGRAL_FINITE_S_DENOMINATOR / MORDELL_WEIL_FINITE_INDEX
TITLE:
Finite-S root-denominator squareclasses reduce to finitely many square power-integral elliptic points
STATUS:
PROVISIONAL_EXACT / AUDIT_PENDING
CLAIM:
Retain
E2: V^2=U*(U^2+1244*U+562500)
and write every finite rational point in standard denominator form
U=N/C^2,
C>0,
gcd(N,C)=1.
Let S={2,3,5,7}. If sf(C)|210, write uniquely
C=d*z^2
with d squarefree and d|210.
For this d define the Q-isomorphic integral elliptic curve
E2^(d): Y_d^2=X_d^3+1244*d^2*X_d^2+562500*d^4*X_d
and
phi_d(U,V)=(d^2*U,d^3*V).
Then exactly
X_d=N/z^4.
Because gcd(N,z)=1, the standard root denominator of phi_d(P) is z^2, an exact square.
Everest-Reynolds-Stevens, On the denominators of rational points on elliptic curves, BLMS 39 (2007), 762-770, DOI 10.1112/blms/bdm061, prove that for a fixed exponent f>1 and a fixed elliptic curve in Weierstrass form there are only finitely many rational points whose root denominator is an f-th power. Applying f=2 to each E2^(d), and noting that there are only 16 squarefree d|210, gives
{P in E2(Q): sf(C_P)|210}
finite.
M3-T11-077 therefore has a qualitative global finiteness consequence: every actual x=27/40 survivor places both H-neighbors P_{n-2,epsilon},P_{n+2,epsilon} in this fixed finite set. Since Q has infinite order, for fixed epsilon the map m -> mQ+epsilon*T is injective. Hence even one H-neighbor finite-S square-denominator condition already restricts n to a finite set; the simultaneous dual-H condition is finite a fortiori.
POPULATION:
General theorem: all finite rational points on the fixed elliptic quotient E2 with canonical standard root denominator C.
Frontier application: exact canonical x=27/40 translated-lift three-packet survivor locus on the four live Mordell-Weil progressions.
HEIGHT:
Set-theoretic finiteness; independent of B. The invoked Faltings-based theorem is ineffective here and supplies no explicit list or height cutoff.
DEPENDS_ON:
M3-T11-066 canonical root-denominator dictionary;
M3-T11-077 and therefore provisional M3-T11-076 for the survivor-locus application;
Everest-Reynolds-Stevens denominator perfect-power finiteness theorem.
IMPLIES:
The qualitative H-side problem after M3-T11-077 is no longer an open density/primitive-divisor heuristic: the allowed Mordell-Weil index set is finite.
The next legal task is to audit the M3-T11-076 -> 077 -> 078 chain and then check the exact same-measure physical reconstruction/multiplicity consequence. Effective enumeration of the finite set is a separate optional task if an explicit classification is required.
ALIASES:
X27Over40FiniteSSquareDenominatorPowerIntegralFiniteness;
X27Over40HNeighborPowerIntegralScaling;
FiniteSSquareKernelRootDenominatorFiniteness.
DUPLICATE_OF:
none found under semantic rematch. Existing Faltings warnings concern moving families/fibers. Here E2 is fixed and only 16 fixed Q-isomorphic scaled models occur, so there is no moving-curve summation.
SUPERSEDES:
the need to prove qualitative finiteness of the M3-T11-077 H-side by an independence heuristic, a primitive-divisor density estimate, or a new EDS perfect-power theorem. It does not supersede effective classification or the remaining K-side u/v allocation.
DO_NOT_REPEAT:
Do not multiply the two H-neighbor conditions as independent probabilities.
Do not claim that Everest-Reynolds-Stevens gives an effective list in the general Faltings branch.
Do not identify finiteness of the H-neighbor Mordell-Weil index set with a completed rational-point classification of the full Stage37 problem.
Do not promote a fixed-power saving, primary theorem-gate closure, or P(B)/M3(B) credit until the provisional 076/077 dependency and exact physical counting adapter are audited.
REOPEN_CONDITION:
Retract or change M3-T11-077/M3-T11-076, or exhibit a failure of the exact scaling/root-denominator calculation or of the applicability of the fixed-f=2 denominator theorem to one of the 16 fixed curves E2^(d).
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 86.
FLAGS:
M3_T11_X_27_OVER_40_H_NEIGHBOR_FINITE_S_ROOT_DENOMINATOR_SET_FINITE=PROVISIONAL
M3_T11_X_27_OVER_40_DUAL_H_NEIGHBOR_MW_INDEX_SET_FINITE=PROVISIONAL
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40FiniteSSquareDenominatorPowerIntegralFinitenessAudit
RESEARCH_CARD=M3-T11-078
