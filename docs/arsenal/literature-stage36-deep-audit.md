# Stage36 Delta Phase 2 — Deep Mathematical Literature Audit

Status: **DISCOVERY ONLY — no Arsenal implementation, no merge**

```text
STAGE36_DELTA_ONLY=true
DISCOVERY_PR=1690
BRANCH=arsenal-stage36-literature-strengthening-audit
PHASE1_HEAD=3566ae0010dcdc06c25c0c0058cb2e4c6267150a
ARSENAL_BASE_MAIN=386b6a52d7bfec2e8903412c7ca56976b46c288b
STAGE36_ARSENAL_SOURCE_HEAD=2fc3f4b8afb28bb23765bd861cbd7c52aafd6563
STAGE36_HARVEST_SNAPSHOT_HEAD=07a465cb5025e7c0188fb63610bb40e4b54e7a84
STAGE36_DISCOVERY_DEDUP_EXACT_HEAD=0ad4a2fc78ebd3ee55c47d9bf5100d8e4cee3b66
LITERATURE_DISCOVERY_ONLY=true
ARSENAL_IMPLEMENTATION_PERFORMED=false
MERGE_AUTHORIZED=false
```

The machine companion `docs/arsenal/literature-stage36-deep-audit.json` contains the full per-entry hypotheses, theorem metadata, missing inputs/adapters, exact strength deltas, bibliography, blockers, duplicates and Phase-3 handoff. This audit consumes only Phase-1 P0/P1/P2 entries; Stage30–35 literature search is not restarted.

## Executive classification

Over the ten Phase-2 targets, the principal classifications are: **DIRECT_STRENGTHENING=2, ADAPTER_STRENGTHENING=2, EXTEND_OLDER_CARD=2, EXTEND_STAGE36_CARD=2, SOURCE_ANCHOR_ONLY=2**. There is no currently usable new terminal. One genuinely stronger global terminal interface is identified for Hilbert/Selmer coupling, but it is **BLOCKED_BY_ADAPTER**.

| Target | Classification | Exact literature-level verdict |
|---|---|---|
| `S36-PW01` | `SOURCE_ANCHOR_ONLY` | Pardini Theorem 2.1 + Riemann–Hurwitz place the character-quotient inventory inside standard abelian-cover theory; Stage36 value is exact marking/inertia/open-strata bookkeeping. |
| `S36-PW02` | `DIRECT_STRENGTHENING` | Kani–Rosen 1989 Theorem B gives the exact V4 Jacobian isogeny relation. Stage36 is an exact specialization plus explicit maps/differential verification, not a new decomposition theorem. |
| `S36-PW03` | `EXTEND_STAGE36_CARD` | quadratic-extension anti-invariant rank is standard twist eigenspace algebra; rank-jump theorems require extra surface hypotheses and do not imply receiver compatibility/full MW. |
| `S36-PW04` | `ADAPTER_STRENGTHENING` | strong route to genuine H1/Kummer/Selmer semantics exists, but the pointwise chart tuple must first be proved to come from one global torsor/cover class. |
| `S36-PW05` | `SOURCE_ANCHOR_ONLY` | explicit order-4 half/2-isogeny normalization is classical descent interface; no full torsion/Selmer/MW conclusion follows. |
| `S36-PW06` | `DIRECT_STRENGTHENING` | Gusić–Tadić 2012 **Theorem 1.1** matches the split-full-2 injective-specialization step essentially exactly. This is the strongest direct theorem match. |
| `S36-PW07` | `ADAPTER_STRENGTHENING` | Serre Chapter III gives an exact global Hilbert-symbol compatibility theorem, but Stage36 dynamic reservoir rows are not yet one fixed global H1/Kummer localization system. |
| `B01 -> S30-W01` | `EXTEND_OLDER_CARD` | Arf/Witt/classical-group theory can compress abstract quadratic-space type, but not source-labelled subgroup orbits/canonical representatives without an acting-group theorem. |
| `B08 -> S31-W01` | `EXTEND_OLDER_CARD` | successive-cover genus preflight is standard branch/Riemann–Hurwitz mathematics; Stage36 adds exact reconstruction/degeneration routing. |
| `B12 -> S34-W02` | `EXTEND_STAGE36_CARD` | specialization/rank-jump literature strengthens the growth taxonomy/anti-loop boundary; it does not make the exceptional receiver locus finite or empty. |

## 1. Finite quadratic / symplectic modules

Arf's characteristic-2 quadratic-form classification and standard Witt theory give a real compression opportunity: after extracting the radical, a nonsingular F2 quadratic quotient is structurally classified by dimension/Witt-Arf type. Classical-group results can then describe full orthogonal/symplectic orbits and stabilizers when the acting group is actually the required full classical group. This is **not** enough to replace the Stage36 enumeration wholesale. Stage36 B01 classifies *source-defined* kernels under a *source-defined symmetry subgroup*, carries stabilizer/radical/squareclass-rank/orbit metadata, and keeps base-field and extension-field equivalence relations separate. Structural classification does not supply those source semantics.

The safe compression architecture is therefore:

`source-labelled finite population -> radical -> nondegenerate quotient -> dimension/Arf/Witt type -> classical-group orbit theorem only if the repo proves the acting source group -> residual source-subgroup orbit/canonicalization audit`.

A proposed Stage36 transvection literature weapon would be duplicate. Existing `S32-PW06` already owns the basis-independent symplectic-transvection pruning interface and already has a literature delta for the F2 transvection direction normal form. B01 should strengthen `S30-W01`, not duplicate Stage32.

## 2. Reciprocal / birational transformations

No surviving P0/P1/P2 Stage36 entry supports a new reciprocal literature weapon. Hostile Stage36 dedup was mathematically meaningful here. The rejected reciprocal candidate A03 is an involution-quotient-with-reconstruction operation and belongs to the broad `S35-PW02 EXACT_RECEIVER_INVOLUTION_QUOTIENT_ADAPTER`; A04/A07 are source-lift square criteria already represented by `S35-PW03`. `S35-PW04` remains a different operation: reciprocal *shared-factor scaling compression* after a simultaneous-square receiver has already been materialized.

General birational/Cremona/involution literature cannot replace the load-bearing repo interfaces: exact source open, denominator/fixed locus, inverse reconstruction, field of definition and physical chamber. Consequently B08 remains only an upstream cover/genus preflight extension of `S31-W01`. **No new Stage36 reciprocal/birational literature weapon is recommended.**

## 3. Characters / squareclasses / Selmer semantics

Pure F2 row-span and squareclass algebra is already covered by the Stage34/35 squareclass lineage. The meaningful Stage36 delta is not linear algebra itself but the source-bound functions and local charts.

For `S36-PW04`, Schaefer/Stoll/explicit n-descent literature gives a clear adapter target: identify the chart tuple with one genuine global torsor or n-cover class in the appropriate H1, and prove the repo's chart evaluations are its Kummer/localization coordinates. Only after that binding can the data feed a genuine Selmer or n-cover object such as existing `LIT-PW03`. Pointwise triviality/nontriviality of several squareclasses is not by itself a Selmer-group statement.

Thus PW04 is a strong **ADAPTER_STRENGTHENING**, not a new terminal and not a marked Brauer/H2 claim. Its repo-specific value is the canonical chart selection, transition-square proof, exact open coverage and iff source reconstruction.

## 4. Hilbert reciprocity / local-global coupling

This is the largest unrealized strengthening. Serre, *A Course in Arithmetic*, Chapter III Theorems 2–4 gives the relevant exact interface. In particular, once finitely many global coefficients/classes are fixed, the simultaneous prescribed local Hilbert signs come from a single global element exactly when the finite-support, product-formula and local-realizability compatibility conditions hold. This is much stronger than treating prime rows independently.

However, it does **not** currently close Stage36. `S36-PW07` has source-dependent moving prime reservoirs and point/class-dependent local rows. The repo has not yet proved that these are localizations of one fixed global H1/Kummer variable system. Therefore:

`local rows -> Hilbert reciprocity -> contradiction`

is invalid at present. The required interface is:

`REPO_LOCAL_DATA -> FIXED_GLOBAL_H1/KUMMER_CLASS_SYSTEM -> EXACT_LOCAL_HILBERT/TATE_PAIRINGS -> SERRE / POITOU-TATE GLOBAL COMPATIBILITY -> COMPATIBILITY OR OBSTRUCTION`.

Poitou–Tate, e.g. Milne Theorem I.4.10, becomes genuinely relevant only after the finite global Galois module and its dual local conditions are source-bound. Before that point it is terminology, not an adapter. Stage36 negative boundaries E06 and E07 therefore remain load-bearing: Hilbert product formula is a checksum, and local admissibility is not global solvability.

The only new terminal candidate from Phase 2 is **GLOBAL_HILBERT_SELMER_COMPATIBILITY_TERMINAL**, but its status is `BLOCKED_BY_ADAPTER`. It must not be implemented as an active Arsenal weapon yet.

## 5. Quadratic twists / rank jump / Mordell–Weil

### PW06 — strongest direct match

Gusić–Tadić, *A remark on the injectivity of the specialization homomorphism*, Glasnik Mat. 47 (2012), Theorem 1.1, treats a nonconstant

`E: y^2=(x-e1)(x-e2)(x-e3),  ei in Z[t]`

and gives the square-free-divisor nonsquare criterion used to certify injectivity of specialization. This matches the exact proof shape of Stage36 36-09N. The source-lock already records the same criterion and the audited `q0=6` check; Phase 2 supplies the exact theorem-level locator. The injectivity step is therefore standard literature mathematics. Stage36's reusable contribution is the exact `q0=6` criterion replay plus the fixed-fiber 2-isogeny descent, relative visible section/torsion checks and Kummer-image synthesis.

Crucially, injectivity plus rank equality is still not a full generic MW-group certificate. A stronger promotion would need a certified complete specialized MW basis/saturation/index and proof that the visible generic sections map onto the necessary specialized free generators, with torsion controlled. `explicit non-torsion point != full MW group` remains enforced.

### PW03 and B12 — rank-jump literature is not a terminal

The rank identity over a quadratic extension is standard twist eigenspace algebra: the extension rank is the sum of the base curve and quadratic-twist ranks. This directly source-anchors the anti-invariant step of PW03.

Loughran–Salgado, *Rank jumps on elliptic surfaces and the Hilbert property*, Ann. Inst. Fourier 72 (2022), Theorems 1.1 and 1.2, can give non-thin rank-jump loci under specific geometric hypotheses. Those hypotheses have not been established for the exact Stage36 family. Even if they were, the theorem gives abundance of rank growth, not receiver compatibility, full MW groups, or a finite exceptional-parameter theorem. Thus the strongest current use is anti-loop/growth-locus context for PW03/B12, not closure.

If future Stage36 data reaches a certified full MW subgroup/index plus exact receiver-local subsets, do **not** create another terminal species. Route to existing `LIT-PW01` Mordell–Weil sieve (Bruin–Stoll 2010) or `LIT-PW02` elliptic Chabauty (Bruin 2003), as appropriate.

## 6. Finite fields / Weil completion

There is no accepted Stage36 positive card that independently classifies all exceptional primes. `S36-PW07` explicitly withholds finite-exceptional-prime credit. Therefore the standard smooth-curve Hasse–Weil estimate does not justify a new Stage36 literature weapon.

If a Stage36 auxiliary quotient later needs `small-prime census + smooth bounded-genus large-prime point existence`, route it to `S35-PW05 FINITE_EXCEPTIONAL_PRIME_CLASSIFICATION_BY_CENSUS_WEIL_COMPLETION`. A finite-field point gives a p-adic point only after the required nonsingularity/Hensel-lift argument. A new Stage36 Weil-completion weapon would currently be **DUPLICATE**.

## 7. Gaussian / norm support

For an actual cyclic norm equation, the Hasse norm theorem is potentially stronger than independent local prime filters: an element is a global norm iff it is a norm everywhere locally. In particular this is relevant in principle for a genuine `Q(i)/Q` Gaussian norm object.

PW07 does not yet expose that input. It has directional prime support, conjugation/unit-sensitive source factorization and local character rows; that is not automatically one global norm equation. The missing bridge is `GAUSSIAN_SUPPORT_TO_EXACT_GLOBAL_NORM_EQUATION`. Until such an equation is source-locked, invoking Hasse norm/genus theory would over-credit the data. If the bridge is eventually proved, the result should first be deduped against the older Stage14/Stage35 Gaussian lineage rather than creating a new Stage36 terminal by default.

## Strongest results

**Strongest direct strengthening:** `S36-PW06`. Gusić–Tadić 2012 Theorem 1.1 is an unusually exact literature match and converts the prior generic source reference into theorem-level provenance. `S36-PW02` is second: Kani–Rosen Theorem B exactly explains its V4 Jacobian decomposition.

**Strongest adapter strengthening:** `S36-PW07`, narrowly ahead of PW04. If the dynamic reservoir rows can be bound to one global Kummer/H1 localization system, Serre/Poitou–Tate machinery can replace independent local filters by a coupled global compatibility test. PW04 supplies the natural torsor/Kummer side of the same bridge.

**New terminal candidate:** only `GLOBAL_HILBERT_SELMER_COMPATIBILITY_TERMINAL`, currently `BLOCKED_BY_ADAPTER`. No terminal credit is added in Phase 2.

**Existing-card extensions:** B01 should extend `S30-W01`; B08 should extend `S31-W01`. PW03/B12 may later feed the existing MW sieve/elliptic-Chabauty literature terminals but do not justify duplicates.

**Duplicates:** new Stage36 transvection method -> `S32-PW06`; new reciprocal method -> Stage35 PW02/PW03/PW04 according to interface; new finite-field Weil completion -> `S35-PW05`; new MW sieve/elliptic Chabauty terminal -> existing `LIT-PW01/LIT-PW02`.

## Main hypothesis blockers / research gaps

1. PW07/PW04 lack a proved fixed global H1/Kummer class/localization system tying together all pointwise/dynamic local rows.
2. PW03/B12 lack a proof that the exact Stage36 elliptic surface satisfies Loughran–Salgado Theorem 1.1 or 1.2 hypotheses.
3. B01 lacks a proof that the source symmetry subgroup is the full classical group needed for structural orbit theorems to replace residual enumeration.
4. PW06 lacks the stronger basis/saturation/preimage data required for full generic MW credit; injectivity alone is insufficient.
5. Gaussian support has not been source-bound to one global cyclic norm equation.
6. There is no separate Stage36 finite-exceptional-prime contract to strengthen; S35-PW05 remains the correct owner.

## Phase 3 exact handoff

1. **PW07 + PW04 first:** attempt `DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM`. Identify the exact finite global module/class variables, prove every Stage36 local row is their localization/evaluation, and materialize Serre Chapter III Theorem 4 compatibility data. If dynamic support prevents one fixed global system, fail closed and retain E06/E07.
2. **PW06:** lock Gusić–Tadić 2012 Theorem 1.1 directly from the original paper and compare every polynomial/divisor hypothesis against the `q0=6` certificate. Separately inspect whether full specialized MW basis/saturation data exists; do not infer full generic MW from rank equality.
3. **PW02:** lock Kani–Rosen Theorem B directly from the original paper and encode the exact V4/genus-zero specialization. Keep Jacobian-isogeny and rational-point credit separate.
4. **PW03 + B12:** test the exact Stage36 elliptic surface against every Loughran–Salgado Theorem 1.1/1.2 hypothesis. If neither matches, freeze `NOT_APPLICABLE` for that strengthening rather than broadening theorem credit.
5. **B01:** only if enumeration compression is operationally useful, compute radical/nondegenerate quotient/Arf-Witt type and prove the actual acting source group before replacing any orbit enumeration. Dedup transvection work against `S32-PW06`.
6. **PW01/B08/PW05:** source-lock theorem locators only; no new weapon unless a genuinely stronger output than the current card/older-card contract is found.

No `NOVEL`, `NEW_THEOREM`, or `FIRST_RESULT` claim is made. A bounded search miss may only be recorded as `NO_DIRECT_MATCH_FOUND_IN_THIS_BOUNDED_SEARCH`.
