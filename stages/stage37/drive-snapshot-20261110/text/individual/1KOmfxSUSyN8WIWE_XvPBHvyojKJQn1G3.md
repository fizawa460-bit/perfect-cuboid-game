# M3-T11-210 — Ten-layer physical character receiver and short-prime diagonal budget

STATUS=PROVED_EXACT_VALUATION_LAYER_ADAPTER_AND_SCOPED_METHOD_BUDGET / FINITE_REPLAY_PASS / GLOBAL_COUNTING_CREDIT=0.
Authority: fresh Drive MAIN/INDEX/shortLEDGER/latest209; active ROUTE157 second-moment certificate and17 physical reconstruction checked selectively. Gate OPEN;TI parked;120 retracted;147–149 frozen. No retraction; independent audit covers162–185 only,186–210 NOT RUN.

## 1. Target and what is new

209 completes third-face detection but does not count the exact endpoint sum. This batch derives its squarefree-kernel character directly from the original integer branch through a bounded collection of valuation slices, then proves a necessary diagonal budget for the conventional absolute-correlation second-moment bound on this actual population. No character cancellation or asymptotic tail saving is proved.

The second-moment principle itself is reused from157, not a new sieve method.157 is on primitive Euler bricks with terminal T and zero-free inert primes; here the population is the canonical raw sphere/two-integral-face tail, the missing third face has the two coprime208 branches, and their square-part divisibility cannot be ignored.158's large-sieve collision-energy obstruction and the historical finite-tensor anti-loop remain. This card does not reopen those receivers.

Use R2(B),canonical maximizing eligible chart,c_chart,a,h,D,u,epsilon,A± and M_2R exactly as207–209. Every sorted primitive object is counted once. Define X(B,C)={e in R2(B):c_chart>C and M_2R(e)}, N=|X|. Every full endpoint with c_max>C belongs to X. A±=(D±u)/epsilon are positive coprime integers<2B. c_chart=c_max only on endpoints; c_u is separate. All original two-face equations, primitive/canonical masks, moving h and intrinsic R<=B remain inside X.

## 2. Kernel character is not the ordinary branch character

For an odd prime p and positive integer A, write v=v_p(A),U=A/p^v and kappa=sqf(A). Extend the Legendre symbol by chi_p(0)=0 and set

lambda_p(A)=chi_p(U) if v is even, and0 if v is odd.

Then lambda_p(A)=chi_p(kappa). In particular positive integer squares give lambda_p(A)=1 even when p divides their root. Also Q_p(A), the full Q_p-square indicator of209, equals (lambda_p(A)^2+lambda_p(A))/2.

The exact integer expansion is

lambda_p(A)=sum_{j>=0,p^(2j)|A} chi_p(A/p^(2j)).                 (210.1)

Proof: all terms before j=v/2 have a p-divisible argument and vanish; a final term occurs precisely when v is even, and equals the p-free unit symbol. There are no later divisible powers. This proof includes odd valuations, p|A and moving square roots. All quotients are evaluated as integers before reduction, never by an inverse of p.

This matters on the actual active tail: e=(48063,87584,281112),R=298337,c_chart=R passes M_2R; A-=210753=3²*23417. At p=3 (outside2R), chi_3(A-)=0 but lambda_3(A-)=chi_3(23417)=-1. Thus a modulo-p root test accepts the zero residue, while the full local condition fails. This is not a retraction of209:209 used full valuation/unit tests. It refutes silently replacing its kernel/unit character by the ordinary integer Legendre symbol without handling square-root divisibility. Standard ordinary square sieves with a correctly paid zero stratum are not refuted.

## 3. Four one-prime layers and ten two-prime layers

Let the fixed prime pool S have all primes p>=P>1. For p!=q, exact expansion of(210.1) gives

lambda_p(A)lambda_q(A)
=sum_{j,k>=0,p^(2j)q^(2k)|A} chi_pq(A/(p^(2j)q^(2k))),          (210.2)

where chi_pq=chi_p chi_q. Removing the other prime's even power does not change either nonzero unit symbol, which proves the identity including zero cases.

If P^8>2B then A<2B admits only j=0,1,2,3 in(210.1) and j+k<=3 in(210.2). Hence each same-branch two-prime physical sum has exactly the following ten possible slices:
(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),(3,0),(2,1),(1,2),(0,3).

For sigma in {-,+}, define
H_sigma(p,q)=sum_{e in X} lambda_p(A_sigma(e))lambda_q(A_sigma(e)).
Then H_sigma(p,q)=sum_{j+k<=3} H_sigma,j,k(p,q), with
H_sigma,j,k(p,q)=sum_{e in X,p^(2j)q^(2k)|A_sigma} chi_pq(A_sigma/(p^(2j)q^(2k))).

This is a same-physical-measure identity with no exceptional remainder or support enlargement. It does not assume any slice has small mass. For P=B^beta and beta>1/8, P^8>2B eventually. Thus it applies in the209 band beta=alpha=0.156632664928... . This band need not exhaust the small-prime detector; it is a chosen fixed band for a correlation certificate. Constants in209 and the full J_B detector remain untouched.

Highest layers expose an extra limitation: for p~B^alpha with alpha>1/7, A/p^6<2B/P^6=O(B^(1-6alpha))<p eventually. Its character period as a function of the unscaled A is p^7, exceeding the entire branch height. Full residue-period cancellation in this layer cannot simply be multiplied by interval volume. At alpha=0.156632664928..., the quotient exponent is0.060204010432... . The occupied physical quotient support is still uncounted. This is a scope statement, not proof that all incomplete methods fail.

## 4. Actual-population second moment and an explicit diagonal constraint

Let Q=|S|>=1. Put S_sigma(e)=sum_{p in S}lambda_p(A_sigma(e)), and
O=sum_{e in X,p in S,sigma}1_{v_p(A_sigma) odd}.

An endpoint has S_-=S_+=Q. Nonendpoint squares of these sums are nonnegative, so with E=#E(B;c_max>C),

E <= [sum_{e in X}(S_-²+S_+²)]/(2Q²)
   = N/Q - O/(2Q²) + (1/Q²)sum_{p<q in S}[H_-(p,q)+H_+(p,q)].   (210.3)

The diagonal equality uses lambda_p²=1 exactly when the valuation is even. This averaged two-branch second moment has diagonal N/Q, not N/Q²; it does not assert independent branch density or a tensor saving. The prime pool is fixed for all objects, including primes dividing R. On X, p|R already gives lambda_p(A±)=1 from M_2R; these values must remain in H. This is a necessary-condition count, so adding those primes to the fixed pool is legitimate without changing the exact J_B definition or its object-dependent exclusion.

Define the conventional absolute-correlation majorant
U_abs=N/Q-O/(2Q²)+(1/Q²)sum_{p<q}(|H_-|+|H_+|).
Then E<=U_abs. Each A<2B has at most log(2B)/log P distinct prime divisors from S; hence O<=2N log(2B)/log P and

U_abs >= (N/Q)[1-log(2B)/(Q log P)].                           (210.4)

Consequently, when Q tends to infinity and log P is a positive fixed fraction of log B, an absolute-moment certificate U_abs<=T requires N <= (1+o(1))QT. This is a necessary cost condition for this particular certificate, not an endpoint lower bound.

For the active T=B^(1/2+o(1))/C,C=B^gamma,gamma=1/6+xi,0<xi<1/12, and a pool contained in209's L_B=K_eta(2B)^alpha with alpha<1/6, Q<=L_B=O_eta(B^alpha). Thus this short-pool absolute-moment route needs

N <= B^(1/2-gamma+alpha+o(1)).                                (210.5)

Merely inserting an unsieved half-power upper N<=B^(1/2+o(1)), IF supplied by a correctly adapted theorem, would leave the weaker exponent1/2-alpha. This card does not claim that the current masked N saturates a half-power bound, nor establish such an upper from scratch. The gap gamma-alpha is positive; for eta=1/200 it is at least0.010034001738...+xi.

No new raw-count theorem satisfying(210.5) was found/proved in this batch. Possible ways beyond this scoped obstruction: prove this missing saving in N; use a longer prime pool with Q at least the content scale and pay the larger modulus/valuation costs; obtain signed correlations that genuinely cancel the diagonal; or prove a different higher joint moment/incidence estimate with all costs. Two-branch tensorization may alter the diagonal but introduces mixed moments and is not licensed by the two marginal sums above. The historical tensor completion barrier is not bypassed by naming more detectors.

## 5. Replay and limits

Input208 JSON DRIVE_ID=1uhhVhXKwiae-7sHeYw29pn7uVeCp_9iG; SHA256=3bce05e1ded1adabf70dd597de2e76ed8c0d4fdc96f604a2b5b7de239280adcd. It contains207's independently reproduced255 raw objects with R<=10^6. No larger census is asserted.

76630 single-prime layer checks include all255 records at13 primes plus a dense integer check1..10000 at7 primes.22950 two-prime ten-slice checks use primes11..43 and the exact finite condition11^8>2*10^6. Both PASS. Six M_2R survivors have unit nonresidues hidden by ordinary zero symbols, including the c_chart=R example in§2. No missing layer is assumed negligible.

At B=10^6 all three strict cutoffs3/16,5/24,11/48 select N=22. With S={3,5,7,11,13,17,19,23,29,31,37,41,43}, Q=13, the exact diagonal is568, odd incidences4, signed off-diagonal sum74 and total branch sum-square716. Formula(210.3) gives358/169 (so at most2 integer endpoints from this weaker finite certificate). Direct branch-square testing gives0. The moment certificate does not recover209's finite complete-detector zero; neither result is an asymptotic extrapolation.

SCRIPT_DRIVE_ID=1DCwDSJ8PI77oIbLbwL5wWZJMmzmLykVW (stage37_layers_210.py).
JSON_DRIVE_ID=1STghE27A5_Cwj4eGzAsSHohhb5wHX68h (M3-T11-210-verification.json).
Reproduce with208 input and210 script in one directory: python stage37_layers_210.py. Standard Python only.

## 6. Handoff

NEXT211: attack an actual H_sigma,j,k sum with the original sphere/two-face/primitive/canonical/height masks and summed content/family costs, especially the depth layers rather than silently discarding them; alternatively prove(210.5), enlarge the prime pool with an explicit budget, or count the exact209 J_B endpoint sum by a different theorem. Do not rederive the elementary moment, local density, four-layer decomposition, or the finite17 cutoff as new progress. Keep raw T_2R distinct from the endpoint sum and c_u/full-S distinct from c_max.205/206/171/174 sectors retained.

New substantive content is the exact valuation-aware integer adapter, ten-slice physical correlations and scoped short-prime diagonal budget. No asymptotic saving, no independent audit, no closure, global credit0/Gate OPEN. Readback PASS: card/code/JSON and source208 input downloaded from Drive and byte-compared. MAIN exact changes, INDEX14 fields/chip/link and209 restart, LEDGER unchanged history/control/append verified. Current latest210/NEXT211; new chat can resume from Drive only.
