# M3-ODD-001 — OddEdgeIsSourceLegLCM

CARD_ID: M3-ODD-001
CANONICAL_CARD_KEY: M3-ODD-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-ODD-001
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: The physical unique odd edge is X=lcm(U1,U2). For fixed X<=B, the number of primitive Master source tuples producing X is X^o(1)<=B^o(1), and therefore the fixed-X M3 multiplicity 
主張の抜粋: The physical unique odd edge is X=lcm(U1,U2). For fixed X<=B, the number of primitive Master source tuples producing X is X^o(1)<=B^o(1), and therefore the fixed-X M3 multiplicity is B^o(1). Consequently, for every fixed epsilon>0, #{E in M3(B): X(E)<=B^(1/3-epsilon)} =o(M3(B)).
対象・測度: exact physical M3.
依存関係: exact Master coverage and M3(B)>>B^(1/3).
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Section97.1-97.2.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 294270
SOURCE_END: 295221
SOURCE_SHA256: fd805d4eef28d8bc1977722b413dcb54e371ce9005cc3f8bb977697e7c1c6047

## M3-ODD-001
TYPE: THEOREM
STATUS: PROVED_EXACT


CLAIM:
The physical unique odd edge is
X=lcm(U1,U2).
For fixed X<=B, the number of primitive Master source tuples producing X is
X^o(1)<=B^o(1),
and therefore the fixed-X M3 multiplicity is B^o(1).
Consequently, for every fixed epsilon>0,
#{E in M3(B): X(E)<=B^(1/3-epsilon)}
=o(M3(B)).


POPULATION:
exact physical M3.


HEIGHT:
exact R<=B.


DEPENDS_ON:
exact Master coverage and M3(B)>>B^(1/3).


IMPLIES:
after an M3-negligible deletion, the odd edge satisfies
X>=B^(1/3-epsilon).


ALIASES:
OddEdgeIsSourceLegLCM;
FixedOddEdgeMasterMultiplicity;
SmallOddEdgeRegionNegligible.


DUPLICATE_OF:
M3-FIB-001 is anti-concentration in the moving t-coordinate; this is anti-concentration in the physical odd edge.


SUPERSEDES:
none.


DO_NOT_REPEAT:
Do not assume many M3 points can concentrate at one fixed small odd edge.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Section97.1-97.2.


---
