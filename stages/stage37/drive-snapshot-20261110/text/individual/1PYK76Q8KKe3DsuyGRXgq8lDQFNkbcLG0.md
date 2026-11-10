# M3-HIST16S-SPACE-001 — Stage16S SPACE_AT_LEAST theorem

CARD_ID: M3-HIST16S-SPACE-001
CANONICAL_CARD_KEY: M3-HIST16S-SPACE-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-HIST16S-SPACE-001
現行一覧の状態: PROVED_AUDITED
種別: THEOREM_RESULT / POPULATION_BASELINE
要点: For primitive canonical positive triples 0<a<b<c, gcd(a,b,c)=1, with exact geometric cutoff R=sqrt(a^2+b^2+c^2)<=B, let S_all(B) be the subpopulation with integral space diagonal R
主張の抜粋: For primitive canonical positive triples 0<a<b<c, gcd(a,b,c)=1, with exact geometric cutoff R=sqrt(a^2+b^2+c^2)<=B, let S_all(B) be the subpopulation with integral space diagonal R in
対象・測度: primitive canonical positive cuboids with integral space diagonal and no face-diagonal restriction.
依存関係: Stage16S final R01; Hurlimann 2015 working form as frozen by Stage16S; M3-HIST16-SOURCE-001.
再開条件の抜粋: a sharper effective asymptotic or secondary term for N_S^all(B).
旧詳細位置: Stage16S final self-contained interface bundle R01.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 506923
SOURCE_END: 509217
SOURCE_SHA256: e8e56e6e2153a60dd516700bb8ea05a971d1bf740e3d36ce8b7e1d048b8e0c2d

## M3-HIST16S-SPACE-001
TYPE: THEOREM_RESULT / POPULATION_BASELINE
STATUS: PROVED_AUDITED
CLAIM:
For primitive canonical positive triples
0<a<b<c, gcd(a,b,c)=1,
with exact geometric cutoff
R=sqrt(a^2+b^2+c^2)<=B,
let S_all(B) be the subpopulation with integral space diagonal R in Z.
Writing G=L(2,chi_4) for Catalan's constant, Stage16S proves
N_S^all(B) ~ B^2/(32G).
On every target object the positive integer space diagonal d satisfies d=R exactly, so d<=B iff R<=B with no height adapter.
The external load-bearing theorem is Hurlimann's asymptotic for distinct primitive positive Pythagorean cuboids with odd diagonal, together with the repeated-edge term O(B).
Stage16S proves the project-specific adapters: primitive objects have odd d, gcd(a,b,c)=1 iff gcd(a,b,c,d)=1 on the space equation, and repeated-edge objects are exactly the lower-order x^2+2y^2=d^2 correction needed to pass from unordered/distinct conventions to strict canonical ordering.
Combining with the frozen Stage16 source-universe theorem
U(B)=pi/(36*zeta(3))*B^3+O(B^2)
gives
N_S^all(B)/U(B) ~ [9*zeta(3)/(8*pi*G)]*B^(-1).
POPULATION:
primitive canonical positive cuboids with integral space diagonal and no face-diagonal restriction.
HEIGHT:
literal R<=B, equal to d<=B on the target.
DEPENDS_ON:
Stage16S final R01; Hurlimann 2015 working form as frozen by Stage16S; M3-HIST16-SOURCE-001.
IMPLIES:
integral space-diagonal integrality by itself has intrinsic polynomial cost exactly one power of B in the ambient primitive canonical cuboid population.
ALIASES:
Stage16S SPACE_AT_LEAST theorem;
primitive Pythagorean-cuboid baseline;
B^2/(32G) space-diagonal law;
intrinsic space cost B^-1.
DUPLICATE_OF:
none; Stage16 records the ambient source universe but not this integral-space-diagonal subpopulation theorem.
SUPERSEDES:
heuristic estimates of the unconditional space-diagonal population.
DO_NOT_REPEAT:
Do not impose any face-diagonal condition in S_all.
Do not use a comparable height in place of d=R.
Do not infer an effective error term not supplied by the external theorem.
Do not infer perfect-cuboid information from this ambient space-only baseline.
REOPEN_CONDITION:
a sharper effective asymptotic or secondary term for N_S^all(B).
DETAIL_DOC:
Stage16S final self-contained interface bundle R01.
---
