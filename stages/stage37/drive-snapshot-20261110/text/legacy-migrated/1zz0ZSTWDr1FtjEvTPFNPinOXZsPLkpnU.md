M3-T11-114 — Psi incremental-conductor squarepart tail and parity-sensitive height window
STATUS=PROVISIONAL / HOSTILE_AUDIT_REQUIRED / EXACT_SAME_MEASURE_UPPER_BOUND
TYPE=INCREMENTAL_CONDUCTOR_ADAPTER / JOINT_SQUARECLASS_TAIL / PARITY_SENSITIVE_HEIGHT_WINDOW
POPULATION=Exact nondegenerate Stage37 physical endpoints with R<=B in one fixed content/coefficient packet, restricted to psi/A4; one endpoint is one count.
DEPENDENCIES=113 HOSTILE_AUDIT_PASS; 040/041/043 capped conductor; corrected 111; 036 uniform fixed-u multiplicity.
ALIASES=PsiIncrementalConductorSquarepartTail; PsiConductorParityHeightWindow.
DUPLICATE_SEARCH=RESULT-LEDGER, active ROUTE, NEGATIVE-REGISTER and CARD-INDEX checked for squarepart/parity/conductor variants. 112 is a fixed-modulus lattice count; 113 used M_rel^2 only and explicitly left C_u uncharged. Older squarefree kernels belong to different populations or equations. This result newly routes the incremental C_u squarepart into the joint norm-squareclass count.
DUPLICATE_OF=NONE.

1. Exact parity-safe square divisor.
Let M=M_rel and C=C_u. The accepted divisibility is
M^2*C | N_u=a^2+b^2,
with 0<=c_p=v_p(C)<=2lambda_p for every p^lambda_p||M.
Write uniquely C=kappa*T^2, where kappa=sf(C) is squarefree and
T=product_(p|M) p^floor(c_p/2).
Define S_sq=M*T. This symbol is NOT the existing symmetric coordinate S.
Then exactly
S_sq^2=M^2*C/kappa | N_u,
M<=S_sq<=M^2.
Only divisibility is used. The formula remains valid at capped extreme depth even if actual norm valuations exceed the cap. No old exact-saturation assertion is imported.
For psi, N_u=F(r,s)/g^2, g in {1,2}, so S_sq^2|F as well.

2. Joint actual-conductor upper bound.
Let E_psi(B;H,S0) count the physical subset admitting a primitive psi parameter of height<=H and whose actual S_sq>=S0>=1.
The canonical d=sf(N_u)=sf(F) satisfies
d=sf(N_u/S_sq^2)<=N_u/S_sq^2<=116H^4/S0^2.
Audited 113 gives B^o(1) physical endpoints uniformly per d; sum over canonical d only, simultaneously over all M,C.
Thus for H<=B^A,
E_psi(B;H,S0)<<_A B^o(1)min(H^2,H^4/S0^2).
If floor(116H^4/S0^2)=0 the subset is empty.
In a shell M>=M0, C>=C0, kappa<=K0, every endpoint has S_sq^2>=M0^2*C0/K0, hence
E_psi<<_A B^o(1)min(H^2,H^4*K0/(M0^2*C0)).
K0>=1. No sum over conductor pairs or kappa values is needed. This is one replacement count, not 113 multiplied by a new independent probability.

3. Exponent window and gain over 113.
If H<=B^h, M>=B^m, C>=B^c, kappa<=B^k, then
E_psi<<B^(4h-2m-c+k+o(1)).
It beats one-twelfth on this subset if
4h-2m-c+k<1/12.
On the extreme amplified allocation C=M^2, kappa=1 and S_sq=M^2. Therefore the joint upper bound over all M>=B^m is
E_psi<<B^(4h-4m+o(1)),
and suffices when h<m+1/48.
For m=1/12-eta this allows h<5/48-eta, compared with 113's h<1/16-eta/2.
Example: H<=B^(5/48-epsilon), M>=B^(1/12-eta), C=M^2, epsilon>eta implies
E_psi<<B^(1/12-4epsilon+4eta+o(1)).
This includes a wider height window on this allocation, but no assertion that all physical psi endpoints lie in it or in the extreme allocation.

4. Parity obstruction and precise remaining receiver.
One cannot replace S_sq^2 by M^2*C unless C is a square. Odd c_p leaves p in kappa. Example lambda=1,c_p=1 gives C=p, kappa=p and S_sq=M: no new square divisor is extracted.
A large C alone therefore supplies no polynomial improvement if kappa is comparably large.
For a dyadic parameter shell H~B^h, a sufficient low-occupancy condition is
S_sq>=B^(2h-1/24+epsilon),
giving E_psi<<B^(1/12-2epsilon+o(1)).
The still-uncontrolled physical subset is high parameter height with small S_sq relative to this threshold. Within the amplified-u branch C>=M, this includes high odd-valuation kernel kappa, not just large C.
The old complementary identity Q_S*C=M^2 remains available; no distribution/correlation theorem for kappa, Q_S, H or actual endpoints is proved here.

5. Supporting checks and firewall.
48 valuation profiles lambda=1..6, c=0..2lambda, with three actual norm depths at or above the guaranteed depth, verified S_sq^2=M^2*C/kappa, divisibility and sf(norm)<=norm/S_sq^2.
The exact proof is the displayed primewise floor formula and audited 113 routing; finite tests are supporting only.
IMPLIES=Incremental C_u can strengthen the joint psi bound only through its squarepart. A larger scoped height window exists on C=M^2; high-height/low-squarepart occupancy remains the blocker.
DO_NOT_REPEAT=Do not charge C magnitude without removing kappa; do not multiply lattice/density/torsion savings; do not replace the existing symmetric S by S_sq; do not treat C=M^2 as covering all endpoints.
REOPEN_CONDITION=Audit rejects parity-safe divisor, capped-depth dependence, fixed-d uniformity, actual-endpoint routing or exponent arithmetic.
CREDIT=Provisional scoped replacement count and height window only; no global saving or closure.
NEXT_LEGAL_ACTION=Hostile-audit 114, then seek exact physical correlation/occupancy control of high H with low S_sq, including the amplified-u odd-kappa tail; complementary Q_S and phi/nonlocal S4/theta routes remain open.
NEXT_RESEARCH_CARD_ID=M3-T11-115
PSI_INCREMENTAL_CONDUCTOR_SQUAREPART_TAIL=PROVISIONAL
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


AUDIT ADDENDUM — supersedes historical provisional status
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / NO_GLOBAL_POWER_SAVING
AUDIT=Stage37-HOSTILE-AUDIT-M3-T11-114-PASS (Stage37-AUDIT).
PROMOTED=Parity-safe square divisor, joint physical tail and scoped exponent windows.
GUARD=sf(C_u) is not asserted to equal the actual fresh-relative norm squareclass at extreme capped depth.
NEXT=M3-T11-115 core-supported actual norm-squareclass adapter; large Xi support remains open.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

