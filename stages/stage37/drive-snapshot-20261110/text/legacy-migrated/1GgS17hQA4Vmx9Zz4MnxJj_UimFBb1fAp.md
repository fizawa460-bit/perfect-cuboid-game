# M3-T11-151 — Integer-wide dominant-prime exclusion and quantitative marginal-support barrier

STATUS=ALL_ENDPOINT_NECESSARY_CONDITION_PROVED_MARGINAL_COUNTING_BRIDGE_REJECTED
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
CURRENT_ATTACK=JointGaussianSupportCorrelationUnderExactR
NEXT=M3-T11-152 JointGaussianSupportCorrelationUnderExactR

## Authority and population

Fresh MAIN / INDEX / RESULT-LEDGER / active T11 ROUTE and research-card150 are the authority.150 stopped degree-by-degree curve escalation. This card works directly with every original primitive physical integer endpoint, including points outside the rational curves studied in147–149. No carrier assignment, parameter degree, genus restriction, or polynomial-root-pair interpretation of an integer R is used.

Write positive edges e1,e2,e3, complementary face diagonals f1,f2,f3, and the integer space diagonal R, with gcd(e1,e2,e3)=1, ei^2+fi^2=R^2 and sum ei^2=R^2. Exact cutoff is R<=B. Canonical endpoint masks remain in force; enlarging to these equations is safe only for an upper bound. Retained138/141 ensure R odd and the edge/R contents are pairwise coprime. Every prime dividing R is 1 modulo4: an inert prime dividing ei^2+fi^2 forces it to divide every ei, contradicting primitivity. This elementary argument is included here as a dependency, not claimed as historical novelty.

## 1. Global arithmetic theorem

For EACH prime power p^n exactly dividing R, put m=R/p^n. Then every such endpoint satisfies

 p <= 3 m^2.                                             (151.1)

There are stronger branch conditions. Let r be the number of edges not divisible by p. Then r is2 or3. If r=2, p<=2m^2. If r=3, p^n<=3m^2. In particular, a primitive positive endpoint cannot have R equal to a power of a single prime. This is a theorem about actual integer endpoints, uniform in height and in all possible geometric complexity; it is not an application of149's curve-polynomial theorem.

Proof in Z[i]. Choose p=pi*bar(pi), Norm(pi)=p. Independently conjugate Hi=ei+i fi so v_pi(Hi)<=v_bar(pi)(Hi); this changes only the sign of fi. Norm(Hi)=R^2. For an edge not divisible by p, v_pi(Hi)=0 and v_bar(pi)(Hi)=2n, hence
 Hi=bar(pi)^(2n) Gi,  Gi in Z[i], Norm(Gi)=m^2.
At least two edges are not divisible by p: if two edges are divisible by p, sum ei^2=R^2 forces the third to be divisible by p as well. Let I be the set of these r edges and C=sum_(i in I) Gi^2.

The exact sphere identity is
 sum Hi^2 + sum bar(Hi)^2 + 2R^2 = 0.                    (151.2)
All terms outside bar(pi)^(4n) C are divisible by pi^2. Indeed, a remaining edge divisible by p has both Gaussian valuations at least1; the conjugates of the I-terms have valuation4n; and R^2 has valuation2n. Thus pi^2 divides C. If r=3, there is no remaining edge, and the conjugate terms have valuation4n while 2R^2 has valuation exactly2n. Consequently v_pi(C)=2n.

C is nonzero. For r=3, C=0 would make both entire sums of squares in(151.2) zero, contradicting R>0. For r=2, C=0 gives H1^2+H2^2=0 and its conjugate;(151.2) then reduces to4e3^2=0, contradicting positivity. Finally |Gi^2|=m^2, so Norm(C)<=r^2 m^4. A nonzero Gaussian integer divisible by pi^2 has norm at least p^2; in the r=3 case it has norm at least p^(2n). These yield the stated inequalities. Units are absorbed into Gi; no complex phase cancellation is assumed absent.

Thus all original endpoints lie in the explicit diagonal support
 S(B)={odd R<=B: all p|R are1 mod4, and p<=3(R/p^v_p(R))^2 for every p|R}.
The excluded diagonal part has EXACTLY ZERO physical endpoints; all remaining endpoint mass is on S(B). This is an exact global support reduction, not a curve/residual covering conjecture. It supplies no bound on the mass remaining there.

## 2. Quantitative test: this marginal condition cannot itself reach the certified scale

Do not embark on an unlimited sequence of additional scalar prime tests without testing their surviving support. The set S(B) already has

 #S(B) >> B^(2/3)/log B.                                (151.3)

Explicit proof. For every prime q=1 mod4, q>5, choose the least k>=0 with 3*5^(2k)>=q and set R(q)=5^k q. Both prime divisors are split. For p=q the support condition holds by construction; for p=5 it holds because 5<=3q^2. Moreover this family even passes the stronger inequalities p^n<=3m^2 at BOTH prime divisors: q<=3*5^(2k), and 5^k<5 sqrt(q/3)<=3q^2. Minimality gives R(q)<(5/sqrt(3))*q^(3/2). Distinct q give distinct R(q). Taking q<=((sqrt(3)/5)B)^(2/3) and applying the prime number theorem in progression1 modulo4 proves(151.3).

External theorem used only for this obstruction's quantitative size: NIST DLMF section27.11, final paragraph, https://dlmf.nist.gov/27.11 (accessed in this session), states pi(x;k,h)~x/(phi(k)log x) for coprime h,k. The construction and its support inequalities are derived here. These R(q) are NOT asserted to support physical cuboids. They are counterexamples to deducing an o(B^(1/3)) DIAGONAL-CANDIDATE bound from(151.1), even if the stronger branch inequalities are imposed without joint edge data.

Therefore the dominant-prime sieve is useful as a zero-mass exclusion, but is FAIL as a standalone route to the sufficient o(B^(1/3)) endpoint scale. This does not prove that o(M3(B)) is impossible, nor rule out combining this condition with other correlated constraints. It rules out assigning global-counting credit to this condition alone.

## 3. Exact remaining joint receiver and counting costs

Let H(R)={H in Z[i]: Norm(H)=R^2}. For split R, unique factorization gives
 #H(R)=4 product_(p^n||R)(2n+1).
Each signed triple H1,H2,H3 with real parts e1,e2,e3 satisfies the sphere condition exactly when(151.2) holds. For each R define J(R) to count such triples with nonzero real and imaginary parts, primitive real parts, and the original physical/canonical masks retained or explicitly enlarged. Choose a deterministic positive sign convention and edge order for an injection from canonical physical endpoints into the triples; discarded masks only enlarge J. Then
 P(B) <= sum_(R in S(B)) J(R).
There is no uncounted geometric residual: every physical endpoint has its three complementary face diagonals and hence a triple. No packet constants or curve-family costs have been hidden. The crude bound J(R)<=#H(R)^3=R^o(1) only gives B^(1+o(1)); it has NO global exponent credit.

The load-bearing task is the averaged EXACT joint identity(151.2), not the separate marginal divisibilities pi^2|C, the number of allowable R, or a fixed-R representation bound. The same Hi must work at every prime and satisfy the archimedean equality; treating local choices as independent would discard the essential correlation. Content/prime orientation choices depend on the edge, and must be charged in any enlarged count.

## 4. Decision, scope and restart

151 proves an all-endpoint arithmetic exclusion and proves quantitatively that its scalar support relaxation is too large for the certified sufficient scale. It does NOT meet150's acceptance criterion for aggregate exponent improvement. GLOBAL_COUNTING_CREDIT remains0; the gate remainsOPEN. The theorem is a valid uniform link from the original population to explicit arithmetic support, with zero excluded mass, but should not be marketed as closure progress in the endpoint sum.

Next152: attempt a uniform averaged bound for the correlated Gaussian triple identity above, including the growing prime-factor/valuation allocation cost under exactR. A claimed improvement must bound the complete sum or a specified part AND its complement. First dedupe against the existing Gaussian/root-packet and charged cofactor routes; do not rename their fixed-block estimates. If no summed saving follows, record that obstruction promptly rather than enumerating degrees or local prime-factor cases.147–149 remain retained and curve escalation remains paused. TI parked;120 retracted.

Verification: audit151 gives the complete valuation and support-budget proof. verify151.py / verification151.json replay Gaussian divisibility/norm inequalities on explicit finite domains and the relaxed-support construction. The mathematical proof above, not a finite search for absent cuboids, certifies the theorem. No general perfect-cuboid nonexistence or novelty relative to all literature is claimed.
