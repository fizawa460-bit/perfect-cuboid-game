# M3-GCD-003 — kappa-four mean-gcd law

CARD_ID: M3-GCD-003
CANONICAL_CARD_KEY: M3-GCD-003
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-GCD-003
現行一覧の状態: PROVED_CONDITIONAL
種別: AUXILIARY
要点: With f(n)=phi(n)*(rho(n)/n^2)^2 and g(n)=n*f(n), one has exactly for odd primes g(p)=4-8/p+5/p^2-1/p^3. Thus the Selberg-Delange mean-value parameter is kappa=4, predicting a trunc
主張の抜粋: With f(n)=phi(n)*(rho(n)/n^2)^2 and g(n)=n*f(n), one has exactly for odd primes g(p)=4-8/p+5/p^2-1/p^3. Thus the Selberg-Delange mean-value parameter is kappa=4, predicting a truncated sum sum_{n<=D} f(n) of order (log D)^3. The exact kappa=4 prime-level calculation is proved; the archive did not verify every analytic-
対象・測度: historical parameter-side gcd distribution.
依存関係: M3-GCD-002.
再開条件の抜粋: verify the remaining standard Selberg-Delange analytic hypotheses if an exact asymptotic constant becomes load-bearing.
旧詳細位置: LEGACY-COLD Section 26.4.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 269518
SOURCE_END: 270648
SOURCE_SHA256: be10c9ee2b8a82223e905148ccdb307ddee8147bed3ec622f6aafba32c1ff3c7

## M3-GCD-003
TYPE: AUXILIARY
STATUS: PROVED_CONDITIONAL


CLAIM:
With f(n)=phi(n)*(rho(n)/n^2)^2 and g(n)=n*f(n), one has exactly for odd primes
g(p)=4-8/p+5/p^2-1/p^3.
Thus the Selberg-Delange mean-value parameter is kappa=4, predicting a truncated sum
sum_{n<=D} f(n) of order (log D)^3.
The exact kappa=4 prime-level calculation is proved; the archive did not verify every analytic-continuation/growth hypothesis needed for a full Selberg-Delange asymptotic.


POPULATION:
historical parameter-side gcd distribution.


HEIGHT:
parameter cutoff D; not exact physical R<=B.


DEPENDS_ON:
M3-GCD-002.


IMPLIES:
explains the observed cubic-log growth and refines parameter-side Markov tail estimates.


ALIASES:
kappa-four mean-gcd law;
log-cube gcd growth mechanism.


DUPLICATE_OF:
none.


SUPERSEDES:
the earlier naive (log D)^4 Euler-product heuristic.


DO_NOT_REPEAT:
Do not label the full asymptotic as proved from the archive alone.


REOPEN_CONDITION:
verify the remaining standard Selberg-Delange analytic hypotheses if an exact asymptotic constant becomes load-bearing.


DETAIL_DOC:
LEGACY-COLD Section 26.4.


---
