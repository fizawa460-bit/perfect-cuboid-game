# M3-T11-212 — endpoint-safe raw graph host and cleared ordinary character receiver

Stage37 current research card; 2026-10-03. Status: PROVED_HOST_ADAPTER_AND_NORMALIZATION_COST / ACTUAL_GRAPH_CORRELATION_OPEN. Gate OPEN; global counting credit 0. No retraction. Independent audit for 186–212 NOT RUN; the 162–185 audit scope is unchanged.

## 1. Scope and result

Continue 211's ordinary zero-layer receiver, retaining 207–208's sorted primitive raw two-face sphere, intrinsic R<=B, canonical eligible face-pair choice, M_2R branch mask and content tail c_chart>C. Here C=B^gamma, gamma=1/6+xi<1/4 when discussing the target T=B^(1/2-gamma+o(1)). c_chart is the cross-content of the chosen eligible pair; it is not c_u. On full endpoints it agrees with the all-pair maximum under the established canonical choice.

Let X be that actual physical support. Define X*=X intersect {the three positive physical edge lengths are pairwise distinct}, and N*=|X*|. This extra postfilter is endpoint-safe: a full endpoint with two equal edges would require the corresponding integral face diagonal to equal a*sqrt(2), impossible for positive integer a. Thus every counted endpoint remains in X*. This argument does NOT exclude equal-edge raw two-face objects from X, does not invoke the nonexistence of perfect cuboids, and does not claim an upper bound for unfiltered X without a separate equal-edge argument.

New certified input: N*<=B^(1/2+o(1)), uniformly in the retained masks and C, inherited from the full Stage14 raw graph proof, including triple-face endpoints. This supplies the missing long-prime-pool host budget in 211 after the safe postfilter. The inherited exponent is not a new global saving. A second exact reduction clears the gcd normalization in A± and pays all affected prime pairs by O(N*/Q). No cancellation of the actual graph character sum has been proved.

## 2. Full-endpoint-inclusive graph injection

Verified source: Stage14 final.md, Drive file 1JmRC2GSXxhYOt9ANyeJn2JjoDrl2J6_y, especially Lemmas 3.1–3.2 and Proposition 3.6, not merely its final exactly-two theorem. The independently matching R06 HTML is 1rvtE0fC0u833u4Um6hH-NofFx3VUfQwx. Stage37 active CROSS-GCD route 1hRZvWUMvITpvzj8E6AI8hFnOc0PTmB1yO6RvvB6rhUg states the same raw graph contract. AR003/AR004 gluing and incidence convention are retained.

The proof contract used here is: the raw graph for 0<a<b<c and integral space diagonal R<=B has a primitive oriented Pythagorean face at each vertex and each compatible pair of such faces sharing a physical edge as an edge. Its edge count is E_graph=N_2+3*T_full. Uniform degree Delta=B^o(1) and active-vertex count V<=B^(1/2+o(1)) imply E_graph<=V*Delta/2<=B^(1/2+o(1)). The full endpoint component is present before the exactly-two selection. Proposition 3.6 bounds the whole active face set; it is not an estimate conditional on absence of the third face. The source's detailed proportional/nonproportional branches are retained in that source, not re-proved by finite verification here.

For a chosen face pair with physical shared edge a and other edges b,c, set d1=gcd(a,b), d2=gcd(a,c), F1=(S1,X1,H1)=(a/d1,b/d1,sqrt(a²+b²)/d1), and F2=(S2,X2,H2) analogously. The S-coordinate records which leg is shared. With g=gcd(S1,S2), primitive physical gluing gives

    a=S1*S2/g, b=S2*X1/g, c=S1*X2/g.

Indeed gcd(a,b,c)=1 gives gcd(d1,d2)=1 and g=a/(d1*d2). Thus the unordered pair of oriented face vertices reconstructs the physical object; deterministic canonical selection gives an injection X* -> E_graph. Intrinsic height and all physical masks are subfilters, never new independent variables. A full endpoint selects one of its three graph edges; we do NOT divide the bound for all edges by three, since exactly-two objects have one edge. This proves N*<=E_graph and the stated inherited half-power bound.

## 3. Cleared normalization and aggregate bad-prime cost

Use the exact 208 receiver h=gcd(R,a), eps=2 if a is odd and eps=1 otherwise, and positive integers A±=(R±a)/(eps*h). Define

    K±=eps*h*(R±a)=(eps*h)^2*A±.

K± is positive and <=4B². It is a square if and only if A± is a square, and both are squares at every full endpoint. For every odd prime p, ordinary Legendre symbols, including zero, satisfy

    chi_p(K±)=chi_p(eps*h)*chi_p(R±a).

For p not dividing h, this equals chi_p(A±), since eps*h is a nonzero square multiplier after squaring. For p dividing h the cleared symbol is zero and equality with chi_p(A±) is not asserted. No modular inverse of h is taken; no independent gcd-density estimate is used.

Fix a common prime pool S of Q distinct odd primes, all p>=P>1. For sigma in {-,+}, define on precisely X*

    G_sigma(p,q)=sum_x chi_pq(A_sigma(x)),
    C_sigma(p,q)=sum_x chi_pq(eps(x)*h(x))*chi_pq(R(x)+sigma*a(x)).

Write s(x)=#{p in S:p|h(x)}. Since h<=B, s<=D_h=floor(log B/log P). For a fixed x, at most s*Q-s*(s+1)/2 <=s*(Q-1) unordered pairs meet this bad set. On each such pair, the absolute difference of the two object contributions is at most 1, because the cleared contribution is zero. Therefore

    sum_(p<q) |C_sigma(p,q)-G_sigma(p,q)|
      <= N* D_h (Q-1).

After division by a denominator asymptotic to Q², the replacement cost is O(N*/Q) for fixed beta in P~B^beta. This handles the h-supported normalization error in aggregate without excluding endpoint primes or silently assuming h=1. 211's summed nonzero-depth costs remain retained; this card supplies a compatible graph receiver, not a new depth decomposition.

There is also a direct ordinary square-score inequality for K. Put d_K=floor(log(2B)/log P). At an endpoint sqrt(K_sigma)<=2B, so at most d_K pool primes divide that integer square root. The score sum_p chi_p(K_sigma) is consequently >=Q-d_K. For Q>d_K, expansion of the average of the two squared scores yields

    E(X*) <= [N*Q + sum_(p<q)(C_-(p,q)+C_+(p,q))] / (Q-d_K)^2.

The diagonal is bounded by N*Q because chi_p(K)^2<=1. This uses ordinary symbols only and is not the full local detector J_B of 209. Replacing each C by |C| gives a sufficient, possibly weaker, upper bound. The graph sum is weighted by the canonical choice, the exact sphere/two-face condition, M_2R, content tail, primitive constraint and intrinsic height. These weights may not be discarded or tensorized, and h remains a physical gcd inside the coefficient.

## 4. What is now paid; precise residual theorem

For a dyadic prime pool p in [B^beta,2B^beta] with gamma<beta<1/4, its usual cardinality is Q=B^(beta+o(1)); alternatively keep every statement in the explicit parameters P,Q. The inherited host bound now gives N*/Q<=B^(1/2-beta+o(1)), strictly below the requested tail target B^(1/2-gamma+o(1)). d_K and D_h are O_beta(1). Both the diagonal and the normalization replacement cost fit this budget. Ordinary modulus pq has size B^(2beta)<B^(1/2), but its being below this scale alone supplies no cancellation.

Still required: a theorem for the actual weighted raw-graph sums C_sigma, for example

    sum_(p<q)(|C_-(p,q)|+|C_+(p,q)|)
      <= Q² B^(1/2-gamma+o(1)),

with the correct masks and family/content costs, or a suitably bounded signed sum in the exact inequality. No such theorem is proved here. Completing a period, separating R and a, treating h as an independent weight, or using the exactly-two bound alone is invalid. The original broad raw-tail N(X) estimate remains separate because equal-edge raw objects were not generally excluded. All full endpoints are nevertheless retained in X*, which is sufficient for this endpoint receiver. large-c_u/full-S, large W, unshared conductor and fixed-q_min/low-median averaging remain OPEN.

## 5. Verification and reproducibility

Reproducible standard-Python script stage37_graph_212.py and output M3-T11-212-verification.json use the exact 208 source JSON, Drive 1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG, SHA256 3bce05e1ded1adabf70dd597de2e76ed8c0d4fdc96f604a2b5b7de239280adcd. They check 255 injective primitive oriented graph reconstructions and canonical cross-gcd identities; 5,100 physical cleared-character identities; 2,520 abstract normalization cases, including h divisible by pool primes; and the aggregate bad-prime pair bound. For the three inherited gamma examples 3/16,5/24,11/48 the finite masked tail has N*=22 and correlation difference zero. Those physical examples have h=1; this is not a theorem that h=1 generally. Abstract cases exercise the h>1 exception.

All checks PASS. Finite checks neither prove the inherited asymptotic graph bound nor provide character cancellation or endpoint existence/nonexistence. That bound is used from the source proof with the scope stated above. Independent audit NOT RUN.

Drive verification artifacts: SCRIPT_FILE_ID=1IWwOeQVCRg18y9v89EC5KPR1cxKprFX_; JSON_FILE_ID=1x-fQpI7yN0xML9wo-7_mBlBB4TmXD_3m. Both are in Stage37's auxiliary-artifact folder. INPUT_JSON_FILE_ID=1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG.

## 6. Handoff

NEXT213: prove an actual weighted raw-graph C_sigma two-prime correlation theorem, or identify and prove a structural graph decomposition that supplies it, with all canonical sphere/M_2R/content masks paid. Use X* and the certified half-power host bound; do not reopen 211's aggregate depth payment or assume broad X has distinct edges. 209 exact detector, 210 short-pool budget and 211 depth lemma remain retained. MAIN/INDEX/short RESULT-LEDGER should point to this card and NEXT213. Proof text belongs here once; the ledger records only the change and authoritative links.
