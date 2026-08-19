# StructureRadar literature ledger — search batch 09

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-09-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-065,SR-STR-066,SR-STR-067,SR-STR-068,SR-STR-069,SR-STR-070,SR-STR-071,SR-STR-072
SEARCH_BATCH_SIZE=8
EVIDENCE_POLICY=repo exact receiver first; external primary literature is adjacent unless population, height and quantifiers match
NOVELTY_BY_SEARCH_ABSENCE=false
VALIDATION_RETRIGGER=exact-head controller after self-clean

## SR-STR-065 — Support-energy upper exponent gate
The Cauchy--Schwarz implication #T<=B^sigma and sum w^2<=B^eta => N2<=B^((sigma+eta)/2+o(1)) is retained as an elementary repo gate. The full energy includes the diagonal N2 term, so no ambient energy estimate may be double-charged to obtain a strict saving. Transfer verdict: `REPO_EXACT_ENERGY_GATE`. Arsenal decision: `ACTIVE`.

## SR-STR-066 — Reduced tau height bound and height-only support no-go
The reduced physical-height adapter H(tau)<2B^2 is repo-specific. Counting rational parameters by height at this scale does not improve the certified half-power support bound. Transfer verdict: `REPO_HEIGHT_ADAPTER_AND_NEGATIVE_ROUTE_CERTIFICATE`. Arsenal decision: `ACTIVE`.

## SR-STR-067 — Fixed-tau ambient conic before the space-square filter
For reduced tau=p/q, p y^2-q x^2=p+q is retained as the exact ambient conic on the two-face toric host. It is not the Stage19 survivor fibre until the integral-space-square condition is imposed. Transfer verdict: `REPO_EXACT_AMBIENT_CONIC`. Arsenal decision: `ACTIVE`.

## SR-STR-068 — Pointwise subpower fibre bound versus uniform max-fibre firewall
Pointwise fixed-fibre bounds depending on rank do not supply the uniform max_tau estimate needed by the Stage19 counting gate. Naccarato, *Counting rational points on elliptic curves with a rational 2-torsion point* (arXiv:2105.04032), and Dujella, *Uniform Bounds for the Number of Rational Points of Bounded Height on Certain Elliptic Curves* (arXiv:2312.03655), give strong bounded-height estimates under rational torsion hypotheses; they are adjacent literature only unless the Stage19 fibres satisfy the same torsion, height and family-uniformity contracts. Transfer verdict: `REPO_QUANTIFIER_FIREWALL_WITH_ADJACENT_ELLIPTIC_LITERATURE`. Arsenal decision: `ACTIVE`.

## SR-STR-069 — Reduced tau core-scale decomposition
The exact decomposition A=pg, D=qg and core bound g<2B^2/H(tau) are retained as the repo dyadic-height adapter. They stratify collision packets but do not count representations or collisions. Transfer verdict: `REPO_EXACT_CORE_SCALE_ADAPTER`. Arsenal decision: `ACTIVE`.

## SR-STR-070 — Full collision-energy diagonal barrier
E_tau=N2+C_tau with E_tau>=N2 is an exact bookkeeping identity. A half-power bound for the full energy cannot by itself prove a strict sub-half estimate for N2; only off-diagonal or bandwise savings can do that. Transfer verdict: `REPO_DIAGONAL_BARRIER`. Arsenal decision: `ACTIVE`.

## SR-STR-071 — Support/off-diagonal collision hybrid gate
The inequality N2<=S+sqrt(S C) is retained as the exact no-double-charge hybrid gate. Strict sub-half requires separate bounds sigma<1/2 and sigma+kappa<1, with C genuinely off-diagonal. Transfer verdict: `REPO_EXACT_HYBRID_GATE`. Arsenal decision: `ACTIVE`.

## SR-STR-072 — Dyadic tau-height/core restart contract
On H(tau)~T, the core bound g<<B^2/T together with N_T<=S_T+sqrt(S_T C_T) defines the correct restart interface. No external theorem located here supplies the required uniform bandwise support and off-diagonal collision savings in the same primitive canonical physical measure. Transfer verdict: `REPO_DYADIC_RESTART_INTERFACE`. Arsenal decision: `ACTIVE`.

## Firewalls
- `NOVELTY_BY_SEARCH_ABSENCE=false`.
- Full collision energy may not be reused as an independent off-diagonal saving.
- Ambient fixed-tau conics are not survivor fibres until the space-square filter is imposed.
- Pointwise fixed-fibre bounds do not imply a uniform max-fibre bound.
- Rational-height support counting at H(tau)<2B^2 does not cross the half-power wall.
- Torsion-specific elliptic-curve literature is not transferred without matching torsion, height and family-uniformity hypotheses.
- Core-scale and dyadic decompositions are adapters, not collision estimates.
- No perfect-cuboid existence or nonexistence claim is made.
