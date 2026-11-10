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
