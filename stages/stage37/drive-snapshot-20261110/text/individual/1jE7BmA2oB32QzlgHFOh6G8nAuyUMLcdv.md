# M3-HIST16-ONEFACE-001 — Stage16 one-face baseline

CARD_ID: M3-HIST16-ONEFACE-001
CANONICAL_CARD_KEY: M3-HIST16-ONEFACE-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-HIST16-ONEFACE-001
現行一覧の状態: PROVED_AUDITED
種別: THEOREM_RESULT / CAUSAL_DECOMPOSITION
要点: For primitive canonical positive cuboids 0<a<b<c, gcd(a,b,c)=1, with exact geometric cutoff R=sqrt(a^2+b^2+c^2)<=B and exactly one integral face diagonal, Stage16 proves M_1(B) asy
主張の抜粋: For primitive canonical positive cuboids 0<a<b<c, gcd(a,b,c)=1, with exact geometric cutoff R=sqrt(a^2+b^2+c^2)<=B and exactly one integral face diagonal, Stage16 proves M_1(B) asymp B^2 log B. The exact proof decomposes the unique integral face as one positive scale k times one primitive Euclid face, with the primitiv
対象・測度: primitive canonical cuboids with exactly one integral face diagonal; no integral-space-diagonal condition.
依存関係: Stage16 final R01; primitive Euclid decomposition AR-002; primitive/canonical convention AR-001.
再開条件の抜粋: a genuine leading-constant/full-asymptotic theorem for M_1(B), not another proof of the same order.
旧詳細位置: Stage16 final self-contained bundle R01; Stage16 checkpoints 30-60.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 500679
SOURCE_END: 502862
SOURCE_SHA256: 57b10034d7aea87612cd9b98f1eb7a09eb9c4f2c2c26424da04c954344cb8526

## M3-HIST16-ONEFACE-001
TYPE: THEOREM_RESULT / CAUSAL_DECOMPOSITION
STATUS: PROVED_AUDITED
CLAIM:
For primitive canonical positive cuboids
0<a<b<c, gcd(a,b,c)=1,
with exact geometric cutoff
R=sqrt(a^2+b^2+c^2)<=B
and exactly one integral face diagonal, Stage16 proves
M_1(B) asymp B^2 log B.
The exact proof decomposes the unique integral face as one positive scale k times one primitive Euclid face, with the primitive Pythagorean-face count
P(X) asymp X.
The upper bound is obtained from
M_1(B) <= B * sum_{k<=B} P(B/k),
while the lower construction keeps kh<=B/4, chooses B/3<z<=B/2 with (z,k)=1, and deletes the two accidental nondesignated-face square conditions by divisor-many factor-pair bounds.
The power drop from the unrestricted three-edge source is caused by the one-face Pythagorean restriction; the single logarithm comes from the harmonic scale sum over k.
Primitivity and canonicalization alter density/multiplicity but not the proved B-power/log order.
POPULATION:
primitive canonical cuboids with exactly one integral face diagonal; no integral-space-diagonal condition.
HEIGHT:
literal R=sqrt(a^2+b^2+c^2)<=B.
DEPENDS_ON:
Stage16 final R01; primitive Euclid decomposition AR-002; primitive/canonical convention AR-001.
IMPLIES:
the intrinsic Stage16 population order has polynomial exponent 2 and logarithmic power 1.
ALIASES:
Stage16 one-face baseline;
M1 B^2 log B theorem;
one-face Pythagorean dimension drop;
harmonic face-scale logarithm.
DUPLICATE_OF:
none; AR-001/002 provide reusable normalization/parametrization, not this Stage16 population synthesis.
SUPERSEDES:
finite-data exponent guesses for the exactly-one-face population.
DO_NOT_REPEAT:
Do not require integral space diagonal in this Stage16 population.
Do not charge the unique-face parametrization multiplicity as a separate saving.
Do not promote the accidental-square divisor deletion B^o(1) to a fixed-power gain.
Do not infer a leading asymptotic constant from the Theta/asymp theorem.
REOPEN_CONDITION:
a genuine leading-constant/full-asymptotic theorem for M_1(B), not another proof of the same order.
DETAIL_DOC:
Stage16 final self-contained bundle R01; Stage16 checkpoints 30-60.
---
