# M3-PESCH-TI-004 — Legendre matrix rank bound and exact Master pair kernel

CARD_ID: M3-PESCH-TI-004
CANONICAL_CARD_KEY: M3-PESCH-TI-004
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-PESCH-TI-004
現行一覧の状態: PROVED / IN_SESSION_SCOPED_AUDIT_PASS
種別: LEGENDRE_MATRIX_RANK_BOUND / EXACT_MASTER_PAIR_KERNEL
要点: 任意sourceで rank E3<=delta。G_torかつdelta=0ならTI_CLOSED。
主張の抜粋: 3局所character lemma; 2 F2 matrices。Master逆変換が一意でmu=h/2。
対象・測度: Exact primitive canonical physical R<=B; gcd scaling and face-square retained.
依存関係: TI-001/002/003; M3-MASTER-001。無限族・密度・saving未証明。
再開条件の抜粋: PARKED_BY_EXPLICIT_USER_REQUEST / 既存結果保持。現在のprimaryはM3-T11-GATE-001。通常stage37mainbatchでTIを自動再開しない。TI再開時は最新TI-005からTI-006へ。1072 HOLD、global saving未証明。
旧詳細位置: audit 1EqGhddWUTK8Gn7QmnWyFBrUa6Uo3_RAk; producer 1tJmFcYcFr5S0z2JR6bBT6oQdiU7-gQdK; verifier 1DkZ9nC5hBshjJO_g6dIdLWbw5sTt8Ie4
旧詳細リンク: https://drive.google.com/file/d/1dUz306uHWV6DwqybIGLUUeO6w1fpWcFK/view
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 1078931
SOURCE_END: 1083555
SOURCE_SHA256: e14d6e1c91d1ea6eea027f7eb8832e58ca7e47dff816f7a22d34889cadd60ecc

M3-PESCH-TI-004 — UNIFORM LEGENDRE RANK BOUND / EXACT MASTER PAIR KERNEL
DATE=2026-09-30
CARD_FILE_ID=1dUz306uHWV6DwqybIGLUUeO6w1fpWcFK
AUDIT_FILE_ID=1EqGhddWUTK8Gn7QmnWyFBrUa6Uo3_RAk
PRODUCER_SCRIPT_FILE_ID=1tJmFcYcFr5S0z2JR6bBT6oQdiU7-gQdK
INDEPENDENT_VERIFIER_SCRIPT_FILE_ID=1DkZ9nC5hBshjJO_g6dIdLWbw5sTt8Ie4
EXAMPLES_JSON_FILE_ID=1RyG0ixHBVJq7BKJArkGsHIqWWFNKQ2YM
VERIFICATION_JSON_FILE_ID=1IbRM6zZt0nVmgTNltC6uooo2dwvkdBAe
STATUS=PROVED / WITHIN_SESSION_SCOPED_ADVERSARIAL_AUDIT_PASS
Three character lemmas give two F2 matrices A,B and rank E3<=delta=(omega(U)-rank A)+(omega(2VW)-1-rank B). delta=0 on G_tor proves TI_CLOSED. delta>0 is UNKNOWN, not positive rank.
K_char is a uniform sufficient arithmetic criterion; no infinitude or density theorem. Existing (4,1),(9,4) independently reverified, no new source count.
Unique primitive canonical Master inverse gives h_B(p,q) equal to the exact face-square indicator times the existing physical R cutoff, and mu_B=h_B/2 off diagonal, zero on diagonal. This is an exact kernel identity, not a weight bound.
P<=R_DD+2F(X_tor), D_char=G_tor intersect {delta>=1}, X_tor=17017|UVW. Both residual weights unbounded here.
Independent full-pair verifier:28 cover obstructions; binary kernel checks; independent primitive edge enumeration maxedge<=300 with2 reconstructed bricks. Diagnostic cutoff does not replace physical R.
NEXT=TI-005: obtain defect/exception weight bounds on this exact square locus. 1072 HOLD; gate OPEN; all asymptotic/nonexistence flags false.


CURRENT AUTHORITY CONTROL — TI-004 Legendre matrix bound and exact Master kernel
PRIMARY_GATE=M3-PESCH-TI-GATE-001
PRIMARY_GATE_STATUS=OPEN
ACTIVE_ROUTE=M3-PESCH-TI-ROUTE-MAIN
ACTIVE_ROUTE_FILE_ID=198IsZ3zb1FRRbnO3BLiyqCJglDFw_4AU
LOAD_BEARING_CARD=M3-PESCH-TI-001
LOAD_BEARING_CARD_DOC_ID=1Tmy_8CX29vqVaJah5WhOuTyzDrqveeYOdCvH9MVt-9U
ACTIVE_RESEARCH_CARD=M3-PESCH-TI-004
ACTIVE_RESEARCH_CARD_FILE_ID=1dUz306uHWV6DwqybIGLUUeO6w1fpWcFK
LATEST_RESEARCH_CARD=M3-PESCH-TI-004
LATEST_AUDITED_RESEARCH_CARD=M3-PESCH-TI-004
LATEST_AUDIT_FILE_ID=1EqGhddWUTK8Gn7QmnWyFBrUa6Uo3_RAk
LATEST_PRODUCER_SCRIPT_FILE_ID=1tJmFcYcFr5S0z2JR6bBT6oQdiU7-gQdK
LATEST_INDEPENDENT_VERIFIER_SCRIPT_FILE_ID=1DkZ9nC5hBshjJO_g6dIdLWbw5sTt8Ie4
LATEST_EXAMPLES_JSON_FILE_ID=1RyG0ixHBVJq7BKJArkGsHIqWWFNKQ2YM
LATEST_VERIFICATION_JSON_FILE_ID=1IbRM6zZt0nVmgTNltC6uooo2dwvkdBAe
LATEST_CARD_STATUS=PROVED_UNIFORM_CHARACTER_RANK_BOUND_AND_EXACT_MASTER_PAIR_KERNEL / WITHIN_SESSION_SCOPED_AUDIT_PASS
E3_UNIFORM_MINIMAL_SEMISTABLE_MODEL_PROVED=true
E3_TORSION_FOUR_ON_G_TOR_PROVED=true
UNCONDITIONAL_MODULAR_RANK_ZERO_CERTIFIER_PROVED=true
UNIFORM_LEGENDRE_RANK_UPPER_BOUND_PROVED=true
EXACT_MASTER_PAIR_KERNEL_PROVED=true
E3_RANK_ZERO_ARITHMETIC_CRITERION_PROVED=true
E3_INFINITE_RANK_ZERO_FAMILY_PROVED=false
E3_RANK_ZERO_ARITHMETIC_FAMILY_PROVED=false
FAMILY_FLAG_SCOPE=The uniform K_char criterion is proved; existence of an infinite family or density theorem is not.
M3_PESCH_TI_1072_AGGREGATE_STATUS=HOLD
M3_PESCH_TI_WEIGHTED_HARD_LOCUS_SAVING_PROVED=false
NEXT_RESEARCH_CARD_ID=M3-PESCH-TI-005
NEXT_T11_RESEARCH_CARD_ID=M3-T11-122
PROVISIONAL_FRONTIER_CARD=NONE
PROVISIONAL_FRONTIER_AUDIT_STATUS=NOT_APPLICABLE
CURRENT_ATTACK=MatrixDefectOnExactMasterSquareLocus|PhysicalExceptionalMarginal
NEXT_LEGAL_ACTION=Read active route latest TI-004 section, card, audit and replay files. Study delta>0 on the exact Master pair kernel with unchanged physical R cutoff; bound joint D_char mass and X_tor marginal. Do not relabel delta>0 as positive rank or finite tests as an infinite family.
CHARACTER_RECEIVER=P(B)<=R_DD(B)+2 sum_{p in X_tor}F_B(p); D_char={p in G_tor:delta(p)>=1}, X_tor={17017|UVW}. Neither physical weight is evaluated.
PAIR_KERNEL=mu_B(p,q)=h_B(p,q)/2 for distinct primitive sources; diagonal zero. h_B requires exact Master face square and existing canonical physical R<=B. Unique oriented source pair proved.
PRIMARY_RECEIVER=P(B)<=R_HH(B); weighted o(M3) remains unproved.
WEIGHT_FIREWALL=No raw source density transfer, no independence, no numerical physical mass, no new finite-source count versus TI-003 or external1072.
GOAL_UNCHANGED=P(B)/M3(B)->0 on exact primitive canonical physical R<=B.
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
T11_121_RESEARCH_STATUS=RETAINED_PROVED_EXACT_STRUCTURE / PARKED_PRIMARY_RESEARCH
T11_120_STATUS=RETRACTED_PHYSICAL_ADAPTER
HISTORICAL_MAIN_RECORD_BELOW=Lower historical continuation pointers are superseded by this control; audited mathematical scopes remain.

## Retained standalone source — M3-PESCH-TI-004.md
SOURCE_FILE_ID: 1dUz306uHWV6DwqybIGLUUeO6w1fpWcFK
SOURCE_URL: https://drive.google.com/file/d/1dUz306uHWV6DwqybIGLUUeO6w1fpWcFK/view?usp=drivesdk

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
