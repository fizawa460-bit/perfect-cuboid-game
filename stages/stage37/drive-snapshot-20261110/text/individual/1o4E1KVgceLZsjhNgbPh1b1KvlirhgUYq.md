# M3-T11-192 — All-content fixed-ordinate divisor fibers and an intrinsic integer full-lift receiver

CARD_ID: M3-T11-192
STATUS: PROVED_ALL_CONTENT_FIXED_ORDINATE_DIVISOR_FIBER / EXACT_INTEGER_RECEIVER / SMALL_ORDINATE_SUBSUMED_163 / OCCUPIED_SUPPORT_OPEN
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Current authority and result
Fresh MAIN, operational CARD-INDEX latest191/blank next row, short RESULT-LEDGER, active ROUTE17 and latest191 were checked. Bounded INDEX searches for fixed Y, Y² and halfpoint locate190/191 but no indexed earlier fixed-ordinate result. No historical full reread. Continue191's lost-content numerator transfer; use190's original full lift, not189's independent-phase projection.

New theorem: the absolute REDUCED numerator N_y=|Num(y)| of the canonical elliptic halfpoint has a divisor-many endpoint fiber, summed over ALL content, faces, rational denominators and descent labels. No fixed-face elliptic theorem or outer h/C multiplier is required for this fiber. Its proof provides an exact integer receiver reconstructing g,R,edges and diagonals before any phase variable is introduced. Moving N_y support is still unbounded at the needed power. Small N_y is covered by163; no new sector disposal/global credit.

All original positive primitive endpoints R<=B, canonical face/sign/orientation/cyclic routing,134 four-square/intrinsic-R tests and current phase filters are retained. The ALL-content fiber below does not extend190's K=1-only forced Kummer table to K>1. Large-c threshold tail and K>1 low-median averaging remain OPEN.

## 2. Denominators and height needed here extend without the K=1 parity table
For a canonically selected face let e1=gA,e2=gF, gcd(A,F)=1, A odd,F even, A²+F²=n². Define t=e3/g,r1=|f1|/g,r2=|f2|/g,z=R/g as190. Primitivity gives gcd(e3,g)=1. Since R²=e3²+g²n², also gcd(R,g)=1, independent of the individual h_i=gcd(e_i,R).

Use the canonical190 point

x=(z+r1)(z+r2), y=-x(r1+r2),
y²=x(x-A²)(x-F²).

Its initial expression has Den(x)|g². The valuation argument for an integral monic elliptic cubic (191 section2) shows that its exact reduced denominators are d²,d³ for an integer d|g:

x=X/d², y=-N_y/d³,
X,N_y,d positive; gcd(X,d)=gcd(N_y,d)=1.        (192.1)

This general denominator fact does not use primitive individual space triangles. The191 odd-prime/2-adic denominator selection rule also extends here: its proof only needs R,f1,f2 to be units at primes of g, which follows from gcd(R,g)=1 and f_i²=R²-e_i². The odd prime powers are all retained or all removed; at2 use the same191 formula. No individual primitive space triangle is needed. The frozen squareclass1/2 and Kummer table from190 remain K=1-only.

Moreover r1²+r2²=z²+t², so r1+r2>z. Consequently x, x-A² and x-F² are all >z². Their upper bounds are each <4z². Hence

n³d³ < (Rd/g)³ < N_y < 8(Rd/g)³ <=8B³.       (192.2)

The upper bound follows directly from |y|=x(r1+r2)<8z³. These are ordinary reduced-integer heights, with no canonical-height or rank assertion.

## 3. Pure divisor reconstruction: no moving-face multiplier
Clear the denominators in the elliptic equation:

N_y² = J0 J1 J2,
J0=X,
J1=X-A²d²,
J2=X-F²d²,                                  (192.3)

with all J_i positive integers. Fix N_y. Each J_i is a divisor of N_y²; choosing J0,J1 determines J2. There are at most tau_div(N_y²)² ordered triples, where tau_div denotes the integer divisor function (not residual tau).

For each triple require J0-J1 and J0-J2 to be positive integer squares. Put

a_d=sqrt(J0-J1), f_d=sqrt(J0-J2),
d=gcd(a_d,f_d), A=a_d/d, F=f_d/d.             (192.4)

Thus ONE triple recovers d and the entire primitive face legs, not just a fixed-face point. Require the chosen parity/order, n²=A²+F² to be an integer square, reduced conditions(192.1), and the original190 canonical branch. Then x,y and the full face curve are fixed. delta, if used on K=1, is derived rather than summed separately. g is also derived below, not an independent scale choice.

This is the reason the fixed-N_y theorem has no outer count of faces, contents, denominators or delta labels. Their dependence is exact gcd/divisor arithmetic.

## 4. Integer quartic square and exact intrinsic reconstruction
For a candidate in section3 define

D0=2N_y d,
L=X²-A²F²d⁴,
L1=X²-2A²Xd²+A²F²d⁴,
L2=X²-2F²Xd²+A²F²d⁴.                         (192.5)

The remaining190 square becomes the INTEGER square condition

W² = L²-n²D0², W>0.                          (192.6)

Indeed H(x)=w² and w=2yt imply W=|w|d⁴; t=W/D0 and z=L/D0. Require L,L1,L2>0 and the original canonical positive branch (equivalently retain the190 halfpoint/inverse tests).

Let

k0=gcd(L,D0).                                (192.7)

Then, on a full-lift candidate,

g=D0/k0, R=L/k0, e3=W/k0,
e1=gA,e2=gF,
|f1|=L1/k0, |f2|=L2/k0, |f3|=gn.             (192.8)

The letter k0 here is a normalization gcd, NOT181's shared k. Keep n=h*k_shared only on the K=1 subpopulation.

No additional denominator equality may be charged as a saving. For any integers L,W,D0,n satisfying(192.6),

gcd(W,D0)=gcd(L,D0)=k0.                      (192.9)

Proof prime by prime: let v=v_p(D0). If v_p(L)<v, the difference W²=L²-n²D0² has valuation2v_p(L), so v_p(W)=v_p(L). If v_p(L)>=v, then W² is divisible by p^(2v), so v_p(W)>=v. The two gcd valuations, capped at v, agree at EVERY prime, including2. Thus Den(t)=Den(z)=g is automatic from this original square, not a fresh selector. It also implies k0|W, gcd(e3,g)=gcd(R,g)=1.

Require k0|L1,L2 (equivalently recover the integral diagonals) and verify the190 rational inverse/canonical equations; on an actual full-lift point these divisibilities follow because the rational diagonal squares become integers. The reconstructed edges are primitive because gcd(A,F)=1 and gcd(e3,g)=1. Apply R<=B, original parity/cyclic/content/orientation masks and all remaining exact original tests. For K=1 also require gcd(gA,R)=gcd(gF,R)=1 and recover h=gcd(e3,R),tau=R/h,k_shared=n/h. For general content compute every h_i directly and impose the retained common-content relations. No assumed h ceiling enters(192.8).

191's lost factor is now exact:

ell_lost=g/d=2N_y/k0, so k0=2N_y/(g/d).       (192.10)

It is a normalization determined by the same factors/quartic, not another freely moving label. Additionally gcd(L,W)=k0*gcd(R,e3); the physical third content is recovered exactly. This gcd may be used as a filter, but does not by itself bound occupied support.

## 5. All-content fixed-ordinate endpoint theorem
For the current canonical physical population define N_y by deterministic face routing and the positive halfpoint above. Sections3–4 show that each ordered factor triple gives at most O(1) canonical endpoint/sign witnesses: x,y,face,d are recovered, W has one positive choice, and g,R and all physical integers are reconstructed. Remaining masks only discard candidates. Thus uniformly for1<=N<=8B³,

m_Ny(N;B)
= #{primitive canonical original endpoints R<=B with N_y=N}
<= O(tau_div(N²)²)=B^{o(1)}.                  (192.11)

This includes ALL face/content/denominator choices. It is an elementary divisor proof and uses no retained uniform elliptic rational-point bound. In particular there is no outer C or C^(3/2) multiplier.

Let O_y(B) be the occupied integer N_y support in the same physical population. Then

|O_y| <= #E(B) <= B^{o(1)} |O_y|.             (192.12)

A sufficient new upper target would be |O_y|<<B^(1/3-epsilon), fixed epsilon>0, or an explicit occupancy envelope with the fiber loss paid. The whole interval N<=8B³ is not an occupied-support bound of that size. Fibers cannot be multiplied by the retained183 fixed-c fibers as independent density gains.

On the current finite nonzero phase population, fixed-c fibers183 and fixed-N_y fibers192 make the joint occupied (c,N_y) relation bounded-degree B^o on both sides. Thus their occupied supports are power-equivalent through the SAME physical endpoints. Moving to N_y does not settle the large-c gate by a change of label. It does supply the explicit integer equations in sections3–4 for a future coupling proof.

## 6. Small-ordinate sector is old, not new credit
From(192.2), N_y<=Z implies n<Z^(1/3)/d<=Z^(1/3), and hence the primitive face short leg min(A,F)<Z^(1/3). Retained163 gives, summed over every face/content,

#E(N_y<=Z) <= Z^(1/3) B^{o(1)}.               (192.13)

This improves the bare sum Z B^o of(192.11), but its proof is precisely inclusion in163. It creates NO new disposal. For Z=B^(1-epsilon), fixed epsilon>0, it is negligible on the retained M3 benchmark, already covered by old short-face deletion.

Conversely the163 interior min(A,F)>E forces N_y>(nd)³>(Ed)³. All-three-face routing remains in force. Therefore one cannot dispose the residual simply by calling N_y an ordinary integer with small fixed fibers. The occupied large-integer support remains OPEN.

## 7. Original phase and NEXT193
Reconstruct the actual e_i,R,|f_i| from(192.8), then use only bounded original signs f_i. Compute the ORIGINAL polynomials

U=e1e2e3-e1f2f3-e2f1f3-e3f1f2,
V=f1e2e3+f2e1e3+f3e1e2-f1f2f3,
N_T=e1f1+e2f2+e3f3.

Reduce by G_phase=gcd(U,V) to obtain b_phi=U/G_phase,a_phi=V/G_phase,c=R³/G_phase. The actual common-u/product phase and186 q_phase/D_S follow; apply187/188 both-legs-large and gap-large tests,134 full-S/fresh D-only and all physical filters. A separate assigned phase triangle is prohibited by189. The normalization gcd k0 is unrelated to G_phase unless a further theorem proves a relation.

NEXT193: attack occupied N_y support (or its power-equivalent c support) using the simultaneous positive factor product, two square differences, primitive face square, INTEGER W square, exact normalization/height and actual phase pullback. Seek a summed correlation/c,tau cap on the163 interior; do not repeat fixed-N_y fibers or small-N_y inclusion as global credit. Pay every moving label, and do not charge(192.9), forced bits or correlated square factors independently. If these constraints produce only old-support relabeling, record that obstruction and return to the same large-c/full-S joint gate rather than claiming closure. Large-c threshold tail and K>1 low-median averaging remain separately OPEN.

## 8. Verification and audit scope
verify_m3_t11_192.py / M3-T11-192-verification.json PASS:6585 pairs of two primitive space triangles replay positive factor product, square differences, exact gcd recovery of d,A,F,g,R and both diagonal numerators.1639 further two-triangle pairs with non-unit individual contents replay the same divisor/intrinsic reconstruction, without a K=1 assumption.2040 primitive-face ZERO-third-edge boundaries replay the full integer W receiver and N_y bounds.16320 scaled integer right-triangle examples replay(192.9). Two-triangle and scaled examples are over-cover tests; zero-edge boundaries are not positive endpoints. Physical endpoints enumerated=0. All-content extension/fiber bound is deductive, not claimed independently audited. No independent hostile audit performed. Separate-chat audit scope remains162–185, not186–192.

No retraction.190 K=1 forced-bit/Kummer table remains scoped;191 denominator selection is extended as proved in section2.189 obstruction,187/188 sectors,186 conservation,183 fibers,180/181 filters and134 fresh D-only (Q_S=M_rel²,C_u=M_G=1) are retained. TI parked,120 retracted,147–149 frozen. Gate OPEN, global credit0.

## Durable references
191: https://drive.google.com/file/d/1ClMIXWd8nOdC9ZVVjeCdaLo_nhLHwkZ9/view
190: https://drive.google.com/file/d/1r94c4fxMP3SXlWFh13JviKo0t7-ld9SV/view
163: https://docs.google.com/document/d/1Iz44vneEdanTNfZq7BRrNrl6ns26GTYze4--BVJ36V4/edit
183: https://docs.google.com/document/d/156OI672uaTABWO1UaogndaieH8kYIUL7LFizZATcqGg/edit
MAIN: https://docs.google.com/document/d/1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE/edit
CARD-INDEX: https://docs.google.com/spreadsheets/d/1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4/edit
RESULT-LEDGER: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit
SCRIPT_DRIVE_ID: 1I7Y2aJQh9QlxHNv8MpiXS_OQelOLlqOi
JSON_DRIVE_ID: 18ggozzDBkF5lFyV4w8gY46VtFRcWXSW2
