# M3-T11-158 — Physical two-prime kernel test: interval transfer and large-sieve energy obstruction

STATUS=PROVED_SCOPED_METHOD_OBSTRUCTIONS / COMPLETE_FINITE_KERNEL_REPLAY / PHYSICAL_ASYMPTOTIC_OPEN
AUDIT_MODE=WRITTEN_PROOF_AND_TWO_ENUMERATIONS_NOT_EXTERNAL_HOSTILE_AUDIT
PRIMARY_GATE_STATUS=OPEN
GLOBAL_COUNTING_CREDIT=0
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
DECISION=STOP_AUTOMATIC_LOCAL_CHARACTER_ESCALATION_WITHOUT_NEW_PHYSICAL_INPUT
NEXT_CANDIDATE=M3-T11-159 PhysicalCoefficientSeparationFeasibilityTest on existing T11-026; not a new gate or a claim of a usable theorem

## 1. Current authority and verdict
Fresh native MAIN, INDEX, RESULT-LEDGER, active T11 ROUTE all designate157. The entire157 written card is read from the current ledger. Its exact whole-M3 second-moment implication is retained:

 P(B)/M3(B) <= 1/k + (2/k^2) sum_{p<q in S} W_pq(B)/M3(B).

158 tests the displayed divisor kernel with ALL primitive/canonical/third-face-square/physical-height masks. Two genuine analytic inputs are checked: interval/box character bounds and the quadratic large sieve for arbitrary weighted coefficients. Neither supplies the required relative cancellation using the presently certified inputs. This is a failed theorem match with specific quantified obstructions, not a proof that physical cancellation is impossible.

There is no new global bound and no evidence that only a few research cards remain. Further prime cases, local CRT identities, or higher block enumeration are not the next attack. The existing LOCAL-GATE-001 remains PAUSED pending an actual physical distribution/energy estimate.

## 2. Exact physical terminal measure and naive Abel-transfer obstruction
For primitive Euler bricks E in M3(B), use the unique odd edge X and even edges Y<Z. Put T(E)=X^2+Y^2+Z^2 and L=floor(B^2). Define

 nu_B(n)=#{E in M3(B): T(E)=n}, 1<=n<=L,
 N_B=sum_n nu_B(n)=M3(B),
 W_m(B)=sum_n nu_B(n) chi_m(n), m=pq, p!=q inert.

This equals157's integer divisor kernel because K=4T and chi_m(4)=1. Divisor quotients are evaluated in the integers, including when a prime divides a divisor. No face mask is dropped.

Every T is odd. Indeed primitivity forces exactly one odd edge; two odd edges would give a face square2 mod4. Moreover both even edges are divisible by4: an even edge2 mod4 would make its odd-edge face5 mod8. Thus T=1 mod8. Extend nu_B by0 at n=0 and n=L+1. Every occupied position has zero immediate neighbors, so exactly

 sum_{n=0}^L |nu_B(n+1)-nu_B(n)| = 2 N_B.       (158.1)

This is proved for ALL physical B, not inferred from the census. Let A_m(t)=sum_{n=1}^t chi_m(n). Discrete partial summation gives

 W_m = sum_{n=1}^L A_m(n)[nu_B(n)-nu_B(n+1)],
 |W_m| <= 2N_B max_{t<=L}|A_m(t)|.             (158.2)

For fixed m, periodicity of the nonprincipal chi_m gives a bounded prefix sum, but no factor tending to0 with B. Hence naive total-variation transfer from ordinary interval character bounds does not prove W_m=o(N_B). A stronger bound for unweighted intervals cannot by itself repair the coefficient variation cost. Since max|A_m|>=1 when L>=1, the displayed certificate cannot even become a small relative bound by making its prefix estimate optimally sharp.

Scope: this rejects THIS Abel/total-variation estimate only. Regrouping the1-mod8 support, analyzing weighted sums directly, or exploiting additional physical structure could work with new input; none is disproved. Reindexing only the occupied terminals replaces A_m by character sums on the unknown sparse physical sequence, so it does not inherit an interval theorem.

## 3. A valid quadratic-large-sieve match and the missing energy
Unlike an interval theorem, a quadratic large sieve genuinely accepts arbitrary coefficients. Its correct coefficient cost is squareclass collision energy, not automatically sum_n nu_B(n)^2. Let

 a_d(B)=#{E in M3(B): squarefree_part(T(E))=d},
 E_sq(B)=sum_{d squarefree} a_d(B)^2
        =sum_{n1*n2=square} nu_B(n1) nu_B(n2).

Both definitions are identical by the unique factorization n=d*r^2. In particular a_1=P(B), E_sq>=P(B)^2 and E_sq>=N_B. Different terminal values can lie in the same squareclass; distinct T values do not justify dropping those collisions.

External primary input: Zihao Liu, Explicit quadratic large sieve inequality, arXiv2505.09637v2, Introduction(2) and Section5.1(37), which prove/state the arbitrary-coefficient form of Heath-Brown's quadratic large sieve:

 sum_{primitive quadratic chi, conductor<=Q} |sum_{n<=L} c_n chi(n)|^2
 <<_epsilon (QL)^epsilon (Q+L) sum_{n1*n2=square}|c_n1*c_n2|.     (158.3)

We use the conventional epsilon form, not a parsed iterated-log explicit constant. On the exact physical coefficients c_n=nu_B(n), and fixed inert primes p<=Z, the pair character chi_p chi_q is primitive quadratic of conductor pq<=Z^2. Thus for h=k(k-1)/2 pairs,

 sum_{p<q}|W_pq|^2 <<_epsilon (Z^2 L)^epsilon (Z^2+L) E_sq,
 sum_{p<q}|W_pq| <= sqrt(h) [C_epsilon (Z^2 L)^epsilon (Z^2+L) E_sq]^(1/2).

Combining with157 is valid, with all physical masks retained:

 P/N_B <= 1/k + (2sqrt(h)/k^2)
          [C_epsilon (Z^2 L)^epsilon (Z^2+L) E_sq]^(1/2)/N_B.     (158.4)

For the intended fixed S before B-limit, L~B^2; this certificate has a B*sqrt(E_sq)/N_B cost. It does not shrink using current information. One elementary upper bound suffices to see the budget failure: each odd X<=B has at most tau(X^2)^2 divisor pairs before masks, so N_B<=B^(1+o(1)). Together with E_sq>=N_B, the B*sqrt(E_sq)/N_B part is at least B^(1/2-o(1)). This is an obstruction in the numerical upper-bound certificate, not a lower bound on the actual character sum.

Allowing Z to grow can remove the B/Z loss, but not the unknown energy. Even in an optimistic prime budget k of order Z/log Z and Z>=B, the energy cost is of order B^o(1)*log Z*sqrt(E_sq)/N_B. No theorem presently bounds that ratio appropriately. The universally safe E_sq<=N_B^2 leaves a nonvanishing/vacuous error. Proving E_sq=o(N_B^2) would itself already imply P/N_B->0 through a_1=P. Therefore invoking large sieve without a new physical energy estimate just relocates the hard problem. This is not authorization to rename E_sq as a new independent completed weapon; terminal energy is not declared equivalent to the existing TQ receiver.

## 4. Why removing the third-face mask is not a theorem match
Bryce Kerr, Some mixed character sums, arXiv1410.3587v1, Theorems1-2 concern interval sums with polynomial additive phases; Theorems3-5 concern boxes. They do not state a bound for157's moving-divisor set with an exact third-face-square mask. A comparison is therefore a failed range/coefficient match, not a numerical application of the theorem.

More explicitly, if an ambient population has size A, physical subpopulation size N, theta=N/A, and |f|<=1, then

 sum_physical f = theta sum_ambient f + sum_ambient (1_physical-theta)f,
 |second term| <= sqrt(N(A-N)).                         (158.5)

The inequality follows from Cauchy and sum(1_physical-theta)^2=N(1-theta). Its relative cost can be sqrt(A/N-1); an ambient cancellation bound alone supplies no saving after sparse conditioning. This is a general calculation, not a claim of any actual physical lower correlation. In particular no Selberg/CRT half-density factor is multiplied by the old endpoint upper bound.

## 5. Complete finite physical replay, with two face enumerations
verify158.cpp enumerates ALL positive primitive Euler bricks with sqrt(T)<=10^6, canonical X odd,Y<Z, in two ways:
(A) factor every odd X<=B, generate a|X^2,a<X and Y=(X^2/a-a)/2, retain X^2+Y^2<=B^2; pair the Y values and apply primitive, third-face-square and T<=B^2 masks;
(B) generate all primitive Pythagorean odd/even faces (m^2-n^2,2mn,m^2+n^2), gcd(m,n)=1 and opposite parity, use all odd scales k with k(m^2+n^2)<=B, group by odd X, then use the same final exact brick predicate.
Completeness follows from the divisor difference-of-squares dictionary for(A), and the primitive Pythagorean parametrization after removing gcd for(B). Each face has one positive even partner; Y<Z and unique odd X give one count. The two full sorted brick lists coincide. The final brick predicate is also replayed in Python with integer square roots and recovery of both divisor partners.

All intermediate Y values are bounded by B BEFORE y*y is evaluated in64-bit arithmetic. An initial missing guard was corrected, the incomplete run discarded, and only the corrected complete dual-enumeration output is used. Maximum retained squared quantities are <=3*(10^6)^2, safely within signed64-bit. This is within-session validation, not external independent auditing.

Fixed diagnostic S={7,19,23,31,43,47,59,67,71,79,83,103};3 and11 are excluded from thinning as157 requires.

| B, exact sqrt(T) cutoff | M3 | E_sq | max a_d | selected-prime all-pass |157 second-moment bound|
|---|---:|---:|---:|---:|---|
|1000|5|5|1|0|3/20|
|10000|18|18|1|0|47/324|
|100000|60|60|1|0|211/2160|
|1000000|219|219|1|0|761/7884|

The physical cutoff is the Euclidean space diagonal sqrt(T), not maximum edge; do not compare these counts to a max-edge census without an adapter. All219 terminal squareclasses are distinct in THIS range. This does not prove injectivity, bounded squareclass multiplicity, decay of E_sq/N^2 at infinite height, or the absence of perfect cuboids globally. The selected12-prime all-pass count0 is a finite census exclusion only. The second-moment bound near0.0965 at the last cutoff is not a predicted limiting constant. All single/pair character sums and exact fractions are in verify158-result.json.

## 6. Decision, next concrete candidate, and retained state
158 is completed as a concrete failed analytic match and a verified physical kernel test. The global two-prime correlations remain OPEN. Stop automatic local-character/prime-block escalation. Reopen only with a genuine same-M3 weighted character/energy estimate, not more finite primes, interval estimates without weights, or a replacement of physical masks by a uniform residue model.

As the next separate candidate, use155 portfolio's existing third reserve, particularly T11-026's physical coefficient separation problem. Next159 should inspect the ACTUAL W_M coefficient with its common-parent/primitive/height masks and try one exact theorem-compatible bilinear/trilinear decomposition, with coefficient energy and endogenous squared-modulus ranges retained. Before detailed work, state the full content/family budget: a fixed-content B^(1/12-delta) result alone is not global closure. No new gate is created and analytic applicability is not presumed. If no separation or new same-measure input appears, preserve the blockage instead of issuing more Fourier/Gauss algebra cards. This recommendation is based on the existing155 ordering, not evidence of high success probability.

Retain152/153 sector results, unresolved E_bal,155 witness equivalence,156 uniform raw-tail obstruction and its restricted-threshold firewall,157 zero-free certificate. TI parked;120 retracted;147-149 local curve structure retained; automatic degree ladder paused. PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; GLOBAL_FIXED_POWER_SAVING=false.

## Primary references and replay
- [Liu primary preprint v2](https://arxiv.org/html/2505.09637v2) — Introduction(2),(10), Section5.1(37). Arbitrary-coefficient energy matters. This is a preprint theorem input, not asserted peer-review certification.
- [Kerr primary preprint v1](https://arxiv.org/html/1410.3587v1) — Theorems1-5, interval/box range comparison only. No claim that this exhausts every weighted character theorem in the literature.
- Drive authority157, scoped ledger024/026, and155 portfolio audit file1lN_OijU_GBmtGicloRJcr_hLMFsgBBGn were freshly read. Known history was not reread in full.
- Replay: g++ -O3 -std=c++17 verify158.cpp -o verify158; ./verify158 1000000; python verify158.py. C++17 and Python standard library only. Save the exact219-row census, both source files and JSON with this card. No finite output is promoted to an infinite-height theorem.
