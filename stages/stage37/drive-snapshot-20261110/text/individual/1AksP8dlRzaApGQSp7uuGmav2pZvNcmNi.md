# M3-HIST15-FIXEDS-001 — Stage15 fixed-S squareclass sieve

CARD_ID: M3-HIST15-FIXEDS-001
CANONICAL_CARD_KEY: M3-HIST15-FIXEDS-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-HIST15-FIXEDS-001
現行一覧の状態: PROVED_EXACT
種別: THEOREM_RESULT / SAME_MEASURE_ADAPTER
要点: For every fixed finite set S of good split primes, Stage15 proves a congruence-refined asymptotic on the same physical exactly-two measure: M_{2,S}(B) = C_M2*(product_{p in S} rho_
主張の抜粋: For every fixed finite set S of good split primes, Stage15 proves a congruence-refined asymptotic on the same physical exactly-two measure: M_{2,S}(B) = C_M2*(product_{p in S} rho_p)*B(log B)^5 +o_S(B(log B)^5). Every integral-space-diagonal survivor satisfies all local parity conditions, so for fixed S limsup_{B->infi
対象・測度: Stage15 primitive canonical exactly-two ambient/survivor populations on exact R<=B.
依存関係: M3-HIST15-AMBIENT-001, M3-HIST15-LOCALDENS-001, Stage15 15-6dz/15-6-final; Arsenal AR-035 as reusable architecture only.
再開条件の抜粋: only for a stronger effective/uniform theorem, not for the frozen qualitative result.
旧詳細位置: Stage15 15-6dz/result.md; 15-6ea/result.md; 15-6-final.md; Stage15 final self-contained R02.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 494353
SOURCE_END: 496494
SOURCE_SHA256: 33a8d977624b328231dfbb6af3aa9976b6f23509da138bedd6d37f5796616a5c

## M3-HIST15-FIXEDS-001
TYPE: THEOREM_RESULT / SAME_MEASURE_ADAPTER
STATUS: PROVED_EXACT
CLAIM:
For every fixed finite set S of good split primes, Stage15 proves a congruence-refined asymptotic on the same physical exactly-two measure:
M_{2,S}(B)
=
C_M2*(product_{p in S} rho_p)*B(log B)^5
+o_S(B(log B)^5).
Every integral-space-diagonal survivor satisfies all local parity conditions, so for fixed S
limsup_{B->infinity} N_2(B)/M_2(B)
<= product_{p in S} rho_p.
Only after taking B->infinity is S enlarged.
Because the reciprocal-prime sum over split primes diverges and
1-rho_p=4/p+O(p^-2),
the ordered product tends to zero and Stage15 independently proves
N_2(B)/M_2(B)->0,
equivalently N_2(B)=o(B(log B)^5).
This is a direct Stage15 application of the reusable fixed-prime ordered-limit architecture, with the Stage15 local law and same-measure fixed-S asymptotic reproved rather than imported.
POPULATION:
Stage15 primitive canonical exactly-two ambient/survivor populations on exact R<=B.
HEIGHT:
exact R<=B.
DEPENDS_ON:
M3-HIST15-AMBIENT-001, M3-HIST15-LOCALDENS-001, Stage15 15-6dz/15-6-final; Arsenal AR-035 as reusable architecture only.
IMPLIES:
Stage15 has an internal causal zero-density theorem independent of the imported Stage14 half-power numerator bound.
ALIASES:
Stage15 fixed-S squareclass sieve;
same-measure ordered-limit causal thinning;
N2 over M2 tends to zero;
15-6dz/6ea causal theorem.
DUPLICATE_OF:
none; AR-035 is the reusable method, while this card records the Stage15-specific theorem instance and exact local factors.
SUPERSEDES:
attempts to prove Stage15 zero density by changing measure, growing the modulus inside a fixed-modulus theorem, or relying on finite census alone.
DO_NOT_REPEAT:
Fix S first, take B->infinity, and only then enlarge S.
Do not infer an effective decay rate without uniformity in growing S.
Do not multiply this qualitative sieve saving into M3-HIST15-QUANT-FW-001.
REOPEN_CONDITION:
only for a stronger effective/uniform theorem, not for the frozen qualitative result.
DETAIL_DOC:
Stage15 15-6dz/result.md; 15-6ea/result.md; 15-6-final.md; Stage15 final self-contained R02.
---
