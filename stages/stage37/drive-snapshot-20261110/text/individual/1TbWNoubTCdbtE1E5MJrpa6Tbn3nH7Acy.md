# M3-HIST15-LOCALDENS-001 — Stage15 split-prime local squareclass density

CARD_ID: M3-HIST15-LOCALDENS-001
CANONICAL_CARD_KEY: M3-HIST15-LOCALDENS-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-HIST15-LOCALDENS-001
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE / LOCAL_RESULT
要点: On the same charged Stage15 physical toric measure, the squareclass survivor condition at a prime is v_p(A)==v_p(B) mod 2. For inert odd primes p==3 mod 4, Gaussian norm valuations
主張の抜粋: On the same charged Stage15 physical toric measure, the squareclass survivor condition at a prime is v_p(A)==v_p(B) mod 2. For inert odd primes p==3 mod 4, Gaussian norm valuations are even and the exact local acceptance is rho_p=1. For every good split prime p==1 mod 4, after resolving the four toric corners the A- an
対象・測度: Stage15 primitive canonical exactly-two toric physical measure before imposing the integral-space-diagonal survivor condition.
依存関係: M3-HIST15-SQCLASS-001; Stage15 15-6dy.
再開条件の抜粋: none for the exact local density.
旧詳細位置: Stage15 15-6dy/result.md; Stage15 final self-contained R02.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 492568
SOURCE_END: 494353
SOURCE_SHA256: b424a1d8dc7ffddd12ba9afdf54dc86781241fdb6f7b855c09ca579f0b6c9fc9

## M3-HIST15-LOCALDENS-001
TYPE: EXACT_STRUCTURE / LOCAL_RESULT
STATUS: PROVED_EXACT
CLAIM:
On the same charged Stage15 physical toric measure, the squareclass survivor condition at a prime is
v_p(A)==v_p(B) mod 2.
For inert odd primes p==3 mod 4, Gaussian norm valuations are even and the exact local acceptance is rho_p=1.
For every good split prime p==1 mod 4, after resolving the four toric corners the A- and B-divisors decompose into smooth strict components with exactly controlled intersections, giving the exact acceptance density
rho_p=(p^4+4p^3+22p^2+4p+1)/((p+1)^2*(p^2+6p+1)).
Hence
1-rho_p=4p(p-1)^2/((p+1)^2*(p^2+6p+1))
=4/p+O(p^-2).
This density already integrates all p-adic valuation levels; prime powers are not independent extra rejection events.
POPULATION:
Stage15 primitive canonical exactly-two toric physical measure before imposing the integral-space-diagonal survivor condition.
HEIGHT:
local statement compatible with the global exact R<=B measure.
DEPENDS_ON:
M3-HIST15-SQCLASS-001; Stage15 15-6dy.
IMPLIES:
split primes give a genuine first-order local rejection, while inert primes give none.
ALIASES:
Stage15 split-prime local squareclass density;
rho_p exact formula;
15-6dy local parity law.
DUPLICATE_OF:
none; Arsenal AR-035 provides a reusable ordered-limit sieve architecture but does not contain this Stage15-specific local law.
SUPERSEDES:
heuristic Bernoulli-one-half or independent-prime models for the Stage15 survivor condition.
DO_NOT_REPEAT:
Do not charge p,p^2,p^3 as independent sieve factors.
Do not transfer rho_p to another population or measure.
Do not infer a fixed-power global saving from 1-rho_p~4/p.
REOPEN_CONDITION:
none for the exact local density.
DETAIL_DOC:
Stage15 15-6dy/result.md; Stage15 final self-contained R02.
---
