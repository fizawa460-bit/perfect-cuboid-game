# R5 / Stage35EX-e: universal 8P height certificate and absolute S270 four-TOP bounds

RUN_ID: R5-20261020-POSTC157-UNIFORM-EIGHTP-N4-1151-N1-3299-V1  
SHARED_HEAD: C35-157 COMPLETE (four controllers plus COMPLETE receipt).  
FORMAL_AUTHORITY: V74_GOAL4AK_SECTION334; R5 authority provisional only.  
STATUS: R0_REVIEW_PREPARED; R0_ACCEPTED=false; OWNER_COMMITTED=false; HOSTILE_AUDIT=false.  
BRANCH_A=USER_PAUSED; BRANCH_B=OPEN; STAGE35=OPEN; E1=UNPROVEN.  
This is an **unconditional arithmetic uniformization of inherited conditional source constraints**, NOT a physical source exclusion, rank upper, or all-index solution.

## 1. Exact theorem and application boundary

Let `(A,B,C)` range over **every** primitive positive labelled Pythagorean triple `A²+B²=C²`, with `C` odd. Put `D=AC`, `H=A²+C²`, and let the **original** `E:y²=x(x−A²)(x+C²)` and `P=(D,BD)` remain unchanged. Let the S252 error be

`c_E=bit_length(256D⁸H⁴)`.

Retain S252's certified dyadic lower height values

`lambda_k=[3(bit_length(K_k)−1)−2c_E]/(12·4^k)`,
`K_k=max(abs(num(x([2^k]P)),den(x([2^k]P)))` in lowest terms.

**THEOREM A (genuine new all-base exact rational arithmetic):** For EVERY such labelled base, `lambda_3>0`. In fact with `L=log₂(C)`,

`lambda_3 > L/16−41/768 > 67/768 >0`.

No sampling, Mordell–Weil basis/rank calculation, finite-C cutoff, or 16P normalized polynomial resultant is assumed for this exact 8P result.

**THEOREM B (new all-base quantitative bridge under OLD S270):** Define the S270 thresholds **with the explicit universally valid choice** `lambda=lambda_3`. Then for EVERY such base

`N4(A,B,C) <=1151`,  `N1(A,B,C) <=3299`.

These are *absolute* upper bounds for S270's exact four-TOP nonempty threshold and four-TOP one-percent threshold, including ACTUAL critical-H top sources. They do **NOT** assert that every TOP source is GOOD. This refines the previous effective but moving-base-dependent S270 cutoffs. R0 should independently verify that substituting this lambda into the inherited S270 inequalities is legitimate.

**PHYSICAL SOURCE CONSEQUENCE (one-way necessary only):** On any hypothetical COMPLETE original indexed inner Branch B packet, for ALL labelled primitive bases:
- if `m=|n|>=1152`, every one of the FOUR distinct exact-top `GOOD or actual-critical-H` source branches has a nontrivial prime product `U_{J+},U_{J-},U_{K+},U_{K-}>1`;
- if `m=|n|>=3300`, each branch obeys `U_i^100>=b_m`, hence its logarithmic mass is at least `1%` of the whole actual canonical denominator.

This uses the unchanged global S243 four positive integer roots, same S269 primitive Gaussian/shared quartic, actual source W_n/W_2m, original signed orbit/chamber, Q/Qsharp infinite quotient, same positive coprime b_J>b_K>1/alpha, all true S270 TOP/PROPER GOOD/H ordinary-beta masks, historical holds. Not one of those is manufactured by this theorem.

## 2. Original-curve exact x(8P) numerator and full coprimality

This section proves Theorem A and the *fully reduced* numerator identity, not merely a floating numerical inequality. Introduce **auxiliary** `m4=A⁴+A²B²+B⁴=C⁴−A²B²` and `f4=2ABC`. These auxiliary variables are NOT S237's M/N or S269's Gaussian f/g. Direct original E doubling gives

`x([2]P)=D²/B²`, `x([4]P)=(m4/f4)²`.

For any original E point `Q=(x,y)`, the exact duplication formula is

`x([2]Q)=(x²+D²)²/[4x(x−A²)(x+C²)]`.

Put `s_minus=m4²−A² f4²`, `s_plus=m4²+C² f4²`, `N=m4⁴+D² f4⁴`. Then direct substitution yields

`x([8]P)=N²/[4 f4² m4² s_minus s_plus]`. (8P.1)

The factors `s_minus=(B⁴+A²B²−A⁴)²>0` and `s_plus=(A⁴+3A²B²+B⁴)²>0`. Nonzero follows as `[4]P` is not 2-torsion (S252 independently proves P nontorsion), or directly because `(B²/A²)²+(B²/A²)−1=0` has no rational solution.

**FULL gcd certificate.** `m4` is odd, and `gcd(m4,f4)=1`: modulo any prime of `A`, `B`, `C` it reduces to a fourth power of a coprime leg, and `f4` also accounts for 2. Thus `gcd(s_minus,f4)=gcd(s_plus,f4)=1`. Modulo `H=A²+C²` use `C²≡−A²`, `B²=C²−A²≡−2A²`; then `m4≡3A⁴`, `f4²≡8A⁶`, and

`s_minus≡s_plus≡A⁸ (mod H)`.

Since `gcd(A,H)=1`, both `s_minus` and `s_plus` are coprime to H. Moreover

`N≡A²H f4⁴ (mod s_minus)`, `N≡C²H f4⁴ (mod s_plus)`.

Therefore N is coprime to both s factors. Reduction modulo `m4` gives `N≡D² f4⁴`, modulo `f4` gives `N≡m4⁴`; those residues are units because `gcd(m4,f4)=1` and `D|f4`. Lastly N is odd. Consequently

`gcd(N,4 f4² m4² s_minus s_plus)=1`. (8P.2)

So (8P.1) is the **genuinely reduced** x-coordinate: `K_3>=N²` with no uncharged cancellation.

Now `A²B²<=C⁴/4` by `(A²−B²)²>=0`, hence `m4>=3C⁴/4`. Also `N>=m4⁴`. Since `10·3⁸>4⁸`,

`K_3>=N²>=m4⁸> C³²/10`. (8P.3)

This exact lower bound on a reduced rational numerator is the key new input.

## 3. Explicit certified λ₃ lower bound

Let `L=log₂ C`. Every positive primitive Pythagorean hypotenuse obeys `C>=5` and hence `L>9/4`, since `5⁴=625>512=2⁹`. By `D<C², H<2C²`,

`c_E=bit_length(256D⁸H⁴)<13+24L`. (8P.4)

From (8P.3), `bit_length(K_3)−1=floor(log₂ K_3)>32L−5`, because `log₂ 10<4` and floor(x)>x−1. Substituting into S252's **original** lambda definition at k=3:

`lambda_3>[3(32L−5)−2(13+24L)]/768`
`=(48L−41)/768=L/16−41/768`.

Because `L>9/4`, this exceeds `67/768>0`. Therefore **S252's doubling-to-positive routine terminates by k=3 on EVERY primitive labelled base**, not only the ten historical diagnostic bases. This is a derived exact result, not a restatement of S308's older normalized-16P coefficient bound or S316's older low-base tiny absolute height floor.

## 4. Absolute N4 and N1 bounds, with no floating-point endpoint

Retain precisely S270's definitions: `H_o=oddpart(H)`, `c=1` for A even, c=2 for A odd, `Z4=ceil(16 C⁷H_o¹⁶/(A³c²))`, `beta0=1/2+c_E/12`,

`K4=bit_length(Z4)/8+c_E/24`, `a4=(3/49)lambda_3`,
`N4=max{N>=0:a4N²−beta0N−K4<=0}`.

S270 also defines

`K1=bit_length(Z4)/8+13c_E/300`, `a1=(26/1225)lambda_3`,
`N1=max{N>=0:a1N²−beta0N−K1<=0}`.

Because `H_o<=H<2C²` and `A,c>=1`, the *integer* `Z4<=2²⁰ C³⁹`; hence `bit_length(Z4)<22+39L`. Together with (8P.4), obtain the uniform upper comparisons

`beta0<2L+19/12`,
`K4< (47/8)L+79/24`,
`K1< (1183/200)L+497/150`.

Use `lambda_3>L/16−41/768`. For the S270 N4 quadratic at the **single integer** n=1152, lower-bound its value by

`Phi4(L)=[3/49](L/16−41/768)·1152²−(2L+19/12)1152−[(47/8)L+79/24]`.

Its slope in L is positive. At the exact rational endpoint L=9/4,

`Phi4(9/4)=300191/4704>0`. (8P.5)

Thus the *true* S270 quadratic is positive at n=1152 for ALL bases. Since a4>0, its polynomial starts negative at n=0 and has a unique positive zero. Hence `N4<=1151` universally.

For the 1%-mass N1 quadratic, evaluate at **n=3300**:

`Phi1(L)=[26/1225](L/16−41/768)·3300²−(2L+19/12)3300−[(1183/200)L+497/150]`.

Again the slope in L is positive, and the exact rational endpoint is

`Phi1(9/4)=8522743/117600>0`. (8P.6)

Thus `N1<=3299` for ALL primitive positive labelled bases. These are universal analytic inequalities; the accompanying bounded replayer only verifies algebraic implementation and old S270 calibration.

## 5. Consequences for R5 post-theorem closure planning

Let `I_idx` denote the **selected indexed INNER Branch B original complete source**, not an unproved cover of the wider physical population. C157's residual signed indices are:

`EVEN: all signed n with |n|>=12`, OR
`ODD: signed n with |n|>=7199 and n≡1 (mod32)`, all historic masks retained.

**UNCONDITIONAL NECESSARY RESTRICTION on I_idx:** EVERY residual ODD index necessarily has all four exact-top GOOD/H pools nontrivial AND `U_i^100>=b_m` individually, because 7199>=3300. This is a quantitative four-branch target for R2. It is NOT an upper bound and does not exclude a packet.

**NEW CONDITIONALLY SUFFICIENT R2 route (TOP MASS GAP):** If R2 proves on the SAME original complete source that for **every** primitive labelled base and every surviving signed |n|>=3300, at least one of the FOUR TRUE exact-top `GOOD or ACTUAL critical-H` branch products has `U_i^100<b_m`, then ALL such indices are impossible by (8P.6) and S270. Only the even signed indices `12<=|n|<=3299` remain: **3,288 signed index slots** with a still infinite moving-base family. An independent all-base exclusion for all those finite index slots completes indexed Branch B, without any need to prove R1/R2/R3 all completed or R4 finished. This result sharpens the old R2 “GOOD one-hole” plan because no moving M1(H_o) cutoff is used.

**STRONGER TOP ONE-HOLE route:** If R2 proves `min(U_i)=1` for all original complete-source signed `|n|>=1152`, then ALL such indices are impossible by (8P.5). Only signed even `12<=|n|<=1151` remain: **1,140 signed index slots**, still infinitely many primitive bases. A separate full-source exclusion of these slots is required. These future R2 upper lemmas are **UNPROVED**, and their source assumptions may themselves be difficult; nothing here manufactures them.

**R1 SOLO:** Older R5 C145 HΣ3 and full same-source mask contradiction is already a sufficient conditional route for indexed Branch B and gets ZERO repeated credit. The new finite-set compression means that an R1 *only-low-even* all-base theorem (slots <=3299 or <=1151, as appropriate) would suffice **jointly with R2 high-index result**, but R1's current all-index success remains unproved.

**R3 SOLO:** A complete all-index moving-family rational-point source classification and exclusion would suffice; present fixed D18/±12 information is NOT such a cover. Alternatively R3 could exclude the finite index slots and combine with future R2 high-index contradiction. Fixed index slots are NOT finitely many moving bases and do not automatically admit exhaustive rational-point proof.

**WIDE SOURCE GAP:** No result establishes `B_wide⊆I_idx`; swap EX1 is at-most-one indexed orientation, not existence of indexed orientation. The theorem only pertains to original selected indexed inner B, and wider closure requires a separate adapter/exclusion.

## 6. Exact proof of the GOOD-only moving cutoff obstruction

The prior R5 C157 GOOD one-hole argument requires `m>max(N4,M1(H_o))`, with `M1=floor((H_o−1)/8)`. This M1 has NO base-independent upper bound: take `u=2k, v=1`, `A=u²−1, B=2u, C=u²+1`, k>=1. This is a primitive B-even positive labelled base. Then `H=2(u⁴+1)`, `H_o=u⁴+1`, `M1=u⁴/8=2k⁴→infinity`. This explicit infinite family proves that replacing GOOD/H by GOOD alone in the uniform top mass theorem is invalid. No actual physical H-denominator event is asserted for these bases.

## 7. Deduplication, interpretation and R0 audit requests

SOURCE-OLD (ZERO repeat credit): S252 duplication/height comparison and positivity algorithm; S267 H first-entry congruence; S268 canonical b top/proper allocations; S269 global Gaussian/shared quartic; S270 N4/N1 four-branch necessity and 1%-mass inequalities; S308 old normalized x(16P) lambda4; S316 unconditional all-base low-height floor and high-index count; S317 conditional near-quarter mass distribution on odd-rough indices; R5 older C145/146 solo-closure case table and C157 GOOD-only one-hole per-base T(a).

POTENTIAL PROJECT-NEW DIFFERENCE: explicit primitive original x(8P) FULL gcd=1 rational numerator certificate, uniform k=3 lambda positivity with coefficient in log2 C, and absolute S270 thresholds N4<=1151, N1<=3299 with R5's exact source-locked post-theorem closure routing. Targeted bounded Drive queries for exact thresholds, 'uniform k3 lambda', x8P numerator, TOP branch bounds found no equivalent combination. This is a bounded PJ comparison only, not proof of historical/literature priority. If S308/another prior artifact already implies this bound more directly, downgrade to OLD/EQUIVALENT. The portable exact verifier samples 2074 primitive labelled bases and independently checks original E group law/gcd and both threshold endpoints. Finite replay is *not* the proof of universal quantifiers.

R0 independently audit (i) x([4]P), x([8]P) exact fractions and coprimality for **both** orientations; (ii) S252 normalizing bit_length/lambda3; (iii) rational endpoint arithmetic `300191/4704` and `8522743/117600`, monotone-in-L slopes; (iv) S270 definitions of N4/N1 and H-vs-GOOD population; (v) historic INDEX/S308/S316/S317 dedup; (vi) source scope and continuing UNKNOWN low even index cover; (vii) keep all R1-R5 STATE and R0 controller permissions unchanged.

PRIMARY SOURCES (Drive):
- S252 https://drive.google.com/file/d/1xXbdt9AD-HEdo2XmwIVRQ8ymY7_ahb5z/view
- S270 https://drive.google.com/file/d/11Khz8znsWCzovBnWPDhZvsE36IBTAYRh/view
- S308/S316 comparison https://drive.google.com/file/d/1c_5feVjzkD4I8zSPKJhYD_FfrQeAEPLn/view
- S317 https://drive.google.com/file/d/1gRPENh1fX50RZHpSxWi9S61xXTe_rfsWexnUC5-KnL8/view
- Previous R5 post-C157 one-hole https://drive.google.com/file/d/19pCa5Ipf1QNsOKnqNRv0MflZyLE-F2Ua/view
- C157 R0 receipt https://docs.google.com/document/d/1fVQDbA2licjGxF8NjXDYWRjnTKas5kFgNER0srtkVfw/edit
