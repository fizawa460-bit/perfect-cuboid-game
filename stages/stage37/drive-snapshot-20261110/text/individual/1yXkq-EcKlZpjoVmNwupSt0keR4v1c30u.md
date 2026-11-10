# M3-T11-080 — x=-1/8 residual-squareclass j=1728 compression and fixed-D fiber receiver

CARD_ID: M3-T11-080
CANONICAL_CARD_KEY: M3-T11-080
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-080
現行一覧の状態: PROVED EXACT_STRUCTURE / FIXED_D_BO1_HOSTILE_AUDIT_PASS / ACTIVE_D_SUPPORT_OPEN
種別: THEOREM / EXACT_STRUCTURE / SAME_MEASURE_SUPPORT_COMPRESSION
要点: x=-1/8 residual cofactor squareclasses compress to one moving D; fixed-D physical multiplicity is now audited B^o(1).
主張の抜粋: Write D=d_-d_+=sf((a^2+b^2)/M_rel^2). The smooth quartic Z^2=-d_+^2 X^4+6D X^2-d_-^2 has Jacobian V^2=U(U-36D)(U+36D), j=1728 and full rational 2-torsion. Over fixed Q(i) it has a base point; Dujella uniform bounded-height counting plus 2^omega(D)=B^o(1) splittings gives fixed D + fixed packet => B^o(1). The moving realized-D support deficit remains open.
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh physical x=-1/8 singular carrier, exact R<=B.
依存関係: M3-T11-035; audited M3-T11-036 theorem species; M3-T11-046; Stage37-HOSTILE-AUDIT-M3-T11-080-PASS.
再開条件の抜粋: Reopen only if M3-T11-046 coprime/even-valuation structure is retracted, the quartic/Jacobian algebra fails, the fixed-field Q(i) torsor identification fails, or the polynomial-height/Dujella adapter is invalidated.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 89-90.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 811457
SOURCE_END: 819326
SOURCE_SHA256: f5c03f463cb80001ba7f873d46950a325c160f6dc4f59fbc069b064264e871f7

CARD_ID: M3-T11-080
TITLE: x=-1/8 residual-squareclass j=1728 compression and fixed-D fiber receiver
TYPE: EXACT_STRUCTURE / SAME_MEASURE_SUPPORT_COMPRESSION / THEOREM_CANDIDATE
STATUS: PROVISIONAL EXACT STRUCTURE / FIXED-D B^o(1) CANDIDATE / HOSTILE_AUDIT_REQUIRED / ACTIVE-D SUPPORT OPEN
ROUTE: TrivialSplitCyclicDirectionOneThird


CLAIM:
Retain M3-T11-035, the audited M3-T11-036 fixed-u theorem, and M3-T11-046. On the exact x=-1/8 singular carrier write
c^2=a^2+2*b^2,
N_u=a^2+b^2=(c-b)(c+b),
with c-b and c+b positive, odd, and coprime.


Define
d_- = sf(c-b),
d_+ = sf(c+b),
where sf denotes squarefree kernel. Write uniquely
c-b=d_-*y_-^2,
c+b=d_+*y_+^2,
with positive y_-,y_+ and gcd(y_-,y_+)=1.
Then d_-,d_+ are coprime squarefree, and with
D=d_-*d_+
one has exactly
D=sf(N_u)=sf(N_u/M_rel^2).
Every relative-fresh prime in M_rel occurs with even valuation in exactly one of c-b,c+b by M3-T11-046, hence
gcd(D,M_rel)=1.
This does NOT make D fixed or finite-S; D remains a moving residual squareclass parameter.


Eliminating b,c gives
c=(d_+*y_+^2+d_-*y_-^2)/2,
b=(d_+*y_+^2-d_-*y_-^2)/2,
and
(2a)^2=-d_+^2*y_+^4+6*D*y_+^2*y_-^2-d_-^2*y_-^4.
Thus, with
X=y_+/y_-,
Z=2a/y_-^2,
every physical point maps to the binary quartic
C_{d_-,d_+}:
Z^2=-d_+^2*X^4+6*D*X^2-d_-^2.


EXACT GEOMETRY:
The quartic discriminant is
2^14*d_-^6*d_+^6=2^14*D^6,
so every positive d_-,d_+ fiber is smooth genus one.
Its binary-quartic invariants are
I=48*D^2,
J=0.
Under the same scaled-Jacobian convention used in M3-T11-036, the Jacobian is
E_D:
V^2=U^3-1296*D^2*U
=U*(U-36D)*(U+36D).
Therefore every fiber has j=1728 and full rational 2-torsion. The quartic also has the canonical point
(X,Z)=(0,+/- i*d_-)
over the one fixed field K=Q(i), so it is a K-genus-one torsor with a fixed-field base point.


FIXED-D COUNTING CANDIDATE:
For a fixed D, the number of ordered coprime squarefree splittings D=d_-*d_+ is
2^omega(D)=D^o(1).
M3-T11-035 gives N_u=B^O(1) on the exact physical packet, hence D<=B^O(1) and this splitting loss is B^o(1).
The physical quartic point has polynomial height: a,b,c,d_-,d_+,y_-,y_+ are B^O(1), and the quartic-to-Jacobian map has fixed degree. Since the Jacobian has an exact rational point of prime order 2, the same fixed-field Dujella bounded-height theorem species already hostile-audit accepted in M3-T11-036 is a candidate to give B^o(1) K-points uniformly in the polynomial-height family.
Moreover reduced X=y_+/y_- recovers y_+,y_-; Z recovers a; then the displayed formulas recover b,c and hence u=a/b up to only bounded sign/orientation conventions. Audited M3-T11-036 then gives B^o(1) physical endpoints for each recovered u.


Accordingly the candidate consequence is:
fixed D + fixed content/coefficient packet
=> B^o(1) physical x=-1/8 endpoint states.
This counting consequence is NOT promoted before hostile audit of the K-point anchoring, quartic-to-Jacobian height adapter, Dujella uniformity, and physical reconstruction.


NEW SUPPORT RECEIVER:
If the fixed-D candidate passes audit, the x=-1/8 one-twelfth problem reduces to the moving support of the single residual squareclass parameter
D=sf((a^2+b^2)/M_rel^2).
A sufficient next theorem is
# {realized D on the physical x=-1/8 carrier in one fixed content/coefficient packet}
<< B^(1/12-delta)
for some fixed delta>0,
up to B^o(1) losses.
Canonical name:
XMinusOneEighthResidualSquarefreeKernelSupportOneTwelfth.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh physical endpoints on the x=-1/8 singular carrier; exact R<=B retained.


DEPENDS_ON:
M3-T11-035 common-u norm/height adapter;
M3-T11-036 audited fixed-u B^o(1) theorem and its fixed-field torsion bounded-height theorem species;
M3-T11-046 coprime factorization, full-S-denominator purity, and two-fresh-core even-valuation routing;
elementary binary-quartic invariant algebra.


SIDE PREFLIGHT / NO PROMOTION:
The separate M3-T11-045 generic fixed-x torsion algebra was rechecked exactly:
disc_v(P_x)=2^24*x^8*(1+8x)*(40x-27)^3;
at v0=-(64x^2-48x+3)/3 the stated R0 satisfies P_x(v0)=R0^2;
and the tangent-inflection identity for order 3 vanishes identically.
This does not replace the pending hostile audit of the generic fixed-x physical pushforward/height adapter.


ALIASES:
XMinusOneEighthResidualSquareclassJ1728;
XMinusOneEighthFixedDGenusOneFiber;
XMinusOneEighthResidualSquarefreeKernelSupportOneTwelfth.


DUPLICATE_OF:
None found under semantic rematch of RESULT-LEDGER, active ROUTE, NEGATIVE-REGISTER, and the card index.
This is not M3-T11-046: 046 gives the determinant-M_rel^2 / two-fresh-core lattice receiver; 080 pushes the remaining cofactor squareclasses into one moving D and an explicit j=1728 genus-one family.


SUPERSEDES:
No exact result is retracted.
Conditional on audit of the fixed-D counting adapter, this becomes the preferred first attack over a direct determinant-lattice physical range theorem for x=-1/8.


DO_NOT_REPEAT:
Do not claim d_- or d_+ is supported on a fixed finite prime set.
Do not infer D is finite-S merely because M_rel fresh valuations are even.
Do not charge M_rel^-2 from the old lattice determinant.
Do not count the d_-*d_+ split and fixed-u multiplicity as independent density savings.
Do not promote fixed-D B^o(1), x=-1/8 power saving, the primary Stage37 gate, or P(B)/M3(B) before audit and an active-D support theorem.


REOPEN_CONDITION:
Retract or alter the M3-T11-046 coprime factorization/even fresh valuations; find an error in the quartic/Jacobian identities; or show that the fixed-field torsion/height theorem cannot be transferred to this exact physical quartic family.


NEXT_LEGAL_ACTION:
Run stage37audit on the M3-T11-080 fixed-D counting adapter. In mainbatch, attack XMinusOneEighthResidualSquarefreeKernelSupportOneTwelfth without assuming the audit candidate as theorem credit; keep GenericXMovingSupportDispersion and InteriorCharacterGlobalDispersion as separate live supporting routes. Do not reopen x=27/40 for one-twelfth credit.


FLAGS:
M3_T11_X_MINUS_ONE_EIGHTH_RESIDUAL_KERNEL_SPLIT=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_RESIDUAL_D_EQUALS_SF_NU_OVER_MREL2=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_RESIDUAL_QUARTIC_J1728=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_RESIDUAL_QUARTIC_FULL_RATIONAL_2TORSION=PROVISIONAL
M3_T11_X_MINUS_ONE_EIGHTH_FIXED_D_BO1_CANDIDATE=true
M3_T11_X_MINUS_ONE_EIGHTH_ACTIVE_D_SUPPORT_DEFICIT_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
M3_T11_FIXED_X_GENERIC_BO1_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X_MINUS_ONE_EIGHTH_ATTACK=XMinusOneEighthResidualSquarefreeKernelSupportOneTwelfth
RESEARCH_CARD=M3-T11-08


CARD M3-T11-080 — HOSTILE AUDIT PROMOTION
TYPE=THEOREM / EXACT_STRUCTURE
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS
CLAIM=On the x=-1/8 carrier, D=sf(N_u/M_rel^2) and the fixed-D quartic fibers are smooth genus-one torsors with j=1728 Jacobian E_D: V^2=U^3-1296D^2U and full rational 2-torsion. Over the fixed field Q(i) each torsor has a rational base point. Uniform bounded-height counting plus the B^o(1) number of squarefree splittings gives fixed D + fixed content/coefficient packet => B^o(1) physical endpoints.
POPULATION=exact physical x=-1/8 endpoint states inside one fixed content/coefficient packet
DEPENDS_ON=M3-T11-035,M3-T11-036,M3-T11-046
IMPLIES=XMinusOneEighthResidualSquarefreeKernelSupportOneTwelfth is now the remaining x=-1/8 one-twelfth support gate
CREDIT_LIMIT=No moving-D support deficit, no x=-1/8 carrier power saving, no generic fixed-x theorem, no P(B)/M3(B) credit.
AUDIT_DOC=Stage37-HOSTILE-AUDIT-M3-T11-080-PASS
AUDIT_DOC_ID=1HJotvTyz0subm-JZY3H920GUNfjrcQyBlKGm4OIGBZQ
M3_T11_080_HOSTILE_AUDIT=PASS
M3_T11_X_MINUS_ONE_EIGHTH_FIXED_D_BO1_PROVED=true
M3_T11_X_MINUS_ONE_EIGHTH_ACTIVE_D_SUPPORT_DEFICIT_PROVED=false
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


---
