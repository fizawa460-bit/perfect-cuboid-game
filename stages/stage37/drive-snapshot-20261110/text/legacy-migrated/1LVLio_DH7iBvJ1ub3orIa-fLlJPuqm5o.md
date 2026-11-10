# M3-T11-143 — Synchronized quadratic-square lift on affine plus families

STATUS=PROVED_EXACT_AFFINE_LIFT_RECEIVER_AND_FULL_AP_NO_GO
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-144 SynchronizedMovingLiftSupportWithCoefficientHeightControl

Authority: current MAIN / INDEX / RESULT-LEDGER / active ROUTE all point to142. Read142 and its audit; use139 signed integral lift,138 physical height,141 content-complete cover. Ledger semantic check distinguishes this from M3-LIN-NEG-001 (historical Master relation/genus-one ansatz) and rational-surface domination no-go. Neither is reopened. No full-history reread.

## 1. Exact synchronized nonlocal receiver

On a fixed integer affine candidate family write R(n)=r*n+s and A_i(n)=a_i*n+b_i. Restrict to R>0 and the original physical height/packet mask. Define
 alpha_i=2*r^2-a_i^2,
 beta_i=4*r*s-2*a_i*b_i,
 gamma_i=2*s^2-b_i^2,
 Q_i(n)=alpha_i*n^2+beta_i*n+gamma_i.
The139 unsigned minus lift requires integer Y_i with Y_i^2=Q_i(n). Its discriminant is exactly
 Delta_i=beta_i^2-4*alpha_i*gamma_i=8*(r*b_i-s*a_i)^2.
If alpha_i!=0 this is equivalent to
 X_i^2-alpha_i*W_i^2=Delta_i,
 X_i=2*alpha_i*n+beta_i, W_i=2*Y_i.
Conversely impose W_i even, X_i=beta_i mod2*alpha_i, and THE SAME integer n=(X_i-beta_i)/(2*alpha_i) for all i; these recover precisely the three original integer-square tests. This is a synchronized generalized Pell-type receiver, not three independent densities. If alpha_i is a positive square the equation factors over Q and can be treated by exact divisor pairs; if negative it is a definite norm equation. alpha_i=0 retains the original linear equation Y_i^2=beta_i*n+gamma_i rather than dividing by zero. For integer r!=0, alpha_i=0 is impossible because a_i^2=2r^2 has no nonzero integer solution.

For the full139 lift keep signed Y_i and impose
 sum_i A_i(n)*Y_i=-R(n)^2,
 e_i=(A_i+Y_i)/2>0,
 primitive plus/content/canonical/original T11 orientation and cyclic coefficient masks.
The equations alone do not certify those original masks. The Pell receiver does not replace them and does not yield a global count.

142's second coordinate gives alpha=542,beta=-36,gamma=-9,Delta=20808=8*51^2, hence X=1084*n-36,W=2Y and X^2-542W^2=20808. The retained mod3 certificate already makes its prescribed AP empty. This rewrite is not new credit for excluding142, nor a new leading-character sieve.

## 2. Exact polynomial-lift obstruction

For r!=0 and one coordinate, Q_i(n) can be a square polynomial over R only if its discriminant vanishes, hence r*b_i=s*a_i. Conversely this proportionality gives Q_i=(2-(a_i/r)^2)*R^2; it is a real polynomial square precisely when the scalar is nonnegative. All three real linear minus lifts therefore force every A_i proportional to R, so [A_1:A_2:A_3] is constant wherever R!=0.
Equivalent geometry: the real projective cover A_i^2+Y_i^2=2R^2 for all i has no nonconstant real projective line. For each i, the coefficient vectors (A_i,Y_i) have Gram matrix 2*(r,s)^T*(r,s) and therefore rank<=1; both coordinates are proportional to R. This uses the unsigned square cover already, not the signed sum. It is a lift-line theorem, NOT a theorem that the projected plus variety contains no lines. A projected line can lift nonlinearly; no such exclusion is claimed.
If R is a positive constant, nonconstant linear A_i eventually violates Q_i>=0; the polynomial-square identity also forces each A_i constant. Radial families can satisfy unsigned squares and still fail signed sum/positivity; they are not newly found physical endpoints.

## 3. No entire unbounded AP of moving affine candidates passes the minus lift

Suppose on n=n0+h*k (h>0), ALL sufficiently large integer k have Q_i(n) integer squares for every i and R>0. For each coordinate let z_k=sqrt(Q_i(n0+h*k))>=0, an integer. A nonzero quadratic with positive leading coefficient has expansion z_k=c*k+d+O(1/k); its second differences tend to0. A degree-one positive polynomial has second differences tending to0 as well. Thus integer second differences are exactly0 eventually, so z_k is eventually linear in k. Infinitely many equalities then force the polynomial Q_i(n0+h*k) to equal that linear square identically. Constant or zero Q causes no exception; a negative leading term cannot have an unbounded nonnegative tail. By section2, all A_i/R are constant (or the constant-R family itself is constant).
Therefore no projectively moving integer affine family can pass the complete minus-square tests on an entire unbounded AP tail. This strengthens the polynomial ansatz firewall to integer square roots that were not assumed affine beforehand.

IMPORTANT LIMIT: infinitely many sparse n may still survive nonsquare quadratics. Excluding a complete AP does NOT prove zero density, sublinear support, a fixed power saving, bounded occupancy, or finiteness. No uniform Pell estimate or sum over moving affine coefficients is proved. Arbitrary points can be placed on arbitrary affine lines, so this theorem is not an automatic decomposition/count of the physical population. The primary receiver still requires A_1,1(B)<<B^(1/3-eta) on exact physical measure; no exponent gain is promoted.

## Verification and adversarial audit

Two symbolic identities vanish: Delta_i=8*(r*b_i-s*a_i)^2 and the Pell residual equals4*alpha_i*(Q_i-Y_i^2). Exact integer replay:5831 abstract affine coefficient packets /23324 evaluations;142's1000 AP members retain the mod3 failure. A radial unsigned boundary test verifies that unsigned lifting is not the signed physical converse. No positive physical endpoints enumerated.
Within-session audit checked alpha=0, constant R, zero/constant/linear quadratic cases, negative radicands, nonsquare positive leading terms, eventual integer second differences, square-polynomial implication, signed branch retention, projected-versus-lifted lines, and missing original packet masks. This is not external audit. Finite replay validates algebra only; the AP obstruction is proved by the argument above.

## Handoff

144 must confront sparse synchronized integral lifts and moving coefficients with exact R/content/packet masks. A count of fixed affine families needs a justified cover of realized support, multiplicity control, coefficient-height bounds and a summable estimate before any credit. Do not infer global sparsity from the full-AP no-go or count independent Pell equations. Alternatively return to the full139 signed lift with a genuinely nonlocal support theorem.142 bare-cover Omega(B) obstruction,141 necessity,140 properness,138 eight-fiber adapter,120 retraction and TI parking remain in force. GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false.
