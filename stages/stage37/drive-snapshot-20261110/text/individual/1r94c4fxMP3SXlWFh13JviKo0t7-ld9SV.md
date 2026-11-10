# M3-T11-190 — Original full lift as a doubled elliptic point, split quartic and face-supported Kummer label

CARD_ID: M3-T11-190
STATUS: PROVED_ORIGINAL_LIFT_2DIVISION_ADAPTER / SPLIT_QUARTIC / FORCED_KUMMER_BIT_AND_FACE_DELTA / MOVING_COUNT_OPEN
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Authority and what is actually added

Fresh Drive MAIN, INDEX (latest189, next row blank), short RESULT-LEDGER, latest189 and active ROUTE17 were checked. Targeted old cards ONE-001, ONE-005, BASE-002 and176 were fetched to avoid rediscovery. The product-of-diagonals factorization is already ONE-001; it earns no new credit. Genus-five full-lift geometry is already retained in176/BASE-002; fixed-source high genus or finiteness does not sum moving faces. The present additions are an explicit canonical halving map tied to the ORIGINAL diagonals, its exact inverse and intrinsic scale, a completely split quartic with specified roots, and the K=1 Kummer label/conductor dictionary. No new negligible sector or endpoint count is proved.

Keep original primitive positive endpoints R<=B, canonical orientation/cyclic/content masks and134 full square/intrinsic-R lift.189 ruled out counting an independent phase triangle attached only to numerical Pell/product identities. Here no phase variable is free: it is pulled back from the actual diagonals after full reconstruction.

## 2. Face normalization: distinguish the two k coordinates

For K=1 relabel h_1=h_2=1,h_3=h. Put g=gcd(e_1,e_2), A=e_1/g,F=e_2/g, choosing A odd and F even by the bounded first-two-edge ordering. Let n be the PRIMITIVE FACE HYPOTENUSE:

A²+F²=n², gcd(A,F)=1.

This n is NOT181's shared k.181 gives n=h*k_shared and f_3=h*g*k_shared=g*n. Also e_3=h*u, R=h*tau.

Define rational normalized variables

t=e_3/g>0,
r_1=|f_1|/g>0, r_2=|f_2|/g>0, z=R/g>0.

The original full lift is exactly

r_1²=t²+F²,
r_2²=t²+A²,
z²=t²+n².                                     (190.1)

The reconstructed denominator is g=Den(t), since gcd(e_3,g)=1 for the primitive edge triple. Conversely take rational positive t,r_1,r_2,z satisfying(190.1), write t=p/g in lowest terms, and set e=(gA,gF,p), R=gz and |f|=(gr_1,gr_2,gn). All are integers: their squares are integers and the values are rational. The edge triple is primitive because gcd(A,F)=gcd(p,g)=1. Thus this is an exact intrinsic-height adapter, not an ambient rational box. For the K=1 population further impose gcd(gA,R)=gcd(gF,R)=1, recover h=gcd(p,R),tau=R/h and k_shared=n/h, and retain all original packet masks. g,z alone do not replace those tests.

## 3. Canonical halving on the face elliptic curve

Let a=A²,b=F², so a+b=n². Use

E_(A,F): Y²=X(X-a)(X-b).

The original point is P=(z²,-z r_1 r_2). Define its canonical half Q=(x,y) by

x=(z+r_1)(z+r_2),
y=-(z+r_1)(z+r_2)(r_1+r_2).                    (190.2)

Then x-a=(z+r_1)(r_1+r_2), x-b=(z+r_2)(r_1+r_2), so y²=x(x-a)(x-b). Direct doubling gives [2]Q=P. In particular

X([2]Q)=(x²-ab)²/(4y²)=z².

The explicit inverse on y!=0 is

z=-(x²-ab)/(2y),
r_1=-(x²-2ax+ab)/(2y),
r_2=-(x²-2bx+ab)/(2y).                         (190.3)

These are algebraic identities, not an appeal to an unproved uniform elliptic theorem. For example x²-ab=-2zy follows by subtracting (z-r_1)(z-r_2) from (z+r_1)(z+r_2). The two other identities follow by replacing z with r_1 or r_2 in the analogous calculation. Positive original roots pick the single canonical branch(190.2); signed-root witnesses are bounded and removed by canonical counting.

The actual coordinate bounds and denominators are

z²<x<4z²<=4B²/g²,
|y|<8z³<=8B³/g³,
x=(R+|f_1|)(R+|f_2|)/g²,
y=-(R+|f_1|)(R+|f_2|)(|f_1|+|f_2|)/g³.

Thus reduced Den(x)|g² and Den(y)|g³. These are numerical-coordinate and denominator bounds only, not an asserted bound for canonical height or rank. Numerical smallness of x does not by itself count rational x values of moving denominator.

## 4. The remaining original square is a split quartic

Since t²=z²-n², put w=2yt. Then

w²=H_(A,F)(x),
H(x)=(x²-A²F²)²-4n² x(x-A²)(x-F²).            (190.4)

Conversely a point on E together with w²=H and y!=0 gives t=w/(2y) and (190.3), which satisfy all three equations(190.1). Choose the positive original branch, reconstruct g and R as in section2 and apply the K=1/packet filters. Therefore this double cover is tied to BOTH missing faces and the actual space diagonal; it is not189's free conic projection.

The Pythagorean identity n²=A²+F² makes H split over Q:

H(x)=prod_(epsilon,eta in {+1,-1}) [x-(n+epsilon*A)(n+eta*F)].

One elementary derivation factors H into

[x²-2(n²+AF)x+A²F²] [x²-2(n²-AF)x+A²F²];

the discriminants are (2n(A+F))² and (2n(A-F))². Hence the four specified integral roots, not just their existence, follow. They are distinct, with

Disc(H)=4096 A^8 F^8 n^4 (A²-F²)²,
Res_x(x(x-A²)(x-F²),H)=A^8 F^8(A²-F²)^4.

The canonical positive branch has x>(n+A)(n+F), the largest of the four roots. On a nondegenerate primitive face A,F>0,A!=F the model is smooth after normalization. The original three-quadratic cover has degree8 over t, six distinct branch points and no branch at infinity; Riemann-Hurwitz gives genus5. Equivalently E plus H is degree4 over x with eight distinct branch points, again genus5. The maps above give the explicit birational dictionary on the stated open set. This verifies the full-lift shape in this chart; the genus itself is retained geometry, not a new counting gain.

## 5. K=1 descent label: one forced bit and one face-supported squareclass

For Q use the usual three root squareclasses

([x],[x-A²],[x-F²]).

All quantities on the canonical positive branch are nonzero. Because h_1=h_2=1, (e_i,|f_i|,R) is a primitive odd-hypotenuse triangle for i=1,2. Thus

[R+|f_i|]=[2] if e_i is even, and [1] if e_i is odd.

This follows directly from the primitive Euclid formulas: R+odd_diagonal=2m² or2n²; R+even_diagonal=(m+n)². Let

delta=sf(|f_1|+|f_2|)>0,
Delta_face=A²-F²!=0.

From(190.2), division by g² is a square and the exact labeled Kummer triple is

| parity of g | [x] | [x-A²] | [x-F²] |
| --- | --- | --- | --- |
| g odd (e_3 even) | 2 | delta | 2*delta |
| g even (e_3 odd) | 1 | 2*delta | 2*delta |

Entries mean classes in Q*/Q*², with products reduced modulo squares. Thus the first component is frozen to1 or2 by the ORIGINAL parity. It is not an independently moving fresh-conductor selector.

Moreover

rad(delta) | rad(2*|Delta_face|),
so delta | rad(2*|A²-F²|).                     (190.5)

Proof: set M=|f_1|+|f_2|,N=|f_1|-|f_2|. Then MN=g²(F²-A²). Also gcd(|f_i|,g)=1: modulo each prime of g the square equation gives |f_i|²=h²u², and gcd(g,h*u)=1 by181. For an odd prime outside Delta_face, if it does not divide g then it does not divide M. If it divides g, it cannot divide both M and N, since that would divide both f_i. Hence its valuation in M is either0 or2v_p(g), which is even. Only2 and primes of Delta_face can remain in sf(M).

For fixed (A,F,n), the number of candidate delta classes is at most2^omega(2|Delta_face|)=B^{o(1)}, since A,F<=B. This pays the label choices per fixed face, not the moving-face support. Standard Selmer/conductor sparsity cannot be counted a second time from(190.5). Dropping h_1=h_2=1 also invalidates the displayed forced1/2 bit without new content bookkeeping. No K>1 theorem is promoted.

## 6. Product phase is a derived function on this full cover

Choose the bounded original signs epsilon_i and let d_1=epsilon_1 r_1,d_2=epsilon_2 r_2,d_3=epsilon_3 n. The normalized integer polynomials are

Nhat=A*d_1+F*d_2+t*d_3,
Uhat=A*F*t-A*d_2*d_3-F*d_1*d_3-t*d_1*d_2,
Vhat=d_1*F*t+d_2*A*t+d_3*A*F-d_1*d_2*d_3.

Then N_T=g²Nhat,U=g³Uhat,V=g³Vhat and

Z=(Uhat+iVhat)/z³,
T=Nhat/z²,
Uhat²+Vhat²=z^6,
Nhat*Vhat=2AFt z².

These are the original189 polynomial ties expressed through(190.3)-(190.4). Reduce this actual Z to obtain a_phi,b_phi,c; use186/187 to recover q_phase,D_S,s, not an independent phase parameter. The alpha,beta>A0 and gap>D0 cutoffs from187/188 are consequently rational-function filters on this same cover. They are not extra square conditions independent of its defining equations.

## 7. What remains and next191

The full original lift has been rewritten exactly, not counted globally. Existing010/183 fixed fibers and fixed-face high genus do not sum moving (A,F,n). A per-face B^o label count from(190.5) supplies no power saving for the total support. Likewise the split roots of H do not justify multiplying four square-density probabilities; w²=H is one correlated cover equation on E.

NEXT191: target the joint moving-face count on this canonical branch, using the forced Kummer bit and delta|rad(2|A²-F²|), H(x)=w², exact g=Den(t), R=gz<=B and reconstructed K=1 h/tau/shared-k, with the actual derived phase cutoffs. Seek an averaged occupancy estimate or effective c/tau cap with all face/delta/content costs paid. Do not repeat genus5, per-face finiteness, the fixed Kummer bit, or the split-quartic identity as new credit. Any use of halfpoint heights must prove arithmetic denominator/canonical-height control; the numeric x bound alone is insufficient. Maintain the full original masks. Large-c threshold tail and K>1 low-median averaging remain separate OPEN.

## 8. Verification and authority

verify_m3_t11_190.py / M3-T11-190-verification.json PASS.2040 primitive faces check the split quartic, distinct roots, discriminant/resultant and canonical halving/inverse at t=0.2040 boundary Kummer labels match(190.5) and the g-odd row.400 nonzero finite-field full lifts over41,73,89 check doubling and exact inverse;800 signed polynomial pullbacks check norm and TY identities. Boundary/finite-field points are not positive rational endpoints. Physical endpoints enumerated=0. The general formulas and conductor statement are deductive; finite tests do not prove a moving count. Independent hostile audit NOT RUN. Separate-chat audit scope remains162–185, not186–190.

Gate OPEN, global credit0.189 projection obstruction and187/188 sectors remain;186 denominator conservation and134 fresh D-only (Q_S=M_rel²,C_u=M_G=1) remain. TI parked,120 retracted,147–149 frozen. No new whole-population saving is claimed.

## Durable sources

189: https://drive.google.com/file/d/1Euj8DJXZMXKc9IcQ5FGueAKNQ34v3V3D/view
181: https://docs.google.com/document/d/1oHsUtVShm0IfGrmdxzpTcYgQgtjSGU9n6xguGG5KVHY/edit
176: https://docs.google.com/document/d/17tR8c40SHKmjl9jUr_uw3tDe0SGWofUU9xHMsEZErJM/edit
ONE-001: https://drive.google.com/file/d/1lsDce0EAwekotfh4C7riveDy5KGJ9C33/view
ONE-005: https://drive.google.com/file/d/1VgfLATQMBCvPo_msEmdVbk7luvaiZ4sN/view
BASE-002: https://drive.google.com/file/d/1_mstAv-ua4dDq-HcmoeR-uZlQAeLk12Y/view
MAIN: https://docs.google.com/document/d/1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE/edit
CARD-INDEX: https://docs.google.com/spreadsheets/d/1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4/edit
RESULT-LEDGER: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit
SCRIPT_DRIVE_ID: 1Bao-uXeqZNd6yGfRvUC9cMTqh89ZCASV
JSON_DRIVE_ID: 1E2ypnwYuKrliVGRi_wEQIpL7yAn4DejS
