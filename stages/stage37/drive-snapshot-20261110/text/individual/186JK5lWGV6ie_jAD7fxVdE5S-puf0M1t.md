# M3-ETA-001 — second squarefree core

CARD_ID: M3-ETA-001
CANONICAL_CARD_KEY: M3-ETA-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-ETA-001
現行一覧の状態: PROVED_EXACT
種別: INTERMEDIATE_LEMMA
要点: On the fixed-delta first-conic chart C=f^2+delta*e^2, D=f^2-delta*e^2, with gcd(e,f)=1, define m=f^4+delta^2*e^4=(C^2+D^2)/2 and let eta=sqf(m)>0. Then gcd(delta,m)_odd=1 and every
主張の抜粋: On the fixed-delta first-conic chart C=f^2+delta*e^2, D=f^2-delta*e^2, with gcd(e,f)=1, define m=f^4+delta^2*e^4=(C^2+D^2)/2 and let eta=sqf(m)>0. Then gcd(delta,m)_odd=1 and every odd prime dividing eta is split, hence eta_odd is supported on primes congruent to 1 mod 4. On the endpoint locus, the endpoint equation fo
対象・測度: endpoint points inside the fixed-delta first-conic parameterization.
依存関係: primitive first-conic coordinates and the endpoint square parity argument modulo primes dividing eta.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD route-audit Sections33.1, 33.3 and 33.4.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 375562
SOURCE_END: 377044
SOURCE_SHA256: df850ba7f55810c76afdbf49f70513427eaf27e4d4a5192f3e5e1ae262f8acfc

## M3-ETA-001
TYPE: INTERMEDIATE_LEMMA
STATUS: PROVED_EXACT


CLAIM:
On the fixed-delta first-conic chart
C=f^2+delta*e^2,
D=f^2-delta*e^2,
with gcd(e,f)=1, define
m=f^4+delta^2*e^4=(C^2+D^2)/2
and let eta=sqf(m)>0.
Then gcd(delta,m)_odd=1 and every odd prime dividing eta is split, hence eta_odd is supported on primes congruent to 1 mod 4.
On the endpoint locus, the endpoint equation forces
eta_odd | X*Y | P*Q,
so in particular
eta_odd | rad(PQ).
Together with delta_odd | rad(PQ), both moving squarefree cores are restricted to the fixed Pythagorean base support.


POPULATION:
endpoint points inside the fixed-delta first-conic parameterization.


HEIGHT:
structural endpoint condition; physical height unchanged.


DEPENDS_ON:
primitive first-conic coordinates and the endpoint square parity argument modulo primes dividing eta.


IMPLIES:
for one fixed Pythagorean base, both delta_odd and eta_odd have only
2^omega(PQ)=(PQ)^o(1)
possible odd supports.


ALIASES:
second squarefree core;
endpoint CM-support synchronization;
eta support on rad(PQ).


DUPLICATE_OF:
M3-DELTA-001 controls the first squarefree core delta; this card is the distinct endpoint-only second core eta.


SUPERSEDES:
treating eta as a polynomially free moving squareclass on a fixed base.


DO_NOT_REPEAT:
The eta restriction is endpoint-only; do not impose eta_odd|rad(PQ) on arbitrary M3 packets.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD route-audit Sections33.1, 33.3 and 33.4.


---
