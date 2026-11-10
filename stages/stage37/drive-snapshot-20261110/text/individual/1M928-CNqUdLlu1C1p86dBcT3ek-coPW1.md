# M3-T11-113 — Psi norm-squareclass twists have full rational 2-torsion. Joint moving-conductor tail is B^o(1)min(H^2,H^4/M0^2); the low-height window can beat one-twelfth.

CARD_ID: M3-T11-113
CANONICAL_CARD_KEY: M3-T11-113
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-113
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / FIXED_NORM_SQUARECLASS_BO1 / NO_GLOBAL_POWER_SAVING
種別: THEOREM_ADAPTER / FIXED_SQUARECLASS_UNIFORM_FIBER / HEIGHT_WINDOW_POWER_BOUND
要点: Psi norm-squareclass twists have full rational 2-torsion. Joint moving-conductor tail is B^o(1)min(H^2,H^4/M0^2); the low-height window can beat one-twelfth.
主張の抜粋: F=26r^4-4r^3s+52r^2s^2+4rs^3+26s^4. Its d-twist Jacobian is y^2=(x-624d)(x+276d)(x+348d). Uniform fixed d=sf(a^2+b^2) gives B^o(1) parameters/endpoints. M_rel>=M0 implies d<=116H^4/M0^2. 4h-2m<1/12 gives a bounded-height-window saving.
対象・測度: Exact R<=B, fixed packet, psi/A4. H<=B^A is polynomial; no asserted global small-H bound.
依存関係: 036,035,040,041,109,corrected111,audited112; Dujella Thm1.1 (arXiv:2312.03655).
再開条件の抜粋: Audit PASS: explicit degree-four covariant map, x-height<=149184*d*H^4, torsion theorem threshold, measure and joint tail checked. Audit ID 12wFjeNIdAohCd-kP_Neje-676eFj2Eki. Next 114 parity-safe C_u squarepart.
旧詳細位置: ROUTE section 129; card file ID 1XGT5kuG7GPxHcEYWdGmytIHUtYiIlFOd
旧詳細リンク: https://drive.google.com/file/d/1XGT5kuG7GPxHcEYWdGmytIHUtYiIlFOd/view
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 990241
SOURCE_END: 999154
SOURCE_SHA256: 02c12a5a51ab0a842a3aefdca97059b4def4cb2b5c294637577465c880dd94c9

M3-T11-113 — Psi norm-squareclass twist compression and joint large-conductor tail
STATUS=PROVISIONAL / HOSTILE_AUDIT_REQUIRED / EXACT_SAME_MEASURE_THEOREM_ADAPTER
TYPE=FIXED_SQUARECLASS_UNIFORM_FIBER / MOVING_CONDUCTOR_JOINT_TAIL / HEIGHT_WINDOW_POWER_BOUND
POPULATION=Exact nondegenerate Stage37 physical endpoints with R<=B in one fixed content/coefficient packet, restricted to the audited psi/A4 image. One endpoint is one count.
DEPENDENCIES=109 psi parametrization; corrected 111; audited 112; 035/040/041 exact common-u conductor; 036 audited fixed-u physical multiplicity and polynomial physical coordinate-height machinery; Dujella Theorem 1.1.
DUPLICATE_SEARCH=RESULT-LEDGER, NEGATIVE-REGISTER, active ROUTE and CARD-INDEX were compared. The earlier genus-2 fixed-squareclass variable d in 101..107 is sf(2Pi), not the variable below. This card fixes sf(a^2+b^2) only on psi, using a new fixed norm quartic. It does not reopen local S4 squareclass work or ordinary fixed-theta Kummer.
ALIASES=PsiCommonUNormSquareclassTwistCompression; PsiJointLargeMConductorTail; PsiLowParameterHeightOneTwelfthWindow.
DUPLICATE_OF=NONE.


1. Exact norm and reduction.
Write primitive psi parameter t=r/s and
N=r^2-2rs-s^2, Q0=r^2+s^2, u=N/(5Q0).
Define
F(r,s)=N^2+25Q0^2
=26r^4-4r^3s+52r^2s^2+4rs^3+26s^4.
IMPORTANT_COEFFICIENT=52, not 48.
For primitive (r,s), g=gcd(N,5Q0) is exactly 1 or 2. Odd common divisors of N,Q0 are excluded by the resultant 8s^4; N has no primitive zero mod5. For mixed parity g=1; for both odd N,Q0 each have valuation exactly 1 at 2, so g=2.
Thus reduced u=a/b has
a^2+b^2=F(r,s)/g^2.
The canonical positive squarefree kernel
d=sf(a^2+b^2)=sf(F(r,s))
is independent of the parameter preimage: g^2 and projective scaling are squares.
For H=max(|r|,|s|), |N|<=4H^2 and Q0<=2H^2, hence
0<F(r,s)<=116H^4.
This is a direct height inequality; no physical B-exponent for H is imported.


2. New fixed-d genus-one fiber.
For a positive squarefree d, write F(r,s)=d q^2. Then the parameter point lies on the smooth genus-one double cover
C_d: Y^2=d F(t,1),
with Y=d q/s^2 on the finite chart, and the projective infinity chart retained.
For the binary quartic F, using the same scaled-Jacobian convention as 036:
I=10864,
J=2219776,
4I^3-J^2=201553920000 !=0.
For dF the invariants are I_d=d^2 I, J_d=d^3 J. Therefore
E_d: y^2=x^3-293328d^2 x-59933952d^3
=(x-624d)(x+276d)(x+348d).
For every d>0 the three roots are distinct. Consequently E_d has full rational 2-torsion over Q; in particular (624d,0) has exact order 2.
This family is a rational quadratic-twist family of one fixed elliptic curve, not the old fixed-u or fixed-theta family.


3. Uniform fixed-d parameter and physical count.
Assume H<=B^A for one fixed A, as allowed by the audited polynomial physical range. For realized d, d<=116H^4<=B^O_A(1).
The standard degree-four binary-quartic 2-cover C_d -> Jac(C_d)=E_d, used as a counting interface in 036, has fixed-degree algebraic formulas whose coefficient heights grow polynomially in d. Thus a parameter point of height <=H and Y=d q/s^2 maps to an E_d(Q) point of naive x-height B^O_A(1). Branch/pole/infinity charts contribute only bounded exceptional points.
The model height h(E_d)=O(log d)=O_A(log B).
The canonical-height comparison quoted in Dujella's paper gives canonical height O_A(log B). Choose a single enlarged height parameter T=B^K_A, with K_A fixed and large enough both for the induced point bound and T>=exp(max(h(E_d),e)).
Dujella Theorem 1.1 applies over the fixed field Q with prime order 2:
# such E_d(Q) points <=exp(O_A(log B/log log B))=B^o(1),
uniformly for every realized d.
The covering degree is four, so fixed d gives B^o(1) primitive projective psi parameters in the physical polynomial-height range. Composing each parameter t -> u with audited 036 gives B^o(1) physical endpoints for fixed d and fixed packet. Two subpolynomial bounds multiply to a subpolynomial bound; they are not charged as separate density savings.


4. Joint large-conductor tail — no per-modulus +1 sum.
Let E_psi(B;H,M0) count those exact physical endpoints admitting a primitive psi parameter of height <=H and with their actual M_rel>=M0>=1.
The audited common-u conductor gives M_rel^2 | a^2+b^2, hence M_rel^2 | F(r,s).
Removing the square factor M_rel^2 preserves d and leaves a positive integer, so
d=sf(F/M_rel^2)<=F/M_rel^2<=116H^4/M0^2.
Therefore every endpoint is routed once by its canonical d to one of at most
D=floor(116H^4/M0^2)
positive squarefree integer values.
Applying (3) to each d gives the provisional same-measure upper bound
E_psi(B;H,M0) <<_A B^o(1) H^4/M0^2.
If D=0 the subset is empty. The elementary ambient parameter upper bound plus 036 also gives B^o(1)H^2; hence
E_psi(B;H,M0) <<_A B^o(1) min(H^2,H^4/M0^2).
This sums over all moving actual M_rel and C_u simultaneously. It does not sum 112's +1 over conductor pairs, and it does not assume any distribution or independence of d.
The incremental C_u is not charged; only the already-existing square M_rel^2 is used as a deterministic divisor in a replacement count.


5. Precisely scoped exponent consequence.
On a height/conductor window H<=B^h and M_rel>=B^m, the new bound is
E_psi << B^(4h-2m+o(1)).
Thus a one-twelfth support deficit is obtained for this psi subpopulation if
4h-2m<1/12.
For the hard conductor threshold m=1/12-eta, it is sufficient to have
h<1/16-eta/2.
For example H<=B^(1/16-epsilon), M_rel>=B^(1/12-eta), with 4epsilon>2eta, gives
E_psi << B^(1/12-4epsilon+2eta+o(1)).
This is a bounded-height-window result only. No claim is made that all physical psi endpoints satisfy this small parameter-height bound. The remaining high-height psi region is uncontrolled by this one-twelfth argument.
No primary-gate closure, total numerator improvement or P/M3 limit is claimed.


SOURCE.
Marta Dujella, Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves, arXiv:2312.03655, Theorem 1.1, PDF pages 2-3; theorem threshold and height comparison checked directly.
The source supplies the uniform torsion counting theorem only; all norm/Jacobian/physical adapters here are newly derived and provisional.


VERIFICATION=Exact integer coefficient multiplication confirmed F's coefficient 52; exact I,J formulas and factorization confirmed; 2224 primitive pairs in [-30,30]^2 verified reduction, squarefree invariance, positivity bound, and d<=F/M^2 whenever tested M^2|F. Finite checks are supporting evidence, not the proof.
IMPLIES=The psi moving-conductor route has a joint squareclass-tail bound and an explicit low-height window; moving high-height support remains the blocker.
DO_NOT_REPEAT=Do not conflate d=sf(a^2+b^2) with old d=sf(2Pi). Do not charge torsion, norm divisibility, p=1 mod12 density or 112's determinant as independent savings. Do not assume H<=B^(1/16) from an ambient degree-two psi height relation. Do not claim that the low-height window covers the entire physical population.
REOPEN_CONDITION=Hostile audit rejects the norm coefficient/reduction, Jacobian convention, full rational 2-torsion, degree-four covering-height adapter, Dujella threshold/uniformity, fixed-u pushforward, or squareclass-tail routing.
CREDIT=Provisional fixed-d uniform count and height-window power bound only. No global fixed-power saving or new closure credit.
NEXT_LEGAL_ACTION=Hostile-audit 113. If PASS, attack the high-parameter-height psi stratum through exact physical height constraints or cross-height/conductor correlation; phi global allocation, nonlocal S4 and theta!=0 remain live.
NEXT_RESEARCH_CARD_ID=M3-T11-114
PSI_FIXED_NORM_SQUARECLASS_UNIFORM_BO1=PROVISIONAL
PSI_JOINT_LARGE_CONDUCTOR_TAIL=PROVISIONAL
PSI_LOW_PARAMETER_HEIGHT_ONE_TWELFTH_WINDOW=PROVISIONAL
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


CURRENT CONTINUATION POINTER — supersedes older operational lines above
LATEST_RESEARCH_CARD=M3-T11-113
LATEST_AUDITED_RESEARCH_CARD=M3-T11-112
PROVISIONAL_FRONTIER_CARD=M3-T11-113
PROVISIONAL_FRONTIER_AUDIT_STATUS=HOSTILE_AUDIT_REQUIRED
CARD_113_FILE_ID=1XGT5kuG7GPxHcEYWdGmytIHUtYiIlFOd
AUDIT_DOC_ID_112=1w5zvca-ctnZ2HqNtphuMdUteUFfdM7jG
NEXT_RESEARCH_CARD_ID=M3-T11-114
NEXT_LEGAL_ACTION=Hostile-audit 113, then control the high-height psi region outside 4h-2m<1/12. Global saving and primary gate remain open.




M3-T11-113 — HOSTILE AUDIT PROMOTION
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / NO_GLOBAL_POWER_SAVING
AUDIT_DOC_ID_113=12wFjeNIdAohCd-kP_Neje-676eFj2Eki
RESULT=Canonical d=sf(a^2+b^2) has uniform B^o(1) psi parameter/physical fibers. E_psi(B;H,M0)<<B^o(1)min(H^2,H^4/M0^2) is accepted for H<=B^A. Explicit covariants give x=3d*H_F/(4F), y=27*K_F/(8q^3), degree four, and naive x-height<=149184*d*H^4. Historical provisional state is superseded here. No global height coverage or closure is promoted.

## Retained standalone source — M3-T11-113.md
SOURCE_FILE_ID: 1XGT5kuG7GPxHcEYWdGmytIHUtYiIlFOd
SOURCE_URL: https://drive.google.com/file/d/1XGT5kuG7GPxHcEYWdGmytIHUtYiIlFOd/view?usp=drivesdk

M3-T11-113 — Psi norm-squareclass twist compression and joint large-conductor tail
STATUS=PROVISIONAL / HOSTILE_AUDIT_REQUIRED / EXACT_SAME_MEASURE_THEOREM_ADAPTER
TYPE=FIXED_SQUARECLASS_UNIFORM_FIBER / MOVING_CONDUCTOR_JOINT_TAIL / HEIGHT_WINDOW_POWER_BOUND
POPULATION=Exact nondegenerate Stage37 physical endpoints with R<=B in one fixed content/coefficient packet, restricted to the audited psi/A4 image. One endpoint is one count.
DEPENDENCIES=109 psi parametrization; corrected 111; audited 112; 035/040/041 exact common-u conductor; 036 audited fixed-u physical multiplicity and polynomial physical coordinate-height machinery; Dujella Theorem 1.1.
DUPLICATE_SEARCH=RESULT-LEDGER, NEGATIVE-REGISTER, active ROUTE and CARD-INDEX were compared. The earlier genus-2 fixed-squareclass variable d in 101..107 is sf(2Pi), not the variable below. This card fixes sf(a^2+b^2) only on psi, using a new fixed norm quartic. It does not reopen local S4 squareclass work or ordinary fixed-theta Kummer.
ALIASES=PsiCommonUNormSquareclassTwistCompression; PsiJointLargeMConductorTail; PsiLowParameterHeightOneTwelfthWindow.
DUPLICATE_OF=NONE.

1. Exact norm and reduction.
Write primitive psi parameter t=r/s and
N=r^2-2rs-s^2, Q0=r^2+s^2, u=N/(5Q0).
Define
F(r,s)=N^2+25Q0^2
=26r^4-4r^3s+52r^2s^2+4rs^3+26s^4.
IMPORTANT_COEFFICIENT=52, not 48.
For primitive (r,s), g=gcd(N,5Q0) is exactly 1 or 2. Odd common divisors of N,Q0 are excluded by the resultant 8s^4; N has no primitive zero mod5. For mixed parity g=1; for both odd N,Q0 each have valuation exactly 1 at 2, so g=2.
Thus reduced u=a/b has
a^2+b^2=F(r,s)/g^2.
The canonical positive squarefree kernel
d=sf(a^2+b^2)=sf(F(r,s))
is independent of the parameter preimage: g^2 and projective scaling are squares.
For H=max(|r|,|s|), |N|<=4H^2 and Q0<=2H^2, hence
0<F(r,s)<=116H^4.
This is a direct height inequality; no physical B-exponent for H is imported.

2. New fixed-d genus-one fiber.
For a positive squarefree d, write F(r,s)=d q^2. Then the parameter point lies on the smooth genus-one double cover
C_d: Y^2=d F(t,1),
with Y=d q/s^2 on the finite chart, and the projective infinity chart retained.
For the binary quartic F, using the same scaled-Jacobian convention as 036:
I=10864,
J=2219776,
4I^3-J^2=201553920000 !=0.
For dF the invariants are I_d=d^2 I, J_d=d^3 J. Therefore
E_d: y^2=x^3-293328d^2 x-59933952d^3
=(x-624d)(x+276d)(x+348d).
For every d>0 the three roots are distinct. Consequently E_d has full rational 2-torsion over Q; in particular (624d,0) has exact order 2.
This family is a rational quadratic-twist family of one fixed elliptic curve, not the old fixed-u or fixed-theta family.

3. Uniform fixed-d parameter and physical count.
Assume H<=B^A for one fixed A, as allowed by the audited polynomial physical range. For realized d, d<=116H^4<=B^O_A(1).
The standard degree-four binary-quartic 2-cover C_d -> Jac(C_d)=E_d, used as a counting interface in 036, has fixed-degree algebraic formulas whose coefficient heights grow polynomially in d. Thus a parameter point of height <=H and Y=d q/s^2 maps to an E_d(Q) point of naive x-height B^O_A(1). Branch/pole/infinity charts contribute only bounded exceptional points.
The model height h(E_d)=O(log d)=O_A(log B).
The canonical-height comparison quoted in Dujella's paper gives canonical height O_A(log B). Choose a single enlarged height parameter T=B^K_A, with K_A fixed and large enough both for the induced point bound and T>=exp(max(h(E_d),e)).
Dujella Theorem 1.1 applies over the fixed field Q with prime order 2:
# such E_d(Q) points <=exp(O_A(log B/log log B))=B^o(1),
uniformly for every realized d.
The covering degree is four, so fixed d gives B^o(1) primitive projective psi parameters in the physical polynomial-height range. Composing each parameter t -> u with audited 036 gives B^o(1) physical endpoints for fixed d and fixed packet. Two subpolynomial bounds multiply to a subpolynomial bound; they are not charged as separate density savings.

4. Joint large-conductor tail — no per-modulus +1 sum.
Let E_psi(B;H,M0) count those exact physical endpoints admitting a primitive psi parameter of height <=H and with their actual M_rel>=M0>=1.
The audited common-u conductor gives M_rel^2 | a^2+b^2, hence M_rel^2 | F(r,s).
Removing the square factor M_rel^2 preserves d and leaves a positive integer, so
d=sf(F/M_rel^2)<=F/M_rel^2<=116H^4/M0^2.
Therefore every endpoint is routed once by its canonical d to one of at most
D=floor(116H^4/M0^2)
positive squarefree integer values.
Applying (3) to each d gives the provisional same-measure upper bound
E_psi(B;H,M0) <<_A B^o(1) H^4/M0^2.
If D=0 the subset is empty. The elementary ambient parameter upper bound plus 036 also gives B^o(1)H^2; hence
E_psi(B;H,M0) <<_A B^o(1) min(H^2,H^4/M0^2).
This sums over all moving actual M_rel and C_u simultaneously. It does not sum 112's +1 over conductor pairs, and it does not assume any distribution or independence of d.
The incremental C_u is not charged; only the already-existing square M_rel^2 is used as a deterministic divisor in a replacement count.

5. Precisely scoped exponent consequence.
On a height/conductor window H<=B^h and M_rel>=B^m, the new bound is
E_psi << B^(4h-2m+o(1)).
Thus a one-twelfth support deficit is obtained for this psi subpopulation if
4h-2m<1/12.
For the hard conductor threshold m=1/12-eta, it is sufficient to have
h<1/16-eta/2.
For example H<=B^(1/16-epsilon), M_rel>=B^(1/12-eta), with 4epsilon>2eta, gives
E_psi << B^(1/12-4epsilon+2eta+o(1)).
This is a bounded-height-window result only. No claim is made that all physical psi endpoints satisfy this small parameter-height bound. The remaining high-height psi region is uncontrolled by this one-twelfth argument.
No primary-gate closure, total numerator improvement or P/M3 limit is claimed.

SOURCE.
Marta Dujella, Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves, arXiv:2312.03655, Theorem 1.1, PDF pages 2-3; theorem threshold and height comparison checked directly.
https://arxiv.org/pdf/2312.03655
The source supplies the uniform torsion counting theorem only; all norm/Jacobian/physical adapters here are newly derived and provisional.

VERIFICATION=Exact integer coefficient multiplication confirmed F's coefficient 52; exact I,J formulas and factorization confirmed; 2224 primitive pairs in [-30,30]^2 verified reduction, squarefree invariance, positivity bound, and d<=F/M^2 whenever tested M^2|F. Finite checks are supporting evidence, not the proof.
IMPLIES=The psi moving-conductor route has a joint squareclass-tail bound and an explicit low-height window; moving high-height support remains the blocker.
DO_NOT_REPEAT=Do not conflate d=sf(a^2+b^2) with old d=sf(2Pi). Do not charge torsion, norm divisibility, p=1 mod12 density or 112's determinant as independent savings. Do not assume H<=B^(1/16) from an ambient degree-two psi height relation. Do not claim that the low-height window covers the entire physical population.
REOPEN_CONDITION=Hostile audit rejects the norm coefficient/reduction, Jacobian convention, full rational 2-torsion, degree-four covering-height adapter, Dujella threshold/uniformity, fixed-u pushforward, or squareclass-tail routing.
CREDIT=Provisional fixed-d uniform count and height-window power bound only. No global fixed-power saving or new closure credit.
NEXT_LEGAL_ACTION=Hostile-audit 113. If PASS, attack the high-parameter-height psi stratum through exact physical height constraints or cross-height/conductor correlation; phi global allocation, nonlocal S4 and theta!=0 remain live.
NEXT_RESEARCH_CARD_ID=M3-T11-114
PSI_FIXED_NORM_SQUARECLASS_UNIFORM_BO1=PROVISIONAL
PSI_JOINT_LARGE_CONDUCTOR_TAIL=PROVISIONAL
PSI_LOW_PARAMETER_HEIGHT_ONE_TWELFTH_WINDOW=PROVISIONAL
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


AUDIT ADDENDUM — supersedes the historical provisional status above
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / NO_GLOBAL_POWER_SAVING
Explicit covering map verified: H_F=(F_rs^2-F_rr*F_ss)/3, K_F=(F_s*(H_F)_r-F_r*(H_F)_s)/12; x=3d*H_F/(4F), y=27*K_F/(8q^3), F=dq^2. Degree-four map and x-height<=149184*d*H^4 establish the uniform adapter without an unspecified height constant.
AUDIT=Stage37-HOSTILE-AUDIT-M3-T11-113-PASS (Stage37-AUDIT).
NEXT=114 parity-safe incremental C_u squarepart adapter; high-height/low-squarepart physical occupancy remains open.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
