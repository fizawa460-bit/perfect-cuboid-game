# Stage32 MB104 — Class-3 hypothesis roadmap — 2026-09-18

Status: **ROADMAP ONLY / FOUR HYPOTHESES / NO MATHEMATICAL CREDIT**

## Purpose

MB104 should no longer advance by choosing the next technically available
calculation. Each run must first test whether a proposed route can close the
whole MB104 obligation.

The exact success target remains one of:

1. exclude the exact balanced dangerous ray for every `l >= 1`; or
2. exclude it uniformly for `l > L`, with an explicit finite and exact backend
   for `1 <= l <= L`.

A calculation on one mask, one prime, one local lift, or finitely many values
of `l` is evidence only. It closes MB104 only after the forward adapter,
uniform theorem, reverse adapter, and any finite backend are all proved.

## What every successful proof must contain

Every route must supply all four blocks below.

| Block | Required statement |
|---|---|
| F — forward adapter | Every hypothetical integral genus-one MB104 carrier, for every surviving orbit and allowed `e`, produces the exact object used by the route. |
| U — uniform engine | The route excludes all `l >= 1`, or gives an explicit effective bound `l <= L`. |
| R — reverse adapter | The route's vanishing, invariance, nilpotence, or classification conclusion really contradicts the original carrier; no formal-class/existence substitution is allowed. |
| B — bounded backend | If U leaves `1 <= l <= L`, every surviving orbit and allowed `e` is checked by an exact certificate. |

Failure of F or R is a route failure, not a request for a deeper computation.

## Known numerical pressure

For `D_l = 7lH - 4l sum_{p in Sigma} E_p`, the retained calculation gives

```text
chi(O_S(D_l)) = 168l^2 - 56l + 8,
delta_required = 168l^2 + 56l.
```

After cancellation the apparent pressure is `112l - 8`. This does **not**
itself prove nonexistence: the archived equigeneric/conductor computation
exhibits superabundance of size `112l`. Any route that merely repackages the
same expected-dimension subtraction is to be stopped.

## Portfolio

### H1 — symmetry-amplified translate overlap

**Hypothesis.** For every carrier `C`, some automorphism outside the support
stabilizer makes the packet force
`I(C,gC) > D_l . gD_l` unless `C = gC`. Invariance would then descend to a
marked elliptic normalization, whose finite-order automorphisms are
incompatible with the two typed degree-`56l` divisors and saturated-fibre
passport.

**Why it could close MB104.** The intersection comparison is quadratic and
uniform in `l`; the remaining elliptic automorphism types are finite
(translation or orders 2, 3, 4, 6).

**First shallow gate.** Over all relevant `Aut(S)` double cosets outside the
support stabilizer, compute only scheme-theoretic local multiplicity lower
bounds that do not use residual sheet signs or unnamed tangent labels. Compare
their `l^2` coefficient with the exact cross-class intersection.

**Promote when.** At least one double coset reaches or exceeds the exact
intersection for every surviving support orbit, using source-valid packet
data. Equality cases may receive one tangent-character refinement.

**Stop when.** Every translate has a fixed quadratic deficit; the comparison
needs the archived conductor-sheet labels; or invariant elliptic passports
form an unbounded scalable family.

**Depth cap.** One finite group/double-coset preflight, then at most one
elliptic-classification leaf.

### H2 — graded incidence / finite-generation reduction

**Hypothesis.** The exact packet and geometric-genus-one condition define a
saturated graded incidence module `M_Sigma` over the section/Cox ring
`R = direct_sum_l H^0(S,O_S(D_l))`, and `M_Sigma` is finite length (strongly,
zero). Equivalently, a finite regularity or nilpotence certificate reduces all
`l` to finitely many degrees.

**Why it could close MB104.** An actual carrier gives a nonzero homogeneous
class in `M_{Sigma,l}`; finite length gives an explicit `L`, after which an
exact bounded backend handles the remainder. This is the clearest route from
an infinite ray to finite verification.

**First shallow gate.** Do not compute large degrees. First prove or refute
that normalization, integrality, geometric genus one, the balanced packet, and
the passport can be encoded scheme-theoretically (for example by incidence,
Fitting/discriminant, and saturation conditions) with both F and R adapters.

**Second gate only after the first passes.** Compute degrees `l=1,2`, and only
if needed `3`: initial Hilbert values, multiplication closure, minimal
generators, and equivariant pieces.

**Promote when.** The exact incidence is Noetherian and source-complete, and
the truncated Hilbert data is compatible with zero-dimensional support or a
provable regularity bound.

**Stop when.** The incidence has positive-degree support/positive Hilbert
polynomial; a non-torsion class survives multiplication; new generators grow
as a genuine section ring; or the genus-one condition cannot be encoded with
a reverse adapter.

**Depth cap.** One adapter-design run, one `l=1,2` run, one optional
`l=3`/regularity run.

### H3 — packet-specific equisingular rank slope

**Hypothesis.** After parameter motion and the known `h^1` superabundance are
included exactly, the *actual* packet-imposed tangent codimension still
eventually exceeds the section dimension. Equivalently, the packet defines
universal schemes `Z_{P,l}` for which
`H^0(S,O_S(D_l) tensor I_{Z_{P,l}})=0` for `l > L`, with a finite backend
below `L`.

**Why it could close MB104.** It attacks carrier nonexistence directly and
could turn the residual linear `112l - 8` pressure into a theorem.

**First shallow gate.** Audit the exact parameter freedom before any rank
calculation: fixed/finite, `O(l)`, or `Theta(l^2)`. Then evaluate the exact
tangent/jet matrix only at `l=1`, and `l=2` only if the first result is
informative, across all representative surviving masks.

**Promote when.** Moving parameters cost `cl` with a justified `c < 112`, the
rank deficit does not consume the linear margin, and a multiplication or
regularity theorem can plausibly make the estimate uniform.

**Stop when.** Motion is `Theta(l^2)`; no source-valid universal ideal exists;
rank loss is at least `112l`; or the argument collapses to the archived naive
Severi/conductor count.

**Depth cap.** One freedom audit and one small-degree rank experiment. H3
cannot become DEEP unless H2's exact incidence adapter has already passed.

### H4 — infinite-family forces global geometry

**Hypothesis.** Carriers for unbounded `l` cannot remain unrelated isolated
sections: finite generation or bounded-genus geometry forces a fixed
component, a positive-dimensional subsystem, or a genus-one fibration. The
forced global object is then incompatible with the retained intersection and
packet data.

**Why it could close MB104.** A contradiction for any unbounded sequence
would yield `l <= L`, leaving a finite backend, without classifying each degree
separately.

**First shallow gate.** Prove or refute the compactness/specialization bridge:
does the existence of carriers for infinitely many `l` actually produce one
fixed geometric structure? No fibration calculation begins before that
implication is established.

**Promote when.** A precise theorem turns an unbounded carrier sequence into a
fixed component, finitely generated subsystem, bounded Chow/Hilbert stratum,
or fibration with explicit packet inheritance.

**Stop when.** The carriers may occupy infinitely many isolated graded
pieces; packet data is lost under specialization; or the route reduces to the
already-rejected generic fibration/bounded-genus argument.

**Depth cap.** One theorem-source/derivation gate, then one numerical
contradiction gate.

## Initial portfolio score

Each axis is scored 0–3. “Adapter” means closeness to a complete F/R bridge;
“anti-tunnel” means ability to remain shallow and globally relevant.

| Route | closure | coverage | adapter | cheap test | reuse | anti-tunnel | total | initial state |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| H1 symmetry overlap | 2 | 2 | 1 | 3 | 2 | 3 | 13 | ACTIVE preflight |
| H2 graded incidence | 3 | 3 | 1 | 2 | 3 | 3 | 15 | ACTIVE adapter gate |
| H3 rank slope | 2 | 2 | 1 | 3 | 2 | 2 | 12 | CONDITIONAL on H2 adapter |
| H4 global geometry | 3 | 3 | 0 | 2 | 3 | 3 | 14 | PREFLIGHT |

Scores rank experiments; they are not evidence for a theorem.

## Run protocol

One invocation of `stage32mb-mainbatch` performs **one shallow gate**, not an
open-ended proof search.

Per run:

- one primary hypothesis;
- at most one new load-bearing lemma;
- `l=1,2` only, with `l=3` permitted solely by a recorded promotion gate;
- at most one individual mask or prime as a diagnostic, never as closure;
- no heavy workflow until an explicit finite certificate target and storage
  estimate exist;
- end with `PASS`, `FAIL`, or `HOLD`, never an inflated theorem claim.

A route becomes a DEEP candidate only when closure and coverage are each at
least 2, its shallow gate passes, and its total score is at least 12. Only one
route may be DEEP at a time. The same missing premise producing two HOLDs parks
the route. A counterexample or quantifier failure rejects it.

Every three runs, return to the top level and rescore the full portfolio.

Each run must record:

```text
route_id / hypothesis
exact_MB104_target
covered_l / covered_orbits / covered_e
forward_adapter
uniform_engine
reverse_adapter
bounded_backend
one_turn_gate
evidence_and_counterevidence
PASS | FAIL | HOLD
strongest_safe_claim
missing_lemma
score_before / score_after
depth_count
next_action
revisit_condition
```

## Recommended first cycle

1. **Run 1 — H1 translate-overlap preflight.** It is the cheapest genuinely
   different kill-test. If no double coset reaches the intersection budget,
   reject H1 immediately.
2. **Run 2 — H2 exact-incidence adapter gate.** Decide whether the nonlinear
   genus-one and packet conditions admit a saturated graded object with both
   adapters. Do not compute Hilbert functions until this passes.
3. **Run 3 — H4 infinite-family bridge gate.** Decide whether “unbounded `l`”
   forces a fixed global geometry. Reject it if this is only the old fibration
   route in new language.
4. **Portfolio review.** If H2 passed, choose between H2 finite-generation and
   the conditional H3 rank test. If none passed, record a genuine theorem
   block rather than opening a fifth lateral tunnel.

## Archived-route firewall

Until a materially new adapter is proved, keep these parked:

- conductor residual-sheet recovery and sign enumeration;
- ambient `H^1`, Picard torsion, or integrality as sole obstruction;
- U12 spin/`P^6`, isolated `p=167`, or unnamed dyadic marking;
- fixed finite-cover compression;
- counting-only Riemann–Hurwitz, Bezout, Severi, or jet recombinations;
- generic fibration/foliation/web and ordinary effectivity searches.

H1 must stop before residual-sheet labels. H3 must stop if it reproduces the
`112l` superabundance wall. H4 must stop before generic fibration analysis
unless its infinite-family bridge has first been proved.

## Credit firewall

This roadmap proves no exclusion, no finite degree window, and no MB104
closure. A passed shallow gate authorizes only the next stated gate.

```text
MB104_complete=false
all_l_exclusion_proved=false
finite_degree_window_proved=false
theorem_credit=false
effectivity_credit=false
receiver_credit=false
endpoint_credit=false
merge_authorized=false
```


## Cycle 1 disposition after H1 / H2 / H4

The first three shallow runs are complete.

| Route | shallow result | disposition |
|---|---|---|
| H1 symmetry overlap | FAIL | PARKED; non-stabilizer translates retain a positive quadratic cross-intersection deficit. |
| H2 graded incidence | FAIL | PARKED; exact carrier semantics are not preserved by section-ring multiplication, so the proposed graded-module F/R adapter fails. |
| H3 rank slope | NOT RELEASED | Remains conditional on an exact incidence adapter; H2 did not supply one. |
| H4 infinite-family global geometry | FAIL | PARKED; the classes have unbounded Hilbert/Chow data, the carriers are degreewise equigenerically rigid, and no flat-family/fixed-fibration bridge is forced by the retained data. |

Cycle-1 conclusion: none of H1--H4 is a DEEP candidate. Do not deepen H3 merely because H1/H2/H4 are parked.

### Cycle 2 candidate routes

These are hypotheses only; they receive no credit until their own shallow gates pass.

#### H5 — exact etale-correspondence quotient rigidity

Use the retained Beauville equality geometry only after an exact carrier reaches it. Test whether the equal-bidegree etale correspondence in the fixed product cover, together with the fixed quotient action and supported-node type data, has a finite or explicitly bounded equivariant classification. The shallow gate is an F/R classification adapter, not a generic correspondence-degree bound.

Stop if the correspondence problem admits scalable families with the required quotient semantics or if the packet cannot be transported to the product cover without the parked conductor-sheet data.

#### H6 — finite monodromy / Nielsen-passport obstruction

Encode the supported branch packet in the fixed modular quotient as an exact permutation/monodromy problem. The shallow gate is to prove that every hypothetical carrier supplies a source-complete Nielsen datum and that every datum accepted by the finite problem reconstructs the required carrier-level packet. Do not reuse the retracted per-branch-value divisibility assumption.

Stop if branch-to-fixed-point concentration is again required, if the number of branch points or cycle data grows freely with l, or if the reverse adapter loses the carrier semantics.

#### H8 — logarithmic boundary inequality

The retained ordinary one-curve Miyaoka inequality leaves the ray open. Test a genuinely different log/orbifold pair using the fourteen supported exceptional curves and the exact balanced contact data. The shallow gate is symbolic: derive the exact l-dependent log Chern/intersection expression and check whether its leading coefficient can ever have the sign needed for an all-l or large-l exclusion.

Stop before any heavy computation if the log inequality reproduces the already-satisfied ordinary BMY polynomial, if admissibility of the boundary coefficients fails, or if the packet contacts cannot enter the theorem with an exact F/R adapter.

Initial cycle-2 order is H8, then H5, then H6. This order may be changed only by a new source-complete theorem or an operational cross-lane demand.


### Cycle 2 run 1 disposition — H8

H8 logarithmic-boundary inequality: **FAIL / PARKED**.

The exact exceptional-boundary calculation admits a retained-data-compatible formal witness in which the full off-exceptional defect `168l^2+56l` is assigned to ordinary nodes. For boundary

```
B=aC+sum_i b_i E_i,
0<=a,b_i<=1,
```

the orbifold-BMY slack of this witness satisfies

```
3 e_orb(S,B) - (K_S+B)^2 >= 147
```

for every `l>=1` and every choice of the fourteen exceptional weights. Thus the exact `8l` contacts on the supported exceptional curves do not by themselves yield a quadratic log-BMY obstruction. H8 may be reopened only with a new theorem forcing the off-exceptional analytic singularity types or stronger local orbifold data.

Cycle-2 routing now advances to **H5 exact etale-correspondence quotient rigidity**. H6 remains queued after H5.


### Cycle 2 run 2 disposition — H5

H5 exact etale-correspondence quotient rigidity: **FAIL / PARKED**.

The retained equality geometry does provide a bare equal-degree finite etale self-correspondence of `C8` from any actual balanced carrier. That is not enough for a finite reduction.

Two independent blockers were recorded:

1. `C8=X(8)` is the Wiman genus-five curve, whose full automorphism quotient has signature `(2,3,8)`; this triangle group is arithmetic. The corresponding compact surface group therefore has dense commensurator, so finite etale self-correspondences of the fixed target are not an ambient finite/bounded universe.
2. The exact MB104 packet is not source-completely transported to product-cover fixed lifts. The historical per-node concentration `u_q=8l*m_q` was retracted, and the current `000707` e=2 passport retains aggregate exhaustion/parity while explicitly leaving the pointwise branch/residual-lift transition unresolved.

Thus H5 has a valid forward adapter only to the bare correspondence, not to the finite equivariant object required for closure, and its reverse adapter also fails.

Cycle-2 routing advances to **H6 finite monodromy / Nielsen-passport obstruction**. H6 must first test whether a source-complete Nielsen object can be defined without reintroducing the same concentration/lift assumption.


### Cycle 2 run 3 disposition — H6

H6 finite monodromy / Nielsen-passport obstruction: **FAIL / PARKED**.

For the active `000707` e=2 factor map, the retained passport has degree

```
n=28l
```

and eight branch values.  At each branch value the local branch-cycle type is

```
2^(r_q) 1^(u_q),
u_q+2r_q=28l,
u_q even.
```

For the first factor, the four residual-pair totals are fixed by the retained node table as

```
32l, 24l, 56l, 0.
```

The `56l` pair is forced to split as `28l+28l`, and the zero pair is fixed.  But the first pair permits

```
u_(+a)=4l+2i,
u_(-a)=28l-2i,
0<=i<=12l,
```

while the second permits

```
u_(+b)=2j,
u_(-b)=24l-2j,
0<=j<=12l.
```

Every such choice satisfies the retained degree, evenness, pair-total, Riemann--Hurwitz and residual-pair sign-parity constraints.  Therefore the retained aggregate interface alone permits at least

```
(12l+1)^2
```

distinct aggregate cycle-type passports before any full permutation tuple is chosen.  This grows without bound with `l`.

A genuine Nielsen tuple lives in `S_(28l)^8` and carries still more information. Compressing these growing cycle data to a fixed finite object requires exactly the branch-to-fixed-product-lift information that remains missing. If that information is discarded, different carrier-level allocations map to the same reduced passport and the reverse adapter fails.

Thus H6 reaches the roadmap stop condition: cycle data grow freely with `l`, and the finite compression would reintroduce the same source-incomplete concentration/lift assumption rejected in H5.

### Cycle 2 portfolio review

Cycle 2 is complete.

| Route | result | disposition |
|---|---|---|
| H8 log boundary | FAIL | PARKED; exact exceptional packet admits uniform positive orbifold-BMY slack. |
| H5 etale correspondence rigidity | FAIL | PARKED; ambient correspondence universe is unbounded and packet-to-fixed-lift adapter is missing. |
| H6 finite Nielsen passport | FAIL | PARKED; aggregate cycle-type space already grows at least `(12l+1)^2`, and reverse adapter loses branch-lift semantics. |

No Cycle-2 route is a DEEP candidate. H3 remains unreleased.

### Cycle 3 candidate routes

These are hypotheses only; no credit is assigned.

#### H9 — uniform stable-base / Zariski-ray obstruction

Work directly with the exact active divisor ray `D_l=lD_1`.  Instead of asking whether the integral Picard class exists, compute whether the source-complete negative-curve/fibration inventory forces a nonzero fixed component in every effective member of `|lD_1|`.  A forced component would contradict an integral carrier uniformly in `l`.

First shallow gate: compute the exact intersections of `D_1` with the retained source-complete negative-curve classes and decide whether a Zariski/stable-base witness is actually complete enough for an F/R proof.  Do not enumerate sections.

Stop if all known tests are nonnegative and the negative-curve inventory is not source-complete, or if the proposed fixed component is one already known not to occur on the active incidence-16 survivors.

#### H10 — receiver-preserving explicit degeneration

Construct one specific algebraic degeneration of the cuboid surface and the ray `D_l` to a computable boundary model, with a proved specialization adapter for an integral normalization-genus-one carrier and the balanced packet.

First shallow gate: prove the degeneration preserves enough of the receiver to make nonexistence on the special fibre reversible.  Do not perform special-fibre enumeration before that gate passes.

Stop if integrality, geometric genus, or the exact branch packet can disappear into components/embedded points under specialization, or if only generic Hilbert compactness is available (already rejected by H4).

#### H11 — off-exceptional singularity localization theorem

The unresolved quadratic defect is largely off the fourteen exceptional contacts.  Test whether the cuboid equations/product-cover geometry force those singularities onto a fixed finite union of special divisors or grids with an exact global capacity smaller than `168l^2+56l`.

First shallow gate: prove the localization statement itself from source-locked geometry.  No Bezout/capacity arithmetic begins unless every off-exceptional singularity of a hypothetical carrier is captured.

Stop if arbitrary off-grid ordinary nodes remain compatible; that would reduce to the already parked H8/U1/special-grid counting walls.

Initial Cycle-3 order: **H9, H10, H11**.


## Wide-scan override — user-directed 2026-09-18

The sequential Cycle-3 order `H9 -> H10 -> H11` is **paused**.

Reason: after two cycles of route-by-route work, the research process was drifting toward construction of missing adapters rather than broad search for native MB104-closing mechanisms.

Authoritative wide-scan portfolio:

```
stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MB104-WIDE-SHALLOW-CLOSURE-SCAN-20260918.md
```

During wide-scan mode:

- inspect 4--6 materially different closure mechanisms per mainbatch invocation;
- prefer routes whose native theorem attacks effectivity, low normalization genus, or the exact ray directly;
- do not create a subproject to construct a missing adapter;
- an adapter-dependent route may be marked promising, but adapter construction is deferred;
- only candidates surviving two independent shallow kill tests may return to DEEP consideration.

Initial Round A is W1/W2/W3/W4/W6:
Bogomolov--Reider superabundance, symbolic/Waldschmidt effectivity, Aut-norm invariant sections, K3 quotient pushdown, and modular-form valence.


### Wide scan Round A disposition

Round A checkpoint:

```
MB104-WIDE-SHALLOW-ROUND-A-20260918.md
```

Five routes were screened with one cheap kill-test each:

```
W1 Bogomolov--Reider                 DROP
W2 symbolic/Waldschmidt effectivity DROP
W3 Aut(S)-norm invariant section    DROP
W4 K3 quotient pushdown             PASS-TO-SECOND-SCAN
W6 modular-form valence             DROP
```

No route is DEEP.  W4 receives exactly one second shallow test, in parallel with Round B.

Next invocation scans:

```
W4-second  fixed K3 lattice / (-2)-curve / elliptic-fibration test
W5         higher symmetric differentials
W8         simultaneous sign-quotient genus budget
W10        ambient fat-point Hilbert function
W11        elliptic-normalization linear-series collapse
```

Do not reopen W1/W2/W3/W6 during this round.


### Wide scan Round B disposition

Round B checkpoint:

```
MB104-WIDE-SHALLOW-ROUND-B-20260918.md
```

Five route instances were screened:

```
W4-second K3 quotient lattice/fibration     DROP
W5         higher symmetric differentials  DROP
W8         simultaneous sign-quotient RH   DROP
W10        ambient fat-point Hilbert        DROP
W11        elliptic normalization series    DROP
```

No route is DEEP and no second-scan survivor remains.

The broad scan remains active.  Round C is:

```
W7   cyclic/abelian-cover BMY amplification
W9   finite-characteristic specialization
W12  receiver-preserving explicit degeneration
W14  zero-quartic restriction-map obstruction
W13  stable factorization / fixed-component section-ring theorem
```

W15 simultaneous zero-quartic restriction rank is conditional on W14 showing that both individual restriction maps can be nonzero.

W14/W13 are prioritized because they attack irreducibility directly and require no branch-to-product-cover adapter.


### Wide scan Round C corrected disposition

Round C checkpoint:

```
MB104-WIDE-SHALLOW-ROUND-C-20260918.md
```

Corrected result after archive semantic replay:

```
W7   cyclic/abelian-cover BMY       DROP
W9   finite-characteristic route    DROP
W12  explicit degeneration          DROP
W13  stable factorization           DROP
W14  zero-quartic restriction map   DROP_ALREADY_RETAINED
```

W14 was a rediscovery.  The retained archive leaf
`GENUS1-SPAN5-BALANCED16-000707-PRIMITIVE-RANK.md`
already proves `h0(A)=124`, characteristic-zero primitive jet rank `220`, explicit nonzero restriction to `Q0`, and nonfixedness of both active zero quartics for every `l>=1`.

No Round-C route is DEEP and there is no second-scan survivor.

Round D is archive-prechecked and remains broad:

```
W16 minimal Cayley--Bacharach conductor subcluster
W17 support-stabilizer carrier dichotomy
W18 elliptic projection / secant-center capacity
W19 adaptive Wronskian / unbounded-jet budget
W20 support-hyperplane residue / Abel relation
```

One cheap test each.  No missing-adapter construction.
