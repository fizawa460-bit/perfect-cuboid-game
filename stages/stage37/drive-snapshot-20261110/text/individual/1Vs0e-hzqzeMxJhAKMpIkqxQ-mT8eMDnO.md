# M3-NORM-002 — FixedFirstNormM3Multiplicity

CARD_ID: M3-NORM-002
CANONICAL_CARD_KEY: M3-NORM-002
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-NORM-002
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: For every fixed n, #{E in M3(B): N_-(E)=n} <=B^o(1) uniformly for n<=B^2; symmetrically the same holds for N_+. Therefore, for each fixed epsilon>0, the regions N_-<=B^(1/3-epsilon
主張の抜粋: For every fixed n, #{E in M3(B): N_-(E)=n} <=B^o(1) uniformly for n<=B^2; symmetrically the same holds for N_+. Therefore, for each fixed epsilon>0, the regions N_-<=B^(1/3-epsilon) and N_+<=B^(1/3-epsilon) are each o(M3(B)). After deleting an M3-negligible set, B^(1/3-epsilon)<=N_-,N_+<=B^(5/3+epsilon).
対象・測度: exact physical M3.
依存関係: M3-NORM-001, divisor-many representations, squareclass orientations, and uniform bounded-height counting on the resulting rational-2-torsion genus-one fibers.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Sections100.4-100.7.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 301385
SOURCE_END: 302485
SOURCE_SHA256: d9011eecd12259e181b9aee30c95aec9afe10710e1c104c65424bcbdf59df8dc

## M3-NORM-002
TYPE: THEOREM
STATUS: PROVED_EXACT


CLAIM:
For every fixed n,
#{E in M3(B): N_-(E)=n}
<=B^o(1)
uniformly for n<=B^2;
symmetrically the same holds for N_+.
Therefore, for each fixed epsilon>0,
the regions
N_-<=B^(1/3-epsilon)
and
N_+<=B^(1/3-epsilon)
are each o(M3(B)).
After deleting an M3-negligible set,
B^(1/3-epsilon)<=N_-,N_+<=B^(5/3+epsilon).


POPULATION:
exact physical M3.


HEIGHT:
exact product height N_-N_+<=B^2.


DEPENDS_ON:
M3-NORM-001, divisor-many representations, squareclass orientations, and uniform bounded-height counting on the resulting rational-2-torsion genus-one fibers.


IMPLIES:
both primitive norms are exact M3 anti-concentration coordinates.


ALIASES:
FixedFirstNormM3Multiplicity;
small-Nminus negligibility;
small-Nplus negligibility.


DUPLICATE_OF:
M3-ODD-001 and M3-FIB-001 are analogous anti-concentration theorems in different coordinates.


SUPERSEDES:
none.


DO_NOT_REPEAT:
Fixed-norm B^o(1) does not itself prove the moving square-kernel incidence is rare.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Sections100.4-100.7.


---
