# M3-T11-130 — Actual cubic unit root excludes strict-interior fresh allocation

CARD_ID: M3-T11-130
CANONICAL_CARD_KEY: M3-T11-130
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-130
現行一覧の状態: PROVED_EXACT_PHYSICAL_INTERIOR_EXCLUSION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_CREDIT0
種別: ACTUAL_ANTIROOT_CUBIC / STRICT_INTERIOR_EMPTY
要点: 実際の単位anti-rootがGaussian root-line深さを満たさずstrict interior fresh割当を排除。
主張の抜粋: k=2lambda-c_p; vp(V-u)=vp(V²+1)=k<2lambda。全odd split fresh interior、finite-u branch。
対象・測度: Exact physical necessary-condition contradiction; no R count/saving. 200 allocations/26 AP checks PASS.
依存関係: ROUTE35–37/47–48;029/033/040.120 remains retracted.
再開条件の抜粋: 131 completed: actual extreme orientation, Gaussian2S=u and nonzeroH_G divisor lock. Next132 same physical height/count adapter; credit0.
旧詳細位置: ROUTE/LEDGER130; audit 1UOg27VCOCjOOBt3fB746aWaipMx9Eslx
旧詳細リンク: M3-T11-130.md
旧LEDGERリンク: K16-C3-M3-RESULT-LEDGER

## Retained LEDGER source 1
SOURCE_START: 1186844
SOURCE_END: 1199128
SOURCE_SHA256: d3261806a7e87dc26a9b3cc0ffe0e719c503e97ae6dd09b97bd4043788c582d1

# M3-T11-130 — Actual cubic unit root excludes strict-interior fresh allocation


Date: 2026-09-30. Current authority: Stage37 Drive, batch129 controls. Status: PROVED_EXACT_PHYSICAL_INTERIOR_EXCLUSION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0. This is an internal rederivation, not an external review.


## Primary result and dependencies


On the canonical finite-u, nondegenerate physical packet branch, every odd split fresh prime p^lambda || m_i has only extreme allocations c_p=0 or c_p=2lambda. No physical packet has 0<c_p<2lambda. This concerns original physical anti-roots, not quartic algebra roots.


Dependencies read from current ROUTE: Section35 gives A=1+u^2, E=4uS/A-4u^2/A, P=4u^2S/A and f(X)=X^3-SX^2+EX-P, whose roots are the actual v_i. Sections36–37 (M3-T11-029/033) give the targeted v_i a p-unit with v_p(v_i^2+1)>=2lambda; the other two have valuation -2lambda. Sections47–48 (M3-T11-040) give Q_S C_u=M_rel^2, c_p=v_p(C_u), k=2lambda-c_p, and min(4lambda,v_p(N_u))=2lambda+c_p for reduced u=a/b. At an interior prime b and a are units, v_p(A)=v_p(N_u)=n=2lambda+c_p=4lambda-k and v_p(S)=-k. Positive k makes this denominator valuation exact, not just capped.


## Exact proof


Suppose 0<c_p<2lambda, hence 0<k<2lambda and n>k. The terms involving S dominate E and P, so v_p(E)=v_p(P)=-(n+k)=-4lambda. Set g(X)=p^(n+k)f(X), an integral p-adic polynomial. Its ascending coefficient valuations are (0,0,n,n+k). Mod p it is a nonzero unit multiple of X-u, because P/E reduces to u. Thus it has exactly one unit root V in Q_p, reducing to u; its derivative there is a unit. Any physical unit anti-root must equal this V.


Direct substitution gives


f(u)=u^2 [u(A-4)/A-S].


Since p is odd and v_p(A)=n>k, A-4 is a unit, and the bracket has valuation -n. Therefore v_p(g(u))=k. Since u and V have the same residue, the factorization g(u)-g(V)=(u-V) times a p-adic unit proves v_p(V-u)=k exactly. Also V+u is a unit, since p is odd. Consequently


v_p(V^2+1)=v_p(A+(V-u)(V+u))=k<2lambda.


This contradicts the original physical condition v_p(v_i^2+1)>=2lambda. The strict-interior branch is empty. The argument needs no N_u square hypothesis, S4 hypothesis, rational discriminant square assumption, residual Selmer computation, or independence model.


## Independent contradiction check


If the physical unit root V existed, V mod p=u and both V^2+1 and u^2+1 would vanish to depth at least 2lambda. The same simple Hensel branch of X^2+1 would force v_p(V-u)>=2lambda, whereas the actual cubic forces the exact smaller depth k. This uses the actual anti-root V only. It does not identify quartic theta with physical z=S/2 and does not revive retracted120.


## Concrete local impostors above the129 S4 family


Take r=932+41250j, j>=0; a=2r, b=r^2-1, c=r^2+1, u=a/b, A=c^2/b^2. This is a subfamily of129's r=8+66k and retains square N and certified S4. Set q=1/625, d=1, S=Aq^2/(8u^2), z=S/2=(cq/(4a))^2. At p=5, lambda=2, c_p=2, k=2: v_5(A)=6 and v_5(S)=-2. The q-scaled cubic reduces to Y(Y^2+1), with three simple roots 0,2,3 mod5, hence splits over Q_5. The residual w^2=-F(z)/N is also locally soluble: its valuation is -12 and its unit reduction a square. The genus3 physical-equation projection103 likewise has a Q_5 lift (T=256u^4 A w). These local algebraic tests do not enforce the physical root-line.


The unique unit root instead satisfies v_5(V^2+1)=2, below the required4. Thus even these split/local-cover impostors fail a necessary original physical equation. For j=0: (a,b,c)=(1864,868623,868625), z=48288601/1389798400. This is an abstract local witness, not a rational physical endpoint, not an all-place global nonpole construction, and not an R<=B counting family.


## Verification and adversarial audit


verify_m3_t11_130.py is standard-library exact rational arithmetic and digit-by-digit unique Hensel lifting. It checks200 abstract allocations: p=5,13,17,29, lambda=1..5, every interior c_p, two S units. All coefficient valuations, f(u), root displacement and norm depth match the proof. It checks26 nested AP packets for the local splitting, residual square and failed physical root-line. PASS; physical endpoints enumerated0. Symbolic replay independently verifies f(u) and its Taylor expansion. Finite checks support, but do not replace, the universal proof.


Audit guards: odd p only; no conclusion at2 or content primes; finite-u nondegenerate branch only; lambda>=1; c_p extremes not included; all denominator reductions retained; targeted physical root is the unique unit root, not either pole root; the Gaussian root-line is an original necessary condition, not a newly charged density. Scalar squareclass choices cannot repair an actual root norm valuation. No extra multiplicity/count estimate is inferred.


## Authority consequence and next legal task


M3-T11-106/107 and ROUTE48 interior residual-unit identities remain correct conditional algebra on projected/local packets, but their strict-interior physical occupancy is now empty. Earlier interior character-dispersion attacks are superseded on this physical branch. Do not claim those abstract packets as realized endpoints. M3-T11-120 remains retracted; its quartic-root lock, extreme phi allocation and fourth-power tails are not reinstated.


Next card M3-T11-131: ExtremeAllocationActualAntiRootPhysicalSupport. Analyze c_p=0 and c_p=2lambda using the actual cubic plus the original coordinate-specific root-lines. In the all-extreme branch Q_S and C_u are squares on fresh support and partition M_rel^2. This is a routing identity, not a counting saving. Retain same physical R<=B, one endpoint one count, all content/exceptional branches and common-packet conditions. Seek a same-measure extreme-support theorem; if root-line compatibility is automatic, record that precisely and advance to genuinely joint physical conditions. Projective u=infinity/degenerate cases are not disposed of here.


GLOBAL_COUNTING_CREDIT=0; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false. TI remains parked. Retain123 class-group/n factors,128 real signatures and129 scoped residual pole/local persistence results;130 supplies an additional original physical obstruction, not a whole S4 Selmer collapse.


CURRENT AUTHORITY CONTROL — M3-T11-130 AUDITED / ACTUAL CUBIC EXCLUDES STRICT-INTERIOR FRESH ALLOCATION
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-130
ACTIVE_RESEARCH_CARD_FILE_ID=19WPPyTQ0uXSfUYyCIT05EKD17YNyiVkc
LATEST_RESEARCH_CARD=M3-T11-130
LATEST_AUDITED_RESEARCH_CARD=M3-T11-130
LATEST_AUDIT_FILE_ID=1UOg27VCOCjOOBt3fB746aWaipMx9Eslx
LATEST_VERIFICATION_SCRIPT_FILE_ID=1DmoHOhL97hjL3qJmNDsKJK6U7Fx_awgg
LATEST_VERIFICATION_JSON_FILE_ID=10Pr-rPaMWZhHs4ln4X6VbPUZQH3IPzrc
LATEST_SYMBOLIC_REPLAY_FILE_ID=1MaCyHNfi84hQnZATvh-E6W6V2PeH4Hf3
LATEST_CARD_STATUS=PROVED_EXACT_PHYSICAL_INTERIOR_EXCLUSION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
LATEST_AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
NEXT_RESEARCH_CARD_ID=M3-T11-131
CURRENT_ATTACK=ExtremeAllocationActualAntiRootPhysicalSupport
NEXT_LEGAL_ACTION=Read130 actual cubic proof then ROUTE35-37 and47-48. Analyze extreme c_p=0 or2lambda with actual anti-root Gaussian root-lines, all original packet equations, exact physicalR<=B and oneendpointonecount. Establish same-measure extreme-support tail; no ambient height substitution, no multiplied root-line densities. Projective/degenerate/content branches retained.
INTERIOR_130_PHYSICAL_OCCUPANCY=EMPTY on finite-u nondegenerate branch at every odd split fresh p^lambda||m_i with0<c_p<2lambda.
INTERIOR_130_PROOF=k=2lambda-c_p,n=2lambda+c_p;vp(S)=-k,vp(A)=n. g=p^(4lambda)f has coefficientvaluations(0,0,n,4lambda),linearreductionX-u. Uniqueunitanti-rootV hasvp(V-u)=vp(V²+1)=k<2lambda,contradicting originalphysicalrootline.
INTERIOR_130_SCOPE=Actual cubic rootV, NOTquartic theta orphysicalz identification. Applies independently ofN square/S4/characterselectors; no resultat2/content/extremes/u=infinity.
INTERIOR_130_VERIFICATION=200 abstractallocations and26 nested129AP localimpostors PASS; physicalendpointcount0. Localcubic splits/residualsquare/genus3lift can hold butphysicalnormrootlinefails.
INTERIOR_106_107_48_STATUS=Conditionalalgebraic/residuallocalidentities RETAINED; strictinteriorphysicaloccupancy EMPTY by130. Interiorphysicalcharacterdispersion superseded.
EXTREME_130_ROUTER=All surviving fresh c_p in{0,2lambda};Q_S andC_u squareonfreshsupport,Q_S*C_u=M_rel². Routingonly,no countingcredit; neitherextremetailproved.
S4_129_STATUS=RETAINED explicitS4 squareN family,poleclassc0/xi0 and allplace separate nonpolelocalpersistence. Notphysicalpoints;130 addsmissingoriginalrootlineobstructiononinterior.
S4_128_STATUS=RETAINED exactgammaexclusion4real,two-real scalarquotientfirewall.
S4_123_STATUS=RETAINED beta=Nm-nalpha,gamma=alpha(aN-balpha),xi=beta/gamma; original[Nn beta],Cl(K_u)[2] andactualdenominatorn retained.
THETA_FULL_PHYSICAL_GLOBAL_R_AND_EXACT_HEIGHT_GATE=OPEN_RETAINED
PHI_122_STATUS=JOINT_DENOMINATOR_SUPPORT_RECEIVER_RETIRED
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER; quarticrootlock/extremephiallocations/fourthpowertailsNOTreinstatedby130
BACKWARD_REAUDIT_117_119=PASS_WITH_RETAINED_SCOPE_LIMITS
STARTUP=MAIN/INDEX currentcontrol ->130 card/audit/replay -> activeROUTE/RESULT-LEDGER latest130 -> targeted35-37/47-48 and105/106 fornext131. No fullhistoryreread.
PRIMARY_RECEIVER=P(B)<=B^o(1) A_1,1(B); sufficient A_1,1(B)<<B^(1/3-eta) forfixedeta>0 onexactphysicalmeasure.
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
LOWER_OPERATIONAL_POINTERS=Historical and superseded by this current control; mathematical statements retain their audited scope


STAGE37 INDEPENDENT HOSTILE RE-AUDIT — M3-T11-130 — 2026-10-01
VERDICT=PASS_WITHIN_STATED_SCOPE
AUDIT_KIND=Fresh rederivation from current Drive authority; existing within-session audit was treated only as evidence to check, not as authority for this verdict.
CORE_CHECK=For strict interior 0<c_p<2lambda, k=2lambda-c_p and n=2lambda+c_p satisfy 0<k<2lambda<n. After scaling the actual physical cubic by p^(n+k), its reduction is a nonzero unit multiple of X-u with unit derivative. The unique physical unit anti-root V therefore lies on that Hensel branch. Exact f(u)=u^2*(u*(A-4)/A-S) gives v_p(g(u))=k, hence v_p(V-u)=k. Since p is odd split-fresh, V+u is a unit, so v_p(V^2+1)=k<2lambda, contradicting the original coordinate-specific physical root-line v_p(v_i^2+1)>=2lambda.
FIREWALL_CHECK=No quartic algebra root is identified with physical z=S/2; withdrawn M3-T11-120 is not revived. Local S4/pole/impostor families remain nonphysical. No conclusion at p=2, content primes, projective u=infinity, degenerate branch, or extreme c_p=0,2lambda.
AUTHORITY_CONSEQUENCE=Strict-interior fresh allocation is physically empty on the stated canonical finite-u nondegenerate branch. Conditional projected/local interior identities remain algebraically valid but no longer define an occupied physical branch there.
CREDIT=GLOBAL_COUNTING_CREDIT=0; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false.
CURRENT_POINTER=LATEST_AUDITED_RESEARCH_CARD=M3-T11-130; NEXT_RESEARCH_CARD_ID=M3-T11-131; NEXT_ATTACK=ExtremeAllocationActualAntiRootPhysicalSupport; TI remains parked.
.




M3-T11-131 SAVED AUTHORITY
Card file ID: 1ViXKYPeNIV_YLeSzULQF_wQPotZJdVGB
Audit file ID: 1cRyuP0LeYE50nkoxz6WnLKh6TQGMeOz8
Replay script file ID: 1wpBLDt99IgvE-GcRvGIhoTRpYNHGvAEw
Verification JSON file ID: 1TezWCsZ5fYrbUh6IfFfbmGD40sw9i8cZ
Symbolic replay file ID: 1x07bdWhzepf5DJSsWJuaW8DZGikjeP9L
Next: M3-T11-132 / GaussianExtremeCoupledNonzeroIntegerReceiverSamePhysicalHeight. GateOPEN/globalcredit0/TIparked.
