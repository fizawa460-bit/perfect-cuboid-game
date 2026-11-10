# M3-T11-098 — Split dual 2-Kummer residual brackets complete-square collapse

CARD_ID: M3-T11-098
CANONICAL_CARD_KEY: M3-T11-098
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-098
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / FULL_SPLIT_2KUMMER_NO_GO / NO POWER SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE NO-DOUBLE-CHARGE / ANTI_LOOP_FIREWALL / DESCENT_PREFLIGHT
要点: The split-dual residual 2-Kummer brackets left open by M3-T11-097 factor as complete squares over the old source class, so the full ordinary split dual 2-Kummer tuple contains no new squareclass information.
主張の抜粋: With eta^2=Theta, kappa=N_0/b^2 and m=M_rel^2, B_+=(eta+kappa/2)^2/kappa and B_-=-(eta-kappa/2)^2/kappa. Hence q^2-alpha_+=-(4M_rel^2/kappa)(eta+kappa/2)^2 and q^2-alpha_-=-(4M_rel^2/kappa)(eta-kappa/2)^2. Every nonzero root-difference class is [-N_0], [Xp]=1, and the split-torsion special-value case again gives [-N_0]. Thus the ordinary split dual tuple is (1,[-N_0],[-N_0]) up to ordering.
対象・測度: Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B and theta!=0. Same physical measure; no fixed-power saving credit.
依存関係: M3-T11-096 hostile-audit PASS; M3-T11-097 provisional split-root formulas and notation.
再開条件の抜粋: Reopen if hostile audit rejects the bracket factorization or M3-T11-097 split-root identities, an audited dependency changes, or a genuinely non-Kummer invariant carries new same-measure information beyond (1,[-N_0],[-N_0]).
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 108.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 901482
SOURCE_END: 906069
SOURCE_SHA256: ba4e71f6b9b1e2db1ed36fb68a18a6a4f95d8b1ca58964c19ea9015e9b72620d

RESEARCH_CARD=M3-T11-098
---
CARD_ID=M3-T11-098
TITLE=Split dual 2-Kummer residual brackets complete-square collapse
STATUS=PROVISIONAL EXACT_REDUNDANCY / FULL_SPLIT_2KUMMER_NO_GO / HOSTILE_AUDIT_REQUIRED / NO_POWER_SAVING
TYPE=EXACT_STRUCTURE / SAME_MEASURE_NO_DOUBLE_CHARGE / ANTI_LOOP_FIREWALL / DESCENT_PREFLIGHT
CLAIM:
Retain M3-T11-097 notation on the surviving theta!=0 generic full-S branch, with M=M_rel, m=M^2, eta^2=Theta, kappa=(v+1)/M^2=N_0/b^2, and the dual split roots alpha_+=9+4theta+4sqrt(theta), alpha_-=9+4theta-4sqrt(theta). For the physical dual point Xp=q^2, M3-T11-097 writes
q^2-alpha_+=-4*M^2*B_+,
q^2-alpha_-=4*M^2*B_-,
B_+=eta+3omega-momega^2+mTheta,
B_-=eta-3omega+momega^2-mTheta.
Using audited M3-T11-096,
Theta=kappa*(kappa-12omega+4momega^2)/(4v),
v=m*kappa-1.
Hence exactly
3omega-momega^2+mTheta
=
kappa/2+(4Theta-kappa^2)/(4kappa),
and since eta^2=Theta,
B_+=(eta+kappa/2)^2/kappa,
B_-=-(eta-kappa/2)^2/kappa.
Therefore
q^2-alpha_+=-(4*M^2/kappa)*(eta+kappa/2)^2,
q^2-alpha_-=-(4*M^2/kappa)*(eta-kappa/2)^2.
For nonzero coordinates their K-squareclasses are both
[-1/kappa]=[-N_0],
while [Xp]=1.
If one displayed coordinate vanishes, then eta=+/-kappa/2, equivalently 4theta=(v+1)^2, and the dual image is split nonzero 2-torsion. The standard full-2-descent special value uses the product of root differences; because the nonzero root equals q^2 and the relevant root difference is -4*M^2*kappa in the corresponding sign convention, the same squareclass [-N_0] results.
Thus the full ordinary split dual 2-Kummer tuple is, up to ordering,
(1,[-N_0],[-N_0])
throughout the physical carrier. The residual bracket classes left open by M3-T11-097 contain no new squareclass information.
POPULATION:
Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical endpoint branch with exact R<=B and theta!=0. M3-T11-097 remains provisional.
HEIGHT:
No change. Exact physical R<=B measure.
DEPENDS_ON:
M3-T11-096 hostile-audit PASS; M3-T11-097 provisional split-dual formulas and notation.
IMPLIES:
The ordinary split dual 2-Kummer route, including the residual bracket classes left open by M3-T11-097, has zero independent fresh-conductor/support-saving credit. Genuinely non-Kummer higher descent and genuinely independent global moving-support/dispersion remain open.
ALIASES:
ThetaSplitDual2KummerResidualCollapse;
ThetaFullSplit2DescentOldClassFirewall;
ThetaResidualBracketCompleteSquare.
DUPLICATE_OF:
none. This strictly extends M3-T11-097 by closing its explicitly open residual split-2-Kummer bracket squareclasses.
SUPERSEDES:
The M3-T11-097 provisional flag M3_T11_DUAL_SPLIT_2KUMMER_RESIDUAL_CLASSES_OPEN=true, conditional on hostile-audit PASS of the 097->098 chain.
DO_NOT_REPEAT:
Do not revisit ordinary split 2-Kummer root differences, their residual brackets, the torsion special-value case, or multiplication-by-n Kummer variants as independent fresh-conductor savings after this chain passes audit.
REOPEN_CONDITION:
Hostile audit rejects the exact bracket factorization or the M3-T11-097 split-root identities; an audited dependency changes; or a genuinely non-Kummer invariant is proved to carry new same-physical-measure information beyond the tuple (1,[-N_0],[-N_0]).
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 108.
CREDIT:
No fixed-power moving-theta support deficit. No denominator-extreme closure. No primary-gate closure. No endpoint theorem. No P(B)/M3(B) limit. No Perfect Cuboid nonexistence credit.
FLAGS:
M3_T11_DUAL_SPLIT_2KUMMER_BRACKETS_COMPLETE_SQUARE=PROVISIONAL
M3_T11_DUAL_SPLIT_2KUMMER_RESIDUAL_CLASSES_OPEN=false
M3_T11_DUAL_SPLIT_2KUMMER_CLASSES_MINUS_N0=PROVISIONAL
M3_T11_DUAL_SPLIT_2KUMMER_TORSION_SPECIAL_VALUE_MINUS_N0=PROVISIONAL
M3_T11_FULL_SPLIT_2KUMMER_NEW_SAVING=false
M3_T11_THETA_NONKUMMER_HIGHER_DESCENT_OPEN=true
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
LATEST_RESEARCH_CARD=M3-T11-098
LATEST_AUDITED_RESEARCH_CARD=M3-T11-096
PROVISIONAL_FRONTIER_CARD=M3-T11-098
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CURRENT_ATTACK=GenericFullSThetaNonzeroFourthPowerSupportOneTwelfth|InteriorCharacterGlobalDispersion
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer|InteriorCharacterGlobalDispersion
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-097 and M3-T11-098 as one dependency chain. Mainbatch may continue only on genuinely non-Kummer higher-descent or global moving-support/dispersion information not determined by the theta/Kummer identities.
NEXT_RESEARCH_CARD_ID=M3-T11-099
