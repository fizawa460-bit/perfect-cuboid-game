# M3-T11-133 — physical half-angle lift forces square norm; exact signed reconstruction and Gaussian extreme routing

STATUS=PROVED_EXACT_PHYSICAL_LIFT_AND_GLOBAL_NORM_SQUARE_NECESSITY
AUDIT=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_PASS_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0; PRIMARY_GATE=OPEN; TI=PARKED_BY_USER

## Authority, conventions and scope
Current authority: MAIN/INDEX/RESULT-LEDGER/active ROUTE and latest132. Targeted source reads: ROUTE17 common physical phase, ROUTE24 full double-lift equation, ROUTE29 distinguished roots, corrected ROUTE32 distinct anti-roots, ROUTE35 symmetric cubic, residual105/106 (ROUTE118/120), and retained131/132. No full historical reread. Work on finite nonzero u and nondegenerate physical endpoints; u=infinity and singular/content branches remain separately retained. Use the actual signed anti-root definitions z_i=i v_i, not independently chosen signs of their squared traces. Quartic theta is never identified with a physical direction or anti-root.

Write normalized physical directions a_i=x_i+i y_i=Q/r_i in Q(i), N(a_i)=1, x_i=e_i/R>0, and sum x_i²=1. The y_i are signed complementary face diagonals divided by R. ROUTE24 gives
 C=a_2 a_3, s=a_1/a_2, t=a_1/a_3.
Here C,s,t are torus coordinates; below S=sum v_i and u is the corrected symmetric parameter. These notations must not be conflated.

## 1. Exact anti-root-to-physical-direction adapter
The G3-targeted root from29 is z_3=1+(1+C²+C²s²)t/(Cs). Substitution gives
 z_3=1+a_1²+a_2²+a_3^(-2).
Similarly, using the s-target quadratic and the corrected G1 relabeling (Cs,t/s,1/s),
 z_2=1+a_1²+a_2^(-2)+a_3²,
 z_1=1+a_1^(-2)+a_2²+a_3².
The real parts vanish because sum x_i²=1. Thus exactly,
 v_i=2(sum_j x_j y_j)-4x_i y_i,
 S=2 sum_j x_j y_j,
 d_i:=(S-v_i)/2=2x_i y_i.
Consequently every physical point satisfies the SIX simultaneous rational-square conditions
 L_i^+²=1+d_i, L_i^-²=1-d_i,
where L_i^+=x_i+y_i, L_i^-=x_i-y_i. None can vanish: a rational unit-circle point cannot have x_i=+/-y_i, since 2x_i²=1 has no rational solution.

This is a global physical lift beyond merely having a rational split cubic, residual quartic point, or local root-lines. It is the original physical condition expressed in actual anti-root coordinates, not a new independent acceptance probability.

## 2. NEW global consequence: N_u=a²+b² is necessarily a square
The symmetric cubic is f(X)=X³-SX²+EX-P, E=4u(S-u)/(1+u²), P=4u²S/(1+u²). Let A=1+u². Exact evaluation gives
 product_i(1+d_i)=f(S+2)/8=(2+S+Su)²/(4A),
 product_i(1-d_i)=-f(S-2)/8=(2-S+Su)²/(4A).
Both products are rational squares on a physical point. At least one numerator is nonzero: if both vanish, subtracting yields S=0 and then 2=0. In fact neither vanishes on a rational physical lift by Section1. Therefore A is a rational square.

If u=a/b is reduced, b>0, then A=(a²+b²)/b². An integer that is a rational square is an integer square, so
 N_u=a²+b²=c², c>0, gcd(a,b)=1.
This is a necessary theorem on the finite physical branch, not an assumption or a sufficient criterion. It restricts moving u to a rational Pythagorean conic, for example u=2r/(1-r²) with rational projective r and appropriate sign chart. It is NOT a thin-set/counting theorem on exact R<=B. No B^(-epsilon) factor follows merely from ambient conic sparsity.

Rational cubic splitting does not imply this norm-square condition: u=-1/2,S=4/5, roots (-4/5,-2/5,2) satisfy all displayed cubic identities, but N_u=5 is nonsquare, and cannot lift physically. This example is an algebraic enlargement, not a physical point.

## 3. Gaussian extreme: p==5 mod8 forced onto D, unconditionally on physical points
Retain131: at a fresh Gaussian extreme p^lambda||m_i, L=2lambda, v_p(A)=2L, S and S-u are units, 2S=u modp^L and the targeted unit anti-root V=-u modp^L. Put rho=u modp, rho²=-1. Then
 d_i=(S-V)/2=3rho/4 modp,
 1+/-d_i=1+/-3rho/4 modp.
The exact residue identities are
 (3+/-rho)²=8(1+/-3rho/4).
For p!=5 the two factors are nonzero and each has quadratic character (2|p). For p=5 one factor is zero, but the other equals2 and is a nonsquare. Hence every odd split fresh G prime must satisfy
 p==1 mod8.
All fresh p==5 mod8 therefore belong to the denominator extreme D, without separately ASSUMING N_u square.

This also follows from the newly proved global N_u square and131's retained pole splitting criterion chi(-2/A0)=1: A0=A/p^(4lambda) is now a p-adic square, so chi(2)=1. These are TWO PROOFS OF ONE restriction, not two independent filters. On p==1 mod8, the targeted half-angle square factors are nonzero square units, and their deeper square lifting is automatic by Hensel. Do not charge another local precision gain. Other half-angle components, signed compatibility and global packet reconstruction remain live.

N_u square means all surviving physical u lie in the square-norm branch already explored in129. The129 certified S4 family and residual all-place separate local persistence remain valid within their nonphysical scope. They do not automatically satisfy these six squares or give actual physical endpoints. The general123 scalar/class-group framework remains retained; physical norm-square restriction narrows its base parameters rather than computing Cl(K_u)[2].

## 4. Exact finite signed reconstruction and physical height
For a fixed ordered rational anti-root triple v_i, put d_i=(S-v_i)/2. Choose rational L_i^+,L_i^- with the six square equations above. A compatible normalized cuboid direction lift is EXACTLY a sign choice satisfying
 sum_i L_i^+ L_i^-=-1,
 x_i=(L_i^++L_i^-)/2>0,
 y_i=(L_i^+-L_i^-)/2.
Proof: x_i²+y_i²=1, 2x_i y_i=d_i, and
 sum x_i²=(3+sum L_i^+ L_i^-)/2=1.
Conversely every actual lift supplies these L_i. Moreover sum d_i=S, so reconstructing the signed anti-roots from x_i y_i recovers precisely v_i, not merely v_i². With a_i=x_i+i y_i and C,s,t above,
 F(C,s,t)/(Cst)=4(sum x_i²-1)=0,
and the distinguished root formulas recover z_i=i v_i.

There are at most2^6=64 sign choices, fewer after positivity/canonical ordering; no moving rational parameter is concealed in this direction lift. This does not replace the retained fixed-u subpolynomial theorem or prove a moving-support deficit.

For each retained positive sign branch define
 R_0=lcm_i Den(x_i), e_i=R_0 x_i.
Then e_i are integers, sum e_i²=R_0². Also R_0 y_i is an integer: its square is the integer R_0²-e_i² and a rational square root of an integer is integral. The quadruple is primitive since any common divisor of R_0,e_i would contradict minimality of R_0. In fact gcd(e_1,e_2,e_3)=1 as well, since a common prime divisor of all e_i divides R_0 by the sphere equation.
Thus the exact primitive Euclidean space-diagonal height is R=R_0. Apply R_0<=B directly, not height(u) or height(S). Rational face diagonals are R_0 y_i up to sign. To enter the fixed Stage37 T11 packet, still verify original content, Gaussian orientation, parity, cyclic-cover and coefficient kappa conventions. The sign system alone is not a blanket converse for a preassigned packet. Count each reconstructed canonical endpoint once.

For integral audit coordinates v_i=A_i/B_i, S=s/t reduced with B_i,t>0, the six rational square conditions are equivalently the six integer-square tests
 J_i^+/-=2t B_i[2t B_i +/- (s B_i-t A_i)].
No coprimality of these unreduced factors is assumed; q=n/d is a rational square iff nd is an integer square when d>0. Their shared denominators and the two global product identities prohibit independent density multiplication.

## Verification, audit and limits
Exact replay verify_m3_t11_133.py PASS: 160 finite-field oriented roots at split primes below1000; 180 local G examples with actual cubic pole splitting and original unit root-line, including p5mod8 local impostors now excluded by the half-angle lift; 500 rational cubic-split enlargement samples for product identities/integer square equivalence; 277 rational boundary spheres for forward/reverse sign reconstruction and exact primitive R. Boundary samples have a zero edge and are NOT positive endpoints. Local G samples are not global norm-square or physical points. Physical endpoints enumerated=0.
Symbolic replay verifies three phase identities, two cubic product identities and two rho identities. A separate Groebner reduction of the symmetric surface relation from x_i²+y_i²=1 and sum x_i²=1 is zero. Computations support the displayed proofs; no finite test establishes global counts. Audit is within-session, not external.

Retain130 interior exclusion,131 D/G structure,132 no-double-charge H identity and height windows, all D Legendre/singular shells, and129/123 within stated scope. 120 remains RETRACTED. Global fixed-power saving, primary closure, P/M3 limit and nonexistence credit remain false.

NEXT=M3-T11-134
ATTACK=SquareNormSixHalfAngleSignedPhysicalLiftMovingSupport
Read133 then131/132, targeted129 square-norm S4 persistence and ROUTE17/24/35–37. Restrict to N_u=c² from the outset; study the simultaneous SIX half-angle squares plus signed sum and exact R_0<=B with original fixed packet. Identify residual global information beyond the two product identities and p1mod8 G routing. A same-measure support bound or a genuine collapse of the remaining cover is needed. Do not repeat a standalone nonsquare-N residual screen, charge p1mod8 twice, treat square-N conic points as endpoints, or drop the signed compatibility / physical-height / packet reconstruction.
