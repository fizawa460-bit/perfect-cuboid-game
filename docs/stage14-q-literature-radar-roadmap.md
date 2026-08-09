# Stage14-q — Literature Radar Roadmap

## Purpose

Stage14-q is the recurring literature-surveillance track for Stage14. Its job is not to prove the theorem directly. Its job is to periodically ask whether the current mathematical bottlenecks already have a usable human-developed weapon: a theorem, proof architecture, reduction, computational package, classification, sieve, descent, lattice method, or explicit data set that can be transferred into the active Stage14 tracks.

This track continues the role previously played by PR #185 (`agent/stage14-literature-radar`), but makes the literature radar a named, persistent Stage14 route rather than a one-off search.

## Operating principle

Do not search the literature continuously and broadly. Search when the active proof tracks expose a concrete bottleneck, then perform a focused pass against that bottleneck. A useful Stage14-q result must end in one of four states:

- `DIRECT`: theorem/data can be imported essentially as stated after checking hypotheses.
- `NEAR`: a proof architecture or lemma has a concrete Stage14 transfer test.
- `BACKGROUND`: conceptually relevant but not currently actionable.
- `BLOCKED`: tempting lead fails a named hypothesis or geometry/arithmetic compatibility condition.

Never promote a citation merely because its vocabulary resembles Stage14. Record exact theorem/lemma numbers, hypotheses, variables, losses, field-of-definition conditions, and the precise Stage14 object to which it would be applied.

## Current frontier (2026-08-09, after q2)

The original arbitrary `W(u,v)` obstruction has been reduced substantially by the active proof tracks. `Stage14-s5i` proves a rank-one bulk for pure Euclid divisibility incidence and leaves an explicit centered discrepancy `Delta(u,v)`, primitive Möbius bookkeeping, and sparse large-modulus blocks. `Stage14-4av` proves a bare CRT reciprocal-block power saving and leaves growing auxiliary-state coupling plus endpoint ranges.

Stage14-q2 found no theorem that directly proves the required `L2` dispersion for `Delta`. It did identify two direct subroutines: Heath-Brown/Liu for separated rectangular Jacobi blocks and Cameron Wilson for separated hyperbolic/lopsided Jacobi blocks. The preferred proof order is now centered congruence covariance first, divisor switching for sparse large moduli, and modular-root/spectral escalation only if the norm column survives the elementary dispersion reduction.

The `14-t` track has reached a global missing-face squareclass collision target (`t19 -> t20`), so q4 will later have a concrete collision-energy object to search against. The exact Shimada K3 package remains standing reusable infrastructure.

## Roadmap

### Stage14-q1 — Reconstruct the literature ledger

Recover and normalize the useful results from PR #185 and related literature notes. Build one ledger keyed by active Stage14 bottleneck, with `DIRECT / NEAR / BACKGROUND / BLOCKED`, exact source identifiers, theorem/lemma numbers, hypotheses, and the last date checked. Preserve negative results so later agents do not repeat failed searches.

Deliverable: `docs/stage14-q1-literature-ledger.md`.

### Stage14-q2 — Correlated bilinear / quadratic-large-sieve pass

Target the common `14-4` / `14-s` obstruction. Search specifically for results that tolerate or exploit coefficients `W(u,v)` correlated through Pythagorean/Euclidean parametrization, reciprocal divisors, quadratic characters, or congruence-root structure.

Priority method families:

1. quadratic large sieve with structured coefficients;
2. dispersion method / Linnik-type bilinear decomposition;
3. bilinear forms in quadratic characters and Jacobi symbols;
4. divisor switching and reciprocal-divisor decompositions;
5. low-rank, tensor, Fourier/Mellin, or dyadic separable decompositions of two-variable weights;
6. spectral/Kuznetsov treatments if the correlation can be encoded by Kloosterman-type sums;
7. determinant/incidence methods if the Euclid relation creates sparse algebraic support.

For every promising source, write the exact model sum and compare it line-by-line with the Stage14 sum. The pass succeeds only if it either produces a legitimate transfer lemma or a precise incompatibility certificate.

Result: `docs/stage14-q2-correlated-bilinear-literature.md`.

### Stage14-q3 — Small-point / first-point height pass

Refresh the `14-s` Petsche / Naccarato / Le Boudec line. Test the actual Stage14 discriminant, minimal discriminant, conductor, Szpiro ratio, and 2-descent data rather than citing generic elliptic-curve height bounds. Determine whether a lower bound for the first non-torsion physical point survives uniformly or for density-one Pythagorean fibers.

Deliverable: a transfer table listing each required hypothesis and whether Stage14 satisfies it.

### Stage14-q4 — Squareclass / Selmer collision pass

When `14-t` has an explicit global squareclass-signature collision statement, search for a theorem architecture in Selmer groups, squareclass sieves, thin sets, Hilbert irreducibility, square-value problems, branched covers, Prym/generalized Jacobian methods, or arithmetic statistics that matches the exact signature map.

Do not restart generic local-obstruction searches if the local images are already known to be full.

### Stage14-q5 — K3 / lattice computational refresh

Audit whether the Shimada computational package has been fully consumed by `14-4`. If the remaining obstruction is still geometric, search only for exact lattice/automorphism/Galois tools that close a named gap: identification of the physical class `M`, effective `(-2)`-curve enumeration, rational descent, orbit reduction, or bisection classification.

Avoid broad K3 literature once the exact level-4 modular K3 data already supplies the needed object.

### Stage14-q6 — Cross-track weapon test

Compare all `DIRECT` and `NEAR` weapons against the current frontiers of `14-4`, `14-s`, `14-t`, and numerical/fingerprint tracks. A method discovered for one route may transfer to another. Record explicit handoffs with the target stage name and the minimal lemma/computation the receiving track should attempt next.

### Stage14-q7 — Negative-results archive

Maintain a compact archive of attractive but invalid transfers: wrong height, wrong field, fixed-twist versus non-isotrivial family, independent versus correlated coefficients, geometric existence versus `Q`-rational classification, local obstruction versus global collision, etc. This is part of the result, not failed work.

### Stage14-q8+ — Periodic focused radar passes

After q1–q7, do not manufacture a fixed endless sequence. Open the next q-stage only when an active Stage14 route reports a stable named obstruction or when a materially new paper/data set appears. Each new pass must state at its top:

- `TRIGGER_STAGE`
- `EXACT_OBSTRUCTION`
- `SEARCH_FAMILIES`
- `LAST_RADAR_BASELINE`
- `PROMOTION_STANDARD`

This keeps literature work coupled to the proof rather than becoming an unbounded bibliography project.

## Handoff discipline

A Stage14-q worker may recommend a theorem or method but must not silently modify another track's proof contract. Every handoff must include:

1. source and exact theorem/lemma/data object;
2. Stage14 variable dictionary;
3. verified hypotheses;
4. unverified hypotheses;
5. quantitative loss/exponent/constants that matter;
6. the smallest receiving-stage experiment or lemma that can falsify the transfer quickly.

If any critical hypothesis is unknown, classify the lead as `NEAR`, not `DIRECT`.

## Immediate next task

Start **Stage14-q3**: refresh the Petsche / Naccarato / Le Boudec first-small-point line against the actual Stage14 minimal discriminant, conductor, Szpiro ratio, and complete 2-descent data. Keep the q2 handoff active in `Stage14-s5j` and `Stage14-4aw`; do not reopen a generic correlated-bilinear literature search unless those stages expose a new named obstruction.
