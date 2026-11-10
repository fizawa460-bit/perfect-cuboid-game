# M3-T11-050 — X27Over40E2TranslatedSquareLiftMordellWeilSieve

CARD_ID: M3-T11-050
CANONICAL_CARD_KEY: M3-T11-050
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-050
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: On the x=27/40 genus-two receiver of M3-T11-047/048/049, both elliptic quotients have Mordell-Weil rank exactly one. For the complementary quotient
主張の抜粋: On the x=27/40 genus-two receiver of M3-T11-047/048/049, both elliptic quotients have Mordell-Weil rank exactly one. For the complementary quotient E_2: V^2=U*(U^2+1244*U+562500), the standard 2-isogenous curve is E_2': y^2=x*(x+256)*(x-2744). Exact primitive local-solubility elimination on the 2-isogeny homogeneous sp
対象・測度: Exact x=27/40 singular fixed-x physical endpoint carrier of M3-T11-045 through M3-T11-049.
依存関係: M3-T11-047; M3-T11-048; M3-T11-049; classical 2-isogeny descent for curves with rational 2-torsion; the two rational bielliptic involutions of the genus-two carrier.
再開条件の抜粋: Certify an exact saturated Mordell-Weil basis for E_2(Q), preferably also E_1(Q), and classify E_2(Q) points satisfying U-2500=14*r^2 with the physical finite-point exclusions; or carry out an explicit split-Jacobian quadratic-Chabauty comp
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 57.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 681847
SOURCE_END: 687095
SOURCE_SHA256: 4c1c2e40814f6d838cf7fb27ae6fe09eae1094e1c5bba80a62f83615f21f6958

## M3-T11-050


ID:
M3-T11-050


TYPE:
THEOREM


STATUS:
PROVED_EXACT


CLAIM:
On the x=27/40 genus-two receiver of M3-T11-047/048/049, both elliptic quotients have Mordell-Weil rank exactly one.


For the complementary quotient


E_2:
V^2=U*(U^2+1244*U+562500),


the standard 2-isogenous curve is


E_2':
y^2=x*(x+256)*(x-2744).


Exact primitive local-solubility elimination on the 2-isogeny homogeneous spaces gives


im(alpha_E2)={1,2}


and


im(alpha_E2')={1,-1,14,-14}.


The classical rational-2-torsion descent formula therefore gives


rank E_2(Q)=1.


For the first quotient


E_1:
Y_E^2=X*(X^2-484*X+72900),


the standard 2-isogenous curve is


E_1':
y^2=x*(x-56)*(x+1024),


and the same exact local descent gives


im(alpha_E1)={1,2},
im(alpha_E1')={1,-1,14,-14},


hence


rank E_1(Q)=1.


The M3-T11-049 lift


t^2=8750/(9*U-22500)


is exactly equivalent for finite t to


U-2500=14*r^2,


r=25/(3*t).


Thus the live lift is the translated squareclass condition


[U-2500]=14.


Moreover, because im(alpha_E2)={1,2}, every rational E_2 point already has U-squareclass 1 or 2. The M3-T11-048 packet split is therefore exhaustive on E_2(Q) and is not an additional global restriction after passing to this quotient.


The two rational involutions of the genus-two curve induce a Q-isogeny


Jac(C) ~ E_1 x E_2,


so


rank Jac(C)(Q)=2.


Since genus(C)=2, the classical Chabauty-Coleman condition rank(J)<g fails exactly. Since the split product gives rho(J)>=2, the quadratic-Chabauty finiteness inequality


rank(J)<dim(J)+rho(J)-1


is satisfied.


POPULATION:
Exact x=27/40 singular fixed-x physical endpoint carrier of M3-T11-045 through M3-T11-049.


HEIGHT:
Exact physical R<=B remains inherited. No change of counting measure or height.


DEPENDS_ON:
M3-T11-047;
M3-T11-048;
M3-T11-049;
classical 2-isogeny descent for curves with rational 2-torsion;
the two rational bielliptic involutions of the genus-two carrier.


LOCAL_CERTIFICATE:
For E_2 and E_1, positive candidate Kummer classes
{1,2,3,5,6,10,15,30}
are reduced by exact primitive residue tests:
mod 16 removes 3,6,15,30;
mod 7 removes 5,10;
1 and 2 are realized.


For both isogenous curves, candidate classes
{+/-1,+/-2,+/-7,+/-14}
are reduced modulo 5:
+/-2 and +/-7 are impossible;
1,-1,14,-14 are realized by rational 2-torsion.


BOUNDARY_CHECK:
For E_2, t=+/-1/3 maps to
U=11250=2*75^2,
V=+/-1260000.


For a chosen sign P=(11250,1260000),
2P=(2500,157500).


The U=2500 points are the images of the two points at infinity of the smooth genus-two model; they are not finite affine t-points.


For E_1, t=+/-1/3 maps to
X=1458=2*27^2,
Y_E=+/-46656.


IMPLIES:
The x=27/40 continuation is no longer primarily a three-packet or U-squareclass problem.
The first direct global attack is the rank-one E_2 translated square-lift
U-2500=14*r^2,
with exact physical exclusions.
A split-Jacobian quadratic-Chabauty computation is a valid secondary route.
Plain rank<genus Chabauty is closed.


ALIASES:
X27Over40E2TranslatedSquareLiftMordellWeilSieve;
X27Over40RankOneE2TranslatedLift;
X27Over40BiellipticRankTwoJacobian;
X27Over40SplitJacobianQuadraticChabauty.


DUPLICATE_OF:
none.


SUPERSEDES:
Treating [U]=1 or [U]=2 as a further restrictive global condition on E_2(Q);
treating classical rank<genus Chabauty as available for this genus-two carrier.


DO_NOT_REPEAT:
Do not reopen the 64-class S={2,3,5} descent.
Do not analyze the three M3-T11-048 packets globally as unrelated curves before using the E_2 compression.
Do not claim that P=(11250,1260000) is a saturated Mordell-Weil generator until odd saturation is certified.
Do not claim rational-point classification from rank=1.
Do not claim rational-point classification merely from the quadratic-Chabauty rank inequality.


REOPEN_CONDITION:
Certify an exact saturated Mordell-Weil basis for E_2(Q), preferably also E_1(Q), and classify E_2(Q) points satisfying
U-2500=14*r^2
with the physical finite-point exclusions;
or carry out an explicit split-Jacobian quadratic-Chabauty computation and Mordell-Weil sieve.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 57.


FLAGS:
M3_T11_X_27_OVER_40_E2_KUMMER_IMAGE_EXACT=true
M3_T11_X_27_OVER_40_E2_RANK_ONE=true
M3_T11_X_27_OVER_40_E1_KUMMER_IMAGE_EXACT=true
M3_T11_X_27_OVER_40_E1_RANK_ONE=true
M3_T11_X_27_OVER_40_JACOBIAN_RANK_TWO=true
M3_T11_X_27_OVER_40_CLASSICAL_CHABAUTY_RANK_LT_GENUS=false
M3_T11_X_27_OVER_40_QUADRATIC_CHABAUTY_RANK_INEQUALITY=true
M3_T11_X_27_OVER_40_E2_U_SQUARECLASS_EXHAUSTIVE=true
M3_T11_X_27_OVER_40_TRANSLATED_LIFT_CLASS_14=true
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


CURRENT_CANONICAL_GATE=SymmetricCommonUFullFreshRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthTwoFreshCoreGaussianSquarePair|X27Over40E2TranslatedSquareLiftMordellWeilSieve|InteriorCharacterGlobalDispersion
NEXT_ATTACK=X27Over40E2OddSaturationAndTranslatedLiftMordellWeilSieve|X27Over40SplitJacobianQuadraticChabauty|XMinusOneEighthTwoCorePhysicalRangeDeficit|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion
