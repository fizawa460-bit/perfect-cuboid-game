# M3-T11-152 — Weighted prime-support summation, growing-sector saving and uniform unit-equation finiteness

CARD_ID: M3-T11-152
CANONICAL_CARD_KEY: M3-T11-152
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-152
現行一覧の状態: PROVED_WEIGHTED_SUPPORT_SUM_AND_UNIFORM_ALPHABET_FINITE_BOUND / SECTOR_COUNTING_PROGRESS=true / GLOBAL_COUNTING_CREDIT=0
種別: WEIGHTED PRIME-SUPPORT SUM / GROWING-SECTOR SAVING
要点: 指定split-prime alphabet S上のphysical endpoint総数を一様に平均計数。polylog alphabet sectorでo(M3)。
主張の抜粋: P_S(B)<=64 B^sigma∏_{p∈S}F(p^-sigma), F=(1+23x+23x^2+x^3)/(1-x)^4。|S_B|<=(log B)^AならP_S<=B^(1-1/A+o(1)); A=4/3でB^(1/4+o(1))=o(M3)。
対象・測度: 全primitive canonical positive physical endpoints、exact R<=B。ただしsectorはsupp(R)⊂指定S_B。補集合E_outは保持。
依存関係: 151 exact Gaussian triple receiver;138 odd/exact height。unit-equation nondegeneracyとRankin weighted sum。
再開条件の抜粋: 153で全moving primeの小余因子部分を総和しo(M3)を証明。次154はS_B外かつ全pで余因子が大きいbalanced residualを評価。152のsector定理は保持。
旧詳細位置: RESULT-LEDGER152; audit 15w2bqTRn-24EFR24RMX7RP8ICPFoGzu_
旧詳細リンク: https://drive.google.com/file/d/1msa8WnZZ7je4kql-sG9LWO455HV32mKV/view
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 99944
SOURCE_END: 104241
SOURCE_SHA256: 666b537e8deeffe13e23a56529c649ba9efc7e3d96edfaec73448044b75b6cf1

CURRENT AUTHORITY CONTROL — M3-T11-152 / WEIGHTED PRIME-SUPPORT SUMMATION AND GROWING-SECTOR SAVING
PRIMARY_GATE=M3-T11-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE
ACTIVE_ROUTE_DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE
ACTIVE_RESEARCH_CARD=M3-T11-152
ACTIVE_RESEARCH_CARD_FILE_ID=1msa8WnZZ7je4kql-sG9LWO455HV32mKV
LATEST_RESEARCH_CARD=M3-T11-152
LATEST_AUDITED_RESEARCH_CARD=M3-T11-152
LATEST_AUDIT_FILE_ID=15w2bqTRn-24EFR24RMX7RP8ICPFoGzu_
LATEST_AUDIT_MODE=WITHIN_SESSION_PROOF_REDERIVATION_AND_EXACT_REPLAY_NOT_EXTERNAL
LATEST_CARD_STATUS=PROVED_WEIGHTED_SUPPORT_SUM_AND_UNIFORM_ALPHABET_FINITE_BOUND / SECTOR_COUNTING_PROGRESS=true / GLOBAL_COUNTING_CREDIT0
NEXT_RESEARCH_CARD_ID=M3-T11-153
CURRENT_ATTACK=LargePrimeResidualOrSummableSupportCover
PRIMARY_CURVE_CLASSIFICATION=STOPPED_AS_MAIN_ATTACK_PENDING_GLOBAL_BRIDGE
DEGREE6_PHASE_SYSTEM_STATUS=OPEN_BUT_NOT_DEFAULT_ATTACK
PHYSICAL_152_RECEIVER=All original endpoints remain inside151 exact Gaussian triple receiver. For one specified finite split-prime alphabet S, P_S(B) counts original primitive canonical positive physical endpoints with exact R<=B and supp(R) subset S.
PHYSICAL_152_NONDEGENERACY=For zi=Hi^2/R^2, every physical tuple satisfies z1+z1^-1+z2+z2^-1+z3+z3^-1=-2 with no nonempty vanishing subsum. Positivity/nonzero-edge and odd primitive R are essential.
PHYSICAL_152_UNIT_EQUATION=Norm-one phase group over S has rank |S|; three phases give rank3|S|. Published multiplicative-group equation bound gives height-independent P_S(infinity)<=C0*K^|S|. This is retained as uniform finiteness, not the main sector exponent.
PHYSICAL_152_WEIGHTED_SUM=For R=prod p^n, ordered Gaussian triples <=64 prod(2n+1)^3. Rankin summation gives P_S(B)<=64 B^sigma prod_{p in S} F(p^-sigma), F(x)=(1+23x+23x^2+x^3)/(1-x)^4, with exponent/unit/allocation costs included.
PHYSICAL_152_SECTOR=Uniformly for any one specified alphabet |S_B|<=(log B)^A, A>1, P_{S_B}(B)<=B^(1-1/A+o(1)). For A=4/3 this is B^(1/4+o(1))=o(M3(B)) using retained M3(B)>>B^(1/3).
PHYSICAL_152_PARTITION=Choose S_B as first floor((log B)^(4/3)) split primes. Then E(B)=E_small disjointunion E_out, P_small=o(M3). Full target is equivalent to proving P_out=o(M3). E_out consists of endpoints with at least one prime divisor of R outside S_B; NO residual estimate yet.
PHYSICAL_152_COVER=For a family F_B of specified alphabets, P_covered<=sum_{S in F_B} min(C0*K^|S|,inf_sigma W_S). If #F_B<=B^alpha and |S|<=(log B)^A, exponent alpha+1-1/A+o(1); at A=4/3 any alpha<1/12 suffices for covered part. Complement must still be bounded.
PHYSICAL_152_VERDICT=First proved aggregate o(M3) sector on the current all-endpoint Gaussian route, but not a whole-population bound. GLOBAL_COUNTING_CREDIT remains0 because E_out is unresolved.
NEXT_LEGAL_ACTION=153 must bound E_out under exact R<=B, or construct a support-alphabet cover with summable total cost and bound its complement. Do not spend the next card on one more fixed alphabet, prime-factor count, curve degree, or huge-constant optimization without changing the global residual sum.
GLOBAL_TARGET=P(B)/M3(B)->0
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
TI_RESEARCH_STATUS=PARKED_BY_EXPLICIT_USER_REQUEST / RESULTS_RETAINED
TI_RESUME_POLICY=Do not automatically resume TI during ordinary stage37mainbatch.
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
VERIFICATION_ARTIFACT_STATUS=NOT_CONFIRMED_BY_CURRENT_DRIVE_SEARCH; standalone152 card/audit reference verify152.py and verification152.json, but their separate Drive files were not located. Do not invent IDs or claim byte-exact replay persistence.
ARTIFACT_READBACK=152 standalone research-card and audit fetched from Drive and content checked before authority promotion.
STARTUP=MAIN/INDEX current152 -> standalone152 card/audit -> ROUTE/LEDGER152 ->153 residual target. Historical dependencies only as needed; no full-history reread.
LOWER_OPERATIONAL_POINTERS=151 and below historical/superseded operationally; mathematics retained within audited scopes.


PRIOR AUTHORITY MATERIAL — HISTORICAL OPERATIONAL POINTERS BELOW; MATHEMATICS RETAINED WITHIN ITS AUDITED SCOPE.

## Retained standalone source — M3-T11-152-research-card.md
SOURCE_FILE_ID: 1msa8WnZZ7je4kql-sG9LWO455HV32mKV
SOURCE_URL: https://drive.google.com/file/d/1msa8WnZZ7je4kql-sG9LWO455HV32mKV/view?usp=drivesdk

# M3-T11-152 — Weighted prime-support summation, growing-sector saving and uniform unit-equation finiteness

STATUS=PROVED_WEIGHTED_SUPPORT_SUM_AND_UNIFORM_ALPHABET_FINITE_BOUND
AUDIT_MODE=WITHIN_SESSION_PROOF_REDERIVATION_AND_EXACT_REPLAY_NOT_EXTERNAL
SECTOR_COUNTING_PROGRESS=true
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-153 LargePrimeResidualOrSummableSupportCover

## Authority and what is counted

Fresh MAIN / INDEX / RESULT-LEDGER / active T11 ROUTE and complete research-card151 remain the starting authority.150 paused automatic curve-degree escalation;151 supplies the integer-wide Gaussian sphere identity but no aggregate saving. Here P_S(B) counts ORIGINAL primitive canonical positive physical endpoints with exact R<=B and every prime dividing R belonging to ONE specified finite set S. All content/coefficient/cyclic/parity masks are retained; enlarging the set of solutions is only an upper-bound operation. Signed complementary face diagonals are allowed with the retained canonical convention. One endpoint is one count; supports are not counted as endpoints.

No restriction on curve degree, genus, rational parameterization, exponent v_p(R), or coefficient packet is imposed. By138 and151, R is odd and its prime factors split in Z[i]. We may therefore take S to consist of primes1 modulo4. The contribution outside this support restriction is explicitly retained below.

## 1. The missing uniform link: no vanishing subsum

Put H_i=e_i+i f_i and z_i=H_i^2/R^2 for i=1,2,3. Then |z_i|=1, conjugation is inversion, and151's exact identity becomes

 z1+z1^(-1)+z2+z2^(-1)+z3+z3^(-1)=-2.                 (152.1)

Every physical tuple is NONDEGENERATE as a six-variable linear equation: no nonempty subsum of the six terms vanishes. This is not assumed from genericity.

Proof. The real numerator of each term with common denominator R^2 is e_i^2-f_i^2, which is odd since R is odd and the circle pair has opposite parity. A subsum with an odd number of terms has odd real numerator and cannot vanish. A two-term zero involving the same i would imply e_i^2=f_i^2, hence R^2=2e_i^2, impossible for nonzero integers. A two-term zero involving different i,j has real part2(e_i^2+e_j^2-R^2)/R^2; its vanishing and the sphere equation force the remaining edge to be zero. For four terms summing to zero, the two complementary terms sum to-2 by(152.1). Two unit complex numbers sum to-2 only when both equal-1. But z_i=-1 implies e_i=0, again forbidden. All six terms sum to-2, not0. These cases exhaust all63 nonempty subsets.

Positivity/nonzero-edge and primitive odd-R hypotheses are essential to this argument. Degenerate zero-edge boundary families do have vanishing subsums and are NOT included in the count.

## 2. A height-independent bound for one entire prime alphabet

For each p in S choose p=pi_p*bar(pi_p). Let G_S be the norm-one subgroup of Q(i)^* supported at these Gaussian primes. Unique factorization gives

 G_S=mu_4 * <pi_p/bar(pi_p):p in S>,   rank G_S=|S|.

The valuation vectors at distinct Gaussian primes are independent. Each z_i belongs to G_S because Norm(H_i)=R^2. The group

 Gamma_S={(u1,u1^(-1),u2,u2^(-1),u3,u3^(-1)):u_i in G_S}

has rank3|S|, not6|S|. Apply the quantitative nondegenerate multiplicative-group equation theorem with n=6, coefficients all-1/2, and this group. The verified Amoroso–Viada bound yields

 P_S(B) <= 48^[5184(7+3|S|)] = C0*K^|S|,              (152.2)
 C0=48^36288,  K=48^15552,  kappa=log K.

This is uniform in the actual primes, their sizes, all exponents and B. In fact it bounds P_S(infinity). There is no additional multiplication by the number of exponent allocations or by the2^|S| subsets: the group count already contains them all.

Injection check: z_i determines H_i/R up to sign; its positive real part selects exactly one square root. This recovers the ordered normalized edges and the signed face diagonals. Positive primitive integer edge triples on one rational ray are unique, so R and the entire canonical endpoint are recovered. Thus no height-dependent inverse multiplicity is hidden. Enlarging to the multiplicative-group solutions can introduce nonphysical tuples, which only increases the upper bound.

External theorem, precise source: Amoroso and Viada, “On the zeros of linear recurrence sequences”, Acta Arithmetica147.4, pp.387–396, DOI10.4064/aa147-4-4. In the proof of Lemma2.1 on p.389, the authors explicitly state their six-variable-applicable bound (8n)^[4n^4(n+r+1)] for nondegenerate solutions in a group of rank r, citing their earlier Theorem6.2. Primary publisher PDF: [Amoroso–Viada, p.389](https://www.impan.pl/shop/en/publication/transaction/download/product/83761). The formula and hypotheses were checked in extracted text AND the rendered page. The application, nondegeneracy lemma and physical injection above are derived here. As a weaker independently checked fallback, Evertse–Schlickewei–Schmidt Theorem1.1 gives exp((6n)^(3n)(r+1)); [ESS primary paper](https://arxiv.org/pdf/math/0409604), pp.807–808. No claim of literature-wide novelty is made.

## 3. Stronger aggregate bound by direct weighted summation

An internal comparison corrected the initial research emphasis: using(152.2) with |S_B|<=logB/(4kappa) gives C0 B^(1/4), but that growing-sector conclusion is DOMINATED by the following elementary bound. It must not be presented as a counting gain that requires the deep unit-equation theorem. The uniform all-height finiteness(152.2) is retained as a separate result. Its constants are enormous: kappa about60204.918 and log C0 about140478.142.

For each split R,151 gives #H(R)=4 product_(p^n||R)(2n+1), so the complete ordered Gaussian-triple count is at most64 product(2n+1)^3. This includes every original endpoint. We now SUM those exponent-allocation costs rather than replacing each fixed-R count by a name. For any sigma>0, Rankin's elementary inequality1_(R<=B)<=B^sigma/R^sigma gives

 P_S(B) <= W_S(B,sigma)
 :=64 B^sigma product_(p in S) F(p^(-sigma)),           (152.3)
 F(x)=sum_(n>=0)(2n+1)^3 x^n
     =(1+23x+23x^2+x^3)/(1-x)^4.

The finite Euler product sums EVERY exponent vector, including zero exponents, all three Gaussian representation allocations and all units. It imposes no independence probability and drops the joint sphere equation only in the safe upper-bound direction. No uncounted packet multiplicity remains. The displayed generating-function identity follows by applying (2x d/dx+1)^3 to1/(1-x).

Uniform in the actual prime values, write s=|S| and order them p_j>=j+1. For0<sigma<1 fixed away from0 and1, log F(p^(-sigma))<=C_sigma p^(-sigma), since log F(x)/x is bounded on0<=x<=2^(-sigma). Hence

 log product F(p^(-sigma)) <= C'_sigma s^(1-sigma).

Let A>1 be fixed and let S_B be ANY one specified alphabet with |S_B|<=(logB)^A. Taking sigma=1-1/A+epsilon gives an exponent1-1/A+epsilon+o(1). Equivalently, choose epsilon=(loglogB)^(-1/2) for large B; the constants stay bounded and s^(1-sigma)<=logB*exp(-A sqrt(loglogB))=o(logB). Therefore

 P_(S_B)(B) <= B^(1-1/A+o(1)), uniformly in S_B.       (152.4)

In particular, A=4/3 gives P_(S_B)(B)<=B^(1/4+o(1))=o(M3(B)) under the retained M3(B)>>B^(1/3). More generally every fixed1<A<3/2 yields a negligible sector. This is the main aggregate sector estimate of152. It allows a larger alphabet than the unit-equation corollary and has no gigantic unit-equation constant. The main sector proof is self-contained elementary counting; it does not depend on the external theorem.

For a concrete exhaustion choose S_B as the first floor((logB)^(4/3)) split primes. Exact remaining partition: E(B)=E_small(B) disjoint-union E_out(B), where E_small has all prime divisors ofR in S_B and E_out has at least one outside. P_small=o(M3) is proved; the full target is now equivalent to P_out=o(M3). NO residual estimate is proved. Eventual coverage of each fixed R is not uniform coverage of moving endpoint mass.

## 4. Summable-cover version and the remaining cost

For any explicitly specified family F_B of finite split-prime alphabets, a union bound gives

 P_covered(B) <= sum_(S in F_B) min(C0*K^|S|, inf_(sigma>0) W_S(B,sigma)). (152.5)

Overlaps are safe in this upper bound; use the first alphabet in a fixed ordering if an exact partition is needed. All sub-supports of one alphabet are already counted. Do not sum its2^s subsets again. For #F_B<=B^alpha and every |S|<=(logB)^A, (152.4) gives
 P_covered(B)<=B^(alpha+1-1/A+o(1)).
Thus alpha+1-1/A<1/3 is sufficient for this covered part. At A=4/3, any alpha<1/12 suffices. Full closure still requires the complementary residual bound. The alternative unit-equation budget C0 sum K^|S| can be better in particular sparse finite-support regimes; take the minimum of replacement counts, never multiply their savings.

Do NOT replace “one specified S” by “at most s prime factors anywhere” without paying for all supports. Arbitrary moving primes produce a family cost, which neither theorem removes. The exact scalar majorant W_S is allowed for an upper bound; unlike151's marginal necessary-condition set, its support-size restriction has a proved summed cost. No claim that physical endpoints satisfy this restriction automatically is made.

## 5. Dedupe, credit and next task

Targeted current-ledger searches found no Rankin/smooth-number support-alphabet count or Evertse/Schlickewei/Amoroso/Viada finite-rank equation adapter. Existing M3-COMMON-001 and M3-XD-001 give Gaussian root packets / physical congruence images with a separate globalization gate. HIST14-GAUSS-FW-001 forbids double charging orientations.118/119 give scoped phi/conductor counts, not this unrestricted-alphabet endpoint count.047/048 are a fixed singular-carrier S={2,3,5} descent. Bare Gaussian phases/Fricke identities are older; they are NOT claimed new.152 adds an explicit weighted exponent sum and uniform growing-support budget, alongside a separate no-subsum degeneration and all-height arithmetic-group count. Standard Rankin and unit-equation theory are not claimed new mathematics.

SECTOR_COUNTING_PROGRESS=true. The whole population still has GLOBAL_COUNTING_CREDIT=0, GLOBAL_FIXED_POWER_SAVING=false, PRIMARY_GATE_CLOSED=false, P_OVER_M3_LIMIT_PROVED=false. TI remains parked;120 retracted;147–149 retained and curve escalation paused. The external theorem is published; this application has within-session proof audit, not external independent hostile review.

Next153: work on E_out(B), or construct a support-alphabet cover with an actually summable cost in(152.5) and bound its complement.151's dominant-prime bound may help constrain that residual, but scalar prime tests by themselves remain too large. Do not continue by classifying one more degree, one more prime-factor count, or optimizing the huge universal constant unless that changes a proved global sum. The objective is a residual mass bound, not a larger catalog of alphabets. Do not spend another card rediscovering that polylog-sized alphabets have sparse smooth-number support.

Replay: verify152.py classifies all63 subsum masks, checks exact boundary counterexamples and group embedding rank, verifies the generating-function coefficients and weighted Euler-product majorants on finite supports, and checks exponent budgets. It supplements the written proofs; it is not an unsuccessful finite search used as nonexistence evidence. Proof/audit/replay and current pointers are saved in Stage37 so a new chat can resume from153 using Drive alone.
