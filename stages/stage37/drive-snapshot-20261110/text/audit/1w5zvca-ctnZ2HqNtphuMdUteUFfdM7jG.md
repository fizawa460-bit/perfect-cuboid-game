M3-T11-112 — HOSTILE AUDIT
VERDICT=PASS
SCOPE=Fixed-conductor deterministic upper bound only; no global saving.
TARGET=Card file 16RuTNZyatx6ljzh_1z5m828aBTJ6CcaM; ROUTE section 128; RESULT-LEDGER 112.
METHOD=Independent derivation within this session plus deterministic stress tests; no separate external auditor is claimed.

A. Primitive lattice lemma. A Gauss-reduced basis b1,b2 has angle bounded away from 0, and |b1||b2| is comparable to determinant L. Inverting the basis gives |m|<=K H/|b1| and |n|<=K H/|b2|. Z^2-primitivity implies gcd(m,n)=1. The n=0 line contributes at most two vectors. If n!=0 occurs, H/|b2|>=1/K, and hence H/|b1|>=1/K. The rectangular count is then O(H^2/(|b1||b2|))=O(H^2/L). This proves the bound uniformly even in arbitrarily thin lattices. Necessity, not sufficiency, of lattice-coordinate primitivity is used.

B. CRT. For each selected projective root line modulo p^n, a primitive covector defines it. CRT glues covectors into a surjection Z^2 -> Z/L; its kernel has exact index L. Infinity-chart roots are retained. Two Gaussian orientations and two pullback roots per prime give at most 4^omega(M) choices, not independent density factors.

C. Physical pushforward. Every counted endpoint admits one primitive parameter in the counted set. Each parameter maps to one u; audited 036 bounds physical multiplicity over that u by B^o(1). Noninjectivity of psi only enlarges the upper bound. Exact R<=B remains a post-filter, and no change of measure occurs.

D. Boundary cases. For c_p=2lambda use the capped depth 4lambda supplied by corrected 111. For M=1 the lattice is Z^2 and the bound is O(H^2+1). Zero or excluded u-values can be discarded monotonically. H>=1 and polynomial physical range are necessary for absorbing 4^omega(M) into B^o(1).

E. Moving-modulus clause. Summing fixed-conductor bounds gives the stated union upper bound, including +1. The one-twelfth sufficient criterion requires a fixed exponent margin so the B^o(1) factor can be absorbed; it is not an established occupancy estimate.

VERIFICATION=Congruence lattices with L=1..150, six primitive covectors per L, H in {1,2,4,8,16}; maximum count/(H^2/L+1) was 4. Exact proof A, not this finite check, supplies the theorem.
PROMOTION=112 fixed-conductor upper bound B^o(1)(H^2/(M_rel^2*C_u)+1).
FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
