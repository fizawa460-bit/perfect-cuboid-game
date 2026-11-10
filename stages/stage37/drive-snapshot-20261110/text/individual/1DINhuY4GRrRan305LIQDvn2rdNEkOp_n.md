# M3-T11-061 — K-side biquadratic split filter and exact ramified-7 routing

CARD_ID: M3-T11-061
CANONICAL_CARD_KEY: M3-T11-061
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-061
現行一覧の状態: PROVED_EXACT_STRUCTURE / GLOBAL_CLASSIFICATION_OPEN
種別: EXACT_STRUCTURE / THEOREM_GATE REFINEMENT
要点: Retain M3-T11-059/060, with J=100*a^2+7*b^2 and u*v=H*K, gcd(H,K)|7. For every odd fresh prime p notin {2,3,5,7} dividing K, primitiveness gives p∤a*b and p|J, hence (10*a/b)^2 == 
主張の抜粋: Retain M3-T11-059/060, with J=100*a^2+7*b^2 and u*v=H*K, gcd(H,K)|7. For every odd fresh prime p notin {2,3,5,7} dividing K, primitiveness gives p∤a*b and p|J, hence (10*a/b)^2 == -7 (mod p). Therefore Legendre_p(-7)=+1 and on K-side Legendre_p(-14)=Legendre_p(2). Thus K-side fresh primes are split/locally ambiguous ex
対象・測度: Exact x=27/40 translated-lift carrier inherited from M3-T11-045 through M3-T11-060, excluding the already-handled boundary for fresh-prime statements.
依存関係: M3-T11-059; M3-T11-060; J=100*a^2+7*b^2; gcd(a,b)=1; support(d) subset {2,3,5}; the four exact delta packets.
再開条件の抜粋: Derive a global product/squareclass constraint on the remaining H-split and K-biquadratic-split parts strong enough to reduce the four delta packets to finitely solvable lower-genus/Thue/elliptic cases, then intersect with M3-T11-057.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 68.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 719848
SOURCE_END: 723376
SOURCE_SHA256: 65e4ba5124a0f632f6fa42418d6617b7f53b8aa8d1fbf7d792e21824be6949f4

## M3-T11-061
ID:
M3-T11-061
TYPE:
EXACT_STRUCTURE / THEOREM_GATE REFINEMENT
TITLE:
K-side biquadratic split filter and exact ramified-7 routing
STATUS:
PROVED_EXACT_STRUCTURE / GLOBAL_CLASSIFICATION_OPEN
CLAIM:
Retain M3-T11-059/060, with J=100*a^2+7*b^2 and u*v=H*K, gcd(H,K)|7.


For every odd fresh prime p notin {2,3,5,7} dividing K, primitiveness gives p∤a*b and p|J, hence
(10*a/b)^2 == -7 (mod p).
Therefore
Legendre_p(-7)=+1
and on K-side
Legendre_p(-14)=Legendre_p(2).
Thus K-side fresh primes are split/locally ambiguous exactly when p==1 or 7 mod 8, and inert/deterministically routed exactly when p==3 or 5 mod 8. Equivalently, after combining with Legendre_p(-7)=+1:
K-side split/ambiguous classes mod 56 are
{1,9,15,23,25,39},
while K-side inert/deterministic classes mod 56 are
{11,29,37,43,51,53}.


The ramified prime 7 is also exact. If 7∤a then 7∤J and gcd(H,K)=1. If 7|a with h=v_7(a)>=1, then v_7(J)=1, v_7(H)=h, v_7(K)=1, so gcd(H,K)=7 and all 7^(h+1) in u*v lies on exactly one of u,v. In the four delta packets:
delta in {1,2} forces all 7-power into v and Legendre_7(b/d)=+1;
delta in {7,14} forces all 7-power into u and Legendre_7(b/d)=-1.
Hence 7 is not a free exceptional allocation prime.


POPULATION:
Exact x=27/40 translated-lift carrier inherited from M3-T11-045 through M3-T11-060, excluding the already-handled boundary for fresh-prime statements.
DEPENDS_ON:
M3-T11-059;
M3-T11-060;
J=100*a^2+7*b^2;
gcd(a,b)=1;
support(d) subset {2,3,5};
the four exact delta packets.
IMPLIES:
The residual split-prime problem is narrower than M3-T11-060: unresolved allocation freedom remains only on H-side primes split in Q(sqrt(-14)), K-side primes in the six biquadratic split classes {1,9,15,23,25,39} mod 56, and finite 2,3,5 normalization data. The ramified prime 7 is completely routed.
ALIASES:
X27Over40KSideBiquadraticSplitFilter;
X27Over40Ramified7ExactRouting;
X27Over40KSplitMod56SixClasses.
DUPLICATE_OF:
none found under semantic rematch of the active ROUTE and RESULT-LEDGER; M3-T11-060 only distinguishes Q(sqrt(-14)) inert versus split and leaves split primes plus {2,3,5,7} residual.
SUPERSEDES:
the part of M3-T11-060 that treats 7 as residual allocation freedom and treats all K-side Q(sqrt(-14))-split primes as equally ambiguous.
DO_NOT_REPEAT:
Do not infer that H-side split primes satisfy Legendre_p(-7)=+1.
Do not promote the six K-side residue classes to a rational-point classification.
Do not charge fixed-power or P/M3 credit from this structural refinement.
REOPEN_CONDITION:
Derive a global product/squareclass constraint on the remaining H-split and K-biquadratic-split parts strong enough to reduce the four delta packets to finitely solvable lower-genus/Thue/elliptic cases, then intersect with M3-T11-057.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 68.
FLAGS:
M3_T11_X_27_OVER_40_K_FRESH_MINUS7_SPLIT=true
M3_T11_X_27_OVER_40_K_SPLIT_EQ_TWO_CHARACTER=true
M3_T11_X_27_OVER_40_K_SPLIT_MOD56_SIX_CLASSES=true
M3_T11_X_27_OVER_40_RAMIFIED7_ROUTING_EXACT=true
M3_T11_X_27_OVER_40_GCD_HK_EXACT_ONE_OR_SEVEN=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40SplitPrimeResidualGlobalSquareclass
CURRENT_X27_FIRST_SUBATTACK=X27Over40KSideBiquadraticSplitFilterAndRamified7Routing
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-06
