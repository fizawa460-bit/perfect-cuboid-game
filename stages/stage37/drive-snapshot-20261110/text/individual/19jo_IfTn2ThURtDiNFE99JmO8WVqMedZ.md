# M3-T11-048 — X27Over40ThreePacketS235Descent

CARD_ID: M3-T11-048
CANONICAL_CARD_KEY: M3-T11-048
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-048
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: For the exact x=27/40 singular-carrier genus-two receiver of M3-T11-047, its finite S={2,3,5} squareclass descent reduces by exact local solubility to exactly three squareclass pac
主張の抜粋: For the exact x=27/40 singular-carrier genus-two receiver of M3-T11-047, its finite S={2,3,5} squareclass descent reduces by exact local solubility to exactly three squareclass packets. With t=a/b reduced and A0=18*a^2+7*b^2, B_minus=81*a^2-6*a*b+25*b^2, B_plus=81*a^2+6*a*b+25*b^2, write A0=d0*r0^2, B_minus=d_minus*r_m
対象・測度: Exact x=27/40 singular fixed-x physical endpoint carrier of M3-T11-045/046/047.
依存関係: M3-T11-047; finite S={2,3,5} squareclass support for A0,B_minus,B_plus; exact finite local residue arithmetic.
再開条件の抜粋: Further exact local or global analysis of Packet III; classification of Packet I (and hence II by sign symmetry); or a direct rational-point theorem for the genus-two receiver.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 55.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 675245
SOURCE_END: 678786
SOURCE_SHA256: 90c80415bbb3b1a31bed907b1ec6fd38060ec1ef078e1b73c10ec4f3554ea636

## M3-T11-048


ID:
M3-T11-048


TYPE:
EXACT_STRUCTURE


STATUS:
PROVED_EXACT


CLAIM:
For the exact x=27/40 singular-carrier genus-two receiver of M3-T11-047, its finite S={2,3,5} squareclass descent reduces by exact local solubility to exactly three squareclass packets.


With t=a/b reduced and


A0=18*a^2+7*b^2,
B_minus=81*a^2-6*a*b+25*b^2,
B_plus=81*a^2+6*a*b+25*b^2,


write


A0=d0*r0^2,
B_minus=d_minus*r_minus^2,
B_plus=d_plus*r_plus^2


with d_i in {1,2,3,5,6,10,15,30}. The condition 2*d0*d_minus*d_plus=square gives exactly 64 initial triples.


Exact local residue tests reduce these as follows:


64 -> 16 mod 7 -> 12 mod 11 -> 9 mod 29 -> 5 mod 4 -> 3 mod 16.


The final triples are exactly


(1,2,1),
(1,1,2),
(2,1,1).


Equivalently every rational point must satisfy one of


I:
A0=r0^2,
B_minus=2*r_minus^2,
B_plus=r_plus^2;


II:
A0=r0^2,
B_minus=r_minus^2,
B_plus=2*r_plus^2;


III:
A0=2*r0^2,
B_minus=r_minus^2,
B_plus=r_plus^2.


I and II are exchanged by a -> -a.


The exact deeper local conditions are:


I:
b == 3*a mod 81,
b/a mod 16 in {3,7,11,15};


II:
b == -3*a mod 81,
b/a mod 16 in {1,5,9,13};


III:
b == 0 mod 81,
b/a mod 16 in {0,4,8,12},
hence 324|b.


The 3-adic congruences are certified by exhaustive projective residue checks modulo 3^5=243 after normalizing the forced 3-adic unit a=1. The 2-adic congruences are certified modulo 16.


POPULATION:
Exact x=27/40 singular fixed-x physical endpoint carrier of M3-T11-045/046/047.


HEIGHT:
Exact physical R<=B is inherited. The local reduction does not replace the physical measure by a raw box.


DEPENDS_ON:
M3-T11-047;
finite S={2,3,5} squareclass support for A0,B_minus,B_plus;
exact finite local residue arithmetic.


IMPLIES:
The first x=27/40 attack is sharpened from a 64-class S-unit descent to three covering packets, only two up to sign symmetry.


ALIASES:
X27Over40ThreePacketS235Descent;
X27Over40Local64To3;
X27Over40PacketIII324Divisibility.


DUPLICATE_OF:
none.


SUPERSEDES:
Treating all 64 S={2,3,5} squareclass allocations as live.


DO_NOT_REPEAT:
Do not reopen the 61 locally impossible squareclass triples.
Do not infer that the three surviving packets possess rational points.
Do not infer rational-point classification or fixed-power saving from the local reduction.
Do not treat the bounded-height screen of M3-T11-047 as proof.


REOPEN_CONDITION:
Further exact local or global analysis of Packet III;
classification of Packet I (and hence II by sign symmetry);
or a direct rational-point theorem for the genus-two receiver.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 55.


LOCAL_CERTIFICATE:
64 -> 16 (mod 7) -> 12 (mod 11) -> 9 (mod 29) -> 5 (mod 4) -> 3 (mod 16).
Survivors:
(1,2,1),(1,1,2),(2,1,1).


FLAGS:
M3_T11_X_27_OVER_40_S235_64_TO_3_LOCAL_REDUCTION=true
M3_T11_X_27_OVER_40_THREE_PACKET_DESCENT=true
M3_T11_X_27_OVER_40_PACKET_I_II_SIGN_SYMMETRY=true
M3_T11_X_27_OVER_40_PACKET_III_B_DIVISIBLE_324=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


CURRENT_CANONICAL_GATE=SymmetricCommonUFullFreshRootLineSupportOneTwelfth
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthTwoFreshCoreGaussianSquarePair|X27Over40ThreePacketS235Descent|InteriorCharacterGlobalDispersion
NEXT_ATTACK=X27Over40PacketIIILocalGlobalElimination|X27Over40PacketIBoundaryClassification|XMinusOneEighthTwoCorePhysicalRangeDeficit|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion
