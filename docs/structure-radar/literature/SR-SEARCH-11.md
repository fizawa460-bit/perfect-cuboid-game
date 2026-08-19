# StructureRadar literature ledger — search batch 11

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-11-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-084,SR-STR-085,SR-STR-086,SR-STR-087,SR-STR-088,SR-STR-089,SR-STR-090,SR-STR-091,SR-STR-092,SR-STR-093
SEARCH_BATCH_SIZE=10
EVIDENCE_POLICY=repo exact receiver first; external primary literature is adjacent unless target population, height, multiplicity, modulus growth and quantifiers match
NOVELTY_BY_SEARCH_ABSENCE=false

## SR-STR-084 — Exact normalized physical-height identity with primitive scale retained
Retain Gamma^2 R^2=4 delta^2 h^2 J(p+q) as the exact repo height adapter with primitive scale Gamma. The asymmetric core-height consequences alone do not improve the exponent. Transfer verdict: `REPO_EXACT_HEIGHT_IDENTITY`. Arsenal decision: `ACTIVE`.

## SR-STR-085 — Cross-gcd primitive-scale factorization and physical diagonal product
Retain the three cross-gcd channels, Gamma=2 delta epsilon C, R=(h/epsilon) kappa w' c', and h*kappa<=epsilon B as the exact normalization. Fixing R gives kappa|R but leaves an R^(1+o(1)) hyperbolic boundary. Transfer verdict: `REPO_EXACT_GCD_FACTORIZATION_AND_HEIGHT_ADAPTER`. Arsenal decision: `ACTIVE`.

## SR-STR-086 — Residual-height versus cross-gcd threshold dichotomy
Retain the small-h*kappa / large-cross-gcd split as a theorem interface only; neither branch has a uniform fixed-power saving. Transfer verdict: `REPO_THRESHOLD_DICHOTOMY`. Arsenal decision: `ACTIVE`.

## SR-STR-087 — Cross-gcd residual physical-coordinate chart
Retain the residual edge/face-diagonal formulas and exact physical-edge budget as a coordinate normal form. Large cross-gcd cancellation is not promoted to sparsity. Transfer verdict: `REPO_EXACT_RESIDUAL_COORDINATE_CHART`. Arsenal decision: `ACTIVE`.

## SR-STR-088 — Residual squareclass incidence system and small-L witness
Retain the coupled squareclass receiver together with the actual Stage19 L=1 witness, which blocks any unconditional pointwise L>1 theorem. Transfer verdict: `REPO_SQUARECLASS_RECEIVER_WITH_COUNTERMODEL`. Arsenal decision: `ACTIVE`.

## SR-STR-089 — Residual completion rigidity at fixed outer cell
At fixed outer residual data the completion multiplicity is at most one; moving outer-cell support remains the bottleneck. Transfer verdict: `REPO_EXACT_COMPLETION_RIGIDITY`. Arsenal decision: `ACTIVE`.

## SR-STR-090 — Uniform Pell compression of the residual completion fiber
Retain the maximal-order Pell compression as the repo mechanism for subpower completion multiplicity without uniform Mordell-Weil rank. Bounded-region Pell literature is adjacent because the Stage19 discriminant/coefficient package moves. Transfer verdict: `REPO_UNIFORM_PELL_COMPRESSION_WITH_ADJACENT_PELL_LITERATURE`. Arsenal decision: `ACTIVE`.

## SR-STR-091 — Squarefree-kernel paired-slope residue receiver
Retain kappa|(m^2-n^2), kappa|(r^2+s^2), gcd(kappa,mnrs)=1 and paired slope residues as the exact growing-modulus sieve receiver. Generic square/geometric sieves do not supply lower growth of kappa; kappa=1 witnesses remain. Transfer verdict: `REPO_GROWING_MODULUS_SIEVE_RECEIVER`. Arsenal decision: `ACTIVE`.

## SR-STR-092 — Dyadic kappa raw-slope sieve
Retain the dyadic raw slope-sieve/divisor switch as an early-pipeline upper-bound tool; later physical fibers and budgets must still be charged. Transfer verdict: `REPO_RAW_SLOPE_SIEVE`. Arsenal decision: `ACTIVE`.

## SR-STR-093 — Raw-slope sieve composition barrier
Retain the composition barrier as proof accounting: an early raw-slope saving cannot be double-charged after later physical fibers. A physical-weighted kappa sieve remains open. Transfer verdict: `REPO_NO_DOUBLE_CHARGE_FIREWALL`. Arsenal decision: `ACTIVE`.

## External literature checked
- Ong–Ismail, *Integer solutions of Pell equation in bounded regions* (arXiv:2509.17882): adjacent bounded-region Pell enumeration only.
- Bhargava, *The geometric sieve and the density of squarefree values of invariant polynomials* (arXiv:1402.0031): adjacent framework, not the exact paired-slope/growing-kappa receiver.
- Baier–Patankar, *Applications of the square sieve to a conjecture of Lang and Trotter for a pair of elliptic curves over the rationals* (arXiv:1710.02125): adjacent square-sieve methodology; target population does not match Stage19.

## Firewalls
- `NOVELTY_BY_SEARCH_ABSENCE=false`.
- Exact height/gcd normal forms are adapters, not population savings.
- The L=1 witness forbids an unconditional pointwise residual-height lower bound.
- Fixed-outer-cell rigidity and Pell compression do not count moving outer-cell support.
- Generic sieves do not provide the missing kappa-growth theorem.
- Raw slope savings cannot be double-charged after later physical fibers.
- CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT remains 1/2; no strict sub-square-root whole-family theorem is claimed.
- No perfect-cuboid existence or nonexistence claim is made.
