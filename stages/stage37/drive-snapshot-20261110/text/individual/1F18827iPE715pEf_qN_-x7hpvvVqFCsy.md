# M3-T11-219 — Original signed-trace square-gcd allocation of fresh-S and the extracted cofactor squareclass

STATUS: PROVED_ORIGINAL_TRACE_FRESH_S_SQUARE_GCD_ROUTER / PROVED_EXTRACTED_COFACTOR_PRODUCT. Fresh/mixed occupancy OPEN; Gate OPEN; global counting credit0. No retraction. Independent audit186–219 NOT RUN;162–185 scope unchanged. TI parked;120 retracted;147–149 frozen.

## 1. Authority, population and notation

Fresh Drive MAIN, operational INDEX and short LEDGER are latest218/NEXT219. Read218,203,134,171,174 and the active CROSS-GCD control; old route NEXT headers are historical. The latest218 hidden-content height tail is retained. Work on the same primitive positive physical endpoints, finite nonzero corrected u, intrinsic R<=B, every content/orientation/cyclic/four-square mask. No perfect endpoint is enumerated in this batch.

Use the ORIGINAL signed complementary face diagonals f_i, f_i²=R²-e_i², with the signs belonging to the actual retained phase. Define

    N=N_T=sum_i e_i f_i,
    A_i=N-2e_i f_i,
    S=2N/R², v_i=2A_i/R².

Thus sum_i A_i=N. Auxiliary independent changes of the f_i signs are not permitted when labeling an original phase. R is odd, and h_i=gcd(R,e_i), H=h1h2h3. Retain216–218:

    H=H_Q H_S, tau=tau_Q tau_B tau_C tau_F,
    q=q_phase=H_Q tau_Q, R=q H_S tau_B tau_C tau_F,
    c=c_u=tau_B tau_C tau_F H_Q² tau_Q³,
    gcd(R²,|N|)=q².

tau_F is fresh-S outside H, not all fresh primes and not tau_Q. Its primes divide all three primitive space denominators, have unit e_i,f_i,N, and v_p(R)=v_p(tau_F)=beta.134 gives relative D-only occupancy on this support.203's hidden-content row(C) is not included in tau_F. n=N/q² is an integer, possibly negative. Finite nonzero u and S!=0 imply N and all A_i are nonzero via the retained conic identity below.

Drive dependencies:218 markdown1RIE32-7wipGoTPj3zYlkrb4SbI-zTFT-;203 native1VW2ya-fuknvwzGls_7q5tx7BUZpd02el83m3PIINWH4;134 markdown1Uxm_NWVBDZJj4dGZNSZkI8nMP2XFoJzs;171 native1cIVglf5RjsFKYBdzy5suR1JSTpKs35bp-8Ga5Pb4-u4;174 native1_ic-h_X9wS8EZwpNflXzGZEDPEKg2qCAgHveaOwLyeE.134 retains the corrected031 conic and original half-angle adapter;216–218 contracts are explicitly reproduced above.

## 2. Direct physical proof of exact fresh prime allocation

Let p^beta||tau_F. Then p is odd, p does not divide H, all e_i are p-units, and f_i²=-e_i² mod p. Consequently -1 is a square mod p. Choose a root r of -1 modulo p^(4beta); each original f_i has a unique sign s_i in {+1,-1} relative to r e_i modulo p. Hensel uniqueness and the binomial identity give

    f_i = s_i r (e_i-R²/(2e_i)) mod p^(4beta).

These are identities in the local ring; all displayed inverses are units. Use sum e_i²=R², not a generic root-line density. If all three signs equal t, then

    N = -t r R²/2 mod p^(4beta).

This has exact N-depth2beta and cannot belong to fresh-S, where N is a unit. Thus exactly one sign is different. Let i be the unique odd-sign index, with s_i=t and s_j=s_k=-t. Then

    N = t r (2e_i²-R²/2) mod p^(4beta),
    A_i = t r R²/2 mod p^(4beta),
    A_j = -2t r e_k² mod p, A_k=-2t r e_j² mod p.

Therefore exactly v_p(A_i)=2beta and v_p(A_j)=v_p(A_k)=0. In particular v_i=2A_i/R² has the prescribed root line v_i=t r mod p^(2beta). The familiar anti-root root line is thereby recovered directly from the ORIGINAL sphere and signed physical faces. It supplies no independent extra density.

## 3. Canonical integer square-gcd receiver

Group the full p^beta blocks of tau_F by the unique index just proved, obtaining pairwise coprime m_1,m_2,m_3 with tau_F=m1m2m3. The grouping requires no separately assigned Gaussian orientation once the original integer endpoint and its signed trace are fixed. Exactly

    gcd(tau_F²,|A_i|)=m_i², i=1,2,3.

The three gcds are perfect squares, pairwise coprime, and their product is tau_F². Define signed nonzero integer cofactors

    K_i=A_i/m_i².

Then every K_i is a unit at EVERY tau_F prime:

    gcd(|K1 K2 K3 N|,tau_F)=1,
    m1² K1+m2² K2+m3² K3=N=q² n.

The untruncated gcd with R² may include content or q-side powers; it must not replace the gcd with tau_F². This receiver is valid with all contents moving, including the mixed tau_C/tau_F cells outside218's closing window. It does not lift tau_F*rad(tau_F) into R.

## 4. Exact cofactor product and squareclass cancellation

Let the actual reduced physical product phase be (a+i b)/c, a²+b²=c², with u=±b/a as in184/133. Here b is the original imaginary phase leg, not an independent conic variable; the finite nonzero-u condition makes a,b nonzero. The retained corrected031 conic says P/S=4u²/(1+u²), P=v1v2v3. Substituting v_i=2A_i/R² proves the inherited physical identity

    A1 A2 A3 = N R⁴ b²/c².

Extracting EXACTLY the fresh square gcds and using216's conservation gives the new integral normal form

    K1 K2 K3 = n * (H_Q H_S² tau_B tau_C b)².       (219.1)

Indeed R²/(c tau_F)=H_S² tau_B tau_C/tau_Q and N=q²n; the apparent tau_Q denominator cancels. All fresh tau_F factors disappear from the explicit square multiplier. Thus the signed squareclass of the cofactor product is that of the reduced original trace n. This holds on the same endpoint, rather than by imposing three unrelated square tests. b and n still move and depend on that endpoint.

Equation(219.1), the weighted sum and the square-gcd constraints together are necessary physical incidence conditions. They are not sufficient to reconstruct an endpoint: retain original f_i²=R²-e_i², primitive space triangles, positive/canonical masks, the full four-square lift and intrinsic R. In particular189's independent projected-phase countermodels are not admitted merely because an invented phase satisfies a product relation.

Novelty is the explicit all-content original-integer square-gcd extraction and its cofactor normal form relative to the retrieved portfolio. The local anti-root/conic identities themselves are inherited, not a second new constraint or a literature-wide novelty claim. Targeted INDEX searches for N_T and fresh receivers found203 content-gcd,206 gap trace,134 denominator/root-line and177–181 K1 conductor receivers; none states this extracted all-content cofactor system. No external theorem is needed for the elementary proof.

## 5. Limits and next research

No occupied-support deficit or fresh tail bound follows from the gcd/product identities alone. For fixed tau_F, its three labels have divisor-many allocations, but summing moving tau_F retains the unresolved outer cost. A general residue selector or pairwise density multiplication would recycle134/029's already retained root lines. There is no claimed extra factor tau_F^(-2), no generic powerful-label census, and no new primary sector disposal.

The new receiver makes the next gate concrete: count ORIGINAL physical incidence in the simultaneous weighted-sum / cofactor-squareclass system, or prove a correlation with171's Sigma,174's D_min and the four-square height masks that actually changes its moving-label budget. Both the trace n and original phase leg b must be charged. A fixed-fiber relabeling or root-line CRT on one anti-root is insufficient; the three A_i remain distinct.

NEXT220: investigate the occupied (n,b,K_i,m_i) support of this exact receiver on the residual after217/218's closing sectors. Seek a genuine all-content count or an explicit full-physical obstruction to a proposed relaxation; do not promote necessary-only integer records to endpoints. If the squareclass alone is unhelpful, establish that with a scoped countermodel and preserve the unrelaxed original equations. K1 conductor177–181 remains stopped;215 moving-squareclass dilation, large-W/unshared-conductor, large-c threshold andK>1 low-median gates remain separately OPEN.

## 6. Verification and durability

stage37_freshtrace_219.py checks992 modular sphere/three signed-face states at p=5,13,17,29,41 and beta=1,2:744 relative allocations verify exact2beta depth, other two units and sum A=N;248 all-same controls verify N-depth2beta and exclusion from fresh-S.256 exact rational ratio checks verify the cancellation in219.1. All PASS. These modular states are local sphere/face roots, not positive global perfect endpoints. The finite checks do not prove occupancy sparsity or constitute an independent audit.

The proofs above use no empirical extrapolation. Preserve audit162–185 without extending it. MAIN/INDEX/short LEDGER must become latest219/NEXT220; the new card and reproduction script/JSON stay in Stage37, with byte readback and synchronization recorded in LEDGER/INDEX. Do not append proofs to archived MAIN/LEDGER or the active route.

Drive reproduction artifacts: SCRIPT_FILE_ID=1HUUi34p4Yx7OLz4pty6CeSsxHWKQl4fD; JSON_FILE_ID=11Kw7dTuOWvK_3WqVnT8Xh4WMxnaBmDZg. Standard Python is sufficient. The final readback receipt belongs to the short LEDGER and INDEX row448.
