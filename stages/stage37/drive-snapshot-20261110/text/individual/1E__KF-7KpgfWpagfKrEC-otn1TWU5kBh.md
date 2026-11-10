# M3-T11-125 — Physical theta denominator parity and a joint b-height label tail

CARD_ID: M3-T11-125
CANONICAL_CARD_KEY: M3-T11-125
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-125
現行一覧の状態: PROVED_PHYSICAL_NECESSARY_STRUCTURE / PROVED_SCOPED_ENDPOINT_BOUND / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS
種別: THETA_DENOMINATOR_PARITY / B_HEIGHT_UNION_LABEL_TAIL
要点: 物理平方条件よりC=2^epsilon*d*k²、d|b。b-heightを含む分母候補の和集合評価。
主張の抜粋: 奇p∤bはv_p(C)偶数。p|d=>p=1mod4かつ11平方剰余。Etheta<=B^o(8/3)U/L³ min(V,4sqrt(VH)).
対象・測度: Exact R<=B fixed packet; generic full-S theta!=0, b<=H label-box subset; one physical endpoint per count.
依存関係: 092 physical homogeneous square;093 audited fixed-theta;094 cofactor;124 gcd/label tail;095/096 firewalls.
再開条件の抜粋: 126完了：theta最小判別式/componentpacketを保存。numerator全体収縮未達、次127 globalmovingcurve image。125部分集合上界保持、TIparked。
旧詳細位置: ROUTE/LEDGER M3-T11-125; audit 17IQHyrp7T-4HuyCIcJHLh3NEPe08vJJB
旧詳細リンク: M3-T11-125.md
旧LEDGERリンク: K16-C3-M3-RESULT-LEDGER

## Retained LEDGER source 1
SOURCE_START: 1118220
SOURCE_END: 1132436
SOURCE_SHA256: a86e0370163117d32fbac9c33e9d0028d9f151b77d9e4ce8962857b88a9a4d1c

# M3-T11-125 — Physical theta denominator parity and a joint b-height label tail
DATE=2026-09-30
STATUS=PROVED_PHYSICAL_NECESSARY_DENOMINATOR_STRUCTURE / PROVED_SCOPED_ENDPOINT_BOUND / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS
AUDIT_MODE=Within-session adversarial rederivation, not external or independent-agent audit.
CURRENT_AUTHORITY=Drive MAIN/INDEX/RESULT-LEDGER/active ROUTE latest124.
PRIMARY_GATE=M3-T11-GATE-001 OPEN
DEPENDENCIES=audited092 homogeneous endpoint square equation;093 fixed-theta B^o(1) and fourth-power carrier;094 theta cofactor/theta0 elimination;124 reduced cofactor and label tail. Preserve095/096/098–105 firewalls, withdrawn120, retained123 and TIparked.


## 1. Exact physical equations and notation
Take u=a/b and S=s/t reduced, b,t>0, a*b*s!=0, gcd(a,b)=gcd(s,t)=1. Put N=a²+b² and
Phi=N*s^4-16ab*s³t+(44a²-4b²)s²t²+48ab*st³-16a²t^4.
Every retained physical endpoint satisfies the audited necessary equation Omega²=-N*Phi with integral Omega. A rational square root of an integer is integral. This necessary square locus may contain nonphysical states; no converse is asserted.


Define
Q=N*s²-12ab*st+4a²t²,
J=N*s²-16ab*st+48a²t²,
Hden=(2abs)².
Then theta=N*Q/Hden, and the exact identity is
Phi+4t²Q=s²J.
It follows either by direct expansion or from audited092 Phi=-4t²Pell+s³(Ns-16abt) with Pell=Q-12a²s².


On audited full-S branch, N=M²N0,t=M²t0 and Q=M²Psi, with
Psi=N0*s²-12ab*st0+4a²M²t0².
Writing F=N0*Psi and g=gcd(|F|,Hden), theta=A/C is reduced with
A=M^4*F/g, C=Hden/g.
The full fraction gcd gcd(|NQ|,Hden) equals g because gcd(M,Hden)=1. Thus the new theorem controls the actual cancellation retained by124.


## 2. Odd denominator parity theorem
THEOREM: For every reduced theta=A/C!=0 on the necessary physical square locus above, every odd prime p not dividing b has v_p(C) even.


Proof. It suffices to show gcd(|NQ|,Hden) has even valuation at those p, since Hden is a square. Let h=v_p(a),k=v_p(s); p is odd and b is a unit.
(a) If h=k=0, p does not divide Hden.
(b) If h>0,k=0, N and Q are units; the gcd valuation is0.
(c) If h=0,k>0, t is a unit and Q=4a²t² modp is a unit. If p does not divide N the gcd valuation is0. If p divides N, Phi=-16a²t^4 modp is a unit, so Omega²=-N Phi forces v_p(N) even. The gcd valuation min(v_p(N),2k) is even.
(d) If h,k>0, N and t are units. If h!=k, the first and last terms of Q have distinct valuations2k and2h, while the middle term has valuation at leasth+k. Consequently v_p(Q)=2min(h,k), giving even gcd valuation.
If h=k=e, v_p(Q)>=2e and v_p(s²J)>=4e. If v_p(Q)<4e, Phi=-4t²Q+s²J has that same valuation; Omega² with N a unit forces v_p(Q) even. If v_p(Q)>=4e, the gcd is capped at v_p(Hden)=4e. Both cases give even gcd valuation. No division by3 or11 was used; those odd primes are included. theta=0 is excluded.


## 3. The only possible odd-parity primes and their residue conditions
If an odd prime p has v_p(C) odd, then p|b by Section2. Thus p does not divide a or N.
If p|s then Q=4a²t² modp is a unit and v_p(C)=2v_p(b*s), which is even; hence s is a unit.
Odd v_p(C) then requires
0<v_p(Q)<2v_p(b), v_p(Q) odd,
v_p(C)=2v_p(b)-v_p(Q).
Modulo p, Q=a²(s²+4t²), so s²+4t²=0. Since s is a unit, t is a unit too. Hence -1 is a square modulo p and p=1 mod4.


Under b=0 and s²=-4t² modulo p,
Phi=a²(s^4+44s²t²-16t^4)=-176a²t^4.
Therefore -N Phi=16*11*a^4*t^4 modulo p. Since p=1 mod4 excludes p=11, this is a nonzero unit. The necessary physical square equation forces 11 to be a quadratic residue modulo p.


COROLLARY: There is a UNIQUE decomposition
C=2^epsilon*d*k², epsilon in{0,1}, k>=1,
where d is odd squarefree, d|b, and every p|d has p=1 mod4 and (11|p)=+1.
No statement fixing epsilon is made. d need not be1. The complete necessary square equation remains stronger than this denominator consequence.


A local caution: (a,b,s,t)=(1,5,1,1) gives theta=-39/5, and -N Phi=-2964 is a unit square in Q_5 (its residue is1 mod5). Thus an odd b-prime may have odd denominator valuation compatibly with the local square equation. This tuple fails the real square condition and is NOT a physical endpoint. It only blocks strengthening the LOCAL argument to all denominators being squares; no global nonsquare-denominator endpoint is asserted.


## 4. Actual b-height denominator occupancy
Restrict the original exact R<=B, fixed content/coefficient packet, generic full-S theta!=0 population further by b<=H, |A|<=U,C<=V,M_rel>=L, where U,V,H,L>=1 are integers and physical-induced heights remain polynomial in B.
Let D(V,H) be the number of positive denominators admitted by Section3 for SOME b<=H. Since d|b, d<=H. Dropping squarefreeness, oddness and the residue restrictions for an upper bound gives
D(V,H) <= sum_{1<=d<=H} (floor(sqrt(V/d))+floor(sqrt(V/(2d))))
<= 2(1+1/sqrt2)*sqrt(VH) <4sqrt(VH).
Also D(V,H)<=V. A denominator might be counted several times in this enlarged sum; this is safe. There is NO sum of endpoint multiplicities over b: denominators are first unioned and each theta is counted once.


For a single fixed b, the analogous bound is
D_b(V) <= (1+1/sqrt2)*sqrt(V)*sum_{d|b,d odd squarefree} d^(-1/2)
<=2*tau(b)*sqrt(V).
This fixed-b estimate is an auxiliary denominator statement, not an extra fixed-u endpoint saving.


Replacing124's denominator factor V by the UNION count above yields
E_theta(B;U,V,H,L)
<= B^o(1)*(8/3)*(U/L³)*min(V,4sqrt(VH)).
This is a same-exact-R<=B endpoint bound for the stated subset, using audited093 fixed-theta multiplicity exactly ONCE. It is not a density product. If U<L^4 the subset is empty. Restrictions on admissible M or coprimality can only shrink the set.


In power notation U=B^u,V=B^v,H=B^h,L=B^m,
E_theta <= B^[u+min(v,(v+h)/2)-3m+o(1)].
The denominator improvement is a factor sqrt(V/H) when H is smaller than V at fixed-power scale. No theorem imposing such a scale on the WHOLE physical population is promoted.


## 5. Feasibility and hard-branch boundary
A sufficient scoped one-twelfth window is
u+min(v,(v+h)/2)-3m <1/12-delta
with a fixed strict margin.
Nonemptiness still requires u>=4m and v,h>=0. Hence the displayed exponent is at leastm.
On the actual hard threshold M_rel>B^(1/12-eta), the receiver alone cannot guarantee the required B^(1/12-delta) with delta>eta: its sufficient power exponent cannot fall below the conductor scale. This is a limitation of this receiver, NOT a lower bound for actual endpoints.


124's relaxed labels theta=p^4,C=1,M=p=5mod12 also satisfy the new coarse denominator consequence (epsilon=0,d=1,k=1), for any H>=1. They are still NOT physical homogeneous realizations. Thus adding just this denominator consequence to the coarse fourth-power/saturation constraints does not remove124's barrier. This does not rule out using the FULL Omega²=-N Phi equation, v=u², rational-r, actual cancellation/cofactor relation or other physical constraints to obtain a sparse realized numerator image.


## 6. Audit, verification and restart
Within-session hostile rederivation checked every overlapping-prime case, the odd/2 separation, the b-prime residue argument, full-S gcd equivalence, denominator union before counting theta, polynomial-height uniformity and the hard threshold eta/delta distinction.
Exact replay checks130047 primitive tuples;144640 odd-prime parity cases;117692 local-square cases;5743 locally compatible odd-b denominator cases;25 denominator boxes. Six necessary global square-locus tuples in the bounded check are NOT asserted physical cuboids. Finite checks verify implementation and sanity; the proofs above establish the lemmas.
Wolfram expansion returns identity0 and resultant
Res_t(Q,Phi)=256a^8*N*(121a²-7b²)*s^8;
the resultant is recorded as a symbolic check, not independent counting credit.


NEXT_RESEARCH_CARD_ID=M3-T11-126
CURRENT_ATTACK=ThetaRealizedNumeratorCofactorOccupancyBeyondDenominatorParity
NEXT_LEGAL_ACTION=Exploit the full normalized equation Omega0²=-N0*Phi0 together with F/g=N0*Psi/g, v=u² and rational-r on the exact physical population to bound ACTUALLY occupied (M,q=A/M^4) support. Denominator parity and pure height-box refinements alone retain a conductor-scale barrier; do not merely attempt to force their impossible hard-branch sufficient window. Retain125's scoped b-height bound for unions where applicable. Nonlocal S4 realized norm-kernel/cross-u remains an alternative. TI stays parked.
DO_NOT_REPEAT=Do not drop g; do not claim C square; do not count the denominator residue tests as independent probabilities; do not multiply fixed-theta with fixed-u/ell/x; do not revive ordinary Kummer/split bracket savings or withdrawn120; do not call local test tuples physical.


PHYSICAL_NECESSARY_DENOMINATOR_STRUCTURE=true
SCOPED_ENDPOINT_UPPER_BOUND=true
WHOLE_FULL_S_DENOMINATOR_SUPPORT_BOUND_PROVED=false
NEW_GLOBAL_COUNTING_CREDIT=false
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false




CARD_FILE_ID=1rwfCx-nGJRhORWJdkoJQ0V87SJ4Pt1vZ
CARD_URL=https://drive.google.com/file/d/1rwfCx-nGJRhORWJdkoJQ0V87SJ4Pt1vZ/view
AUDIT_FILE_ID=17IQHyrp7T-4HuyCIcJHLh3NEPe08vJJB
AUDIT_URL=https://drive.google.com/file/d/17IQHyrp7T-4HuyCIcJHLh3NEPe08vJJB/view
VERIFICATION_SCRIPT_FILE_ID=1jh1nYq2qaPDaM1EkV4HtKHWazjvDhvgY
VERIFICATION_JSON_FILE_ID=1TNr-oO4w0AKFZ4u2ivGF4UtzZShORzld
SYMBOLIC_REPLAY_FILE_ID=1QSrwR9kLcXz1YGAlqPpcwFVpAQ0zkk9L


CURRENT_CONTROL_AT_PROMOTION
CURRENT AUTHORITY CONTROL — M3-T11-125 AUDITED / PHYSICAL THETA DENOMINATOR PARITY
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-125
ACTIVE_RESEARCH_CARD_FILE_ID=1rwfCx-nGJRhORWJdkoJQ0V87SJ4Pt1vZ
LATEST_RESEARCH_CARD=M3-T11-125
LATEST_AUDITED_RESEARCH_CARD=M3-T11-125
LATEST_AUDIT_FILE_ID=17IQHyrp7T-4HuyCIcJHLh3NEPe08vJJB
LATEST_VERIFICATION_SCRIPT_FILE_ID=1jh1nYq2qaPDaM1EkV4HtKHWazjvDhvgY
LATEST_VERIFICATION_JSON_FILE_ID=1TNr-oO4w0AKFZ4u2ivGF4UtzZShORzld
LATEST_SYMBOLIC_REPLAY_FILE_ID=1QSrwR9kLcXz1YGAlqPpcwFVpAQ0zkk9L
LATEST_CARD_STATUS=PROVED_PHYSICAL_NECESSARY_DENOMINATOR_STRUCTURE / PROVED_SCOPED_ENDPOINT_BOUND / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS
LATEST_AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-126
CURRENT_ATTACK=ThetaRealizedNumeratorCofactorOccupancyBeyondDenominatorParity
NEXT_LEGAL_ACTION=Use full normalized Omega0²=-N0*Phi0 with q=A/M^4=N0*Psi/g, v=u² and original rational-r/endpoint equation to bound ACTUALLY occupied(M,q) on exact R<=B.125 denominator parity/height tail retains a conductor-scale barrier; do not try to force its impossible hard-branch sufficient window. Retain scoped125 bound where applicable. S4 realized norm-kernel/cross-u remains alternative.
THETA_125_PHYSICAL_STRUCTURE=C=2^epsilon*d*k², epsilon0or1; d odd squarefree dividesb; p|d =>p=1mod4 and11 squaremodp. Odd p not dividingb has even v_p(C). Keep actual gcd g.
THETA_125_SCOPED_BOUND=E_theta(B;|A|<=U,C<=V,b<=H,M>=L)<=B^o(1)*(8/3)*U/L³*min(V,4sqrt(VH)); empty if U<L^4. Audited093 fixed-theta multiplicity used exactly once.
THETA_125_POWER_EXPONENT=u+min(v,(v+h)/2)-3m>=m on nonempty shells. For hardM>B^(1/12-eta), this receiver alone cannot guarantee targetB^(1/12-delta) withdelta>eta. This is NOT physical lower bound or full theta no-go.
THETA_124_STATUS=RETAINED reduced-label tail and relaxedp4 barrier; C1 examples satisfy125 denominator consequence but remainNONPHYSICAL.
THETA_STANDALONE_FOURTH_POWER_OR_DENOMINATOR_PARITY_SAVING_RECEIVER=FROZEN_FOR_GLOBAL_HARD_CLOSURE; full nonlinear realized numerator/cofactor remains LIVE.
S4_123_STATUS=RETAINED; coarse norm[-1] fiber universally nonempty, full Selmer/realized cross-u unresolved; retain Cl(K_u)[2].
PHI_122_STATUS=RETAINED_PROVED_EXACT_STRUCTURE / JOINT_DENOMINATOR_SUPPORT_RECEIVER_RETIRED
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
BACKWARD_REAUDIT_117_119=PASS_WITH_RETAINED_SCOPE_LIMITS
STARTUP=MAIN top control ->125 card/audit/replay -> active ROUTE latest control -> INDEX/RESULT-LEDGER125; targeted092/093/094/124 as needed. Known history need not be reread.
PRIMARY_RECEIVER=P(B)<=B^o(1) A_1,1(B); sufficient A_1,1(B)<<B^(1/3-eta) for fixedeta>0 on exact physical measure.
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
PHYSICAL_NECESSARY_DENOMINATOR_STRUCTURE=true
SCOPED_ENDPOINT_UPPER_BOUND=true
WHOLE_FULL_S_DENOMINATOR_SUPPORT_BOUND_PROVED=false
NEW_GLOBAL_COUNTING_CREDIT=false
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
LOWER_OPERATIONAL_POINTERS=Historical and superseded by this current control; mathematical statements retain their audited scope


STAGE37 INDEPENDENT HOSTILE RE-AUDIT — M3-T11-125 — 2026-09-30
VERDICT=PASS_WITHIN_STATED_SCOPE
AUDIT_KIND=Fresh independent rederivation from current Drive authority; existing within-session PASS not taken as sufficient evidence.
CHECKED=Odd-prime denominator parity including balanced v_p(a)=v_p(s) cancellation; p|b odd-parity residue conditions; unique C=2^epsilon*d*k^2 decomposition; denominator union D(V,H)<4*sqrt(VH); same-measure fixed-theta use exactly once; hard-threshold feasibility; withdrawn M3-T11-120 noncontamination.
RESULT=No new blocker found. M3-T11-125 remains valid only as a physical NECESSARY denominator theorem plus SCOPED b-height endpoint bound. It does not prove whole-population denominator support, actual realization, global fixed-power saving, primary-gate closure, P/M3 limit, or Perfect Cuboid nonexistence.
CURRENT_AUTHORITY=LATEST_AUDITED_RESEARCH_CARD=M3-T11-125; NEXT_RESEARCH_CARD_ID=M3-T11-126.
NEXT_LEGAL_ACTION=Continue 126 only through actual normalized Omega0^2=-N0*Phi0 and N0*Psi/g realized numerator/cofactor occupancy, retaining v=u^2, rational-r, exact R<=B measure and all existing firewalls. TI remains parked.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
.
