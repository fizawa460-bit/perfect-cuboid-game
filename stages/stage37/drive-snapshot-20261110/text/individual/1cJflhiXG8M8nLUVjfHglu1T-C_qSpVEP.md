# M3-T11-221 — off-value squareclass collision feasibility test

Status: PROVED_SHORT_MULTIPLIER_BOUND / NO_GO_DIVISOR_ONLY_RELAXATION / ACTUAL_LONG_LONG_ENERGY_OPEN / GLOBAL_CREDIT=0.
Authority: Stage37 MAIN / operational CARD-INDEX / short RESULT-LEDGER; latest mathematical predecessor220, direction ROUTE-SEARCH-220-R1. Independent proof audit186–221 NOT RUN; audit162–185 scope retained. This is a within-session mathematical derivation and finite replay, not a separate audit.

## 1. Population and intended question

Use the actual endpoint-inclusive canonical raw population X*(B,C) of212/214/215, with positive primitive edges, integral space diagonal R<=B, at least two integral face diagonals, the inherited canonical eligible pair, c_chart>C=B^gamma, pairwise-distinct edges and M_2R mask. Keep all content, height, local branch restrictions and the kappa=1 endpoint class. The chart content c_chart is not intrinsic c_u. For the shared edge a of the selected pair, M=R²−a²=b²+c² satisfies 0<M<=B². Write uniquely M=kappa y², kappa positive squarefree, y positive integer.

Let nu(m)=#{x in X*:M(x)=m}, N=|X*| and D=max_m nu(m). Empty population gives all energies zero.215 gives N<=B^(1/2+o(1)), D<=B^o(1), uniformly after all inherited raw costs. Let mu(kappa)=sum_y nu(kappa y²), E_equal=sum_m nu(m)², E_sq=sum_kappa mu(kappa)², E_off=E_sq−E_equal. These are ordered pair energies; E_off requires unequal M values.

Target at gamma=1/6: an independently proved actual E_off<=B^(2/3−eta+o(1)), 0<eta<1/6, would via215 give X* endpoint tail<=B^(1/3−eta/2+o(1)). This target remains unproved. It addresses X* only, not other residual receivers.

## 2. Proven short-multiplier bound

For real Y>=1 set s_kappa(Y)=sum_{1<=y<=Y} nu(kappa y²). The fixed-value bound gives s_kappa<=floor(Y)D. Count E_off,short(Y), the ordered unequal-value same-squareclass pairs with min(y1,y2)<=Y. Every such pair has at least one short member, hence

E_off,short(Y) <= 2 sum_kappa s_kappa(Y) mu(kappa) <= 2 floor(Y) D N.

No masks, endpoints or moving classes are removed; summing mu=N pays all outer classes once. Thus E_off,short<=Y B^(1/2+o(1)). For general gamma, Y<=B^(1/2−2gamma−eta) reaches the required B^(1−2gamma−eta+o(1)) energy sector. At gamma=1/6 take Y=B^(1/6−eta). The remaining off-value pairs have both multipliers larger than Y and kappa<B²/Y² (strict when both y>Y).

There is no new endpoint saving: in class kappa=1 the short condition is the small missing-diagonal sector already handled by215. The total energy target cannot follow from this partial estimate.

## 3. Proven high-squarefree-kernel bound and overlap

For real K>=1, M<=B² and kappa>=K imply y<=B/sqrt(K). Therefore mu(kappa)<=D floor(B/sqrt(K)), and

sum_{kappa>=K} mu(kappa)² <= D floor(B/sqrt(K)) N <= B^(3/2+o(1))/sqrt(K).

The formula includes equal-value pairs. At gamma=1/6, K>=B^(5/3+2eta) gives the desired sector energy exponent2/3−eta. This is contained in the preceding short-multiplier sector with Y=B/sqrt(K); the two estimates cannot be multiplied or credited as independent gains. For K>1 it excludes the endpoint class kappa=1 and supplies no endpoint bound. Low-kappa long-long pairs, including kappa=1, remain OPEN.

## 4. Exact pair adapter — no fresh count credit

For a same-class unequal-value pair, write y1=g r, y2=g s, gcd(r,s)=1. Then L=gcd(M1,M2)=kappa g² and M1=L r², M2=L s². With H=max(r,s), L<=B²/H². This is an exact height constraint, not a density theorem: all L,r,s support/range sums and the two simultaneous raw realizations still need to be paid. This adapter alone does not bound actual E_off.

## 5. Formal countermodel and method-level NO_GO

The following is a coefficient model, NOT an actual raw cuboid family. Let T>=16 be an integer, B=T², N=T, y_j=B/2+j for0<=j<T (choose even T for integer B/2), and assign nu(2y_j²)=1, nu=0 elsewhere. The N values are distinct, positive, <=B² and all have squarefree class2; D=1, N=B^1/2, E_equal=N, E_off=N(N−1)~B. Their multipliers are at least B/2, outside every short sector B^(1/6−eta). They obey the short/high-kernel inequalities above but violate any uniform target B^(2/3−eta+o(1)).

Consequently N<=B^(1/2+o), uniform fixed-value D<=B^o, host range M<=B² and these divisor-only sectors do not logically imply the energy target. Decision: NO_GO_DIVISOR_ONLY_RELAXATION. It does not refute the desired estimate on actual X*, does not supply a physical counterfamily, and says nothing about existence of a perfect cuboid. A new proof must retain an additional compatibility restriction from the actual two-face/sphere realization. Rephrasing this coefficient model as a physical obstruction is prohibited.

## 6. Exact finite diagnostics

Both exhaustive integer generators at R<=4,000,000 returned the same473 sorted primitive raw edge triples. One enumerates Pythagorean leg pairs through factors of a²; the other uses scaled primitive Euclid triples. Both test positive edges, primitivity and exact integral R, then deduplicate unordered edge triples. For any object with at least two integral faces, their shared edge occurs in the outer loop, so it is covered. Both generators permit equal edges and three-face endpoints rather than dropping them. The finite verifier finds exactly two integral faces in every returned record; its assertion is a reported finite result, not an asymptotic restriction or an endpoint-safe replacement of212.

Each generator visited17,610,396 directed leg pairs and340,534,605 sphere pair trials. The R<=1,000,000 key subset matches all255 old208 records, with the old input SHA checked. For the finite two-face records the canonical pair is unique, so M=R²−a_shared² and c_chart=gcd(R,e_i)gcd(R,e_j) are unambiguous.

| population | N | distinct M | distinct sf(M) | E_equal | E_off |
|---|---:|---:|---:|---:|---:|
| all primitive raw records, R<=4,000,000 |473|473|473|473|0|
| X*, gamma=1/6, same bound |43|43|43|43|0|

The verifier uses exact integer factoring and local unit tests at2 and every prime dividing R for both coprime A−,A+ branches. It checks distinct edges, c_chart^6>B, all sphere/two-face equations, pair-gcd formulas and explicit finite D versions of both inequalities. Other gamma and height-window counts are in the JSON. Zero off-value collisions here neither proves a uniform energy theorem nor disproves the actual route. It is evidence for keeping a conditional physical-compatibility search open, not grounds for automatic GO. The formal model tests T=16,32,64,128 all pass their stated conditions.

## 7. Reproduction and durable inputs

Download the following files into one working directory `batch221`. Compile each C++ source with g++ -O3 -std=c++17, run from that directory with argument4000000, then run Python3 verifier. Standard-library-only verifier; no SymPy dependency. Its source input path is ROOT.parent/attachments/098192f5-df13-43ac-93a2-55f349dbac19/M3-T11-208-verification.json; create that directory or adjust SOURCE to the downloaded208 JSON. Generator default is1,000,000, so pass4000000 explicitly. Memory-intensive Euclid adjacency needs a normal research runtime. The JSON stores SHA256 of all five replay files and the old input.

- [raw divisor generator](https://drive.google.com/file/d/1Xio9hs-qxtdpP2t5lTvSniCLy-tXTwfc/view)
- [independent Euclid generator](https://drive.google.com/file/d/1gjvdwkOKl0R9hl84N34j6qHG1dn5Uh4b/view)
- [exact Python verifier](https://drive.google.com/file/d/1l1QAVU1w6XEj9uXSHlQlvDbyW5qRieQ5/view)
- [473-record census](https://drive.google.com/file/d/1yg_JdjMHuUtBt-9Hn3akUwPYNN-EzyBl/view)
- [independent key set](https://drive.google.com/file/d/17kZeo3E3_yvEdzY738Son1a0UI5rHN52/view)
- [verification JSON and hashes](https://drive.google.com/file/d/1egR6CmJNL65NLRXOBVKFGmU4uCcj3vUX/view)
- [208 input JSON](https://drive.google.com/file/d/1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG/view)
- [215 fixed-value and energy theorem](https://docs.google.com/document/d/1VaPpB1NJkRXuFYAgkhtYBiD7BqOnGS7on9IUpkjBBxg/edit)
- [route-search220R1](https://drive.google.com/file/d/1-bwpwiooMOr1lZ8aaOwcOxFSXj0IBVsn/view)

## 8. Handoff / next222 preflight

Mathematical latest221; strategy search220R1 retained, selected feasibility test now completed with scoped bounds and method-level NO_GO.219/220 automatic identity extension remains HOLD. Do not automatically start a generic large-sieve/moving-squareclass chain from this card.

Next222 is MECHANISM_SELECTION_PREFLIGHT: first look for a genuinely additional simultaneous two-face/sphere compatibility constraint on low-kappa long-long actual pairs, or a legitimate actual raw counterfamily. Before GO state what inequality changes the N,D-only relaxation, pay all outer L,r,s/content/height/mask costs and retain kappa=1. If no such input is found, keep actual E_off OPEN and record method HOLD; compare the separate218 mixed-occupancy/other existing receivers only if a distinct quantified mechanism is available. No candidate is certified promising merely because it has a new identity. X* outside/K>1/large-c_u/large-W/unshared conductor receivers remain separately OPEN. TI parked,120 retracted,147–149 frozen. No new global saving, Gate OPEN, credit0.
