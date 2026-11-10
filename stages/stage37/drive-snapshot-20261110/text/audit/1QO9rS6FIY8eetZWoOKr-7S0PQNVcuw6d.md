Stage37-HOSTILE-AUDIT-M3-T11-114-PASS
AUDITED_CARD=M3-T11-114
VERDICT=PASS / EXACT_SAME_MEASURE_UPPER_BOUND / NO_GLOBAL_CLOSURE
AUDIT_MODE=Hostile rederivation and exact valuation tests in this session; no separately staffed or external reviewer is claimed.
POPULATION=Exact nondegenerate physical R<=B endpoints, fixed content/coefficient packet, psi/A4.

Primewise proof.
For C=C_u, kappa=sf(C), T=product p^floor(c_p/2), one has C=kappa*T^2 exactly. Thus S_sq=M_rel*T is integral and S_sq^2=M_rel^2*C/kappa divides N_u. C divides M_rel^2, so M_rel<=S_sq<=M_rel^2. This uses guaranteed divisibility only and remains valid at capped extreme depth.
Since dividing by a square preserves sf(N_u), d<=N_u/S_sq^2<=116H^4/S0^2. Audited 113 supplies uniform B^o(1) fibers for this canonical d. Summing d, not conductors, proves the stated joint bound; the ambient H^2 bound is pushed to physical endpoints by audited 036.

Exponent and boundary proof.
The shell lower bound S_sq^2>=M0^2*C0/K0 is correct. The exponent 4h-2m-c+k and extreme allocation exponent 4h-4m are correct. C=M^2 gives kappa=1, S_sq=M^2 and h<m+1/48; m=1/12-eta gives h<5/48-eta. The dyadic threshold S_sq>=B^(2h-1/24+epsilon) gives exponent 1/12-2epsilon.
When floor(116H^4/S0^2)=0 the subset is empty. If odd c_p=1 with lambda=1, kappa=p and no extra square divisor is extracted. Large C alone is insufficient.

What is not certified.
This audit does not prove actual N_u has no valuation above the capped depth, that kappa equals the full actual relative norm squareclass, that all endpoints have C=M^2, or that the displayed windows cover every physical H. In particular the full actual odd kernel at extreme depth must be retained in future support-localization arguments.

VERIFICATION=240 valuation cases (lambda=1..6, c=0..2lambda, five surplus choices at extreme depth); all parity-safe divisors and actual odd-kernel formulas passed. Non-extreme surplus was held zero as required by the capped-depth law.
PROMOTED=114 joint squarepart tail and precisely scoped exponent windows.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

