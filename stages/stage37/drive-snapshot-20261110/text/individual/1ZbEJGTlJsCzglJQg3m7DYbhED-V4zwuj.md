# M3-PARAM-002 — fixed-finite-prime Master contraction

CARD_ID: M3-PARAM-002
CANONICAL_CARD_KEY: M3-PARAM-002
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-PARAM-002
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: For any fixed finite set S of sufficiently large good odd primes, CRT gives exact independence of the local Master residue states across p in S, hence Pr(H square at every p in S |
主張の抜粋: For any fixed finite set S of sufficiently large good odd primes, CRT gives exact independence of the local Master residue states across p in S, hence Pr(H square at every p in S | M square at every p in S) = product_{p in S}(1/2+O(p^(-1/2))). For S={p:p0<=p<=z}, the parameter-measure survival decays as exp(-Theta(z/lo
対象・測度: uniform Master-Hit parameter residue measure modulo the product modulus.
依存関係: M3-PARAM-001, CRT and standard prime-sum estimates.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Sections7-8.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 330550
SOURCE_END: 331834
SOURCE_SHA256: cccdd9eb6820ba423f1c982437474b277fee402441c4b49df15fdcc37e06feb9

## M3-PARAM-002
TYPE: THEOREM
STATUS: PROVED_EXACT


CLAIM:
For any fixed finite set S of sufficiently large good odd primes, CRT gives exact independence of the local Master residue states across p in S, hence
Pr(H square at every p in S | M square at every p in S)
=
product_{p in S}(1/2+O(p^(-1/2))).
For S={p:p0<=p<=z}, the parameter-measure survival decays as
exp(-Theta(z/log z))
as z->infinity.


POPULATION:
uniform Master-Hit parameter residue measure modulo the product modulus.


HEIGHT:
parameter-side only; no physical/canonical height transfer.


DEPENDS_ON:
M3-PARAM-001, CRT and standard prime-sum estimates.


IMPLIES:
the historical local algebra and growing-prime sieve are already strong on the ambient parameter measure; the unresolved issue is the same-measure physical adapter.


ALIASES:
fixed-finite-prime Master contraction;
parameter growing sieve;
CRT Master square sieve.


DUPLICATE_OF:
M3-LOCAL-GATE-001 asks for the missing exact-M3 analogue, not this parameter theorem.


SUPERSEDES:
claims that an additional Selberg-weight mechanism is necessary merely to obtain parameter-side growing-prime decay.


DO_NOT_REPEAT:
Never transfer exp(-Theta(z/log z)) directly to P(B)/M3(B).


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Sections7-8.


---
