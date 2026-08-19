# StructureRadar literature ledger — search batch 19

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-19-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-179,SR-STR-180,SR-STR-181,SR-STR-182,SR-STR-183,SR-STR-184,SR-STR-185,SR-STR-186,SR-STR-187,SR-STR-188
SEARCH_BATCH_SIZE=10
NOVELTY_BY_SEARCH_ABSENCE=false

## Primary-source literature checked
- D. R. Heath-Brown and J.-L. Colliot-Thélène, *The density of rational points in curves and surfaces*, Annals of Mathematics 155 (2002), 553–598; arXiv:math/0405392. It gives degree-uniform bounded-height rational-point upper bounds for projective curves. This is adjacent to SR-STR-180, but the repo good-cell theorem also uses its exact moving quartic, smaller-diagonal slope injection, physical height and separate multiplicity adapter.
- Olivier Robert and Gérald Tenenbaum, *Sur la répartition du noyau d’un entier*, Indagationes Mathematicae 24 (2013), 802–914, DOI 10.1016/j.indag.2013.07.007. It gives uniform asymptotics/estimates for N(x,y)=#{n<=x:k(n)<=y}, directly supporting the small-squarefree-kernel sparsity input behind SR-STR-182, not the full Stage14 physical-cell count.
- D. R. Heath-Brown, *The square sieve and consecutive square-free numbers*, Mathematische Annalen 266 (1984), 251–259, DOI 10.1007/BF01475576. This is the direct square-sieve method carrier behind SR-STR-186; the exact quartic, inert-prime trace cancellation, H^(4/5) optimization and physical packet summation remain repo-specific.
- Lei Fu, *Twisted Exponential Sums*, arXiv:math/0607164. Under Newton-polyhedron nondegeneracy it controls weights/dimensions of the relevant torus cohomology and estimates multiplicatively twisted additive sums. This is a direct general carrier for the Newton-polyhedron side of SR-STR-188 after the repo face-by-face nondegeneracy check.
- Nicholas M. Katz and Gérard Laumon, *Transformation de Fourier et majoration de sommes exponentielles*, Publications Mathématiques de l’IHÉS 62 (1985), 145–202, DOI 10.1007/BF02698808. Fourier-transform/stationary-phase machinery is a direct general carrier for the second route in SR-STR-188, while the exact H polynomial and diagonal/axis receivers remain repo-specific.
- Fisher–Sills/Fisher explicit covering-descent literature checked in batch18 remains adjacent context for SR-STR-183/185; it does not replace the repo exact eight-state Q2 image or edge-routed overlap support.

## Search outcome
- SR-STR-179: retain the elementary CRT projective-line/lattice cover as repo exact. External quadratic-congruence literature is unnecessary for the exact index-q and 2^omega(q) accounting.
- SR-STR-180: Heath-Brown supplies a uniform fixed-degree curve-counting framework, but not the complete moving-diagonal-pair physical-height/multiplicity adapter; keep the repo theorem as the exact receiver.
- SR-STR-181: primitive shared-edge gluing and compact conjugate-gap identities are coordinate adapters only; no population theorem is inferred.
- SR-STR-182: Robert–Tenenbaum directly supports small squarefree-kernel counting. The Stage14 supported base/class sparsity and polynomial witness boxing remain a composed repo adapter.
- SR-STR-183: exact eight-state Q2 Kummer image remains repo-specific local descent; generic descent sources do not imply global solubility or moving-family equidistribution.
- SR-STR-184/185: injective third-face transfer and pairwise gcd support are retained as exact elementary/reduction statements; necessity is not promoted to sufficiency.
- SR-STR-186: Heath-Brown square sieve is the method carrier. The fixed quartic trace cancellation and balanced/thin packet dispatch remain repo exact and cannot be transplanted without the original physical measure.
- SR-STR-187: ordered fixed-prime same-measure sieve remains an elementary qualitative-zero-density adapter; the limit order does not yield a fixed-power saving.
- SR-STR-188: Lei Fu and Katz–Laumon supply the two general finite-field engines. The archived O(p) result still depends on repo verification of Newton nondegeneracy and separate diagonal/axis receivers.

## SR-STR-179 — Full-radical squarefree CRT projective-line incidence cover
For odd squarefree q and unit A,B, A x^2=B y^2 mod q is empty if a local ratio is nonsquare; otherwise it is covered by 2^omega(q) CRT projective lines x=r y mod q, each a rank-two lattice of index q. The full odd radicals R_S,R_X,R_H are exact witness congruence moduli even when selected kernels are proper divisors.
Potential weapon types: CRT, LATTICE_COVER, LOCAL_OBSTRUCTION.
Applicability gaps: q must be odd squarefree with unit coefficients.; Both line multiplicity and lattice index must be retained.
Transfer verdict: `REPO_EXACT_CRT_LATTICE_COVER` — preserve full radical modulus, line multiplicity and index-q lattice accounting.
Arsenal decision: `ACTIVE`.

## SR-STR-180 — Moving diagonal-pair genus-one quartic with smaller-diagonal enumeration
Fixing a core and one diagonal pair puts the opposite reduced slope t on a smooth even quartic W^2=F0((b0d0)^2-(a0c0)^2t^4), with an injective primitive-diagonal-to-slope map. Smaller-diagonal enumeration plus a separate B^o(1) bounded-height multiplicity theorem gives the good-cell bound; genus one alone does not.
Potential weapon types: GENUS_ONE, HEIGHT_COUNTING.
Applicability gaps: The exponent is receiver-specific.; A uniform bounded-height input is essential.
Transfer verdict: `ADJACENT_UNIFORM_CURVE_COUNT_WITH_PHYSICAL_ADAPTER_GATE` — uniform fixed-degree curve counting is external, but the moving quartic height/multiplicity theorem remains repo-specific.
Arsenal decision: `ACTIVE`.

## SR-STR-181 — Primitive physical two-face gluing and compact conjugate-gap chart
For oriented primitive Pythagorean faces with S1=g*alpha and S2=g*beta, minimal shared-edge gluing is e=g*alpha*beta=lcm(S1,S2), x=beta*X1, y=alpha*X2; a common scale t equals gcd(e,x,y), so primitivity forces t=1. With t1=X1/S1, t2=X2/S2 and L=lcm(S1,S2), (e,x,y)=L(1,t1,t2) and the ambient real height is D_R=L*sqrt(1+t1^2+t2^2), without any rational or integral space-diagonal condition. On the physical space-diagonal branch, G^2=H^2*S2^2+S^2*X2^2=S^2*H2^2+X^2*S2^2 gives an induced integral triple, while compact conjugates satisfy N_phys*N_-=S^2*X^2*(R_-)^2 and Z_-=-U*V/X2^2. These are exact coordinate adapters, not population estimates.
Potential weapon types: COORDINATE_ADAPTER, PYTHAGOREAN_GLUING.
Applicability gaps: No count or independence follows.; The primitive gcd scale must be retained.
Transfer verdict: `REPO_EXACT_COORDINATE_ADAPTER` — gluing and compact conjugate identities create no count or independence.
Arsenal decision: `ACTIVE`.

## SR-STR-182 — Radical-poor hypotenuse support sparsity and polynomial witness box
In the recorded Stage14 receiver, hypotenuse support radical at most B^rho gives a B^(rho+epsilon)-sparse supported base/class family. Separately, a logarithmic canonical-height witness has denominators and integral factors in a fixed polynomial box, so finite-dimensional dyadic subdivision costs B^epsilon. Neither statement alone counts rational points.
Potential weapon types: SPARSE_FAMILY, HEIGHT_ADAPTER.
Applicability gaps: rho is tied to the recorded population.; Polynomial boxing is not a point-count theorem.
Transfer verdict: `DIRECT_SMALL_KERNEL_INPUT_WITH_REPO_CELL_ADAPTER` — Robert–Tenenbaum carries the small-kernel counting input; Stage14 population transfer remains separate.
Arsenal decision: `ACTIVE`.

## SR-STR-183 — Exact eight-state Q2 Kummer covering image
For the normalized local triple [q],[q-1],[q+t^2] with v2(t)>=2, exactly eight of the 64 product-square states occur: (1,1,1),(3,7,5),(5,1,5),(7,7,1),(2,1,2),(6,7,10),(10,1,10),(14,7,2), using representatives 1,3,5,7,2,6,10,14 in Q2*/Q2*^2.
Potential weapon types: LOCAL_DESCENT, Q2_KUMMER_IMAGE.
Applicability gaps: Membership is local necessity, not global solubility.; The eight states are not equidistributed in a moving physical family.
Transfer verdict: `REPO_EXACT_Q2_KUMMER_IMAGE` — eight local states are necessary conditions only and are not assigned moving-family frequencies.
Arsenal decision: `ACTIVE`.

## SR-STR-184 — Injective primitive third-face transfer from a physical two-face edge
Given physical F1=(S,X,H), F2=(S2,X2,H2), g=gcd(S,S2), G=gd and c=gcd(H,X2), the primitive reduction F3=(HS2/(gc), SX2/(gc), d/c) is Pythagorean and H3<=d. The physical edge is recoverable from (F2,F3), so the map is injective. Every image satisfies (S3X2)^2-(X3S2)^2 being a nonzero square, only a necessary condition.
Potential weapon types: INJECTIVE_TRANSFER, PYTHAGOREAN_REDUCTION.
Applicability gaps: The cross gcd c is mandatory.; The displayed square condition is not sufficient for arbitrary primitive-face pairs.
Transfer verdict: `REPO_EXACT_INJECTIVE_TRANSFER` — the cross-gcd reduction is retained and the displayed square condition remains necessary-only.
Arsenal decision: `ACTIVE`.

## SR-STR-185 — Pairwise gcd support of integral witness factors
For G0=A, G1=A-S^2D^2, G2=A+X^2D^2 with gcd(A,D)=1, every prime dividing D is coprime to all Gi and gcd(G0,G1)|S^2, gcd(G0,G2)|X^2, gcd(G1,G2)|H^2. Thus odd overlap supports 01,02,12 lie on the disjoint primitive Pythagorean edges S,X,H.
Potential weapon types: GCD_SUPPORT, SQUAREFREE_KERNEL.
Applicability gaps: This precedes and does not replace the full signed-kernel factorization.; Overlap primes cannot be moved between edges.
Transfer verdict: `REPO_EXACT_GCD_SUPPORT` — overlap primes stay on their primitive Pythagorean edge supports and do not replace signed-kernel descent.
Arsenal decision: `ACTIVE`.

## SR-STR-186 — Balanced inert-prime quartic square-sieve dispatch
For the fixed quartic F(P,Q)=PQ(Q-P)(Q+P), inert primes p=3 mod 4 have exact complete trace cancellation. On a product-square packet with square-part box volume M=XYZW and H=min(X,Y,Z,W), the proved square-sieve inequality is optimized at auxiliary prime scale L=H^(4/5), giving N_packet << M H^(-4/5) B^o(1). Thin packets switch to the exact shared-squareclass four-cell decomposition rather than being discarded.
Potential weapon types: SQUARE_SIEVE, CHARACTER_CANCELLATION.
Applicability gaps: The fixed quartic and product-square packet normalization must be retained.; Thin packets require the shared-squareclass four-cell switch; they are not automatically sparse.; A packet saving must still be summed in the original physical measure.
Transfer verdict: `DIRECT_SQUARE_SIEVE_METHOD_WITH_PACKET_FIREWALL` — Heath-Brown supplies the sieve engine; exact trace cancellation and physical packet dispatch stay repo-specific.
Arsenal decision: `ACTIVE`.

## SR-STR-187 — Same-measure fixed-prime ordered-limit squareclass sieve
For Q(B) subset P(B) with identical physical measure and, for each fixed finite good-prime set S, a CRT-refined asymptotic plus necessary local acceptance rho_p, limsup Q(B)/P(B)<=prod_{p in S}rho_p. Only after B->infinity may S expand; if the ordered products tend to zero, Q(B)/P(B)->0. This proves qualitative zero density, not a fixed-power saving.
Potential weapon types: LOCAL_SIEVE, ZERO_DENSITY, ORDERED_LIMIT.
Applicability gaps: The Stage15 rho_p cannot be transplanted to another population.; Growing modulus with B requires a separate uniform theorem.; No fixed-power saving follows from the ordered limit.
Transfer verdict: `REPO_ORDERED_LIMIT_ZERO_DENSITY_ADAPTER` — fixed-prime products prove qualitative zero density only after B-to-infinity first.
Arsenal decision: `ACTIVE`.

## SR-STR-188 — Uniform adjacent two-cell O(p) transform via Newton-polyhedron and stationary phase
For the adjacent two-cell mixed transform, the four-Kummer Gauss lift has Phi=hR+kS+U(1-RS)+V(1+RS)+W(S-R)+Z(S+R). Lei Fu Newton-polyhedron nondegeneracy yields uniform torus O(p) off h=±k, with exceptional lines treated exactly. Independently, Katz-Laumon stationary phase for H=(1-RS)(1+RS)(S-R)(S+R) gives uniform |T_p(h,k)|<<p after generic, diagonal and axis splitting. The archived mainline proof also records the adjacent two-cell square-sieve consequence N_2cell(R,S) << (R S)^(2/3) B^o(1) on the physical packet.
Potential weapon types: TRACE_FUNCTION, NEWTON_POLYHEDRON, STATIONARY_PHASE.
Applicability gaps: Newton nondegeneracy must be checked face by face.; Diagonal and axis frequencies require separate receivers.
Transfer verdict: `DIRECT_FINITE_FIELD_ENGINE_WITH_FACE_AND_EXCEPTIONAL_FREQUENCY_ADAPTERS` — Lei Fu/Katz–Laumon carry the engines, not the repo nondegeneracy and exceptional-line checks.
Arsenal decision: `ACTIVE`.

## Firewalls
- Search absence is not a novelty claim.
- Uniform fixed-degree curve bounds do not by themselves supply the repo moving-family physical-height multiplicity theorem.
- Small-squarefree-kernel asymptotics are an input, not a full Stage14 physical-cell count.
- Local Q2 membership is not global solubility and is not assumed equidistributed.
- Square-sieve and finite-field savings are charged only in the original physical packet measure; automatic or previously charged savings are not multiplied again.
- Lei Fu/Katz–Laumon transfer requires the repo face-by-face nondegeneracy and diagonal/axis exception checks.
- Ordered fixed-prime products give qualitative zero density, not a fixed polynomial exponent.
- No perfect-cuboid existence or nonexistence claim is made.
