# M3-T11-051 — E2 torsion-normalized free class, rational cyclic 3-isogeny, and exact 3-saturation

CARD_ID: M3-T11-051
CANONICAL_CARD_KEY: M3-T11-051
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-051
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: On the x=27/40 E_2 quotient of M3-T11-050,
主張の抜粋: On the x=27/40 E_2 quotient of M3-T11-050, E_2: V^2=U*(U^2+1244*U+562500), with rational 2-torsion T=(0,0) and the M3-T11-050 point P=(11250,1260000), there is a smaller rational point Q=(50,5600) satisfying exactly P+Q=T. For every R=(U,V) with U!=0, R+T=(562500/U,-562500*V/U^2), so P and Q represent the same free ran
対象・測度: Exact x=27/40 singular fixed-x physical endpoint carrier inherited from M3-T11-045 through M3-T11-050.
依存関係: M3-T11-050; exact elliptic-curve group law on E_2; exact 3-division polynomial; exact good-reduction calculation at ell=11.
再開条件の抜粋: For full saturation, obtain a rigorous upper bound for the saturation index of <Q,T> and certify p-saturation for every remaining candidate odd prime. Then classify the normalized translated lift X*(225-X)=14*s^2 by a rank-one Mordell-Weil 
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 58.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 687095
SOURCE_END: 691215
SOURCE_SHA256: 60aac59fee08a12433adb4ec811f80c772978083dff2075d8647e6bd062abf1f

## M3-T11-051


ID:
M3-T11-051


TYPE:
EXACT_STRUCTURE


STATUS:
PROVED_EXACT


TITLE:
E2 torsion-normalized free class, rational cyclic 3-isogeny, and exact 3-saturation


CLAIM:
On the x=27/40 E_2 quotient of M3-T11-050,


E_2:
V^2=U*(U^2+1244*U+562500),


with rational 2-torsion


T=(0,0)


and the M3-T11-050 point


P=(11250,1260000),


there is a smaller rational point


Q=(50,5600)


satisfying exactly


P+Q=T.


For every R=(U,V) with U!=0,


R+T=(562500/U,-562500*V/U^2),


so P and Q represent the same free rank-one Mordell-Weil class up to sign and rational 2-torsion. Odd saturation of P is therefore equivalent to odd saturation of Q.


The translated lift


U-2500=14*r^2


is exactly equivalent, under


X=562500/U,
s=X*r/50,


to


X*(225-X)=14*s^2.


The E_2 3-division polynomial factors exactly as


psi_3(U)
=
3*U^4+4976*U^3+3375000*U^2-316406250000


=
(3*U+1250)
*(U^3+1242*U^2+607500*U-253125000).


At the rational root U=-1250/3 one has


V^2=-2450000000/27,


of squareclass -6. Thus the corresponding order-3 pair is defined over Q(sqrt(-6)) and forms a Galois-stable cyclic subgroup. Hence E_2 admits a rational cyclic 3-isogeny.


At the good prime ell=11,


#E_2(F_11)=12


and the reduction of Q satisfies


[4]Q=(5,4) != O.


Therefore Q cannot equal 3R for any R in E_2(Q), because otherwise reduction modulo 11 would give [4]Q=[12]R=O. Hence the free rank-one class represented by P/Q is exactly 3-saturated.


POPULATION:
Exact x=27/40 singular fixed-x physical endpoint carrier inherited from M3-T11-045 through M3-T11-050.


HEIGHT:
Exact physical R<=B remains inherited. No counting-measure or height change.


DEPENDS_ON:
M3-T11-050;
exact elliptic-curve group law on E_2;
exact 3-division polynomial;
exact good-reduction calculation at ell=11.


IMPLIES:
A smaller preferred free-class representative Q=(50,5600) is available.
The p=3 saturation obstruction is closed exactly.
The active translated-square lift has the exact torsion-normalized form


X*(225-X)=14*s^2.


The next Mordell-Weil step should work with Q and this normalized lift.


ALIASES:
X27Over40E2TorsionNormalizedFreeClass;
X27Over40E2RationalThreeIsogeny;
X27Over40E2ThreeSaturation;
X27Over40E2TorsionNormalizedTranslatedLift.


DUPLICATE_OF:
none.


SUPERSEDES:
Using P=(11250,1260000) as the only preferred free-class representative for saturation calculations;
leaving p=3 as an unresolved possible saturation-index prime.


DO_NOT_REPEAT:
Do not infer a full Mordell-Weil generator from this p=3 certificate.
Do not call the rational cyclic 3-isogeny rational 3-torsion.
Do not reopen the old three-packet U-squareclass restriction; M3-T11-050 already makes that exhaustive rather than restrictive.


REOPEN_CONDITION:
For full saturation, obtain a rigorous upper bound for the saturation index of <Q,T> and certify p-saturation for every remaining candidate odd prime.
Then classify the normalized translated lift


X*(225-X)=14*s^2


by a rank-one Mordell-Weil sieve with the physical finite-point exclusions.
If that does not close the carrier, use the split-Jacobian quadratic-Chabauty route retained in M3-T11-050.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 58.


FLAGS:
M3_T11_X_27_OVER_40_E2_TORSION_NORMALIZED_Q_FOUND=true
M3_T11_X_27_OVER_40_E2_RATIONAL_3_ISOGENY=true
M3_T11_X_27_OVER_40_E2_FREE_CLASS_3_SATURATED=true
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


CURRENT_CANONICAL_GATE=SymmetricCommonUFullFreshRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthTwoFreshCoreGaussianSquarePair|X27Over40E2SaturationIndexBoundAndTorsionNormalizedMordellWeilSieve|InteriorCharacterGlobalDispersion
NEXT_ATTACK=X27Over40E2SaturationIndexBoundAndAuxiliaryPrimeSieve|X27Over40E2TorsionNormalizedTranslatedLiftMordellWeilSieve|X27Over40SplitJacobianQuadraticChabauty|XMinusOneEighthTwoCorePhysicalRangeDeficit|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion
