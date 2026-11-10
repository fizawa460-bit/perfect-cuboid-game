M3-T11-111 — HOSTILE AUDIT
VERDICT=FAIL_AS_WRITTEN / PASS_AFTER_SCOPE_CORRECTION
SCOPE=Exact structure only; no independent saving.
TARGET=ROUTE section 127; RESULT-LEDGER M3-T11-111; audited dependencies 035/036/041/043/106/107/109.
METHOD=Separate algebraic derivation and deterministic projective-root checks; no external independent reviewer is claimed.

1. Odd cancellation. Put N=r^2-2rs-s^2, Q0=r^2+s^2. Modulo Q0, N=-2s(r+s). Thus Res(N,Q0)=4s^2*Res(Q0,r+s)=8s^4. At an odd prime, a common divisor of N,Q0 would force p|s and then p|r, contradicting primitivity.

2. The prime 5. The exact conic identity is
2Q0^2-N^2=(r^2+2rs-s^2)^2.
If v5(u)>=0 then y^2=2-25u^2 reduces to the nonsquare 2 modulo 5. Hence v5(u)<0. In reduced u=a/b, 5|b and 5 does not divide a or a^2+b^2. Independently N has no primitive projective zero modulo 5, since its discriminant 8 is nonsquare and the infinity value is 1.

3. Valuation transfer. For p|a^2+b^2, p does not divide b; p=5 is already excluded. Also p does not divide Q0: otherwise p|N, contradicting (1). Thus reducing N/(5Q0) loses no such odd p, and rho=a/b modulo p^n legitimately gives N-5rho Q0=0.

4. Discriminant and support. F_rho=(1-5rho)r^2-2rs+(-1-5rho)s^2 has discriminant 8-100rho^2=108 modulo p^n. A fresh p is odd and splits in Q(i); p=3 is therefore absent. Nontrivial projective isotropy implies (3/p)=1. Combining with p=1 modulo 4 gives p=1 modulo 12. This holds for every odd reduced norm support prime, and therefore for relative-fresh support.

5. Exact depth and charts. Over Z/p^n, 108 is a unit square. Two distinct simple projective roots modulo p lift uniquely to depth n. A vanishing leading coefficient is handled in the infinity chart; p=13 must not be discarded. Each primitive physical parameter lies on one of the two lines, not simultaneously on both. For interior primes n=2lambda+c_p is exact. At c_p=2lambda the same expression is the capped depth 4lambda; the actual valuation may be larger. This distinction is inherited from the existing saturation identity and creates no false exact valuation claim.

6. Local A4. The decomposition group acts through A4 and fixes the canonical Q_p root from 106. Its image is contained in that point stabilizer C3, so the complementary cubic is cyclic irreducible or fully split, never 1+2. The local squareclass firewall in 107 is retained.

VERIFICATION=36 root systems for odd primes below 80 and depths 1,2 passed in both projective charts, including p=13. Primitive conic/reduction checks on [-50,50]^2 passed. Finite checks support, but do not replace, proofs (1)-(6).
CORRECTION=Original 111 overstated exact depth at c_p=2lambda. The corrected claim is n_cap=min(v_p(a^2+b^2),4lambda)=2lambda+c_p. Internal depth is exact; extreme depth is capped. The original formulation is superseded, not silently erased.
PROMOTION=Corrected 111 exact support/capped-root-line/A4 router only.
FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
