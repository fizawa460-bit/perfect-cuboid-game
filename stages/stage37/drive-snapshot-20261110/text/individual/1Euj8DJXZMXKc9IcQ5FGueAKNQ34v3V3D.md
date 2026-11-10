# M3-T11-189 — Half-power obstruction for the projected joint receiver and original phase parity

CARD_ID: M3-T11-189
STATUS: PROVED_PROJECTED_RECEIVER_OMEGA_SQRT_B / RESTORED_ORIGINAL_PHASE_PARITY / FULL_PHASE_COMPATIBLE_COUNT_OPEN
PRIMARY_GATE: M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT: 0
INDEPENDENT_HOSTILE_AUDIT: NOT_RUN

## 1. Authority, attempted count and precise conclusion

Fresh Drive MAIN, operational INDEX (row417=188, row418 blank), short RESULT-LEDGER, latest188 and active ROUTE section17 were checked first. Necessary181/186/187 definitions are retained from the immediately preceding continuation; no history-wide reread. Index queries phase parity, primitive product-phase, A_f²+2, square area and phase Pell found no previous card stating the counterfamily below.

188 explicitly called its displayed K=1 joint integer system NECESSARY, not sufficient, and retained original complementary triangles, four-square/intrinsic R and packet masks. Its small phase-gap sector remains valid. No retraction of188 or187 is made.

This turn tests whether the displayed Pell/product/two-triangle equations alone can support the desired B^(1/3-eta) bulk bound. They cannot: an explicit family of projected integer counterstates has cardinality Omega(B^(1/2)), even with both phase legs and phase gap of order B, h=1, large tau and large face-space k. These are not physical endpoints and are not asserted to satisfy the full original packet. A simple original product-phase parity condition excludes every member. Therefore the obstruction concerns the enlarged projected receiver ONLY. It gives neither a lower bound for endpoints nor a no-go theorem for counting the correctly reconstructed population.

## 2. Original product-phase parity must remain labeled

Use original positive edges e_i and signed complementary diagonals f_i with R odd, sum e_i²=R² and e_i²+f_i²=R². Exactly one e_i is odd: reducing the sphere equation modulo4 excludes every other odd-edge count. In an integer right triangle with odd hypotenuse every even leg is divisible by4. Hence the two even e_i are divisible by4; the f_i opposite the odd edge is divisible by4, and the other two f_i are odd. Signs do not change these facts.

For the ORIGINAL cubic and sum numerators of187,

U=e_1e_2e_3-e_1f_2f_3-e_2f_1f_3-e_3f_1f_2,
V=f_1e_2e_3+f_2e_1e_3+f_3e_1e_2-f_1f_2f_3,
N_T=sum e_i f_i,

termwise reduction gives

U odd, 4|V, 4|N_T.

The phase gcd G=H D_S² and q=q_phase are odd by186. Thus

b_phi=U/G odd,
4|a_phi=V/G,
4|s=N_T/q².

The even phase leg is specifically the IMAGINARY/product-phase numerator a_phi used in s*a_phi=2prod(e_i/h_i). It is not an unlabeled option. Bounded leg swaps used to upper-bound conic labels do not authorize swapping a_phi and b_phi while keeping s and the original cubic unchanged. These are restored explicit original filters, not a new independent density saving.

## 3. Exact counterfamily for the enlarged joint equations

Start with any primitive Pythagorean face

A²+B_f²=k²,
A odd, B_f even, gcd(A,B_f)=1.

Write B_f as F below to avoid confusing it with the physical height bound B. Thus A²+F²=k². Put

h=1, g=2F,
u=A², v=2Fk,
tau=R=A²+2F²,
e_1=2AF, e_2=2F², e_3=A².

Then the retained face and space equations hold exactly:

A²+F²=h²k²,
u²+g²k²=tau²,
f_12=gk=hv,
e_1²+e_2²+e_3²=R².

The original edge triple is primitive, gcd(e_1,e_2)=g, and gcd(e_i,R)=1 for all i, so its CONTENT GCD LABELS are h_1=h_2=h_3=1. This does not assert that the other two face diagonals exist. Also

gcd(A F,tau)=gcd(g,tau)=gcd(k,tau)=gcd(u,v)=1,
gcd(h,g)=1.

To build the projected phase record, choose

a*=alpha=A²,
b*=beta=2Fk,
c*=tau,
q*=1, D_S*=R,
s*=8AF³,
W*=alpha+beta, d*=|alpha-beta|.

Its phase is primitive and a*²+b*²=c*². With sigma=sign(alpha-beta), every equation displayed in188 section4 holds:

W*²-2tau²(q*)^4=-(d*)²,
s*(W*+sigma*d*)=4g² A F u,
s* alpha=2g² A F u,
gcd(s*,D_S*)=gcd(s*,tau)=1,
c*=tau(q*)², D_S*=R/q*.

Even the numeric norm/TY/gcd identities from186–188 can be imitated if their numerators are treated as free variables. Define

G*=R²,
U*=G* beta, V*=G* alpha, N*=s*.

Then

U*²+V*²=R^6,
gcd(U*,V*)=G*=H*(D_S*)²,
gcd(U*±V*,R³)=G*,
gcd(N*,R²)=(q*)²,
N* V*=2e_1e_2e_3 R²,
H c_star D_S_star²=R³.

These identities do not enforce the ORIGINAL polynomial definitions of U,V,N_T. Here U* is even and V* is odd, whereas the original product requires U odd and 4|V. Equivalently a*=A² is odd. Every such phase record fails the original product-phase parity and is nonphysical as a record.

Swapping to the even phase leg beta does not repair it. The product would force

s_swap=2e_1e_2e_3/beta=4A³F²/k.

Since k>1 is odd and gcd(k,AF)=1, this is not an integer. Thus even allowing the other leg label with recomputed s cannot give an integer phase-compatible record with the same q=1 and c=tau. This excludes the displayed counterstates; it is not a claim excluding every possible phase or endpoint for their underlying edge coordinates.

## 4. Full family budget and survival of the large-coordinate cutoffs

Take primitive Euclid parameters

N<=m<=2N,
m/10<=n<=m/8,
m odd, n even, gcd(m,n)=1,
A=m²-n², F=2mn, k=m²+n².

The map is injective: the ordered primitive face recovers (m,n), and the projected edge tuple recovers A from e_3=A² and F from e_2=2F².

Here R=m^4+6m²n²+n^4, so

N^4<=R<18N^4,
k is of order N²,
A,F,|A-F| are of order N²,
alpha=A², beta=4mn(m²+n²) and d=alpha-beta are of order N^4.

In particular alpha>beta in this wedge. An explicit lower bound is

d >= (1889/4096)m^4,
beta >= (2/5)m^4.

Therefore at B_N=18N^4 these counterstates have R,tau,c,alpha,beta,d of order B_N, and k,A,F,|A-F| of order B_N^(1/2). For every fixed epsilon>0 they eventually pass alpha,beta>B_N^(1/3-epsilon), d>B_N^(1/3-epsilon), the analogous small-face-coordinate deletions on their existing face, and the181 large-k cutoff B_N^(1/6-xi-epsilon_k). h=1 also passes any positive small-content ceiling. Missing-face and original packet tests remain unverified and must not be inferred from these projections.

The wedge has area 3N²/80. For each odd divisor j, the lattice m,n divisible by j with m odd,n even has this area divided by4j², plus O(N/j+1) boundary error. Mobius inversion, summed through j<=2N, gives

#(m,n)= (3N²/320) prod_(p odd)(1-1/p²)+O(N log N).

The product is positive. This proves Omega(N²)=Omega(B_N^(1/2)) distinct projected counterstates with the full moving parameter cost paid. Taking N=floor((B/18)^(1/4)) gives the same lower bound for all sufficiently large height ceilings B, not merely a sparse sequence. Thus no O(B^(1/3-eta)) upper bound can hold for ALL states of this enlarged integer system, even after these large-coordinate cutoffs.

This is an enlarged-state count, not a physical support or physical occupancy lower bound. It does not contradict183's physical fixed-c fibers or187/188 physical sector bounds. The entire constructed family is deleted by section2's mandatory labeled product-phase parity. No obstruction to the parity-corrected, fully lifted count is proved.

## 5. Receiver correction and next190

Use the original f_i variables and their two missing square equations explicitly in the K=1 chart:

f_1²=g² F²+h²u²,
f_2²=g² A²+h²u²,
f_3=epsilon_3*h*g*k,
e=(gA,gF,hu), R=h*tau.

Define U,V,N_T by the original polynomials, rather than introducing an independent phase triangle satisfying only norm and product equations. Then set

a_phi=V/(h D_S²), b_phi=U/(h D_S²), s=N_T/q²,
D_S=R/q, c=tau*q²,
W=|a_phi|+|b_phi|, d=||a_phi|-|b_phi||.

Integrality, exact gcds, labeled parity,134 four-square/intrinsic R and the original orientation/coefficient/cyclic masks remain required. The two missing-square equations and the original polynomial tie are not interchangeable with the one norm equation for a separate phase label.

NEXT190: seek a joint count or useful c/tau cap on this parity-correct, polynomial-anchored original population with alpha,beta>A0,d>D0. A proof bounding only the bare Pell/product projection is now blocked by section4. Mod2 removes this counterfamily but is not a new fixed-power endpoint saving and does not solve the remaining count. Do not spend another card relabeling the projection, changing its cutoff, or adding a free phase triangle. Large-c threshold tail and K>1 low-median averaging remain separate OPEN tasks.

## 6. Verification and authority limits

verify_m3_t11_189.py / M3-T11-189-verification.json PASS:
- 6454 projected counterstates across N=100,200,400,800; counts77,302,1220,4855. All displayed188 equations and numeric186–188 identities pass.
- All6454 fail original product-phase parity; all swapped even phase legs force nonintegral s.
- 6144 necessary mod8 assignments of original edge/diagonal parities verify U odd, V and N_T divisible by4.
- Both missing-face squares fail in all6454 finite samples. This finite observation is not promoted to an all-parameter edge nonexistence theorem; the proven record exclusion uses labeled phase parity.

Physical endpoints enumerated=0. The count and exclusion are deductive; finite checks verify the algebra only. Independent hostile audit NOT RUN. Separate-chat audit remains162–185, not186–189. 187/188 sector theorems and186 conservation are retained. Primary gate OPEN, global credit0;134 fresh D-only retained (Q_S=M_rel²,C_u=M_G=1); TI parked,120 retracted,147–149 frozen.

## Durable references

188: https://drive.google.com/file/d/1y_rWgvoJMbGh7iZ291yNt0X8Z6oc90Cs/view
187: https://drive.google.com/file/d/1tk-qZWSstLRnHyj2Np9KeTiag1BWpqM0/view
186: https://drive.google.com/file/d/18OiB75lUTZzAWsW_SxDaAMCiZ6dL_V94/view
181: https://docs.google.com/document/d/1oHsUtVShm0IfGrmdxzpTcYgQgtjSGU9n6xguGG5KVHY/edit
MAIN: https://docs.google.com/document/d/1gMO3D7hK2C4WgmpTz9RqeYEhvqAeKMqa0xOTxYW8TTE/edit
CARD-INDEX: https://docs.google.com/spreadsheets/d/1skBS4TxofX8A25cnhfoxO5VZZjfBRlW_sfzHkSTNiL4/edit
RESULT-LEDGER: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit
SCRIPT_DRIVE_ID: 1wuggIACCIS3A4793rdOOnoX8j84VMXCN
JSON_DRIVE_ID: 1yEGp3qf7bzOzGdjeeaDXu4rSddMBhvP1
