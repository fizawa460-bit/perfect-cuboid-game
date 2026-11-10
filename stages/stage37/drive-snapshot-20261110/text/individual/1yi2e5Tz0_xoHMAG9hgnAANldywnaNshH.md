# M3-FOURIER-001 — ExplicitPrimeFourierBounds

CARD_ID: M3-FOURIER-001
CANONICAL_CARD_KEY: M3-FOURIER-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-FOURIER-001
現行一覧の状態: PROVED_EXACT
種別: THEOREM
要点: For the four-variable polynomials E4,H4,E4H4 at a good prime p, additive Fourier coefficients satisfy: zero frequency O(p^(7/2)); one variable-pair degenerate frequency O(p^(5/2));
主張の抜粋: For the four-variable polynomials E4,H4,E4H4 at a good prime p, additive Fourier coefficients satisfy: zero frequency O(p^(7/2)); one variable-pair degenerate frequency O(p^(5/2)); generic nonzero frequency O(p^2). Consequently a prime incomplete box obeys |sum_box chi_p(...)| << V*p^(-1/2) + p^(1/2)*(AB+CF)*(log p)^2 
対象・測度: ambient four-variable boxes for E4,H4,E4H4.
依存関係: M3-FOUR-LOCAL-001 and explicit finite-field Fourier analysis.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Section113, Theorems 113-A through 113-C.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 328096
SOURCE_END: 329333
SOURCE_SHA256: e91317081fa5ef25db5a9c56586ac93f1d2596dbd560312c938d787771b22270

## M3-FOURIER-001
TYPE: THEOREM
STATUS: PROVED_EXACT


CLAIM:
For the four-variable polynomials E4,H4,E4H4 at a good prime p, additive Fourier coefficients satisfy:
zero frequency O(p^(7/2));
one variable-pair degenerate frequency O(p^(5/2));
generic nonzero frequency O(p^2).
Consequently a prime incomplete box obeys
|sum_box chi_p(...)|
<<
V*p^(-1/2)
+
p^(1/2)*(AB+CF)*(log p)^2
+
p^2*(log p)^4,
and the squarefree-modulus analogue is
<< q^epsilon [V*q^(-1/2)+q^(1/2)(AB+CF)+q^2].


POPULATION:
ambient four-variable boxes for E4,H4,E4H4.


HEIGHT:
usable inside physical dyadic decomposition, but not itself conditioned on M3.


DEPENDS_ON:
M3-FOUR-LOCAL-001 and explicit finite-field Fourier analysis.


IMPLIES:
the exact incomplete-sum ceiling for elementary completion methods is quantified.


ALIASES:
ExplicitPrimeFourierBounds;
PrimeIncompleteBoxCharacterBound;
SquarefreeIncompleteBoxCharacterBound.


DUPLICATE_OF:
none.


SUPERSEDES:
generic completion estimates that ignore the frequency-degeneracy hierarchy.


DO_NOT_REPEAT:
Do not claim these ambient box bounds already incorporate the E4-square M3 conditioning.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Section113, Theorems 113-A through 113-C.


---
