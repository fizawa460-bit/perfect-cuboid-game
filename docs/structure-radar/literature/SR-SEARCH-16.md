# StructureRadar literature ledger — search batch 16

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-16-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-134,SR-STR-135,SR-STR-136,SR-STR-137,SR-STR-138,SR-STR-139,SR-STR-140,SR-STR-141,SR-STR-142,SR-STR-143
SEARCH_BATCH_SIZE=10
NOVELTY_BY_SEARCH_ABSENCE=false

## Primary-source literature checked
- Werner Hürlimann, *Exact and Asymptotic Evaluation of the Number of Distinct Primitive Cuboids*, Journal of Integer Sequences 18 (2015), Article 15.2.5. Theorem 7 / equation (10) gives the cumulative primitive cuboid count by inner diagonal: N3(x) ~ x^2/(32G) with the displayed lower-order linear term. This is a direct external match for the ambient space-diagonal baseline in SR-STR-142, after identifying the repo radius with the inner diagonal and preserving canonical/distinct normalization.
- Bonolis–Browning, *Uniform bounds for rational points on hyperelliptic fibrations* (arXiv:2007.14182): adjacent fiberwise-counting/square-sieve literature; it does not furnish the same MAIN physical wall measure or weighted high-occupancy tail required by SR-STR-135/138/140.
- Dimitrov–Gao–Habegger, *Uniform bound for the number of rational points on a pencil of curves* (arXiv:1904.07268): adjacent uniform fibre bounds in a fixed pencil, not a same-measure exceptional-mass theorem for the moving Stage27 wall host.
- Alpoge, *The average number of rational points on genus two curves is bounded* (arXiv:1804.05859): an average theorem for a different height-ordered genus-two family; its averaging measure is not the Stage27 MAIN physical measure.

## Search outcome for the new ambient baselines
- SR-STR-141: targeted search found classical primitive-Pythagorean cumulative counting as an input, but no published theorem was identified that directly states the repo exact-one-face B^2 log B law with its canonical primitive and exact-one exclusions. Retain the repo convolution/harmonic-scale proof as the exact receiver.
- SR-STR-142: Hürlimann Theorem 7 is a direct external carrier for the ambient primitive integral-space-diagonal B^2/(32G) main term. The repo zero-face-dominance complement estimate remains a separate repo theorem and is not attributed to Hürlimann.
- SR-STR-143: targeted search found computational/generative Euler-brick literature but no published theorem matching the repo exactly-two-face M2(B) ~ C_M2 B(log B)^5 law. Do not infer novelty from that search absence; retain the repo exact theorem as the receiver.

## SR-STR-134 — Fixed-moment exponent equivalence on the MAIN witness host
For a fixed positive moment, the MAIN witness sum is exponent-equivalent to occupied support unless a genuine moment deficit is proved; fixed-moment repackaging alone gives no saving.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.; Stage27-20 r302j-l: subpower divisor-fiber multiplicity does not imply a high-occupancy tail deficit. The missing theorem is a fixed-power correlation/exceptional-mass deficit in the same MAIN physical-host measure; no positive alpha,beta are proved.
Transfer verdict: `REPO_EXACT_MOMENT_FIREWALL` — fixed-moment reformulation is exponent-neutral unless an arithmetic moment deficit is proved in the same host.
Arsenal decision: `ACTIVE`.

## SR-STR-135 — Weighted exceptional-class adapter for the T route
A T-route averaged theorem is sufficient only in weighted form: good classes satisfy the target saving while exceptional classes carry power-saving total physical mass.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `SAME_MEASURE_WEIGHTED_GATE_RETAINED` — adjacent averaged/fibrewise theorems use different populations or weights and do not control the T-to-MAIN physical exceptional mass.
Arsenal decision: `ACTIVE`.

## SR-STR-136 — Balanced-wall common-core reconstruction barrier
On the fully balanced wall, common-core scale splitting and reduced-column reconstruction leave a multiplicity term; root-line information cannot be recharged after it already defines the host.
Potential weapon types: UPPER_BOUND_GATE, NEGATIVE_CERTIFICATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `RECONSTRUCTION_BARRIER_RETAINED` — no external theorem licenses recharging root-line information already used to define the balanced-wall host.
Arsenal decision: `ACTIVE`.

## SR-STR-137 — Fixed-U averaging collapses to a pointwise gate
For fixed U the admissible class universe is subpolynomial, so removing only a fixed-power fraction of exceptional classes gives no exponent saving; the surviving theorem must control weighted bad mass.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `POINTWISE_QUANTIFIER_GATE_RETAINED` — subpolynomial class cardinality means class-count averaging alone yields no fixed-power saving.
Arsenal decision: `ACTIVE`.

## SR-STR-138 — Outer-U weighted exceptional-mass receiver
Outer-U cardinality supplies no independent saving; closure requires either a power-saving bound for total bad physical mass or a weighted second moment in the same complete-host measure.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `SAME_MEASURE_L2_OR_BAD_MASS_GATE_RETAINED` — closure still requires a weighted second moment or total bad physical mass bound in the complete MAIN measure.
Arsenal decision: `ACTIVE`.

## SR-STR-139 — Same-measure physical occupancy L1/L2/exceptional-tail equivalence
On MAIN physical fibers, mu_x=H_x/H and rho_x=F_x/H_x in [0,1]. A fixed-power deficit in sum mu_x rho_x, sum mu_x rho_x^2, or the weighted tail mu{rho_x>B^-alpha} is equivalent up to constant exponent loss by Cauchy, rho^2<=rho, splitting, and Markov.
Potential weapon types: COUNTING_LEMMA, MEASURE_ADAPTER.
Applicability gaps: The equivalence creates no fixed-power saving by itself; an arithmetic occupancy or host-mass estimate is still required.; Stage27-20 r302j-l: subpower divisor-fiber multiplicity does not imply a high-occupancy tail deficit. The missing theorem is a fixed-power correlation/exceptional-mass deficit in the same MAIN physical-host measure; no positive alpha,beta are proved.
Transfer verdict: `ELEMENTARY_MEASURE_ADAPTER_CONFIRMED` — L1/L2/tail comparisons are elementary same-measure adapters and create no arithmetic saving by themselves.
Arsenal decision: `ACTIVE`.

## SR-STR-140 — Uniform high-occupancy physical-mass deficit gate on the MAIN wall slab
For fixed eta0, alpha,beta>0, with E_alpha={(P,U):F_MAIN(P,U;B)>B^-alpha H_phys^MAIN(P,U;B)}, the missing theorem is sum_{E_alpha} H_phys^MAIN << B^-beta+o(1) sum_{P,U} H_phys^MAIN. It would imply a strict wall power deficit; no such alpha,beta are proved.
Potential weapon types: EXTERNAL_GATE, UPPER_BOUND_GATE.
Applicability gaps: No fixed alpha,beta are proved; the estimate must use the same MAIN physical-host measure, and the already-charged row CRT product modulus cannot be reused as a new saving.; Stage27-20 r302j-l: subpower divisor-fiber multiplicity does not imply a high-occupancy tail deficit. The missing theorem is a fixed-power correlation/exceptional-mass deficit in the same MAIN physical-host measure; no positive alpha,beta are proved.
Transfer verdict: `EXTERNAL_GATE_UNDISCHARGED` — no checked source supplies fixed alpha,beta for the exact MAIN physical high-occupancy mass; prior CRT savings may not be double charged.
Arsenal decision: `ACTIVE`.

## SR-STR-141 — Exactly-one-face ambient population order and Pythagorean scale mechanism
For primitive canonical R<=B cuboids with exactly one integral face and no space condition, M1(B) asymp B^2 log B and M1(B)/U(B) asymp log(B)/B. The power drop comes from replacing one free edge-pair by scaled primitive Pythagorean faces; the logarithm comes from the harmonic face-scale sum.
Potential weapon types: ASYMPTOTIC, POPULATION_BASELINE, CAUSAL_DECOMPOSITION.
Applicability gaps: This baseline card records the B^2 log B order and Pythagorean-scale mechanism; the leading constant, directional constants, pair-overlap lower-order theorem, and exact-one limit law are normalized separately in SR-STR-228.; Integral space diagonal is not imposed and must not be charged through this ambient baseline.
Transfer verdict: `REPO_EXACT_AMBIENT_BASELINE_RETAINED` — classical Pythagorean counting is only an input; no direct published match to the full exact-one-face B^2 log B theorem was identified.
Arsenal decision: `ACTIVE`.

## SR-STR-142 — Ambient integral-space-diagonal cuboid asymptotic and zero-face dominance
For primitive canonical R<=B cuboids with integral space diagonal and no face restriction, N_S^all(B)~B^2/(32G). The zero-integral-face subpopulation N_S^0(B) has the same main term, while the faceful complement is O_epsilon(B^(1+epsilon)); hence the intrinsic ambient space-diagonal cost relative to U(B) is one power of B.
Potential weapon types: ASYMPTOTIC, POPULATION_BASELINE, UPPER_BOUND.
Applicability gaps: The faceful-complement O_epsilon(B^(1+epsilon)) bound is not asserted sharp; interaction with face conditions belongs to transition stages.
Transfer verdict: `DIRECT_EXTERNAL_AMBIENT_CARRIER` — Hürlimann Theorem 7 matches the primitive ambient integral-space-diagonal quadratic main term; repo zero-face dominance remains separate.
Arsenal decision: `ACTIVE`.

## SR-STR-143 — Exactly-two-face ambient asymptotic and cubic-host thinning law
For primitive canonical R<=B cuboids with exactly two integral face diagonals and no space-diagonal condition, M2(B)~C_M2 B(log B)^5 with C_M2>0; against U(B)=pi B^3/(36 zeta(3))+O(B^2), M2/U~[36 zeta(3) C_M2/pi](log B)^5/B^2.
Potential weapon types: ASYMPTOTIC, POPULATION_BASELINE.
Applicability gaps: The law does not impose an integral space diagonal and does not by itself isolate the incremental second-face or third-face cost.
Transfer verdict: `REPO_EXACT_AMBIENT_BASELINE_RETAINED` — no direct published match to the exactly-two-face B(log B)^5 asymptotic was identified in the targeted search.
Arsenal decision: `ACTIVE`.

## Firewalls
- Search absence is not a novelty claim.
- Hürlimann is promoted only for the ambient primitive integral-space-diagonal count in SR-STR-142; it does not prove the repo zero-face complement bound or any face-conditioned transition theorem.
- SR-STR-141 and SR-STR-143 remain repo-exact asymptotic baselines unless an exact external theorem with matching primitive/canonical/exact-face population is located.
- SR-STR-134..140 retain the same-measure physical-host quantifier firewall; generic averages in other families cannot discharge the fixed-power wall deficit.
- CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT remains 1/2; no strict sub-square-root whole-family theorem is claimed.
- No perfect-cuboid existence or nonexistence claim is made.
