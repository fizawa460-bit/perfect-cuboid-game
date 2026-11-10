# M3-T11-019 — Six-bilinear Plucker eliminants on the active-tau selector

CARD_ID: M3-T11-019
CANONICAL_CARD_KEY: M3-T11-019
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-019
現行一覧の状態: PROVED_EXACT_STRUCTURE / DETERMINANT_PREFLIGHT_OPEN
要点: Six-bilinear Plucker eliminants on the active-tau selector
主張の抜粋: Homogenize the Section-20 torus coordinates by t_i=v_i/u_i, H_i=u_i^2+v_i^2. Define A_ij=u_i*u_j+v_i*v_j, B_ij=v_i*u_j-u_i*v_j, F_ij^+=A_ij+B_ij, F_ij^-=A_ij-B_ij. Then the six-bilinear square selector is, up to a square denominator, W^2 = 2* product_{i<j} F_ij^+ F_ij^-. For fixed i, the map (u_j,v_j)->(F_ij^+,F_ij^-) has exact determinant 2H_i. The six factors satisfy exact charged-once eliminants: F_12^+ F_13^+ + F_12^- F_13^- = H_1(F_23^+ + F_23^-), F_12^+ F_13^- - F_12^- F_13^+ = -H_1(F_23^+ - F_23^-), together with cyclic permutations. Thus two factor-pairs incident to one torus core reconstruct the third pair with denominator H_i.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 21.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 386200
SOURCE_END: 387962
SOURCE_SHA256: 4d115bded6ec7913d84f0893b4e48c43d485101b3db759731e5ad25899a4e6f9

CARD_ID: M3-T11-019
TITLE: Six-bilinear Plucker eliminants on the active-tau selector
STATUS: PROVED_EXACT_STRUCTURE / DETERMINANT_PREFLIGHT_OPEN
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
Homogenize the Section-20 torus coordinates by


t_i=v_i/u_i,
H_i=u_i^2+v_i^2.


Define


A_ij=u_i*u_j+v_i*v_j,
B_ij=v_i*u_j-u_i*v_j,
F_ij^+=A_ij+B_ij,
F_ij^-=A_ij-B_ij.


Then the six-bilinear square selector is, up to a square denominator,


W^2
=
2*
product_{i<j}
F_ij^+ F_ij^-.


For fixed i, the map


(u_j,v_j)->(F_ij^+,F_ij^-)


has exact determinant


2H_i.


The six factors satisfy exact charged-once eliminants:


F_12^+ F_13^+ + F_12^- F_13^-
=
H_1(F_23^+ + F_23^-),


F_12^+ F_13^- - F_12^- F_13^+
=
-H_1(F_23^+ - F_23^-),


together with cyclic permutations.


Thus two factor-pairs incident to one torus core reconstruct the third pair with denominator H_i.


CARD_ROUTER_MATCH:
This meets the structural reopen condition in M3-A-GATE-001 for a charged-once eliminant.


It is theorem-species adjacent to M3-CROSSCORE-002 but not a duplicate:
the old card is a different reciprocal-product identity on a different physical common-core measure.


NO_CREDIT_YET:
No determinant or lattice saving is claimed until it is proved that the factor H_i is genuinely uncharged on the fixed-content active-tau measure and that the pushforward multiplicity/height contract is exact.


NEXT_ATTACK:
CyclicSixBilinearEliminantDeterminantNovelty.


DO_NOT_REPEAT:
Do not multiply the determinant 2H_i by an already-paid four-core/tau spacing.
Do not import M3-CROSSCORE-002 savings across measures.
Do not call a generic determinant theorem before proving the exact physical-height adapter.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 21.


---
