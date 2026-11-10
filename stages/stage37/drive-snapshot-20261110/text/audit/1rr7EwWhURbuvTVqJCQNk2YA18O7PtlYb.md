# Stage37 in-session adversarial audit — M3-PESCH-TI-003

VERDICT=PASS_EXACT_CERTIFIER_AND_TWO_FINITE_CLOSED_FIBERS
This is an in-session verification, not an independently staffed external audit.
NO_INFINITY_OR_DENSITY_CREDIT=true
GLOBAL_SAVING=false
1072_AGGREGATE=HOLD

1. The E3 model comes from TI-002's birational identity. The new E' is two-isogenous, so ranks agree; its different torsion group is not confused with E3 torsion. Both descent images are checked. PASS.
2. Candidate sets include signed squarefree support correctly. E uses positive divisors of U after the real obstruction. E' includes both signs and every prime dividing 2VW, including primes of even exponent. Exceptional O/(0,0) class 1 retained. PASS.
3. Covers require coprime z,t; all rational points yield integral cover solutions. Testing primitive pairs modulo prime powers gives SOUND rejection only. Surviving covers remain UNKNOWN, not declared soluble. PASS.
4. Chart enumeration is complete by unit scaling. Independent verifier instead enumerates every primitive pair for 22 witnesses; all obstructions hold. No random or partial sampling. PASS.
5. Four known E' classes are supplied by explicit rational points; VW nonsquare makes them distinct. Product of image sizes 1*4 and the standard descent formula certify rank zero for (4,1),(9,4). Torsion FOUR is checked on E3 by good reduction at 7, not transferred from E'. PASS.
6. The producer covered 31 primitive sources with m<=12; exactly 2 certificates passed and 29 remained UNKNOWN. No rank inference from failure, no 2/31 density statement, no claim these are new fibers relative to external lists. PASS.
7. Weighted receiver uses exact physical mu_B and restores the joint C,C term: M3-2F(C)+R_CC. Coincident sources counted once, independence not assumed. Weights not actually evaluated, no saving credit. PASS.
8. The generic sufficient membership test is not promoted to an infinite rank-zero arithmetic family or a weighted family theorem. Next work must extract family conditions and weights rather than silently replace that obligation with larger finite tables. All gate/limit flags stay false; 1072 HOLD. PASS.

Reproduce: python ti003_descent.py; python audit_ti003.py, with the saved certificate JSON. Producer returns [(4,1),(9,4)]; independent replay returns 22 obstruction proofs and exact dual point/torsion checks PASS.
