# M3-NORM-001 — PrimitiveNormRectangle

CARD_ID: M3-NORM-001
CANONICAL_CARD_KEY: M3-NORM-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-NORM-001
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: There are positive odd primitive rectangle coordinates a,c,d0,k with X^2=a*c*d0*k and P=(d0*a+c*k)/2, Y=(c*k-d0*a)/2, Q=(d0*c+a*k)/2, Z=(a*k-d0*c)/2. Define the primitive Gaussian 
主張の抜粋: There are positive odd primitive rectangle coordinates a,c,d0,k with X^2=a*c*d0*k and P=(d0*a+c*k)/2, Y=(c*k-d0*a)/2, Q=(d0*c+a*k)/2,
対象・測度: exact primitive physical M3.
依存関係: the Section98 cross-gcd decomposition and M3-ONE-001.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Section100.1-100.3.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 300263
SOURCE_END: 301385
SOURCE_SHA256: 27a356aec20d3e50a0b7231c30d835369f64b5c5328e06009ce79a56089cef75

## M3-NORM-001
TYPE: EXACT_STRUCTURE
STATUS: PROVED_EXACT


CLAIM:
There are positive odd primitive rectangle coordinates a,c,d0,k with
X^2=a*c*d0*k
and
P=(d0*a+c*k)/2,
Y=(c*k-d0*a)/2,
Q=(d0*c+a*k)/2,
Z=(a*k-d0*c)/2.
Define the primitive Gaussian norms
N_-=(a^2+c^2)/2,
N_+=(d0^2+k^2)/2.
Then
PQ-YZ=d0*k*N_-,
PQ+YZ=a*c*N_+,
and exactly
R_phys^2=N_-*N_+.
Thus the physical height cutoff is the exact product region
N_-*N_+<=B^2.


POPULATION:
exact primitive physical M3.


HEIGHT:
exact physical R<=B.


DEPENDS_ON:
the Section98 cross-gcd decomposition and M3-ONE-001.


IMPLIES:
the one-factor problem is compressed to two primitive sum-of-two-squares norms with exact product height.


ALIASES:
PrimitiveNormRectangle;
TwoPrimitiveNormDictionary;
ExactPhysicalHeightProduct.


DUPLICATE_OF:
M3-QUOT-001 is an earlier transverse-fibration integral model; this is the later norm-rectangle compression.


SUPERSEDES:
parameter-box height models for this route.


DO_NOT_REPEAT:
Do not replace N_-*N_+<=B^2 by independent boxes without proof.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Section100.1-100.3.


---
