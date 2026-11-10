# M3-T11-121 — Phi evaluation/root difference: resultant support and denominator firewall

STATUS=PROVED_EXACT_STRUCTURE / WITHIN_SESSION_HOSTILE_AUDIT_PASS / NO_GLOBAL_POWER_SAVING
TYPE=GLOBAL_LINEAR_CUBIC_FACTOR_SUPPORT / NORMALIZATION_FIREWALL
POPULATION=Existing nondegenerate exact fixed-packet physical Stage37 endpoints with R<=B, restricted to the audited phi/1+3 image; one endpoint per count. No new population or height cutoff is introduced.
DEPENDENCIES=Audited 105 physical negative-square norm; 106 z_phys=S/2; 109/110 phi parameterization and root; 099/100 interior denominator depth; 120 correction. Audited 036 is used only for the already-known fixed-u counting comparison.
DUPLICATE_PREFLIGHT=Targeted current RESULT-LEDGER, active ROUTE, RESEARCH-INDEX, NEGATIVE-REGISTER and CARD-INDEX checks found the 120 correction's open difference/cubic correlation but no explicit homogeneous linear/cubic resultant or integer-difference support theorem below. This is not another fixed-u multiplicity theorem, local density factor, or replacement for 119.
ALIASES=PhiIntegerDifferenceTwistSupport; PhiLinearCubicResultant; PhiDifferenceDenominatorFirewall.

## 1. Exact integral factorization

Write primitive phi parameters r,s, and put
Q0=r^2+s^2,
Q1=r^2-4rs+5s^2,
N=r^2-2rs-s^2,
K=r^2+2rs-s^2,
U=-2s(r-s)N,
V=r^4-6r^3s+12r^2s^2-14rs^3+11s^4.
The physical branch has finite nonzero u=U/V. U^2+V^2=Q0*Q1^3; vartheta=N/Q0.

Define P(z)=V^2 Q_u(z). Exactly
P(z)=(Q0*z-N)*D(z),
where D(z)=d3*z^3+d2*z^2+d1*z+d0, with integer homogeneous coefficients
d3=Q1^3,
d2=N*(r^4+4r^3s-50r^2s^2+100rs^3-51s^4),
d1=4s(r-s)*(3r^4-17r^3s+35r^2s^2-41rs^3+32s^4),
d0=4s^2(r-s)^2*N.
The cubic D is not the conductor C_u. Its monic version is D/Q1^3.

The exact linear/cubic resultant is
Res_z(Q0*z-N,D(z))=2*Q1^2*N*K^3.
Equivalently,
Q0^3*D(N/Q0)=2*Q1^2*N*K^3.
For a nonzero rational parameter pair, Q0,Q1>0 and N,K are nonzero: their roots in r/s involve sqrt(2), and the infinity value is nonzero. Thus the factors never share a rational root here.

## 2. Integer evaluation support theorem

Let the actual evaluation point be z_phys=a/b=S/2 in lowest terms, b>0 and gcd(a,b)=1. These a,b are evaluation numerator/denominator, not the reduced numerator/denominator of u.
Set
L=Q0*a-N*b,
D_h=d3*a^3+d2*a^2*b+d1*a*b^2+d0*b^3.
The physical negative-square norm gives
L*D_h/(Q0*Q1^3*b^4)=-w^2,
so L*D_h=-Q0*Q1^3*(b^2*w)^2 with b^2*w rational.
Both factors are nonzero on the retained distinct-root physical locus. In particular L is not forced to vanish.

Let delta be the signed squarefree integer representative of L: L=delta*y^2 with y a positive integer. Then
rad(|delta|) divides rad(2*Q0*Q1*N*K).

Proof: take p not dividing 2Q0Q1NK. If p divides b, Q0*a is a unit modulo p, so p does not divide L. Otherwise a/b is defined modulo p. If both L and D_h vanished modulo p, N/Q0 would be a root of D modulo p, contradicting the nonzero resultant. Hence p|L implies p does not divide D_h. The displayed negative-square relation then forces v_p(L) even. This proves the support statement for all such primes, without a local-probability assumption. Bad primes are retained rather than divided away.

With H=max(|r|,|s|)>=1,
|delta|<=|2Q0Q1NK|<=640H^8.
For each fixed parameter pair there are at most 2^(omega(2Q0Q1NK)+1) signed delta labels; in the retained polynomial physical height range this is B^o(1). This is a support theorem, not a count of moving parameter pairs or a new endpoint saving.

## 3. Actual rational difference keeps the denominator

The true difference is
z_phys-vartheta=L/(Q0*b).
In Q^*/Q^{*2}, exactly
[z_phys-vartheta]=[delta*Q0*b].
Consequently the integer delta support theorem does NOT bound the rational linear etale component solely by 2Q0Q1NK. Odd-valuation primes of the moving evaluation denominator b can enter that component. They cannot be silently discarded or replaced by the phi parameter height.

For clarity, fixed (r,s) already fixes u and audited 036 already supplies B^o(1) physical endpoints. The B^o(1) number of delta labels at fixed (r,s) is therefore not a second saving. A fixed delta across varying (r,s) has no uniform B^o(1) endpoint theorem here.

## 4. Interior allocation consistency check

For a relative-fresh interior p^lambda, 0<c_p<2lambda, audited 099/100 and 106 give v_p(b)=k=2lambda-c_p, v_p(a)=0, and norm depth n=2lambda+c_p.
On Q0 allocation, v_p(Q0)=n>k and N is a unit, hence v_p(L)=k. Thus v_p(delta) mod 2=c_p mod 2. The rational difference has valuation k-n-k=-n, agreeing with the canonical negative-valuation root comparison.
On Q1 allocation, Q0,N are units and b is p-divisible, hence L is a unit. Thus p does not divide delta. But the rational difference has valuation -k, with parity c_p. The denominator restores exactly the local class that would be lost by using delta alone.
These checks recover the old local tuple; neither allocation supplies independent rarity. No statement is made here about endpoint occupancy at these primes, extreme-only support, or the withdrawn 120 valuation equalities.

## 5. Continuation and credit boundary

The valid global correlation problem now has explicit integral coordinates:
L=delta*y^2,
L*D_h=-Q0*Q1^3*(b^2*w)^2,
supp(delta) subset supp(2Q0Q1NK),
actual linear class=[delta Q0 b].
A useful next theorem must control moving (r,s), delta and evaluation denominator b jointly on the same physical R<=B measure, or produce a genuine cross-invariant constraint not implied by the existing norm and primewise tuple. In particular it must cover the full residual outside 119's height/conductor windows, including high-height shells. A mere sum over divisor-many delta values per fixed parameter adds no exponent credit.

DO_NOT_REPEAT=Do not identify evaluation and root; do not confuse integer L with rational z-vartheta; do not drop b from its squareclass; do not call the resultant support a fixed-d endpoint theorem; do not multiply it into 119 or charge the interior Q0/Q1 parity check as density; do not infer phi emptiness from bounded no-hit tests.
REOPEN_CONDITION=An exact factorization/resultant or the physical negative-square/depth adapter fails, or a proved same-measure joint moving-parameter/denominator theorem gives a new quantitative receiver.
NEXT_LEGAL_ACTION=Test whether the simultaneous two-factor twist equations plus the exact physical denominator/conductor representation impose a genuinely new global joint-support bound. If they only reproduce the consumed norm tuple, park this receiver and pivot to nonlocal S4/theta!=0.
AUDIT_MODE=Within-session adversarial rederivation and two computational implementations, not a separately staffed external review.
VERIFICATION=Wolfram exact homogeneous factorization and resultant; independent Python integer coefficient arithmetic verified the complete factorization, resultant evaluation identity and Gaussian norm identity. Bounded primitive evaluation checks verified factorization and common-factor support. The bounded negative-square search found no nonzero cases and receives no existence, emptiness or counting credit; the theorem rests on the exact identities and valuation proof.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
