# M3-T11-154 — Global bridge audit: alphabet-cover cost, bilateral peeling and geometric height budget

STATUS=PROVED_CERTIFICATE_COST_BARRIER_AND_BILATERAL_DEGREE_FIREWALL
GLOBAL_BRIDGE_VERDICT=FAIL_FOR_TESTED_CERTIFICATES_NOT_IMPOSSIBILITY_OF_THE_TARGET
AUDIT_MODE=WITHIN_SESSION_PROOF_REDERIVATION_AND_EXACT_REPLAY_NOT_EXTERNAL
NEW_GLOBAL_OR_NEGLIGIBLE_SECTOR_BOUND=false
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
NEXT=M3-T11-155 SameWitnessGlobalIncidenceBudget

## Starting authority and why154 is an audit

Fresh MAIN, INDEX, RESULT-LEDGER, active T11 ROUTE and the complete153 card all designate153 as latest.152's prescribed-alphabet sector and153's small-cofactor sector are retained. The unresolved population E_bal consists of original primitive canonical positive endpoints at exact R<=B with some prime outside S_B and with R/p^v_p(R)>Y_B for every p|R, where S_B is the first floor((log B)^(4/3)) split primes and Y_B=B^(1/3)/(1+log B)^30.

The user specifically asked whether repeated partial exclusions really lead to closure.154 tests that logical bridge. It does not add another negligible sector and does not claim a new global exponent. It proves a lower bound for a proposed NUMERICAL CERTIFICATE, distinguishes that from a lower bound on physical endpoints, and tests a genuine all-degree geometric theorem with the correct height.

## 1. The scalar balanced residual has nearly linear size

Let T tend to infinity, B=4T^2, and V_T be the primes p in [T,2T] with p=1 modulo4 that are outside S_B. Write v=|V_T|. The prime number theorem for progression1 modulo4 gives

 v ~ T/(2 log T),
 #{pq:p,q in V_T,p<q}=binom(v,2) asymp B/(log B)^2.   (154.1)

Removing at most |S_B|=O((log B)^(4/3)) primes does not change this asymptotic. Unique factorization makes the products distinct. Every such R=pq lies between B/4 and B; is odd and split; satisfies151's scalar conditions p<=3q^2 and q<=3p^2; lies outside the prescribed alphabet; and has both complementary factors p,q>=T>Y_B for large T.

These are SCALAR DIAGONAL CANDIDATES. None is asserted to support a physical cuboid or to pass all Gaussian witness conditions. The conclusion is that the displayed residual support inequalities themselves do not make the remaining candidate set small.

The external input is only the standard fixed-modulus prime number theorem, stated in the final paragraph of [NIST DLMF27.11](https://dlmf.nist.gov/27.11). The construction, residual checks and counting consequence here are derived in this card.

## 2. A rigorous lower bound on152's full alphabet-cover certificate

For a finite split-prime alphabet S, retain152's numerical cap

 U_S(B)=min(C0*K^|S|, inf_(sigma>0) W_S(B,sigma)),
 W_S=64 B^sigma product_(p in S) F(p^(-sigma)),
 F(x)=sum_(n>=0)(2n+1)^3 x^n,
 C0=48^36288, K=48^15552.

Put k=|S intersect V_T|. Then, for EVERY S,

 U_S(B) >= binom(k,2).                                (154.2)

Proof. Each pair of distinct primes from S intersect V_T gives R=pq<=B. Its term in the positive Euler expansion of W_S is64*(3*3)^3*(B/R)^sigma, at least1. Thus W_S>=binom(k,2) for every sigma, and its infimum has the same lower bound. Separately, C0*K^|S|>=2^|S|>=binom(|S|,2)>=binom(k,2), including the cases k<2. Taking the minimum preserves this lower bound.

Consequently, for ANY family F_B of alphabets covering EVERY scalar candidate pair from V_T,

 sum_(S in F_B) U_S(B)
 >= sum_(S in F_B) binom(|S intersect V_T|,2)
 >= binom(v,2) asymp B/(log B)^2.                     (154.3)

This is a lower bound on the particular upper-bound certificate proposed in152, not on P(B). It applies regardless of alphabet sizes, overlaps or how cleverly the alphabets are chosen. Therefore covering all of this scalar residual and then adding those existing numerical caps cannot certify o(B^(1/3)). It must first exploit PHYSICAL support thinning, or replace the caps by stronger joint arithmetic estimates. It is not enough to add more alphabets.

For the polylog-sized design |S|<=(log B)^A, an additional transparent family-cost bound is #F_B >> B/(log B)^(2+2A). This has polynomial exponent1, whereas152's sufficient covered-sector budget requires alpha+1-1/A<1/3. The exact certificate obstruction(154.3) is stronger and does not rely on using that sufficient budget.

## 3. Two-sided prime peeling: bounded fibers do not multiply

Test the same balanced two-prime window, now retaining actual cofactor witnesses. Fix q in V_T. Since Norm(G)=q^2 has12 Gaussian solutions, the labelled witness count in153 is

 3*12^2+12^3=2160.

For each nonzero C, Norm(C)<=9q^4<=144T^4. If T>12, three distinct candidate primes p in [T,2T] with p^2|Norm(C) would force Norm(C)>=T^6>144T^4. Thus at most TWO such p exist for a fixed witness. Here n=1. The constant-fiber reconstruction in153 consequently gives at most4320 encodings for fixed q, and

 P_two-prime-window(B) <=4320 v=O(B^(1/2)/log B).     (154.4)

This is an upper bound on physical endpoints in the specified window, not a new o(M3) sector theorem. It is still above the sufficient B^(1/3) scale. The reverse p-fixed count has the same bound.

Define a directed NECESSARY relation A(q,p): some two- or three-term Gaussian cofactor witness at q has C!=0 and p^2|Norm(C). Its out-degree in the window is at most4320. Physical pairs must lie in the mutual relation A(q,p) and A(p,q). The two existential witnesses need not reconstruct the SAME endpoint; that compatibility cannot be dropped and later treated as an independent saving.

There is a precise logical firewall: bounded degrees on both sides alone do not imply o(T^(2/3)) edges. A matching on v vertices has degree1 in both directions but floor(v/2) edges, asymptotically much larger than T^(2/3). This is an ABSTRACT countermodel to inference from degree bounds; it is NOT a claim that the arithmetic graph contains a matching of this size. Its actual norm-form correlations may yield a much stronger theorem. That is exactly the missing work.

One explicit shared-witness condition is available. For p^n,q^m||R and an index i that is a unit at both primes (such an index exists), the p-oriented and q-oriented reconstructions satisfy

 bar(pi_p)^(2n) G_i^(p)
   = bar(pi_q)^(2m) G_i^(q), or its complex conjugate. (154.5)

Their real parts are the SAME positive physical edge. This equality, the remaining coordinates and the exact sphere identity must be counted together. Two separate norm-divisor tests or two independently chosen witnesses do not supply(154.5). No correlation saving is proved here.

## 4. A genuine all-degree geometric bridge also misses the current budget

Consider the standard cuboid surface X in P^6 with coordinates (a,b,c,u,v,w,R) and equations

 u^2=a^2+b^2, v^2=a^2+c^2, w^2=b^2+c^2,
 R^2=a^2+b^2+c^2.

This is a geometrically integral complete-intersection surface of degree16. Here is the adapter rather than an unsupported degree claim. Over an algebraically closed characteristic-zero field, the four squareclasses a^2+b^2, a^2+c^2, b^2+c^2, a^2+b^2+c^2 are independent in the projective base function field: each has a branch component occurring to odd order in it and in none of the other three. The four monic quadratic extensions therefore have generic degree16. The coordinate algebra is free of rank16 over the edge-coordinate algebra, hence embeds in this generic field and is integral. The four quadrics have codimension4; Bezout gives degree16. For a positive primitive endpoint the full integral tuple is primitive and its maximum coordinate is exactly R. Thus the project's cutoff is the projective height H<=B, with NO favorable rescaling.

Salberger, “Counting rational points on projective varieties”, Theorem0.9(b), supplies for a geometrically integral degree-d surface a collection of O(B^(3/(2sqrt(d))) log B+1) bounded-degree curves, outside which the point count is O(B^(3/sqrt(d)+o(1))). Applying it with d=16 gives

 number of covering curves: O(B^(3/8) log B+1),
 exceptional point budget: O(B^(3/4+o(1))).             (154.6)

Primary source: [Salberger2023, Theorem0.9](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/plms.12508). The general, possibly singular surface theorem is used; the smooth P^3 theorem0.5 is NOT silently transferred to X. This is a quantitative coverage-plus-residual theorem of the type discussed in150, but its supplied exponents do not certify o(B^(1/3)). Even an optimistic constant occupancy per curve would leave the supplied curve-family budget above that scale, and the exceptional term independently remains too large. These are insufficient UPPER budgets, not lower bounds on the best possible cover or the true point count.

Raising the embedding degree is not a remedy. Under the k-th Veronese embedding, degree becomes16k^2 while the exact endpoint height becomes R^k. The two exponents after converting back to B are

 k*3/(2sqrt(16k^2))=3/8,
 k*3/sqrt(16k^2)=3/4.                                (154.7)

The degree formula is (kH)^2=k^2 H^2. The height equality follows because the Veronese coordinates include every pure k-th power; their gcd is1 for a primitive tuple, and the largest is R^k. This prevents artificial exponent credit from an embedding change.

## 5. Decision, historical dedupe and next gate

The generic finite-fiber warning and balanced-semiprime warning already occur in HIST14-WITNESS-FW-001. They are not new principles.151 also proves a scalar-support barrier, using a different unbalanced candidate family.154 adds the exact certificate lower bound(154.3) on153's present residual; the concrete2160/4320 bilateral adapter and its precise inference limit; and the degree16/exact-height Salberger and Veronese budget audit. It does not rebrand the old warnings as a newly solved density theorem.

VERDICT:152/153 remain useful retained theorems, but automatic alphabet enlargement or repeated one-prime peeling is STOPPED AS A CLOSURE METHOD unless a new same-witness correlation changes the total bound. General curve-cover invocation and degree inflation also do not close the present gate. This is failure of the tested bridge certificates, not impossibility of proving P/M3->0 and not a retraction of152/153.

Next155=SameWitnessGlobalIncidenceBudget. The load-bearing target is a summed estimate on ALL E_bal for the exact joint Gaussian population J(R) of151, maintaining same-edge compatibility such as(154.5), prime allocation costs and exact R<=B. A sufficient target is sum J(R)<<B^(1/3-delta) for a fixed delta>0; a direct o(M3) comparison is also acceptable. A stronger denominator theorem could change the sufficient budget, but no such theorem is imported here.

Before starting a new classification, write its total family/witness budget and explain which bound beats154's obstruction. The balanced semiprime graph is a diagnostic test, not authorization to enumerate2,3,4,... prime-factor cases indefinitely. A semiprime-only improvement still requires a bound for the rest of E_bal. If no genuine correlation estimate is found, record the specific theorem obstruction and change mechanism; do not issue another renamed small-sector card.

GLOBAL_COUNTING_CREDIT=0; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false. TI remains parked,120 retracted,147–149 retained within their scopes, and automatic curve-degree escalation paused. No “a few more cards will close it” forecast is justified.

Replay artifacts verify154.py / verification154.json contain exact Gaussian necessary-relation checks, scalar product uniqueness, finite cover-cap checks, the abstract matching countermodel, and exact rational Veronese exponent arithmetic. The finite graph data are not a physical cuboid census and imply no general nonexistence result.
