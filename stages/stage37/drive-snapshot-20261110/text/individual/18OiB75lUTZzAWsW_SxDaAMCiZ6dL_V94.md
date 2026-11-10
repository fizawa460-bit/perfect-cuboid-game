# M3-T11-186 — Full-content denominator conservation and a content-free square-divisor tail

STATUS=PROVED_FULL_CONTENT_DENOMINATOR_CONSERVATION / PROVED_SQUARE_S_DENOMINATOR / SCOPED_CONTENT_FREE_Q_TAIL / GLOBAL_CLOSURE_OPEN
PRIMARY_GATE=M3-T11-GATE-001 OPEN; GLOBAL_COUNTING_CREDIT=0
AUDIT_MODE=WITHIN_SESSION_DEDUCTIVE_REDERIVATION; INDEPENDENT_HOSTILE_AUDIT=NOT_RUN
TI=PARKED;120=RETRACTED;147–149=FROZEN

## Authority, population and notation

Fresh MAIN/latest185, CARD-INDEX rows409–414, current short RESULT-LEDGER, active ROUTE17.1–17.2 and retained134/181 interfaces. Historical control blocks are not current NEXT instructions. Targeted index searches for Den(S), square denominator and saturation found no prior full-content identity below; no history restart.

Count primitive positive physical endpoints R<=B on the retained finite nonzero corrected common-u locus, with one canonical order/sign witness, all original coefficient/content/orientation/cyclic masks,134 four-square lift and intrinsic R. Put H=h1*h2*h3, h_i=gcd(e_i,R), tau=R/H, x_i=e_i/R, y_i=f_i/R with signed complementary face diagonals, w_i=x_i+i*y_i. The h_i are pairwise coprime and R is odd. Define Z=w1*w2*w3=X+iY, c=c_u=den(Z), T=sum x_i*y_i, S=2T, t=Den(S).

184 gives T*Y=2e1*e2*e3/R^3 and Y=±a/c with gcd(a,c)=1.134 gives t|R^2 and each primitive space-triangle denominator D_i=R/h_i.185 gives the fresh denominator depths. The content-prime proof below completes them; it does not discard the corrected content-supported kappa coefficients.

## 1. Local norm-one denominator lemma

For an odd split prime p and a primitive rational norm-one phase with coordinate denominator of p-depth d>0, its valuations at the two Gaussian primes over p are (+d,-d) in one order. Their sign is determined by which root f/e=±iota modp is selected when the corresponding integral edge and face leg are p-units. A norm-one phase with p-integral coordinates has valuations(0,0).

For a product phase, the signed valuations add. If their sum is A!=0, the real/imaginary coordinate denominator has depth |A|: one of the two conjugate phase terms has strictly smaller valuation, so their half-sum/half-difference cannot cancel it. If A=0, both coordinates are p-integral. This is Gaussian valuation addition with the ACTUAL physical phases, not a global-unit approximation to content coefficients.

Every prime p|R is split: at least two h_i are p-units, hence some primitive D_i retains p in its odd Pythagorean hypotenuse. There is no prime2 in R or in c,t. Also c|R^3/H and t|R^2, so primes outside R need not be considered.

## 2. Partial content: an exact three-case depth table

Fix p^lambda||R with positive content depth kappa=v_p(H)<lambda. Relabel so p|h3. Then v_p(e3)=kappa EXACTLY, while e1,e2 are p-units. The physical phases w1,w2,w3 have denominator depths lambda,lambda,lambda-kappa. Gaussian signed addition gives exactly these possible c-depths:

| v_p(c) | v_p(t) |
| --- | --- |
| 3lambda-kappa | 0 |
| lambda+kappa | 2(lambda-kappa) |
| lambda-kappa | 2lambda |

All possible c-depths are positive. Thus v_p(Y)=-v_p(c). The product identity forces

v_p(T)=kappa-3lambda+v_p(c).

In all three rows this is nonpositive; since p is odd, t=Den(2T) has the displayed depth. Therefore, at every partial-content prime,

v_p(c)+v_p(t)=3lambda-kappa,
v_p(t) is even.

Rows that are not realized in a particular packet simply contribute no endpoints; no independence or local probability is inferred.

## 3. Saturated content: numerator compatibility removes the apparent deficit

Now kappa=lambda, so e3 has valuation nu>=lambda. The third phase w3 is p-integral because D3=R/h3 has no p. The first two phases still have depths lambda,lambda. Consequently c-depth is either2lambda (same Gaussian orientation) or0 (opposite orientation).

If v_p(c)=2lambda, then v_p(Y)=-2lambda. The product identity gives v_p(T)=nu-lambda>=0, hence v_p(t)=0.

If v_p(c)=0, the first two orientations are opposite. Choose a local square root iota of-1. With f1/e1=epsilon*iota and f2/e2=-epsilon*iota modp, the numerator

N_T=e1*f1+e2*f2+e3*f3

satisfies

N_T=epsilon*iota*(e1^2-e2^2)=2epsilon*iota*e1^2 modp,

because e1^2+e2^2+e3^2=R^2 and p|e3,R. This is a p-unit. Therefore v_p(T)=-2lambda and v_p(t)=2lambda EXACTLY. In particular the p-integral imaginary coordinate Y has depth nu-lambda, as also follows from the product identity; its possible numerator divisibility does NOT create a denominator-product deficit.

The saturated table is exactly

| v_p(c) | v_p(t) |
| --- | --- |
| 2lambda | 0 |
| 0 | 2lambda |

Again the depth sum is3lambda-kappa=2lambda and the S denominator depth is even. Merely using t|R^2 would have left an apparent deficit; the physical opposite-orientation numerator is the missing equality input. A preliminary weaker divisor/deficit hypothesis is superseded by this exact unit computation. No genuine deficit branch remains to count.

## 4. Full global identity and integer square-divisor coordinate

Outside content,185 gives(c-depth,t-depth)=(3lambda,0) at all-same fresh primes or(lambda,2lambda) at relative fresh primes. Sections2–3 complete every prime dividing R. Hence, on the full retained physical population,

H*c*t=R^3,
t=D_S^2 with D_S a positive integer divisor of R.

The second assertion is about the REDUCED DENOMINATOR, not about S being a square rational number. Let

q=R/D_S.

Then q is a positive integer divisor of R, q<=R<=B, and

c=tau*q^2, tau=R/H.

This q is a new product-phase/full-S coordinate; it is not174's historical q_min,181's Euclid allocation q, or any anti-root denominator. Write q_phase if using several routes together. Its definition includes all content primes.

In185 notation t=M^2*t_H, R=T0*M*R_H and c=M*T0^3*w_H. The new theorem gives

t_H=D_H^2, D_H|R_H,
q=T0*R_H/D_H,
w_H*t_H=R_H^3/H.

These strengthen185's support-only constraints without retracting them. Content coefficients remain norm-one, not global Gaussian integer units. H=1 reduces to185's previously proved specialization.

## 5. Scoped tail bound with no outer content cost

Let E(Z,D) be all retained primitive positive physical endpoints R<=B with c<=Z and q_phase>=D, parameters bounded by fixed powers of B and D>=1. All original masks and intrinsic height remain in the set being counted.183 bounds every global fixed-c endpoint fiber by B^o, over ALL content packets.

Since c=tau*q^2, for each integer q>=D there are at most floor(Z/q^2) positive integer tau choices. Dropping the remaining physical tests and q|R constraints here is only an upper-bound relaxation. Summing q>=D gives O(Z/D); repeated representations of c are safe in an upper bound. Consequently

#E(Z,D) <= (Z/D)*B^o.

The set is empty for D>sqrt(Z). The dyadic form, q~Q and c<=Z, is also Z/Q*B^o. No h<=C restriction or external C multiplier is needed. This is a summed endpoint inequality, not a density product or a renamed occupied support assertion.

Because q>=T0, the K=1 population from184 with T0>=D now satisfies the combined retained bound

#E_K1(c<=Z,T0>=D,h<=C) <= B^o*min(Z/D, C*Z/D^2).

The new bound improves the old first term Z to Z/D; the cubic cofactor term is retained. Do not multiply the two savings.

One scoped consequence: sectors with Z/D<=B^(1/3-epsilon), for fixed epsilon>0, are negligible at the retained M3 scale. This is CONDITIONAL ON THESE THRESHOLDS and is not a proof the present entire residual meets them.

## 6. Residual budget and next counted task

The primary gate is still open. On K=1,174 gives D_min=tau; the current residual retains tau>B^(1/3-delta_D). In a dyadic cell c~B^z, q~B^d, tau~B^r, the exact identity forces z=r+2d. The new available upper-bound exponent z-d is r+d. Thus large q is not automatically a closing tail when the allowed c grows with tau*q^2: the bound needs an independent cap or a physical occupancy estimate. This is a limitation of the available upper estimate, NOT a lower bound for actual endpoint counts.

The full-content denominator uncertainty is now resolved. NEXT187 must use the exact pair(tau,q_phase), H*c*Den(S)=R^3 and square Den(S) in the original134 four-square/intrinsic-R lift and181 face-space filters to prove a moving PHYSICAL occupancy saving, or establish a genuinely useful c threshold on the residual. Repeating the denominator table, generic square-divisor sparsity, supported-integer compression or the exponent calculation is not a new result. Fixed-S BO1 still fixes the entire rational value, not just D_S. No independent cube-image, core-modulus, Euclid or E-denominator density charge.

Large-c threshold tail and K>1 low-median averaging remain separately OPEN. All180/181/183 sectors and184/185 identities are retained. Gate OPEN, global credit0, TI parked,120 retracted,147–149 frozen.

## 7. Verification, scope and durable handoff

verify_m3_t11_186.py uses deterministic synthetic p-adic sphere/space-triangle witnesses at p=5,13,17,29, lambda=1,2,3, edge-depth nu=1 through3lambda+2,12 samples per stratum and all8 face signs. Modulus is p^(12lambda+12). At nu=lambda, the third reduced circle is explicitly parameterized to ensure a valid square lift; at p5 its complementary leg can be p-divisible and is not incorrectly required to be a unit. All9216 cases across204 reported depth strata PASS the product identity, partial/saturated tables, even t-depth, exact zero deficit, and c-depth-(lambda-kappa)=2lambda-t-depth>=0.

The initial diagnostic demanded a nonzero deficit example, but none occurred. The saturated numerator proof above explains why that preliminary expectation was wrong; the final script instead requires deficit=0 in every case. No physical counterexample or failed theorem case is presented as a PASS. Tests are synthetic local witnesses, not positive rational endpoints; physical endpoints enumerated=0. The written valuation proof establishes the universal result; finite verification does not establish asymptotic counts or independent hostile audit.

Current proof lives only in this card. MAIN and short LEDGER summarize; CARD-INDEX registers the proof and next187. Active ROUTE17 supplies primitive phase/content conventions and earlier proof dependencies only; its historical latest184 header does not override current MAIN. No proof is appended to the large ROUTE/archived LEDGER.

THIS_CARD_FILE_ID=18OiB75lUTZzAWsW_SxDaAMCiZ6dL_V94.
VERIFICATION_SCRIPT_FILE_ID=11P3EHOOovBOmaVD6liuwIacLSOOj6gdA.
VERIFICATION_JSON_FILE_ID=1CKqhDIR5-hVrSO-CJP4BKsLmRPzvNFur.
Dependencies:185 CARD_FILE_ID=1WoBtJLeBILL9XXGruJVE0sNYvvUOVnWb;184 CARD_DOC_ID=1jvdtwROi4MPSmaRha7XX1Q8SXv-OUrwgQNmKRNQLoBM;134 CARD_FILE_ID=1Uxm_NWVBDZJj4dGZNSZkI8nMP2XFoJzs;183 global fixed-c fiber via CARD-INDEX;174 and181 via CARD-INDEX. Active ROUTE DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE.
