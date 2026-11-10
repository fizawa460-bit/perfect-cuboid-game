# M3-T11-211 — Summed physical depth layers fit the diagonal budget

STATUS=PROVED_SAME_PHYSICAL_AGGREGATE_DEPTH_BOUND / ZERO_LAYER_CORRELATION_OPEN / GLOBAL_COUNTING_CREDIT=0.
Authority: fresh Drive MAIN/INDEX/shortLEDGER/latest210 and active ROUTE17/157 checked selectively. Gate OPEN;TI parked;120 retracted;147–149 frozen. No retraction. Independent audit162–185 retained;186–211 NOT RUN.

## 1. Result and scope

210 left the nine nonzero valuation layers as potential individual correlation targets. They can all be paid together on the actual physical population, without an equidistribution or character-cancellation theorem. For a large-prime pool of cardinality Q, their contribution to the endpoint second-moment bound is O(N/Q), the same order as the diagonal; layers deep at both primes cost only O(N/Q²). Thus separate cancellation in the highest p^6 layer is not needed for this moment route. The surviving analytic target is the zero-layer ordinary two-prime physical character sum, plus the already identified N/Q budget.

This is an aggregate counting bound on the same population, not a new density, new sieve method, or an absolute tail saving. The elementary second-moment principle of157/210 is reused.210's exact layers, hidden-unit example and short-pool diagonal obstruction remain valid; its suggestion to attack each deep layer separately is refined by the summed bound here.209's full local detector/J_B is retained unchanged. No ordinary Legendre test is claimed equivalent to the full Q_p-square detector.

Use207–210's sorted primitive R2(B) with at least two integral faces, canonical eligible maximizing pair, c_chart,shared edge a,h=gcd(R,a),epsilon,D,u and A±=(D±u)/epsilon. All sphere/two-face/primitive/canonical masks and intrinsic R<=B remain. X(B,C) is the c_chart>C,M_2R tail, N=|X|. Every endpoint with c_max>C lies in X, and its two branches are positive integer squares. A±<2B. c_chart=c_max on endpoints only; c_u/full-S is separate. The following proof sums over X directly and never counts an enlarged ambient residue population.

## 2. Uniform square-prime incidence bound

Fix a set S of Q distinct odd primes, all p>=P>1. Put
d=floor(log(2B)/(2 log P)).
For each positive integer A<2B let D(A)={p in S:p² divides A},s(A)=|D(A)|. Distinct squared primes have product at least P^(2s), which divides A; hence s(A)<=d. This is pointwise, uniform in all contents, charts, kernels and physical objects.

Let chi_p be the ordinary Legendre symbol with value0 on multiples of p, and let lambda_p(A)=chi_p(sqf(A)) as in210. These symbols differ only when v_p(A) is positive and even. In particular

|lambda_p(A)lambda_q(A)-chi_p(A)chi_q(A)|
 <= 1_{p in D(A) or q in D(A)}                              (211.1)

for distinct p,q. Both products have absolute value at most1; when a change occurs the ordinary product is0, so the difference has absolute value at most1, not2.

There are exactly sQ-s(s+1)/2 unordered prime pairs meeting D(A). Therefore, with H_sigma(p,q) the210 kernel correlation and G_sigma(p,q)=sum_{e in X}chi_pq(A_sigma(e)) its ordinary zero layer,

sum_{p<q}|H_sigma(p,q)-G_sigma(p,q)|
 <= sum_{e in X}[s_sigma(e)Q-s_sigma(e)(s_sigma(e)+1)/2]
 <= Nd(Q-1).                                               (211.2)

No claim that individual square-divisor strata are sparse in X is made; a stratum could contain every object for one prime. The saving comes from summing the prime incidences at fixed actual A, then summing the objects. This order keeps all moving family/content costs in N exactly once.

## 3. Absolute budget for every nonzero layer

210 gives H_sigma(p,q)=sum_{j,k}H_sigma,j,k(p,q), with integer quotients and p^(2j)q^(2k)|A_sigma. At fixed A,p,q at most one term can be nonzero: the valuations at both primes must be even and j=v_p(A)/2,k=v_q(A)/2. If either valuation is odd all terms vanish. Thus triangle inequality before summing yields the stronger layerwise statement

sum_{p<q}sum_{j+k>0}|H_sigma,j,k(p,q)| <= Nd(Q-1).           (211.3)

It is not necessary to rely on cancellation between layers to prove this bound.

For the interior layers j>=1,k>=1, both primes lie in D(A); hence

sum_{p<q}sum_{j>=1,k>=1}|H_sigma,j,k(p,q)|
 <= sum_{e in X}binom(s_sigma(e),2) <= N binom(d,2).         (211.4)

If P^8>2B,210's ten-slice expansion applies and d<=3. Summing both branches gives at most2Nd(Q-1) for all nine nonzero layers, and2N binom(d,2) for the interior ones. After division by Q² these costs are O(N/Q) and O(N/Q²), respectively. The axial layers are retained and paid; the interior layers are retained and paid more cheaply. No higher-p-power local gain is credited.

The argument actually works without the ten-layer cutoff: all possible even-valuation layers are summed by the same incidence proof. The bounded ten-slice representation is useful for exact replay, not an extra analytic assumption.

## 4. Reduction to ordinary physical two-prime sums

Insert(211.2) into210's exact endpoint second moment and drop its nonpositive odd-valuation correction. With E=#E(B;c_max>C),

E <= [1+2d(1-1/Q)]N/Q
     + Q^(-2)sum_{p<q}[G_-(p,q)+G_+(p,q)].                 (211.5)

Replacing the final sum by sum(|G_-|+|G_+|) gives a conventional sufficient upper certificate. At fixed beta>0 and P=B^beta, d=O_beta(1), so the total depth cost fits the existing diagonal order. The earlier concern about the individual deep-layer character period exceeding branch height is still true, but no completion in that period is used here.

A sharper standard zero-stratum version uses the ordinary branch score directly. An endpoint has A_sigma=root²; only primes dividing its root give chi_p(A_sigma)=0, and there are at most d such primes. Consequently sum_{p in S}chi_p(A_sigma)>=Q-d. If Q>d, positivity of the two squared scores gives

E <= [sum_{e in X}{(sum_p chi_p(A-))²+(sum_p chi_p(A+))²}]/[2(Q-d)²]
  <= [NQ+sum_{p<q}(G_-+G_+)]/(Q-d)².                      (211.6)

This is an upper bound for counting squares with a correctly paid zero stratum, not the exact detector. The numerator inequality uses ordinary diagonal terms<=2NQ; the underlying exact numerator is nonnegative. The absolute-G version is also sufficient. As Q grows, its diagonal is N/Q times1+O(d/Q). No assumption about nonendpoint zero residues is required. Ordinary zero residues are permitted in X, and every prime dividing R stays in the fixed prime pool and in G; none is silently declared negligible or independent.

Only G_sigma(p,q)=sum_{e in X}chi_pq(A_sigma(e)) now needs a genuine physical character theorem for this second-moment route. Integers A± and quotients are formed before modular reduction; moving h,epsilon and the two-face equations cannot be replaced by modular inverses or an ambient interval.157's Euler-brick terminal numerator is a different measure and cannot be substituted for G.

## 5. Remaining budget and a longer-pool window

210's short-pool obstruction is unchanged: with Q<=O(B^alpha),alpha<1/6 and C=B^gamma,gamma=1/6+xi,0<xi<1/12, an absolute second-moment certificate still requires the N saving of210.5. Paying the depth layers at diagonal order does not supply that saving or signed cancellation.

There is now no need to constrain a counting prime pool by209's completeness cutoff. For every gamma in(1/6,1/4), one may test the candidate band P~B^beta with gamma<beta<1/4. This is a parameter choice, not a proved cancellation estimate. If its chosen cardinality is Q=B^(beta+o(1)), and if a correctly adapted theorem supplies N<=B^(1/2+o(1)) on X, then N/Q is below the desired B^(1/2-gamma+o(1)). Moreover P^6>2B eventually, so d<=2 and only j+k<=2 occurs (six slices, all paid by§3). The remaining ordinary character modulus pq is O(B^(2beta)), below B^(1/2). This does not imply physical interval coverage or justify completion on the occupied support. It specifies the concrete remaining modulus range.

Do not use a theorem about EXACTLY-two objects alone as a bound on X, which also contains full endpoints. The inspected Stage14 Arsenal AR-006 is expressly exactly-two; a half-power bound for X must cite and verify a receiver including its full endpoint component. The statements above remain conditional on that adapter. No new N upper or weighted-content tail has been proved here.172/175's moment obstruction is not reopened as a proved moment upper.

Thus the next analytic problem is either a same-X ordinary G estimate in this longer-pool window with an explicit N input, the short-pool missing N saving, a signed-correlation theorem, or another direct209 J_B count. It is no longer necessary to solve nine separate depth-layer cancellation problems for the ordinary second moment.

## 6. Replay and handoff

Source208 JSON DRIVE_ID=1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG; SHA256=3bce05e1ded1adabf70dd597de2e76ed8c0d4fdc96f604a2b5b7de239280adcd. This is the known255 raw objects at R<=10^6, not an extended census.

Verification:100000 dense integer checks of incidence bounds and square-score lower bounds;31 additional abstract integer cases include p^6=11^6 and two square-prime factors, verifying individual ten-layer and interior budgets.5940 physical pair/layer checks on the three known strict tails PASS. Abstract integer checks are not claimed to be physical objects.

For B=10^6,S={11,13,17,19,23,29,31,37,41,43},Q=10,d=3, each cutoff3/16,5/24,11/48 gives N=22. Minus-branch summed absolute depth is0, plus-branch9; each is below594. Interior depth is0, below66 per branch. Ordinary zero-layer signed sums are-9 and88, diagonals217 and218, moments199 and394. Formula(211.6)'s direct score bound is593/98; direct branch testing has endpoint0. This finite bound is deliberately not promoted to a tail theorem or universal prime cutoff.

SCRIPT_DRIVE_ID=1HZ36cLthKsnE9ywGpgu74-_CiuNDmU6Y (stage37_depthsum_211.py).
JSON_DRIVE_ID=1csezK5iXWctTlqIz1WKYm1ckcLuEoZmh (M3-T11-211-verification.json).
Reproduce with208 input and211 script in one directory: python stage37_depthsum_211.py. Standard Python only.

NEXT212: attack the actual zero-layer G_sigma(p,q), with all primitive/canonical/sphere/two-face masks and intrinsic height/content costs. Before claiming a longer-pool diagonal budget, verify an N bound including full endpoints; or instead prove the short-pool missing N tail. Do not independently reopen/rediscover the now-paid depth layers.209 exact detection,210 integer adapter/diagonal budget,205/206/171/174 sectors retained; c_max and c_u/full-S remain separate.

Adopted result: a uniform summed bound for all depth correlations on the same physical tail, with interior layers one extra Q factor cheaper. Total endpoint/tail count OPEN, global credit0. Readback PASS: card/code/JSON and source208 input downloaded from Drive and byte-compared; MAIN exact changes, INDEX14 fields/chip/link plus210 restart, and shortLEDGER history/control/append verified. Latest211/NEXT212 synchronized; Drive-only continuation ready. No independent hostile audit claimed.
