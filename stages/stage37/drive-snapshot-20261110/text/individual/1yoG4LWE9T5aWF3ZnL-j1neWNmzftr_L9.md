# M3-T11-081 — x=-1/8 Sophie-Germain residual kernel and distinguished negative-square 2-descent point

CARD_ID: M3-T11-081
CANONICAL_CARD_KEY: M3-T11-081
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-081
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / SOPHIE-GERMAIN ROUTER / NO POWER SAVING
種別: EXACT_STRUCTURE / THEOREM_ROUTER / LITERATURE_FIREWALL
要点: x=-1/8 moving D is routed to one fixed Sophie-Germain quartic with an actual large square divisor and a distinguished negative-square 2-descent point.
主張の抜粋: For primitive conic parameters, F(r,s)=r^4+4s^4=D*(epsilon*M_rel*h)^2. With W=epsilon*M_rel*h, alpha=2rs/W, beta=(r^2-2s^2)/W, gamma=(r^2+2s^2)/W give P_D=(-alpha^2,alpha*beta*gamma) on Y^2=X^3-D^2X with X+D=beta^2 and X-D=-gamma^2. Thus every realized D lies in this distinguished congruent-number 2-descent class. No support saving is claimed.
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh physical x=-1/8 singular carrier, exact R<=B.
依存関係: M3-T11-035; M3-T11-046; hostile-audit-passed M3-T11-080; primitive x=-1/8 conic parameterization.
再開条件の抜粋: Reopen only if the audited x=-1/8 conic normalization, F=D*W^2 identity, point formula, or nondegeneracy is retracted. The 081 point is the same rational point as 082 and carries no independent saving.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 91.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 819326
SOURCE_END: 823127
SOURCE_SHA256: 7560eabb29149de8b905d9f3389af8091556d5e8e9337d2d9e89ef77ea087409

CARD_ID: M3-T11-081
TITLE: x=-1/8 Sophie-Germain residual kernel and distinguished negative-square 2-descent point
TYPE: EXACT_STRUCTURE / THEOREM_ROUTER / LITERATURE_FIREWALL
STATUS: PROVISIONAL EXACT CONSEQUENCE / HOSTILE_AUDIT_REQUIRED / NO POWER SAVING
ROUTE: TrivialSplitCyclicDirectionOneThird
CLAIM:
On the exact x=-1/8 carrier, with primitive conic parameters
a=(r^2-2*s^2)/epsilon, b=2*r*s/epsilon, c=(r^2+2*s^2)/epsilon,
the fixed decomposable quartic
F(r,s)=r^4+4*s^4=epsilon^2*N_u.
Using audited M3-T11-080 and M3-T11-046,
D=sf(N_u/M_rel^2)=sf(F(r,s)),
gcd(D,M_rel)=1,
and there is h>=1 with
F(r,s)=D*(epsilon*M_rel*h)^2.
Thus every realized moving D is a squarefree kernel of one fixed Sophie-Germain quartic together with an actual large square-divisor witness divisible by M_rel.


Put W=epsilon*M_rel*h and
alpha=2*r*s/W,
beta=(r^2-2*s^2)/W,
gamma=(r^2+2*s^2)/W.
Then
gamma^2-alpha^2=D,
gamma^2-beta^2=2*alpha^2,
and
P_D=(-alpha^2,alpha*beta*gamma)
is a rational point on
E_D: Y^2=X^3-D^2*X,
with
X=-alpha^2, X+D=beta^2, X-D=-gamma^2.
On the nondegenerate physical carrier the ordinate is nonzero. Hence every realized D lies in this distinguished negative-square 2-descent class; the standard point-to-triangle formulas give a rational right triangle of area D, so realized D is a congruent number.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh physical endpoints on the x=-1/8 singular carrier; exact physical R<=B retained.
DEPENDS_ON:
M3-T11-035; M3-T11-046; hostile-audit-passed M3-T11-080; primitive x=-1/8 conic parameterization.
IMPLIES:
The canonical moving-D gate is unchanged, but its preferred supporting theorem species is now a same-measure large-square-divisor / distinguished 2-descent support theorem on the fixed quartic F(r,s)=r^4+4*s^4.
CANONICAL_RECEIVER:
XMinusOneEighthResidualSquarefreeKernelSupportOneTwelfth.
SUPPORTING_ATTACK:
XMinusOneEighthSophieGermainNegativeSquare2DescentSupport.
LITERATURE_PREFLIGHT:
Ambient power-free-value theorems for binary forms (Greaves; Stewart-Top; Xiao) do not themselves yield the required fixed-power support deficit: they concern ambient binary-form values rather than the exact physical Stage37 subpopulation carrying M_rel|W. Generic congruent-number density is likewise not an exact-M3 saving.
CREDIT_LIMIT:
No active-D support deficit, no x=-1/8 carrier power saving, no generic fixed-x theorem, no primary-gate closure, no endpoint credit, and no P(B)/M3(B) credit.
DUPLICATE_OF:
None. The Sophie-Germain factorization itself is already present in M3-T11-046 ancestry; the new content is the exact residual-kernel equation with the large square-divisor witness and the explicit distinguished negative-square 2-descent point.
DO_NOT_REPEAT:
Do not award credit for the factorization alone; do not import ambient squarefree/congruent-number density; do not charge the old M_rel^-2 determinant.
REOPEN_CONDITION:
Retract the M3-T11-046/080 fresh valuation and residual-kernel identities; find an algebraic error in F=D*W^2 or P_D; or show the asserted nondegenerate physical branch permits alpha*beta*gamma=0.
NEXT_LEGAL_ACTION:
Hostile-audit M3-T11-081. In mainbatch, without theorem credit from 081, attack the exact same-measure support of D through F(r,s)=D*W^2 with M_rel|W and the distinguished negative-square 2-descent class, or derive the physical R<=B -> (r,s,W) height/range adapter needed for a large-square-divisor theorem.
FLAGS:
M3_T11_X_MINUS_ONE_EIGHTH_SOPHIE_GERMAIN_KERNEL_ROUTER=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_NEGATIVE_SQUARE_2DESCENT_POINT=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_REALIZED_D_CONGRUENT=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_ACTIVE_D_SUPPORT_DEFICIT_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


---
