# M3-T11-134 — exact half-angle denominators remove the fresh Gaussian extreme; four-square lift and unique positive reconstruction

CARD_ID: M3-T11-134
CANONICAL_CARD_KEY: M3-T11-134
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-134
現行一覧の状態: PROVED_FRESH_D_ONLY / EXACT_FOUR_SQUARE_HEIGHT_LIFT / WITHIN_SESSION_AUDIT_PASS / GLOBAL_CREDIT0
種別: FRESH_G_EMPTY / INTRINSIC_DENOMINATOR / UNIQUE_LIFT
要点: Den(d_i)=D_i²とequal-tauでfreshG空。c_p=0,Q_S=Mrel²,C_u=1,M_G=1。
主張の抜粋: Signedsumはsurface＋六平方から自動、一意positive lift。squareNで四平方テストで十分。
対象・測度: ExactR=lcm sqrtDen(d_i);h_i,R,tau,c_i復元。originalpacketfilters retained。
依存関係: 133;ROUTE6/7/32/37/48;D045/046/singularshells live;129/123 retained;120 retracted。
再開条件の抜粋: 135完了：x=-1/8 finite-u physical EMPTY。次136 generic D-only four-square exactR moving support。
旧詳細位置: ROUTE/LEDGER134; audit 1d7403fZeg7xxba0eHdU6dLDU0Mo5rtkr
旧詳細リンク: M3-T11-134.md
旧LEDGERリンク: K16-C3-M3-RESULT-LEDGER

## Retained LEDGER source 1
SOURCE_START: 1242222
SOURCE_END: 1261654
SOURCE_SHA256: 5b0d69854a42af47046aaeca563db70d53e3e239b4f99c37a2354ff19b537de1

# M3-T11-134 — exact half-angle denominators remove the fresh Gaussian extreme; four-square lift and unique positive reconstruction


STATUS=PROVED_EXACT_FRESH_DENOMINATOR_ONLY_ROUTER_AND_PHYSICAL_HEIGHT_ADAPTER
AUDIT=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_PASS_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0; PRIMARY_GATE=OPEN; TI=PARKED_BY_USER


## Current authority and population
Continuation of latest133 and current MAIN/INDEX/RESULT-LEDGER/active ROUTE. Targeted reads:133; ROUTE6/7/17 physical triangle contents and equal tau; ROUTE32/37 actual distinct anti-roots and fresh unit/pole valuations; ROUTE35 symmetric surface; ROUTE48 allocation; retained129 square-norm S4 residual persistence. No full-history reread. Keep exact primitive physical R<=B, one canonical endpoint counted once, original coefficient/orientation/cyclic packet masks.


Notation: normalized directions x_i=e_i/R, y_i=signed opposite face diagonal/R satisfy x_i²+y_i²=1 and sum x_i²=1. Actual signed anti-roots from133 give
 d_i=(S-v_i)/2=2x_i y_i, S=sum v_i.
Physical space-triangle hypotenuse D_i=R/h_i, h_i=gcd(R,e_i); anti-root denominators B_i are DIFFERENT objects. Frozen contents c_1=h_2h_3, c_2=h_1h_3, c_3=h_1h_2 and D_i=tau*c_i, R=(h_1h_2h_3)tau, as already proved in ROUTE6/7.


## 1. Exact reduced denominators recover R and the entire content triple
In the primitive reduced space triangle write x_i=C_i/D_i, y_i=F_i/D_i, with C_i²+F_i²=D_i², D_i odd and gcd(C_iF_i,D_i)=1. Hence
 d_i=2C_iF_i/D_i²,
 Den(d_i)=D_i² EXACTLY, with no cancellation.
Also Den(1+d_i)=Den(1-d_i)=D_i², and the reduced denominators of L_i^+=x_i+y_i and L_i^-=x_i-y_i are both D_i. No fresh or content coefficient is silently discarded.


Therefore, given a lifted anti-root triple, set q_i=sqrt(Den((S-v_i)/2)). Then q_i=D_i and
 R=lcm(q_1,q_2,q_3),
 h_i=R/q_i,
 tau=gcd(q_1,q_2,q_3)=q_1q_2q_3/R²,
 c_i=q_i/tau,
 R=(h_1h_2h_3)tau.
All these are exact integers. The lcm formula follows also from133's R=lcm Den(x_i), since each Den(x_i)=D_i. The recovered h_i are pairwise coprime by ROUTE6; the equivalent product/gcd formulas are not extra independent constraints.


Thus the physical height is intrinsic to the ordered anti-root triple, independent of a lift sign search:
 sqrt(lcm_i Den(d_i))<=B.
In a fixed content packet this is exactly (h_1h_2h_3)tau<=B with q_i=tau*c_i. Moreover Den(S) and each Den(v_i) divide R², since S=sum d_i and v_i=S-2d_i. These are exact physical denominators, not an ambient rational box or an assumed B-uniform packet constant.


## 2. NEW physical router: all odd split fresh relative primes are denominator extreme
Let p^lambda||m_i, an odd split fresh relative prime outside all frozen content. Pairwise-coprime tau_j imply v_p(tau)=lambda, and p does not divide any c_j. Section1 forces, for ALL THREE directions,
 v_p(D_j)=lambda, v_p(d_j)=-2lambda.


The corrected ROUTE37 gives the targeted actual anti-root v_i a p-adic unit (v_p(v_i)=0), while the two other anti-roots have poles of depth2lambda. Since
 S-v_i=2d_i,
the exact physical denominator above implies
 v_p(S-v_i)=-2lambda,
 v_p(S)=-2lambda.
No cancellation against a unit can alter this pole depth.


Insert the retained040/48 conservation law
 k_p=v_p(Den S)=2lambda-c_p.
It follows that c_p=0 at EVERY such physical prime. Therefore
 Q_S=M_rel², C_u=1,
 M_D=M_rel, M_G=1,
 v_p(N_u)=2lambda and v_p(Den S)=2lambda.
On133's square-norm branch N_u=c², this gives
 c=M_rel*c_*, t=Den(S)=M_rel²*t_*, gcd(c_*t_*,M_rel)=1.


In particular the Gaussian extreme c_p=2lambda is PHYSICALLY EMPTY on this fresh equal-tau packet, for p1mod8 as well as p5mod8. In the old G local model S and targeted V are units, so d_i=(S-V)/2 is a unit (3u/4 modp), whereas the original physical triangle requires a pole of depth2lambda. Equivalently, its inferred local hypotenuse depths are (0,lambda,lambda) instead of (lambda,lambda,lambda); a content prime would be needed in the missing direction, contradicting freshness.


This is an exact original-space-triangle adapter, not a quartic-root identification and not a local density argument.130's strict-interior exclusion is retained and now has a shorter same-physical-denominator proof.131's abstract local D/G classifications and133's G p1mod8 necessity remain algebraically valid; the G model has no occupancy on the full fresh physical packet.132's H_G pullback remains true but its fresh G divisor receiver is vacuous because M_G=1. Retire the LARGE FRESH GAUSSIAN EXTREME TAIL as a physical research branch; retain every D Legendre/pole/singular-shell receiver.


SCOPE: odd split fresh relative support only, with the actual targeted anti-root unit theorem and original equal-tau content. No exclusion is claimed at2, at content-supported primes, or for arbitrary residual/cubic/local points without physical packet reconstruction. Finite nonzero u is used for the displayed N_u allocation; no new projective u=infinity theorem is promoted. The valuation statement from d_i itself does not use an identification with quartic theta.


Normalized48 can consequently be written with N_*=(c/M_rel)², Phi_*=Phi/M_rel² and W_*=W/M_rel². Then W_*²=-N_*Phi_* implies -Phi_* is an integer square. This is the old discriminant condition after the now-proved physical norm-square restriction, NOT another independent saving.


## 3. The signed compatibility equation is automatic on the symmetric surface
Define the symmetric surface polynomial
 T(v)=(SE+P)²-S²P(4S-P), E=sum_{i<j}v_iv_j, P=v_1v_2v_3.
For delta_i²=1-d_i² there is the exact eliminant identity
 product_{epsilon_i in {+1,-1}}(1+epsilon_1 delta_1+epsilon_2 delta_2+epsilon_3 delta_3)=T(v).
An explicit radical-free left side, with q_i=1-d_i², is
 [1+sum q_i²-2sum q_i-2sum_{i<j}q_iq_j]²-64q_1q_2q_3.


If all six1+/-d_i are rational squares, choose rational square roots L_i^+,L_i^- and delta_i=L_i^+L_i^-. Since T(v)=0, some sign choice has sum delta_i=-1. Flipping one root sign realizes each delta sign. Thus133's signed sum is NOT a further independent arithmetic filter once the six squares and the symmetric surface are imposed.


On the nondegenerate open branch d_i!=0 and1+/-d_i!=0, the compatible delta-sign triple is UNIQUE. If two triples worked, the sum over the nonempty set of flipped deltas would be zero. A singleton would force delta_i=0 and d_i²=1, impossible because the six rational squares would include2. Flipping all three contradicts sum delta_i=-1. Flipping two forces the remaining delta_k=-1 and hence d_k=0, excluded. For fixed compatible deltas, simultaneous flipping of L_i^+,L_i^- only changes the signs of x_i,y_i; x_i>0 selects exactly one choice per direction. Therefore an ordered signed anti-root triple has a UNIQUE positive normalized direction lift, improving133's safe at-most64 bound.


The open mask is essential. Zero-edge boundary triples can have several delta-sign branches; they are not positive endpoints. On the finite nonzero-u real split-cubic branch with S,P nonzero, d_i=0 would give v_j=-v_k and P/S=-v_j², contradicting P/S=4u²/(1+u²)>0. Still retain explicit nondegenerate masks in the counting population.


## 4. Four square tests suffice on square norm; exact endpoint-cover interface
On A=1+u² in Q², the133 product identities make
 product_i(1+d_i), product_i(1-d_i)
nonzero rational squares on the physical open mask. Hence it suffices to test the FOUR values
 1+d_1,1-d_1,1+d_2,1-d_2 in Q²;
the third plus/minus values follow by division by nonzero squares. Any two labeled directions may be used. This is a sufficient generating set of square tests, NOT a proof that their squareclasses are generically independent.


For an ordered rational anti-root triple on T(v)=0, on the nondegenerate open mask with finite nonzero u and A square, these four tests are equivalent to a unique positive normalized cuboid direction lift. Reconstruct via the unique delta signs and133's x_i,y_i, use R=lcm sqrt(Den d_i), and scale by that R to recover primitive edges and integral opposite face diagonals. To belong to a PREASSIGNED Stage37 T11 packet, still verify the original Gaussian orientation, coefficient, parity and cyclic-cover masks; the denominator identities alone are not a blanket packet converse.


An ordered positive endpoint has at most8 signed-y choices, and each ordered signed v triple has at most1 positive direction inverse on this open branch. Canonical ordering/orientation must remove this bounded witness multiplicity so one endpoint is counted once. No rational free sign parameter remains. This exact denominator/height interface is suitable for a same-measure count; it does not establish that count.


## Audit, verification, scope and next action
verify_m3_t11_134.py PASS:1331 generic rational eliminant identities;307 primitive rational unit-circle denominator identities;1000 arbitrary rational torus triples checking the eliminant versus signed sums (these are not physical sphere points);307 zero-edge boundary sphere/content/height tests showing why the open mask matters;144 old G local cubic-split/unit-rootline examples at p17,41,73,89,97,113 with square norm units, whose inferred triangle-depth pattern fails equal tau. Local norm-square means local units only; no global physical point is claimed. Physical endpoints enumerated=0. Symbolic replay has three zero identities. The proofs, not finite tests, establish branch emptiness and uniqueness; no positive physical endpoint was found or enumerated. Audit is within-session, not independent external.


Retain129's square-norm S4 residual class/local persistence: it is nonphysical and does not establish the four-square or denominator packet lift.123 class-group factors retained.120 remains RETRACTED. TI stays parked. Global power saving, P/M3 limit, nonexistence and primary closure flags remain false.


NEXT=M3-T11-135
ATTACK=DenominatorOnlyFourSquareExactPhysicalHeightMovingSupport
Read134 then133,045/046 and later D singular shells; target square-norm ordered anti-root triples with the FOUR square tests and exact q_i=tau*c_i, R=(h_1h_2h_3)tau<=B. On fresh relative support impose c_p=0, Q_S=M_rel² and C_u=1 from the outset. Seek the remaining denominator-extreme moving-S/active-M_rel support theorem on this exact measure, retaining all coefficient/orientation/cyclic filters. The canonical fixed-packet one-twelfth/primary exponent budgets remain unchanged. Do not resume a fresh Gaussian tail, a signed-sum rarity screen, a six-independent-square-density argument, or an ambient rational height substitution. Existing fixed-u/fixed-tau subpolynomial multiplicity does not count moving support.


ARTIFACT_IDS=card:1NVKsuCg4-ZK7Pq32p_6Xl-Cl4E85Qb6Z;audit:1d7403fZeg7xxba0eHdU6dLDU0Mo5rtkr;script:1ATMODmo9-QTzX650zTmMVI06TWaBt1N7;json:1T-q00P88la4Etu71Wm3uDiK5c1u3t_GE;wl:13DoxVxkMEUV46a_kMsHAtibWDvjoE9nl


CURRENT AUTHORITY CONTROL — M3-T11-134 AUDITED / FRESH DENOMINATOR ONLY AND EXACT FOUR SQUARE HEIGHT LIFT
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-134
ACTIVE_RESEARCH_CARD_FILE_ID=1NVKsuCg4-ZK7Pq32p_6Xl-Cl4E85Qb6Z
LATEST_RESEARCH_CARD=M3-T11-134
LATEST_AUDITED_RESEARCH_CARD=M3-T11-134
LATEST_AUDIT_FILE_ID=1d7403fZeg7xxba0eHdU6dLDU0Mo5rtkr
LATEST_VERIFICATION_SCRIPT_FILE_ID=1ATMODmo9-QTzX650zTmMVI06TWaBt1N7
LATEST_VERIFICATION_JSON_FILE_ID=1T-q00P88la4Etu71Wm3uDiK5c1u3t_GE
LATEST_SYMBOLIC_REPLAY_FILE_ID=13DoxVxkMEUV46a_kMsHAtibWDvjoE9nl
LATEST_CARD_STATUS=PROVED_EXACT_FRESH_DENOMINATOR_ONLY_ROUTER_AND_PHYSICAL_HEIGHT_ADAPTER / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
LATEST_AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-135
CURRENT_ATTACK=DenominatorOnlyFourSquareExactPhysicalHeightMovingSupport
NEXT_LEGAL_ACTION=Read134 then133 and045/046/D singularshells. Freshc_p=0,Q_S=Mrel²,C_u=1,M_G=1 fromstart. CountsquareN orderedactualanti-root triples withfour squaretests andq_i=sqrtDen((S-v_i)/2)=tau*c_i,R=Hc*tau<=B plusoriginalpacketfilters. NeedremainingD moving-S/active-Mrel supporttheorem; noGtail,signedsumrarity,orambientheight.
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
STARTUP=MAIN/INDEX currentcontrol ->134 card/audit/replay -> activeROUTE/RESULT-LEDGER latest134 ->133,ROUTE6/7/32/37/48,045/046 andlaterDsingularshells. No fullhistoryreread.
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
PHYSICAL_133_SIGNED_ADAPTER=v_i=2sum(x_j*y_j)-4x_i*y_i;d_i=(S-v_i)/2=2x_i*y_i. L_i+/-²=1+/-d_i,all6nonzero.
PHYSICAL_133_NORM_SQUARE=On finiteu branch physicalN_u=a²+b²=c² NECESSARY. ProductsLplus²=(2+S+Su)²/(4A),Lminus²=(2-S+Su)²/(4A),A=1+u². Atleastonenumeratornonzero,soA square. Splitcubic alone insufficient.
PHYSICAL_133_GAUSSIAN_ROUTER=EveryfreshGprime p1mod8;freshp5mod8 forcedD. Previouslyconditional131 squareN clause nowunconditionalPHYSICAL byglobalNsquare. Targethalfangle andpolecriterion areone restriction,nottwofilters.
PHYSICAL_133_EXACT_LIFT=Sixsquares AND signed sumLplus*Lminus=-1 ANDpositive x_i=(Lplus+Lminus)/2. Atmost64branches perorderedv. PrimitiveR0=lcmDen(x_i);originalcontent/orientation/coefficients/cyclicpacketfilters retained.
PHYSICAL_133_VERIFICATION=160finitefield/180splitlocalG/500rationalsplitenlargement/277zero-edgeboundary PASS;7symboliczero;physicalendpointcount0. Within-sessionauditNOTexternal.
PHYSICAL_133_SCOPE=SquareNconic notendpoints oruniformsupportcount.129squareN S4/localpersistence RETAINED nonphysical;123Cl2 retained. GlobalcountOPEN.
PHYSICAL_134_DENOMINATOR=Den(d_i)=D_i² exactly, d_i=(S-v_i)/2;D_i physicalhypotenuseNOTanti-rootB_i. R=lcmD_i,h_i=R/D_i,tau=gcdD_i=productD_i/R²,c_i=D_i/tau.
PHYSICAL_134_FRESH_D_ONLY=Atodd splitfresh p^lambda all3D_i depthlambda,all3d_i depth-2lambda. Targetv_i unitforcesvpS=-2lambda,c_p=0. Q_S=Mrel²,C_u=1,M_D=Mrel,M_G=1. FreshGaussianextremeEMPTY includingp1mod8;noGtailresearch.
PHYSICAL_134_G_SCOPE=131Glocalclassification/133p1mod8necessity RETAINED algebraicenlargement;Goccupancyfails originalequal-tauphysicalhypotenuses. No claimat2/content/infinity.130interiorempty retainedwithshorterdenominatorproof.
PHYSICAL_134_SIGNED_ELIMINANT=Product8(1+sum epsilon_i delta_i)=T(v),delta_i²=1-d_i². Signedsumautomaticaftersixsquares/surface;uniquepositive directionlift onnondegenerateopenmask.133atmost64 bound sharpened,NOTnewcountsaving.
PHYSICAL_134_FOUR_SQUARES=OnA=1+u² squareandnonzerofactors,1+/-d_1 and1+/-d_2 squares implyboththirdvalues via133productidentities. Sufficientsquaretestset,NOTgenericindependence/density.
PHYSICAL_134_HEIGHT=IntrinsicR=sqrt(lcmDen(d_i))<=B;fixedpacketD_i=tau*c_i andR=Hc*tau. DenS/Denvi divideR². Originalorientation/coefficients/cyclicmasks andoneendpointonecountretained.
PHYSICAL_134_VERIFICATION=1331eliminant/307unitcircledenominator/1000off-spheretorus/307zero-edgeboundary/144oldGlocalimpostor PASS;3symboliczero;physicalendpointcount0;withinsessionauditNOTexternal.
PHYSICAL_134_OPEN=RemainingD-onlymovingS/activeMrel support. Fixed-u/fixed-tau multiplicitydoesNOTcountmoving support;globalcredit0/gateOPEN.129squareNresidualpersistence/123Cl2 retained,120retractionretained.
LOWER_OPERATIONAL_POINTERS=Historical and superseded by this current control; mathematical statements retain their audited scope.
