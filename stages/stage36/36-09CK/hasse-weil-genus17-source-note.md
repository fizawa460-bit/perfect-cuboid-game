# 36-09CK Hasse-Weil and local-reduction source lock for the good-prime cover

Scope: this note supplies only the standard point-count and good-reduction facts used for the Stage36 good-prime local calculation. It does not supply global rational-point, Jacobian-rank, Selmer, BSD, H1, receiver-closure, or endpoint credit.

External sources:
- Stacks Project, Section 64.32, “Counting points”, https://stacks.math.columbia.edu/tag/03W2
- Stacks Project, Lemma 29.43.1, valuative criterion for properness, https://stacks.math.columbia.edu/tag/0BX5
- Stacks Project, Section 59.32, “Henselian rings”, including Hensel lifting of simple roots over Z_p, https://stacks.math.columbia.edu/tag/03QD

Stage36 application to an odd good prime q not dividing 2*P*M*D0*Q*A*B*C*D:
- Put L=lambda^2=P^2/M^2 mod q. Then L is nonzero and L is not +/-1 because
  P^2-M^2=8D0 and P^2+M^2=2Q^2.
- After the usual y=(B/A)t^2 normalization, the five square conditions have squareclass targets
  (d,k,r,kd,rd)
  on the five linear factors
  (y,1-y,1+y,1-Ly,1+Ly),
  where d=chi_q(AB), k=chi_q(kappa*A), r=chi_q(rho*A).
- The six geometric branch points are
  y=0,1,-1,L^{-1},-L^{-1},infinity.
- The five function squareclasses are geometrically independent: each finite linear factor has a unique finite zero not shared by the others. Hence the normalization is a connected degree-32 (Z/2)^5-cover of P^1.
- Each of the six branch points has inertia order 2. Riemann-Hurwitz gives
  2g-2 = 32*(-2) + 6*(32/2) = 32,
  so g=17.

Exact F_q-point criterion at a good prime:
- For a finite residue y not equal to a branch point, a point exists above y iff the five nonzero linear factors have characters exactly (d,k,r,kd,rd).
- At one of the five finite branch residues, exactly one factor is zero. The ramified square root imposes no residue-character condition on that vanishing factor; the other four nonzero factors must have their prescribed characters. Equivalently, in the finite residue scan, zero is accepted for the unique vanishing factor.
- At infinity, divide the last four square equations by the first. Since L is a square mod q, a rational point above infinity exists iff
  d=+1, k=chi_q(-1), r=+1.
- These finite-branch and infinity cases exhaust the smooth projective normalization over F_q.

Passage between F_q and Q_q:
- The good-prime normalization is smooth and proper over Z_q. Therefore any Q_q-point extends over Z_q by properness and reduces to an F_q-point.
- Conversely every F_q-point on the smooth special fibre lifts to a Q_q-point by Hensel/smooth lifting.
- Hence, for this good-prime model, the exact finite residue/branch/infinity criterion is equivalent to Q_q-local solubility. In particular, absence of every listed F_q point is a genuine Q_q obstruction, not merely an affine residue-search failure.

Large-good-prime automatic range:
- For a smooth geometrically irreducible projective curve X/F_q of genus g, the Weil estimate gives
  |#X(F_q) - (q+1)| <= 2 g sqrt(q).
- Here #X(F_q) >= q+1-34*sqrt(q). For every prime q>=1163 this lower bound is positive, so the good-prime cover has an F_q-point and therefore a Q_q-point.
- Because the removed receiver-open divisor is finite on the curve, a q-adic neighborhood of a smooth local point contains points off that divisor as well; this does not create a global receiver or rational-point claim.

Thus only odd good primes q<1163 require exact finite checking in the 36-09CK verifier.