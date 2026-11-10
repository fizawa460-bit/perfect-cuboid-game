# M3-T11-213 — fixed-face curve character receiver and sparse L1 completion firewall

Stage37 research card, 2026-10-03. PROVED_EXACT_CURVE_ADAPTER / COMPLETE_LOCAL_BOUND / SCOPED_L1_COMPLETION_OBSTRUCTION. Actual physical signed correlation OPEN; Gate OPEN; global counting credit 0. No retraction. Independent audit 186–213 NOT RUN; 162–185 scope unchanged.

## 1. Current physical measure and contribution

Use precisely 212's endpoint-safe X*: sorted primitive raw two-face sphere, intrinsic R<=B, deterministic eligible canonical pair, M_2R branch mask and c_chart>C, with pairwise distinct physical edges. Every full endpoint is retained. N*=|X*|<=B^(1/2+o(1)) and the uniform oriented-face raw graph degree Delta(B)=B^o(1) are inherited from the verified Stage14 proof, not new exponents.

This card proves an exact fixed-face genus-one receiver for the cleared characters C_sigma of 212. Its complete finite-field character average is O(1/sqrt(pq)) uniformly at good primes. It also proves that replacing the actual sparse partner measure by this complete measure and bounding the error by its full L1 norm cannot furnish a saving relative to N_good: that norm is (2-o(1))N_good. This is a scoped obstruction to that completion method, NOT a no-go for signed character cancellation, moving-family averaging or the overall route. Existing 158's interval/large-sieve obstruction and PARAM-NEG-001 remain retained; this is a specific face-graph adapter and sparsity theorem, not renewed generic CRT evidence.

## 2. Exact curve and character map

For each canonical chosen pair, order its primitive oriented face vertices lexicographically and charge the first one F=(S,X,H), S²+X²=H², S,X,H positive primitive integers. If its physical face edges are a=dS,b=dX and its other physical edge is c, set

    t=c/d, v=sqrt(a²+c²)/d, w=R/d.

Then the actual rational point lies on

    E_F: v²=t²+S², w²=t²+H².

Conversely the positive primitive physical point retains d, height, the chosen pair and all masks; no complete curve is substituted for the physical point set. Here d=gcd(a,b) and gcd(d,c)=1, so the reduced denominator of t recovers d. Each F receives at most Delta(B) objects, by 212's graph injection and the inherited degree bound.

Let h=gcd(R,a) and eps=2 for a odd, 1 otherwise. The exact identity is

    K_sigma=eps*h*(R+sigma*a)=eps*h*d*(w+sigma*S).

At primes not dividing d, this holds on reduction of the rational point. Thus the cleared ordinary character equals chi_p(eps*h*d) chi_p(w+sigma*S). The scale coefficient is genuinely object-dependent; it is NOT set to 1, presumed independent, or averaged independently of the curve.

## 3. Good-prime cost and uniform complete local bound

For each object define the nonzero integer

    L_x=2*d*h*S*X*H*|S²-X²| <= 2B^7.

S!=X over Q because S²+X²=H² has no positive integral equal-leg solution. A common pool of Q primes p>=P contains at most D_7=floor(log(2B^7)/log P) primes dividing L_x. Removing from a two-prime sum all object contributions for which either prime divides L_x costs, per branch summed over unordered prime pairs, at most

    N* D_7 (Q-1).

This follows by counting the pairs meeting the object's bad set before summing objects, exactly as in 212. For P~B^beta with fixed beta>0 it is O(N*Q), hence O(N*/Q) in the normalized score. This simultaneously pays bad reduction, denominator and scale primes without deleting endpoints from the score inequality: their removed contributions are accounted for as error.

At an odd prime not dividing 2SXH, the smooth projective model of E_F is geometrically connected genus one. Proof: its degree-four biquadratic map to the t-line has four distinct branch locations t=±iS,±iH; each has two ramification points of index two. Riemann–Hurwitz gives 2g-2=-8+8=0. At infinity it has four rational points [t:v:w:z]=[1:±1:±1:0]. Thus its affine point count M_F(p) satisfies

    |M_F(p)+4-(p+1)|<=2sqrt(p),
    M_F(p)>=p/2 for p>=29.

For p additionally not dividing S²-X², the rational function f_sigma=w+sigma*S has four simple zeros: w=-sigma*S, t²=-X², v²=S²-X². It has four simple poles at the points at infinity. Consequently it is geometrically nonsquare, its double cover zeta²=f_sigma has eight branch points, and the smooth cover has genus five by Riemann–Hurwitz. Above every infinity point the cover has one ramified rational point. Therefore the complete affine character sum is exactly the projective point-count difference between the cover and E_F, with no uncharged boundary term:

    T_F,sigma(p)=sum_(P in E_F^aff(F_p)) chi_p(f_sigma(P)),
    |T_F,sigma(p)|<=12sqrt(p).

The bound uses the ordinary Hasse–Weil inequality on genera five and one. Reference for the standard theorem and genus/cover background: Bjorn Poonen, Lectures on rational points on curves, §§2.9,3.1–3.3, https://math.mit.edu/~poonen/papers/curves.pdf (read for this batch). The explicit curve, branch computation and its application here are derived above; the reference is not a theorem about Stage37's integer population.

For distinct good p,q>=29, CRT gives the complete affine product set Omega_F(m)=E_F^aff(F_p) x E_F^aff(F_q), m=pq, size M_F(m)>=m/4, and complete average

    mu_F,sigma(m)=T_F,sigma(p)T_F,sigma(q)/M_F(m),
    |mu_F,sigma(m)|<=576/sqrt(m).

Uniformity includes moving F at good primes. This is a complete residue-set theorem only; no physical equidistribution follows.

## 4. Exact weighted discrepancy receiver

For each p,q, keep only the object contributions good at both primes. For each charged face F and coefficient residue z=eps*h*d mod m in (Z/mZ)^*, let nu_F,z(P) count the actual objects reducing to P in Omega_F(m). Let n_F,z=sum_P nu_F,z(P). Every physical mask is built into this counting measure. Set

    phi_sigma(P)=chi_p(w_p+sigma*S)chi_q(w_q+sigma*S),
    delta_F,z(P)=nu_F,z(P)-n_F,z/M_F(m).

Then exactly

    C_sigma^good(p,q)=U_sigma(p,q)+D_sigma(p,q),
    U_sigma=sum_(F,z) chi_m(z)n_F,z mu_F,sigma(m),
    D_sigma=sum_(F,z) chi_m(z)sum_P delta_F,z(P)phi_sigma(P).

In particular |U_sigma|<=576 N_good/sqrt(m). The z-strata are an exact partition of the real coefficient, not an independent scale variable. Summing this complete term over a dyadic pool p~B^beta and normalizing by Q² costs O(N*/P). Together with bad-prime cost O(N*/Q), 212's diagonal and 211's aggregate depth cost, it lies below T=B^(1/2-gamma+o(1)) when gamma<beta<1/4, Q=B^(beta+o(1)). Constants are absolute here; the o(1) is inherited only from the physical host/degree and prime-pool cardinality.

Remaining sufficient target:

    sum_(p<q)(|D_-(p,q)|+|D_+(p,q)|)
      <= Q² B^(1/2-gamma+o(1)),

or an appropriate signed average inserted into 212's exact score inequality. This remains OPEN. Summing family-wise absolute errors or replacing D by an L1 norm fails to supply a relative saving, as shown next.

## 5. Sparse L1 completion obstruction

For any nonnegative measure nu of total mass n on M points with occupied support r, let delta=nu-n/M. Its empty cells contribute (M-r)n/M to the L1 norm, and its occupied cells contribute at least the same amount by the triangle inequality. Hence

    2n(1-r/M)<=||delta||_1<=2n.

Apply this to each actual (F,z) block. Its occupied support r<=n_F,z<=Delta(B), and M_F(m)>=m/4. Therefore, with L1(p,q)=sum_(F,z)||delta_F,z||_1,

    2N_good(1-4Delta(B)/m)<=L1(p,q)<=2N_good.

For p,q~B^beta and fixed beta>0, Delta(B)/m=B^(-2beta+o(1)), so L1=(2-o(1))N_good uniformly, wherever the good population is nonempty. This does not require a positive lower bound for N_good. It rules out an o(N_good) full-L1 equidistribution theorem on this exact fixed-face completion. It does not rule out |D_sigma|=o(N_good), since the signs and the character test can cancel despite large L1 distance.

If N* is already below the target, direct counting suffices; this obstruction matters when trying to improve the inherited N* ceiling by completion. Do not misread it as an impossibility theorem for physical correlations or an endpoint count. Aggregation over moving faces or another genuinely arithmetic character-sensitive input is still available.

## 6. Exact verification and continuation

stage37_curve_213.py uses the Drive source208 JSON (file 1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG; SHA256 3bce05e1ded1adabf70dd597de2e76ed8c0d4fdc96f604a2b5b7de239280adcd). It verifies 255 rational adapters, 183 distinct charged faces, 2,564 complete good face/prime cases (including both complete character sums and Hasse count), 7,126 physical good-prime phase identities, and five exact rational CRT/discrepancy/L1 identities on the same 22-object masked tail. All PASS. Genus and asymptotic statements follow from the proofs above and retained source contracts, not finite extrapolation. No independent audit or physical cancellation theorem is claimed.

NEXT214: prove a character-sensitive estimate for the actual signed D_sigma summed over moving F,z and prime pairs, or a structural arithmetic decomposition that yields it with all canonical/height/M_2R/content costs. Do not seek a small full L1 error in each fixed-face fiber; 213 proves that premise false in the sparse regime. Do not discard z, tensor independent variables, or reopen the already-paid 211 depth layers. 212 endpoint-safe host and normalization, 210 short-pool budget, 209 exact detector and other retained sectors remain unchanged. c_u/full-S joint occupancy is still a separate OPEN gate. Proof occurs here once; MAIN/INDEX/short LEDGER should point to this card and NEXT214.

Drive reproduction artifacts in the Stage37 auxiliary folder: SCRIPT_FILE_ID=1EdGJG5bZKWsPRUBod1kvEaIKzcdj8tvC; JSON_FILE_ID=1EH_dvFzmnL57kZz-yNEInlUSc8SjkaV5. Source-input ID is recorded above. MAIN/INDEX/LEDGER carry the writeback verification receipt.
