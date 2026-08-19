## SR-STR-179 — Full-radical squarefree CRT projective-line incidence cover
For odd squarefree q and unit A,B, A x^2=B y^2 mod q is empty if a local ratio is nonsquare; otherwise it is covered by 2^omega(q) CRT projective lines x=r y mod q, each a rank-two lattice of index q. The full odd radicals R_S,R_X,R_H are exact witness congruence moduli even when selected kernels are proper divisors.
SEARCH: quadratic congruence squarefree modulus projective lines | CRT square roots lattice index
TYPES: lattice covering | quadratic congruences
WEAPONS: CRT, LATTICE_COVER, LOCAL_OBSTRUCTION
GAPS: q must be odd squarefree with unit coefficients. | Both line multiplicity and lattice index must be retained.
TARGETS: Stage14 squarefree incidence cells

## SR-STR-180 — Moving diagonal-pair genus-one quartic with smaller-diagonal enumeration
Fixing a core and one diagonal pair puts the opposite reduced slope t on a smooth even quartic W^2=F0((b0d0)^2-(a0c0)^2t^4), with an injective primitive-diagonal-to-slope map. Smaller-diagonal enumeration plus a separate B^o(1) bounded-height multiplicity theorem gives the good-cell bound; genus one alone does not.
SEARCH: moving quartic genus one reduced slope | uniform rational point count binary quartic
TYPES: genus-one fibration | height counting
WEAPONS: GENUS_ONE, HEIGHT_COUNTING
GAPS: The exponent is receiver-specific. | A uniform bounded-height input is essential.
TARGETS: Stage14 diagonal-pair good cells

## SR-STR-181 — Primitive physical two-face gluing and compact conjugate-gap chart
For oriented primitive Pythagorean faces with S1=g*alpha and S2=g*beta, minimal shared-edge gluing is e=g*alpha*beta=lcm(S1,S2), x=beta*X1, y=alpha*X2; a common scale t equals gcd(e,x,y), so primitivity forces t=1. With t1=X1/S1, t2=X2/S2 and L=lcm(S1,S2), (e,x,y)=L(1,t1,t2) and the ambient real height is D_R=L*sqrt(1+t1^2+t2^2), without any rational or integral space-diagonal condition. On the physical space-diagonal branch, G^2=H^2*S2^2+S^2*X2^2=S^2*H2^2+X^2*S2^2 gives an induced integral triple, while compact conjugates satisfy N_phys*N_-=S^2*X^2*(R_-)^2 and Z_-=-U*V/X2^2. These are exact coordinate adapters, not population estimates.
SEARCH: shared leg Pythagorean triples gluing identity | compact elliptic conjugate numerator
TYPES: Diophantine parametrization | coordinate transformation
WEAPONS: COORDINATE_ADAPTER, PYTHAGOREAN_GLUING
GAPS: No count or independence follows. | The primitive gcd scale must be retained.
TARGETS: Stage14 shared-edge two-face configurations

## SR-STR-182 — Radical-poor hypotenuse support sparsity and polynomial witness box
In the recorded Stage14 receiver, hypotenuse support radical at most B^rho gives a B^(rho+epsilon)-sparse supported base/class family. Separately, a logarithmic canonical-height witness has denominators and integral factors in a fixed polynomial box, so finite-dimensional dyadic subdivision costs B^epsilon. Neither statement alone counts rational points.
SEARCH: radical poor Pythagorean hypotenuse | canonical height denominator polynomial box
TYPES: smooth-number sparsity | height comparison
WEAPONS: SPARSE_FAMILY, HEIGHT_ADAPTER
GAPS: rho is tied to the recorded population. | Polynomial boxing is not a point-count theorem.
TARGETS: Stage14 radical-poor and bounded-height cells

## SR-STR-183 — Exact eight-state Q2 Kummer covering image
For the normalized local triple [q],[q-1],[q+t^2] with v2(t)>=2, exactly eight of the 64 product-square states occur: (1,1,1),(3,7,5),(5,1,5),(7,7,1),(2,1,2),(6,7,10),(10,1,10),(14,7,2), using representatives 1,3,5,7,2,6,10,14 in Q2*/Q2*^2.
SEARCH: Q2 Kummer image eight squareclass states | 2 descent valuation cylinder classification
TYPES: local 2-descent | Kummer image
WEAPONS: LOCAL_DESCENT, Q2_KUMMER_IMAGE
GAPS: Membership is local necessity, not global solubility. | The eight states are not equidistributed in a moving physical family.
TARGETS: Stage14 prime-2 local Kummer covering

## SR-STR-184 — Injective primitive third-face transfer from a physical two-face edge
Given physical F1=(S,X,H), F2=(S2,X2,H2), g=gcd(S,S2), G=gd and c=gcd(H,X2), the primitive reduction F3=(HS2/(gc), SX2/(gc), d/c) is Pythagorean and H3<=d. The physical edge is recoverable from (F2,F3), so the map is injective. Every image satisfies (S3X2)^2-(X3S2)^2 being a nonzero square, only a necessary condition.
SEARCH: primitive third Pythagorean face transfer injective | shared edge cross gcd square condition
TYPES: Diophantine injection | primitive reduction
WEAPONS: INJECTIVE_TRANSFER, PYTHAGOREAN_REDUCTION
GAPS: The cross gcd c is mandatory. | The displayed square condition is not sufficient for arbitrary primitive-face pairs.
TARGETS: Stage14 physical ordered two-face edges

## SR-STR-185 — Pairwise gcd support of integral witness factors
For G0=A, G1=A-S^2D^2, G2=A+X^2D^2 with gcd(A,D)=1, every prime dividing D is coprime to all Gi and gcd(G0,G1)|S^2, gcd(G0,G2)|X^2, gcd(G1,G2)|H^2. Thus odd overlap supports 01,02,12 lie on the disjoint primitive Pythagorean edges S,X,H.
SEARCH: pairwise gcd elliptic integral witness factors | squarefree kernel Pythagorean edge support
TYPES: gcd structure | 2-descent
WEAPONS: GCD_SUPPORT, SQUAREFREE_KERNEL
GAPS: This precedes and does not replace the full signed-kernel factorization. | Overlap primes cannot be moved between edges.
TARGETS: Stage14 integral witness factorizations

## SR-STR-186 — Balanced inert-prime quartic square-sieve dispatch
For the fixed quartic F(P,Q)=PQ(Q-P)(Q+P), inert primes p=3 mod 4 have exact complete trace cancellation. On a product-square packet with square-part box volume M=XYZW and H=min(X,Y,Z,W), the proved square-sieve inequality is optimized at auxiliary prime scale L=H^(4/5), giving N_packet << M H^(-4/5) B^o(1). Thin packets switch to the exact shared-squareclass four-cell decomposition rather than being discarded.
SEARCH: inert prime square sieve quartic kernel | balanced character cancellation square parts
TYPES: square sieve | character sums
WEAPONS: SQUARE_SIEVE, CHARACTER_CANCELLATION
GAPS: The fixed quartic and product-square packet normalization must be retained. | Thin packets require the shared-squareclass four-cell switch; they are not automatically sparse. | A packet saving must still be summed in the original physical measure.
TARGETS: Stage14 balanced fixed-quartic squareclass packets

## SR-STR-187 — Same-measure fixed-prime ordered-limit squareclass sieve
For Q(B) subset P(B) with identical physical measure and, for each fixed finite good-prime set S, a CRT-refined asymptotic plus necessary local acceptance rho_p, limsup Q(B)/P(B)<=prod_{p in S}rho_p. Only after B->infinity may S expand; if the ordered products tend to zero, Q(B)/P(B)->0. This proves qualitative zero density, not a fixed-power saving.
SEARCH: fixed prime ordered limit sieve zero density | same measure local acceptance product
TYPES: local sieve | density theorem
WEAPONS: LOCAL_SIEVE, ZERO_DENSITY, ORDERED_LIMIT
GAPS: The Stage15 rho_p cannot be transplanted to another population. | Growing modulus with B requires a separate uniform theorem. | No fixed-power saving follows from the ordered limit.
TARGETS: Stage15 two-face space-diagonal survivors and compatible future physical measures

## SR-STR-188 — Uniform adjacent two-cell O(p) transform via Newton-polyhedron and stationary phase
For the adjacent two-cell mixed transform, the four-Kummer Gauss lift has Phi=hR+kS+U(1-RS)+V(1+RS)+W(S-R)+Z(S+R). Lei Fu Newton-polyhedron nondegeneracy yields uniform torus O(p) off h=±k, with exceptional lines treated exactly. Independently, Katz-Laumon stationary phase for H=(1-RS)(1+RS)(S-R)(S+R) gives uniform |T_p(h,k)|<<p after generic, diagonal and axis splitting. The archived mainline proof also records the adjacent two-cell square-sieve consequence N_2cell(R,S) << (R S)^(2/3) B^o(1) on the physical packet.
SEARCH: Lei Fu Newton polyhedron twisted exponential sums | Katz Laumon stationary phase Kummer surface
TYPES: finite-field exponential sums | stationary phase
WEAPONS: TRACE_FUNCTION, NEWTON_POLYHEDRON, STATIONARY_PHASE
GAPS: Newton nondegeneracy must be checked face by face. | Diagonal and axis frequencies require separate receivers.
TARGETS: Stage14 adjacent two-cell mixed finite-field transforms
