# M3-T11-153 — Summed small-cofactor count with unrestricted moving primes

STATUS=PROVED_UNIFORM_MOVING_PRIME_SMALL_COFACTOR_COUNT
AUDIT_MODE=WITHIN_SESSION_PROOF_REDERIVATION_AND_EXACT_REPLAY_NOT_EXTERNAL
SECTOR_COUNTING_PROGRESS=true
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
CURRENT_ATTACK=BalancedResidualJointGaussianCount
NEXT=M3-T11-154 BalancedResidualJointGaussianCount

## Authority, population and the actual improvement

The live MAIN / INDEX / RESULT-LEDGER / active T11 ROUTE already designate152 as current authority.152 proves a negligible sector for ONE prescribed prime alphabet, but leaves the moving-prime complement unbounded.153 uses151's exact Gaussian valuation identity to SUM a different sector, allowing the exceptional prime to range over ALL split primes. No restriction on curve degree, genus, prime-support alphabet, or coefficient packet is introduced.

P(B) counts the original primitive canonical positive physical endpoints at exact R<=B. As in151, use positive integer edges e1,e2,e3, complementary face diagonals f1,f2,f3, gcd(e1,e2,e3)=1, ei^2+fi^2=R^2, and sum ei^2=R^2. Original canonical masks remain in force; dropping masks is used only for an upper bound. R is odd and all its primes split in Z[i]. One endpoint is one count, using the endpoint-to-edge-triple injection retained in151.

For B>=2 and 1<=Y<=B, let N(B,Y) count endpoints for which SOME prime power p^n exactly dividing R has complementary factor m=R/p^n<=Y. This is a union over all primes and all valuations, not a fixed-prime statement.

THEOREM:

 N(B,Y) <= 512 Y (1+log Y)^27 (1+log B).                 (153.1)

The constant512 is deliberately nonoptimal. Thus N(B,B^theta)<=B^(theta+o(1)) for any fixed0<theta<1. In particular theta<1/3 gives o(M3(B)) from retained M3(B)>>B^(1/3).

More sharply, put L=1+log B and Y_B=B^(1/3)/L^30. For sufficiently large B so Y_B>=1,

 N(B,Y_B) <= 512 B^(1/3)/L^2 = o(M3(B)).                 (153.2)

This counts moving primes and all their exponents at a nearly B^(1/3) complementary-factor threshold. It does NOT bound all endpoints or the entire complement of152.

## 1. Prime discovery from the cofactor witnesses

Fix an endpoint and a prime p^n exactly dividing R; put m=R/p^n. Choose one deterministic Gaussian prime pi above p. For each edge not divisible by p, independently change the sign of its complementary diagonal so that

 H_i=e_i+i f_i=bar(pi)^(2n) G_i,   Norm(G_i)=m^2.

These conjugations leave the positive edges unchanged. Let I={i:p does not divide e_i}; primitivity and the sphere equation give r=|I| in {2,3}. Write C=sum_(i in I)G_i^2.151 proves, directly from the exact sphere identity,

 C != 0,   pi^2 divides C,   Norm(C)<=r^2 m^4<=9m^4.    (153.3)

For completeness: the terms of sum H_i^2+sum bar(H_i)^2+2R^2=0 outside bar(pi)^(4n)C are all divisible by pi^2. If r=3 and C=0 the identity contradicts R>0; if r=2 and C=0 it reduces to4e_j^2=0 for the remaining edge. Positivity rules this out. Each |G_i^2|=m^2 gives the norm bound. No independence of prime orientations is assumed.

Crucially, for FIXED m,I,(G_i), the nonzero integer Norm(C) is already fixed BEFORE p is chosen. Every permissible p satisfies p^2|Norm(C), p>=5, and p does not divide m. There are at most

 log(9m^4)/(2 log5)

such distinct primes. The smaller Gaussian condition pi^2|C may safely be discarded for this upper bound. A fixed cofactor therefore pays O(log m) prime choices, even though the primes move globally. A bound p<=3m^2 alone would not have this property.

## 2. Reconstruction prevents an extra physical fiber cost

Let A(m)=#{G in Z[i]:Norm(G)=m^2}=4D(m), with D(m)=product_(q^a||m)(2a+1), for the split m that occur here. The witness count for fixed m is

 3A(m)^2+A(m)^3 <= 112 D(m)^3.                         (153.4)

The factor3 is the choice of the two-element set I. The three-element case has one I. Units and all Gaussian allocations are already included in A(m). Tuples with C=0 are discarded, since no positive endpoint maps to them.

Given m,I,(G_i),p,n, the chosen pi determines H_i=bar(pi)^(2n)G_i for i in I. Their real parts determine those edges. If r=3 all edges are known. If r=2 the remaining POSITIVE edge is uniquely determined, if it exists, by

 e_j=+sqrt(R^2-sum_(i in I)e_i^2).

Reject nonsquares, zero or negative edges, wrong p-divisibility, nonprimitive triples and failed face-diagonal/canonical masks. The remaining face diagonals are then fixed in the original sign convention. There is at most ONE original endpoint for this complete witness. No factor R^o(1), extra curve-family count, or uncontrolled inverse multiplicity is needed.

Each physical endpoint in N(B,Y) is encoded at least once. One can choose its least qualifying p to obtain a deterministic injection. The enumeration may contain several encodings of an endpoint, which is harmless in an upper bound. It is not necessary to charge the number of possible qualifying primes a second time.

For each fixed p and m, n>=1 and mp^n<=B allow at most log B/log5 choices. This explicitly sums all valuations, including the r=2 branch where151 did not bound p^n by3m^2.

## 3. Sum all complementary factors, with explicit logarithmic cost

Combining the preceding steps gives

 N(B,Y) <= [112/(2(log5)^2)] log B
             * sum_(m<=Y) D(m)^3 log(9m^4).             (153.5)

Extending the m-sum to all positive integers is safe. Let tau_27 be the27-fold divisor function. Locally,

 (2a+1)^3 <= binom(a+26,26), hence D(m)^3<=tau_27(m).

Proof of the local inequality: equality holds at a=0. The ratio comparison follows from

 (2a+1)^3(a+27)-(2a+3)^3(a+1)
 =184a^3+240a^2+82a >=0.

The elementary ordered-factor count gives

 sum_(m<=Y) tau_27(m)
 <= Y (sum_(a<=Y)1/a)^26 <= Y(1+log Y)^26.

Indeed, fix the first26 positive factors and bound the number of last factors by Y divided by their product; enlarging each of the26 sums to a<=Y is an upper bound. Since log(9m^4)<=4(1+log Y), (153.5) implies(153.1), with room in the displayed constant512. No prime number theorem, deep unit-equation theorem, probabilistic sieve, or hypothesis on the actual prime sizes is used in this summed estimate.

## 4. Exact new residual after combining152 and153

Keep152's prescribed S_B: the first floor((log B)^(4/3)) primes1 modulo4. Let E_small have supp(R) contained in S_B. Define E_peel to contain endpoints OUTSIDE E_small with some p^n||R and R/p^n<=Y_B. Define E_bal to contain the remaining endpoints. Then, on the original physical measure,

 E(B)=E_small disjoint-union E_peel disjoint-union E_bal,
 P_small(B)=o(M3(B)),
 P_peel(B)<=N(B,Y_B)=o(M3(B)).                         (153.6)

Thus P(B)/M3(B)->0 is equivalent to P_bal(B)/M3(B)->0. Every endpoint still requiring a bound has BOTH:

 (a) some prime divisor of R outside S_B;
 (b) R/p^v_p(R)>Y_B for EVERY prime p dividing R.

Equivalently, every full prime-power divisor is <R/Y_B. This is only a necessary support description of the unresolved mass. Do not confuse a bound involving B with a dyadic statement involving the actual R. The result counts actual endpoints in the removed sectors; it does not claim the surviving diagonal set has few integers.

On a dyadic top shell B/2<R<=B, the small-cofactor sector at Y_B cannot have r=3 for large B, since151 would force R<=3m^3<=3B/L^90. Nor can it have n=1, since p<=3m^2 gives the same contradiction. Thus the new top-shell count acts on the r=2, repeated-prime-power branch; do not market it as disposing of all large squarefree prime divisors. Both branches were correctly included in the uniform theorem.

## 5. Scope, dedupe and next task

151's marginal candidate construction 5^k*q allowed many q merely satisfying q<=3*5^(2k).153 instead requires the actual nonzero cofactor witness C and charges its prime divisors after fixing the witness. The new summed estimate therefore does not contradict151's candidate-support lower bound; most relaxed candidates may never pass this correlated witness condition.

Targeted current-ledger review: COMMON-001 and XD-001 are root-line/rectangle or fixed-physical-image estimates with a separate globalization gate.118/119 concern the audited phi/1+3 image and a moving conductor there. Stage14 charged-cofactor receivers have different fixed-U and projective-class populations.153 imports none of those estimates.151 supplies(153.3);153 adds the prime-discovery order, constant-fiber reconstruction and explicit sum(153.5) on ALL original endpoint types. No literature-wide novelty is claimed.

GLOBAL_COUNTING_CREDIT=0; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false. Sector progress is real but the balanced residual remains unbounded. TI stays parked;120 remains retracted;147–149 remain retained, and automatic curve-degree escalation stays paused.

Next154: obtain a summed bound for E_bal using the same joint Gaussian witnesses at more than one prime, with reconstruction and moving cofactor costs explicitly paid. An acceptable alternative is a different global arithmetic estimate on this exact residual. A claim that the cofactor inequalities alone are sparse, independent local probabilities, another fixed alphabet, or a repeated proof of153's small-cofactor tail does not qualify. Test the aggregate budget before pursuing a detailed classification. The target is now explicitly balanced residual mass, not all large primes indiscriminately.

## Replay and handoff repair

verify153.py / verification153.json replay the coefficient inequality, the exact witness-prime budget on finite Gaussian cofactor domains, exponent enumeration, and the positive-root reconstruction uniqueness. These checks exercise the counting steps; they are not a finite search used to assert perfect-cuboid nonexistence. The written proof supplies the uniform claim.

The152 authority head had reported its replay files as not located. Direct fetch now CONFIRMS verify152.py (1WBlzhBdvCA-oyMhNJC6V_JJHW4GMy1vM) and verification152.json (1Q1gCTytRlm6xCxROlIb4477ZbCyiwA7I). Both, and the152 card/audit, were downloaded and compared byte-for-byte with the saved final artifacts: all four matched. This repairs the handoff metadata without changing152's mathematical claims.
