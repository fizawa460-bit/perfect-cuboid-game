M3-T11-115 — Psi core-supported norm squareclass compression without a small parameter-height cutoff
STATUS=PROVED_EXACT / HOSTILE_AUDIT_PASS / EXACT_SAME_MEASURE_SUPPORT_ADAPTER
TYPE=GLOBAL_CORE_SUPPORT_LOCALIZATION / FIXED_SUPPORT_UNIFORM_FIBER / HEIGHT_FREE_SUPPORT_WINDOW
POPULATION=Exact nondegenerate Stage37 physical endpoints with R<=B in one fixed content/coefficient packet, restricted to psi/A4. One endpoint is one count.
DEPENDENCIES=113 HOSTILE_AUDIT_PASS; audited 114; corrected 111; 036 polynomial physical heights; corrected three-anti-root denominator carriers (ROUTE section 32); 033 fixed-content support; the integer-normal-form M3-T11-042 entry, explicitly identified by N_u/g_u|D (not the other historical 042 entry).
ALIASES=PsiCoreSupportedNormSquareclassCompression; PsiCommonCoreRadicalTimesActualRelativeOddKernel.
DUPLICATE_SEARCH=MAIN/INDEX/RESULT-LEDGER/ROUTE/NEGATIVE-REGISTER and CARD-INDEX checked for d_rel, core radical and norm-support variants. 084/085 localized the residual kernel on the retired x=-1/8 carrier, where relative norm valuations are even. This result instead treats the live psi/A4 population, retains its actual relative odd kernel, and uses 113's new fixed norm-quartic fibers. 113/114 only bounded d by parameter height divided by a square divisor. This result counts core-supported d without a small-H cutoff.
DUPLICATE_OF=NONE.

1. Retained support carrier and explicit packet primes.
Write the corrected anti-roots v_i=A_i/B_i reduced, D=B_1*B_2*B_3 and R_rel=tau_1*tau_2*tau_3.
The valid complementary carriers are
B_1 | L_1*(tau_0*tau_2*tau_3)^2,
B_2 | L_2*(tau_0*tau_1*tau_3)^2,
B_3 | L_3*(tau_0*tau_1*tau_2)^2,
where each L_i is a positive fixed-packet factor in the retained polynomial range.
Multiplying gives
D | L_1*L_2*L_3*tau_0^6*R_rel^4.
For the canonical reduced u=a/b, N_u=a^2+b^2 and g_u=gcd(4,N_u) in {1,2}, the integer-normal-form identity gives
N_u/g_u | D.
Consequently
N_u | 2*L_1*L_2*L_3*tau_0^6*R_rel^4.
Only support containment is needed. No false same-v CRT from old section 31 is used.

Let P_pkt=2*L_1*L_2*L_3*c_1*c_2*c_3 and Delta_pkt=rad(P_pkt).
Keep these packet primes explicitly: L_i may contain coefficient primes outside the content-prime set.
P_pkt is fixed within the packet and <=B^K for one fixed retained K, so
2^omega(P_pkt)=B^o(1).
This follows from the primorial/factorial lower bound, uniformly over the allowed polynomial packets.

2. Actual relative odd kernel, not a capped proxy.
Let d=sf(N_u) be 113's canonical positive norm squareclass.
Define
d_rel=gcd(d,rad(M_rel))
=product_(p|M_rel, v_p(N_u) odd) p.
Set R0=rad(tau_0^sharp), with tau_0^sharp the part of tau_0 outside the content-prime set, and
Xi=R0*d_rel.
Xi is a positive integer in the polynomial physical range; it is not an independent random coordinate.
All primes of R_rel/M_rel lie in the content-prime set. Thus if p|d but p does not divide Delta_pkt*M_rel, the support carrier in (1) forces p|tau_0^sharp. Since d is squarefree,
d | Delta_pkt*R0*d_rel = Delta_pkt*Xi.

3. Uniform fixed-Xi physical count; all physical parameter heights included.
For any fixed Xi, at most 2^omega(Delta_pkt*Xi)=B^o(1) squarefree values d divide Delta_pkt*Xi.
Audited 113 gives B^o(1) physical psi endpoints per d, uniformly on the retained polynomial physical-height range. Hence
# physical psi endpoints compatible with fixed Xi << B^o(1).
No count of M_rel,C_u, anti-root triples, parameter heights or Gaussian orientations is multiplied into this estimate. They are all absorbed within the canonical fixed-d physical fiber.
Every physical psi point has a polynomial parameter-height bound: reduced psi denominator is b=5(r^2+s^2)/g with g in {1,2}, so H(t)^2<=r^2+s^2=g*b/5<=2b/5. Polynomial physical height of u from 036 therefore places its primitive psi preimages in 113's allowed polynomial range. No H<=B^(1/16) or other small exponent is assumed.

Let E_psi(B;Xi<=Z) count physical endpoints admitting a retained core representation with Xi<=Z, Z>=1 polynomially bounded. Then
E_psi(B;Xi<=Z)<<B^o(1)*Z.
If a core representation is not unique, the union over integer Xi values is still an upper bound and endpoints remain counted once. No injectivity of Xi is needed.
In particular Xi<=B^(1/12-delta) gives
E_psi<<B^(1/12-delta+o(1))
with no small parameter-height cutoff.
More generally any allowed Xi support set of cardinality A(B) gives A(B)*B^o(1).

4. Connection to 114 and the extreme-depth guard.
At p^lambda||M_rel, corrected 111 gives min(v_p(N_u),4lambda)=2lambda+c_p.
For c_p<2lambda, actual parity equals c_p mod2.
For c_p=2lambda, actual valuation may exceed 4lambda; its excess parity must be retained.
Define
e_ext=product_(p|M_rel, c_p=2lambda_p, v_p(N_u) odd) p.
Then with kappa=sf(C_u),
d_rel=kappa*e_ext.
Their supports are disjoint, because extreme capped c_p is even.
Thus the new receiver is explicitly
Xi=rad(tau_0^sharp)*sf(C_u)*e_ext.
Do not silently set e_ext=1 from capped data. Even C_u=M_rel^2 only implies kappa=1; actual even norm valuation is an additional condition for d_rel=1.

For the actual-even relative stratum d_rel=1, the subset R0<=B^(1/12-delta) is small at the same physical one-twelfth scale for every physical parameter height.
For general d_rel, a sufficient window is R0<=B^a and d_rel<=B^b with a+b<1/12.
On an intersection also satisfying 114's H,S0 cutoffs one may take the minimum of valid upper bounds:
E_psi<<B^o(1)*min(Z,H^2,H^4/S0^2).
This is a minimum of replacement counts, not a product of savings.

5. What remains unresolved.
The result does not prove that every psi endpoint has small Xi, or that the occupied Xi support has cardinality below B^(1/12).
Large Xi can arise from a large all-same core radical, a large actual relative odd kernel, or both. Such large support is the new minimal global occurrence/correlation receiver.
Some high-H/low-S_sq points are now controlled if Xi is small; no claim is made that all such points are controlled.
The fixed Xi fiber bound does not itself constrain how many Xi values occur. Bounding occupied Xi cardinality is required to close the population by this Xi-union argument alone. Other receivers can count large-Xi endpoints directly; this is not a necessity theorem for every future method.
The local S4 tuple remains frozen, x=-1/8 stays retired, and phi/nonlocal S4/theta!=0 remain live.

VERIFICATION=1296 synthetic prime-support allocations verified d|Delta_pkt*Xi; 240 conductor valuation cases verified d_rel=kappa*e_ext with extreme surplus retained. These test algebra/support only and do not assert physical endpoint existence.
IMPLIES=The psi route now has a core-support window valid at all physical parameter heights; large Xi support remains the blocker.
DO_NOT_REPEAT=Do not omit coefficient packet primes, replace actual d_rel by capped sf(C_u), infer small Xi globally, or multiply fixed-Xi compression with lattice/torsion/local densities.
REOPEN_CONDITION=Hostile audit rejects corrected denominator support, N_u/g_u|D, uniform polynomial packet factor bound, actual relative kernel, fixed-d pushforward, or physical preimage-height adapter.
CREDIT=Audited same-measure fixed-Xi multiplicity and small-Xi window only; zero total-population or primary-gate closure credit.
AUDIT_DOC_ID_115=1Egd3YW74bOS-JwN2iO4PtSGfeZ0gc_jG
AUDIT_KIND=Within-session hostile rederivation, not an independent external review.
NEXT_LEGAL_ACTION=Hostile-audit 116; then count the simultaneous physical residual outside small Xi, norm quotient and complementary norm cofactor. Preserve phi/nonlocal S4/theta options.
NEXT_RESEARCH_CARD_ID=M3-T11-117
PSI_CORE_SUPPORTED_FIXED_XI_UNIFORM_BO1=true
PSI_SMALL_XI_HEIGHT_FREE_WINDOW=true
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
