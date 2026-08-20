# Stage27-19 — StructureRadar full-classification rematch to r402h

```text
TASK_ID=Stage27-19-StructureRadar-r402h-rematch
BASE_MAIN=9fbb1bd3ca6796016aaac287a6f62371d80ff1c4
CHECKPOINT=40
CURRENT_MU=1/2
SOURCE_CORPUS=docs/structure-radar/structure-registry.json + Arsenal24/25 + post-Arsenal cards
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Receiver being rematched

After r6d and r402g-h, fixed `(p,q,g)` representation multiplicity is only `B^{o(1)}`.  The live upper problem is therefore the same-physical-measure support of

\[
A=s^2(m^2+n^2),\qquad D=n^2(r^2-s^2),\qquad A,D<2B^2,
\]

with

\[
g=\gcd(A,D),\qquad (p,q)=(A/g,D/g),
\]

and, uniformly on every dyadic band

\[
T\le H(p/q)<2T,
\]

a sufficient target

\[
\boxed{\#\mathcal P_T(B)\ll B^{1/2-\delta+o(1)}}
\]

for one fixed `delta>0`, retaining all Stage19 primitive/canonical/exactly-two physical masks.  Equivalently an on-measure weighted energy theorem strong enough for the frozen r402f hybrid bound is acceptable.

The rematch uses the StructureRadar rule that a changed receiver/measure is a distinct applicability profile.  Therefore prior `FAIL`/`EXTERNAL_GATE` verdicts are not blindly inherited when r6d has removed a former polynomial multiplicity/weight obstruction.

## 2. Rematch verdict scale

- `GREEN_DIRECT`: an existing classified theorem/weapon already supplies the required fixed-power estimate after a proved adapter.
- `GREEN_STRUCTURAL`: exact reusable receiver/adapter, but no fixed-power theorem by itself.
- `AMBER_STRONG`: existing arsenal theorem species is close and the new r402h receiver materially weakens an old obstruction; one explicit repo-native adapter could make it legal.
- `AMBER_WEAK`: related theorem species but multiple nontrivial adapters remain.
- `RED`: wrong population/measure, duplicate already-paid condition, only logarithmic/subpower information, or an already-audited no-go for this receiver.

No `GREEN_DIRECT` card is identified in the current classified corpus.

## 3. Highest-priority rematches

### SR-STR-166 — `AMBER_STRONG` — first choice

StructureRadar classifies the dual-root-line eliminant dichotomy as `ACTIVE`: derive a charged-once eliminant first; if a genuinely new determinant/hyperdeterminant factor appears, Reuss-type determinant/lattice counting is legal, while an exact zero-loss inverse-fraction transform allows Bettin-Chandee / Dong-Robles-Zeindler type bounds.

This is now the closest match to r402h because the live target is literally a coupled two-form image/support problem.  The old r402h stop said “determinant/incidence theorem required” but did not perform the StructureRadar-mandated **eliminant preflight**.

Exact missing adapter:

```text
R402H_ELIMINANT_ADAPTER:
On the original Stage19 physical variables and one dyadic (T,g) packet, eliminate the already-charged reconstruction variables from
A=s^2(m^2+n^2), D=n^2(r^2-s^2)
and the retained space-diagonal/physical identities, producing an irreducible bilinear/trilinear hypersurface relation whose determinant/hyperdeterminant is not an already-paid Stage14/15 spacing factor.  Prove the map to physical (A,D) support has B^o(1) fibers and compatible height boxes.
```

If such a new factor exists, the classified determinant/lattice weapon becomes legally testable.  If the eliminant collapses to the known squareclass/common-core relations, this route is RED by double-charge and freezes immediately.

```text
SR166_R402H_REOPEN=true
SR166_DIRECT_POWER_PROVED=false
NEXT_PRECHECK=R402H_CHARGED_ONCE_ELIMINANT_AND_DETERMINANT_NOVELTY
```

### SR-STR-169 — `AMBER_STRONG` — receiver-change reopen

SR-STR-169 is an `EXTERNAL_GATE` for same-measure signed physical-selector correlation.  Its focused Work search failed on the old Stage14 `H_phys^MAIN` receiver because the theorem had to preserve correlated modulus/common-parent allocations and arbitrary sparse physical weights simultaneously.

The r402h receiver is materially different: r6d proves every fixed `(p,q,g)` core has only `B^{o(1)}` physical representations.  Hence one former polynomial-weight/multiplicity obstruction has disappeared.  This satisfies the StructureRadar pause policy's explicit reopen condition “Stage27 changes the receiver so an existing theorem may become legally applicable.”

Exact missing adapter:

```text
R402H_CORRELATION_ADAPTER:
Rewrite the dyadic realized-(A,D) indicator or its second moment as a signed/bilinear correlation with coefficients indexed by realized cores, showing all pushforward weights are B^o(1) and that no Stage14/15 spacing or squareclass saving is recharged.  Then compare the resulting coefficient/modulus ranges with the already-classified multivariable/Kloosterman/dispersion theorem species in SR-STR-169.
```

This is not a direct theorem import yet, but the old global `WORK_RESULT=FAIL` cannot be used as a blanket RED verdict for the new receiver.

```text
SR169_R402H_REOPEN=true
OLD_WORK_FAIL_AUTOMATICALLY_BINDING=false
SR169_DIRECT_POWER_PROVED=false
```

### SR-STR-161 — `AMBER_STRONG` — separated quadratic/Jacobi route

SR-STR-161 is `ACTIVE`: after **genuine one-variable coefficient separation**, Heath-Brown/Liu quadratic large-sieve and Wilson rectangular/hyperbolic machinery are reusable.  It explicitly forbids applying these bounds to an arbitrary correlated matrix `W(u,v)`.

For r402h the forms share `n,s`, so separation is not currently proved.  However r6d removes fixed-core representation entropy, making a separation attempt on fixed `(p,q,g)` or dyadic `(T,g)` packets much cleaner than in the old Stage14 host.

Exact missing adapter:

```text
R402H_ONE_VARIABLE_SEPARATION:
After fixing the charged core data, express the realized-support indicator/energy as B^o(1) separated quadratic-character blocks (or prove an L2/covariance reduction to such blocks), with physical masks and dyadic T quantifiers retained.
```

If this succeeds, the pre-classified large-sieve package may be applied without a new broad literature search.

## 4. Structural GREENs that validate the receiver but do not save a power

### SR-STR-173 — `GREEN_STRUCTURAL`

The conditioned support hierarchy says existential support must be controlled on the same charged measure, and its first/second witness moments are the legal route from multiplicity to support.  This exactly supports r402g-h's move from raw representation multiplicity to same-measure realized `(A,D)` support/energy.

It does **not** itself prove a fixed-power deficit.  Its value is that the r402h receiver is correctly normalized and that ambient divisor averages cannot substitute for the required physical support theorem.

### SR-STR-166 — structural portion also GREEN

The “derive eliminant first and test determinant novelty before importing determinant/Kloosterman machinery” rule is already a legal structural router.  Only its quantitative branch remains AMBER pending the preflight above.

## 5. Relevant but currently non-opening cards

### SR-STR-164 — `RED_CURRENT`

Square/polynomial-sieve collision covers are active in general, but r6b proved that the occupied-R squareclass collision is exactly the already-frozen Stage15 squareclass predicate.  Reusing that square-lift as a fresh r402h saving would double-charge the same arithmetic condition.  Reopen only if the eliminant preflight produces a genuinely **new** nonsquare polynomial cover independent of the Stage15 predicate.

### SR-STR-165 — `AMBER_WEAK`

Gaussian Hecke large-sieve technology is powerful after one-ideal coefficient separation, but r402h is presently an integer `(A,D)` support problem and no new one-ideal character decomposition has been proved.  It remains secondary to SR-STR-161/166.

### SR-STR-168 — `RED_CURRENT`

The weighted Gaussian norm-ratio collision gate is structurally adjacent, but the r6 occupied-R exploration already reduced its new squareclass content to an old Stage15 predicate and found only logarithmic split-prime support.  No polynomial Gaussian modulus/sample family retaining the r402h measure has appeared.

### SR-STR-170 / SR-STR-171 — `RED_CURRENT`

Divisor-in-an-interval and unitary-divisor shadows cannot supply a new saving here.  r402h proved `(tau,g)` is merely the gcd decomposition of `(A,D)`; another divisor/core decomposition is a reparameterization unless it adds a genuinely new coupled-form restriction.

### SR-STR-172 — `RED_AS_POSITIVE_WEAPON`

The rectangular AP product-set theorem is a useful **negative certificate**: multiplicative collisions in its exact ambient rectangle lose only polylogarithmic factors.  It does not yield the desired fixed-power support deficit on the sparse Stage19 physical subset.

### SR-STR-174 — `RED_CURRENT`

Its filtered `tau_3` intersection theorem gate is tied to a different deterministic pushforward/filter pair.  The same-measure philosophy is relevant, but no exact dictionary to the r402h `(A,D)` forms exists.

### SR-STR-216 — `RED_POPULATION`

The Peyre-Tamagawa constant is for primitive exactly-two **without** the space-diagonal filter.  StructureRadar explicitly forbids promotion to the N2 space-diagonal-filtered population without additional toric equidistribution/thin-set transfer.

### SR-STR-222 — `RED_RECEIVER`

The super-Kai Gaussian prime sector/ray-character gate concerns an individual prime-occupancy receiver, not the current coupled-form `(A,D)` support.  No direct adapter is present.

### SR-STR-223 — `RED_RECEIVER`

The Humbert-Edge moving small-point family is a different elliptic/fiber-product receiver.  Fixed-fiber geometry is not a family support theorem for r402h.

### SR-STR-224 — `RED_ALREADY_CONSUMED`

This is exactly the fixed-R hyperbolic-boundary/outer-support barrier already consumed by r5/r6.  r6 is its post-StructureRadar continuation and found no fixed-power occupied-R deficit.  Reopening it would loop.

### SR-STR-225 — `RED_RECEIVER`

The signed fixed-U Kummer/Rayleigh receiver is tied to the Stage14 fixed-U Kummer packet.  No exact zero-loss map from r402h realized `(A,D)` support to that signed matrix is proved.

## 6. Arsenal24/25 terminal classification coverage

All terminal Arsenal decisions were explicitly rematched rather than only keyword-matching the three preferred cards.

- `076,154`: RED/PARKED finite regression only.
- `161`: AMBER_STRONG.
- `162`: RED_RECEIVER (thin-Pythagorean first-small-point family, not the present support image).
- `163`: RED/LOWER_STRUCTURAL for r402h; descent interface may matter only if a new lower/cover route is opened.
- `164`: RED_CURRENT duplicate squareclass unless a new cover emerges.
- `165`: AMBER_WEAK.
- `166`: AMBER_STRONG + GREEN_STRUCTURAL.
- `167`: AMBER_WEAK at best; requires B^o(1)-complexity multiplicative selector decomposition not presently derived.
- `168`: RED_CURRENT.
- `169`: AMBER_STRONG because receiver changed after r6d.
- `170,171`: RED_CURRENT reparameterization/transfer wall.
- `172`: RED_AS_POSITIVE_WEAPON / useful no-go certificate.
- `173`: GREEN_STRUCTURAL.
- `174`: RED_CURRENT.
- `216`: RED_POPULATION.
- `222,223`: RED_RECEIVER.

Stage26 backflow `S26-W01/W02/W03` is also RED for the r402h upper receiver because it lives on the Euler-cuboid/no-space-diagonal or adjacent-stratum populations and StructureRadar explicitly forbids transfer to `N2` without an adapter.

## 7. Decision

The earlier route-arbitration statement “new theorem input required” was directionally correct but **too coarse**.  StructureRadar already contains three pre-classified theorem species worth a repo-native adapter attack before declaring Stage19 externally stalled.

Priority:

1. **SR-STR-166 eliminant/determinant-novelty preflight** — cheapest and most decisive.  This is algebraic and can be attempted inside Stage27 immediately.
2. **SR-STR-169 new-receiver correlation adapter** — only if (1) does not produce a determinant weapon.  The r6d multiplicity theorem means the old Work failure must be re-tested against the new coefficient measure, not copied verbatim.
3. **SR-STR-161 one-variable separation** — parallel/alternate analytic adapter; if separation is proved, existing searched large-sieve machinery becomes available.

No broad new literature search is needed before these three adapter tests; the relevant theorem species are already in the StructureRadar corpus.

```text
STRUCTURE_RADAR_FULL_CLASSIFICATION_REMATCHED=true
DIRECT_GREEN_FIXED_POWER_THEOREM_FOUND=false
GREEN_STRUCTURAL=SR-STR-173,SR-STR-166-router
AMBER_STRONG=SR-STR-166,SR-STR-169,SR-STR-161
AMBER_WEAK=SR-STR-165,SR-STR-167
R402H_THEOREM_GATE_REOPENED_FOR_ADAPTER_TEST=true
FIRST_NEXT_ROUTE=Stage27-19-r7a_SR166_ELIMINANT_DETERMINANT_PREFLIGHT
BROAD_EXTERNAL_SEARCH_REQUIRED_BEFORE_R7A=false
CURRENT_MU=1/2
ADVANCE_TO_CHECKPOINT50=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-19-StructureRadar-rematch-audit
```
