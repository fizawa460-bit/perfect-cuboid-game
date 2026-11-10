# M3-T11-196 — One-curve two-point incidence joining pair conductors to the intrinsic W receiver

CARD_ID: M3-T11-196
STATUS: EXACT_ALL_CONTENT_TWO_POINT_W_RECEIVER / PROVED_K1_FULL_PAIR_ORDINATE_COLLISION_SPLIT / FIXED_PAIR_TRACE_FIBER / SMALL_TRACE_SUBSUMED_195 / LARGE_SUPPORT_OPEN
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Authority, result and limits

Fresh MAIN, short RESULT-LEDGER, operational CARD-INDEX latest195/blank next row, card195 and active ROUTE17 were checked. Use retained192 integer W,193 signed ordinate collision,194 all-content elliptic fiber and195 complementary denominator law; no historical full reread. A bounded INDEX two-point search found no earlier indexed formulation of this receiver. The Theta below is a new pair-trace coordinate, NOT093's recombined defect theta.

Two substantive deductions:

1. ALL-content physical pair phase and192's intrinsic W map to two points on ONE integral full-2-torsion curve E_Theta:Y²=X³−Theta²X. The positive point carries the actual pair phase/Phi; the negative point carries the third edge and signed diagonal coupling. Exact integer gcd formulas embed this incidence directly in192's receiver, retaining content and primitive normalization.
2. On K=1,193's all-same collision law extends to a complete split across the two complementary unit-pair conductors: gcd(N_y,s)=gcd(|A−eta F|,s), gcd(N_y,R/s)=gcd(|A+eta F|,R/s). This describes shared conductor, not the unshared tail.

Uniform fixed nonzero Theta fibers are B^{o(1)} by the already retained uniform torsion input and finite primitive reconstruction. Their small-Theta sector is SUBSUMED by195 because |Theta|>Phi on every nondegenerate physical pair. No new primary disposal or global bound follows. A two-point incidence is not an independence theorem. The third face square, all original U,V/common-phase masks and the192 canonical branch remain required.

## 2. Physical one-curve construction

Use the original primitive positive endpoints R<=B, signed w_l=(e_l+i f_l)/R and pair i,j with complement k. Put

Q=e_i e_j+f_i f_j,
P=f_i e_j−e_i f_j,
T=e_i f_i+e_j f_j.

Retained194 gives Q²+P²=R⁴ and Q²−T²=e_k⁴. Reduce the ACTUAL pair phase to (q+i p)/c. By195, with kappa=h_i*h_j,

c=kappa*u², Phi=kappa*u|R,
q²+p²=c², gcd(q,p,c)=1,
Theta=kappa*q.                              (196.1)

Theta is signed, nonzero and |Theta|<=Phi²<=B². Physical degenerations q=0 or p=0 are excluded by194's positive-edge/face argument. No unit-content restriction enters this section.

On the same curve

E_Theta: Y²=X³−Theta²X

define the positive point

P_plus=(Phi², kappa*Phi*p)                   (196.2)

and the negative point

P_minus=(−(Phi*e_k/R)²,
         −Phi³*e_k*T/R³).                    (196.3)

For P_plus, use Phi²=kappa*c and q²+p²=c². For P_minus, multiply194's E_a map by the change X->Phi²X, Y->Phi³Y, since a=Q/R²=q/c=Theta/Phi². Both equations therefore hold exactly. The curve is nonsingular, with rational 2-torsion at0,+Theta,−Theta.

The two points encode genuinely different parts of the SAME physical endpoint: P_plus has positive integral square X; P_minus has negative rational square X. Their square-root quotient is precisely e_k/R. This is a necessary incidence, not a claim that two freely chosen curve points are endpoints.

## 3. Finite reconstruction and heights

From a fixed signed Theta and P_plus require X_plus=Phi²>0 with Phi a positive integer. Set

a=Theta/Phi²,
b=Y_plus/Phi³.

The curve equation gives a²+b²=1. From P_minus require X_minus=−r²<0 with r>0 rational and set z=r/Phi. It must satisfy0<z<1. Use194's exact reconstruction

S²=(1+a)(1−z²/a), D²=(1−a)(1+z²/a),
xi_i=(S+D)/2, xi_j=(S−D)/2,
eta_j=(a xi_j−xi_i)/b,
eta_i=b xi_j+a eta_j.

There are at most four (S,D), then finite third diagonal/sign choices. Require positive edges, the third circle eta_k²=1−z², and the signed T relation from Y_minus. Restore/check the original sign and cyclic routing. Primitive R is lcm of the three edge denominators, as194. Recompute h_i,h_j,kappa and the reduced phase; require the reconstructed Phi and Theta to satisfy(196.1), and impose192's original W/canonical branch and all original common-phase U,V and other masks. Counting a larger set of receiver pairs is only an upper bound.

All heights are polynomial uniformly in B. Theta<=B²; curve coefficient Theta²<=B⁴. X_plus<=B² and |Y_plus|<=B⁴. For the negative point X_minus=−Phi² e_k²/R² has numerator height <=B⁴ and denominator <=B²; Y_minus has numerator <=B⁶ and denominator <=B³. Thus logarithmic model and point heights are O(log B). The uniform rational-2-torsion theorem already verified in194 applies after choosing a sufficiently large absolute power of B for its height threshold. Each point set is B^{o(1)}, so their Cartesian product is B^{o(1)} without an independence assumption. Finite reconstruction proves an ALL-content fixed-Theta physical fiber B^{o(1)}. Fixing |Theta| adds only two signs.

This statement does NOT yield a large-Theta support deficit: the a priori support has size O(B²). Multiplying local selector densities, or interpreting two B^{o(1)} fibers as a moving-support theorem, is invalid.

## 4. Exact insertion into192's integer receiver

Relabel the chosen pair as1,2. Use192's canonical UNSIGNED diagonals f1^+=|f1|, f2^+=|f2|, e1=gA,e2=gF, A odd/F even under the original canonical branch. Denote the face hypotenuse by n_face, so A²+F²=n_face². Do not confuse n_face with Theta. In192 notation:

D0=2N_y*d,
L=X²−A²F²d⁴,
L1=X²−2A²Xd²+A²F²d⁴,
L2=X²−2F²Xd²+A²F²d⁴,
W²=L²−n_face² D0²,
k0=gcd(L,D0).

The intrinsic reconstruction is

R=L/k0, g=D0/k0, e3=W/k0,
f1^+=L1/k0, f2^+=L2/k0.

For the ACTUAL signs epsilon1,epsilon2 and eta=epsilon1*epsilon2 form the INTEGER polynomials

B_Q=D0² A F+eta L1 L2,
B_P=D0(epsilon1 F L1−epsilon2 A L2),
B_T=D0(epsilon1 A L1+epsilon2 F L2).          (196.4)

Exactly B_Q=k0² Q, B_P=k0² P, B_T=k0² T. Hence

B_Q²+B_P²=L⁴,
B_Q²−B_T²=W⁴.                               (196.5)

Let G=gcd(B_Q,B_P)>0. Compute the actual pair content intrinsically:

h1=gcd(D0 A,L)/k0,
h2=gcd(D0 F,L)/k0,
kappa=h1*h2.                                (196.6)

On a physical full-lift point195 implies

G=kappa*H², H=sqrt(G/kappa) is integer,
Phi=L/H, H=k0*R/Phi,
q=B_Q/G, p=B_P/G,
Theta=kappa*q.                              (196.7)

Thus the TWO points become the directly checkable receiver formulas

P_plus=(Phi²,kappa*Phi*p),
P_minus=(−(W/H)²,−W B_T/H³),
B_T²+W⁴=kappa² H⁴ q².                      (196.8)

No extra content or face scale is free here. H is determined by the SAME gcd of the original receiver polynomials, and W/k0 is the physical third edge. The original integer W, not a independently chosen rational negative point, must be used. All integrality/positivity/original inverse masks of192 remain. The gcd-square/content normalization is automatic from195 on physical points and receives no separate saving.

On K=1's unit pair kappa1, write s=Phi and v=R/s. Then H=k0*v. The sign-flipped pair has H'=k0*s, so HH'=k0*L and gcd(H,H')=k0. These are195's complementary laws transported into192; again they are reconstruction identities, not a second detector.

## 5. K=1 full-pair ordinate collision split

Use the canonical halfpoint's absolute reduced numerator N_y and UNSIGNED diagonals f_i^+, as193. For every odd p|R on the two-unit pair, g and the halfpoint denominator d are p-units, and

v_p(N_y)=v_p(f1^++f2^+).

Let s=Phi_12 be the denominator root of the ACTUAL signed ratio, v=R/s, gcd(s,v)=1. At p^lambda||v the actual two Gaussian orientations agree; at p^lambda||s they oppose. Let iota be the Hensel root of−1 modulo p^{2lambda}. The signed diagonals then give respectively

f1^++f2^+ = sigma*iota*g*epsilon1*(A+eta F)
             mod p^{2lambda}, on v;
f1^++f2^+ = sigma*iota*g*epsilon1*(A−eta F)
             mod p^{2lambda}, on s.

The multiplier is a p-unit. Truncate valuations at lambda, including primes supported on the actual content h, to obtain the EXACT gcd laws

gcd(N_y,s)=gcd(|A−eta F|,s),
gcd(N_y,v)=gcd(|A+eta F|,v).                 (196.9)

These partition the full gcd(N_y,R), since s,v are coprime.193's T0 statement is the subcase T0|v; v need not be all-same across the third direction.193's gcd(N_y,h)=1 and1 mod8 collision support stay retained. The law(196.9) does not cap s, v or their parts coprime to N_y. It isolates exactly the unshared conductor whose total occupied support is still unresolved.

## 6. Small Theta overlap; no additional sector credit

On a nondegenerate primitive integer norm-one phase, both nonzero leg numerators satisfy |q|>sqrt(c), |p|>sqrt(c). To see this, parameterize its primitive Pythagorean triple by coprime M>N>=1, c=M²+N²; the odd leg |M²−N²|>=M+N>sqrt(c) and the even leg2MN>=2M>sqrt(c).

Consequently

|Theta|=kappa*|q| > kappa*sqrt(c)
          =sqrt(kappa)*Phi >=Phi.            (196.10)

The fixed-Theta sum #E(|Theta|<=Z)<=Z B^{o(1)} is valid but its physical sector is already contained in195's Phi<=Z. It is not a new primary disposal. The full-pair gcd split only constrains shared factors; its product is the already known gcd(N_y,R), not an independent probabilistic condition. Fixed-h supported-depth compression remains177/180 already paid. None of these facts closes K=1 large-s/LargeSigmaSharp or K>1 low-median averaging.

## 7. Verification and Drive-only handoff

Exact standard-library script verify_m3_t11_196.py and machine report M3-T11-196-verification.json: PASS17572 signed unit-pair ordinate-collision checks and28 intrinsic W/two-point bridge checks, including4 nonunit-content bridges. Tests use two-circle/partial-sphere loci. The example R697 with edges672,153,104 has a missing integral third face; it is NOT an endpoint. Physical endpoints checked0. The finite checks verify identities and implementation, not the asymptotic input, full physical existence or an independent audit.

LATEST196; NEXT197. Retain the exact integer two-point receiver(196.4)–(196.8) and K=1 split(196.9), alongside195 Phi filters,194 global phase fiber,193 T0 tail,192 W/intrinsic reconstruction,180/174 sectors and134 fresh D-only. Gate OPEN/global credit0; audit162–185 unchanged;186–196 independent audit not run; TI parked120/retracted147–149/frozen.

NEXT197: work on the surviving LARGE-Theta/LARGE-Phi physical two-point incidence with W²=L²−n_face²D0², H²=G/kappa, actual signed B_T, integral third face and original U,V,N_T/Den(S) masks retained. Seek a summed occupied-support deficit or a nonredundant correlation controlling the unshared conductor; counting fixed Theta or independently choosing two elliptic points is insufficient. On K=1 use(196.9) to separate shared face factors from the unshared tail, without capping that tail. No new density product or old-sector re-charge. K>1/large-c averaging remains separately OPEN. MAIN/INDEX/short LEDGER should link here/NEXT197; detailed proof stays in this card.

## 8. Artifact IDs

SCRIPT=1fkDWf9hT8_2hf3CeBfwD4FHmQN0o2HrP
JSON=1sjr2aCrUm-E-F-VxKWQ9bg0da_3UcZe2
Both are in Stage37 verification research auxiliaries; this card is in the research-card folder.
