# M3-T11-073 — Ramified-7 is exactly routed on the four live Mordell-Weil progressions and its compatibility is automatic

CARD_ID: M3-T11-073
CANONICAL_CARD_KEY: M3-T11-073
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-073
現行一覧の状態: PROVED_EXACT / RAMIFIED-7 SUBROUTE CLOSED / GLOBAL CLASSIFICATION OPEN
種別: EXACT_LOCAL_STRUCTURE / FIREWALL / THEOREM_GATE REFINEMENT
要点: Retain M3-T11-066 through M3-T11-072. On
主張の抜粋: Retain M3-T11-066 through M3-T11-072. On E2: V^2=U*(U^2+1244U+562500), Q=(50,5600), T=(0,0), M=2656080, the four live translated-lift progressions are epsilon=0, n==+/-2 mod M, epsilon=1, n==+/-1 mod M. The M3-T11-066 ramified condition 7|a iff v_7(U(nQ+epsilon*T)-2500)>=3 is routed exactly as follows: - on both epsilo
対象・測度: Exact x=27/40 translated-lift carrier restricted to the four M3-T11-067 Mordell-Weil progressions.
依存関係: M3-T11-066; M3-T11-067; M3-T11-069; M3-T11-070; M3-T11-071; M3-T11-072; exact points Q, 2Q, 3Q; 7-adic formal group on E2; split Tate theta normalization at p=7.
再開条件の抜粋: Only reopen ramified-7 if one of the exact inputs M3-T11-066/067/069/070/071/072 or the formal/Tate calculation in this card is retracted. Otherwise continue with the delta-resolved H*K/global packet, with the epsilon=1 reciprocal-root p=3 
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 80.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 769408
SOURCE_END: 774160
SOURCE_SHA256: 4b1718566d97900a3b7501c6bdf0d934d044871457bda31f0c0cf10dd199e37a

## M3-T11-073
ID:
M3-T11-073
TYPE:
EXACT_LOCAL_STRUCTURE / FIREWALL / THEOREM_GATE REFINEMENT
TITLE:
Ramified-7 is exactly routed on the four live Mordell-Weil progressions and its compatibility is automatic
STATUS:
PROVED_EXACT / RAMIFIED-7 SUBROUTE CLOSED / GLOBAL CLASSIFICATION OPEN


CLAIM:
Retain M3-T11-066 through M3-T11-072. On
E2: V^2=U*(U^2+1244U+562500),
Q=(50,5600),
T=(0,0),
M=2656080,
the four live translated-lift progressions are
epsilon=0, n==+/-2 mod M,
epsilon=1, n==+/-1 mod M.


The M3-T11-066 ramified condition
7|a iff v_7(U(nQ+epsilon*T)-2500)>=3
is routed exactly as follows:
- on both epsilon=0 progressions it is always true;
- on both epsilon=1 progressions it is always false.


More precisely, with z=-U/V,
z(3Q)=-7/368 and
v_7(z(mQ))=1+v_7(m)
for nonzero 3|m.
The exact translated formal expansions imply
v_7(U(nQ)-2500)=2+v_7(n-2)
for n==2 mod3, n!=2,
and
v_7(U(nQ)-2500)=2+v_7(n+2)
for n==1 mod3, n!=-2,
with +infinity at n=+/-2.
Since 7|M, epsilon=0 is therefore always ramified.


For epsilon=1, the +/-Q expansion gives
v_7(U(nQ)-225)=1.
Using U(nQ+T)=562500/U(nQ),
one gets exactly
v_7(U(nQ+T)-2500)=1,
so epsilon=1 is never ramified.


On the two epsilon=0 progressions the compatibility itself is also automatic. At p=7 the model has split multiplicative type I_3 and Tate unit
q/7^3 == -1 mod7.
Tate-theta normalization gives
chi_7(W_n/7^R_n(1,3))=+1
for n==+2 mod M,
and
chi_7(W_n/7^R_n(1,3))=-1
for n==-2 mod M.
After the already-closed global normalization,
(C_n|7)=rho7(n0)*sign(W_n),
rho7(+2)=+1,
rho7(-2)=-1.
M3-T11-072 gives
(C_n|3)=rho3(n0)*sign(W_n)
with the identical rho3 values. Hence
(C_n|7)=(C_n|3)
identically on both even live progressions, exactly matching the M3-T11-066 ramified relation because n is even and M3-T11-071 gives kappa5=+1.


Therefore ramified-7 contributes no additional pruning on the four live progression sieve locus and is removed from the unresolved first attack.


POPULATION:
Exact x=27/40 translated-lift carrier restricted to the four M3-T11-067 Mordell-Weil progressions.


DEPENDS_ON:
M3-T11-066;
M3-T11-067;
M3-T11-069;
M3-T11-070;
M3-T11-071;
M3-T11-072;
exact points Q, 2Q, 3Q;
7-adic formal group on E2;
split Tate theta normalization at p=7.


IMPLIES:
The first attack splits cleanly:
- epsilon=0: use the M3-T11-072 Sturmian p=3 character and its delta in {1,14} directly in the delta-resolved H*K/global packet; there is no independent ramified-7 filter left.
- epsilon=1: ramified-7 is absent; determine the actual reciprocal-root p=3 character of A_n/5, then use delta in {7,2} in the same global packet.


ALIASES:
X27Over40Ramified7LiveProgressionRouter;
X27Over40Ramified7CompatibilityAutomaticEven;
X27Over40P7P3SignedEDSMatch;
X27Over40SturmianDeltaHKIntersectionWithEpsilon1TorsionRootSign.


DUPLICATE_OF:
none found under semantic rematch. M3-T11-066 identifies the generic ramified condition and compatibility but does not decide whether it occurs on the four M3-T11-067 progressions. M3-T11-069 gives only valuation normalization, and M3-T11-072 treats p=3, not the p=7 Tate-unit compatibility.


DO_NOT_REPEAT:
Do not carry ramified-7 as an unresolved obstruction on the four live M3-T11-067 progressions.
Do not search for a ramified-7 condition on epsilon=1; it is exactly absent.
Do not claim the epsilon=0 ramified relation prunes points; it is an identity after the p=7 and p=3 normalized EDS laws are matched.
Do not reopen p=5 or any valuation-normalization work.
Do not infer rational-point classification, fixed-power saving, primary theorem-gate closure, or P/M3 credit.


REOPEN_CONDITION:
Only reopen ramified-7 if one of the exact inputs M3-T11-066/067/069/070/071/072 or the formal/Tate calculation in this card is retracted. Otherwise continue with the delta-resolved H*K/global packet, with the epsilon=1 reciprocal-root p=3 sign as the remaining local-character gap.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 80.


FLAGS:
M3_T11_X_27_OVER_40_RAMIFIED7_LIVE_ROUTER_PROVED=true
M3_T11_X_27_OVER_40_RAMIFIED7_EPSILON0_ALWAYS=true
M3_T11_X_27_OVER_40_RAMIFIED7_EPSILON1_NEVER=true
M3_T11_X_27_OVER_40_P7_SIGNED_EDS_UNIT_EVEN_LAW=true
M3_T11_X_27_OVER_40_RAMIFIED7_COMPATIBILITY_AUTOMATIC_EVEN=true
M3_T11_X_27_OVER_40_RAMIFIED7_ADDS_NO_PRUNING_ON_FOUR_LIVE=true
M3_T11_X_27_OVER_40_EPSILON1_ACTUAL_P3_ROOT_CHARACTER_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40SturmianDeltaHKIntersectionWithEpsilon1TorsionRootSign
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-073
