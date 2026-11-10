M3-T11-112 — Psi fixed-conductor primitive lattice counting adapter
STATUS=PROVISIONAL / EXACT_SAME_MEASURE_UPPER_BOUND / HOSTILE_AUDIT_REQUIRED / NO_FIXED_POWER_SAVING
TYPE=QUANTITATIVE_ADAPTER / PRIMITIVE_PARAMETER_COUNT / MOVING_MODULUS_FIREWALL
POPULATION=Exact nondegenerate physical Stage37 endpoints with R<=B in one fixed content/coefficient packet, restricted to psi/A4. One physical endpoint is one count.
DEPENDENCIES=111 HOSTILE_AUDIT_PASS; 109 exact degree-two psi parametrization; 040/041/043 capped common-u conductor; 036 HOSTILE_AUDIT_PASS uniform fixed-u physical multiplicity.
DUPLICATE_SEARCH=Compared RESULT-LEDGER, NEGATIVE-REGISTER, ROUTE and CARD-INDEX. Existing 029/030 fixed root-line occupancy and 046 primitive lattices are related engines; they do not give this psi depth pullback plus uniform primitive fixed-conductor bound. No prior saving or retired density route is reopened.
ALIASES=PsiA4PrimitiveFixedConductorCount; PsiDepthRootLineLatticeUpperBound.

STATEMENT.
Let M=M_rel, C=C_u with 0<=v_p(C)<=2v_p(M), and L=M^2 C. Fix M,C (hence L), and restrict physical points to those having at least one primitive psi parameter [r:s] with max(|r|,|s|)<=H, H>=1. Denote their number E_psi(B;M,C,H). Then
E_psi(B;M,C,H) << B^o(1) 4^omega(M) (H^2/L+1).
On the polynomial physical range, equivalently
E_psi(B;M,C,H) << B^o(1) (H^2/(M^2 C)+1).
The B^o(1) factor is the previously audited fixed-u physical multiplicity, not new multiplicity credit.
For a fixed oriented rho modulo L and one choice of the two psi root lines at every p, the primitive parameter count is O(H^2/L+1), with an absolute constant independent of lattice shape.

PROOF.
(i) Audited 111 gives p=1 mod12 at every p|M. Choose the existing common-u Gaussian root rho modulo L. At extreme c_p=2lambda, L uses only the capped depth 4lambda, which is valid even if the actual norm valuation is larger. No unjustified exact saturation is needed.
(ii) At each p^n||L the binary quadratic N-5rho Q0 has exactly two simple projective root lines. A line is the kernel of a primitive covector modulo p^n, including the infinity chart. Selecting one at every p and using CRT gives a primitive covector modulo L. Its kernel in Z^2 is a rank-two lattice Lambda of determinant exactly L: the covector map Z^2 -> Z/L is surjective.
(iii) Primitive lattice lemma. Choose a Gauss-reduced integral basis b1,b2 of Lambda, with |b1|<=|b2| and angle between 60 and 120 degrees. Then |b1||b2| is comparable to det(Lambda)=L. If v=m b1+n b2 has sup norm <=H, elementary inversion gives |m|<=K H/|b1| and |n|<=K H/|b2| for an absolute K. A Z^2-primitive v must have gcd(m,n)=1, since a common divisor divides both integer coordinates of v. For n=0 only m=+/-1 can survive. For n!=0, if such a vector occurs then both H/|b1| and H/|b2| are bounded below by an absolute positive constant. Thus the number is O((H/|b1|)(H/|b2|))=O(H^2/L). Adding the n=0 contribution proves O(H^2/L+1). This is a deterministic upper bound, including highly anisotropic lattices; there is no H/lambda1 error term.
(iv) There are at most 2^omega(M) Gaussian orientations and 2^omega(M) pullback line choices, hence at most 4^omega(M) lattices. Sum their upper bounds. Counting signed primitive pairs overcounts projective parameters by only a bounded factor.
(v) Every counted physical endpoint has a parameter in this set. Each parameter determines exactly one u=psi(r/s); apply audited 036 to bound physical multiplicity for each realized u by B^o(1). Extra endpoint equations and exact R<=B restrictions are monotone post-filters. No ambient density is substituted for the physical population.

HEIGHT AND MOVING-CONDUCTOR CONSEQUENCE.
H is a stated parameter-height cutoff, not an asserted power of B. The exact psi height relation is h(u)=2h(t)+O(1) for logarithmic heights, but no new sharp physical B-exponent is proved here.
For finitely many fixed conductor pairs (M,C) in a shell, with a common valid cutoff H, the rigorous union upper bound is
B^o(1) sum_(M,C) (H^2/(M^2 C)+1).
Duplicates only enlarge this upper bound.
To bound active realized u-values below B^(1/12-delta), it is sufficient to establish that this actual physical-shell sum is O(B^(1/12-delta)), or to replace the separate-modulus sum by a sharper joint incidence bound. Such an estimate is NOT proved.
The +1 term records the thin-lattice / large-modulus occupancy obstruction: when L>H^2, this method gives O(B^o(1)) per conductor pair rather than a reciprocal-L gain that can be summed freely. No physical lower-bound or actual endpoint existence is asserted by this observation.

IMPLIES=The psi fixed-conductor counting adapter is quantitative, but moving-conductor occupancy and a sharp physical height relation remain the blockers.
DO_NOT_REPEAT=Do not multiply p=1 mod12 density, two-line density, common-u root-line charge or determinant probabilities. The displayed estimate replaces a count; it is not an independent factor in a previously obtained numerator bound. Do not delete +1, assume independence, or turn ambient psi height into a physical B-exponent.
REOPEN_CONDITION=Audit rejects the primitive lattice lemma, CRT determinant L, bounded line multiplicity, fixed-u pushforward, or an audited dependency changes. A new result may improve joint moving-(M,C,H) occupancy or prove a sharp physical height adapter.
CREDIT=Zero fixed-power saving; zero new multiplicity credit; primary gate and endpoint ratio remain open.
NEXT_LEGAL_ACTION=Hostile-audit 112; then attack joint moving-conductor occupancy/physical height, or the audited phi global-root allocation, genuinely nonlocal S4 route, or independent theta!=0 route.
NEXT_RESEARCH_CARD_ID=M3-T11-113
FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

AUDIT ADDENDUM
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / NO_GLOBAL_POWER_SAVING
AUDIT_DOC_ID_112=1w5zvca-ctnZ2HqNtphuMdUteUFfdM7jG
The original provisional proof has passed audit; original status is retained above as history.
NEXT_LEGAL_ACTION=Proceed to provisional M3-T11-113 joint norm-squareclass tail; audit 113 before promotion.
