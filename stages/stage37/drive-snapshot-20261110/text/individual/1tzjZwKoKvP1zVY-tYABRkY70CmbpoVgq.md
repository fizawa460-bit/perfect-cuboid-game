# M3-T11-162 — Summed near-equal primitive-face sector by Pell orbits

CARD_ID: M3-T11-162
CANONICAL_CARD_KEY: M3-T11-162
STATUS: PROVED_ENDPOINT_SECTOR_USING_RETAINED_UNIFORM_010 / COMPLEMENT_OPEN
GLOBAL_OPERATION: ACTIVE_T11_RESEARCH_WITH_SCOPED_DECOMPOSITION
PRIMARY_GATE: M3-T11-GATE-001, OPEN
GLOBAL_COUNTING_CREDIT: 0
AUDIT_MODE: WITHIN_SESSION_NOT_INDEPENDENT

## Current decision and sources

The user explicitly permits resuming the original research and decomposing promising parts. This supersedes the earlier operational HOLD and its ban on further sector work. It does not change any mathematical gate or prove a global result. TI remains parked;120 remains retracted;147–149 remain frozen.

Current MAIN, CARD-INDEX, latest161 and active ROUTE were read. Index search covered near-equal legs, differences, Pell, fixed affine families and small-coordinate sectors. Relevant010,144,160 were fetched from Drive.144 is an unsigned affine plus-coordinate count with a moving-coefficient cost; it does not already sum this primitive missing-face angular sector. This card uses fixed quadratic field arithmetic to pay the entire moving difference-family sum. No literature-wide novelty is claimed.

- [Retained010: uniform full physical ratio multiplicity](https://drive.google.com/file/d/1bdxngwOnQmLDzYMRimqFxuWlAI_34REi/view?usp=drivesdk).
- [Retained160: physical first-cover coverage and exact R](https://drive.google.com/file/d/10O7d3ogxEVWW03Iz-sqE6vVYhV3pz2pu/view?usp=drivesdk).
- [Retained161: summed short primitive hypotenuse sector](https://drive.google.com/file/d/1wpu0RydOmsCJH76I5dy9ZNM3t6LVamWg/view?usp=drivesdk).
- [144: distinct affine/Pell coefficient receiver](https://drive.google.com/file/d/1G3tcyK6IdOOy31oiJYUq7SweglUA1m_U/view?usp=drivesdk).
- [Active ROUTE](https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit),14.1.
- [R. Prasad, Investigating GCD in Z[sqrt(2)]](https://math.mit.edu/research/highschool/primes/materials/2013/Prasad.pdf), section3: norm-Euclidean background only. The count and physical transfer below are proved here.

## 1. The geometric statistic and exact physical population

For a principal first-cover state at exact R<=B, reduce its missing-face legs by g=gcd(C,X):
c0=C/g, x0=X/g, p0=sqrt(c0^2+x0^2)<=B.

Define the integer primitive leg difference
d=|c0-x0|=|C-X|/gcd(C,X).

On class1 the primitive Pythagorean legs have opposite parity, so d is positive and odd. Equality is impossible. This is an ABSOLUTE difference after reducing content, not the physical difference |C-X| and not a relative angular width.

Let r_near(B;D) count original H_F states with class1 and d<=D. All physical parents, lifts, contents and original masks remain. Let P_near(B;D) count original primitive canonical endpoints for which at least one of the three reduced face pairs has d_ij<=D. Use 1<=D<=B.

## 2. Uniform arithmetic direction count, including all large hypotenuses

Order the primitive legs c<x and put u=c+x, d=x-c and p=sqrt(c^2+x^2). Then
u^2-2p^2=-d^2, u,d odd, gcd(u,d)=1,
c=(u-d)/2, x=(u+d)/2.
In particular gcd(u,p)=1: a common prime would divide d, contradicting gcd(u,d)=1.

Work in O=Z[sqrt(2)] and alpha=u+p sqrt(2). Its norm is -d^2. The following elementary facts give a uniform count.

(a) O is norm-Euclidean: for a quotient a+b sqrt(2), round a,b to integers. For the error s+t sqrt(2), |s|,|t|<=1/2, hence |s^2-2t^2|<=1/2<1. Multiplicativity of the absolute norm gives Euclidean division. Thus O is a PID and a UFD.

(b) For every odd prime ell|d, an inert ell would divide both u and p, which is impossible. A split ell has two conjugate prime ideals. Both cannot divide (alpha), because then ell divides alpha as an element, again forcing ell|u,p. Consequently, if ell^e||d, the ideal (alpha) contains exactly one of the two conjugate primes, with exponent2e. The ramified prime2 is absent since d is odd. Thus there are at most 2^omega(d) possible ideals (alpha), independent of B. Some choices may have no generator of the required signs, so this is an upper bound.

(c) Two generators with norm -d^2 of the same ideal differ by a norm +1 unit. Positive norm +1 units are epsilon^k, k in Z, with epsilon=3+2sqrt(2). To see completeness directly, epsilon is the smallest unit >1 of norm +1: writing such a unit a+b sqrt(2)>1 gives positive integer a,b, a^2-2b^2=1; b=1 is impossible and b>=2 gives a+b sqrt(2)>=epsilon. Divide any larger unit by a suitable epsilon power into [1,epsilon); the same minimality forces it to be1. Negative units cannot connect the positive alpha values counted here.

(d) alpha>d because u>0 and Norm(alpha)<0. Also u<=sqrt(2)p and p<=B give alpha<=2sqrt(2)B<3B. Along one unit orbit, alpha increases by epsilon each step. Hence at most
1+floor(log(3B/d)/log(epsilon))
values can occur. Positivity of c and primitivity only remove values.

Let A(B,D) be the number of ORDERED primitive positive Pythagorean directions with p<=B and |c-x|<=D. Both leg orders cost a factor2. Therefore

A(B,D) <= 2 sum_(odd d<=D) 2^omega(d) [1+floor(log(3B/d)/log(epsilon))]
         << D(1+log D)(1+log B).

The last step is fully summed: 2^omega(d)=sum_(k|d) mu(k)^2, so
sum_(d<=D)2^omega(d)<=D sum_(k<=D)1/k<=D(1+log D).
No fixed-d constant, unknown class number, moving field, conductor, content or direction-family cost is hidden.

## 3. Transfer to the original physical measure

Each ordered primitive direction supplies exactly one reduced ratio rho=C/X. Retained010 gives, for every eta>0, a single K_eta with
m_rho(B)<=K_eta B^eta
uniformly over all physical ratios, already including contents/lifts.

Thus
r_near(B;D)<=K_eta B^eta A(B,D)
            <<_eta D B^eta(1+log D)(1+log B)
            = D B^o(1).

For a canonical endpoint with some d_ij<=D, choose a face attaining the minimum d_ij, breaking ties in canonical face order. With its complementary edge as the shared edge,160 supplies a principal physical first-cover state. The parent is retained, so the deterministic charging is injective at parent level, with only the retained fixed chart constant.

Therefore
P_near(B;D)<=O(r_near(B;D))<=D B^o(1).

For every fixed 0<delta<1/3, choose D=floor(B^(1/3-delta)). Taking eta<delta and absorbing the logarithms, retained M3(B)>>B^(1/3) gives

P_near(B;D)/M3(B) -> 0.

This is a proved, all-family/all-content endpoint SECTOR bound dependent on retained010. It is not a proof for the complementary endpoints.

## 4. What is additional to161, and the exact residual

161 discards endpoints with some primitive face hypotenuse p_ij<=T.162 discards endpoints with some primitive face difference d_ij<=D, even when the hypotenuse is much larger than T.

These direction families are not the same: d=1 supports the unbounded positive primitive sequence (3,4,5),(20,21,29),(119,120,169),... obtained by the epsilon recurrence. This proves geometric non-containment at the arithmetic-direction level; it does NOT prove that any of these directions is occupied by a full physical endpoint. No physical endpoint examples are asserted.

For disjoint bookkeeping, first charge161's short set, then162's near-equal set restricted to p_min>T. The latter is bounded by P_near. The remaining original endpoints satisfy simultaneously
all three p_ij>T AND all three d_ij>D.
Thus
P(B)<=P_short(B;T)+P_near(B;D)+P_far_long(B;T,D).
At T=D=B^(1/3-delta), the first two terms are o(M3); the last remains OPEN.

This is a genuinely different angular sector with a proved uniform family budget, not another smaller hypotenuse cutoff. It still does not establish sparsity of all principal directions, bound the total principal count below B^(1/3), or solve E_bal. No multiplication of independent face/Pell densities is used.

Restricted near principal energy is <=D^2 B^o. The mixed near/complement energy is only bounded from retained inputs by D B^(1/2+o), which need not meet the B^(2/3) goal. Direct endpoint discard avoids requiring that mixed-energy cleanup.

## 5. Verification and audit limits

verify162.py checks two exact direction enumerations (Euclid and integer circles) at p<=1500:239 unordered primitive directions match.
At p<=50000,7960 directions pass the norm equation, primitive reduction and exact backward/forward epsilon recurrence.
For every odd d<=300, complete reduced-seed enumeration gives77 primitive seeds and verifies the 2^omega(d) orbit envelope.
Four complete Euclid/Pell-orbit comparisons give20/47/104/273 unordered directions for (B,D)=(1500,25),(5000,50),(50000,100),(50000,300), all matching.
956 scaled-content checks preserve both primitive d and p.
Physical endpoints enumerated=0. Finite data verify arithmetic adapters, not the asymptotic theorem or uniform010. Audit is within-session, not independent external.

## 6. Handoff

LATEST_RESEARCH_CARD=M3-T11-162
NEXT_CANDIDATE=M3-T11-163
CURRENT_ATTACK=PrincipalFarLongFaceSupportOrPhysicalDirectionIncidence

Continue research with scoped decomposition permitted by the user. Prefer an actual physical mechanism for the far-long residual, a uniform/averaged admissible-direction estimate, or a genuinely summable extension of the geometric sector lemma. Any new sector must pay all moving parameters/content and state its contribution and complement. An arbitrary smaller cutoff, fixed fiber or renamed residual is not credited as a global result. The separate A001 analytic receiver remains available; no claim that it is exhausted.

NEW_ENDPOINT_SECTOR_BOUND=true
NEW_GLOBAL_ENDPOINT_BOUND=false
PRINCIPAL_CLASS_GLOBALLY_CONTROLLED=false
P_OVER_M3_LIMIT_PROVED=false
GLOBAL_COUNTING_CREDIT=0
TI=PARKED
120=RETRACTED
147–149=FROZEN

## Drive artifacts

- [M3-T11-162-proof-review.md](https://drive.google.com/file/d/10dp3R7cPsixp69FrxPS8mwwe4I8UiPjQ/view?usp=drivesdk)
- [M3-T11-162-verify.py](https://drive.google.com/file/d/1rU8b74r76zwePWDicb2I3Enb6h3Yt0zP/view?usp=drivesdk)
- [M3-T11-162-verification.json](https://drive.google.com/file/d/13vysOkRc8g1B-Y-SnrehBFEO0nD38h2e/view?usp=drivesdk)

