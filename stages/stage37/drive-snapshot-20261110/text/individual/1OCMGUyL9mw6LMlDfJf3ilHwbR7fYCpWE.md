# M3-T11-062 — Principal-factor product squareclass bridge for the x=27/40 translated lift

CARD_ID: M3-T11-062
CANONICAL_CARD_KEY: M3-T11-062
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-062
現行一覧の状態: PROVED_EXACT_STRUCTURE / GLOBAL_CLASSIFICATION_OPEN
種別: EXACT_STRUCTURE / THEOREM_GATE REFINEMENT
要点: In K=Q(sqrt(-14)), s=sqrt(-14), define alpha0=b+a*s, alpha-=50*a-b+4*b*s, alpha+=50*a+b+4*b*s. Then N(alpha0)=F0, N(alpha-)=25F-, N(alpha+)=25F+, and exactly alpha0*alpha-*alpha+ =
主張の抜粋: In K=Q(sqrt(-14)), s=sqrt(-14), define alpha0=b+a*s, alpha-=50*a-b+4*b*s, alpha+=50*a+b+4*b*s. Then N(alpha0)=F0, N(alpha-)=25F-, N(alpha+)=25F+, and exactly alpha0*alpha-*alpha+ = 25*(-R+I*s), with R=b*(124a^2+9b^2), I=a*(100a^2+7b^2). After the M3-T11-059 primitive normalization R=dR0, I=dI0 and R0=delta*u^2-(14/delt
対象・測度: Exact x=27/40 translated-lift carrier inherited from M3-T11-045 through M3-T11-061.
依存関係: M3-T11-058 principal norm forms; M3-T11-059 exact d normalization and four delta packets; elementary multiplication in Q(sqrt(-14)).
再開条件の抜粋: Compute the finite local element-squareclass possibilities of alpha0,alpha-,alpha+ above 2,3,5 for each d/delta profile, identify their images in the three M3-T11-048 packets, and intersect with M3-T11-057.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 69.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 723376
SOURCE_END: 727002
SOURCE_SHA256: 12fe06fd94adc9e19019cedcec25c21862bfa9ede714fade8ad8488484238330

## M3-T11-062
ID:
M3-T11-062
TYPE:
EXACT_STRUCTURE / THEOREM_GATE REFINEMENT
TITLE:
Principal-factor product squareclass bridge for the x=27/40 translated lift
STATUS:
PROVED_EXACT_STRUCTURE / GLOBAL_CLASSIFICATION_OPEN
CLAIM:
In K=Q(sqrt(-14)), s=sqrt(-14), define
alpha0=b+a*s,
alpha-=50*a-b+4*b*s,
alpha+=50*a+b+4*b*s.
Then
N(alpha0)=F0,
N(alpha-)=25F-,
N(alpha+)=25F+,
and exactly
alpha0*alpha-*alpha+
=
25*(-R+I*s),
with R=b*(124a^2+9b^2), I=a*(100a^2+7b^2).
After the M3-T11-059 primitive normalization R=dR0, I=dI0 and
R0=delta*u^2-(14/delta)*v^2,
I0=2uv,
delta in {1,2,7,14},
one has
alpha0*alpha-*alpha+
=
-25*d*delta*(u-(v/delta)*s)^2.
Hence
[alpha0*alpha-*alpha+]=[-d*delta]
in K^x/K^x2.
Because s^2=-14, [7]=[-2], so the four values of [-delta] are respectively
[-1],[-2],[2],[1].
Since d is supported on {2,3,5}, no moving prime outside {2,3,5} survives in the global element-squareclass.
Moreover the coefficient determinants of the three linear factors are
-106-s, -106+s, 100
with norms
11250,11250,10000.
Therefore the three principal factors are pairwise ideal-coprime away from primes above {2,3,5}. For every prime ideal away from {2,3,5,7}, its valuation in the unique alpha_j that contains it is even.
POPULATION:
Exact x=27/40 translated-lift carrier inherited from M3-T11-045 through M3-T11-061.
DEPENDS_ON:
M3-T11-058 principal norm forms;
M3-T11-059 exact d normalization and four delta packets;
elementary multiplication in Q(sqrt(-14)).
IMPLIES:
The M3-T11-061 residual moving split-prime allocation is finite-S at the element-squareclass level. The next non-duplicative task is a finite local match of the alpha_j squareclasses above 2,3,5 against the already-retained three rational packets of M3-T11-048, followed by the M3-T11-057 Mordell-Weil residue intersection.
ALIASES:
X27Over40PrincipalFactorProductSquareclass;
X27Over40FiniteSElementSquareclassMatchToThreePackets;
X27Over40GlobalMinusDDeltaSquareclass.
DUPLICATE_OF:
Not a duplicate of M3-T11-048: that card classifies rational norm-factor squareclasses after a 64-to-3 local descent. M3-T11-062 gives an element-level Q(sqrt(-14)) product identity and directly identifies the four delta-packet scalar class [-d*delta]. It is compatible with, and must be matched back to, M3-T11-048 rather than reopening it.
SUPERSEDES:
The wording in M3-T11-061 that leaves the residual split-prime allocation as an unstructured moving product problem. At element-squareclass level it is finite-S.
DO_NOT_REPEAT:
Do not restart arbitrary split-prime divisor allocation.
Do not rerun the old 64 rational S-squareclass search.
Do not infer rational-point classification or fixed-power saving from the finite-S element class alone.
REOPEN_CONDITION:
Compute the finite local element-squareclass possibilities of alpha0,alpha-,alpha+ above 2,3,5 for each d/delta profile, identify their images in the three M3-T11-048 packets, and intersect with M3-T11-057.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 69.
FLAGS:
M3_T11_X_27_OVER_40_PRINCIPAL_LINEAR_FACTOR_PRODUCT_IDENTITY=true
M3_T11_X_27_OVER_40_GLOBAL_ELEMENT_SQUARECLASS_MINUS_D_DELTA=true
M3_T11_X_27_OVER_40_SPLIT_PRIME_IDEAL_PARITY_FINITE_S=true
M3_T11_X_27_OVER_40_RAMIFIED7_NO_NEW_SQUARECLASS_GENERATOR=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40FiniteSElementSquareclassMatchToThreePackets
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-06
