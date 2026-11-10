# M3-T11-124 — Reduced theta label tail and its relaxed-population barrier

CARD_ID: M3-T11-124
CANONICAL_CARD_KEY: M3-T11-124
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-124
現行一覧の状態: PROVED_SCOPED_LABEL_BOUND / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / NO_GLOBAL_COUNTING_CREDIT
種別: THETA_REDUCED_LABEL_TAIL / CANCELLATION_ADAPTER / COARSE_BARRIER
要点: 既約thetaのラベル尾部 O(VU/L³)。四乗条件だけの緩和集団では一十二分尺度の障壁。
主張の抜粋: A=M^4*N0*Psi/g,C=(2abs)^2/g; Etheta<=B^o min(2UV,(8/3)VU/L³). 非空U>=L^4。p^4ラベルは物理点ではない。
対象・測度: Exact R<=B fixed packet; generic full-S theta!=0 subset; one endpoint per count.
依存関係: 093 audited fixed-theta;094 cofactor/theta0;095 old-w;096 Kummer;123 routing.
再開条件の抜粋: 125完了：物理theta分母parityとjoint b-height尾部。次126実現numerator/cofactor支持。124の粗いp4ラベルは依然NONPHYSICAL。TIparked。
旧詳細位置: ROUTE/LEDGER M3-T11-124; audit 1FMUSkaGf8wT3tMEYEVj_Z8gp3TNmrje4
旧詳細リンク: M3-T11-124.md
旧LEDGERリンク: K16-C3-M3-RESULT-LEDGER

## Retained LEDGER source 1
SOURCE_START: 1107879
SOURCE_END: 1118220
SOURCE_SHA256: fbac1c48212233fc52f1c3bb3058eccef7dc04a4da7877b5ddf50ee374d778b8

# M3-T11-124 — Reduced theta label tail and its relaxed-population barrier
STATUS=PROVED_SCOPED_LABEL_BOUND / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / NO_GLOBAL_COUNTING_CREDIT
PRIMARY_GATE=M3-T11-GATE-001 OPEN
DATE=2026-09-30
CURRENT_AUTHORITY=Stage37 Drive MAIN/INDEX/RESULT-LEDGER/active ROUTE, latest audited123.
DEPENDENCIES=audited093 fixed-theta uniform B^o(1) interface;094 homogeneous cofactor and theta=0 elimination;095 tangent/old-w firewall;096 Kummer firewall;123 current routing.
AUDIT_MODE=within-session adversarial rederivation, not external or independent-agent review.


## Population and measure
One fixed content/coefficient packet of nondegenerate Stage37 physical endpoints on exact R<=B, restricted to audited generic full-S-denominator branch, theta!=0. M=M_rel is its positive relative-fresh conductor. No other denominator allocation is covered. Each physical endpoint is counted once. Parameter bounds below define subsets of this same population; they are NOT new physical-height cutoffs.


Audited093 supplies M^4|A and gcd(C,M)=1 for theta=A/C reduced, C>0, A!=0, and at most B^o(1) physical endpoints per fixed theta in the packet, uniformly for physical-induced polynomial heights. We use that multiplicity exactly once. theta=0 is already physically eliminated by094. No new elliptic theorem is asserted here.


## 1. Exact reduced cofactor adapter
From094, write N=a²+b²=M²N0, t=M²t0, gcd(N0*t0*a*b*s,M)=1,
Psi=N0*s²-12abst0+4a²M²t0²,
W=N0*Psi, H=(2abs)², g=gcd(|W|,H).
For W!=0, gcd(H,M)=1, hence the exact reduced fraction is
A=M^4*(W/g), C=H/g.
In particular q=A/M^4=W/g is an integer, gcd(q,C)=1, gcd(C,M)=1.
This adapter retains cancellation g; setting g=1 without proof would incorrectly identify the actual theta numerator height with a homogeneous polynomial height.


## 2. Deterministic global label tail
Let U,V,L be integers >=1. Let T(U,V,L) contain reduced nonzero A/C with |A|<=U, C<=V for which SOME integer M>=L satisfies M^4|A. Allowing all M, all denominators and both signs only enlarges the physical support. Then
|T(U,V,L)| <= 2V sum_{M=L}^{floor(U^(1/4))} floor(U/M^4)
<= (8/3) VU/L^3.
Also |T|<=2UV; T is empty if L^4>U.
Proof: for each M there are floor(U/M^4) positive numerator choices and at most V denominators; signs cost2. Summing over M overcounts repeated labels, which is legal for an upper bound. The tail of sum M^-4 is at most L^-4+1/(3L^3)<=4/(3L^3). Coprimality and any restrictions on prime factors of M may be discarded for this upper bound.


Thus the EXACT physical subset with |A|<=U,C<=V,M_rel>=L satisfies
E_theta(B;U,V,L) <= B^o(1) min(2UV,(8/3)VU/L^3).
This is an endpoint bound via realized-label containment and ONE fixed-theta multiplicity, not an ambient divisibility probability. Uniformity uses the retained polynomial-height interface; no assertion is made for arbitrary external theta of superpolynomial height.


Dyadically L<=M<2L, the same bound follows by counting pairs (M,q), |q|<=U/L^4, then denominators. Neither q nor theta is independent from the old carrier.


## 3. Feasibility and target
For a nonempty shell, U>=L^4 is necessary. In power notation U=B^u,V=B^v,L=B^m (constant factors allowed),
E_theta <= B^(u+v-3m+o(1)),
and a sufficient scoped one-twelfth window is u+v-3m<1/12, with a fixed strict margin.
Feasibility requires u>=4m and v>=0, so this exponent is at least m. Therefore this particular bound cannot itself supply a fixed saving below B^(1/12) on shells with m>=1/12. If a hard threshold is instead B^(1/12-eta), keep eta explicitly: feasibility alone does not rule out the intervening window. No global theorem forcing U,V into the sufficient window has been proved.


This is a limitation of the displayed receiver, not a lower bound for physical endpoints.


## 4. Sharp coarse-constraint obstruction
In the RELAXED label space choose M=p, theta=p^4/1 for primes L<=p<=2L with p=5 mod12, omitting primes from any fixed finite exceptional packet.
These distinct labels satisfy nonzero theta, fresh split-prime support p=1 mod4, denominator coprime to M, fourth-power divisibility, and the p=5 mod12 exact saturation v_p(A)=4v_p(M).
With U=(2L)^4,V=1 the count is asymptotic to L/(4 log L) by the fixed-modulus prime number theorem in arithmetic progressions. Hence these explicitly listed coarse constraints alone cannot imply O(L^(1-delta)) for any fixed delta>0. Taking L=B^(1/12) gives B^(1/12-o(1)) relaxed labels.


IMPORTANT SCOPE: These are not asserted to arise from any physical endpoint, reduced (a,b,s,t), rational r, elliptic point with v=u², or exact R<=B. They need not satisfy other conductor restrictions imposed by a separate physical subbranch. No lower bound, no existence evidence, and no no-go for the full nonlinear theta route follows. A new physical realization relation or a proved restriction on admissible conductors can improve the result; the example only blocks using the listed coarse constraints by themselves.
Source for the classical AP theorem (not a physical density assertion):
https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_pset9.pdf
Problem5, pp7–8 (PDF page index6), states pi(x;m,a)~x/(phi(m)log x). Apply m=12,a=5; subtract at2L and L; a fixed finite deletion is negligible.


## 5. Anti-loop and next experiment
Do not multiply this tail by M^-4, the ell M² carrier, exact saturation, old-w/tangent, ordinary Kummer, residual character, or split bracket squareclasses. Do not charge fixed-theta and fixed-u multiplicities together. Do not drop gcd cancellation g. Retain all096/098–105 firewalls and withdrawn120.


NEXT_RESEARCH_CARD_ID=M3-T11-125
CURRENT_ATTACK=ThetaHomogeneousCofactorActualRealizationCorrelation
NEXT_LEGAL_ACTION=Starting with A=M^4 N0*Psi/g and C=(2abs)^2/g, derive a same-R<=B restriction on ACTUALLY realized (M,q,C), retaining the original rational-r/endpoint equation and v=u². Seek a cancellation/height/cofactor correlation that covers the shells outside u+v-3m<1/12; do not count the relaxed labels as physical. Ordinary theta fourth-power divisibility alone is now a frozen standalone saving receiver. Full nonlocal theta realization remains live;123 S4 realized norm-kernel/cross-u remains a retained alternative. TI stays parked.


## Verification and credits
Replay verify_m3_t11_124.py checks324 finite label boxes and200 exact homogeneous reductions with Fraction arithmetic; prime examples at L=10,100,1000,10000 give1,6,33,261 labels. These are sanity checks; analytic proofs above establish the theorems. No search for physical solutions was performed. Audit rechecks cancellation, floor/tail constants, boundary feasibility, label-versus-endpoint scope and AP asymptotic separately.
SCOPED_ENDPOINT_UPPER_BOUND=true
NEW_GLOBAL_COUNTING_CREDIT=false
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false




CARD_FILE_ID=1amJWpDN3KJ3L0Y40UpyBc9t_GFPZCDv_
CARD_URL=https://drive.google.com/file/d/1amJWpDN3KJ3L0Y40UpyBc9t_GFPZCDv_/view
AUDIT_FILE_ID=1FMUSkaGf8wT3tMEYEVj_Z8gp3TNmrje4
AUDIT_URL=https://drive.google.com/file/d/1FMUSkaGf8wT3tMEYEVj_Z8gp3TNmrje4/view
VERIFICATION_SCRIPT_FILE_ID=1KAuQrRx_Now3TrzbQ-fi4Dta8Jtx_Vvf
VERIFICATION_JSON_FILE_ID=1V7faZou57oAkU4EjHdx4RpF4R5_gdg5-


CURRENT_CONTROL_AT_PROMOTION
CURRENT AUTHORITY CONTROL — M3-T11-124 AUDITED / REDUCED THETA LABEL TAIL
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-124
ACTIVE_RESEARCH_CARD_FILE_ID=1amJWpDN3KJ3L0Y40UpyBc9t_GFPZCDv_
LATEST_RESEARCH_CARD=M3-T11-124
LATEST_AUDITED_RESEARCH_CARD=M3-T11-124
LATEST_AUDIT_FILE_ID=1FMUSkaGf8wT3tMEYEVj_Z8gp3TNmrje4
LATEST_VERIFICATION_SCRIPT_FILE_ID=1KAuQrRx_Now3TrzbQ-fi4Dta8Jtx_Vvf
LATEST_VERIFICATION_JSON_FILE_ID=1V7faZou57oAkU4EjHdx4RpF4R5_gdg5-
LATEST_CARD_STATUS=PROVED_SCOPED_LABEL_BOUND / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / NO_GLOBAL_COUNTING_CREDIT
LATEST_AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-125
CURRENT_ATTACK=ThetaHomogeneousCofactorActualRealizationCorrelation
NEXT_LEGAL_ACTION=Use audited094 A=M^4*N0*Psi/g, C=(2abs)^2/g with g=gcd(|N0*Psi|,(2abs)^2), retaining original rational-r/endpoint equation and v=u². Prove a same-R<=B restriction on ACTUALLY realized(M,q,C) covering shells outside u+v-3m<1/12. No relaxed-label physical lower bound. S4 realized norm-kernel/cross-u retained alternative.
THETA_124_SCOPED_BOUND=E_theta(B;|A|<=U,C<=V,M>=L)<=B^o(1)*min(2UV,(8/3)VU/L³); empty if U<L^4. Audited093 fixed-theta multiplicity used exactly once.
THETA_124_FEASIBILITY=Nonempty power shell requires u>=4m,v>=0, so displayed exponentu+v-3m>=m. This receiver alone cannot certify below-one-twelfth fixed saving whenm>=1/12; retain eta for smaller thresholds.
THETA_124_COARSE_OBSTRUCTION=Relaxed theta=p^4,C=1,M=p=5mod12 gives ~L/(4logL) labels at U=(2L)^4; NOT physical endpoints and NOT full theta-route no-go.
THETA_124_STANDALONE_FOURTH_POWER_SAVING_RECEIVER=FROZEN; actual cofactor/cancellation realization remains LIVE.
S4_123_STATUS=RETAINED; coarse norm[-1] fiber universally nonempty, full Selmer/realized cross-u unresolved; retain Cl(K_u)[2].
PHI_122_STATUS=RETAINED_PROVED_EXACT_STRUCTURE / JOINT_DENOMINATOR_SUPPORT_RECEIVER_RETIRED
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
BACKWARD_REAUDIT_117_119=PASS_WITH_RETAINED_SCOPE_LIMITS
STARTUP=MAIN top control ->124 card/audit/replay -> active ROUTE latest control -> INDEX/RESULT-LEDGER124; targeted093/094/095/096 only as needed. Known history need not be reread.
PRIMARY_RECEIVER=P(B)<=B^o(1) A_1,1(B); sufficient A_1,1(B)<<B^(1/3-eta) for fixedeta>0 on exact physical measure.
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
SCOPED_ENDPOINT_UPPER_BOUND=true
NEW_GLOBAL_COUNTING_CREDIT=false
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
LOWER_OPERATIONAL_POINTERS=Historical and superseded by this current control; mathematical statements retain their audited scope.
