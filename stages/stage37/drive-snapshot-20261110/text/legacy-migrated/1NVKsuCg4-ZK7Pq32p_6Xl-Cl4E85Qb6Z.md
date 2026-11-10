# M3-T11-134 — exact half-angle denominators remove the fresh Gaussian extreme; four-square lift and unique positive reconstruction

STATUS=PROVED_EXACT_FRESH_DENOMINATOR_ONLY_ROUTER_AND_PHYSICAL_HEIGHT_ADAPTER
AUDIT=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_PASS_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0; PRIMARY_GATE=OPEN; TI=PARKED_BY_USER

## Current authority and population
Continuation of latest133 and current MAIN/INDEX/RESULT-LEDGER/active ROUTE. Targeted reads:133; ROUTE6/7/17 physical triangle contents and equal tau; ROUTE32/37 actual distinct anti-roots and fresh unit/pole valuations; ROUTE35 symmetric surface; ROUTE48 allocation; retained129 square-norm S4 residual persistence. No full-history reread. Keep exact primitive physical R<=B, one canonical endpoint counted once, original coefficient/orientation/cyclic packet masks.

Notation: normalized directions x_i=e_i/R, y_i=signed opposite face diagonal/R satisfy x_i²+y_i²=1 and sum x_i²=1. Actual signed anti-roots from133 give
 d_i=(S-v_i)/2=2x_i y_i, S=sum v_i.
Physical space-triangle hypotenuse D_i=R/h_i, h_i=gcd(R,e_i); anti-root denominators B_i are DIFFERENT objects. Frozen contents c_1=h_2h_3, c_2=h_1h_3, c_3=h_1h_2 and D_i=tau*c_i, R=(h_1h_2h_3)tau, as already proved in ROUTE6/7.

## 1. Exact reduced denominators recover R and the entire content triple
In the primitive reduced space triangle write x_i=C_i/D_i, y_i=F_i/D_i, with C_i²+F_i²=D_i², D_i odd and gcd(C_iF_i,D_i)=1. Hence
 d_i=2C_iF_i/D_i²,
 Den(d_i)=D_i² EXACTLY, with no cancellation.
Also Den(1+d_i)=Den(1-d_i)=D_i², and the reduced denominators of L_i^+=x_i+y_i and L_i^-=x_i-y_i are both D_i. No fresh or content coefficient is silently discarded.

Therefore, given a lifted anti-root triple, set q_i=sqrt(Den((S-v_i)/2)). Then q_i=D_i and
 R=lcm(q_1,q_2,q_3),
 h_i=R/q_i,
 tau=gcd(q_1,q_2,q_3)=q_1q_2q_3/R²,
 c_i=q_i/tau,
 R=(h_1h_2h_3)tau.
All these are exact integers. The lcm formula follows also from133's R=lcm Den(x_i), since each Den(x_i)=D_i. The recovered h_i are pairwise coprime by ROUTE6; the equivalent product/gcd formulas are not extra independent constraints.

Thus the physical height is intrinsic to the ordered anti-root triple, independent of a lift sign search:
 sqrt(lcm_i Den(d_i))<=B.
In a fixed content packet this is exactly (h_1h_2h_3)tau<=B with q_i=tau*c_i. Moreover Den(S) and each Den(v_i) divide R², since S=sum d_i and v_i=S-2d_i. These are exact physical denominators, not an ambient rational box or an assumed B-uniform packet constant.

## 2. NEW physical router: all odd split fresh relative primes are denominator extreme
Let p^lambda||m_i, an odd split fresh relative prime outside all frozen content. Pairwise-coprime tau_j imply v_p(tau)=lambda, and p does not divide any c_j. Section1 forces, for ALL THREE directions,
 v_p(D_j)=lambda, v_p(d_j)=-2lambda.

The corrected ROUTE37 gives the targeted actual anti-root v_i a p-adic unit (v_p(v_i)=0), while the two other anti-roots have poles of depth2lambda. Since
 S-v_i=2d_i,
the exact physical denominator above implies
 v_p(S-v_i)=-2lambda,
 v_p(S)=-2lambda.
No cancellation against a unit can alter this pole depth.

Insert the retained040/48 conservation law
 k_p=v_p(Den S)=2lambda-c_p.
It follows that c_p=0 at EVERY such physical prime. Therefore
 Q_S=M_rel², C_u=1,
 M_D=M_rel, M_G=1,
 v_p(N_u)=2lambda and v_p(Den S)=2lambda.
On133's square-norm branch N_u=c², this gives
 c=M_rel*c_*, t=Den(S)=M_rel²*t_*, gcd(c_*t_*,M_rel)=1.

In particular the Gaussian extreme c_p=2lambda is PHYSICALLY EMPTY on this fresh equal-tau packet, for p1mod8 as well as p5mod8. In the old G local model S and targeted V are units, so d_i=(S-V)/2 is a unit (3u/4 modp), whereas the original physical triangle requires a pole of depth2lambda. Equivalently, its inferred local hypotenuse depths are (0,lambda,lambda) instead of (lambda,lambda,lambda); a content prime would be needed in the missing direction, contradicting freshness.

This is an exact original-space-triangle adapter, not a quartic-root identification and not a local density argument.130's strict-interior exclusion is retained and now has a shorter same-physical-denominator proof.131's abstract local D/G classifications and133's G p1mod8 necessity remain algebraically valid; the G model has no occupancy on the full fresh physical packet.132's H_G pullback remains true but its fresh G divisor receiver is vacuous because M_G=1. Retire the LARGE FRESH GAUSSIAN EXTREME TAIL as a physical research branch; retain every D Legendre/pole/singular-shell receiver.

SCOPE: odd split fresh relative support only, with the actual targeted anti-root unit theorem and original equal-tau content. No exclusion is claimed at2, at content-supported primes, or for arbitrary residual/cubic/local points without physical packet reconstruction. Finite nonzero u is used for the displayed N_u allocation; no new projective u=infinity theorem is promoted. The valuation statement from d_i itself does not use an identification with quartic theta.

Normalized48 can consequently be written with N_*=(c/M_rel)², Phi_*=Phi/M_rel² and W_*=W/M_rel². Then W_*²=-N_*Phi_* implies -Phi_* is an integer square. This is the old discriminant condition after the now-proved physical norm-square restriction, NOT another independent saving.

## 3. The signed compatibility equation is automatic on the symmetric surface
Define the symmetric surface polynomial
 T(v)=(SE+P)²-S²P(4S-P), E=sum_{i<j}v_iv_j, P=v_1v_2v_3.
For delta_i²=1-d_i² there is the exact eliminant identity
 product_{epsilon_i in {+1,-1}}(1+epsilon_1 delta_1+epsilon_2 delta_2+epsilon_3 delta_3)=T(v).
An explicit radical-free left side, with q_i=1-d_i², is
 [1+sum q_i²-2sum q_i-2sum_{i<j}q_iq_j]²-64q_1q_2q_3.

If all six1+/-d_i are rational squares, choose rational square roots L_i^+,L_i^- and delta_i=L_i^+L_i^-. Since T(v)=0, some sign choice has sum delta_i=-1. Flipping one root sign realizes each delta sign. Thus133's signed sum is NOT a further independent arithmetic filter once the six squares and the symmetric surface are imposed.

On the nondegenerate open branch d_i!=0 and1+/-d_i!=0, the compatible delta-sign triple is UNIQUE. If two triples worked, the sum over the nonempty set of flipped deltas would be zero. A singleton would force delta_i=0 and d_i²=1, impossible because the six rational squares would include2. Flipping all three contradicts sum delta_i=-1. Flipping two forces the remaining delta_k=-1 and hence d_k=0, excluded. For fixed compatible deltas, simultaneous flipping of L_i^+,L_i^- only changes the signs of x_i,y_i; x_i>0 selects exactly one choice per direction. Therefore an ordered signed anti-root triple has a UNIQUE positive normalized direction lift, improving133's safe at-most64 bound.

The open mask is essential. Zero-edge boundary triples can have several delta-sign branches; they are not positive endpoints. On the finite nonzero-u real split-cubic branch with S,P nonzero, d_i=0 would give v_j=-v_k and P/S=-v_j², contradicting P/S=4u²/(1+u²)>0. Still retain explicit nondegenerate masks in the counting population.

## 4. Four square tests suffice on square norm; exact endpoint-cover interface
On A=1+u² in Q², the133 product identities make
 product_i(1+d_i), product_i(1-d_i)
nonzero rational squares on the physical open mask. Hence it suffices to test the FOUR values
 1+d_1,1-d_1,1+d_2,1-d_2 in Q²;
the third plus/minus values follow by division by nonzero squares. Any two labeled directions may be used. This is a sufficient generating set of square tests, NOT a proof that their squareclasses are generically independent.

For an ordered rational anti-root triple on T(v)=0, on the nondegenerate open mask with finite nonzero u and A square, these four tests are equivalent to a unique positive normalized cuboid direction lift. Reconstruct via the unique delta signs and133's x_i,y_i, use R=lcm sqrt(Den d_i), and scale by that R to recover primitive edges and integral opposite face diagonals. To belong to a PREASSIGNED Stage37 T11 packet, still verify the original Gaussian orientation, coefficient, parity and cyclic-cover masks; the denominator identities alone are not a blanket packet converse.

An ordered positive endpoint has at most8 signed-y choices, and each ordered signed v triple has at most1 positive direction inverse on this open branch. Canonical ordering/orientation must remove this bounded witness multiplicity so one endpoint is counted once. No rational free sign parameter remains. This exact denominator/height interface is suitable for a same-measure count; it does not establish that count.

## Audit, verification, scope and next action
verify_m3_t11_134.py PASS:1331 generic rational eliminant identities;307 primitive rational unit-circle denominator identities;1000 arbitrary rational torus triples checking the eliminant versus signed sums (these are not physical sphere points);307 zero-edge boundary sphere/content/height tests showing why the open mask matters;144 old G local cubic-split/unit-rootline examples at p17,41,73,89,97,113 with square norm units, whose inferred triangle-depth pattern fails equal tau. Local norm-square means local units only; no global physical point is claimed. Physical endpoints enumerated=0. Symbolic replay has three zero identities. The proofs, not finite tests, establish branch emptiness and uniqueness; no positive physical endpoint was found or enumerated. Audit is within-session, not independent external.

Retain129's square-norm S4 residual class/local persistence: it is nonphysical and does not establish the four-square or denominator packet lift.123 class-group factors retained.120 remains RETRACTED. TI stays parked. Global power saving, P/M3 limit, nonexistence and primary closure flags remain false.

NEXT=M3-T11-135
ATTACK=DenominatorOnlyFourSquareExactPhysicalHeightMovingSupport
Read134 then133,045/046 and later D singular shells; target square-norm ordered anti-root triples with the FOUR square tests and exact q_i=tau*c_i, R=(h_1h_2h_3)tau<=B. On fresh relative support impose c_p=0, Q_S=M_rel² and C_u=1 from the outset. Seek the remaining denominator-extreme moving-S/active-M_rel support theorem on this exact measure, retaining all coefficient/orientation/cyclic filters. The canonical fixed-packet one-twelfth/primary exponent budgets remain unchanged. Do not resume a fresh Gaussian tail, a signed-sum rarity screen, a six-independent-square-density argument, or an ambient rational height substitution. Existing fixed-u/fixed-tau subpolynomial multiplicity does not count moving support.
