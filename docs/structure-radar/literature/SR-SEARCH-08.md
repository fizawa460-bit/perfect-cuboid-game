# StructureRadar literature ledger — search batch 08

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-08-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-057,SR-STR-058,SR-STR-059,SR-STR-060,SR-STR-061,SR-STR-062,SR-STR-063,SR-STR-064
SEARCH_BATCH_SIZE=8
EVIDENCE_POLICY=repo exact receiver first; external primary literature is adjacent unless population/height/quantifiers match
NOVELTY_BY_SEARCH_ABSENCE=false
VALIDATION_RETRIGGER=exact-head controller after self-clean

## SR-STR-057 — Toric master space-diagonal receiver on the two-face host
Retain the exact Stage19 rational-point receiver. Generic fibred-surface literature does not impose positivity, primitivity, exact-two-face, physical height R<=B or canonical multiplicity. Transfer verdict: `REPO_EXACT_RECEIVER`. Arsenal decision: `ACTIVE`.

## SR-STR-058 — Split-factor nonisotrivial genus-one tau torsor
The displayed split factorization and binary-quartic fibre remain the repo normal form. A genus-one model alone gives neither a rational section nor the physical counting saving. Transfer verdict: `REPO_EXACT_FIBRATION`. Arsenal decision: `ACTIVE`.

## SR-STR-059 — Tau-adic parity obstruction to a rational section
The tau-adic parity certificate is retained only for the generic function-field fibre; it is not a nonexistence statement for specialized physical fibres. Transfer verdict: `REPO_LOCAL_NO_SECTION_CERTIFICATE`. Arsenal decision: `ACTIVE`.

## SR-STR-060 — Constant-u bisection genus and physical-degeneration barrier
The constant-u genus/discriminant classification remains repo-specific; degree-two points on z^2=1 are boundary and are not promoted to physical lower families. Transfer verdict: `REPO_BISECTION_CLASSIFICATION`. Arsenal decision: `ACTIVE`.

## SR-STR-061 — Affine-linear moving-u multisection discriminant classification
The sextic/genus-two and rational discriminant-strata classification is retained exactly and is not extended to quadratic or higher-degree moving u. Transfer verdict: `REPO_LINEAR_MULTISECTION_CLASSIFICATION`. Arsenal decision: `ACTIVE`.

## SR-STR-062 — Universal toric physical-height ledger and degree-eight saturation
The formula h_alg=2d_x+2d_y-g is a repo physical-height adapter. R501/R502 saturation at h_alg=8 does not exclude polynomially thicker families. Transfer verdict: `REPO_HEIGHT_ADAPTER`. Arsenal decision: `ACTIVE`.

## SR-STR-063 — Tau pushforward invariant and collision receiver
The tau identity and equal-tau collision equation are retained as the exact pushforward receiver. Any external fibration theorem still needs uniform support/fibre bounds in the same physical measure. Transfer verdict: `REPO_PUSHFORWARD_RECEIVER`. Arsenal decision: `ACTIVE`.

## SR-STR-064 — Support-times-max-fiber upper exponent gate
The inequality N2(B)<=#T(B) max_t w_B(t) is elementary, but sigma+phi<1/2 is valid only when both inputs are uniform in the same primitive canonical physical measure. Bonolis--Browning, *Uniform bounds for rational points on hyperelliptic fibrations* (arXiv:2007.14182), and Loughran--Smeets, *Fibrations with few rational points* (arXiv:1511.08027), are adjacent primary literature and are not promoted without an exact receiver adapter. Transfer verdict: `REPO_EXACT_COUNTING_GATE_WITH_ADJACENT_LITERATURE`. Arsenal decision: `ACTIVE`.

## Firewalls
- `NOVELTY_BY_SEARCH_ABSENCE=false`.
- No-section does not imply no specialized rational points.
- Boundary z^2=1 multisections are not physical lower families.
- Linear multisection classification is not extrapolated to higher degree.
- One-parameter height saturation does not rule out thicker families.
- External fibration literature requires exact population, height, multiplicity and quantifier matching.
- No perfect-cuboid existence or nonexistence claim is made.
