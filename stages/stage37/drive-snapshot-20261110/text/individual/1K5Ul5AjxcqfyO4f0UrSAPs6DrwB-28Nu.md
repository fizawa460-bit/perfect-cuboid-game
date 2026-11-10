# M3-T11-082 — x=-1/8 exact large-denominator point on the moving congruent-number twist

CARD_ID: M3-T11-082
CANONICAL_CARD_KEY: M3-T11-082
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-082
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / STANDARD-DENOMINATOR HEIGHT ADAPTER / NO POWER SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE_HEIGHT_ADAPTER / THEOREM_ROUTER
要点: x=-1/8 realized D carries an explicit rational point on E_D whose standard x-denominator root is exactly q=M_rel*h.
主張の抜粋: Write a^2+b^2=D*q^2 with q=M_rel*h. Then P_D=(-b^2/q^2,abc/q^3) lies on y^2=x^3-D^2x. Since q is odd and gcd(q,abc)=1, q is exactly the standard Weierstrass denominator root C_D, so M_rel|C_D. Also H_x(P_D)=max(b^2,q^2) with q^2<=H_x<=D*q^2. This is an exact height adapter, not a support saving.
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh physical x=-1/8 singular carrier, exact R<=B.
依存関係: M3-T11-046; hostile-audit-passed M3-T11-080; primitive x=-1/8 conic parameterization; M3-T11-081 as equivalent provenance only.
再開条件の抜粋: Reopen only if N_u=D*q^2, q=M_rel*h, gcd(q,a*b*c)=1, the standard denominator convention, or the naive height inequalities are invalidated. No saving follows from q>=M_rel alone.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 92.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 823127
SOURCE_END: 827115
SOURCE_SHA256: a95a2f7cda1e20a5315435a30857d1c6fba82d4c05f8c2eb8fe168cf62184ed1

CARD_ID: M3-T11-082
TITLE: x=-1/8 exact large-denominator point on the moving congruent-number twist
TYPE: EXACT_STRUCTURE / SAME_MEASURE_HEIGHT_ADAPTER / THEOREM_ROUTER
STATUS: PROVISIONAL EXACT CONSEQUENCE / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING
ROUTE: TrivialSplitCyclicDirectionOneThird
CLAIM:
On the exact x=-1/8 carrier write
N_u=a^2+b^2=D*q^2,
q>0.
Audited M3-T11-046/080 give q=M_rel*h with h>=1. The primitive conic c^2=a^2+2*b^2 then yields the explicit rational point
P_D=(-b^2/q^2, a*b*c/q^3)
on
E_D: y^2=x^3-D^2*x.
Indeed
x_D+D=a^2/q^2
and
x_D-D=-c^2/q^2.


Moreover q is odd and gcd(q,a*b*c)=1. Hence this is already standard Weierstrass denominator form:
x_D=A_D/C_D^2,
y_D=B_D/C_D^3,
A_D=-b^2,
B_D=a*b*c,
C_D=q=M_rel*h.
Therefore the actual fresh conductor satisfies M_rel|C_D exactly on this distinguished moving-twist point.
For H_x(P_D)=max(|A_D|,C_D^2),
q^2<=H_x(P_D)<=D*q^2.
Thus on M_rel>B^(1/12-eta),
C_D>B^(1/12-eta)
and
H_x(P_D)>B^(1/6-2*eta).


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh physical endpoints on the x=-1/8 singular carrier; exact physical R<=B retained.
DEPENDS_ON:
M3-T11-046; hostile-audit-passed M3-T11-080; primitive x=-1/8 conic parameterization. M3-T11-081 supplies equivalent provenance but is not required as theorem credit for the denominator calculation.
IMPLIES:
The moving-D gate can be attacked as a same-measure problem of counting squarefree twists E_D that carry the distinguished rational point with standard denominator root C_D divisible by M_rel, once the exact physical upper height/range and multiplicity adapter is supplied.
CANONICAL_RECEIVER:
XMinusOneEighthResidualSquarefreeKernelSupportOneTwelfth.
SUPPORTING_ATTACK:
XMinusOneEighthMovingTwistLargeDenominatorHeightSupport.
LITERATURE_FIREWALL:
Large denominator alone is not a rarity theorem on a positive-rank elliptic curve. Integral-point results for congruent-number curves do not directly cover the present q>1 point on the large-fresh branch. Generic twist-height theorems may be tested only after matching hypotheses and deriving the exact Stage37 R<=B height/range and multiplicity pushforward.
CREDIT_LIMIT:
No active-D support deficit, no x=-1/8 carrier power saving, no generic fixed-x theorem, no primary-gate closure, no endpoint credit, and no P(B)/M3(B) credit.
DUPLICATE_OF:
None found. Existing Stage37 denominator receivers concern other rational coordinates or other fixed curves. M3-T11-081 gives the negative-square 2-descent point but does not identify q as the exact standard Weierstrass denominator root carrying M_rel.
SUPERSEDES:
M3-T11-081 remains valid provisional provenance; M3-T11-082 becomes the preferred supporting attack because it exposes the fresh conductor in a standard elliptic height coordinate.
DO_NOT_REPEAT:
Do not treat q>=M_rel as a density saving; do not replace the exact physical image by all congruent-number points; do not apply integral-point theorems to q>1; do not recharge the old M_rel^-2 determinant.
REOPEN_CONDITION:
Retract M3-T11-046/080; find an error in N_u=D*q^2, q=M_rel*h, the point formula, or gcd(q,a*b*c)=1; or show that the standard denominator convention used here is incompatible with the integral model E_D:y^2=x^3-D^2*x.
NEXT_LEGAL_ACTION:
Hostile-audit M3-T11-082. In mainbatch, without theorem credit from 082, derive an exact physical R<=B upper range for D, q, and H_x(P_D) with B^o(1) pushforward multiplicity, then match or prove a theorem counting realized squarefree D in that denominator/height window.
FLAGS:
M3_T11_X_MINUS_ONE_EIGHTH_MOVING_D_POINT_EXPLICIT=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_MOVING_D_POINT_STANDARD_DENOMINATOR_EXACT=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_MOVING_D_POINT_DENROOT_MULTIPLE_OF_MREL=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_MOVING_D_POINT_NAIVE_HEIGHT_WINDOW=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_ACTIVE_D_SUPPORT_DEFICIT_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
---
