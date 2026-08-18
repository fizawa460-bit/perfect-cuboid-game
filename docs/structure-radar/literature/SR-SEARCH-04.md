# StructureRadar literature ledger — search batch 04

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-04-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-021,SR-STR-022,SR-STR-023,SR-STR-024,SR-STR-027,SR-STR-028,SR-STR-029,SR-STR-030
SEARCH_BATCH_SIZE=8
EVIDENCE_POLICY=primary sources for external theorem claims; repo arsenal checked first
NOVELTY_BY_SEARCH_ABSENCE=false

## SR-STR-021 — Super-Kai individual Gaussian-residue occupancy gate
Repo boundary: AR-022. Kai's refined Mitsui theorem (`arXiv:2209.11816`) gives prime-element distribution in convex sets with possible Siegel-zero terms and pseudopolynomial modulus growth, but does not license extrapolation past its conductor envelope. Thorner--Zaman's effective Chebotarev theorem (`arXiv:1803.02823`) is much stronger in conductor/ray-class scale, but a direct receiver still needs an exact adapter simultaneously identifying the ordinary Gaussian residue (including units), the fixed continuous D4 angular sector, and the long radial interval. No searched primary source discharges that full adapter automatically. Transfer verdict: `EXTERNAL_GATE_RETAINED`. Arsenal decision: `EXTERNAL_GATE`.

## SR-STR-022 — Scalar host versus factor-pair measure separation
Repo theorem: AR-023. This is an exact measure/quantifier firewall, not a literature-dependent asymptotic theorem. A divisor-many map `n=Em` does not preserve pair-dependent filters merely because its fibers are subpolynomial. Transfer verdict: `REPO_EXACT_FIREWALL`. Arsenal decision: `ACTIVE`.

## SR-STR-023 — Conditioned-kernel measure firewall
Repo theorem: AR-024. Equality of the inner reciprocal-CRT formula under two different outer conditionings is insufficient for transferring a density or saving. External harmonic-analysis estimates cannot change the charged measure without an explicit adapter. Transfer verdict: `REPO_EXACT_FIREWALL`. Arsenal decision: `ACTIVE`.

## SR-STR-024 — Valuation-reduced character recombination receiver
Repo receiver: AR-025, with AR-026/027 firewalls. The valuation reduction to `(Q_nu,rho_nu)` and principal/nonprincipal character decomposition is exact, but the desired target-class domination is not supplied by character orthogonality alone. Grimmelt--Merikoski (`arXiv:2508.17979`) proves strong divisor-function equidistribution in arithmetic progressions, including almost-all modulus statements, but not the required every-retained-cell target residue theorem with the original scalar/pair conditioning. Transfer verdict: `EXTERNAL_GATE_RETAINED`. Arsenal decision: `EXTERNAL_GATE`.

## SR-STR-027 — Weighted coprime rectangle convolution
Repo theorem: AR-033. De la Bretèche's multivariable Dirichlet-series framework, *Estimation de sommes multiples de fonctions arithmétiques* (Compositio Math. 128 (2001), DOI 10.1023/A:1011803816545; Orsay preprint 1998/40), is relevant general context for multiple arithmetic sums. The repo result is more specific: it records the exact Stage12 weights, coprimality cross-correction, weighted absolute norm, and the corrected `3/4+epsilon` rectangle tails. No external replacement is needed. Transfer verdict: `REPO_PROVED_TOOLKIT`. Arsenal decision: `ACTIVE`.

## SR-STR-028 — Core-wing-shallow boundary separation
Repo theorem: AR-034. The decomposition is a proof-local boundary-control toolkit: wings and shallow sectors must each be bounded in their own measure before smooth core transfer. Huang (`arXiv:2111.01509`) supplies a modern geometric-sieve/equidistribution context for imposing local conditions, but it does not replace the repo's source-specific boundary estimates. Transfer verdict: `REPO_PROVED_TOOLKIT`. Arsenal decision: `ACTIVE`.

## SR-STR-029 — Fixed-prime overlap sieve with ordered limits
Repo theorem: AR-035. The valid theorem fixes a finite set of rejecting primes, takes `B -> infinity` under a fixed-modulus refined asymptotic, and only then enlarges the prime set. This is deliberately not a growing-modulus theorem. Geometric/Ekedahl sieve literature is compatible background, but no stronger claim is imported. Transfer verdict: `REPO_PROVED_ORDERED_LIMIT_SIEVE`. Arsenal decision: `ACTIVE`.

## SR-STR-030 — Ordered-chamber Gelfand--Leray directional transfer
Repo theorem: AR-036. Gelfand--Leray/coarea theory (for example Trinh, `arXiv:1707.05559`) supports the geometric relation between level-set density and ambient volume, but the Stage13 directional constants require the repo-specific ordered chamber and, crucially, a separately proved common arithmetic factor across directions. Transfer verdict: `REPO_PROVED_ARCHIMEDEAN_TRANSFER`. Arsenal decision: `ACTIVE`.

## Firewalls
- `NOVELTY_BY_SEARCH_ABSENCE=false`.
- No Kai safe-range theorem is extrapolated to the super-Kai receiver.
- Chebotarev/ray-class strength is not silently identified with ordinary-residue-plus-sector occupancy; the adapter remains explicit.
- Average/almost-all modulus results are not promoted to every retained cell or target class.
- Same inner kernel does not imply same outer measure.
- Fixed-prime overlap uses the order `fix finite prime set -> B infinity -> enlarge prime set`; no limit interchange.
- Gelfand--Leray geometry does not prove a common arithmetic factor.
- No perfect-cuboid existence or nonexistence claim is made.
