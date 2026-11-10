# M3-DELTA-002 — FixedBaseDeltaQuartic

CARD_ID: M3-DELTA-002
CANONICAL_CARD_KEY: M3-DELTA-002
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-DELTA-002
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: For a fixed primitive Pythagorean base (P,Q,W), every signed-squarefree delta slice has the smooth even quartic y^2 = -delta*P*Q*t^4 +W^2*t^2 -(P*Q)/delta. Its binary-quartic invar
主張の抜粋: For a fixed primitive Pythagorean base (P,Q,W), every signed-squarefree delta slice has the smooth even quartic y^2 = -delta*P*Q*t^4 +W^2*t^2 -(P*Q)/delta. Its binary-quartic invariants and geometric Jacobian j-invariant are independent of delta because the product of the outer coefficients is (PQ)^2. Thus delta change
対象・測度: Section35 fixed-base squareclass/descent slices.
依存関係: M3-DELTA-001.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD route-audit Section14 delta audit.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 336304
SOURCE_END: 337549
SOURCE_SHA256: 11f68cc749413dc4f2c5d6014ee1754cc0efba01230a53e06123b4727239196c

## M3-DELTA-002
TYPE: THEOREM
STATUS: PROVED_EXACT


CLAIM:
For a fixed primitive Pythagorean base (P,Q,W), every signed-squarefree delta slice has the smooth even quartic
y^2
=
-delta*P*Q*t^4
+W^2*t^2
-(P*Q)/delta.
Its binary-quartic invariants and geometric Jacobian j-invariant are independent of delta because the product of the outer coefficients is (PQ)^2.
Thus delta changes the arithmetic twist/torsor class but creates no new elliptic moduli dimension.


POPULATION:
Section35 fixed-base squareclass/descent slices.


HEIGHT:
fixed-base structural theorem.


DEPENDS_ON:
M3-DELTA-001.


IMPLIES:
the delta descent and the moving elliptic-fibration route share the same moving-base quantifier; delta contributes only subpolynomial twist classes per base.


ALIASES:
FixedBaseDeltaQuartic;
DeltaTwistNoNewModuli;
R2R3 structural merge input.


DUPLICATE_OF:
M3-DELTA-001 gives the squareclass support; this card describes the geometry of each slice.


SUPERSEDES:
treating delta as an independent global moduli parameter.


DO_NOT_REPEAT:
Do not count the delta slices as a second independent closure mechanism from the moving-base fibration.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD route-audit Section14 delta audit.


---
