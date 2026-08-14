# Stage19-70 — bounded maximal synthesis and closeout candidate

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage19 studies the primitive canonical exactly-two-face population after imposing an integral space diagonal. Checkpoints10 through 60 are fresh-audited. Checkpoint70 performs only the bounded synthesis permitted by `docs/stage16-28-stage70-policy.md`; it does not reopen the audited checkpoint50 lower-bound OPEN_GATE or the Stage24 interaction question.

## 1. Known results

The Stage19 target is
\[
\mathcal A_2(B)=\{(a,b,c):0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ I_{ab}+I_{ac}+I_{bc}=2,\ R\in\mathbf Z\},
\]
with
\[
N_2(B)=\#\mathcal A_2(B).
\]
It is literally the frozen Stage15 numerator population and equals the Stage18 exactly-two population intersected with the integral-space condition.

The strongest certified quantitative upper theorem is
\[
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}=B^{1/2+o(1)}.}
\]
With the matched Stage18 denominator
\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]
this gives
\[
\boxed{\frac{N_2(B)}{M_2(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}\to0.}
\]
This is an upper thinning law, not an asymptotic for `N_2` or for the ratio.

Independently, the exact Stage19 survivor predicate in the frozen shared-edge toric coordinates is
\[
\boxed{R\in\mathbf Z\iff \operatorname{sf}(A)=\operatorname{sf}(B)},
\]
where
\[
A=m^2r^2+n^2s^2=N(mr+i\,ns),\qquad
B=m^2s^2+n^2r^2=N(ms+i\,nr).
\]
For good split primes `p=1 mod 4`, the same-measure local parity sieve has
\[
1-\rho_p=\frac4p+O(p^{-2}),
\]
and proves independently
\[
\boxed{N_2(B)/M_2(B)\to0.}
\]
The local sieve is not credited with the half-power bound.

The frozen exact finite census gives
\[
N_2(500{,}000{,}000)=3495,
\qquad
(N_a,N_b,N_c)=(1374,1371,750).
\]
By monotonicity,
\[
\boxed{N_2(B)\ge3495\qquad(B\ge500{,}000{,}000).}
\]
This is a constant finite floor only.

## 2. Additional deductions from the certified ledger

No new theorem input is needed for the following deductions.

1. Stage19 is rigorously nonempty, with at least 3495 distinct primitive canonical objects already certified below the frozen B500m cutoff.
2. Since `M_2(B)~C_{M_2}B(log B)^5` and `N_2/M_2->0`, one may equivalently record
   \[
   N_2(B)=o(B(\log B)^5).
   \]
   This is weaker than the inherited half-power upper bound but belongs to the independent squareclass-sieve theorem species.
3. The Stage18-to-Stage19 restriction has a concrete arithmetic normal form rather than an unspecified “space diagonal becomes square” heuristic: equality of two coupled Gaussian-norm squareclasses.
4. The certified zero-density mechanism and the strongest fixed-power ceiling are logically compatible but have different provenance. Multiplying their savings would be double counting and is forbidden.
5. The B500m numerical panel removes a small-sample objection to empirical inspection, but because the predeclared `N_2(B)/sqrt(B)` stability gate still fails, it supplies no evidence-level upgrade of the half-power exponent.
6. The current theorem ledger does not imply `N_2(B)->infinity`; finite nonemptiness and asymptotic unboundedness remain sharply separated.

## 3. Causal synthesis

The Stage18 source already satisfies the coupled double-Pythagorean geometry
\[
e^2+x^2=u^2,\qquad e^2+y^2=v^2,\qquad x^2+y^2\notin\square.
\]
Stage19 adds one exact arithmetic requirement, which in the unique shared-edge toric coordinates becomes
\[
\operatorname{sf}(N(mr+i\,ns))
=
\operatorname{sf}(N(ms+i\,nr)).
\]
Thus the new predicate is a **paired Gaussian-norm squareclass coincidence** on parameters already constrained by the two-face geometry.

At the mechanism level, split primes impose valuation-parity agreement with a cumulative local product tending to zero. This explains why the integral-space survivors have zero density inside the exactly-two Stage18 population.

At the quantitative level, however, the best certified half-power ceiling comes from the separate Stage14 global graph / elliptic-fiber / complete-host upper-bound chain. The local squareclass sieve naturally supplies a logarithmic local product and has not been proved to generate the fixed half-power.

Therefore the certified causal classification inside Stage19 is:

```text
EXACT_NEW_PREDICATE=PAIRED_GAUSSIAN_NORM_SQUARECLASS_COINCIDENCE
CAUSAL_ZERO_DENSITY_MECHANISM=SPLIT_PRIME_VALUATION_PARITY_SIEVE
FIXED_POWER_CEILING_SOURCE=STAGE14_GLOBAL_WHOLE_FAMILY_THEOREM
LOCAL_SIEVE_PAYS_HALF_POWER=false
DOUBLE_CHARGE_CHECK=PASS
HALF_POWER_INTRINSIC=UNRESOLVED
INDEPENDENT_OF_PRIOR_CONDITIONS=UNRESOLVED_DEFER_STAGE24
```

Stage24 remains the correct receiver for deciding whether the quantitative space-diagonal cost after two integral faces is best classified as independent, correlated, or interaction-dependent relative to the prior face conditions.

## 4. Lower-stage reinterpretations

No lower-stage theorem is reopened.

- Stage18 remains exactly the matched source population. Stage19 refines it by intersecting with `R integral`; this does not alter Stage18's population law or causal double-Pythagorean description.
- Stage15's squareclass normal form and local zero-density theorem are reused literally on the same physical population; Stage19 does not strengthen or rewrite those frozen results.
- Stage14's half-power upper theorem remains an upper bound only. Stage19 does not reinterpret exponent `1/2` as a true growth exponent.
- The numerical observatory remains finite evidence. Its later reuse does not change any historical checkpoint or convert finite `T=0` into a nonexistence theorem.

Accordingly:

```text
LOWER_STAGE_REOPEN_REQUIRED=NO
POPULATION_CONTRACT_INVALIDATED=NO
CUTOFF_CONVENTION_INVALIDATED=NO
UPSTREAM_THEOREM_INVALIDATED=NO
```

## 5. Refinement candidates

The following are legitimate future refinements, not work to be opened inside Stage19-70:

1. prove an unbounded primitive Stage19 construction or any positive-power lower bound;
2. determine whether the current `1/2` upper exponent is sharp or can be improved;
3. at Stage24, classify the Stage18-to-Stage19 cost as independent/correlated/interaction-dependent using matched controls rather than intuition;
4. test any future proposed construction or sharper theorem against NUM-R01/R02/R03 and the exact Stage19 population adapter;
5. if new quantitative local-sieve uniformity becomes available, compare its rate with the global Stage14 half-power ceiling without multiplying the two mechanisms.

## 6. New heuristics

No new heuristic is promoted at closeout.

The finite decrease of `N_2(B)/sqrt(B)` through B500m may motivate future questions, but the predeclared stability gate fails. It remains finite diagnostic behavior only.

```text
NEW_HEURISTICS=NONE_PROMOTED
FINITE_FIT_PROMOTED_TO_ASYMPTOTIC=false
```

## 7. Open gates

The audited checkpoint50 gate remains frozen:

```text
OPEN_GATE=UNBOUNDED_OR_MATCHING_LOWER_BOUND_FOR_STAGE19
OPEN_GATE_STATUS=OPEN_GATE_AUDITED_PASS
OPEN_GATE_REENTRY_JUSTIFIED=NO
```

Its unresolved content includes:

- `N_2(B)->infinity`;
- an infinite primitive construction;
- any `N_2(B)>>B^delta` with `delta>0`;
- a matching `B^(1/2-o(1))` lower bound;
- sharpness or intrinsic status of exponent `1/2`.

The Stage24 interaction classification is a downstream question, not a reopened Stage19 checkpoint.

## 8. Next-stage questions and downstream receivers

Stage20 is the next serial population stage and studies exactly three integral face diagonals without requiring the space diagonal.

Stage19 also supplies frozen interfaces to later transition/synthesis lanes:

- Stage23: Stage17 -> Stage19;
- Stage24: Stage18 -> Stage19, including interaction classification;
- Stage25: Stage16 -> Stage19;
- Stage28: cross-transition synthesis.

These receivers must preserve the Stage19 nonclaims: no matching lower bound, no true half-power exponent, no independence statement, and no perfect-cuboid conclusion.

## 9. Stage-end artifact decisions

A self-contained bundle is required because Stage19 combines several theorem species whose provenance is easy to conflate: an inherited fixed-power upper bound, an independent squareclass zero-density mechanism, a finite exact census, and an audited lower-bound OPEN_GATE. Stage23/24/25/28 need one stable interface that prints these boundaries explicitly.

No new arsenal promotion is required. The reusable normal form and local sieve are already frozen Stage15 interfaces; the global upper machinery belongs to Stage14; the numerical oracle is already promoted as AR-040 / NUM-R01–R03. Stage19 adds no new portable mechanism beyond this population-specific synthesis.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=stable downstream interface needed to prevent conflation of upper-bound, causal-zero-density, finite-evidence, and open-lower-bound theorem species
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE
```

## 10. Bounded synthesis stop

Further progress on the unresolved growth law would require at least one substantially new input: a new construction theorem, a stronger lower-bound method, a sharper global upper theorem, new effective uniform local-sieve theory, or a new large computation designed for a genuinely new hypothesis. The Stage18-to-Stage19 interaction classification belongs to Stage24 by roadmap design.

Therefore Stage19-70 stops here rather than excavating the audited OPEN_GATE or stealing Stage24's question.

```text
KNOWN_RESULTS=population contract; N2/M2 quantitative upper thinning; N2<<B^(1/2+epsilon); paired Gaussian-norm squareclass normal form; independent local-sieve zero density; exact B500m census; finite constant floor
ADDITIONAL_DEDUCTIONS=Stage19 rigorously nonempty with >=3495 certified objects; N2=o(B(log B)^5); theorem-species provenance separation; no unboundedness follows
CAUSAL_SYNTHESIS=paired Gaussian-norm squareclass coincidence plus split-prime valuation-parity rejection explains zero density; fixed half-power remains separate Stage14 upper-bound provenance
LOWER_STAGE_REINTERPRETATIONS=none reopen or invalidate Stage14/15/18
REFINEMENT_CANDIDATES=unbounded primitive construction; positive-power lower bound; sharpness/improvement of half-power; Stage24 interaction classification; future effective local-sieve rate
NEW_HEURISTICS=NONE_PROMOTED
OPEN_GATES=UNBOUNDED_OR_MATCHING_LOWER_BOUND_FOR_STAGE19; HALF_POWER_SHARPNESS; HALF_POWER_INTRINSIC_STATUS
NEXT_STAGE_QUESTIONS=Stage20 population; Stage23/24/25 transition interfaces; Stage28 synthesis
SYNTHESIS_STOP_REASON=further progress requires new theorem/computation or belongs to downstream transition stages
SYNTHESIS_STOP_RULE_SATISFIED=YES
EVIDENCE_LEVEL=PROVED
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,AR-040
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
FINITE_DATA_USED_AS_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_REQUIRED=true
NEXT_STAGE_AFTER_PASS=Stage20
CODEX_REQUIRED=false
CODEX_REASON=bounded synthesis of already audited interfaces; no implementation or independent code-audit task
```
