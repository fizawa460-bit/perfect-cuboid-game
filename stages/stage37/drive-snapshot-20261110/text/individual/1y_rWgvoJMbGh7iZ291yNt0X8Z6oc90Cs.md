# M3-T11-188 — Primitive product-phase gap sector and coupled face-space receiver

CARD_ID: M3-T11-188
STATUS: PROVED_ALL_CONTENT_PHASE_GAP_SECTOR / EXACT_ROTATED_NUMERATOR_GCD / K1_COUPLED_INTEGER_RECEIVER
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Current authority and scope

Continuation of187 from fresh Google Drive MAIN, operational CARD-INDEX (row416=187, row417 blank), short RESULT-LEDGER, latest187 and active ROUTE section17. Only necessary dependencies134,181,162 were read. Historical active ROUTE headers and card migration-time controls do not override MAIN CURRENT STATE. No full-history reread.

Use the primitive positive original endpoint measure R<=B with canonical ordering/orientation/cyclic/content masks and134 four-square/intrinsic-R lift retained. The finite nonzero common-u branch has Z=prod_i (e_i+i f_i)/R=(b_phi+i a_phi)/c, c=c_u, with nonzero coprime signed integer legs a_phi,b_phi and a_phi²+b_phi²=c². Thus c is odd, the two legs have opposite parity, c<=R³<=B³. Write H=prod h_i, h_i=gcd(e_i,R), tau=R/H. Use186 D_S²=Den(S), q=q_phase=R/D_S, c=tau*q²; use187 G=gcd(|U|,|V|)=H*D_S²=R³/c and (U,V)=G(b_phi,a_phi).

The arithmetic Pell lemma below is already proved in162. The new result is its all-content transfer to the product phase via183 and its original integer/K1 interface. This is not a claim of a new Pell counting method, nor of literature-wide novelty. Index searches for product-phase gap, phase gap, U+V and linear phase found no earlier card with this transfer; Pell search identifies162 as an explicit dependency.

## 2. Rotated numerator gcd and the absolute phase gap

Set alpha=|a_phi|, beta=|b_phi|, W=alpha+beta and d=|alpha-beta|. The gap d is a positive odd integer: equality would make c²=2alpha² impossible for nonzero integers. Define it directly on original integer numerators by

d=||U|-|V|| / G,
W=(|U|+|V|)/G.

This is an ABSOLUTE difference after phase reduction; it is not ||U|-|V|| itself and not a fixed relative angular window.

For both signs,

gcd(|a_phi+b_phi|,c)=gcd(|a_phi-b_phi|,c)=1,
gcd(|a_phi+b_phi|,|a_phi-b_phi|)=1.

Proof: a prime dividing c and a_phi±b_phi would divide 2a_phi² by the norm equation. Since c is odd and gcd(a_phi,c)=1, no such prime exists. The gcd of the two odd sums divides 2a_phi and 2b_phi and hence is1. Consequently the ORIGINAL numerators satisfy exactly

gcd(|U+V|,R³)=gcd(|U-V|,R³)=G=H D_S²,
gcd(|U+V|,|U-V|)=G.

These equalities expose two primitive rotated numerators. They are forced by the phase norm and are not independent rare gcd events. They supply no second local-density charge beyond186/187.

Equivalently d=min(|a_phi+b_phi|,|a_phi-b_phi|). Through184 u=±a_phi/b_phi, this is a small numerator of the suitable u±1; the denominator |b_phi| can still be large. Fixed d must not be confused with fixed u or fixed S.

## 3. Summed all-content small-phase-gap count

The primitive phase triangle gives

W²-2c²=-d²,
gcd(W,d)=gcd(W,c)=1,
alpha=(W+sigma*d)/2, beta=(W-sigma*d)/2,
where sigma=sign(alpha-beta) in {+1,-1}.

Use162's completely summed direction lemma at arithmetic height C=B³. For each odd d there are at most 2^omega(d) primitive norm -d² ideals in Z[sqrt(2)], with at most

1+floor(log(3C/d)/log(3+2sqrt(2)))

positive generators in the relevant height window per unit orbit. Ordered legs cost at most2, signed phase conventions at most a fixed factor. The proof is uniform: norm-Euclidean Z[sqrt(2)], each split prime power is allocated wholly to one conjugate ideal, and norm+1 unit growth is 3+2sqrt(2). No class-number, content or fixed-d constant is left unsummed. Since sum_(d<=D)2^omega(d)<=D(1+log D), the phase label count is

O(D(1+log D)(1+log B))  for 1<=D<=B³.

Each label fixes c. The183 global fixed-c physical fiber is uniformly B^{o(1)}, INCLUDING all contents and physical lifts. Charging each phase label this upper bound overcounts some c values and hence is safe. Importantly B remains the physical height; B³ is only the arithmetic phase hypotenuse ceiling. Thus

#E(d<=D) <= D B^{o(1)}.

No outer C_content factor is present. For D=B^(1/3-epsilon), fixed epsilon>0, this is a scoped o(M3) sector on the retained B^(1/3) scale. It is valid on the full admitted content range, not only K=1.

This reaches part of187's both-legs-large complement: d can remain1 while both phase legs become arbitrarily large. The conic directions (3,4,5),(20,21,29),(119,120,169),... have d=1. Their recurrence is W'=3W+4c, c'=2W+3c. These are LABELS, not asserted physical endpoints. They show arithmetic non-containment in a fixed short-leg sector and also show that small d alone gives no finite cap on c. No positive physical realization or occupancy lower bound follows.

Intersecting186,187,188 gives only the legitimate minimum bound

#E(d<=D,ell<=A,c<=Z,q>=Q) <= min(D,A,Z/Q) B^{o(1)},
ell=min(alpha,beta), Q>=1.

Do not multiply these sector densities. For disjoint bookkeeping charge187's ell<=A first, then188's d<=D restricted to ell>A. Their union is at most (A+D)B^{o(1)}. The remaining endpoints have alpha>A, beta>A and |alpha-beta|>D. This is an absolute integer cutoff; the relative phase angle may still approach an axis or diagonal when c grows.

## 4. Joint K=1 face-space / phase-Pell integer receiver

Retain181's exact K=1 labeling: h_1=h_2=1, h_3=h, R=h*tau. Put

g=gcd(e_1,e_2), A_f=e_1/g, B_f=e_2/g,
u=e_3/h, v=f_12/h,
n=f_12/g=h*k, v=g*k, k=gcd(n,v).

The two primitive triangles obey

A_f²+B_f²=h²k²,
u²+g²k²=tau²,
gcd(A_f,B_f)=gcd(u,g*k)=1,
gcd(h,g)=1,
gcd(A_f*B_f,tau)=gcd(k,tau)=gcd(g,tau)=1.

These are181's same-physical filters (gcd(g,tau)=1 also follows from primitive v=g*k). Keep h<=C only when using the existing small-content branch; no extra C is required for188's sector theorem.

From187 let s=N_T/q², s0=|s|. Its exact product relation becomes

s0*alpha=2g² A_f B_f u.

Therefore the synchronized ORIGINAL integer system is

W²-2tau² q^4=-d²,
s0*(W+sigma*d)=4g² A_f B_f u,
u²+g²k²=tau²,
A_f²+B_f²=h²k²,
R=h*tau<=B,
D_S=R/q in Z_{>0},
c=tau*q²,
gcd(s0,D_S)=1.

Also gcd(s0,tau)=1. More generally, outside K=1, each reduced edge e_i/h_i is coprime to R/h_i and hence to tau. The187 product s*a_phi=2prod(e_i/h_i), with tau odd, implies gcd(s,tau)=1. This is an exact consequence, not an added independent congruence saving.

The displayed system couples the phase gap, numerator s, face-space shared gcd k and active tau on one endpoint. It is NECESSARY. It is not asserted sufficient: retain the other complementary triangles,134 four-square/intrinsic R and original packet masks. In particular a Pell solution in the first line alone is not an endpoint. There is no proved B^{o(1)} fixed-s fiber and no bound for the large-d moving support here.

## 5. Verification, review and next189

verify_m3_t11_188.py and M3-T11-188-verification.json PASS:
-15919 primitive phase triangles with c<=100000 check the norm, parity and rotated gcd identities.
-31838 scaled integer norm labels check gcd(U±V,R³)=G and exact reduced d.
-125 primitive Pell seeds for odd d<=500 satisfy the 2^omega(d) envelope; complete Pell reconstruction matches all459 Euclid triangles with c<=100000,d<=500. All small-gap Euclid labels descend to listed seeds.
-The d=1 recurrence reaches (27304196,27304197,38613965), illustrating the absence of a d-only hypotenuse cap.

Physical endpoints enumerated=0. Scaled labels are not physical endpoints. The new physical transfer is deductive from audited162 arithmetic and183 fixed-c multiplicity; finite tests establish neither the asymptotic statement nor occupancy. Within-session review checks full family sum, no outer content cost, original height/masks, signs, and no independent density product. Independent hostile audit NOT RUN; the separate-chat audit remains162–185, without extension to186–188.

NEXT189: count the joint K=1 receiver on the alpha,beta>A,d>D residual, or prove a useful c/tau cap using its synchronized numerator/product and face-space conditions. Do not claim that another isolated Pell norm, fixed-d fiber or extra rational phase sector resolves the bulk. Small-leg and small-gap phase sectors are now recorded; repeat transfer or cutoff adjustment gets no new global credit. Large-c threshold tail and K>1 low-median averaging remain separate OPEN tasks. Keep134 fresh D-only (Q_S=M_rel²,C_u=M_G=1); no fresh Gaussian/interior restart without withdrawing134. TI parked,120 retracted,147–149 frozen. Main gate OPEN and global credit0.

## 6. Durable references

187: https://drive.google.com/file/d/1tk-qZWSstLRnHyj2Np9KeTiag1BWpqM0/view
186: https://drive.google.com/file/d/18OiB75lUTZzAWsW_SxDaAMCiZ6dL_V94/view
162 arithmetic Pell lemma: https://drive.google.com/file/d/1tzjZwKoKvP1zVY-tYABRkY70CmbpoVgq/view
183 fixed-c fiber: https://docs.google.com/document/d/156OI672uaTABWO1UaogndaieH8kYIUL7LFizZATcqGg/edit
181 face-space receiver: https://docs.google.com/document/d/1oHsUtVShm0IfGrmdxzpTcYgQgtjSGU9n6xguGG5KVHY/edit
134 lift: https://drive.google.com/file/d/1Uxm_NWVBDZJj4dGZNSZkI8nMP2XFoJzs/view
MAIN: https://docs.google.com/document/d/1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE/edit
CARD-INDEX: https://docs.google.com/spreadsheets/d/1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4/edit
RESULT-LEDGER: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit
SCRIPT_DRIVE_ID: 1V4xGAwFvtoaE55o6NLPGLWS_deu4pgEg
JSON_DRIVE_ID: 17dYucGaghfCdfoJE-vSQp3BSHmUZcdbG
