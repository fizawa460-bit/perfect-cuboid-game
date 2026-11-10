# M3-HIST16S-FACELESS-001 — Stage16S SPACE_ONLY theorem

CARD_ID: M3-HIST16S-FACELESS-001
CANONICAL_CARD_KEY: M3-HIST16S-FACELESS-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-HIST16S-FACELESS-001
現行一覧の状態: PROVED_AUDITED
種別: THEOREM_RESULT / FILTER_RESULT
要点: Let S_0(B) be the Stage16S integral-space-diagonal population with zero integral face diagonals, and define the faceful complement C_F(B)=N_S^all(B)-N_S^0(B). Stage16S proves, for 
主張の抜粋: Let S_0(B) be the Stage16S integral-space-diagonal population with zero integral face diagonals, and define the faceful complement C_F(B)=N_S^all(B)-N_S^0(B). Stage16S proves, for every epsilon>0, C_F(B)=O_epsilon(B^(1+epsilon)). The proof marks one integral face, writes a^2+b^2=e^2 and e^2+c^2=d^2, drops primitive/can
対象・測度: Stage16S SPACE_ONLY versus SPACE_AT_LEAST under the same exact R=d<=B cutoff.
依存関係: M3-HIST16S-SPACE-001; Stage16S faceful-complement divisor-bound proof.
再開条件の抜粋: a sharp asymptotic/order for C_F(B) or for its face-multiplicity components.
旧詳細位置: Stage16S final R01, faceful complement proof.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 509217
SOURCE_END: 511009
SOURCE_SHA256: 56243746d7fdc48f39df0f96d1ab5c061b93af0decc590227b1133f15e3a6c39

## M3-HIST16S-FACELESS-001
TYPE: THEOREM_RESULT / FILTER_RESULT
STATUS: PROVED_AUDITED
CLAIM:
Let S_0(B) be the Stage16S integral-space-diagonal population with zero integral face diagonals, and define the faceful complement
C_F(B)=N_S^all(B)-N_S^0(B).
Stage16S proves, for every epsilon>0,
C_F(B)=O_epsilon(B^(1+epsilon)).
The proof marks one integral face, writes
a^2+b^2=e^2 and e^2+c^2=d^2,
drops primitive/canonical filters for an upper bound, and controls the numbers of (e,c) and (a,b) by
r_2(d^2)<=4*tau(d^2)
and
r_2(e^2)<=4*tau(e^2).
After summing d<=B and the three face choices this is lower order than the quadratic S_all main term.
Therefore
N_S^0(B) ~ B^2/(32G)
and
N_S^0(B)/N_S^all(B) -> 1.
Thus, among primitive canonical integral-space-diagonal cuboids, having no integral face is asymptotically dominant.
POPULATION:
Stage16S SPACE_ONLY versus SPACE_AT_LEAST under the same exact R=d<=B cutoff.
HEIGHT:
literal R=d<=B.
DEPENDS_ON:
M3-HIST16S-SPACE-001; Stage16S faceful-complement divisor-bound proof.
IMPLIES:
deleting every one-face/two-face/three-face object does not alter the quadratic main term of the ambient integral-space-diagonal population.
ALIASES:
Stage16S SPACE_ONLY theorem;
faceful complement bound;
zero-face dominance under space integrality.
DUPLICATE_OF:
none.
SUPERSEDES:
finite-census impressions about the relative frequency of faceful space-integral cuboids.
DO_NOT_REPEAT:
Do not claim a sharp order or asymptotic constant for C_F(B).
Do not split the O_epsilon(B^(1+epsilon)) bound into separate asymptotics for face multiplicities 1,2,3.
Do not use finite Stage16S census as theorem input.
REOPEN_CONDITION:
a sharp asymptotic/order for C_F(B) or for its face-multiplicity components.
DETAIL_DOC:
Stage16S final R01, faceful complement proof.
---
