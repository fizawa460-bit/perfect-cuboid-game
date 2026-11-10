# M3-COMMON-001 — DualGaussianRootPacket

CARD_ID: M3-COMMON-001
CANONICAL_CARD_KEY: M3-COMMON-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-COMMON-001
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: For fixed common norm core h, the primitive Gaussian ratios (a:c) and (d0:k) each lie on at most 2^omega(h) Gaussian root lines modulo h. Thus the pair lies in at most 4^omega(h)=h
主張の抜粋: For fixed common norm core h, the primitive Gaussian ratios (a:c) and (d0:k) each lie on at most 2^omega(h) Gaussian root lines modulo h. Thus the pair lies in at most 4^omega(h)=h^o(1) dual root packets. Within one fixed pair of root classes, the primitive rectangle count obeys the determinant bound O((1+Area_-/h)*(1+
対象・測度: Section100 primitive norm rectangles with h|N_- and h|N_+.
依存関係: M3-NORM-001 and Gaussian roots of -1 modulo prime powers.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Section101, Theorems 101-A and 101-B.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 303511
SOURCE_END: 304698
SOURCE_SHA256: 68082e049a1bea602389110007df78dd12fc76b36dc65f55c3efa33b46dcf4b6

## M3-COMMON-001
TYPE: THEOREM
STATUS: PROVED_EXACT


CLAIM:
For fixed common norm core h, the primitive Gaussian ratios
(a:c) and (d0:k)
each lie on at most 2^omega(h) Gaussian root lines modulo h.
Thus the pair lies in at most
4^omega(h)=h^o(1)
dual root packets.
Within one fixed pair of root classes, the primitive rectangle count obeys the determinant bound
O((1+Area_-/h)*(1+Area_+/h)).


POPULATION:
Section100 primitive norm rectangles with h|N_- and h|N_+.


HEIGHT:
packet/local lattice statement; physical-height globalization is separate.


DEPENDS_ON:
M3-NORM-001 and Gaussian roots of -1 modulo prime powers.


IMPLIES:
the common core h produces simultaneous transverse lattice spacing on both primitive norm pairs.


ALIASES:
DualGaussianRootPacket;
DualRootPacketLatticeBound.


DUPLICATE_OF:
related to M3-KMINUS-001 but uses the full common core h rather than only its squarefree kernel.


SUPERSEDES:
single-root-line treatments that use only one Gaussian pair.


DO_NOT_REPEAT:
Do not multiply the two root-line savings again after using the joint determinant packet.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Section101, Theorems 101-A and 101-B.


---
