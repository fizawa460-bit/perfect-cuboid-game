# M3-T11-116 — complementary norm-cofactor fibers and a height-free two-sided window

STATUS=PROVISIONAL / HOSTILE_AUDIT_REQUIRED / EXACT_SAME_MEASURE_UPPER_BOUND
TYPE=COMPLEMENTARY_NORM_COFACTOR / JOINT_MOVING_CORE_COUNT / TWO_SIDED_SUPPORT_WINDOW
POPULATION=Exact nondegenerate physical Stage37 psi/A4 endpoints with R<=B in one fixed content/coefficient packet; one endpoint is one count.
DEPENDENCIES=Audited 113, 114, 115; corrected denominator carriers; integer-normal-form N_u/g_u|D; polynomial physical range from 036.
ALIASES=PsiComplementaryNormCofactor; PsiTwoSidedNormSquarepartWindow.
DUPLICATE_SEARCH=Current MAIN/INDEX/RESULT-LEDGER/active ROUTE checked for norm quotient/cofactor and complementary squareclass variants. Older theta cofactors and elliptic/genus-2 quotients concern different equations/populations. 113/114 count small norm squareclasses; 115 counts small core support. None uses the integer quotient of the live psi norm into its even-power core carrier. DUPLICATE_OF=NONE.

## 1. Integral cofactor with fixed-packet squareclass

Let L=L1*L2*L3, Rrel=tau1*tau2*tau3, and define

W_car=2*L*tau0^6*Rrel^4,
J_car=W_car/N_u.

Audited 115 gives N_u | W_car, so J_car is a positive integer. This symbol J_car is unrelated to the binary-quartic invariant J=2219776. W_car is not the actual reduced denominator D: it is an upper divisibility carrier. No equality D=W_car is assumed.

The core contribution tau0^6*Rrel^4 is a square. From N_u*J_car=W_car it follows exactly that

d=sf(N_u)=sf(2*L*J_car).

Thus for fixed J_car and the fixed packet, d is uniquely determined. Audited 113 gives B^o(1) physical psi endpoints for that d. This absorbs all moving core choices, conductor allocations, orientations and parameter heights; none is charged again. If endpoints admit several retained core representations, union counting remains valid.

For Y>=1 in the polynomial physical range,

E_psi(B; J_car<=Y) << B^o(1)*Y.

More generally an allowed J_car support set of cardinality A gives A B^o(1). This receiver applies to large-Xi endpoints as well: no condition on rad(tau0^sharp)*d_rel is imposed. It does not prove J_car small globally.

## 2. A high-parameter-height window

Write the primitive psi parameter t=r/s and H=max(|r|,|s|). Audited reduction gives N_u=F(r,s)/g^2, g in {1,2}, where

F=(r^2-2rs-s^2)^2+25(r^2+s^2)^2 >=25 H^4.

Therefore N_u >=(25/4)H^4. On any exact physical subset with H>=H0, tau0<=T0 and Rrel<=U0 (U0 is a magnitude bound, not 115's common-core radical R0),

J_car <=(8/25)*L*T0^6*U0^4/H0^4,
E_psi << B^o(1)*floor((8/25)*L*T0^6*U0^4/H0^4).

If the floor is zero this subset is empty. L is fixed in the packet; it may grow polynomially with B and must not be silently treated as an absolute constant. With L<=B^ell, T0<=B^t, U0<=B^r, H0>=B^h, a sufficient one-twelfth window is

ell+6t+4r-4h <1/12.

This complements the low-H windows of 113/114. It is a scoped bound, not a proof that all physical parameter heights are high enough relative to their cores.

## 3. Height-free two-sided covering criterion

Retain 114's S_sq=M_rel*T with C_u=kappa*T^2 and kappa=sf(C_u). Then S_sq^2 | N_u and S_sq^2 | W_car. Define

V_norm=N_u/S_sq^2,
K_car=W_car/S_sq^2.

Both are positive integers, and exactly

d=sf(V_norm),
V_norm*J_car=K_car.

For Z,Y>=1, endpoints admitting a representation with K_car<=Z*Y satisfy V_norm<=Z or J_car<=Y. If both strict inequalities failed, their product would exceed Z*Y. The first subset has d<=Z and the second has at most floor(Y) cofactor values. Therefore

E_psi(B; K_car<=Z*Y) << B^o(1)*(floor(Z)+floor(Y)).

In particular, for polynomial K0>=1,

E_psi(B; K_car<=K0) << B^o(1)*sqrt(K0),

by choosing Z=Y=sqrt(K0). Hence K_car<=B^(1/6-2delta), delta>0, gives a one-twelfth support deficit B^(1/12-delta+o(1)) without any small-H cutoff. This is a union of two replacement counts; no independence is assumed.

Explicitly

K_car=2*L*tau0^6*Rrel^4*kappa/(M_rel^2*C_u).

Do not infer that a large C_u alone makes K_car small: the actual kappa and all common/nonfresh core factors remain. Because S_sq<=M_rel^2<=Rrel^2, K_car>=2*L*tau0^6. Thus this balanced window cannot automatically cover large common-core magnitude. The direct small-J_car window is more general than the balanced criterion.

## 4. Exact residual receiver and audit plan

For chosen Z_Xi,Z,Y, the union of Xi<=Z_Xi, V_norm<=Z and J_car<=Y has count <<B^o(1)*(Z_Xi+Z+Y). The unresolved complement has simultaneously Xi>Z_Xi, V_norm>Z and J_car>Y, and therefore K_car>ZY. This is a receiver definition, not a distribution theorem. It replaces the overly exclusive requirement to control large Xi by Xi cardinality alone.

NEXT_LEGAL_ACTION=Audit integrality of J_car, fixed-packet squareclass identity, uniform fixed-d pushforward, high-height constants and two-sided union on the same physical measure. If PASS, seek occurrence/correlation bounds for this simultaneous residual complement, keeping actual relative odd surplus and common/nonfresh core magnitudes. Phi global root allocation, genuinely nonlocal S4 and theta!=0 remain live; local S4 tuples remain frozen and x=-1/8 retired.

VERIFICATION=39,768 synthetic divisor cases checked sf(N)=sf(2L*J_car), exact product V_norm*J_car=K_car and min(V_norm,J_car)^2<=K_car. 513 primitive psi parameters checked g in {1,2} and N_u>=(25/4)H^4. These checks support the algebra and assert no physical endpoint existence.
REOPEN_CONDITION=Audit rejects corrected carrier divisibility, fixed packet L, canonical squareclass identity, polynomial range, fixed-d physical fibers, or union routing.
DO_NOT_REPEAT=Do not call J_car the quartic invariant J; replace W_car by D; drop L from exponents; multiply the two windows as probabilities; assert small J_car or K_car on the total population; or discard extreme odd norm surplus.
CREDIT=Provisional complementary-cofactor count and two-sided scoped window only; zero global saving or closure credit.
NEXT_RESEARCH_CARD_ID=M3-T11-117
PSI_FIXED_COMPLEMENTARY_NORM_COFACTOR_UNIFORM_BO1=PROVISIONAL
PSI_TWO_SIDED_HEIGHT_FREE_WINDOW=PROVISIONAL
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
