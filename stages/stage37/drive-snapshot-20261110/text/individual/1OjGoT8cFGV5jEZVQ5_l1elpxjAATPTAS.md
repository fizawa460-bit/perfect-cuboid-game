# M3-T11-198 — Full 2-Kummer coset of the physical pair and translated doubling graph

STATUS: EXACT_ALL_CONTENT_COSET / THIRD_FACE_DOUBLING_GRAPH / PRE_THIRD_FACE_CYCLIC_WITNESS / GLOBAL_COUNTING_CREDIT=0.
Current authority: Stage37 MAIN, operational CARD-INDEX, short RESULT-LEDGER, active ROUTE §17.3–17.4, latest197. This card continues197; no full historical reread. Gate OPEN. NEXT199. Independent audit NOT RUN; separate-chat audit162–185 scope unchanged. TI parked120/retracted147–149frozen. No retraction.

## 1. Input and actual physical scope

Use196 notation, all content, including nonunit kappa. For signed pair phase (q+ip)/c, kappa=h_i h_j, c=kappa u², Phi=kappa u divides R, Theta=kappa q is signed nonzero and |Theta|<Phi²<=B². On E_Theta: y²=x³−Theta²x put

P_+=(Phi²,kappa Phi p),
P_-=(-(Phi e_k/R)²,−Phi³ e_k T/R³), T=e_i f_i+e_j f_j.

Normalize a=Theta/Phi², b=kappa p/Phi², z=e_k/R, S=(e_i+e_j)/R, D=(e_i−e_j)/R. Then a²+b²=1, a,b nonzero, and197's two adjacent-face cover is

S²=(1+a)(1−z²/a), D²=(1−a)(1+z²/a).

All original192 W/integer n_face, intrinsic and primitive normalization, U,V,N_T/Den(S), fresh D-only134 masks remain. The new equation below neither discards these masks nor closes their moving support.

## 2. Exact full 2-Kummer coset, with converse on the open set

Let T_(0)=(0,0) be the order-two point on E_Theta. This symbol denotes torsion, not193's all-same content T0. Then every physical pair satisfies

**P_-−P_+−T_(0) belongs to 2E_Theta(Q).**

Equivalently P_-=P_++T_(0)+[2]Q_aux for some rational Q_aux. Q_aux is not192's face-halfpoint; this is196's congruent-number curve and pair anchor.

Proof. Write r=Phi z. The standard full2 Kummer map on the non-root open is delta(P)=([x],[x−Theta],[x+Theta]), with squareclasses in Q*/Q*² and kernel2E(Q). At T_(0), its extended value is ([-1],[-Theta],[Theta]). Thus

delta(P_++T_(0))=([-1],[-Theta(Phi²−Theta)],[Theta(Phi²+Theta)]).

The adjacent-face identities give

D²=(Phi²−Theta)(Theta+r²)/(Phi² Theta),
S²=(Phi²+Theta)(Theta−r²)/(Phi² Theta).

For P_-, x=−r², hence

delta(P_-)=([-1],[-Theta/(Phi²−Theta)],[Theta/(Phi²+Theta)]),

which equals the displayed anchor class since the ratios of corresponding entries are squares (Phi²∓Theta)². The kernel assertion proves the claim. This uses all three classes, not only the negative square first coordinate.

Conversely, a rational P_- in this coset on the nondegenerate open has x=−r² from its first class; its other two classes make the displayed D²,S² squares. Finite sign choices recover z,S,D and the two adjacent-face/sphere relaxation. The full original physical masks and third-face square are additional requirements. Root/boundary cases use extended Kummer values and are not part of the strict-positive physical chamber.

For an explicit half, take R_diff=P_-−P_+−T_(0)=(x,y). Choose rational r1²=x,r2²=x−Theta,r3²=x+Theta with r1*r2*r3=−y; put sigma=r1*r2+r1*r3+r2*r3. Then

Q_aux=(x+sigma,−y−(r1+r2+r3)*sigma), [2]Q_aux=R_diff.

R_diff=O allows Q_aux=O. The rational halves differ by E_Theta[2], at most four. Rational group formulas and square roots give polynomial height transport from physical coordinates; no rank-independence follows.

Primary-source input: MIT official lecture notes https://math.mit.edu/~setia/7370sp20.pdf, Example3.25.6, pp75–76, describes the full2-descent embedding E(Q)/2E(Q) using root-difference squareclasses and its covering equations. The pair-specific equality above and subsequent branch computation are this card's deductions, not claims attributed to that source.

## 3. Third face as one translated-doubling square

Set A=P_++T_(0). Since x(P_-)=−Phi²z², the remaining face condition becomes exactly

**V_aux²=Phi²+x(A+[2]Q_aux), V_aux=Phi f_k/R.**

This is the same third-face condition as197, transported onto the rational Q_aux parameter. It is not a new independent density selector or an extra point to count independently.192's integer W and integer n_face already imply197's third-face incidence on the actual receiver; none of that is forgotten here.

The smooth fixed-parameter double cover of the elliptic Q_aux base has eight simple geometric branch points and genus5. Indeed, poles occur at the four preimages A+2Q=O, each of even order2, so cause no branching. Zeros occur at

A+2Q=B_±=(-Phi²,±iY_+)=±[i]P_+, Y_+=y(P_+),

where [i](x,y)=(-x,iy) is the CM automorphism over Q(i). Consequently the branch dictionary is

[2]Q=(±[i]−1)P_+−T_(0).

The targets B_± are distinct because Y_+≠0. Multiplication by2 is etale of degree4, giving eight simple zeros. Riemann–Hurwitz gives 2g−2=8, g=5. The Q(i) notation only describes geometric branch points; it does not revive the parked torsion-intersection route.

Compatibility with197's complete cover: the two-quadratic cover in S,D is the full2 covering attached to the anchor class. On normalized E_a the anchor is P_ph=(1,b), and P_ph+T_(0)=(-a²,a²b). The rational boundary point z=a,S=b,D=b maps there (one edge zero). This trivializes the full2 covering into a translated doubling map from E_a. Adding t²=1−z² gives precisely the above double cover; finite sign conventions and the usual smooth projective completion apply. This is an explicit chart for the already-known genus5 cover, not new genus or fixed-fiber credit.

## 4. Exact cyclic-subgroup witness: independence cannot be inferred

Take a=5/13,b=12/13 on E_a and P=(1,b). Choose Q_aux=2P, so P_-=5P+T_(0). Both physical-pair points are in the subgroup generated by P and T_(0); no certification of the full Mordell–Weil rank is needed or claimed. The reconstructed positive primitive partial sphere has

R=31127962482877,
(e1,e2,e3)=(29384126102760,1819327557852,10110055823275),
(f1,f2)=(-10272447688477,−31074750128885).

The two adjacent face squares and e1²+e2²+e3²=R² hold exactly. The third-face square fails. Thus the pre-third-face coset/sphere/two-face relaxation does not force two independent points, and the coset alone does not force the third face. This is one exact partial witness, not a full original-mask endpoint, not a density lower bound and not a counterexample to the unresolved actual endpoint estimate.

## 5. Verification and credit accounting

Executable: verify_m3_t11_198.py, SCRIPT_FILE_ID=1wjfY_z9ViCiFCRKqQWVIhv7hQIrJB2Rp.
Report: M3-T11-198-verification.json, JSON_FILE_ID=1ddQrKLJsZN98KLyp0i_XSG1J92kWyjda.

Python stdlib exact fractions/group law, explicit halving checked by doubling: 28 rational coset/halving cases including4 nonunit cases. Finite fields17,41,73: 5408 exhaustive checks against the computed image2E(F_p), with denominators/nondegeneracy enforced. Exact cyclic witness above verified including primitivity and failed third face. PASS; physical endpoints0; independent audit false. These tests support formulas and implementation; they are not the proof of a uniform occupancy theorem.

New substantive result is the actual-pair full2 coset and its translated-doubling third-face/CM-branch dictionary. The coset is already paid by197's two quadratics, so no independent Selmer density. Generic genus5 already190/176/BASE002; no extra genus count. Five factors197 share z; no independent multiplication. Fixed Theta fiber saving196 and small Theta sum195 unchanged. No rank>=2 assumption. All moving coefficient/anchor and unshared-support costs remain. Gate OPEN/global credit0; large-c and K>1 low-median remain separatelyOPEN.134 Q_S=M_rel²,C_u=M_G=1 retained.

## 6. NEXT199: moving anchored-doubling square occupancy

Prove a genuinely summed estimate on the large-Theta/Phi residual for

V_aux²=Phi²+x(P_++T_(0)+2Q_aux),

with the physical negative-X chamber, primitive W/H and every192 original mask, and P_+ the actual phase anchor. Pay the moving Theta and anchor-height support. Physical endpoints lift to at most four halves and finite signs, so this is a bounded-choice transport, not extra independent variables. A closing bound must beat the required global B^(1/3) scale by a positive exponent after all summation costs; fixed-curve/fixed-anchor results alone do not supply it.

The eight CM branch points describe variation and potential correlated square occupancy, not a new standalone selector. A next result must distinguish what is already implied by192 W+integer n_face and197 complete cover. Do not count coset, branch points, five factors, first-coordinate Kummer class or previously closed small-Theta sectors again. K=1 unshared support and K>1/large-c must be treated at their own scopes. Restart from198 plus196/197 and relevant ROUTE17; full history unnecessary.
