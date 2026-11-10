# M3-FIB-SCAN-FW-001 — occupied-fiber selection bias

CARD_ID: M3-FIB-SCAN-FW-001
CANONICAL_CARD_KEY: M3-FIB-SCAN-FW-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-FIB-SCAN-FW-001
現行一覧の状態: FROZEN
種別: COMPUTATIONAL_FIREWALL
要点: Empirical occupied-fiber/rank frequencies are highly sensitive to sampling and search depth. Sampling t-values obtained from already-found Master-Hits strongly oversamples occupied
主張の抜粋: Empirical occupied-fiber/rank frequencies are highly sensitive to sampling and search depth. Sampling t-values obtained from already-found Master-Hits strongly oversamples occupied positive-rank fibers. Separately, using a fixed point-search bound while the Pythagorean base size grows creates a fake decline in observed
対象・測度: computational scans of the K_c rational fibration.
依存関係: M3-FIB-FW-001 and explicit point search on valid Pythagorean base values.
再開条件の抜粋: a rigorously scaled search protocol or, preferably, an exact moving-base counting theorem.
旧詳細位置: LEGACY-COLD Sections25.2, 26.3 and 27.1.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 360645
SOURCE_END: 362356
SOURCE_SHA256: a1d99758a3a3dc16bd93c06dbfa41ad7236ee53dd91742a26b550f4f43740dc4

## M3-FIB-SCAN-FW-001
TYPE: COMPUTATIONAL_FIREWALL
STATUS: FROZEN


CLAIM:
Empirical occupied-fiber/rank frequencies are highly sensitive to sampling and search depth.
Sampling t-values obtained from already-found Master-Hits strongly oversamples occupied positive-rank fibers.
Separately, using a fixed point-search bound while the Pythagorean base size grows creates a fake decline in observed occupancy: in the archive, enlarging the search bound by 3x recovered 17 of 75 previously "not found" cases and raised the apparent 10.7% bucket to about 31%.
Therefore neither "40/40 found fibers have rank>=1" nor a fixed-bound declining occupancy curve estimates the underlying base distribution.


POPULATION:
computational scans of the K_c rational fibration.


HEIGHT:
finite search diagnostics only.


DEPENDS_ON:
M3-FIB-FW-001 and explicit point search on valid Pythagorean base values.


IMPLIES:
fiber-density experiments require unbiased base selection and a search bound scaled with base complexity.


ALIASES:
occupied-fiber selection bias;
fixed-search-bound fake decline;
fibration scan bias firewall.


DUPLICATE_OF:
M3-FIB-FW-001 states the stronger algebraic requirement that t itself be physical; this card concerns statistical/search bias after valid bases are chosen.


SUPERSEDES:
the old 40/40 interpretation and the initial declining-density plot.


DO_NOT_REPEAT:
Do not interpret "not found" as rank zero or unoccupied.
Do not compare occupancy fractions across growing base ranges with a fixed point-search cutoff.


REOPEN_CONDITION:
a rigorously scaled search protocol or, preferably, an exact moving-base counting theorem.


DETAIL_DOC:
LEGACY-COLD Sections25.2, 26.3 and 27.1.


---
