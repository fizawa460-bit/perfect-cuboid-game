# M3-T11-052 — Exact good-reduction saturation panel through odd prime 251 and saturation-index floor 257

CARD_ID: M3-T11-052
CANONICAL_CARD_KEY: M3-T11-052
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-052
現行一覧の状態: PROVED_EXACT_FINITE_PANEL / FULL_SATURATION_OPEN
要点: Retain the exact rank-one elliptic quotient
主張の抜粋: Retain the exact rank-one elliptic quotient E_2: V^2=U*(U^2+1244*U+562500), with rational 2-torsion T=(0,0) and preferred point Q=(50,5600). For every odd prime p<=251 there exists a good-reduction prime ell such that, with N_ell=#E_2(F_ell), one has p|N_ell and [N_ell/p]Qbar != O. Therefore Q notin p*E_2(Q) for every 
対象・測度: Exact x=27/40 singular fixed-x physical endpoint carrier inherited from M3-T11-045 through M3-T11-051.
依存関係: M3-T11-050; M3-T11-051; the inherited exact 2-Kummer non-divisibility; rank E_2(Q)=1; rational torsion of order 2; good reduction of E_2 away from {2,3,5,7}; exact finite-field group arithmetic record
再開条件の抜粋: Obtain a proof-grade upper bound I<257, preferably by canonical-height/regulator saturation bounds or an exact Mordell-Weil-basis computation on this exact E_2 model. After that, run the rank-one Mordell-Weil sieve on X*(225-X)=14*s^2 with 
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 59.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 691215
SOURCE_END: 695425
SOURCE_SHA256: 68f4b5b65d0aaaaa22721a8edf09f3a7363a50f1601dc162f0798191f5ec2b45

## M3-T11-052


ID:
M3-T11-052


TITLE:
Exact good-reduction saturation panel through odd prime 251 and saturation-index floor 257


STATUS:
PROVED_EXACT_FINITE_PANEL / FULL_SATURATION_OPEN


CLAIM:
Retain the exact rank-one elliptic quotient


E_2:
V^2=U*(U^2+1244*U+562500),


with rational 2-torsion T=(0,0) and preferred point Q=(50,5600).


For every odd prime p<=251 there exists a good-reduction prime ell such that, with


N_ell=#E_2(F_ell),


one has p|N_ell and


[N_ell/p]Qbar != O.


Therefore


Q notin p*E_2(Q)


for every odd prime p<=251.


The exact 53-row witness table, including ell, N_ell and the nonzero reduced point [N_ell/p]Qbar, is recorded in
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 59.


The p=3 row is the M3-T11-051 witness ell=11, N_ell=12, [4]Qbar=(5,4).
The new panel extends the exact non-divisibility certificate through every odd prime from 5 to 251.


PROOF:
For any good prime ell and any odd p|N_ell, if Q=pR in E_2(Q), reduction modulo ell gives Qbar=pRbar and hence


[N_ell/p]Qbar=[N_ell]Rbar=O.


Thus a nonzero [N_ell/p]Qbar is an exact obstruction to p-divisibility over Q.


Every Section-59 row was independently rechecked by direct finite-field point counting, exact scalar multiplication, and substitution into the reduced curve equation. In every recorded witness, p divides N_ell exactly once.


POPULATION:
Exact x=27/40 singular fixed-x physical endpoint carrier inherited from M3-T11-045 through M3-T11-051.


HEIGHT:
Exact physical R<=B remains inherited. No population, measure, field, or height change.


DEPENDS_ON:
M3-T11-050;
M3-T11-051;
the inherited exact 2-Kummer non-divisibility;
rank E_2(Q)=1;
rational torsion of order 2;
good reduction of E_2 away from {2,3,5,7};
exact finite-field group arithmetic recorded in Route Section 59.


IMPLIES:
Let


I=[E_2(Q):<Q,T>].


The inherited 2-Kummer certificate excludes 2|I. For odd p, because multiplication by p is an automorphism on the rational 2-torsion, p|I would force Q to be p-divisible.


Hence the new panel gives exactly


I=1
or
I>=257.


So it is now sufficient to prove the single quantitative bound


I<257


to certify full Mordell-Weil saturation of <Q,T>.


ALIASES:
X27Over40E2OddPrimeSaturationThrough251;
X27Over40E2IndexPrimeDivisorFloor257;
X27Over40E2IndexUpperBoundBelow257Gate.


DUPLICATE_OF:
none.


SUPERSEDES:
Treating every odd saturation-index prime other than 3 as unresolved;
the unbounded auxiliary-prime search as the immediate first task.


DO_NOT_REPEAT:
Do not infer full saturation from the finite p<=251 panel alone.
Do not call Q a full Mordell-Weil generator until an exact index upper bound I<257 or an equivalent full-basis certificate is proved.
Do not restart the old U-squareclass packet search.
Do not infer rational-point classification or a fixed-power saving from finite saturation tests.


REOPEN_CONDITION:
Obtain a proof-grade upper bound


I<257,


preferably by canonical-height/regulator saturation bounds or an exact Mordell-Weil-basis computation on this exact E_2 model.


After that, run the rank-one Mordell-Weil sieve on


X*(225-X)=14*s^2


with the physical finite-point exclusions. Retain split-Jacobian quadratic Chabauty as fallback.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 59.


FLAGS:
M3_T11_X_27_OVER_40_E2_ODD_PRIME_SATURATION_THROUGH_251=true
M3_T11_X_27_OVER_40_E2_INDEX_PRIME_DIVISOR_FLOOR_257=true
M3_T11_X_27_OVER_40_E2_INDEX_UPPER_BOUND_LT_257_PROVED=false
M3_T11_X_27_OVER_40_E2_P_SATURATED_GENERATOR_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


CURRENT_CANONICAL_GATE=SymmetricCommonUFullFreshRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthTwoFreshCoreGaussianSquarePair|X27Over40E2IndexUpperBoundBelow257ThenTorsionNormalizedMordellWeilSieve|InteriorCharacterGlobalDispersion
NEXT_ATTACK=X27Over40E2IndexUpperBoundBelow257|X27Over40E2TorsionNormalizedTranslatedLiftMordellWeilSieve|X27Over40SplitJacobianQuadraticChabauty|XMinusOneEighthTwoCorePhysicalRangeDeficit|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion
