# M3-T11-194 — global pair-phase fiber and K=1 square-denominator summation

Status: retained scoped counting result; gate OPEN; global credit 0. Current authority: Stage37 MAIN / operational CARD-INDEX / short RESULT-LEDGER / active ROUTE §17. Dependencies: 010 uniform torsion counting input; 134 fresh D-only route; 180 overlap check; 182–193 retained physical normalization and receiver constraints. No retraction. Separate-chat audit162–185 stays at its existing scope; 186–194 have no independent audit. TI parked120/retracted147–149/frozen remain unchanged.

## 1. Result and measure

Let E(B) denote the original primitive positive physical endpoints with integer space diagonal R<=B, all face-square conditions and the retained original masks. e_i>0 are edges, f_i are signed opposite face diagonals, sum e_i²=R² and e_i²+f_i²=R². Sign and permutation choices are finite and can be canonically routed. Set w_i=(e_i+i f_i)/R.

For each pair i,j define its reduced rational norm-one phase psi_ij=w_i/w_j=a+i b and its common reduced denominator c_ij. The following bounds sum over ALL contents, without an outside h or C multiplier:

* Fixed admissible psi_ij: #E(B;psi_ij fixed)<=B^{o(1)}, uniformly in phases actually attained at R<=B.
* #E(B;min_{i<j} c_ij<=Z)<=Z B^{o(1)}.
* For K=1, choose the canonical two unit-content directions h_1=h_2=1. Then c_12=s_12² with s_12 a unitary divisor of R, and #E_K1(B;s_12<=D)<=D B^{o(1)}.

Consequently D=B^{1/3-epsilon} is a disposable K=1 sector at the existing M3 B^{1/3} comparison scale, for fixed epsilon>0. This is a scoped upper bound, not a proof that the sector contains physical endpoints, and does not close its large-s complement or K>1.

## 2. Exact integer identities and elliptic map

Write Q=e_i e_j+f_i f_j, P=f_i e_j-e_i f_j, T=e_i f_i+e_j f_j, and let k be the remaining index. Direct expansion gives

Q²+P²=R⁴, Q²−T²=e_k⁴, P T=Q(e_j²−e_i²).

The second identity uses (e_i²−f_j²)(e_j²−f_i²)=e_k⁴. No coprimality is needed. Here a=Q/R², b=P/R², z=e_k/R. Map to

E_a: Y²=X³−a² X, with X=−z² and Y=−z T/R².

Indeed Y²=z²(a²−z⁴)=X³−a²X. This full-content map uses the actual physical circle/sphere equations; it is not a free congruence or independent density construction. E_a has rational 2-torsion at X=0,+a,−a, and discriminant 64a⁶.

For positive physical endpoints a and b are nonzero. If a=0 then the circle relation forces e_i²+e_j²=R², hence e_k=0. If b=0 then psi=±1: the negative case contradicts positive real parts, and the positive case gives equal positive edges and an integral face diagonal sqrt(2)e_i, impossible. Thus E_a is nonsingular and 1±a are nonzero.

## 3. Uniform point count and finite reconstruction

The coefficient a has rational height <=B²; coefficient a² has height <=B⁴. The point X=−e_k²/R² has height <=B², and Y=−e_k T/R³ has polynomial height because |T|<=R². All logarithmic curve and point heights are O(log B), with absolute constants.

Primary counting input checked against Marta Dujella, “Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves”, arXiv:2312.03655v1, Theorem1.1 and the height comparison in the proof of Corollary1.3 (pp2–3): over fixed Q, rational prime-order torsion supplies a uniform subpower canonical-height count above the curve-height threshold. Choose the theorem's bound T_*=B^A with an absolute A large enough for BOTH that threshold and canonical/ordinary height comparison. Its bound becomes B^{O(1/log log B)}, uniformly for our E_a. Source: https://arxiv.org/pdf/2312.03655 . This is the existing type of external counting input retained in 010; the pair-phase map and summation here are the new application, not a new external theorem.

Finite reconstruction is essential. Put xi_l=e_l/R, eta_l=f_l/R, S=xi_i+xi_j, D=xi_i−xi_j. The fixed phase yields

S²=(1+a)(1−z²/a), D²=(1−a)(1+z²/a).

For each E_a point, z is determined up to two signs by X=−z², with positivity selecting one. The two equations give at most four (S,D), hence at most four edge pairs. Then eta_j=(a xi_j−xi_i)/b and eta_i=b xi_j+a eta_j. The third signed diagonal has at most two choices, followed by the original masks. Fixing a instead of psi gives at most two b values.

Because gcd(e_1,e_2,e_3)=1, R=lcm(Den(xi_1),Den(xi_2),Den(xi_3)). Therefore contents and R are recovered, not an independent multiplicity to sum outside the curve bound. This proves the global fixed-psi fiber bound even across varying contents. The point need only lie on this receiver curve; reconstruction and masks select its physical subset. Counting extra receiver points only enlarges the upper bound.

## 4. All-content small pair denominator sum

c_ij=R²/gcd(Q,P)<=B². For fixed integer c the primitive norm-one direction is (q+i p)/c, q²+p²=c², gcd(q,p,c)=1. Gaussian divisor factorization bounds the number of such directions by c^{o(1)} (all signs included). Thus the fixed-c pair-phase spectrum times §3 is B^{o(1)}. Summing c<=Z and the three canonically routed pairs proves Z B^{o(1)}. Truncate Z at B² when necessary. This is a summed physical bound; it does not identify c_ij with the pre-existing product-phase denominator c of 183/193.

## 5. K=1 exact squared denominator, including content-supported primes

Take the canonical two directions with gcd(R,e_1)=gcd(R,e_2)=1. Their primitive integer circles imply R odd and every prime divisor of R splits in Z[i]. At every p^lambda||R, including primes supported on the THIRD content h, e_1,e_2 are p-units. Put r_l=f_l/e_l modulo p^{2lambda}; r_l²=−1 there.

If the two Gaussian orientations agree, r_1=r_2, then both Q and P vanish modulo p^{2lambda}; their common valuation is exactly 2lambda, since Q²+P²=R⁴ forbids a larger common valuation. If they oppose, r_1=−r_2, then Q=e_1e_2(1+r_1r_2) is a p-unit. Thus the reduced denominator keeps either p^{2lambda} or nothing. Hence c_12=s_12², where s_12 selects whole prime-power blocks p^lambda of R: s_12|R and gcd(s_12,R/s_12)=1.

For a fixed s<=B, the directions with denominator s² have at most B^{o(1)} possibilities. Applying the ALL-content §3 fiber to each gives B^{o(1)} endpoints for fixed s. Sum s<=D to obtain D B^{o(1)}. No h/C factor appears. This uses the actual whole denominator and its exact square structure; it is not an independent fresh-prime density product. Sign choices only change the selected orientations and remain finite.

## 6. Fresh dictionary, overlap, and remaining obstruction

On 134's K=1 fresh D-only support, let m_i be the fresh relative orientation core unique to direction i, and T0 the all-same core. For pair1,2 the fresh part of s_12 is m_1 m_2: relative core m_3 and T0 cancel. Precisely

s_12=m_1 m_2 a_H, rad(a_H)|h, gcd(a_H,m_1m_2)=1.

a_H selects the full p^lambda depth of R at content-supported primes whose two unit directions oppose. With partial third content it is NOT justified to assume a_H<=h, or to replace s_12 by a fresh-only product. After removal of s_12<=D, for any chosen cutoff A_H the residual splits exactly into a_H>A_H or m_1m_2>D/A_H. These two alternatives require a joint physical count with the moving support; the identity alone supplies no saving.

When h=1, all three pairs are unit-content and s_ij=m_i m_j. Removing the union min s_ij<=D forces every pair product>D, hence M_rel>D^{3/2}. This is already the h=1 case of 180's small SigmaSharp filter. It receives no new primary credit. For arbitrary h, this card proves its full-denominator sector independently; it does not establish any general inclusion or strict improvement over 180's h*min fresh pair product. Nor does it treat this count as a solution to 193's remaining unshared-conductor problem.

## 7. Verification and continuation

Executable standard-library exact checks: verify_m3_t11_194.py; machine report: M3-T11-194-verification.json. PASS: 17572 signed unit-pair square-denominator/unitary checks at R<=20000; 28 rational partial-sphere map/reconstruction checks, including 4 nonunit checks; 1504 full circle/sphere algebra checks over finite fields17,41,73. The example (672,153,104), R697 has only two integral face diagonals185,680; it is NOT a physical endpoint. Finite-field points are NOT rational endpoints. Physical endpoints checked:0. These finite checks verify formulas and implementation, not the asymptotic theorem or an independent audit.

NEXT195: retain the §5 small-s bound, then attack the large-s residual by jointly controlling content orientation a_H and m_1m_2 against 192's integer W/intrinsic normalization and actual U,V, N_T/Den(S), retaining 193's signed collision identity. A new summed correlation estimate must pay the content-supported whole-depth cost. Do not relabel §3's fixed-phase fiber, independently multiply local densities, re-charge h=1/180 or174 small-tau sectors, or reopen134 fresh C_u/G. K>1/large-c low-median remains separately OPEN. MAIN/INDEX/short LEDGER should point here and NEXT195; detailed proof stays in this card.

## 8. Drive verification artifact IDs

SCRIPT=1ENse1O1RbIzNvLjiltHkIKxPfFyDoTZX
JSON=1lQRbnj0sEHHBYiZQTJiWTPEf8Qq6dn07
Both are in Stage37 verification research auxiliaries; this card is in the Stage37 research-card folder.
