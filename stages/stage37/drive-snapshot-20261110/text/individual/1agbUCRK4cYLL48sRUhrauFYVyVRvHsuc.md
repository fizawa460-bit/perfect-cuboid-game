# M3-T11-195 — All-content pair-content divisor coordinate and complementary signed denominator law

CARD_ID: M3-T11-195
STATUS: PROVED_ALL_CONTENT_PAIR_CONTENT_DIVISOR_SUM / EXACT_COMPLEMENTARY_DENOMINATORS / K1_MIXED_PAIR_SUBSUMED_180 / LARGE_SUPPORT_OPEN
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Current authority and outcome

Fresh Drive MAIN, short RESULT-LEDGER, operational CARD-INDEX latest194/blank next row, card194 and active ROUTE17 were checked. Needed180 was read for overlap; its proof cites177's uniform content-supported integer compression. Bounded INDEX searches for pair denominator, h_i*h_j and relevant squareclass entries found no indexed all-content coordinate of the form below. No full historical reread and no external repository access.

195 began at194's large-s content-depth problem. The proposed shortcut of counting h-supported depth as a new sparse gain is rejected:177/180 already pay it at B^{o(1)} for fixed h. No new K=1 large-s correlation saving was obtained.

The retained substantive result is an ALL-content extension of194's unit-pair square denominator. For any pair i,j, let h_i=gcd(e_i,R), kappa_ij=h_i*h_j, and c_ij be the reduced denominator of the actual signed pair phase. Then

c_ij=kappa_ij*u_ij²,
Phi_ij=kappa_ij*u_ij=sqrt(kappa_ij*c_ij) is an integer divisor of R.

Uniformly, the ALL-content fixed-Phi endpoint fiber is B^{o(1)}, and

#E(B; min_{i<j} Phi_ij<=Z) <= Z B^{o(1)}.      (195.1)

This sums varying contents without an outer content-triple/packet cost. It applies before the K=1 / K>1 split. It is a threshold sector, not a global endpoint bound. At Z=B^{1/3-epsilon}, fixed epsilon>0, it is negligible relative to the retained M3 B^{1/3} benchmark. For K=1, the two mixed-content pair sectors are already included in180; the unit pair is194. Thus the actual-phase sector in this card receives no new K=1 primary disposal credit. No strict improvement over the older full-content171 sector is asserted without a proved comparison.

## 2. Measure and sign convention

E(B) means the original positive primitive endpoints R<=B, all integral face diagonals, all exact original common-phase/receiver/content/positivity/cyclic masks. Put w_l=(e_l+i f_l)/R with the ACTUAL retained signed opposite face diagonal f_l. The auxiliary opposite sign below is computed from the same physical edges and signed diagonals. It need not satisfy the original common-phase equations as a replacement phase, and it is never substituted into those equations.

For one pair define

psi_+ = w_i/w_j,
psi_- = w_i/conj(w_j).

Their integer real/imaginary numerators are respectively

Q_+=e_i e_j+f_i f_j, P_+=f_i e_j−e_i f_j,
Q_-=e_i e_j−f_i f_j, P_-=f_i e_j+e_i f_j.

Both have norm1, with c_±=R²/gcd(Q_±,P_±). Changing the sign of f_j exchanges the two. The denominator formula holds even when an auxiliary phase is a unit; actual positive endpoints avoid the degenerate unit/quarter-turn cases as in194. Counting signs introduces only finite multiplicity.

## 3. Primitive contents and local denominator law

R is odd: if two positive edges were odd, their integral face diagonal would have square2 mod4, impossible. Since the edges are primitive, at least one is odd. Consequently exactly one edge is odd and R is odd.

The h_l are pairwise coprime. If p divided R and two edges, the sphere equation would force p to divide the third edge, contradicting primitiveness. Thus for each p^lambda||R at most one edge has rho=v_p(h_l)>0. At least two space circles have a p-unit edge, forcing p=1 mod4. All primes of R therefore split in Z[i].

At a split prime above p, the normalized circle w_l has Gaussian valuations +d_l and −d_l, up to orientation, where

d_l=lambda−v_p(h_l).

This follows by reducing the integer circle by h_l; its primitive Gaussian numerator is a square, its rational denominator has exponent d_l, and the two conjugate Gaussian valuations are opposite. When d_l=0, both valuations are0 and no orientation choice is needed. Rational denominator valuation is the absolute value of the Gaussian valuation.

For a pair, set rho=v_p(kappa)=v_p(h_i)+v_p(h_j). Coprimality of contents implies either d_i=d_j=lambda (rho0), or the unordered depths are lambda and lambda−rho. Conjugating w_j changes the sign of its Gaussian valuation. Therefore the unordered exponents of the two pair denominators are exactly

{v_p(c_+),v_p(c_-)}={rho,2lambda−rho}.       (195.2)

This includes partial content0<rho<lambda and full content rho=lambda. No assumption gcd(h_l,R/h_l)=1 is made. At primes dividing the third content, rho0 and the pair is still a two-unit pair at the full depth lambda.

It follows prime by prime that

c_±=kappa*u_±²,
gcd(u_+,u_-)=1,
u_+u_-=R/kappa.                              (195.3)

Each prime-power block p^{lambda−rho} of R/kappa goes wholly to one u; at rho=lambda it contributes no block. Thus u_± are complementary unitary divisors of R/kappa. The exact complementary identities are

c_+c_-=R², gcd(c_+,c_-)=kappa,
Phi_±=kappa*u_± | R,
gcd(Phi_+,Phi_-)=kappa,
lcm(Phi_+,Phi_-)=R,
Phi_+Phi_-=kappa*R.                          (195.4)

These product/gcd identities are automatic, not independent detectors whose probabilities can be multiplied. In particular a non-unit-content denominator is generally NOT itself a square. The test pair R65, (e_i,f_i)=(25,60), (e_j,f_j)=(39,52) has contents5,13 and denominators65,65. This is a pair of circles, not a physical endpoint.

## 4. All-content fixed-Phi fiber and summed bound

Use194's ALL-content uniform fixed actual pair-phase fiber B^{o(1)}, obtained from E_a:Y²=X³−a²X with finite primitive reconstruction. Its coefficient/point heights are polynomial in B and its external torsion input was checked in194. It already sums the contents not appearing in the phase.

Fix Phi_ij=N<=B. Then kappa is a divisor of N, u=N/kappa and

c_ij=kappa*u²=N²/kappa.                      (195.5)

There are at most d(N)=B^{o(1)} kappa choices. For each such choice, c is fixed and <=B²; the norm-one rational directions with this denominator are at most B^{o(1)} by Gaussian divisor counting. Each direction has B^{o(1)} physical endpoints by194. Individual h_i,h_j and the third content are NOT independently summed. They are recovered from the physical endpoint in194's finite reconstruction. Hence

#E(B;Phi_ij=N)<=B^{o(1)} uniformly.            (195.6)

Sum N<=min(Z,B) and take the finite union over three actual pairs to prove(195.1). For the auxiliary opposite sign, the same receiver proof applies to the derived signed circles: reconstruct physical edges, restore the original sign labels and apply the original masks. It supplies the same bound without asserting that the auxiliary phase satisfies the original common-phase selector. The finite union where any auxiliary Phi_±<=Z has the same Z B^{o(1)} upper bound. No new sector credit is assigned to that auxiliary union here: comparison with180 must use the same signed routing, and the actual fresh m_i are not invariant when one diagonal sign is flipped.

The special fixed-kappa version is #E(kappa fixed,u_ij<=D)<=D B^{o(1)}, even as the third content varies. Summing kappa independently would cost K*D for kappa<=K. The Phi sum instead absorbs kappa into the divisor label N. The coarser194 bound on c<=Z² would cost Z², so(195.1) is a genuinely summed extension using the exact content-normalized structure, rather than a renamed fixed-phase statement.

## 5. K=1 overlap and content-depth obstruction

On K=1 relabel(h_1,h_2,h_3)=(1,1,h). For the two-unit actual pair,

kappa_12=1, Phi_12=s_12=m_1m_2*a_H,

exactly194. Its full content-supported cofactor a_H cannot be capped by h. Opposite sign gives the complementary s'=R/s; this balance does not by itself give a sub-B^{1/3} occupied-support theorem.

For the mixed pairs kappa_13=kappa_23=h. Their fresh u factors are respectively m_1m_3 and m_2m_3, and their remaining factors b_13,b_23 are supported on h. Hence

Phi_13=h*m_1m_3*b_13,
Phi_23=h*m_2m_3*b_23, b_13,b_23>=1.           (195.7)

Therefore180's SigmaSharp=h*min_{pairs}(m_i m_j) is <=Phi_13 and <=Phi_23. Both ACTUAL-phase small mixed-Phi sectors at the same threshold are already disposed by180. This inclusion does not assert the same formula for the auxiliary opposite sign using unchanged fresh m_i. When h1 the unit-pair sectors are194/180 overlap. This precise inclusion is why no new K=1 sector is credited.

For fixed h,177 already supplies #{a<=B^A:rad(a)|h}=B^{o(1)}, uniformly at fixed A.180 uses this for full relative cores. Trying the same estimate for a_H is valid but provides no new saving: summing h and m_1m_2 incurs the old occupied-support problem. It cannot be multiplied as an independent small probability against194 or192. The local complement rule(195.4) is likewise deterministic and supplies no independent density.

For arbitrary contents,195 extends the pair-content coordinate to all K. It does not prove that any physical endpoint lies in a newly covered sector. A comparison against171's full Sigma should be established before calling any K>1 sector strictly new. No K>1 low-median average is closed.

## 6. Verification

Script verify_m3_t11_195.py and report M3-T11-195-verification.json use exact standard-library arithmetic on integer circles with odd R<=5000 and coprime pair contents. PASS:1868 unit pairs,5796 one-nonunit pairs,1908 two-nonunit pairs;19144 signed denominator/reconstruction checks. These check c=kappa*u², the complementary product/gcd laws, Phi|R and fixed-N denominator reconstruction. They include partial and full content depths. This larger circle locus is NOT the endpoint measure; physical endpoints checked0. No independent audit and no asymptotic proof by finite enumeration are claimed. The proof is in sections3–4.

## 7. Drive-only continuation

LATEST=M3-T11-195; NEXT196. Retain194 global pair fiber,195 all-content Phi sector,193 signed collision/T0 tail,192 integer W/intrinsic reconstruction,180/174 filters and134 fresh D-only. Gate OPEN/global credit0; separate-chat audit162–185 unchanged;186–195 independent audit not run; TI parked120/retracted147–149/frozen.

NEXT196 should return to the surviving K=1 large-s/LargeSigmaSharp physical support. A theorem must jointly control content-supported whole R-depth and fresh m1m2 against192 integer W and original U,V,N_T/Den(S), with193 signed collision retained. Use195's complementary gcd law as an exact reconstruction constraint, not a second saving. Fixed-h supported-depth compression is already177/180; neither that lemma nor fixed-phase fibers resolve the moving support. Independently,195's all-content small-Phi bound is available for K>1 threshold routing, but do not conflate that with closing its low-median average. Do not reopen134 fresh C_u/G or independently multiply local densities. Detailed proofs stay here; MAIN/INDEX/short LEDGER point to195/NEXT196.

## 8. Verification artifact IDs

SCRIPT=17wQmPOup3G32-3GEYd0fZX0JiPAXhM8W
JSON=1SdReReip2sTO3QqF7AKg4k8YUAnFJNgb
Both are stored in Stage37 verification research auxiliaries; this card is stored in the research-card folder.
