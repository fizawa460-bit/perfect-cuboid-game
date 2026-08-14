# Stage24-10 discovery ledger

DISCOVERY_CHECKPOINT=10
DISCOVERY_LEDGER_STATUS=COMPLETE
EXPLORATION_PHASE=FULL_TRANSITION_RESEARCH
FORMULA_SUBSTITUTION_ONLY=false

## Search scope actually opened

- `docs/stage16-28-population-roadmap.md`
- `docs/stage21-28-exploration-policy.md`
- `stages/stage18/final.md`
- `stages/stage18/18-controller.json`
- `stages/stage19/final.md`
- `stages/stage19/19-controller.json`
- `stages/stage16s/final.md`
- `stages/stage21/final.md` as a comparison candidate whose current audit status must be rechecked before theorem use
- `stages/stage22/22-controller.json`
- Stage23 audited checkpoint60 interface from main, as the complementary `17 -> 19` comparison

SEARCH_TERMS=Stage24; Stage18->Stage19; exactly-two; space diagonal; integral R; squareclass; sf(A)=sf(B); split-prime parity; half-power; lower bound; unbounded family; interaction; independence; Stage16S; Stage21; Stage22; Stage23
STRUCTURAL_SIGNATURES=shared-edge double Pythagorean host; E^2+X^2+Y^2=4AB; A=m^2r^2+n^2s^2; B=m^2s^2+n^2r^2; sf(A)=sf(B); R integral; split-prime valuation parity; N2(B)<<B^(1/2+epsilon)
DEPENDENCY_NEIGHBORS=Stage14 upper theorem; Stage15 two-face/squareclass machinery; Stage16S intrinsic space baseline; Stage21 one-face-space transition candidate; Stage22 second-face/no-space transition; Stage23 second-face/already-space transition

## Candidate map

### C10-01 — Stage18 exact source law
ACCEPTED.

Population: primitive canonical `0<a<b<c`, `gcd=1`, `R<=B`, exactly two integral faces, no space requirement.

Frozen law:

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

No adapter is needed for Stage24 source use.

### C10-02 — Stage19 literal target interface
ACCEPTED.

Stage19 uses the identical physical population/cutoff and adds only `R in Z`. Therefore

\[
\mathcal A_2(B)=\mathcal B_2(B)\cap\{R\in\mathbf Z\}.
\]

This is a literal subset transition, so `N2/M2` is an actual matched survivor ratio.

### C10-03 — Stage19 quantitative upper theorem
ACCEPTED AS UPPER-ONLY.

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

It must not be promoted to a true exponent or an asymptotic. Stage24 checkpoint40 is explicitly required to re-attack strict sub-square-root improvement and the causal status of the half-power ceiling.

### C10-04 — Stage19 lower frontier
ACCEPTED AS CURRENT CERTIFIED FLOOR ONLY.

\[
N_2(B)\ge3495\qquad(B\ge500,000,000).
\]

Unboundedness, every fixed positive-power lower bound, matching half-power lower bound and a target asymptotic remain open. Stage24 checkpoint50 is required to reopen bounded lower/construction research rather than merely repeat the old OPEN_GATE.

### C10-05 — exact Stage15/19 squareclass predicate
ACCEPTED.

On the positive shared-edge toric host,

\[
R\in\mathbf Z\iff AB\in\square\iff \operatorname{sf}(A)=\operatorname{sf}(B),
\]

with

\[
A=m^2r^2+n^2s^2,\qquad B=m^2s^2+n^2r^2.
\]

This is the exact new Stage24 predicate, not a heuristic probability model.

### C10-06 — same-measure split-prime parity sieve
ACCEPTED AS QUALITATIVE ZERO-DENSITY MECHANISM.

For fixed finite good split-prime sets, Stage19 has local acceptance factors with

\[
1-\rho_p=4/p+O(p^{-2}),
\]

and the fixed-set-then-limit quantifier order proves `N2/M2 -> 0`.

This does not currently yield the half-power rate because no growing-prime uniformity theorem is certified. Stage24 checkpoint40/60 must keep these theorem species separate.

### C10-07 — Stage16S intrinsic ambient space baseline
ACCEPTED FOR LATER COMPARISON.

The ambient primitive/canonical space condition has intrinsic ratio of order `B^-1` with explicit constant. This is the control needed to ask whether imposing space after two integral faces is enhanced, suppressed or correlated relative to the ambient condition.

### C10-08 — Stage21 one-face-space comparison
CANDIDATE_PENDING_CURRENT_AUDIT_STATUS_CHECK.

The available Stage21 final candidate states an exactly-one-face to exactly-one-plus-space transition with a `B^-1 (log B)^2` profile and comparison to Stage16S. Stage24 may use it only after verifying its final audit state at the relevant checkpoint60 interaction analysis.

### C10-09 — Stage22 second-face/no-space transition
ACCEPTED AS COMPARISON-LATTICE INPUT.

Stage22 compares Stage16 -> Stage18. It is not a literal subset transition because exactly-one and exactly-two strata are disjoint, but it provides the cost of adding the second-face condition without space already imposed.

### C10-10 — Stage23 second-face/already-space transition
ACCEPTED AT ITS AUDITED CHECKPOINT60 SCOPE.

Stage23 compares Stage17 -> Stage19 and proves zero density for the second-face addition inside an already-space-integral host. It also revalidated historical attacks and globally excludes one strong Stage18 explicit family from Stage19 by a mod-16 obstruction. This is a dependency neighbor for Stage24 construction work, not a substitute for Stage24's own lower search.

## Comparison lattice frozen at checkpoint10

```text
ambient U
  | +space                 | +one face
  v                        v
Stage16S                 Stage16
                           | +space        | +second face
                           v               v
                         Stage17         Stage18
                           | +second face   | +space
                           v               v
                              Stage19
```

Stage24 owns the bottom horizontal/vertical interaction question in the roadmap: with exactly two faces already paid, what is the additional cost of imposing `R integral`, and how does that compare with the ambient and one-face space costs?

## Mandatory future attack map

Checkpoint30: derive the first legal ratio law but do not treat quotienting frozen formulas as stage completion. Search constants, directional refinements and independent proof routes.

Checkpoint40: reopen the upper side at source level. Fresh Stage19 surgeon first; strict sub-square-root search; moving Jacobi/Kummer receiver boundary; growing-modulus local-sieve uniformity; no attribution of the half-power rate to a mechanism without a proof.

Checkpoint50: fresh lower surgeon first. Test explicit Stage18 families for space lift, generate new Stage19-compatible candidates, seek unbounded primitive families and fixed positive-power lower bounds. If negative, at least four fresh candidates must be materialized and high-value historical dead branches revalidated source-level before an absence-style claim.

Checkpoint60: compare Stage16S, audited Stage21, Stage22 and Stage23; classify enhancement/suppression/correlation and run a strict no-double-charge audit.

## Discovery-audit trigger

DISCOVERY_AUDIT_REQUIRED=false at checkpoint10 because this submission freezes exact source/target contracts and a candidate map only. It does not assert a new `BEST_*`, `NO_KNOWN_*`, exhaustive rejection claim, or new OPEN_GATE.
