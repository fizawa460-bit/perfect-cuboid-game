# M3-T11-047 — X27Over40KummerGenusTwoRationalPoints

CARD_ID: M3-T11-047
CANONICAL_CARD_KEY: M3-T11-047
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-047
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: On the exact x=27/40 singular fixed-x endpoint carrier, the necessary conic w^2=u^2-350 is not sufficient for full rational anti-root splitting. Full splitting is exactly equivalen
主張の抜粋: On the exact x=27/40 singular fixed-x endpoint carrier, the necessary conic w^2=u^2-350 is not sufficient for full rational anti-root splitting. Full splitting is exactly equivalent to a Kummer cube condition over K=Q(sqrt(-3)), and hence to an affine rational point with 1-9*t^2!=0 on Y^2 = 2*(18*t^2+7) *(81*t^2-6*t+25
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the x=27/40 singular carrier from M3-T11-045/046. Every relative-fresh prime has c_p=0 and fresh p=5
依存関係: M3-T11-031 symmetric anti-root cubic; M3-T11-045 fixed-x cubic and x=27/40 discriminant conic; M3-T11-046 singular-carrier full-S-denominator purity; Cardano/Kummer algebra over Q(sqrt(-3)).
再開条件の抜粋: A complete rational-point classification of the displayed genus-two curve; or a complete classification of points on the elliptic quotient with X-1134 square; or a finite S={2,3,5} descent closing all non-boundary classes; or another exact 
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 54.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 671241
SOURCE_END: 675245
SOURCE_SHA256: b98e6bd97ce31ba818c42413a4d606751ae725b8901ca5332c4c7ebe8aa62308

## M3-T11-047


ID:
M3-T11-047


TYPE:
EXACT_STRUCTURE


STATUS:
PROVED_EXACT


CLAIM:
On the exact x=27/40 singular fixed-x endpoint carrier, the necessary conic w^2=u^2-350 is not sufficient for full rational anti-root splitting. Full splitting is exactly equivalent to a Kummer cube condition over K=Q(sqrt(-3)), and hence to an affine rational point with 1-9*t^2!=0 on


Y^2
=
2*(18*t^2+7)
 *(81*t^2-6*t+25)
 *(81*t^2+6*t+25).


This is a smooth genus-two curve.


It has the exact elliptic quotient


y_E^2=x_E*(81*x_E^2-484*x_E+900),
x_E-14=(6*t)^2,


equivalently


Y_E^2=X^3-484*X^2+72900*X,
X-1134 is a rational square.


For t=a/b reduced, the three quadratic factors in the homogenized genus-two equation are pairwise coprime away from {2,3,5}; therefore each factor has squarefree kernel supported on {2,3,5}, giving a finite S-unit 2-descent.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the x=27/40 singular carrier from M3-T11-045/046. Every relative-fresh prime has c_p=0 and fresh p=5 is excluded, as already canonical.


HEIGHT:
Exact physical R<=B is inherited. No raw square-box replacement and no ambient determinant density is used.


DEPENDS_ON:
M3-T11-031 symmetric anti-root cubic;
M3-T11-045 fixed-x cubic and x=27/40 discriminant conic;
M3-T11-046 singular-carrier full-S-denominator purity;
Cardano/Kummer algebra over Q(sqrt(-3)).


IMPLIES:
The carrier-specific open problem is sharpened from
X27Over40SplitCubicSameMeasureCarrier
to
X27Over40KummerGenusTwoRationalPoints,
with preferred first continuation
X27Over40S235SquareclassDescent.


ALIASES:
X27Over40KummerGenusTwoRationalPoints;
X27Over40EllipticSquareLift;
X27Over40S235SquareclassDescent.


DUPLICATE_OF:
none.


SUPERSEDES:
The conic w^2=u^2-350 as a complete description of the splitting condition. The conic remains a necessary first layer.


DO_NOT_REPEAT:
Do not treat square discriminant / w^2=u^2-350 as sufficient for rational anti-root splitting.
Do not promote the bounded rational search to theorem credit.
Do not infer a fixed-power saving from genus two, the elliptic quotient, or the finite S-unit reduction without the rational-point/same-measure theorem.


REOPEN_CONDITION:
A complete rational-point classification of the displayed genus-two curve;
or a complete classification of points on the elliptic quotient with X-1134 square;
or a finite S={2,3,5} descent closing all non-boundary classes;
or another exact same-measure argument eliminating/counting the x=27/40 physical carrier.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 54.


EXACT DERIVATION SNAPSHOT:
For the depressed cubic y^3+p*y+q=0,


p=-4*u^2*(25*u^2-2)/(25*(1+u^2)^2),
q=-288*u^3*(25*u^2-2)/(125*(1+u^2)^3).


With beta=162+5*w*sqrt(-3),


A_K
=
[2*u*beta/(15*(1+u^2))]^3
*
(conj(beta)/beta).


Thus full splitting is equivalent to conj(beta)/beta being a cube in Q(sqrt(-3)). Writing a norm-one cube as


[(1+t*sqrt(-3))/(1-t*sqrt(-3))]^3


gives


w=-486*t*(1-t^2)/(5*(1-9*t^2))


and the genus-two equation above.


EXACT NEGATIVE WITNESS:
u=45/2, w=25/2 lies on w^2=u^2-350, but the cleared cubic


4116841*z^3-1972188*z^2-16084980*z-7873200


reduces modulo 11 to


3*z^3+2*z^2+z+6,


which has no F_11 root. Hence the conic alone is not sufficient.


COMPUTATIONAL_SCREEN:
Primitive max(|a|,b)<=2000 gives only t=+/-1/3, Y=+/-144. These are boundary/extraneous because 1-9*t^2=0. This is not theorem credit.


CURRENT_CANONICAL_GATE=SymmetricCommonUFullFreshRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthTwoFreshCoreGaussianSquarePair|X27Over40KummerGenusTwoRationalPoints|InteriorCharacterGlobalDispersion
NEXT_ATTACK=X27Over40S235SquareclassDescent|XMinusOneEighthTwoCorePhysicalRangeDeficit|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
