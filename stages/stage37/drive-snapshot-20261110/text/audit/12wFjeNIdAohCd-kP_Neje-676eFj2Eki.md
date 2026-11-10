Stage37-HOSTILE-AUDIT-M3-T11-113-PASS
AUDITED_CARD=M3-T11-113
VERDICT=PASS / EXACT_SAME_MEASURE_THEOREM_ADAPTER / NO_GLOBAL_CLOSURE
AUDIT_MODE=Hostile rederivation and exact coefficient tests in this session; not a separately staffed or external audit.
POPULATION=Exact nondegenerate physical R<=B endpoints, one fixed content/coefficient packet, psi/A4 restriction.
SCOPE=Fixed canonical norm squareclass uniform B^o(1) fibers and joint low-parameter-height tail only.

1. Norm/reduction audit.
Re-expanded N^2+25Q0^2 to coefficient tuple (26,-4,52,4,26).
For primitive r,s, odd common divisors of N,Q0 force r^2+s^2=N=0, hence 2s(r+s)=0 and p=2. Mod5, the N quadratic discriminant 8 is nonsquare, excluding 5. For both odd r,s, Q0 and N have exact 2-valuation one; otherwise their gcd is one. Thus g=gcd(N,5Q0) is 1 or 2, reduced norm F/g^2 and sf(norm)=sf(F). This is independent of chosen psi preimage.

2. Smooth twist/Jacobian audit.
I=10864, J=2219776, 4I^3-J^2=201553920000.
E_d:y^2=x^3-293328d^2*x-59933952d^3
=(x-624d)(x+276d)(x+348d).
The roots are distinct and each root with y=0 is a rational exact-order-two point. Nonzero discriminant holds for every positive d.

3. Explicit map and uniform height, strengthening the original adapter.
Let f=F, define polynomial covariants
H_F=(f_rs^2-f_rr*f_ss)/3,
K_F=(f_s*(H_F)_r-f_r*(H_F)_s)/12.
Exact expansion:
H_F=-10768r^4-3328r^3s-21536r^2s^2+3328rs^3-10768s^4.
Exact degree-12 polynomial identity:
27*K_F^2=H_F^3-48I*f^2*H_F-64J*f^3.
For f=d*q^2 the covering has coordinates
x=3d*H_F/(4f), y=27*K_F/(8q^3).
The identity proves y^2=x^3-27d^2I*x-27d^3J. This is the binary-quartic 2-cover, a degree-four map (not degree two): geometrically P maps to [2P-D_infinity] in Pic^0. It requires no choice of a rational base point. F>0 on every nonzero real parameter pair, so these evaluated denominators never vanish on the counted rational parameter population, including s=0.
Since |H_F|<=49728 H^4 and F<=116H^4, naive x-height is at most 149184*d*H^4 before reduction, hence polynomial in B for d<=116H^4 and H<=B^A.
Thus the original unspecified covering-height claim is now supported by explicit formulas.

4. External theorem/threshold audit.
Dujella arXiv:2312.03655 Theorem 1.1 counts canonical height<=log T uniformly over fixed Q with prime torsion order 2, provided T>=exp(max(h(E),e)). Here h(E_d)=O(log d); explicit x-height and the paper's height comparison give canonical height O_A(log B). A fixed enlarged T=B^K_A satisfies both thresholds. Hence the uniform fiber count is exp(O_A(log B/log log B))=B^o(1).
Fisher-Sills arXiv:1103.4944, introduction and Lemma 3.1, supplies the binary-quartic covering convention. Their invariant scale c4=16I,c6=32J gives a short model rationally isomorphic to ours by fixed scaling; this is not a twist or a variable field extension.
Source URLs: https://arxiv.org/pdf/2312.03655 ; https://arxiv.org/pdf/1103.4944 .

5. Measure and tail audit.
A degree-four map has at most four geometric preimages per elliptic point, hence bounded parameter multiplicity. Audited 036 supplies uniform fixed-u physical B^o(1) multiplicity. Composing gives B^o(1) physical endpoints per canonical d, with no independent saving product.
M_rel^2 divides the reduced norm and F. Therefore d=sf(F/M_rel^2)<=116H^4/M0^2 for every counted M_rel>=M0. Routing by canonical d merges all moving conductors; it does not sum per-conductor +1 errors.
The H^2 ambient bound is an upper bound pushed to the same physical population. If floor(116H^4/M0^2)=0 the population is empty.
The exponent 4h-2m and condition 4h-2m<1/12 are correct; no physical high-height coverage follows.

VERIFICATION=Exact polynomial syzygy (all degree-12 coefficients), invariants, and cubic factorization; explicit map on 3072 primitive pairs in [-35,35]^2; norm reduction, kernel invariance and height inequalities on the same range.
VERDICT_BOUNDARY=PASS for E_psi(B;H,M0)<<B^o(1)min(H^2,H^4/M0^2), H<=B^A. High-height region and total-population power saving remain open.
DO_NOT_REPEAT=Do not infer H<=B^(1/16), do not charge torsion as density, and do not confuse sf(norm) with old sf(2Pi).
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

