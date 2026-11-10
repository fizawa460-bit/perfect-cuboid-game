# M3-T11-132 — Gaussian extreme coupled receiver: exact physical height window and consumed root-line audit

CARD_ID: M3-T11-132
CANONICAL_CARD_KEY: M3-T11-132
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-132
現行一覧の状態: PROVED_EXACT_HEIGHT_WINDOW_AND_ROOTLINE_PULLBACK / WITHIN_SESSION_AUDIT_PASS / GLOBAL_CREDIT0
種別: PHYSICAL_HEIGHT / CONSUMED_ROOTLINE_AUDIT
要点: Hの高さ上限からM_Gが消える。H合同は既存V+u root-lineの引戻し。
主張の抜粋: a²D[4b²H+N(bs+at)]=NtW+;Gでtruncated valuation同値。独立CRT密度不可。
対象・測度: Exact R<=B必要windowのみ。500 rational enlargement/300 localG PASS; physicalcount0。
依存関係: 131,130,ROUTE32/042 norm saturation; lcm denominator;120 retracted retained。
再開条件の抜粋: 133完了：physical N squareと六平方signed lift。次134 squareN上のglobal moving support。
旧詳細位置: ROUTE/LEDGER132; audit 1DR1XJ3ARFZZH-rZO-DZFqR0-R2REX3As
旧詳細リンク: M3-T11-132.md
旧LEDGERリンク: K16-C3-M3-RESULT-LEDGER

## Retained LEDGER source 1
SOURCE_START: 1213409
SOURCE_END: 1225587
SOURCE_SHA256: 0370b9089fa2d17937300e79e0b5ed9d6e6b8b446b66ed047e8df0da509144a7

# M3-T11-132 — Gaussian extreme coupled receiver: exact physical height window and consumed root-line audit


STATUS=PROVED_EXACT_IDENTITIES_AND_NECESSARY_HEIGHT_WINDOWS
AUDIT=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_PASS_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0; PRIMARY_GATE=OPEN; TI=PARKED_BY_USER


## Authority and scope
Continuation of current MAIN/INDEX/RESULT-LEDGER/active ROUTE and M3-T11-131. Sources used: ROUTE Sections 8,12–14,16–17,29,32; exact norm saturation 042 (duplicate ID: identify by formula); retained lcm/divisibility facts including 083; 130 strict-interior exclusion; 131 extreme classification. No full historical reread. Finite nonzero u, nondegenerate physical branch; odd split fresh primes outside frozen content. R is the original Euclidean space diagonal, R=H_c tau<=B. Each endpoint counted once. These are necessary conditions, not a parameter-box count.


Write u=a/b, S=s/t in lowest terms, b,t>0, N=a²+b², A=1+u². Actual anti-roots v_i=A_i/B_i, gcd(A_i,B_i)=1, B_i>0, satisfy f(X)=X³-SX²+EX-P, E=4u(S-u)/A, P=4u²S/A. Put D=product B_i, H=2bs-at. Retained 131 gives H!=0 on physical points, M_G²|H, gcd(abt,M_G)=1, N=M_D² M_G⁴ N_*, t=M_D² t_*, with N_*,t_* integral and coprime to fresh support.


## 1. Exact same-physical-height necessary window
ROUTE32 gives |v_i|<=2sqrt(2), hence |S|<=6sqrt(2). Therefore
 |H|<=t(12sqrt(2)b+|a|)<=17t sqrt(N).
The last constant is exact Cauchy: (12sqrt(2))²+1=289. Norm saturation N/g_u|D, g_u=gcd(4,N) in {1,2}, gives N<=2D. Since S=sum v_i, t|lcm(B_1,B_2,B_3), not merely t|D.


Retain packet constants L_i from ROUTE32, L_prod=product L_i, L_vee=lcm L_i. They may depend polynomially on B through frozen content; they are NOT absolute global constants. Complementary-square denominator bounds imply
 D|L_prod tau⁶/R_rel²,  t|L_vee tau²,
where tau=tau_0 tau_1 tau_2 tau_3, R_rel=tau_1 tau_2 tau_3. Consequently
 |a|,b<=sqrt(2L_prod)(B/H_c)³/R_rel,
 |s|<=6sqrt(2)L_vee(B/H_c)²,
 |H|<=17L_vee sqrt(2L_prod)(B/H_c)⁵/R_rel.
These follow forward from R<=B. No converse, uniform multiplicity bound, endpoint parametrization, or ambient-height replacement is asserted.


## 2. M_G cancels in the pointwise normalized size window
Set j=H/M_G², a nonzero integer. Substituting the already-consumed exact norm carrier yields
 1<=|j|<=17t M_D sqrt(N_*)=17M_D³ t_* sqrt(N_*).
There is no M_G-powered deficit in this bound. In particular M_G²<=sqrt(N) already, whereas the size upper bound 17t sqrt(N) is larger. Nonzero H plus this pointwise size estimate cannot alone exclude large M_G. This retires that argument only: H may still be a useful dependent coordinate in a genuinely joint global count.


## 3. Exact pullback: H is the consumed original root-line
Direct substitution of E,P gives the polynomial identity
 4(2S-u)+A(S+u)=(A/u²) product_i(u+v_i).
With W_+=product_i(a B_i+b A_i), clearing denominators WITHOUT dividing globally by a² gives
 a² D [4b² H+N(bs+at)]=N t W_+.


At a fresh Gaussian-extreme p^lambda||m_i, put L=2lambda. By 131, v_p(N)=v_p(D)=4lambda=2L; a,b,t are p-units. The two other factors of W_+ are units (pole roots have denominator depth L and unit numerator), while the targeted unit factor is a p-unit denominator times V+u. The identity implies exactly
 min(v_p(H),4lambda)=min(v_p(W_+),4lambda).
Thus p^(2lambda)|H iff p^(2lambda)|(a B_i+b A_i), the oriented V+u root-line already imposed by 131. Correction N(bs+at) matters at depth 4lambda; untruncated valuation equality is NOT asserted.


Therefore an additional CRT density M_G^(-2) cannot be multiplied into an endpoint count that already consumes these original root-lines. This is a double-charge audit, not a proof that every possible conditional H count is useless. The pole character remains the retained discriminant/splitting selector, not a second independent density.


Optional coordinate check: H/(at)=2S/u-1=2/w-1 for retained w=u/S. This is a Möbius renaming of the existing w fiber, not a new fiber theorem; do not promote the unaudited Section44 candidate through this renaming.


## Verification and adversarial scope checks
verify_m3_t11_132.py: exact rational arithmetic; PASS on 500 rational cubic-split enlargement cases (not physical endpoints), including coefficient identities, integral pullback, real anti-root bounds, constant17, norm saturation and lcm denominator divisibility. PASS on 300 local Gaussian cases for p=5,13,17,29,41, lambda=1..4 and H-depth variation: targeted unit root, truncated valuations and depth-L equivalence. Local cases do not assert all poles split or global physical lift; failed physical root-lines are allowed test cases. Physical endpoints enumerated=0. M3-T11-132-symbolic-check.wl replays the symbolic identity and was evaluated to zero. No finite sample proves global counting. This is an audit within this session, not an independent external audit.


## Preserved results and next legal action
130 interior physical occupancy empty and 131 D/G extreme classifications retained. 045 denominator Legendre receiver and all later singular shells retained. 123 scalar class and Cl(K_u)[2] obstruction retained. 129 S4 family/local persistence retained within its stated nonphysical scope. 120 physical adapter remains RETRACTED; quartic theta is not identified with actual physical z or anti-root V. Full Gaussian-core reconstruction, common phase, global physical lift and exact-R counting remain OPEN. All global fixed-power-saving/nonexistence flags remain false.


NEXT=M3-T11-133
ATTACK=GaussianExtremeGlobalPhysicalLiftBeyondConsumedRootLine
Read this card, 131, then targeted original full physical cover 105/106 and common torus phase ROUTE17/24. On surviving Gaussian extremes identify a global Gaussian-core/phase-square/reconstruction condition not already consumed by N saturation, H divisibility or W_+ root-line. Retain dependent H,j only inside a genuinely joint global receiver. Supply the exact R<=B adapter, content constants and endpoint multiplicity before claiming a tail. No new pointwise CRT density, cofactor renaming or height window alone; no automatic TI resumption.


ARTIFACT_IDS=card:1nahIP04cFPUa0WtkugUXV1fYr71aJQqK;audit:1DR1XJ3ARFZZH-rZO-DZFqR0-R2REX3As;script:1wszT4KY1SpjiAUWj6zgN5IDKuUkYxTuL;json:1Vg79jaAOGHDlKvm4WS0g_0WPqcQ5l5hB;wl:1sSFlRUWtvgnEHg-x2PF1NvfF2b2DY5_H


CURRENT AUTHORITY CONTROL — M3-T11-132 AUDITED / COUPLED HEIGHT WINDOW AND CONSUMED ROOTLINE AUDIT
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-132
ACTIVE_RESEARCH_CARD_FILE_ID=1nahIP04cFPUa0WtkugUXV1fYr71aJQqK
LATEST_RESEARCH_CARD=M3-T11-132
LATEST_AUDITED_RESEARCH_CARD=M3-T11-132
LATEST_AUDIT_FILE_ID=1DR1XJ3ARFZZH-rZO-DZFqR0-R2REX3As
LATEST_VERIFICATION_SCRIPT_FILE_ID=1wszT4KY1SpjiAUWj6zgN5IDKuUkYxTuL
LATEST_VERIFICATION_JSON_FILE_ID=1Vg79jaAOGHDlKvm4WS0g_0WPqcQ5l5hB
LATEST_SYMBOLIC_REPLAY_FILE_ID=1sSFlRUWtvgnEHg-x2PF1NvfF2b2DY5_H
LATEST_CARD_STATUS=PROVED_EXACT_HEIGHT_WINDOW_AND_ROOTLINE_PULLBACK / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
LATEST_AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-133
CURRENT_ATTACK=GaussianExtremeGlobalPhysicalLiftBeyondConsumedRootLine
NEXT_LEGAL_ACTION=Read132 then131 and targeted105/106 fullphysicalcover plusROUTE17/24 commonphase. Seek globalGaussian-core/phase-square/reconstruction condition beyond consumedN,H,Wrootlines. Keep exactR<=B,contentconstants,oneendpointonecount. No independentCRT density orpointwisesizegain. RetainDbranch andsingularshells.
INTERIOR_130_PHYSICAL_OCCUPANCY=EMPTY on finite-u nondegenerate branch at every odd split fresh p^lambda||m_i with0<c_p<2lambda.
INTERIOR_130_PROOF=k=2lambda-c_p,n=2lambda+c_p;vp(S)=-k,vp(A)=n. g=p^(4lambda)f has coefficientvaluations(0,0,n,4lambda),linearreductionX-u. Uniqueunitanti-rootV hasvp(V-u)=vp(V²+1)=k<2lambda,contradicting originalphysicalrootline.
INTERIOR_130_SCOPE=Actual cubic rootV, NOTquartic theta orphysicalz identification. Applies independently ofN square/S4/characterselectors; no resultat2/content/extremes/u=infinity.
INTERIOR_130_VERIFICATION=200 abstractallocations and26 nested129AP localimpostors PASS; physicalendpointcount0. Localcubic splits/residualsquare/genus3lift can hold butphysicalnormrootlinefails.
INTERIOR_106_107_48_STATUS=Conditionalalgebraic/residuallocalidentities RETAINED; strictinteriorphysicaloccupancy EMPTY by130. Interiorphysicalcharacterdispersion superseded.
EXTREME_130_ROUTER=All surviving fresh c_p in{0,2lambda};Q_S andC_u squareonfreshsupport,Q_S*C_u=M_rel². Routingonly,no countingcredit; neitherextremetailproved.
EXTREME_131_DENOMINATOR=cp0,L2lambda,vp(A)=L,vp(S)=-L; uniqueunitV congruent+u modp^L andnormrootlineautomatic. Pole-split/Legendre045 receiverretained; no deeperunit-root sieve.
EXTREME_131_GAUSSIAN=cpL,vp(A)=2L,S/S-u units; targetednormrootline IFF2S congruentu modp^L,thenV congruent-u modp^L. Pole-scaledcubicY(Y²+2/A0),split IFFchi(-2/A0)=+1; allsimplelifts,noadditionalcubicprecisiongain.
EXTREME_131_SQUARE_N=IfNu square,A0 square,Gaussianfreshp mustbe1mod8; p5mod8 forcedD. IfNu=c²,e=vp(c):D lambda=e;G e even,lambda=e/2,p1mod8. Assignmentonly,no endpointcount.
EXTREME_131_COUPLED_INTEGER=H_G=2bs-at; M_G²|H_G;gcd(abt,M_G)=1; H_G!=0 sinceQ(u/2,u)=u²(112+145u²+u4)/16>0 contradictsrealphysicalY²=-A Q. Thus|H_G|>=M_G² on samepacket; exactheight/countadapterOPEN.
EXTREME_131_NOVELTY_FIREWALL=042 norm saturation,043 GaussianPhiStarresidualempty,045 denominatorLegendre retainedNOTnew. G-characterrestatesdiscriminantsquare; notsecondindependentdensity.120 remainsretracted.
EXTREME_131_VERIFICATION=800D cases/272G congruencecases/40G polecases PASS,3symbolicidentitieszero; physicalendpointcount0. SyntheticlocalS=u/2 samples globallyimpossibleoverR,NOTphysicalorallplaceglobalimpostors.
EXTREME_131_SCOPE=Oddsplitfreshoutsidecontent,finite nonzerou,nondegenerate. FullGaussian-core/global lift andRcountnotproved. Denominatorzero-pole-discriminantboundary retained. Largefreshu=infinity exclusionalready035,notnew.
S4_129_STATUS=RETAINED explicitS4 squareN family,poleclassc0/xi0 and allplace separate nonpolelocalpersistence. Notphysicalpoints;130 addsmissingoriginalrootlineobstructiononinterior.
S4_128_STATUS=RETAINED exactgammaexclusion4real,two-real scalarquotientfirewall.
S4_123_STATUS=RETAINED beta=Nm-nalpha,gamma=alpha(aN-balpha),xi=beta/gamma; original[Nn beta],Cl(K_u)[2] andactualdenominatorn retained.
THETA_FULL_PHYSICAL_GLOBAL_R_AND_EXACT_HEIGHT_GATE=OPEN_RETAINED
PHI_122_STATUS=JOINT_DENOMINATOR_SUPPORT_RECEIVER_RETIRED
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER; quarticrootlock/extremephiallocations/fourthpowertailsNOTreinstatedby130
BACKWARD_REAUDIT_117_119=PASS_WITH_RETAINED_SCOPE_LIMITS
STARTUP=MAIN/INDEX currentcontrol ->132 card/audit/replay -> activeROUTE/RESULT-LEDGER latest132 -> targeted131,105/106,ROUTE17/24/32. No fullhistoryreread.
PRIMARY_RECEIVER=P(B)<=B^o(1) A_1,1(B); sufficient A_1,1(B)<<B^(1/3-eta) forfixedeta>0 onexactphysicalmeasure.
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
COUPLED_132_HEIGHT=|H|<=17t sqrt(N)<=17Lvee sqrt(2Lprod)(B/Hc)^5/Rrel; contentconstants retained,forwardnecessarywindowONLY.
COUPLED_132_NORMALIZED=j=H/MG²!=0;|j|<=17t MD sqrt(Nstar);MG cancels,pointwisesizeexclusionretired.
COUPLED_132_PULLBACK=a²D[4b²H+N(bs+at)]=Nt product(aBi+bAi);onG min(vpH,4lambda)=min(vpWplus,4lambda).H depth2lambda iff originalV+u rootline,NOTextraindependentdensity.
COUPLED_132_SCOPE=H/j retainedasdependentcoordinates; jointglobalcountOPEN.500rationalsplitenlargement/300localG PASS,physicalendpointcount0,symboliczero.
LOWER_OPERATIONAL_POINTERS=Historical and superseded by this current control; mathematical statements retain their audited scope.






STAGE37 CONTINUATION RESULT — M3-T11-133
