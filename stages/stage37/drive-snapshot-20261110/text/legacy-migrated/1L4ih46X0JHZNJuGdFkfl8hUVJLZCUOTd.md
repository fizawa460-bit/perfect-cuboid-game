# M3-T11-141 — Content-complete Heron square allocation on exact tau

STATUS=PROVED_PAIR_CONTENT_GCD_ADAPTER_AND_FULL_TAU_FOUR_FACTOR_COVER
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-142 ContentCompleteHeronLargeSquareDivisorRealizedSupport

## Authority and physical scope
Fresh MAIN/INDEX/RESULT-LEDGER/active ROUTE140 and latest140; targeted139 integer signed lift,138 primitive plus-vector and134 denominator/content interface. Targeted Heron/gcd lookup found no earlier content-complete adapter. Known full history not reread. Retain exact primitive positive physical endpoint R<=B, canonical ordered signed face witness, original content/coefficient/orientation/parity/cyclic masks and one endpoint one count.140 parity-empty zero factors and no single full-R-square factor remain;139 exact monic cover and signed R^2 divisor retained.120 remains retracted.

Notation: A_i=e_i+f_i (physical integer PLUS vector), h_i=gcd(A_i,R)=gcd(e_i,R), H_c=h_1 h_2 h_3, tau=R/H_c. These h_i are pairwise coprime and H_c|R by134. Define F_0=sum A_i^2 and F_i=F_0-2A_i^2. All F are odd and nonzero by140, and R^2|product F by139. New q_j below are allocation divisors, NOT physical hypotenuses D_i or historical anti-root denominators.

## 1. Every pairwise overlap on R is bounded by its exact content
For distinct i,j,k in{1,2,3},
 F_0-F_i=2A_i^2, F_j+F_k=2A_i^2.
Because the F factors are odd,
 gcd(F_0,F_i,R^2) divides h_i^2,
 gcd(F_j,F_k,R^2) divides h_i^2.
Absolute values are used in integer gcds. Indeed an odd common divisor divides A_i^2, and gcd(A_i^2,R^2)=h_i^2. These are exact divisor bounds, uniform across packets, with contents explicitly present.

Also gcd of ANY THREE distinct F factors equals1. An odd prime dividing F_0,F_i,F_j would divide A_i,A_j and then the remaining A_k via F_0; a prime dividing F_1,F_2,F_3 would divide every A_i from the pair sums. This contradicts primitive gcd(A)=1. The prime2 divides no F.

## 2. Canonical allocation of ALL tau, including content-supported powers
Fix p^lambda||R and put kappa=v_p(H_c). At most one h_i has positive p-adic depth, and kappa<=lambda. Let d_j=v_p(F_j), j=0..3, using finite valuations because F_j!=0. Triple gcd1 implies at most two positive d_j, and139 gives sum d_j>=2lambda.

If kappa=0, Section1 makes the positive factor unique and its depth at least2lambda.
If kappa>0 and two factors have positive depth, their minimum depth is at most2kappa by Section1. Therefore their maximum depth is at least2lambda-2kappa. If just one factor is positive, its depth is at least2lambda and the same bound holds.
Consequently, for every prime with lambda>kappa, choose the factor j having maximal d_j, breaking ties by smallest index, and allocate p^(lambda-kappa) to q_j.
Then the q_j are uniquely defined by the actual A,R and
 pairwise gcd(q_j,q_k)=1,
 product_(j=0..3)q_j=tau,
 q_j^2|F_j for each j.
This replaces140's router on R_nc (which removed COMPLETE content-supported prime powers) by a router on the ENTIRE exact tau=R/H_c. It keeps the residual exponent lambda-kappa at a content prime; none is discarded. Thus the adapter is valid even with empty relative-fresh M_rel.

Outside content the factor choice agrees with140's n_j. At an original139 relative-fresh p^lambda||m_i, its unique target remains F_i and m_i|q_i. Content primes can occur in two F factors, and no unit/exact-depth assertion is imported there from the fresh theorem. No identification of q_0 with a Gaussian all-same core is made without that route's coefficient/content adapter.

## 3. Same-height integral receiver and a large square divisor
Define signed integers zeta_j=F_j/q_j^2. They are nonzero; zeta_0 is positive. With exact R=H_c*tau,
 0<zeta_0<=6H_c^2(tau/q_0)^2,
 0<|zeta_i|<=4H_c^2(tau/q_i)^2 (i=1,2,3).
Since the q_j are odd, zeta_0=3 mod8 and zeta_i=1 mod8. A further retained global necessity is
 H_c^2 | product_(j=0..3)zeta_j,
obtained by dividing139's R^2|product F_j by tau^2. The other signed minus-square and monic139 conditions are still required; divisibility alone is not a physical converse.

At least one q_j>=tau^(1/4), so one of the four actual physical quadratic forms has an integer square divisor at least tau^(1/2). Its corresponding |zeta_j| is at most6H_c^2*tau^(3/2). This large-square-divisor alternative applies to full tau, with explicit content constants, and is not restricted to fresh support. It is a necessary same-R receiver, not a counting theorem.

For fixed A,R the allocation is canonical, so enlarging the tuple does not multiply endpoint counts. Counting arbitrary tuples A,q,zeta or arbitrary roots instead of realized endpoints requires all original masks plus139 signed integer reconstruction.138 uniform at-most8 physical inverse remains, and that fixed fiber is already consumed.

## 4. What is new, and what remains unproved
New: precise pair-content gcd bounds supply a complete integer tau adapter through content-supported prime powers; the large Heron square-divisor event therefore has no small-fresh-support escape at the level of this necessary cover.
Retained, not newly credited: primitive content formulas, generic R^2 divisor, root-line destination on fresh support, old four Gaussian core dichotomies and fixed-fiber bounds. The new integer receiver is not automatically theorem-equivalent to the older Gaussian inverse-fraction receiver; both keep their own original height/coefficient masks.

The cover does not prove enough scarcity of realized A for a fixed-power saving. The enlarged quadratic square-divisor event can have many nonphysical solutions. No independence, density multiplication, hidden B-uniform H_c constant, or automatic quantitative factor separation is asserted.140 full-factor saturation remains impossible at R, but q_j=tau can still occur when H_c>1; do not replace R by tau in that exclusion.

## Verification and audit
Python PASS:3931 primitive odd-vector triple-gcd checks;9606 abstract R^2-divisor covers, including8346 nontrivial-content cases and1905 with both H_c>1 and tau>1;1488 signed primitive zero-edge boundary adapters. Abstract vectors are algebraic enlargements, not asserted endpoints or original packet witnesses. Boundary examples test the content allocation only; they do not reinstate140 saturation on positive endpoints. Positive physical endpoints enumerated=0.
Symbolic replay {0,0,0,0} checks the four difference/sum identities used by the content bounds. Proof establishes arbitrary prime powers and exact quantifiers; finite tests support replay. Within-session audit explicitly checked the distinction between R_nc and R/H_c, maximum-depth/tie allocation, cases lambda=kappa, partial remaining powers, signed quotients, and all retained physical-converse firewalls. Not external auditing.

## Handoff
M3-T11-142: seek a uniform nonlocal count on REALIZED primitive physical plus-vectors with this content-complete quadratic square-divisor cover, exact R=H_c*tau<=B,139 signed lift/monic relation and all original packet masks. Small/empty relative-fresh support no longer avoids this necessary Heron event, but counting it still needs a new theorem. Compare any proposed estimate to the existing primary/hard one-twelfth budget before charging credit. Physical zero Heron retired; no single full-R saturation retained; TI parked;120 retracted; global credit0 and gateOPEN.

