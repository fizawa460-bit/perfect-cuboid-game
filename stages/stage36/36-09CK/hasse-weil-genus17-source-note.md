# 36-09CK Hasse-Weil source lock for the good-prime cover

Scope: this note supplies only the standard point-count bound used for the Stage36 good-prime local calculation. It does not supply global rational-point, Jacobian-rank, Selmer, BSD, or receiver-closure credit.

External source:
- Stacks Project, Section 64.32, “Counting points”, https://stacks.math.columbia.edu/tag/03W2
- For a smooth geometrically irreducible projective curve X/F_q of genus g, the Weil/Riemann-hypothesis estimate gives
  |#X(F_q) - (q+1)| <= 2 g sqrt(q).

Stage36 application to an odd good prime q not dividing P*M*D0*Q:
- Put L=lambda^2=P^2/M^2 mod q. Then L is nonzero and L is not +/-1 because
  P^2-M^2=8D0 and P^2+M^2=2Q^2.
- After the usual y=(B/A)t^2 normalization, the five quadratic squareclass functions have branch divisors at
  y=0, y=1, y=-1, y=L^{-1}, y=-L^{-1}, and infinity.
- The five function squareclasses are geometrically independent: each finite linear factor has a unique finite zero not shared by the others. Hence the normalization is a connected degree-32 (Z/2)^5-cover of P^1.
- Each of the six branch points has inertia order 2. Riemann-Hurwitz therefore gives
  2g-2 = 32*(-2) + 6*(32/2) = 32,
  so g=17.
- Consequently #X(F_q) >= q+1-34*sqrt(q). For every prime q>=1163 this lower bound is positive, so the smooth projective good-reduction cover has an F_q-point. Hensel lifting on the smooth model yields a Q_q-point; because the removed receiver-open divisor is finite on the curve, a q-adic neighborhood of a smooth local point contains points off that divisor as well.

Small good primes q<1163 are not discharged by the numerical bound. They must be checked exactly by the finite residue/branch-neighborhood criterion in the 36-09CK verifier.
