# M3-T11-131 — Extreme actual anti-root orientation and coupled linear congruence

CARD_ID: M3-T11-131
CANONICAL_CARD_KEY: M3-T11-131
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-131
現行一覧の状態: PROVED_EXACT_EXTREME_LOCAL_CLASSIFICATION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_CREDIT0
種別: ACTUAL_ANTIROOT_ORIENTATION / NONZERO_COUPLED_INTEGER
要点: Gaussian extremeで2S=u modp^(2lambda)。H_G=2bs-atは非零でM_G²が割り切る。
主張の抜粋: D:V=+u modp^L/rootline automatic;G:V=-u modp^L iff2S=u; polechi(-2/A0)=1。squareNならG prime1mod8。
対象・測度: Exact physical necessary conditions; NO height/count saving.800D/272G congruence/40G pole checks PASS.
依存関係: 130,ROUTE35–37/47–50;042 saturation RETAINED not new,043/045 scopes retained;120 remains retracted.
再開条件の抜粋: 132完了：H高さではM_G消去、Hはconsumed rootline。次133 global physical lift。
旧詳細位置: ROUTE/LEDGER131; audit 1cRyuP0LeYE50nkoxz6WnLKh6TQGMeOz8
旧詳細リンク: M3-T11-131.md
旧LEDGERリンク: K16-C3-M3-RESULT-LEDGER

## Retained LEDGER source 1
SOURCE_START: 1199128
SOURCE_END: 1213409
SOURCE_SHA256: a9bfa6c39ca2b8bc2169755ac6248b307a325f4e8e4ada82bfaea9b8accd269b

# M3-T11-131 — Extreme actual anti-root orientation and coupled linear congruence


Authority: Stage37 Drive current130, MAIN/INDEX/ROUTE/RESULT-LEDGER and130 card freshly read. Status: PROVED_EXACT_EXTREME_LOCAL_CLASSIFICATION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0. Audit is internal, not independent external review. TI remains parked.


## Result


For an odd split relative-fresh p^lambda || m_i on the nondegenerate physical branch, put L=2lambda, A=1+u^2, u=a/b reduced, S=s/t reduced with t>0. Retain130: strict interior allocation is empty. The two remaining cases have the following actual targeted anti-root V:


| Allocation | Exact valuations | Actual unit root-line |
| --- | --- | --- |
| c_p=0, denominator extreme | v_p(A)=L, v_p(S)=-L | V congruent u mod p^L; V^2+1 divisible by p^L automatically |
| c_p=L, Gaussian extreme | v_p(A)=2L, S and S-u units | V^2+1 divisible by p^L iff 2S congruent u mod p^L; then V congruent -u mod p^L |


The Gaussian case additionally has both pole roots in Q_p iff chi_p(-2/A_0)=+1, with A_0=A/p^(2L) a unit. Under the displayed root-line congruence this character is sufficient for all three cubic roots over Q_p with valuations (0,-L,-L); there is no additional higher-precision cubic-splitting obstruction. This only classifies the actual cubic plus its targeted root-line, not the entire Gaussian-core/physical lift.


In particular, if N_u=a^2+b^2 is a rational integer square, A is a rational square and A_0 is a local square. A Gaussian-extreme fresh prime must then satisfy p=1 mod8. Fresh primes p=5 mod8 must be denominator extreme. This is not a fixed-power density or a global endpoint theorem.


## Exact proof: denominator extreme


ROUTE35 gives f(X)=X^3-SX^2+EX-P, E=4u(S-u)/A, P=4u^2S/A. Its roots are the actual physical v_i; ROUTE36–37 give one targeted unit root with norm depth >=L and two pole roots of valuation -L. At c_p=0, g=p^(2L)f is integral with ascending coefficient valuations (0,0,L,2L). Its reduction is a nonzero multiple of X-u; there is a unique unit root V, with unit derivative. The identity


f(u)=u^2[u(A-4)/A-S]


has valuation at least -L, because both bracket terms have valuation -L. Consequently v_p(g(u))>=L and, by the unit-derivative factorization, v_p(V-u)>=L. Since v_p(A)=L, the norm V^2+1=A+(V-u)(V+u) has valuation >=L. This required root-line imposes no extra condition on S in this branch. Pole-root splitting is still a separate condition; no denominator-extreme support count is proved.


For a simple pole reduction, writing s_0=p^L S and a_0=A/p^L, the scaled cubic p^(3L)f(Y/p^L) reduces to


Y [Y^2-s_0Y+4u s_0/a_0].


Its quadratic discriminant s_0^2-16u s_0/a_0 must be a square modulo p. A nonzero square is sufficient by Hensel; the zero-discriminant case is not disposed of here. This is the existing045 Legendre receiver in pole-root coordinates, not a newly chargeable density.


## Exact proof: Gaussian extreme


Here v_p(A)=2L and v_p(S)>=0 from allocation. The actual roots give v_p(E)=v_p(P)=-2L: the product of the two pole roots uniquely dominates E and all three root valuations determine P. Since P=4u^2S/A, S is a unit, and E=4u(S-u)/A forces S-u a unit. The exact norm saturation is already retained042, not a new theorem; independently, if the capped branch had v_p(A)>2L, the P valuation would force v_p(S)>0, and E would then have the wrong valuation.


Now g=p^(2L)f has unit constant and linear coefficients; its remaining coefficients vanish modulo p. Its unique unit root reduces to uS/(S-u). Because u^2=-1 mod p, the norm of this residue vanishes iff 2S=u mod p. In that case its residue is -u, not +u.


Direct evaluation gives


f(-u)=u^2 [u(4-A)-S(A+8)]/A.


For a root V reducing to -u, the same unit-derivative factorization gives


v_p(V+u)=v_p(g(-u))=v_p(u(4-A)-S(A+8)).


As v_p(A)=2L, this valuation is >=L iff 2S-u vanishes modulo p^L (p is odd, so8 is a unit). Since V-u is a unit, V^2+1=A+(V+u)(V-u) vanishes modulo p^L iff V+u does. This proves the exact equivalence, including the case where the bracket is zero. When the congruence fails already modulo p, the norm root-line fails already modulo p.


Under 2S=u mod p^L, the pole-scaled cubic reduces to


Y [Y^2+2/A_0].


Thus two pole roots require chi_p(-2/A_0)=+1. Conversely this gives two simple nonzero roots and one simple zero root modulo p, hence all lift uniquely; the nonzero roots give poles of valuation -L, and the zero root corresponds to the already-certified unit V. For square N_u, chi_p(A_0)=1 and p=1 mod4, so chi_p(-2/A_0)=chi_p(2); the elementary supplementary law gives p=1 mod8. This character also restates the discriminant-square equation: Q(S,u)=2 mod p under u^2=-1 and S=u/2. It is not an independent second saving.


## Global integer receiver and nonzero firewall


Let M_D be the product p^lambda over denominator-extreme fresh primes and M_G over Gaussian-extreme primes. Then M_D M_G=M_rel, the factors are coprime, Q_S=M_D^2, C_u=M_G^2, and the exact fresh norm is M_D^2 M_G^4. These are retained130/042 routing identities.


The new Gaussian root-line equivalence gives the integral coupled receiver


H_G=2 b s-a t,
M_G^2 divides H_G,
gcd(a b t,M_G)=1.


This links the same physical S and u; it does not identify distinct anti-roots. The targeted anti-root has orientation +u at D primes and -u at G primes. No product of three root-line densities is taken.


Moreover H_G cannot vanish on a physical packet: H_G=0 implies S=u/2, whereas the original split-discriminant quartic satisfies exactly


Q(u/2,u)=u^2(112+145u^2+u^4)/16>0 for real u!=0.


This contradicts Y^2=-(1+u^2)Q(S,u). Hence |H_G|>=M_G^2. It is a legitimate nonzero integer divisor lock on the original packet, not yet a height/counting theorem. Do not replace physical R<=B by arbitrary heights of a,b,s,t, or assume uniform residues of H_G.


If N_u=c^2 and e=v_p(c)>0 at a fresh prime: denominator allocation requires lambda=e; Gaussian allocation requires e even, lambda=e/2 and p=1 mod8. This is an exact assignment restriction, not an endpoint population estimate.


## Replay, audit and novelty boundary


verify_m3_t11_131.py uses standard-library exact rational arithmetic and digit-by-digit Hensel lifting. PASS:800 denominator packets,272 Gaussian congruence perturbations,40 Gaussian pole packets, p=5,13,17,29,41 and lambda=1..4, both square/nonsquare norm units. It verifies the root-line equivalence and the pole-splitting character, including lifting admitted pole roots. Symbolic replay verifies both f(±u) identities and the positive-real Q(u/2,u) identity. Physical endpoints enumerated0; the synthetic local packets are NOT rational physical endpoints. In particular S=u/2 test packets are globally impossible over R, yet can be locally admissible at a fresh p; they do not prove a global impostor family.


Targeted anti-duplication: retained042 exact norm saturation and043 absence of Gaussian Phi_* residual valuation remain unchanged; neither is claimed new. Retained045/046 and their later audited successors retain the denominator-extreme Legendre/singular-carrier scope. Sections39/40's corrected inverse remains u=SP/(SE+P), not the retracted missing-S inverse. New here are the actual unit-root orientation/equivalence, H_G nonzero coupled integer receiver, and its square-N Gaussian-prime consequence. M3-T11-120 stays retracted: no quartic theta is substituted for physical z or anti-root V, no extreme phi allocation or fourth-power tail is reinstated.


Scope: odd split fresh primes outside content, u finite and nonzero, original nondegenerate packet. Projective infinity on M_rel>1 is already excluded by retained035; no new statement for M_rel=1, content or2-primary/degenerate loci. The zero-discriminant denominator pole case remains a boundary requiring its existing receiver. Other Gaussian-core square/lifting, common-global-point and exact-height conditions are not discarded.


## Next legal continuation


Reserve M3-T11-132: GaussianExtremeCoupledNonzeroIntegerReceiverSamePhysicalHeight. On exact R<=B, determine the actual joint height/range/multiplicity of (a,b,s,t,H_G) and frozen content data, especially the large-M_G branch, and whether the new nonzero divisor lock supplies a legal same-measure tail. If H_G is already consumed by the original root-line product, record the exact no-double-charge identity and move to a genuinely joint lift. The denominator branch must retain045's Legendre receiver and all singular shells; no new higher-p-adic unit-root sieve there. Preserve130 interior exclusion and123/128/129 scoped S4 data. Do not infer a deficit merely from one congruence class per p^L at fixed ambient coordinates.


GLOBAL_COUNTING_CREDIT=0; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false.


CURRENT AUTHORITY CONTROL — M3-T11-131 AUDITED / EXTREME ANTIROOT ORIENTATION AND NONZERO COUPLED RECEIVER
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-131
ACTIVE_RESEARCH_CARD_FILE_ID=1ViXKYPeNIV_YLeSzULQF_wQPotZJdVGB
LATEST_RESEARCH_CARD=M3-T11-131
LATEST_AUDITED_RESEARCH_CARD=M3-T11-131
LATEST_AUDIT_FILE_ID=1cRyuP0LeYE50nkoxz6WnLKh6TQGMeOz8
LATEST_VERIFICATION_SCRIPT_FILE_ID=1wpBLDt99IgvE-GcRvGIhoTRpYNHGvAEw
LATEST_VERIFICATION_JSON_FILE_ID=1TezWCsZ5fYrbUh6IfFfbmGD40sw9i8cZ
LATEST_SYMBOLIC_REPLAY_FILE_ID=1x07bdWhzepf5DJSsWJuaW8DZGikjeP9L
LATEST_CARD_STATUS=PROVED_EXACT_EXTREME_LOCAL_CLASSIFICATION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
LATEST_AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-132
CURRENT_ATTACK=GaussianExtremeCoupledNonzeroIntegerReceiverSamePhysicalHeight
NEXT_LEGAL_ACTION=Read131 actualunitroot/poleclassification and nonzeroH_G receiver. OnexactR<=B derive jointheight/range/multiplicity foru=a/b,S=s/t,H_G=2bs-at,M_G²|H_G!=0 andfrozencontent. Auditdoublechargeagainst originalrootlines. Seek same-measurelargeGaussian-extremesupporttail; retainDbranch045/046/alllatersingularshells. No ambientresidue-density multiplication.
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
STARTUP=MAIN/INDEX currentcontrol ->131 card/audit/replay -> activeROUTE/RESULT-LEDGER latest131 -> targeted35-37,47-50, exactnorm042 duplicate-ID formulas,043/045 and130. No fullhistoryreread.
PRIMARY_RECEIVER=P(B)<=B^o(1) A_1,1(B); sufficient A_1,1(B)<<B^(1/3-eta) forfixedeta>0 onexactphysicalmeasure.
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
LOWER_OPERATIONAL_POINTERS=Historical and superseded by this current control; mathematical statements retain their audited scope.






STAGE37 CONTINUATION RESULT — M3-T11-132
