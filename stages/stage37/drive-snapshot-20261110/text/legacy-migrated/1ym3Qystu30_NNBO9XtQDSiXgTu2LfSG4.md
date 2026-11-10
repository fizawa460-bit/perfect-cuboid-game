# M3-T11-135 — square-norm descent makes the x=-1/8 physical carrier empty

STATUS=PROVED_EXACT_SINGULAR_CARRIER_EMPTINESS / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GENERIC_MOVING_SUPPORT_OPEN
AUDIT_MODE=WITHIN_SESSION_REDERIVATION_NOT_INDEPENDENT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN

## Authority and scope

Continue from MAIN/INDEX/RESULT-LEDGER/active ROUTE current134. Targeted reread:133/134 and ROUTE52–53 (045/046), later singular-shell89–99 and generic100. Known history was not reread in full. T11 remains primary; TI remains parked. All conclusions concern the actual signed anti-roots and finite rational symmetric u, not quartic theta or arbitrary residual local points.

New conclusion: the finite-u nondegenerate physical carrier x=-1/8 has NO endpoints, for every content/coefficient packet and every R. This strengthens its old audited fixed-packet one-twelfth retirement. It does not prove a new generic power saving, primary closure, P/M3 limit or perfect cuboid nonexistence.

## 1. The old carrier and the newly available physical restriction

Use S=sum v_i, A=1+u², u=a/b reduced with b>0, and the Legendre coordinate x=A S/(16u). On x=-1/8,045/046 give

 S=-2u/A,
 f_u(z)=z³-Sz²+Ez-P=(Az-2u)(Az²+4uz-4u²)/A².

The quadratic factor has discriminant 16u²(u²+2). Since u is finite, rational and nonzero, rational anti-root splitting requires a rational w with w²=u²+2. Equivalently the old primitive conic was W²=a²+2b². This conic alone has infinitely many rational points and its old Gaussian lattice receiver did not prove emptiness.

133 now supplies the separate necessary physical identity A=k² with k rational and positive, equivalently a²+b²=c² with c an integer. For completeness it follows from d_i=(S-v_i)/2=2x_i y_i and the six nonzero physical squares 1±d_i: their products are (2+S+Su)²/(4A) and (2-S+Su)²/(4A). At least one numerator is nonzero, so A is a rational square.134 allows four square tests plus A square on the symmetric open mask; neither rational splitting nor the singular conic by itself licenses this restriction.

## 2. Exact descent obstruction, independent of fresh prime allocations

Suppose both necessary conics hold. Choose w>0, k>0. Then w>|u| and

 L=w+u>0, M=w-u>0, H=2k>0,
 L²+M²=2(w²+u²)=4(1+u²)=H²,
 LM/2=(w²-u²)/2=1.

Thus they produce a rational right triangle of area1. Such a triangle is impossible by the following elementary infinite descent, included so that the new adapter does not depend on an unproved elliptic-rank calculation.

Clear denominators and divide by the gcd of the integer legs. The primitive integer right triangle still has square area: scaling multiplies area by a rational square, and an integer that is a rational square is an integer square. Select a hypothetical primitive square-area triangle of minimal integer hypotenuse. Its legs are 2mn,m²-n² and hypotenuse m²+n² with m>n>0, gcd(m,n)=1 and opposite parity. Its area is mn(m+n)(m-n). These four positive factors are pairwise coprime, hence each is a square:

 m=e², n=f², m+n=g², m-n=h².

The latter two are odd squares. Set r=(g+h)/2, s=(g-h)/2, both positive integers. Then

 r²+s²=(g²+h²)/2=m=e²,
 rs/2=(g²-h²)/8=n/4=(f/2)².

Because g,h are odd, g²-h² is divisible by8, so n is divisible by4 and f is even. Therefore (r,s,e) is another integer right triangle with square area. Its hypotenuse e=√m is strictly smaller than m²+n². If it is not primitive, dividing its gcd preserves an integer square area and only decreases its hypotenuse further. This contradicts minimality.

Consequently there is no rational u with both 1+u² and u²+2 rational squares. In particular

 PHYSICAL_FINITE_U_X_MINUS_ONE_EIGHTH_OCCUPANCY=EMPTY.

This is exact set exclusion, not a sieve probability. No denominator-density factor, Gaussian determinant or independence assumption is used. It applies also to packets with empty relative-fresh support and at content-supported or2-primary primes, because its argument is global over Q and does not use primewise allocation. It does not state a new theorem for the projective u=infinity chart or for other x values.

The physical square-norm restriction also makes the old residual kernel D=sf(N_u/M_rel²) equal1 wherever the integral quotient is defined. That identity alone would not exclude the carrier; the descent above supplies the missing global obstruction.

## 3. Relation to old results and remaining research

045/046 singular conic, Gaussian factorization and local root destination statements remain correct in their original necessary-condition scopes. The080–089 fixed-packet bounds and later audited retirement remain valid, but their x=-1/8 physical support receivers are now vacuous on this finite-u physical locus. Do not resume its moving-D, dual-conductor sigma or two-fresh-core Gaussian pair as a live physical count. The conic, cubic-split and local enlargement examples remain legitimate nonphysical examples; the new emptiness does not classify arbitrary conic points as endpoints.

The x=27/40 shell is NOT eliminated by this proof. Keep its existing audited retirement and stated scope. Generic x support remains open. Fresh denominator-only134 routing remains c_p=0, Q_S=M_rel², C_u=1 and M_G=1 on the original odd split fresh support;130/131/132,129 residual persistence and123 class groups retain their stated scopes.120 physical adapter remains RETRACTED. No identification of quartic theta with v_i is reinstated.

The surviving generic physical count must still use four square tests 1±d_1,1±d_2, A square, the symmetric surface, exact q_i=√Den(d_i)=tau*c_i and R=lcm q_i=(h_1h_2h_3)tau<=B, plus original orientation, coefficient and cyclic masks.134's unique positive direction lift provides one endpoint per canonical state. Fixed-u, fixed-x or fixed-tau multiplicity alone does not count moving support. No ambient rational-height count substitutes for exact R.

## 4. Verification and adversarial audit

The proof is infinite descent, not bounded enumeration. The attached exact Python replay separately samples the old singular conic and square-norm conic; verifies coefficientwise cubic factorization, the area and triangle identities, coprimality used in descent, and the descent algebra. Wolfram symbolic replay returned {0,0,1}: zero factorization error, zero triangle equation error and area1. Physical endpoints enumerated0. Finite searches cannot establish nonexistence; they only check adapters.

Within-session adversarial audit PASS: denominator clearing preserves square area; primitive Pythagorean parametrization is legitimate; factor coprimality includes the2-primary parity case; f is even so the new area is integral; the new hypotenuse strictly decreases; all new exclusion claims are restricted to the finite-u x=-1/8 physical carrier. This is not an independent external audit.

External corroboration of the classical theorem only: Keith Conrad, The Congruent Number Problem, Theorem2 and its descent proof, author's University of Connecticut PDF, https://kconrad.math.uconn.edu/articles/congruentnumber.pdf . The application to this Stage37 carrier and the proof above are rederived here. No external source is used for a moving-support bound.

NEXT=M3-T11-136
ATTACK=GenericDenominatorOnlyFourSquareExactPhysicalHeightMovingSupport
NEXT_LEGAL_ACTION=Read135 then134/133 and targeted generic045/090 onward. Remove finite-u x=-1/8 from physical support exactly; retain x=27/40 audited retirement. On fresh support start c_p=0,Q_S=M_rel²,C_u=1,M_G=1. Seek a joint realized-support bound on generic square-N anti-root triples with FOUR square tests and exact R<=B, uniform per original fixed packet. The one-twelfth and primary exponent budgets are unchanged. Do not repeat the old singular conic, square-norm-only residual screen, G tail, signed-sum rarity, or fixed-fiber multiplicity as moving-support savings.
