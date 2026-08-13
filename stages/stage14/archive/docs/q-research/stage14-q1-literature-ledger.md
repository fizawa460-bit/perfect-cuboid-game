# Stage14-q1 — Reconstructed Literature Ledger

## Status

```text
STAGE14_Q1=COMPLETE_RECONSTRUCTED_LITERATURE_LEDGER
BASELINE_PR=185
BASELINE_BRANCH=agent/stage14-literature-radar
CHECKED_AT=2026-08-09
DIRECT_COUNT=0
NEAR_COUNT=10
BACKGROUND_COUNT=4
BLOCKED_COUNT=4
NEXT=Stage14-q2 correlated bilinear / quadratic-large-sieve pass
```

## Purpose

This file reconstructs PR #185 into a durable Stage14-q ledger. The old literature radar was useful but tied to an earlier frontier. q1 preserves the verified weapons and negative results, then remaps them to the current Stage14 frontiers:

- `14-4au -> 14-4av`: reciprocal-divisor blocks with Euclid-correlated coefficients;
- `14-s5h -> 14-s5i`: separable quadratic large-sieve bound proved, but actual Euclid incidence gives a two-variable weight `W(u,v)`;
- `14-t18 -> 14-t19`: local x-squareclass image is full, so the remaining target is global moving squareclass-signature collision energy;
- the exact Shimada K3 package remains reusable infrastructure rather than a literature lead that should be rediscovered.

The classification standard is deliberately strict. `DIRECT` means that the theorem/data can be imported after routine hypothesis verification. `NEAR` means that a concrete Stage14 transfer lemma or computation is visible but still unproved. `BACKGROUND` is useful conceptual provenance. `BLOCKED` means that a named mismatch prevents current transfer.

## A. Cross-track analytic weapons

### A1. Heath-Brown quadratic large sieve — NEAR

**Source.** D. R. Heath-Brown, *A mean value estimate for real character sums* (1995); the inequality is also restated and made explicit in Zihao Liu, *Explicit quadratic large sieve inequality*, arXiv:2505.09637.

**Verified content.** The quadratic large sieve gives square-root cancellation for bilinear families of real/quadratic characters with coefficients that separate into the two character variables. Liu explicitly presents an explicit version of Heath-Brown's inequality.

**Current Stage14 fit.** `14-s5h` has already proved the first separable dyadic estimate of exactly this shape. It therefore remains a valid weapon, but only after the Euclid incidence coefficient is converted to large-sieve-admissible coefficients.

**Missing hypothesis.** The actual Stage14 block carries a correlated two-variable incidence weight `W(u,v)` produced by common Euclid parameters. The large sieve does not justify replacing arbitrary `W(u,v)` by `alpha_u beta_v`.

**Promotion.** `NEAR`, not `DIRECT`.

**Handoff.** `14-s5i`, `14-4av`.

### A2. Dispersion / bilinear decomposition family — NEAR, q2 target

**Source family.** Linnik-style dispersion, bilinear forms in real/quadratic characters, divisor switching, reciprocal Jacobi-symbol bilinear forms, and structured-coefficient refinements of large-sieve estimates.

**Why retained.** Both active analytic tracks independently reached the same coefficient-correlation obstruction. This is now the highest-value literature gap.

**Missing item.** q1 does not promote a specific theorem because PR #185 predates this obstruction. Stage14-q2 must locate a primary-source theorem whose coefficient structure genuinely tolerates the Euclid/Pythagorean incidence, or record a precise mismatch.

**Promotion.** `NEAR` as a method family only; no theorem import yet.

**Handoff.** `14-s5i`, `14-4av`.

## B. K3 / lattice weapons for 14-4

### B1. Ichiro Shimada — exact level-4 modular K3 computational package — NEAR

**Primary source.** Ichiro Shimada, *The elliptic modular surface of level 4 and its reduction modulo 3*, arXiv:1806.05787 / Ann. Mat. Pura Appl. 199 (2020), together with the author's computational-data package.

**Verified content.** The paper studies the same level-4 elliptic modular K3, which has Picard number 20, and determines its automorphism structure using the Neron-Severi lattice and reduction mod 3. The author's live computational-data index still publishes data for this paper.

**PR #185 extracted machine interface.** `GramS0`, `L40vs`, `fsigma`, `AutX0h0`, `AutX0f`, torsion-section/translation data, chamber data, and `Galmu` were identified as the operational objects. The intended lattice problem was

```text
C^2 = -2,
fsigma.C = 2,
M.C = 4,
```

followed by effectivity/chamber, automorphism-orbit, Galois descent, and physical-positivity checks.

**Current fit.** Still computationally actionable and should not be rediscovered. However, the present `14-4av` bottleneck is analytic, so this package is now standing infrastructure rather than the immediate next weapon.

**Missing hypothesis/data.** Exact coordinate expression of the physical class `M` in Shimada's fixed `S0` basis, unless a later 14-4 stage has already supplied it.

**Promotion.** `NEAR`.

### B2. Keum--Kondo automorphism input — BACKGROUND

Provides conceptual provenance for automorphisms used by Shimada. Operationally superseded by Shimada's explicit matrices in the fixed basis.

### B3. Clingher--Malmendier Neron-Severi classification route — BACKGROUND

Useful fallback lattice classification if the exact Shimada package becomes unusable. It is not preferred while the exact surface-specific data are available.

### B4. Greer--Helfer--Sheridan / general bisection-moduli route — BACKGROUND

Useful only if the exact lattice computation unexpectedly leaves a positive-dimensional bisection family. Their rational elliptic-surface setting is not a direct theorem for the special Stage14 K3.

## C. Small-point / first-point weapons for 14-s

### C1. Clayton Petsche — canonical-height lower bound — NEAR

**Primary source.** *Small rational points on elliptic curves over number fields*, arXiv:math/0508160.

**Verified content.** Petsche proves explicit lower bounds for the canonical height of non-torsion points in terms of the number-field degree and Szpiro ratio, with polynomial dependence on those quantities.

**Stage14 fit.** For `Q`, this can be compared against the Stage14 physical upper window once minimal discriminant, conductor, and Szpiro ratio are controlled for

```text
W^2 = Z(Z-S^2)(Z+X^2).
```

**Missing hypothesis.** Uniform or sufficiently strong family control of the Szpiro ratio/minimal model. The polynomial loss may erase the needed saving.

**Promotion.** `NEAR`.

### C2. Francesco Naccarato — point-counting pipeline from Petsche — NEAR

**Primary source.** *Counting rational points on elliptic curves with a rational 2-torsion point*, arXiv:2105.04032.

**Verified content.** The paper extends bounded-height rational-point estimates to curves with a rational 2-torsion point via 2-isogeny descent and explicitly uses Petsche to obtain a stronger subpolynomial bound.

**Stage14 fit.** The important value is proof architecture: discriminant/Szpiro lower bound -> lattice/point counting. It is not by itself a theorem on the least physical non-torsion point in a moving Pythagorean family.

**Promotion.** `NEAR`.

### C3. Pierre Le Boudec — lowest non-torsion point via large-prime factor + complete 2-descent — NEAR, high priority

**Primary source.** *Height of rational points on congruent number elliptic curves*, arXiv:1802.07136.

**Verified content.** Le Boudec proves that a positive proportion of squarefree congruent-number parameters have a strong lower bound for the canonical height of the lowest non-torsion rational point.

**PR #185 transfer interface.** Reproduce, rather than blindly import, the architecture: retain a quantitatively large parameter population with a uniquely identifiable large prime factor, then use complete 2-descent to suppress anomalously small points by divisor-variable counting.

**Current Stage14 fit.** Still one of the best weapons for the `R -> V` first-small-point gate. It may also interact with the new correlated-bilinear obstruction if the large-prime restriction simplifies the Euclid incidence matrix.

**Critical mismatch.** Le Boudec works in a fixed quadratic-twist family with constant `j`; Stage14 is a non-isotrivial Pythagorean family. Density and height variables must be re-proved in Stage14 coordinates.

**Promotion.** `NEAR`.

### C4. Le Boudec — quadratic twists of a fixed elliptic curve — BACKGROUND

Confirms that the distribution of the least non-torsion point is itself deep even in a simpler fixed-twist family. Useful as normalization and as a warning not to replace the statistic by rank alone.

### C5. Loughran--Salgado rank-jump results — NEAR / delimitation

Useful for separating qualitative abundance of positive-rank fibers from the much stronger least-small-point counting problem. It does not deliver the Stage14 physical-height law.

### C6. Wong specialization-height results — NEAR only under a future section/multisection reduction

Potentially useful if active points are eventually shown to arise from finitely many generic sections or multisections. It does not currently control rank-jump points that do not arise from a fixed generic section.

## D. Global squareclass / branched-cover weapons for 14-t

### D1. Generalized Jacobian / Prym explicit descent — NEAR, already imported structurally

**Primary interfaces already used in t17.** Brendan Creutz, *Generalized Jacobians and explicit descents*; Marcucci--Naranjo on Prym varieties of double coverings of elliptic curves; Bruin--Poonen--Stoll on generalized explicit descent.

**Current fit.** t17/t18 have already extracted the correct branch-sensitive squareclass interface and proved that the selected local x-squareclass image is full at every place. Therefore q1 records a negative steering rule: do not spend another literature pass looking for a fixed local prime sieve for this selected branch.

**Missing target.** t19 needs global cancellation / collision-energy control for the moving squareclass-signature packet.

**Promotion.** `NEAR`; structural interface consumed, quantitative family theorem still missing.

### D2. Genus-3 rank-zero / Chabauty tools from PR #185 — NEAR but presently secondary

The PR #185 t-ledger retained genus-3 quotient and rank-zero methods (elliptic quotient strategy, rank-zero hyperelliptic Chabauty, KRZB small-rank uniform bounds). These remain legitimate tools if the t-route returns to explicit individual high-genus lifts, but the present t19 frontier is a family squareclass-collision problem rather than an individual-curve rational-point enumeration.

**Promotion.** `NEAR / secondary`.

## E. Explicit blocked transfers preserved from the old radar

### E1. Function-field Lehmer/canonical-height results — BLOCKED

A lower bound for points over a function field does not directly give the required distribution of least rational points on specialized `Q`-fibers.

### E2. Generic small-point equidistribution — BLOCKED

Equidistribution of algebraic small points on a fixed polarized system is not a theorem on the least rational point per moving elliptic fiber.

### E3. Generic K3 rational-curve existence — BLOCKED for the present task

Existence of infinitely many rational curves over an algebraic closure does not classify `Q`-rational physical curves of fixed `M`-degree or control their physical heights.

### E4. Fixed local squareclass thinning for current t-branch — BLOCKED

t18 proves the selected local x-squareclass image is full at every place. A new fixed-prime local exclusion cannot be advertised as the source of the required global saving without introducing a genuinely different branch condition.

## F. Source-verification notes from q1

The following high-value sources were rechecked against primary or author-hosted records on 2026-08-09:

- Shimada's level-4 modular K3 paper and author computational-data index;
- Petsche's canonical-height paper;
- Naccarato's rational 2-torsion point-counting paper;
- Le Boudec's congruent-number lowest-point paper;
- Zihao Liu's explicit quadratic large-sieve paper, confirming the modern explicit form of the Heath-Brown quadratic large sieve.

q1 does not claim that every theorem in PR #185 has been re-proved or that every old theorem number has been independently audited. Any result promoted to `DIRECT` in a later q-stage must reopen the exact primary-source statement and verify every consumed hypothesis.

## G. Current weapon-to-frontier map

```text
14-4av  <- Heath-Brown/Liu only after correlation decomposition
         <- q2 dispersion / structured bilinear literature search
         <- Shimada package remains standing geometric infrastructure

14-s5i  <- Heath-Brown/Liu separable bound already valid
         <- q2 must attack Euclid-incidence W(u,v)
         <- Petsche/Naccarato and Le Boudec remain alternative height-side weapons

14-t19  <- generalized-Jacobian/Prym interface already consumed
         <- do not retry fixed local thinning
         <- next literature need is global squareclass-signature collision / second-moment control
```

## Decision

There is no forgotten `DIRECT` theorem in PR #185 that instantly closes the present Stage14 bottlenecks. The old radar nevertheless contains three durable weapons: the exact Shimada computational package, the Petsche/Naccarato height pipeline, and the Le Boudec large-prime-factor + complete-2-descent architecture.

The genuinely new common obstacle discovered after PR #185 is the Euclid-correlated bilinear weight. Therefore the correct next literature task is narrowly defined:

```text
NEXT=Stage14-q2 search primary sources for dispersion / structured quadratic-character bilinear estimates that can absorb the actual Euclid-incidence coefficient W(u,v), or prove a precise incompatibility certificate.
```
