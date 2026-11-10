# M3-T11-049 — X27Over40ComplementaryEllipticSquareclassLift

CARD_ID: M3-T11-049
CANONICAL_CARD_KEY: M3-T11-049
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-049
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: The x=27/40 genus-two receiver has a complementary elliptic quotient under (t,Y)->(-t,-Y). On the rational locus t!=0, the exact map U=(8750/t^2+22500)/9, V=8750*Y/(27*t^3) lands o
主張の抜粋: The x=27/40 genus-two receiver has a complementary elliptic quotient under (t,Y)->(-t,-Y). On the rational locus t!=0, the exact map U=(8750/t^2+22500)/9, V=8750*Y/(27*t^3) lands on E_2: V^2=U*(U^2+1244*U+562500). For t=a/b reduced and A0=18*a^2+7*b^2, U=1250*A0/(9*a^2), so in Q*/Q*2, [U]=[2*A0]=2*d0. Using M3-T11-048,
対象・測度: Exact x=27/40 singular fixed-x physical endpoint carrier of M3-T11-045/046/047, with the local packet reduction of M3-T11-048.
依存関係: M3-T11-047; M3-T11-048; the complementary involution (t,Y)->(-t,-Y).
再開条件の抜粋: Determine E_2(Q) sufficiently to classify points in [U]=1 and [U]=2 satisfying the exact lift; or prove a direct local/global obstruction on either squareclass subcover.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 56.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 678786
SOURCE_END: 681847
SOURCE_SHA256: 3006708c3cd948c1c78ff8d2041d7c1e918b9763a3ceea218f8a04657d9f2424

## M3-T11-049


ID:
M3-T11-049


TYPE:
EXACT_STRUCTURE


STATUS:
PROVED_EXACT


CLAIM:
The x=27/40 genus-two receiver has a complementary elliptic quotient under (t,Y)->(-t,-Y). On the rational locus t!=0, the exact map


U=(8750/t^2+22500)/9,
V=8750*Y/(27*t^3)


lands on


E_2:
V^2=U*(U^2+1244*U+562500).


For t=a/b reduced and A0=18*a^2+7*b^2,


U=1250*A0/(9*a^2),


so in Q*/Q*2,


[U]=[2*A0]=2*d0.


Using M3-T11-048, Packets I/II have [U]=2 and Packet III has [U]=1.


Therefore every x=27/40 rational point lies in one of two explicit elliptic squareclass subcovers:


Packet III:
U=s^2,
z^2=s^4+1244*s^2+562500.


Packets I/II:
U=2*s^2,
z^2=2*s^4+1244*s^2+281250.


The exact lift back to the genus-two curve is


t^2=8750/(9*U-22500),


so the elliptic subcover condition alone is not sufficient.


POPULATION:
Exact x=27/40 singular fixed-x physical endpoint carrier of M3-T11-045/046/047, with the local packet reduction of M3-T11-048.


HEIGHT:
Exact physical R<=B remains inherited. This is a rational-map adapter, not a change of counting measure.


DEPENDS_ON:
M3-T11-047;
M3-T11-048;
the complementary involution (t,Y)->(-t,-Y).


IMPLIES:
The x=27/40 rational-point problem can be continued on one explicit elliptic quotient E_2 using its two relevant U-squareclasses plus the exact t-square lift.


ALIASES:
X27Over40ComplementaryEllipticSquareclassLift;
X27Over40E2MordellWeilTwoIsogenySquareLift;
X27Over40PacketSquareclassCompression.


DUPLICATE_OF:
none.


SUPERSEDES:
Treating the three M3-T11-048 packets as three unrelated global curves.


DO_NOT_REPEAT:
Do not drop the lift condition t^2=8750/(9U-22500).
Do not infer rational-point classification merely from the elliptic quotient.
Do not identify an elliptic-rank computation, if later obtained, with endpoint elimination without checking the lift.


REOPEN_CONDITION:
Determine E_2(Q) sufficiently to classify points in [U]=1 and [U]=2 satisfying the exact lift;
or prove a direct local/global obstruction on either squareclass subcover.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 56.


BOUNDARY_CHECK:
t=+/-1/3 maps to
U=11250=2*75^2,
V=+/-1260000,
and on the twice-square subcover one has s=75, z=+/-8400.


FLAGS:
M3_T11_X_27_OVER_40_COMPLEMENTARY_ELLIPTIC_QUOTIENT=true
M3_T11_X_27_OVER_40_PACKET_SQUARECLASS_COMPRESSION=true
M3_T11_X_27_OVER_40_PACKET_III_E2_SQUARE_U=true
M3_T11_X_27_OVER_40_PACKET_I_II_E2_TWICE_SQUARE_U=true
M3_T11_X_27_OVER_40_E2_LIFT_CONDITION_EXACT=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


CURRENT_CANONICAL_GATE=SymmetricCommonUFullFreshRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthTwoFreshCoreGaussianSquarePair|X27Over40ComplementaryEllipticSquareclassLift|InteriorCharacterGlobalDispersion
NEXT_ATTACK=X27Over40E2MordellWeilTwoIsogenySquareLift|XMinusOneEighthTwoCorePhysicalRangeDeficit|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion
