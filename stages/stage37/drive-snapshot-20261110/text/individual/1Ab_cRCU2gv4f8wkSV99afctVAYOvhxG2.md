# M3-T11-220 — Physical trace-slack geometry, cofactor height budgets and imaginary-phase imbalance transfer

STATUS: PROVED_TRACE_SLACK_EDGE_COMPARISON / PROVED_ORIGINAL_IMAGINARY_PHASE_LOWER_BOUND / SCOPED_COFACTOR_AND_PHASE_SECTOR_TRANSFERS. Full fresh/mixed occupancy OPEN; Gate OPEN; global counting credit0. No retraction. Independent audit186–220 NOT RUN;162–185 scope unchanged. TI parked;120 retracted;147–149 frozen.

## 1. Current authority and question

Fresh Drive MAIN/operational INDEX/short LEDGER are latest219/NEXT220. Read219 and204, targeted active CROSS-GCD control, and INDEX Heron search. Count the actual primitive positive endpoints R<=B with all original content/orientation/cyclic/four-square masks. Retain219's finite nonzero-u original phase and fresh-S extraction. No new perfect endpoint is enumerated.

219 leaves moving reduced trace n=N/q_phase², original imaginary phase leg b_phi and fresh cofactors K_i=A_i/m_i², where A_i=N-2e_i f_i and N=sum e_i f_i. The question is whether a small cofactor/phase leg gives a new fresh-support saving. The result below supplies a physical height-sensitive count and identifies its existing small-edge cost. It does not assume fixed n or fixed K has a subpolynomial fiber.

Only new elementary geometry and204's retained all-content count are used:

    #E(e_min<=Z)<=Z B^o, e_min=min_i e_i.

Drive dependencies:219 markdown1F18827iPE715pEf_qN_-x7hpvvVqFCsy;204 native1CRFsg30j329j-hCpyViIhPWCdUBXmEUtFvPQ9bdV1lU.219 reproduces216's physical router and original phase identity;204's bound includes all moving contents.171/174 residual filters and217/218 paid tails remain retained, with no independent multiplication. The active route's old173 NEXT is historical; MAIN is current.

## 2. Trace magnitudes form one strict triangle

First use positive magnitudes F_i=|f_i|=sqrt(R²-e_i²) and X_i=e_i F_i. Sort the EDGES as a<=d<=g, a=e_min; use x_a,x_d,x_g for the corresponding X values. This a is not the phase real numerator. The identity

    x_g²-x_d²=a²(g²-d²)

and its cyclic versions prove x_a<=x_d<=x_g. Define P=x_a+x_d+x_g and the three slacks ell_i=P-2x_i. The smallest is

    ell=x_a+x_d-x_g.

Since x_g+x_d>=2dg,

    x_g-x_d=a²(g²-d²)/(x_g+x_d)
             <=a² g/(2d)<=a g/2<=x_a/2.

Thus ell>=x_a/2>0: these three X are sides of a strict triangle for EVERY positive real edge triple, independent of rationality. Also a²<=d²<= (d²+g²)/2 yields

    x_a=a sqrt(d²+g²)>=sqrt(2/3)*a R.

Consequently

    a R/sqrt(6) <= ell <= a R.                  (220.1)

For every original sign choice f_i=epsilon_i F_i, the multiset

    {|N|,|A1|,|A2|,|A3|}

is exactly {P,ell_1,ell_2,ell_3}. This follows by listing the four linear forms in epsilon_i X_i: a global sign changes nothing, and changing one sign permutes the perimeter and three slacks in absolute value. This is a geometric identity valid for the original signed phase; it does not authorize independent sign assignments in an occupancy sum.

Let Lambda=min(|N|,|A1|,|A2|,|A3|). Then Lambda=ell and

    R e_min/sqrt(6)<=Lambda<=R e_min,
    |N|,|A_i|>=R e_min/sqrt(6),
    |N|,|A_i|<=P<=sqrt(2) R².                  (220.2)

The last inequality is Cauchy-Schwarz, sum F_i²=2R². None of the four trace factors can vanish on a positive endpoint. On all-positive face signs, N=P and all A_i>0. With one opposite face sign, N has the majority sign, the odd-index A has that sign and the other two A have the opposite sign. Cofactor signs therefore cannot be chosen independently.

## 3. Exact height budget for219's cofactors

Use219's A_i=m_i²K_i and N=q²n, q=q_phase. On the actual endpoint,

    |K_i| >= R e_min/(sqrt(6) m_i²),
    |n| >= R e_min/(sqrt(6) q²).                (220.3)

After204's small-edge sector e_min<=E has been paid, every remaining endpoint therefore satisfies all these inequalities with e_min>E. On a shell R>=R0, a proposed short-K cell m_i<=M, |K_i|<=K forces e_min<=sqrt(6)M²K/R0. Applying204 once gives

    #E(R>=R0, exists i: m_i<=M, |K_i|<=K)
       <= min(B,M²K/R0) B^o.                  (220.4)

Constants and the three direction choices are absorbed. If sqrt(6)M²K/R0<1, the set is empty. Thresholds are positive and polynomially bounded; R0<=B. Similarly

    #E(R>=R0,q_phase<=Q,|n|<=T)
       <= min(B,Q²T/R0) B^o.                  (220.5)

The q here is NOT174's q_min. These are all-content physical endpoint counts with no outer H or content sum. They do not assign new fixed-K or fixed-n fibers. Do not multiply them with183 fixed-c,216 q-side,217 row(B),218 hidden-content tails or204's small-edge bound:204 is the sole counted input.

For R0=B^r,M=B^m,K=B^k the cofactor cell is negligible at the retained B^(1/3) scale when 2m+k-r<=1/3-eta for fixed eta>0. The trace cell closes when 2d+t-r<=1/3-eta, Q=B^d,T=B^t. These are real sufficient windows, not a proof the residual lies in them. A large m_i can make K_i small without making the physical edge small; unweighted short-K claims omit its square-weight cost.

## 4. Original imaginary phase leg has a linear edge-ratio lower bound

Write the ORIGINAL unnormalized product phase as

    product_i(e_i+i f_i)=U+iY,
    Y=e1e2 f3+e1e3 f2+e2e3 f1-f1f2f3.

The reduced phase is (a_phi+i b_phi)/c, so |b_phi|/c=|Y|/R³.219's inherited original identity is

    R² A1 A2 A3=N Y².

Multiply by N and use the trace-magnitude permutation:

    N²Y²=R² P ell_1 ell_2 ell_3.

Since |N|<=P, this yields Y²>=R² ell_1 ell_2 ell_3/P. In increasing slack order, the smallest is at least x_a/2, the middle x_a+x_g-x_d is at least x_a, and the largest x_d+x_g-x_a is at least x_g while P<=3x_g. Therefore

    Y² >= R²*x_a²/6 >= a²R⁴/9,
    |b_phi|/c >= e_min/(3R).                   (220.6)

This is stronger than using only a product of three generic lower slack bounds, which would give a weaker (e_min/R)^(3/2) estimate. It uses the actual signed Y, not a free conic leg or three independent squareclasses.

For 0<theta<=1, endpoints with |b_phi|/c<=theta satisfy e_min<=3theta R<=3theta B. Thus

    #E(|b_phi|/c<=theta)<=theta B B^o,          (220.7)
    #E(|b_phi|<=V,c>=C)<=B min(1,V/C) B^o.    (220.8)

The set in220.7 is empty when 3theta B<1. Constants are absorbed; V,C>=1 are polynomial thresholds. The ratio sector closes if theta<=B^(-2/3-eta), or C/V>=B^(2/3+eta). A bare short primitive leg is a different condition:187 already counts it by V B^o; for C<B,220.8 can be weaker, so retain the minimum of valid bounds on their actual intersection rather than adding fictitious credit.

On204's e_min>E residual, the original imaginary leg must satisfy

    |b_phi|>c E/(3R)>=c E/(3B).                (220.9)

Hence BOTH moving labels n and b_phi in219 are constrained by physical edge size, with explicit q² and c/R budgets. No global fresh tail is established.

## 5. Novelty, exclusions and handoff

INDEX Heron search found139–142's PLUS-vector Heron factors, content allocation and bare-cover impostors. Those factors use a different plus-vector variable and do not establish220.1/220.6 for original X_i=e_i|f_i|. Their full signed-lift and no-density firewalls remain valid. This card supplies an original trace/edge comparison, a sharper imaginary-phase lower bound, and counted cofactor/ratio cells through204; it does not rediscover139's polynomial cover or141's four-factor allocation.

These short-factor sectors are paid subsets of204's small-edge sector, so they supply no additional global disposal after small edges have already been removed. The useful change to219's proposed strategy is a quantitative budget: if a short-cofactor or short-imaginary-leg cell survives large edges, its modulus/phase denominator must be correspondingly large. Fixed labels or generic squareclass densities alone cannot bypass that cost. No general impossibility of a future correlation theorem is asserted.

NEXT221: work on219's weighted sum/cofactor-product receiver only on the explicit large-edge region220.3/220.9, with original sphere/faces/four-square/intrinsic R and171/174 conditions. Seek a count tying the required large m_i or large c to the ORIGINAL moving n,b_phi and cofactor squareclasses, or demonstrate a precise obstruction for a proposed enlarged receiver. Do not repeat small-K/short-b transfers as fresh savings, generic sign counting, or existing fixed fibers. K1 conductor177–181 remains stopped; large-c, K>1 low-median,215 moving-squareclass,large-W/unshared conductor gates are separately OPEN.

## 6. Verification and durability

stage37_trace_geometry_220.py replays1140 positive real sphere edge triples with entries1..18 and9120 signed states at80-digit precision. It checks magnitude permutation, strict slack and edge inequalities, the original Y identity and the linear imaginary-phase lower bound. All PASS. Faces are generally irrational; these are geometric numerical checks, NOT perfect endpoints or an occupancy census. Universal proofs are the inequalities above; the counted input is retained204. No external theorem or independent hostile audit is claimed.

Persist this card and reproduction script/JSON in Stage37. MAIN/INDEX/short LEDGER should be latest220/NEXT221; byte-readback and control synchronization must be recorded there. Proof occurs here once; archived MAIN/LEDGER and active ROUTE are not rewritten. Gate OPEN/global credit0.

Drive reproduction artifacts: SCRIPT_FILE_ID=11pLWX0BkZBrTaW78tEQJUxpPN2QTCwUb; JSON_FILE_ID=1sM-MZzn_4mmvTrAl21NnTEBXRRSF_yKW. Python standard library is sufficient. Final byte-readback receipt belongs to the short LEDGER and INDEX row449.
