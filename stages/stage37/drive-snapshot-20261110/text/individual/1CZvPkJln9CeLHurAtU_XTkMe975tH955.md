# M3-T11-206 — Summed primitive-space gap sector and original signed-gap trace

STATUS: PROVED_ALL_CONTENT_SPACE_GAP_SECTOR / PROVED_FIXED_SPACE_GAP_FIBER / EXACT_ORIGINAL_SIGNED_GAP_TRACE / LARGE_GAP_SUPPORT_OPEN.
PRIMARY_GATE=OPEN. GLOBAL_COUNTING_CREDIT=0. Independent hostile audit NOT RUN. Separate-chat audit162–185 scope unchanged;186–206 not independently audited. TI parked;120 retracted;147–149 frozen. Date2026-10-03 JST.

## 1. Startup, decision, and scope

Current Drive MAIN, short RESULT-LEDGER, operational CARD-INDEX through205, latest205, retained174/175,162 and active ROUTE primitive space/content interface were checked. No historical full reread.205 removes small reduced edge u_i but leaves moving large-u support OPEN. Merely summing its fixed-U fibers does not pay that support.206 instead identifies a counted subfamily WITHIN the large-u residual: near-balanced primitive SPACE triangles.

On the original positive primitive canonical endpoint population E(B), R<=B, define positive opposite face F_i=|f_i| and retain the ORIGINAL sign epsilon_i=f_i/F_i. Put

h_i=gcd(R,e_i), u_i=e_i/h_i, v_i=F_i/h_i, D_i=R/h_i,
u_i²+v_i²=D_i², gcd(u_i,v_i)=1,
delta_i=|u_i-v_i|=|e_i-F_i|/h_i.                         (206.1)

Delta_i is a positive odd integer. Equality u_i=v_i would force sqrt(2)u_i=D_i and is impossible. The delta notation here does not denote190's Kummer squareclass,162's primitive physical-face gap,188's product-phase gap, or205's reduced edge u_i.

Uniformly at 1<=Z<=B,

#E(B; min_i delta_i<=Z) <= Z B^{o(1)}.                    (206.2)

For fixed epsilon_delta>0, Z=B^{1/3-epsilon_delta} is scoped o(M3(B)) at the retained lower scale M3(B)>>B^{1/3}. In particular(206.2) also bounds this set restricted to205's all-u-large residual. No global endpoint bound follows for the complement.

## 2. Fully summed direction cost via the retained Pell argument

For one labeled primitive space triangle write x=u+v and delta=|u-v|. Then

x²-2D²=-delta²,
u,v=(x±delta)/2, x>delta, D<=B.                          (206.3)

This is precisely162 Section2's ARITHMETIC direction problem, applied to the two legs of a space triangle. Its physical transfer must be changed; that is done in Section3 below.

For completeness, work in O=Z[sqrt(2)], alpha=x+D sqrt(2), Norm(alpha)=-delta². The norm-Euclidean argument rounds both quotient coefficients, giving absolute error norm<=1/2. Thus O is a PID. Primitive opposite-parity legs imply delta odd and gcd(x,D)=1. At a prime dividing delta, an inert prime would divide x,D, impossible. A split prime can occur on only one conjugate side; both would again force a common prime in x,D. For p^e||delta, the chosen side has exponent2e. Thus at most2^omega(delta) ideals(alpha) are possible.

Positive same-norm generators of one ideal differ by positive norm-one units. The least such unit above1 is3+2sqrt(2): the equation a²-2b²=1 has no positive b=1 and its first positive solution is(a,b)=(3,2). Division into the interval[1,3+2sqrt(2)) proves that all positive norm-one units are its powers. Since delta<alpha<3B, each ideal contributes O(1+log(B/delta)) generators.

Both leg orders cost two. Consequently the number of labeled primitive space triangles with D<=B and delta<=Z is

<=2 sum_(odd delta<=Z) 2^omega(delta)
   [1+floor(log(3B/delta)/log(3+2sqrt(2)))]
<< Z(1+log Z)(1+log B).                                  (206.4)

The bound sums ALL moving gap labels and Pell orbits. The divisor identity2^omega(n)=sum_(k|n)mu(k)^2 gives the last estimate. No field, class number, content, or unspecified fixed-gap constant moves outside the budget.

For a fixed delta=N, the same argument gives B^{o(1)} triangle packets uniformly in N<=B. This is not an assertion that a fixed gap fixes ONE triangle: delta1 has infinitely many primitive triangles of increasing D.

## 3. Physical transfer: use174, not162's face-ratio chart

Each packet in(206.4) fixes a labeled primitive SPACE triangle(u,v,D).174 Sections2–3 supply a uniform B^{o(1)} endpoint fiber for this packet. The elliptic receiver fixes the entire normalized edge vector, and primitivity fixes R uniquely as the lcm of the reduced edge-coordinate denominators. Therefore h_i=R/D and all other contents are reconstructed. No outer h_i or content-triple sum is charged.

Apply174 once per packet, sum(206.4), and take the finite union over the three directions. This proves(206.2). Similarly

#E(B; a specified delta_i=N) <= B^{o(1)}                   (206.5)

uniformly in N<=B. The uniformity uses the retained elliptic point input exactly as174/205; no stronger external theorem is introduced.

162's physical transfer uses a ratio of two physical face edges and a first-cover parent. That transfer is NOT reused here: a space triangle pairs one EDGE with its OPPOSITE FACE DIAGONAL.174 is the correct all-content receiver for these packets.188 instead pairs two primitive PRODUCT-PHASE legs and uses183's phase fiber. These are different coordinates and reconstruction maps.

## 4. New exact original trace in physical gaps

Let k_i=h_i delta_i=|e_i-F_i| be the positive PHYSICAL gap, and set

G_gap=sum_i epsilon_i k_i².

Since e_i²+F_i²=R²,

2 epsilon_i e_i F_i=epsilon_i(R²-k_i²).

Using the original signed f_i and N_T=sum_i e_i f_i gives

2N_T=R² sum_i epsilon_i-G_gap,
S=2N_T/R²=sum_i epsilon_i-G_gap/R².                       (206.6)

This formula preserves the original sign routing. Setting every epsilon_i=+1 without authority would change the receiver.

R is odd on physical endpoints. Therefore

Den(S)=R²/gcd(R²,|G_gap|),
gcd(R²,|G_gap|)=gcd(R²,|N_T|).                            (206.7)

Retained186 has Den(S)=D_S², q_phase=R/D_S. Hence on THAT retained physical population,

gcd(R²,|G_gap|)=q_phase².                                 (206.8)

Equation(206.8) is not valid on arbitrary triples of integer circles: its perfect-square gcd conclusion uses the physical186 theorem. The elementary trace and gcd equality(206.6–7) do hold for three same-R integer circles, regardless of sphere compatibility.

Each individual primitive space gap also has an exact content lock:

gcd(R,|e_i-F_i|)=gcd(R,e_i+F_i)=h_i.                      (206.9)

Indeed gcd(D_i,u_i±v_i)=1: an odd prime dividing D_i and u_i±v_i would force2u_i²=0 modulo that prime, contradicting primitive legs; D_i is odd. Multiplying by h_i proves(206.9), even when h_i and D_i share primes.

If H=h_1h_2h_3,203 and(206.7) give

gcd(H,|G_gap|)=gcd(H,|N_T|)=H_Q,
H_Q unitary in H.                                        (206.10)

Thus the phase/full-S partition of physical content can be expressed as the gcd of ONE original signed quadratic gap norm. The individual gap gcds do not determine the signed SUM gcd.

## 5. Median visible/hidden cancellation receiver

Take h_i=b as the sorted median content, p^alpha||b and beta=v_p(tau), lambda=alpha+beta.203's table, after(206.6), gives

visible(A): v_p(G_gap)>=2lambda;
visible(B): v_p(G_gap)=2alpha;
hidden(C):  v_p(G_gap)=0.                                (206.11)

Rows(A)/(B) coalesce when beta0. Since p^(2alpha)|k_i², visible rows require

epsilon_j k_j²+epsilon_k k_k²=0 mod p^(2alpha),             (206.12)

while hidden row(C) requires this same complementary sum to be a p-unit. The other contents are p-units, but their gaps can depend on every physical coordinate. This is203's original trace cancellation restated in the newly COUNTED space-gap coordinate; it is not a fresh independent congruence or a density saving. In particular(206.12) must not be multiplied by203's visible q-tail or206's gap-sector bound.

The full valuation statement in(A) concerns G_gap INCLUDING the median term. Dropping that term is justified only modulo p^(2alpha), not modulo p^(2lambda) when beta>0.

## 6. Contribution, overlap, and residual

205 disposes of small u_i.206 disposes of small |u_i-v_i|, even when u_i and D_i are large. Arithmetic directions delta1=(3,4,5),(20,21,29),(119,120,169),... show that this gap sector is not just a smaller space-hypotenuse or reduced-edge cutoff. These are triangle directions, NOT physical endpoint examples. No nonempty endpoint difference between sectors is asserted.

Disjoint bookkeeping can first charge205's small-u set, then206's small-gap set restricted to u_min>Z_u. Its contribution is still bounded by(206.2). Retain162/188's different gap sectors and other W/Sigma/Phi sectors by union; multiply no savings.

The remainder satisfies simultaneously

all u_i>Z_u, all delta_i>Z_delta,
the existing large Sigma/large D_min and original masks,
G_gap=sum epsilon_i h_i²delta_i²,
gcd(R²,G_gap)=q_phase² and gcd(H,G_gap)=H_Q.               (206.13)

For median b<=K, the physical gap k_i exceeds b Z_delta. This is an absolute content-normalized exclusion, not a claimed relative angular width independent of b/R.

Neither the Pell packet budget nor the signed trace formula proves sparsity of ALL large-U/large-gap occupied support. The total gap sum to B is still too expensive. Positive/negative sign cancellations in G_gap must be counted on the same endpoint, not estimated by independent square probabilities. There is no fixed-q_min subpower theorem, global endpoint bound or closure gain here.

## 7. NEXT207 and audit status

206 provides a genuinely summed geometric subfamily and its exact original full-S bridge. Do not continue enumerating fixed-gap Pell packets: their entire cost is already paid. NEXT207 should return to the DISTINCT large-c threshold tail, with(206.13) available as the original integer receiver. The retained ROUTE166–168 startup summaries ground this branch as c_max=max_i c_i=max_(j<k)h_jh_k>C=B^(1/6+xi),0<xi<1/12. This is the CONTENT cross-gcd statistic, not common-phase c_u.156/175 rule out the uncapped uniform raw moment shortcut but do not refute this particular threshold tail. A productive result must prove a threshold-specific same-measure raw tail that transfers to endpoints, or an endpoint-only tail with all sphere/face masks. Full-S joint occupancy remains a distinct open alternative; do not silently merge its measure with the c_max tail.

If a proposed gap-norm argument only rewrites203/186 or multiplies separate triangle counts, record that limitation and keep the gate OPEN. Do not reopen134 fresh-C_u,201/202 normalization-scale coupling, or K1-only177–181 as a supposed general K>1 bound.

Verification script verify_m3_t11_206.py: PASS. At D<=50000 and gap<=200, complete Pell/Euclid enumeration agrees on193 unordered primitive directions,51 reduced seeds across100 odd gap labels.7960 primitive triangles support31840 scaled gap/content gcd checks.1200 signed same-R circle triples satisfy the original trace/gcd identities. The circle triples need not satisfy the sphere or original masks; no perfect-square trace gcd is inferred there. Physical endpoints checked=0. Finite checks verify arithmetic adapters only; the counting proof is Sections2–3 using162/174.

Within-session deductive review PASS; independent hostile audit NOT RUN. New research authority206/NEXT207, but primary Gate OPEN/global credit0 and existing audit scope unchanged. No retraction. CARD-INDEX, short LEDGER and MAIN must point here; do not append the proof to the historical ROUTE or archived LEDGER.

Drive artifacts: SCRIPT=1Gl_L-EbvOBFMV8uDxAIAzCI0A2SKcQRr; JSON=1Vxvc0tCvRQAE4eCmaFb-XIDvAvxCDqhV. Both are stored in Stage37 research auxiliaries. Card body remains the proof authority.
