# StructureRadar literature ledger — search batch 05

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-05-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-031,SR-STR-032,SR-STR-033,SR-STR-036,SR-STR-037,SR-STR-038,SR-STR-039,SR-STR-040
SEARCH_BATCH_SIZE=8
EVIDENCE_POLICY=primary sources for external theorem claims; repo arsenal checked first
NOVELTY_BY_SEARCH_ABSENCE=false

## SR-STR-031 — Finite-order Selberg--Delange theorem contract
Repo contract: the finite-order Selberg--Delange receiver requires the declared zeta-power factorization together with the local analytic region, growth control, coefficient majorants and a compatible finite expansion. De la Bretèche--Tenenbaum, *Remarks on the Selberg--Delange method* (Acta Arith. 200 (2021), arXiv:2010.12929), treats Dirichlet series of the form `zeta(s)^rho G(s)` and proves sharp finite asymptotic expansions under explicit hypotheses. This validates the theorem species but does not silently discharge every repo-specific local hypothesis. Transfer verdict: `REPO_CONTRACT_RETAINED`. Arsenal decision: `ACTIVE`.

## SR-STR-032 — Exact shared-hypotenuse representation convolution
Repo theorem: the Stage14 count is an exact weighted convolution over primitive Pythagorean representations sharing a hypotenuse, with the primitive/canonical multiplicity correction kept explicit. Zelator, *A Non-Existence Property of Pythagorean Triangles with a 3-D Application* (arXiv:0903.1280), records common-hypotenuse Pythagorean pairs and related box constructions, but does not supply the repo's exact weighted convolution or moving-base correction. Transfer verdict: `REPO_EXACT_CONVOLUTION`. Arsenal decision: `ACTIVE`.

## SR-STR-033 — Mod-7 two-parameter exactly-one-face family
Repo theorem: coprime parameters `m=2 (mod 14), n=1 (mod 14)` give the declared primitive integral-space exactly-one-face family and the resulting half-power lower construction. Rathbun, *The Integer Cuboid Table* (arXiv:1705.05929), documents face-type integer cuboids and exhaustive computational enumeration, confirming the surrounding cuboid species but not this congruence family, the mod-7 exclusion of the other faces, or its asymptotic lower count. Transfer verdict: `REPO_PROVED_LOCAL_FAMILY`. Arsenal decision: `ACTIVE`.

## SR-STR-036 — Primitive Euclid face decomposition
Repo theorem: an integral right-triangle face with a distinguished leg is reduced uniquely to a scale times a primitive Euclid certificate, with orientation retained. The classical Euclid parametrization is explicitly recalled in Ochieng--Chikunji--Onyango-Otieno, *Pythagorean Triples with Common Sides* (Journal of Mathematics 2019, DOI 10.1155/2019/4286517), including the coprimality and opposite-parity conditions for primitiveness. The repo's distinguished-leg normalization remains part of the adapter. Transfer verdict: `CLASSICAL_PARAMETRIZATION_WITH_REPO_NORMALIZATION`. Arsenal decision: `ACTIVE`.

## SR-STR-037 — Exact two-face gluing with multiplicity one
Repo theorem: two primitive oriented Pythagorean faces glued on the common physical leg reconstruct the primitive canonical cuboid with the repo's declared multiplicity convention. Ochieng--Chikunji--Onyango-Otieno (2019, DOI 10.1155/2019/4286517) derives formulae for pairs of primitive Pythagorean triples with a common leg and counts triples for a fixed leg. This is direct structural prior art for the common-leg mechanism, while the cuboid gluing and canonical multiplicity-one statement remain repo-specific. Transfer verdict: `REPO_PROVED_GLUE_WITH_EXTERNAL_COMMON_LEG_SUPPORT`. Arsenal decision: `ACTIVE`.

## SR-STR-038 — Raw-pair face-incidence graph identity
Repo theorem: `E(B)=N2(B)+3T(B)=1/2 sum_F deg_B(F)` and the raw-edge correction `n_1(B)=3T(B)`, hence `9T(B)^2<=Q_edge(B)`, are exact population/accounting identities in the Stage14 incidence graph. No external asymptotic theorem is needed, and a generic cuboid enumeration cannot substitute for the charged raw-pair measure. Transfer verdict: `REPO_EXACT_POPULATION_IDENTITY`. Arsenal decision: `ACTIVE`.

## SR-STR-039 — Stage14 integral-space exactly-two half-power upper theorem
Repo theorem: for primitive canonical `0<a<b<c` with integral space diagonal `d<=B` and exactly two integral faces, `N2(B)<<B^(1/2+o(1))`. Rathbun (arXiv:1705.05929) supplies a large computational corpus of integer cuboids but not this asymptotic upper theorem. No searched primary source replaces the repo proof, and search absence is not a novelty claim. Transfer verdict: `REPO_PROVED_UPPER_BOUND`. Arsenal decision: `ACTIVE`.

## SR-STR-040 — Consumed and superseded asset recharge discipline
Repo rule: each support, core and fiber is charged once; a superseded theorem may retain valid lemmas, but already consumed data cannot be recharged as an independent saving. This is a proof-accounting firewall rather than a literature-dependent analytic theorem. Transfer verdict: `REPO_EXACT_ACCOUNTING_FIREWALL`. Arsenal decision: `ACTIVE`.

## Firewalls
- `NOVELTY_BY_SEARCH_ABSENCE=false`.
- General Selberg--Delange theory is not silently substituted for the repo-specific local hypothesis contract.
- Common-hypotenuse examples are not promoted to the exact weighted primitive convolution or its moving-base correction.
- Face-cuboid computation does not prove the mod-7 family, the exclusion of the other faces, or the half-power lower count.
- Common-leg Pythagorean formulae do not bypass primitive/canonical cuboid normalization.
- The raw-incidence identity is population accounting, not a collision saving.
- Finite computational enumeration is not an asymptotic proof of the Stage14 half-power upper theorem.
- Proof assets already consumed in one saving are not recharged under a renamed or superseded theorem.
- No perfect-cuboid existence or nonexistence claim is made.
