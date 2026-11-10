# M3-EXP-FW-001 — finite-field admissibility bug

CARD_ID: M3-EXP-FW-001
CANONICAL_CARD_KEY: M3-EXP-FW-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-EXP-FW-001
現行一覧の状態: FROZEN
種別: CORRECTED_BUG
要点: Finite-field Master-Hit experiments must exclude the hypotenuse-degenerate states W1=r^2+s^2 == 0 mod p from the admissible domain. An early experiment omitted this condition and o
主張の抜粋: Finite-field Master-Hit experiments must exclude the hypotenuse-degenerate states W1=r^2+s^2 == 0 mod p from the admissible domain. An early experiment omitted this condition and obtained exact 0/1 square frequencies at small primes. For small split primes, the remaining exclusions can accidentally coincide with the W1
対象・測度: finite-field Master-Hit residue experiments.
依存関係: the exact admissibility conditions for primitive Pythagorean source data.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Section1.2.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 356510
SOURCE_END: 357869
SOURCE_SHA256: 2f9eea2f0f3cf6c928dc1715226af4613c57fd07d3bafda5901407deacebca7b

## M3-EXP-FW-001
TYPE: CORRECTED_BUG
STATUS: FROZEN


CLAIM:
Finite-field Master-Hit experiments must exclude the hypotenuse-degenerate states
W1=r^2+s^2 == 0 mod p
from the admissible domain.
An early experiment omitted this condition and obtained exact 0/1 square frequencies at small primes.
For small split primes, the remaining exclusions can accidentally coincide with the W1-degenerate lines, so small-p panels can be dominated by degeneration rather than the generic local law.


POPULATION:
finite-field Master-Hit residue experiments.


HEIGHT:
local diagnostic only.


DEPENDS_ON:
the exact admissibility conditions for primitive Pythagorean source data.


IMPLIES:
local experiments used as evidence for the generic Weil/character law must remove W1=0 and other stated degeneracies before statistics are interpreted.


ALIASES:
finite-field admissibility bug;
hypotenuse-degenerate local panel;
small-prime degeneration firewall.


DUPLICATE_OF:
none.


SUPERSEDES:
the initial p=5,11,13 diagnostic in which Pr(M square) collapsed to 0 or 1.


DO_NOT_REPEAT:
Do not use very small-prime raw panels as evidence for the generic local density until all admissibility degeneracies are removed.
Do not interpret exact 0/1 frequencies as arithmetic structure before checking W1=0.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Section1.2.


---
