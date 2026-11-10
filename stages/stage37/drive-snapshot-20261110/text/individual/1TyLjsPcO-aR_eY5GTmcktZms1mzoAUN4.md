# M3-T11-058 — Translated-lift common Q(sqrt(-14)) norm factorization

CARD_ID: M3-T11-058
CANONICAL_CARD_KEY: M3-T11-058
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-058
現行一覧の状態: PROVED_EXACT_STRUCTURE / RATIONAL-POINT CLASSIFICATION OPEN
種別: EXACT_STRUCTURE / THEOREM_GATE
要点: On the saturated x=27/40 E2 branch,
主張の抜粋: On the saturated x=27/40 E2 branch, E2: V^2=U*(U^2+1244U+562500), the translated-lift condition U-2500=14*r^2 may be parameterized by r=50m, U=2500+35000m^2. Direct substitution gives V^2=17500^2*(1+14m^2)*(100m^2-4m+9)*(100m^2+4m+9). For m=a/b in lowest terms, F0=b^2+14a^2, F-=100a^2-4ab+9b^2, F+=100a^2+4ab+9b^2, and 
対象・測度: Exact x=27/40 singular physical carrier inherited from M3-T11-045 through M3-T11-057.
依存関係: M3-T11-056; M3-T11-057; exact conic parameterization of U-2500=14r^2; exact polynomial factorization and resultant identities.
再開条件の抜粋: Classify the finite ideal/squareclass packets of Y_h^2=R^2+14I^2 with gcd(R,I) supported on {2,3,5}, and show that every packet is either physically excluded or reduces to a globally solvable lower-genus/Thue/elliptic problem. Intersect sur
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 65.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 710096
SOURCE_END: 713451
SOURCE_SHA256: e6ba7d03143bc6cc74e9ae369029298dd6d84cad2886652016ba0cfec1bf1b34

## M3-T11-058
ID:
M3-T11-058
TYPE:
EXACT_STRUCTURE / THEOREM_GATE
TITLE:
Translated-lift common Q(sqrt(-14)) norm factorization
STATUS:
PROVED_EXACT_STRUCTURE / RATIONAL-POINT CLASSIFICATION OPEN
CLAIM:
On the saturated x=27/40 E2 branch,
E2: V^2=U*(U^2+1244U+562500),
the translated-lift condition U-2500=14*r^2 may be parameterized by r=50m, U=2500+35000m^2. Direct substitution gives
V^2=17500^2*(1+14m^2)*(100m^2-4m+9)*(100m^2+4m+9).
For m=a/b in lowest terms,
F0=b^2+14a^2,
F-=100a^2-4ab+9b^2,
F+=100a^2+4ab+9b^2,
and rational translated-lift points satisfy
Y_h^2=F0*F-*F+.
The pairwise resultant values are exactly
900, 900, 57600,
so the pairwise common-prime support of the three primitive homogeneous factors is contained in {2,3,5}.
Moreover
F0=N(b+a*sqrt(-14)),
25F+=N((50a+b)+4b*sqrt(-14)),
25F-=N((50a-b)+4b*sqrt(-14)),
and
F0*F-*F+
=
[b*(124a^2+9b^2)]^2
+
14*[a*(100a^2+7b^2)]^2.
Thus the translated-lift square condition is a single Q(sqrt(-14)) norm-square equation, primitive away from {2,3,5}.
POPULATION:
Exact x=27/40 singular physical carrier inherited from M3-T11-045 through M3-T11-057.
HEIGHT:
Exact physical R<=B remains inherited. This card changes only the arithmetic presentation of the fixed carrier.
DEPENDS_ON:
M3-T11-056;
M3-T11-057;
exact conic parameterization of U-2500=14r^2;
exact polynomial factorization and resultant identities.
IMPLIES:
A new exact receiver
X27Over40CommonMinus14NormSquare.
The finite S={2,3,5} squareclass behavior is visible directly on the saturated translated-lift model.
The next arithmetic attack may use ideal/squareclass descent in Q(sqrt(-14)) and intersect its finite packets with the M3-T11-057 Mordell-Weil residue classes.
ALIASES:
X27Over40TranslatedLiftMinus14NormFactorization;
X27Over40CommonMinus14NormSquare;
X27Over40Minus14IdealClassDescent.
DUPLICATE_OF:
none.
SUPERSEDES:
none; the earlier three-packet S={2,3,5} descent is retained as an equivalent older coordinate presentation, while this card supplies a new common-norm presentation on the saturated translated-lift model.
DO_NOT_REPEAT:
Do not infer rational-point classification merely because the norm factors have pairwise gcd support {2,3,5}.
Do not infer unique factorization in Q(sqrt(-14)).
Do not infer |n|<M/2 from the norm identity.
Do not charge fixed-power or P/M3 credit from this structural reparameterization alone.
REOPEN_CONDITION:
Classify the finite ideal/squareclass packets of
Y_h^2=R^2+14I^2
with gcd(R,I) supported on {2,3,5}, and show that every packet is either physically excluded or reduces to a globally solvable lower-genus/Thue/elliptic problem. Intersect surviving packets with the M3-T11-057 congruence certificate.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 65.
FLAGS:
M3_T11_X_27_OVER_40_TRANSLATED_LIFT_MINUS14_NORM_FACTORIZATION=true
M3_T11_X_27_OVER_40_TRANSLATED_LIFT_PAIRWISE_GCD_SUPPORT_235=true
M3_T11_X_27_OVER_40_SINGLE_MINUS14_NORM_IDENTITY=true
M3_T11_X_27_OVER_40_COMMON_MINUS14_NORM_RECEIVER=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40CommonMinus14NormIdealClassDescent
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-05
