# M3-T11-044 — Fixed-E physical square lift genus-3 Prym split and reciprocal-involution firewall

CARD_ID: M3-T11-044
CANONICAL_CARD_KEY: M3-T11-044
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-044
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE / NEGATIVE_RESULT / FIREWALL
要点: For the retained fixed-E quartic Z^2=-F_e(x), physicality imposes x=u^2. The true square-x lift C_e: Z^2=-F_e(u^2) is a smooth genus-3 curve on every large-M_rel physical rational 
主張の抜粋: For the retained fixed-E quartic
対象・測度: Physical large-M_rel fixed-E fibers from the symmetric Stage37 route.
依存関係: The retained fixed-E quartic and exact E fourth-power denominator; audited Stage25 R504 even-octic reciprocal criterion.
再開条件の抜粋: An exact non-reciprocal elliptic factor with a compatible counting adapter, or a direct uniform genus-2/genus-3 counting theorem.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 51.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 655251
SOURCE_END: 657529
SOURCE_SHA256: 59921b2b418b9d1cef15fd3f4e42df27e3e4242afb15241bd966e357ed5985cb

## M3-T11-044
TITLE: Fixed-E physical square lift genus-3 Prym split and reciprocal-involution firewall
TYPE: EXACT_STRUCTURE / NEGATIVE_RESULT / FIREWALL
STATUS: PROVED_EXACT
CLAIM:
For the retained fixed-E quartic Z^2=-F_e(x), physicality imposes x=u^2.
The true square-x lift
C_e: Z^2=-F_e(u^2)
is a smooth genus-3 curve on every large-M_rel physical rational e.
Its involution u->-u has the existing elliptic quotient
E_e: Z^2=-F_e(x),
and the complementary involution (u,Z)->(-u,-Z) has the genus-2 quotient
H_e: V^2=-x*F_e(x).
Thus
Jac(C_e) is Q-isogenous to E_e x Jac(H_e).


For the even octic coefficients q4,q3,q2,q1,q0 of F_e(u^2), a Q-rational reciprocal commuting involution u->lambda/u would require
q0*q3^2-q4*q1^2=0.
Exact factorization gives
boxed:
q0*q3^2-q4*q1^2
=
4096*e^4*(e+4)^4*(e^2-12*e+48),
and
e^2-12*e+48=(e-6)^2+12.
Hence no nondegenerate rational e admits such a reciprocal involution.


POPULATION:
Physical large-M_rel fixed-E fibers from the symmetric Stage37 route.
HEIGHT:
Exact physical R<=B retained; this card proves geometry only, not a point count.
DEPENDS_ON:
The retained fixed-E quartic and exact E fourth-power denominator;
audited Stage25 R504 even-octic reciprocal criterion.
IMPLIES:
The direct reciprocal-second-elliptic-quotient route is uniformly closed.
The square-x lift leaves a genuine genus-2 Prym factor.
DOES_NOT_IMPLY:
No exclusion of exceptional non-bielliptic elliptic isogeny factors of Jac(H_e).
No fixed-E uniform B^o(1) point count.
No active-E support deficit.
No P(B)/M3(B) theorem.
ALIASES:
FixedESquareLiftGenus3;
FixedEPrymGenus2;
FixedEReciprocalSecondQuotientClosed.
DUPLICATE_OF:
NONE.
SUPERSEDES:
NONE.
DO_NOT_REPEAT:
Do not search for fixed-E uniformity by a generic Q-rational reciprocal involution u->lambda/u.
REOPEN_CONDITION:
An exact non-reciprocal elliptic factor with a compatible counting adapter, or a direct uniform genus-2/genus-3 counting theorem.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 51.
FLAGS:
M3_T11_FIXED_E_PHYSICAL_SQUARE_LIFT_GENUS3=true
M3_T11_FIXED_E_PRYM_GENUS2_QUOTIENT=true
M3_T11_FIXED_E_RECIPROCAL_SECOND_ELLIPTIC_QUOTIENT=false
M3_T11_FIXED_E_NONBIELLIPTIC_PRYM_FACTOR_EXCLUDED=false
M3_T11_FIXED_E_UNIFORM_BO1_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


---
