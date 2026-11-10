# M3-T11-193 — Signed face/ordinate collision law and an all-content cubic-divisor tail

CARD_ID: M3-T11-193
STATUS: PROVED_K1_SIGNED_ORDINATE_PHASE_COLLISION / PROVED_ALL_CONTENT_T0_CUBIC_TAIL / K1_CLOSING_RANGE_SUBSUMED_SMALL_TAU / JOINT_GATE_OPEN
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Authority and new results
Fresh Drive MAIN, operational CARD-INDEX latest192/blank next row, short RESULT-LEDGER, active ROUTE17 and192 were checked. Only needed181/184/186 were fetched; bounded INDEX searches for cubic-divisor and Z/D² locate184/186. Historical full reread was not used.

Two results advance the current system without pretending fixed fibers close moving support:
1. On K=1,192's reduced ordinate numerator N_y is coprime to the actual content h. Its collision with R is supported on primitive face A²-F² and primes1 mod8. The collision with the ACTUAL fresh all-same core T0 is exactly a signed face-leg-sum gcd, not an independent phase label.
2. Summing the integer cubic-divisor condition T0³|c with183's ALL-content fixed-c fiber removes the unnecessary outer C from184's displayed tail estimate. The resulting all-content bound is Z/D² B^o. This is an improved scoped upper theorem. For K=1 its closing range is already the retained small-tau sector; the primary K=1 interior is not closed by it.

Keep original positive primitive endpoints R<=B, corrected finite nonzero common-u phase, all134 four-square/intrinsic-R/content/orientation/cyclic masks. TI parked,120 retracted,147–149 frozen. No independent density products or endpoint lower bounds. Large-c threshold tail and K>1 low-median averaging remain OPEN.

## 2. Distinguish the unsigned halfpoint from the signed original phase
On K=1 relabel h1=h2=1,h3=h. Use181/190/192:

e1=gA,e2=gF,A²+F²=n²,gcd(A,F)=1,A odd,F even,
n=h*k_shared,R=h*tau,gcd(g,R)=1.

Do NOT assume gcd(h,tau)=1; that is not a retained hypothesis.

Let r_i^+=|f_i| be the positive actual diagonals and let epsilon_i in{±1} be the retained original phase signs, so f_i=epsilon_i*r_i^+. The canonical halfpoint uses r1^+,r2^+ regardless of these phase signs:

x=(R+r1^+)(R+r2^+)/g²,
y=-(R+r1^+)(R+r2^+)(r1^++r2^+)/g³.

Write x=X/d²,y=-N_y/d³, d|g, gcd(X,d)=gcd(N_y,d)=1 as192. Let

M_plus=r1^++r2^+,
Delta=A²-F²,
eta=epsilon1*epsilon2.                       (193.1)

The unsigned M_plus and the signed original phases must not be conflated. In particular the face factor coupled to T0 below is |A+eta F|, and is not always A+F.

## 3. K=1 ordinate/content and R-collision law
At every odd prime p|R, the first two K=1 triangles are primitive, so e1,e2,r1^+,r2^+ are p-units. Also g,d are p-units. Thus

v_p(N_y)=v_p(M_plus).                         (193.2)

Indeed both R+r_i^+ are units; the denominator cancellation by g/d is also a unit at p. Furthermore

M_plus*(r1^+-r2^+)=g²(F²-A²).                 (193.3)

If p|M_plus, then r1^+-r2^+ is a p-unit, since p is odd and the two diagonals are units. Therefore v_p(M_plus)=v_p(Delta) on every such collision prime. It follows that

gcd(N_y,R) divides gcd(|Delta|,R).            (193.4)

For a primitive odd-hypotenuse face, gcd(n,Delta)=1: a common odd prime would divide both A²+F² and A²-F², hence A,F;2 does not divide n. Since h|n, (193.4) implies

gcd(N_y,h)=1.                                (193.5)

This is actual endpoint content h, not the face scale g or192's normalization gcd k0. Those may divide the ordinate numerator.

If p divides gcd(N_y,R), then p|Delta and A,F,n are p-units, with n²=2A² modp. Thus2 is a quadratic residue at p. The primitive space triangle also makes -1 a quadratic residue at p. The two elementary residue conditions give

p=1 mod8 for every p|gcd(N_y,R).              (193.6)

In particular all p=5 mod8 dividing R are ordinate units. This is a local compatibility statement, not an independently chargeable density or a fixed-power saving. The proof is K=1-only here; no all-content collision law is asserted.

## 4. Exact signed coupling to the all-same fresh core
Define T0 as in184/186: product of full prime powers p^lambda of R outside H_content for which the THREE ACTUAL Gaussian phase orientations agree. In K=1 H_content=h. Relative fresh prime powers belong to M_rel. These choices come from signed w_i=(e_i+i f_i)/R, not from an assigned phase triangle.

At p^lambda||T0 all e_i and f_i are p-units. Choose a Hensel root iota of -1 modulo p^(2lambda). Because e_i²+f_i²=R², same orientation gives

f_i = sigma*iota*e_i mod p^(2lambda)

for one common sigma=±1. Hence

M_plus = sigma*iota*g*(epsilon1 A+epsilon2 F)
         mod p^(2lambda).

Using(193.2) and truncating at lambda gives the EXACT integer identity

gcd(N_y,T0)=gcd(|A+eta F|,T0).                (193.7)

This includes all prime-power depths, not just radical support. Since A±F are coprime odd integers, every collision prime on the OTHER signed face factor |A-eta F| forces the first two actual phase orientations to be opposite and hence cannot belong to T0. Thus

p|gcd(N_y,R,A-eta F) implies p does not divide T0. (193.8)

The third orientation still matters when the first two agree: it may be relative. No converse “same first two implies T0” is claimed. No cap for the whole T0 follows from(193.7), because it bounds only its shared part with N_y. Bounding gcd(N_y,T0) by the face-leg sum is not a bound for T0 itself.

Equations(193.5)–(193.8) connect192's ordinate/divisor receiver with the original phase while preserving all signs. They can be inserted into the integer W/normalization receiver. A free common-u triangle or a product of local densities would discard the very coupling proved here.

## 5. All-content cubic-divisor tail: remove the outer content count
Outside H_content, each primitive norm-one phase has local Gaussian valuations(±lambda,∓lambda). An all-same prime has product coordinate denominator depth3lambda; a relative prime has depthlambda. This is184/186's ACTUAL phase valuation argument and applies independently of median content. Consequently

T0³ divides c=c_u.                           (193.9)

Let E_all(Z,D) be retained endpoints with R<=B,c<=Z,T0>=D; no h<=C or K=1 assumption. By183, every fixed positive INTEGER c has at most B^o endpoints over ALL content, uniformly in polynomial height.

Forget the other physical filters only for an upper bound. If a c can occur, there exists an integer t>=D with t³|c. The distinct candidate c values are at most

sum_(t>=ceil(D)) floor(Z/t³) <= O(Z/D²).       (193.10)

Multiple possible t for one c only overcount, which is safe. For integer D>=1 the envelope is at most2Z/D²; it is empty when D³>Z. Hence

#E_all(Z,D) <= (Z/D²) B^{o(1)}.               (193.11)

This is not a raw Gaussian cube-image density. It directly enumerates a superset of the ACTUAL integer coordinate c and then applies a global endpoint fiber theorem. It also does not multiply193's congruences, the four cores or192's fibers.

184 wrote c=T0³ M_rel w_H and summed h and supported w_H separately, obtaining C Z/D². That is a correct but weaker upper bound. In(193.10) the integer c/T0³ already includes M_rel AND the entire content cofactor together; their sum does not require another h multiplier because183's c-fiber has already counted all h. The old upper theorem is retained as valid, but its displayed outer-C envelope and corresponding budget obstacle do not describe the strongest available T0 estimate after193. The separate-chat audit PASS for184 is not retracted or edited.

186's all-content q_phase tail Z/D remains valid for the full q_phase, which includes content primes. The cubic argument cannot be applied with an arbitrary q_phase in place of T0: only T0³|c is used. New(193.11) improves186's displayed T0 envelope min(Z/D,CZ/D²) to Z/D², and extends it without a median/content ceiling.

## 6. K=1 firewall: the closing range is old small-tau
For K=1, retained174/177 give fixed-tau endpoint fiber<=B^o because D_min=tau.186 gives

c=tau*q_phase², q_phase>=T0.

Therefore E_K1(c<=Z,q_phase>=D) has tau<=Z/D², and

#E_K1(c<=Z,q_phase>=D) <= (Z/D²) B^o.          (193.12)

This even holds for full q_phase, by the old fixed-tau fiber, without a cubic-divisor assertion. In particular E_K1(Z,D) is a subset of the OLD174 small-tau sector. If Z/D²<=B^(1/3-epsilon) with fixed epsilon>0, its negligible contribution is already covered by174; no new K=1 disposal should be credited. On the primary K=1 residual tau>B^(1/3-delta_D), thresholds with Z/D² below that cutoff give an empty set.

For general content D_min=(h_(1)h_(2))*tau may exceed tau, so this K=1 subsumption does NOT prove that(193.11)'s entire all-content sector is covered by174. The all-content tail extension is the new counted statement. It does not solve K>1 averaging over its remaining large-c/T0/median regime.

One scoped all-content example is Z=B^(2/5), D=B^(1/20), yielding B^(3/10+o) and thus a fixed-power negligible upper contribution at the retained M3 scale. This is a conditional threshold sector, not proof of occupied/nonempty endpoints or that the whole residual satisfies the thresholds. Its K=1 portion is already small-tau.

The stronger displayed exponent is z-2d, instead of alpha+z-2d. With M_rel>=B^m, T0>=B^d, c<=B^z, feasibility still requires z>=m+3d, so z-2d>=m+d. There is no automatic global budget closure. On a physical dyadic cell c=T0³ M_rel w_H, the exponent is m+d+w; the content-cofactor w is not bounded away by merely removing an outer h sum.

## 7. Residual and NEXT194
Keep192 all-content fixed-ordinate fibers and intrinsic integer W receiver. Apply the K=1 signed identity(193.7), content coprimality(193.5) and residue support(193.6) to the reconstructed actual phase; retain187/188 both-legs/gap interior and134 D-only. Use(193.11) only on threshold cells it actually disposes. Record193.12 as old small-tau inclusion, not new primary credit.

NEXT194: seek a SUMMED physical correlation on the surviving K=1 large-tau/large-relative core, using signed face collision versus relative/all-same allocation, the integer W square and original U,V,N_T/Den(S). In particular (193.7) controls only a gcd: a new theorem must control the unshared conductor or actual joint support before making a T0/c cap. Do not restart the fixed-fiber relabeling, charge the1 mod8 compatibility independently, or reopen134 fresh C_u/G branches. Separately use the all-content T0 tail where applicable and continue the K>1 low-median/large-c residual with its actual content cofactor paid. Primary gate OPEN, global credit0.

## 8. Verification and audit scope
verify_m3_t11_193.py / M3-T11-193-verification.json PASS.63744 signed synthetic p-adic sphere/space-triangle witnesses at p=5,13,17,29,41,73 and lambda=1,2,3 include15936 all-same gcd checks. Unsigned root branches are varied separately from original phase signs;720 collision cases occur at17,41,73 (240 each), none at5 mod8.2040 primitive-face ZERO-third-edge boundaries check content/ordinate coprimality.69 exact integer cubic-divisor cells check union/envelope and empty range.

Synthetic local squares and boundaries are NOT positive rational endpoints; physical endpoints enumerated0. Deductive proofs establish the statements, finite tests do not establish whole occupied support. Independent hostile audit NOT RUN. Preserve separate-chat audit162–185 without extending it to186–193.

No retraction.184/186 older upper bounds remain valid and are strengthened in the stated T0 scope. All retained masks and flags remain. TI parked,120 retracted,147–149 frozen;134 fresh D-only Q_S=M_rel²,C_u=M_G=1. Primary OPEN, global credit0.

## Durable references
192: https://drive.google.com/file/d/1o4E1KVgceLZsjhNgbPh1b1KvlirhgUYq/view
186: https://drive.google.com/file/d/18OiB75lUTZzAWsW_SxDaAMCiZ6dL_V94/view
184: https://docs.google.com/document/d/1jvdtwROi4MPSmaRha7XX1Q8SXv-OUrwgQNmKRNQLoBM/edit
181: https://docs.google.com/document/d/1oHsUtVShm0IfGrmdxzpTcYgQgtjSGU9n6xguGG5KVHY/edit
174: https://docs.google.com/document/d/1_ic-h_X9wS8EZwpNflXzGZEDPEKg2qCAgHveaOwLyeE/edit
MAIN: https://docs.google.com/document/d/1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE/edit
CARD-INDEX: https://docs.google.com/spreadsheets/d/1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4/edit
RESULT-LEDGER: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit
SCRIPT_DRIVE_ID: 1QTxGYfyo3eh-TdpJq45MS2OjcpPFXDTi
JSON_DRIVE_ID: 1T9DLQKJUiALiq82dWmbulspS8zeph0p8
