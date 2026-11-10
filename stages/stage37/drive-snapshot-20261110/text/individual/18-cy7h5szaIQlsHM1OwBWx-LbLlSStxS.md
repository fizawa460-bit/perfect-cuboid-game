# M3-T11-057 — Exact Mordell-Weil sieve compression for the x=27/40 translated lift

CARD_ID: M3-T11-057
CANONICAL_CARD_KEY: M3-T11-057
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-057
現行一覧の状態: PROVED_EXACT_FINITE_SIEVE / GLOBAL_CLASSIFICATION_OPEN
種別: THEOREM / FIREWALL
要点: With E2(Q)=<Q> direct-sum <T>, Q=(50,5600), T=(0,0), write every rational point uniquely as R=nQ+epsilon*T. For the translated-lift condition U(R)-2500=14*r^2, the exact finite loc
主張の抜粋: With E2(Q)=<Q> direct-sum <T>, Q=(50,5600), T=(0,0), write every rational point uniquely as R=nQ+epsilon*T. For the translated-lift condition U(R)-2500=14*r^2, the exact finite local Mordell-Weil sieve with modulus M=2656080 forces epsilon=0 => n == 0,+/-2 mod M, epsilon=1 => n == +/-1 mod M. The only small representat
対象・測度: Exact x=27/40 singular physical carrier inherited from M3-T11-045 through M3-T11-056.
依存関係: M3-T11-050; M3-T11-051; M3-T11-056; exact finite-field reduction of E2 and the translated squareclass condition.
再開条件の抜粋: Prove a rigorous coefficient bound |n|<1328040 for all translated-lift points by elliptic logarithms/heights, or execute the retained split-Jacobian quadratic-Chabauty computation to classify the genus-two rational points.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 64.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 707079
SOURCE_END: 710096
SOURCE_SHA256: b503509a99818671718e10e85b7e288d9a4bb0000fa19166c283ac5a884f9108

## M3-T11-057
ID:
M3-T11-057
TYPE:
THEOREM / FIREWALL
TITLE:
Exact Mordell-Weil sieve compression for the x=27/40 translated lift
STATUS:
PROVED_EXACT_FINITE_SIEVE / GLOBAL_CLASSIFICATION_OPEN
CLAIM:
With
E2(Q)=<Q> direct-sum <T>,
Q=(50,5600), T=(0,0),
write every rational point uniquely as R=nQ+epsilon*T.
For the translated-lift condition
U(R)-2500=14*r^2,
the exact finite local Mordell-Weil sieve with modulus
M=2656080
forces
epsilon=0 => n == 0,+/-2 mod M,
epsilon=1 => n == +/-1 mod M.
The only small representatives are the elliptic identity, the boundary pair +/-2Q at U=2500, and the known finite boundary-preimage pair +/-Q+T at U=11250.
POPULATION:
Exact x=27/40 singular physical carrier inherited from M3-T11-045 through M3-T11-056.
HEIGHT:
Exact physical R<=B remains inherited. This card itself is a fixed-curve rational-point sieve.
DEPENDS_ON:
M3-T11-050;
M3-T11-051;
M3-T11-056;
exact finite-field reduction of E2 and the translated squareclass condition.
CERTIFICATE:
M=2656080=2^4*3^2*5*7*17*31.
Using all good p<2000 with ord_p(Q)|M leaves
epsilon=0: {0,2,771118,1884962,2656078},
epsilon=1: {1,342721,2313359,2656079}.
Then p=2267, ord_p(Q)=1116, eliminates the two extra epsilon=0 classes.
p=2551, ord_p(Q)=1302, eliminates the two extra epsilon=1 classes.
IMPLIES:
Any additional rational translated-lift point must have Mordell-Weil coefficient in one of the same five residue classes modulo M as the known affine/boundary classes. A proof that every translated-lift solution satisfies |n|<M/2 would therefore complete the rational-point classification on this branch.
ALIASES:
X27Over40TorsionNormalizedTranslatedLiftMordellWeilSieve;
X27Over40KnownSolutionResidueClassCertificate;
X27Over40EllipticLogHeightReductionBelow1328040.
DUPLICATE_OF:
none.
SUPERSEDES:
the unspecialized instruction to begin the x=27/40 branch with a broad finite-prime Mordell-Weil sieve after saturation.
DO_NOT_REPEAT:
Do not claim global rational-point classification from a finite congruence sieve.
Do not restart blind local-prime accumulation without a height/elliptic-log reduction target.
Do not charge endpoint or fixed-power saving from the residue-class compression alone.
REOPEN_CONDITION:
Prove a rigorous coefficient bound |n|<1328040 for all translated-lift points by elliptic logarithms/heights, or execute the retained split-Jacobian quadratic-Chabauty computation to classify the genus-two rational points.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 64.
FLAGS:
M3_T11_X_27_OVER_40_MW_SIEVE_MODULUS=2656080
M3_T11_X_27_OVER_40_MW_SIEVE_KNOWN_CLASSES_ONLY=true
M3_T11_X_27_OVER_40_MW_SIEVE_GLOBAL_CLASSIFICATION=false
M3_T11_X_27_OVER_40_ELLIPTIC_LOG_HEIGHT_BOUND_LT_M_OVER_2_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_SECOND_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-057
