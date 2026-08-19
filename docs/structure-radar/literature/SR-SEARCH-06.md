# StructureRadar literature ledger — search batch 06

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-06-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-041,SR-STR-042,SR-STR-043,SR-STR-044,SR-STR-045,SR-STR-046,SR-STR-047,SR-STR-048
SEARCH_BATCH_SIZE=8
EVIDENCE_POLICY=primary sources for external theorem claims; repo arsenal checked first
NOVELTY_BY_SEARCH_ABSENCE=false

## SR-STR-041 — Oriented-record to canonical face-incidence projection
Repo theorem: oriented face records project with exact factor two to canonical face incidences, while one/two/three-face overlaps are corrected separately. This is a repo population/measure adapter rather than a literature-dependent analytic theorem. Generic Pythagorean or cuboid enumeration cannot replace the exact oriented-to-canonical multiplicity contract. Transfer verdict: `REPO_EXACT_MEASURE_ADAPTER`. Arsenal decision: `ACTIVE`.

## SR-STR-042 — Physical restrictions as monotone post-filters for upper bounds
Repo rule: positivity, ordering, primitivity, parity, space-square and exact-face masks can only reduce a proved algebraic-superset upper bound. This is elementary set inclusion, but the one-way quantifier is essential: filters may be dropped for upper bounds only, never for lower bounds or asymptotics. Transfer verdict: `REPO_EXACT_UPPER_FILTER_ADAPTER`. Arsenal decision: `ACTIVE`.

## SR-STR-043 — Common-core decomposition and high-core emptiness
Repo theorem: the Stage14 Cayley common core divides the declared endpoint products, and under the repo coprimality/nonproportional hypotheses the surviving fixed-power cells satisfy the high-core exclusion `chi<=1/4`. No searched primary source states this exact endpoint-product obstruction with the same decorations and physical receiver. Transfer verdict: `REPO_PROVED_DIVISIBILITY_OBSTRUCTION`. Arsenal decision: `ACTIVE`.

## SR-STR-044 — Primitive Gaussian root-line lattice count
Repo theorem: count primitive `(U,V)` in the exact dyadic box on quadratic CRT root lines `C0 | a0^2 U^2 + b0^2 V^2`, under `gcd(C0,a0 b0 U V)=1`, without reintroducing the crude boundary loss. Han--Lee, *Moment formulas of Siegel transforms with congruence conditions in dimension 2* (arXiv:2507.05905), treats primitive planar lattice points with congruence conditions through Siegel-transform moment formulae. Nowak, *Primitive lattice points inside an ellipse* (arXiv:math/0307279; Czechoslovak Math. J. 55 (2005), 187--206), studies primitive points for binary quadratic regions. These validate adjacent theorem species but do not supply the repo's deterministic quadratic-CRT root-line count with the exact dyadic box and coprimality contract. Transfer verdict: `REPO_PROVED_ROOTLINE_COUNT_WITH_ADJACENT_LITERATURE`. Arsenal decision: `ACTIVE`.

## SR-STR-045 — Primitive-ratio rigidity and one-pair reconstruction
Repo theorem: one primitive agreement pair fixes the opposite agreement product and moving root product up to divisor-many fibers, with the fixed decorations and both reciprocal equations retained. This exact reconstruction is specific to the Stage14 reciprocal system; generic divisor bounds do not provide the same variable dictionary. Transfer verdict: `REPO_EXACT_RECONSTRUCTION`. Arsenal decision: `ACTIVE`.

## SR-STR-046 — Endpoint-linear column reconstruction
Repo theorem: reduced endpoint forms `L_-=J_- h_-` and `L_+=J_+ h_+` reconstruct the Stage14 column variable `M` with quantified short support. The determinant identities and support length are repo-specific, so generic linear-algebra literature adds no stronger transferable theorem. Transfer verdict: `REPO_EXACT_LINEAR_RECONSTRUCTION`. Arsenal decision: `ACTIVE`.

## SR-STR-047 — Reverse reciprocal difference-of-squares reconstruction
Repo theorem: after fixing `(U,V,M)`, two coupled difference-of-squares factorizations leave only divisor-many completions, with positivity, nonzero factors and decorations fixed. Classical difference-of-squares factorization is background only; the coupled reciprocal quantifier order and divisor-fiber bound remain the repo theorem. Transfer verdict: `REPO_EXACT_DIVISOR_RECONSTRUCTION`. Arsenal decision: `ACTIVE`.

## SR-STR-048 — CRT row lift as post-reconstruction filter
Repo rule: once reverse reconstruction has reduced the row variables to divisor-many candidates, subsequent CRT congruences can only reject candidates. They do not create an additional independent support factor or saving. This is an exact no-double-charge firewall depending on the column-to-reconstruction quantifier order. Transfer verdict: `REPO_EXACT_CRT_ACCOUNTING_FIREWALL`. Arsenal decision: `ACTIVE`.

## Firewalls
- `NOVELTY_BY_SEARCH_ABSENCE=false`.
- Oriented-record multiplicity is not replaced by generic cuboid enumeration.
- Dropping physical filters is one-way and valid only for upper bounds.
- The common-core `chi<=1/4` obstruction is not generalized beyond the declared endpoint forms and coprimalities.
- Primitive-lattice literature is adjacent context; it is not silently substituted for the exact quadratic-CRT root-line dyadic theorem.
- Generic divisor estimates do not replace the repo reconstruction variable dictionary or quantifier order.
- CRT conditions applied after reconstruction are filters, not a second support power or independent saving.
- No perfect-cuboid existence or nonexistence claim is made.
