# StructureRadar literature ledger — search batch 14

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-14-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-114,SR-STR-115,SR-STR-116,SR-STR-117,SR-STR-118,SR-STR-119,SR-STR-120,SR-STR-121,SR-STR-122,SR-STR-123
SEARCH_BATCH_SIZE=10
NOVELTY_BY_SEARCH_ABSENCE=false

## Primary-source literature checked
- Tom Fisher, *Higher descents on an elliptic curve with a rational 2-torsion point* (arXiv:1509.03234): explicit higher-descent machinery for rational 2-torsion, including full rational 2-torsion; supports descent architecture, not the Stage19 physical support exponent by itself.
- Francesco Naccarato, *Counting rational points on elliptic curves with a rational 2-torsion point* (arXiv:2105.04032): bounded-height point counts over Q under rational 2-torsion; applicable only after matching the precise target height and fixed-field/torsion hypotheses.
- Marta Dujella, *Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves* (arXiv:2312.03655): uniform subpower bounded-height count over a fixed number field when a rational point of exact prime order is present; full rational 2-torsion would satisfy the torsion condition on each exact target model, but height transfer and family normalization still must be charged explicitly.
- Fisher–Sills, *Local solubility and height bounds for coverings of elliptic curves* (arXiv:1103.4944): explicit covering maps and height relations for 2/3/4-coverings; adjacent to SR-STR-115, with no automatic global support saving.

## SR-STR-114 — Full-2-torsion Selmer support under a physical cutoff
The common integral Jacobian has full rational 2-torsion, so its 2-coverings are supported on primes dividing the discriminant and physical cutoff data, giving only a subpolynomial Selmer universe.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `ADJACENT_DESCENT_SUPPORT_ONLY` — descent literature supports the finite bad-prime/Selmer architecture, but the claimed subpolynomial physical Selmer universe still depends on the repo cutoff/discriminant support calculation.
Arsenal decision: `ACTIVE`.

## SR-STR-115 — Two-to-one elliptic receiver with polynomial height transfer
The fixed-(x,delta) quartic admits an explicit degree-two map to an integral elliptic model, and physical points of cutoff B map to rational points of polynomially bounded height.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `HEIGHT_TRANSFER_ADAPTER_SUPPORTED` — covering-map/height literature supports polynomial height comparison in principle; retain the repo explicit degree-two map as the exact receiver.
Arsenal decision: `ACTIVE`.

## SR-STR-116 — Uniform bounded-height count on the moving elliptic receiver
A uniform rational-point theorem on the integral elliptic targets gives a subpolynomial count for every fixed (x,delta), with constants controlled across the moving family.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `CONDITIONAL_EXTERNAL_COUNTING_GATE` — Dujella/Naccarato provide strong bounded-height counts under rational 2-torsion hypotheses, but use requires exact verification that the integral moving targets preserve the required torsion and that repo physical height maps to the theorem height with uniform polynomial constants.
Arsenal decision: `ACTIVE`.

## SR-STR-117 — Occupied first-coordinate support controls the N2 exponent
After the uniform fixed-fiber bound and subpolynomial delta universe, the N2 count equals the exponent of occupied q1-support up to B^o(1); the same holds for bounded-multiplicity j-support.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED` — no external theorem is promoted beyond the repo population/measure/quantifier contract.
Arsenal decision: `ACTIVE`.

## SR-STR-118 — Möbius injection from occupied q1 support to active-face support
An exact fractional-linear coordinate adapter injects occupied q1 values into the frozen Stage14 active-face support and transfers packets without changing the physical cutoff measure.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED` — no external theorem is promoted beyond the repo population/measure/quantifier contract.
Arsenal decision: `ACTIVE`.

## SR-STR-119 — Strict sub-half bound off the critical support wall
For every fixed positive distance from the critical wall, occupied first-coordinate support is O(B^(1/2-epsilon)) up to subpower loss.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED` — no external theorem is promoted beyond the repo population/measure/quantifier contract.
Arsenal decision: `ACTIVE`.

## SR-STR-120 — Critical support wall as the remaining N2 receiver
Combining the support injection and off-wall estimate isolates a fixed critical wall neighborhood as the only possible half-power contribution to occupied q1 support.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED` — no external theorem is promoted beyond the repo population/measure/quantifier contract.
Arsenal decision: `ACTIVE`.

## SR-STR-121 — No-independent-sieve certificate for the frozen local-root ledger
The Stage14 local-root conditions already define the active-face host; multiplying the same ledger into the critical-wall count would double-charge identical local information.
Potential weapon types: UPPER_BOUND_GATE, NEGATIVE_CERTIFICATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED` — no external theorem is promoted beyond the repo population/measure/quantifier contract.
Arsenal decision: `ACTIVE`.

## SR-STR-122 — Diagonal slope-collision energy on critical support
The natural q1/q0 slope adapter is injective on the critical occupied set, so its collision energy contains only diagonal pairs and yields no additive-energy saving.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED` — no external theorem is promoted beyond the repo population/measure/quantifier contract.
Arsenal decision: `ACTIVE`.

## SR-STR-123 — Exponent-neutral q1 projections on critical support
Available projections from the critical occupied set have bounded fibers and images of the same exponent, so projection thinness alone cannot improve the half-power bound.
Potential weapon types: COUNTING_LEMMA, UPPER_BOUND_GATE.
Applicability gaps: Repository normalization only; no external theorem search or arsenal promotion has yet been audited for this exact population and measure.
Transfer verdict: `REPO_EXACT_RECEIVER_RETAINED` — no external theorem is promoted beyond the repo population/measure/quantifier contract.
Arsenal decision: `ACTIVE`.

## Firewalls
- SR-STR-114 descent support is not itself a global power-saving theorem.
- SR-STR-115 height transfer must be matched to the exact physical cutoff before invoking any external point count.
- SR-STR-116 is not treated as an automatic moving-family theorem; torsion, field, model, and height hypotheses remain explicit gates.
- SR-STR-117..123 are repo support reductions/barriers and are not promoted from generic external literature.
- CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT remains 1/2; no strict sub-square-root whole-family theorem is claimed.
- No perfect-cuboid existence or nonexistence claim is made.
