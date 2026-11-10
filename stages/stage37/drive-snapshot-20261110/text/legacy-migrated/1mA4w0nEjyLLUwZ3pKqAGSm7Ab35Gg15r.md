# M3-T11-144 — Explicit logarithmic occupancy of a fixed affine minus-lift family

STATUS=PROVED_FIXED_AFFINE_FAMILY_LOGARITHMIC_COUNT_WITH_EXPLICIT_COEFFICIENT_WEIGHT
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-145 WeightedAffineCoverExistenceOrDirectSignedSupportCount

Authority: fresh MAIN / INDEX / RESULT-LEDGER / active ROUTE all143; standalone143 and audit read.139 supplies the signed physical lift;138 supplies actual plus coordinates and exact R.142 bare Heron counterfamily and141 content-complete necessity retained. Ledger/route semantic search found no prior determinant-gap fixed-affine count. This strengthens143's all-AP obstruction; it does not reopen old Master linear ansatz or count the bare Heron cover.

## 1. Integer determinant gives a gap without any Pell orbit theorem

Let d and D be positive integers. Consider distinct integer solutions x>0,w>=0 of
 x^2-d*w^2=D.
Set z=x+sqrt(d)*w, so z>=sqrt(D), and x=(z+D/z)/2, w=(z-D/z)/(2sqrt(d)). For two solutions with z2>z1,
 J=x1*w2-x2*w1
   =D/(2sqrt(d))*(z2/z1-z1/z2)>0.
Since J is a positive INTEGER, J>=1. Consequently
 log(z2/z1)>=g(d,D):=arsinh(sqrt(d)/D)>0.
This holds for ALL solutions together, including different norm orbits and square d. No fundamental-unit computation, unit-group theorem, local density or independent-Pell assumption is used.
If x<=U and U>=sqrt(D), then z<=2U. Ordering all solutions therefore gives
 #solutions <=1+log(2U/sqrt(D))/g(d,D).
If U<sqrt(D), there are none. w=0 is included. The exact identity
 (x1*x2-d*w1*w2)^2-d*J^2=D^2
is an independent algebraic check of the same gap.

## 2. Apply to143 with the ACTUAL physical height

Fix integer coefficients R(n)=r*n+s,A_i(n)=a_i*n+b_i. Count distinct integer n with 0<R(n)<=B and ALL three integer minus-square tests, then any additional signed/content/packet filters. Suppose r!=0 and choose any coordinate with k=r*b-s*a!=0. Put
 d=2*r^2-a^2 !=0,
 beta=4*r*s-2*a*b,
 D=8*k^2>0,
 X=2*d*n+beta, W=2*abs(Y), Y^2=2R^2-A^2.
143 gives X^2-dW^2=D. Moreover the exact height identity is
 r*X=2*d*R-2*a*k.

For d>0 take
 U=(2*d*B+2*abs(a*k))/abs(r).
Map each n to (abs(X),W); each norm point has at most TWO preimages because X is a nonconstant linear function of n. Thus
 N_line(B)<=2*(1+log(2U/sqrt(D))/arsinh(sqrt(d)/D))
when U>=sqrt(D), and N_line(B)=0 otherwise.
This is O_(fixed coefficients)(log(2B)), already using ONE compulsory coordinate. The same n, the other squares,139 signed sum, positivity, and original T11 masks can only reduce this upper bound; no multiplication of three densities is allowed.

For d<0 the exact equation X^2+abs(d)*W^2=D implies abs(X)<=sqrt(D). The allowed n lie in an interval of length sqrt(D)/abs(d), hence
 N_line(B)<=1+floor(sqrt(D)/abs(d)),
independent of B. The integer d=0 case cannot occur for r!=0. Negative X and either sign of Y are covered; no assumption that n itself is positive is made.

## 3. Degenerate coefficient families and primitive candidates

If r!=0 and k_i=0 for all three coordinates, then A_i/R=a_i/r is constant. Let g=gcd(a_1,a_2,a_3)>0 and a_i=g*v_i with primitive integer vector v. Integer A=(Rg/r)*v forces Rg/r integer. Primitive A then forces abs(Rg/r)=1. With R>0 there is at most ONE (A,R) candidate, if it exists. Count distinct candidates, not repeated parameter labels. If all a_i=0, all b_i=0 and primitive A is impossible.
If r=0, only s>0 can be physical. If some a_i!=0, the necessary bound abs(a_i*n+b_i)<=sqrt(2)*s confines n to length2sqrt(2)*s/abs(a_i), so at most1+floor(2sqrt(2)*s/abs(a_i)) values. If all a_i=0, the family is one constant candidate, whatever the number of parameter labels.
These cases prevent a radial or constant-family multiplicity leak. A nonconstant normalized plus direction always has some k_i!=0 when r!=0.

## 4. Explicit moving-coefficient cost and a CONDITIONAL cover receiver

Let L=max(1,abs(r),abs(s),abs(a_i),abs(b_i)). Then abs(k)<=2L^2,D<=32L^4,1<=d<=2L^2 in the indefinite case, and U<=4L^2*B+4L^3. Since arsinh(x)>=x/(1+x),
 1/g(d,D)<=1+D/sqrt(d)<=1+32L^4.
The preceding formula gives the coarse uniform bound
 N_line(B)<=2+2*(1+32L^4)*log(8L^2*(B+L)).
The definite/constant-R/primitive-radial bounds are also absorbed by O(L^4*log(2L*(B+L))). The sharper d,D,U formula should be retained whenever it matters. The constant depends on explicit coefficients; there is no hidden content constant. All height statements concern integer139 A and the original exact R, not a proxy for R.

Suppose a FINITE, justified family list F_B covers every relevant original physical (A,R) pair in the retained138/139 chart with R<=B. For each pair there are at most8 signed Y triples, hence at most8 reconstructed canonical endpoints from139; original packet filters remain mandatory. A union upper bound gives
 E_chart(B) << sum_(ell in F_B) L_ell^4*log(2L_ell*(B+L_ell)).
Bounded overlap is NOT needed for this sufficient upper bound: multiple covering simply overcounts. A canonical or disjoint cover would improve the estimate but is not an extra mathematical prerequisite. This corrects any interpretation of143's multiplicity-control handoff as requiring disjointness for a union upper bound. The per-pair sign bound is used once; do not multiply again by138's eight-fiber bound.

In particular, J(B) families of coefficient height<=L(B) give O(J(B)*L(B)^4*log(2L(B)*(B+L(B)))) as an UPPER bound if coverage is proved. If such a bound for the REQUIRED A_1,1 population is <<B^(1/3-epsilon) for fixed epsilon>0, with all other charts/retained branches covered, it would meet the primary P(B)<=B^o(1)*A_1,1(B) receiver after absorbing the subpower factor. This is an implication ONLY. No such family list, bound on J or L, or coverage of all charts is proved here.

Taking one arbitrary line per unknown endpoint is circular; choosing arbitrary coefficients of size B makes the L^4 cost useless. Fixed-line logarithmic scarcity cannot itself imply the global fixed power saving. The full global signed/original-packet realized support remains the blocker.

## Verification and within-session audit

PASS:3942 affine coefficient packets (1958 indefinite,1984 definite),899486 exact integer evaluations,3020 unsigned square hits; every count lies below its coefficient-specific bound. These are ONE-coordinate algebraic tests, not full physical points.722 norm sets and1586 consecutive gaps verify positive integer determinant, exact bilinear identity and the analytic gap bound; square and nonsquare d both included. Constant-R intervals and primitive radial repetition were checked separately. Physical endpoints enumerated0.
Adversarial rederivation checked determinant sign/nonzero, all norm orbits, w=0, both X signs, n-to-norm multiplicity<=2, actual R conversion, negative d, impossible d=0, primitive radial exception, r=0, coefficient dependence, sign-fiber count used once, and union-cover logic. Audit is within-session, not external. Numerical scans validate examples only; the infinite count theorem follows from the integer determinant argument.

## Handoff

145: fixed-affine occupancy is now quantitative, so do not repeat143's AP argument or merely search more leading characters. Either construct a genuinely economical coefficient-controlled cover of the ORIGINAL realized support and estimate its weighted sum, or abandon the affine-cover summation in favor of a direct139 signed nonlocal count. A cover construction must carry exact R, primitive A, content and original coefficient/orientation/cyclic masks; no bare Heron enlargement transfer. Global fixed power saving NOT proved; primary gate OPEN, GLOBAL_COUNTING_CREDIT=0, TI PARKED,120 retraction retained, all closure/limit/nonexistence flags false.
