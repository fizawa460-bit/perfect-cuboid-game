# M3-PESCH-TI-004 — Legendre matrix rank bound and exact Master pair kernel

DATE=2026-09-30
STATUS=PROVED_UNIFORM_SUFFICIENT_CRITERION_AND_EXACT_PAIR_PULLBACK
PRIMARY_GATE=M3-PESCH-TI-GATE-001 / OPEN
DEPENDENCIES=TI-001 endpoint adapter; TI-002 torsion screen/Fermat nonsquare VW; TI-003 two-isogeny descent normalization; M3-MASTER-001 primitive canonical coverage.
No infinite-family cardinality, density, physical weight saving or limit credit. External1072 aggregate HOLD.

## 1. Parameter-uniform local character lemmas

Let p=(m,n), m>n>0, gcd(m,n)=1, opposite parity. U=m²−n², V=2mn, W=m²+n² are pairwise coprime, U odd, 4|V, U²+V²=W². Put S=V²+W².
E: y²=x³−2Sx²+U⁴x; E': y²=x³+4Sx²+16V²W²x.
TI-003 supplies 2^r=|alpha(E)| |alpha(E')|/4 and primitive integral covers
c²=d z⁴+a z²t²+(b/d)t⁴, gcd(z,t)=1.
E-image representatives are positive squarefree d|rad(U) (negative x gives negative cubic). E' representatives are signed squarefree products of primes dividing 2VW. The classes ±1, ±sf(VW) occur in E'; sf(VW)>1 by TI-002.

L1. For every odd q|VW, each E-image d satisfies (d/q)=+1.
Proof: q∤Ud, S is a nonzero square modulo q, and U⁴≡S². The cover reduces to d(z²−S t²/d)². If d is nonsquare, c=0 and z²=S t²/d; the latter forces z=t=0 modulo q, contradicting primitivity.

L2. If q|U and q≡3 mod4, q cannot divide an E-image d.
Proof: assume q|d, let e=v_q(U). In c²+2S z²t²=d z⁴+(U⁴/d)t⁴, 2S≡4V² modulo q is a nonzero square. Since −1 is nonsquare, the valuation on the left is even, namely twice the minimum valuation of c and zt. Right valuations are 1+4v_q(z) and 4e−1+4v_q(t), distinct modulo4; their minimum is odd with no cancellation. Contradiction. Zero z/t is handled by infinite valuation; both cannot vanish.

L3. For every q|U with q≡1 mod4, each E'-image d satisfies (d/q)=+1.
Proof: q∤dV, S≡2V² and 16V²W²≡16V⁴. The cover reduces to d(z²+4V²t²/d)². If d is nonsquare, z²=−4V²t²/d forces z=t=0, because −1 is square. This deliberately asserts nothing at q|U with q≡3 mod4. The sign of d is irrelevant for L3. No 2-adic lemma is claimed.

## 2. Two F2 matrices and a rank upper bound

A(p): columns primes u_i|U. Rows: unit row for each u_i≡3 mod4 (L2); character row [epsilon((u_i/q))]_i for each odd q|VW (L1). epsilon(+1)=0, epsilon(−1)=1.
B(p): columns primes v_j|2VW, including2. Rows [epsilon((v_j/q))]_j for each q|U, q≡1 mod4 (L3).
k=omega(U), l=omega(2VW).
delta_E=k−rank_F2(A), delta_dual=l−1−rank_F2(B), delta=delta_E+delta_dual.

The image inclusions give |alpha(E)|<=2^delta_E and |alpha(E')|<=2^(l−rank(B)+1), accounting for the free sign. Thus
**rank E3(p)(Q) <= delta(p).**
The nonzero exponent vector of sf(VW) lies in ker B, so rank(B)<=l−1 and delta_dual>=0. This is a rank upper bound, not a formula for the rank: delta>0 remains UNKNOWN and may include rank-zero curves.

G_tor={p: some q in {7,11,13,17} does not divide UVW}; X_tor={p:17017|UVW}.
K_char={p in G_tor:delta(p)=0} is unconditionally TI_CLOSED by TI-001/002. This is a uniform arithmetic criterion over every primitive source, with nonempty examples; no proof K_char is infinite or has any density is asserted.
D_char={p in G_tor:delta(p)>=1}. Every endpoint source belongs to X_tor union D_char. With the SAME physical measure from the active route,
P(B)<=R_DD(B)+2 sum_{p in X_tor}F_B(p).
Neither term is proved o(M3(B)). Two-source independence is not assumed.

Examples (already certified in TI-003, no new finite-source credit):
p=(4,1): A columns[3,5], rows[1,0],[1,1], rank2; B columns[2,17], row[1,1], rank1. delta=0.
p=(9,4): A columns[5,13], rows[1,0],[1,1], rank2; B columns[2,3,97], rows[1,1,1],[1,0,1], rank2. delta=0.

## 3. Exact Master inverse and source-pair kernel

Use canonical primitive nondegenerate Euler bricks, odd edge X and even edges Y<Z; apply the existing Stage37 canonicalization for R_phys. Every primitive Euler brick has exactly one odd edge: two odd edges would give a face square=2 mod4, and all even violates primitivity. Y=Z is impossible since their diagonal would have square 2Y².
Set d1=gcd(X,Y), d2=gcd(X,Z). Reducing the two faces gives unique primitive Euclid sources p,q with (U_p,V_p)=(X/d1,Y/d1), (U_q,V_q)=(X/d2,Z/d2). Because gcd(d1,d2)=gcd(X,Y,Z)=1 and d1d2|X,
g=gcd(U_p,U_q)=X/(d1d2).
Consequently X=U_pU_q/g, Y=V_pU_q/g, Z=U_pV_q/g. The source pair is unique with V_p/U_p<V_q/U_q. Distinct primitive sources cannot have equal ratios (unique reduced triple).

Conversely primitive sources p,q with that strict orientation reconstruct primitive coordinates: gcd(X,Y)=U_q/g, gcd(X,Z)=U_p/g, whose gcd is1. Two face diagonals are integers. The remaining face is integral exactly when
K_pq²=(V_pU_q)²+(U_pV_q)² is an integer square; then g|K_pq and D=K_pq/g. Hence an exact bijection with primitive canonical M3 objects.

Define h_B(p,q)=1_{K_pq² is a square} * 1_{R_phys(canon(X,Y,Z))<=B} for p!=q; zero on the diagonal. R_phys is the existing Stage37 height without any substitution by max edge, m or n.
w_B(p,q)=1_{V_pU_q<U_pV_q} h_B(p,q).
Then M3(B)=sum_{p,q}w_B(p,q), and the prior symmetric measure becomes exactly
mu_B(p,q)=h_B(p,q)/2 for p!=q; mu_B(p,p)=0.
In particular F_B(p)=1/2 sum_{q!=p}h_B(p,q) and
R_DD(B)=sum_{p,q}w_B(p,q)1_{D_char}(p)1_{D_char}(q).
These identities make the square locus, gcd scaling and physical cutoff explicit. They give no upper bound on the sums. Bare source-box density cannot replace this kernel; it can be used only after proving a transfer through h_B.

## 4. Verification and scope

Producer ti004_legendre.py uses integer factorization, Legendre symbols and F2 elimination, no Sage/GRH/BSD. Independent audit ti004_audit.py enumerates full primitive pairs moduloq or243 for28 obstructed covers in the two examples, rather than using character tests as the verifier; binary kernel enumeration checks matrix ranks. It separately enumerates primitive integer Euler bricks with max edge<=300 and recovers exactly two: (X,Y,Z)=(117,44,240), sources(11,2),(8,5),g39,D244; (275,240,252), sources(8,3),(18,7),g55,D348. This max-edge cutoff is a test fixture, not a Stage37 physical R cutoff. Universal validity rests on the proofs above, not on those finite tests.

Sources: Stage37 cards named above; official two-isogeny documentation for descent normalization: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/descent_two_isogeny.html . The three local lemmas, matrix bound and exact inverse are proved here.

NEXT=M3-PESCH-TI-005: study delta defects directly on the exact Master square locus with physical R cutoff; seek a family/weight theorem for R_DD and the X_tor marginal. First distinguish new uniform structure from a renamed local condition. No blind expansion of finite rank tables. If no weighted saving is obtained, record the obstruction. Existing T11-121 remains valid parked auxiliary structure; no claim TI is already better. A comparison horizon of5–10 substantive batches is an operational estimate, not a mathematical forecast.
FLAGS: UNIFORM_LEGENDRE_RANK_UPPER_BOUND_PROVED=true; EXACT_MASTER_PAIR_KERNEL_PROVED=true; RANK_ZERO_CRITERION_PROVED=true; INFINITE_RANK_ZERO_FAMILY_PROVED=false; WEIGHTED_HARD_LOCUS_SAVING_PROVED=false; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false; TI_1072_AGGREGATE_STATUS=HOLD.
