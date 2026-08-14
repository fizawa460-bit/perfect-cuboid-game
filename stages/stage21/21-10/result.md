# Stage21-10 — Stage16 -> Stage17 transition contract with Stage16S control

EVIDENCE_LEVEL=PROVED
CHECKPOINT=10
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## Transition object

Stage21 studies the cost of adding an integral space diagonal to the primitive/canonical exactly-one-face population.

Source:

\[
\mathcal B_1(B)=\{0<a<b<c,\ \gcd(a,b,c)=1,\ R\le B,\ \text{exactly one integral face diagonal}\},
\]

with count `M_1(B)`.

Target:

\[
\mathcal N_1(B)=\{(a,b,c)\in\mathcal B_1(B): R\in\mathbf Z\},
\]

with count `N_1(B)`.

On target objects the integral space diagonal is `d=R`, so the Stage17 cutoff `d<=B` and the Stage16 cutoff `R<=B` are exactly identical.

```text
SOURCE_STAGE=Stage16
TARGET_STAGE=Stage17
CONTROL_STAGE=Stage16S
SOURCE_POPULATION=primitive canonical exactly-one-face, no space-integrality requirement
TARGET_POPULATION=source plus integral space diagonal
COMMON_CUTOFF=R<=B; target d=R exactly
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

## Intrinsic control

Stage16S supplies the ambient intrinsic space-diagonal baseline. For the ambient primitive/canonical population `U(B)`,

\[
N_S^{all}(B)\sim \frac{B^2}{32G},
\qquad
\frac{N_S^{all}(B)}{U(B)}\sim
\frac{9\zeta(3)}{8\pi G}\,B^{-1}.
\]

Stage21 will compare the conditional exactly-one survival ratio `N_1/M_1` against this intrinsic baseline. Stage21 owns the final interaction classification; checkpoint10 makes no independence/correlation claim.

## Repository-wide reuse preflight

The Stage21-28 exploration policy requires a strongest-interface search before merely dividing the frozen Stage16 and Stage17 summaries.

That search found the merged Euler-side E-1e / PR #128 theorem, which is a literal source-population match and strengthens Stage16's frozen `Theta(B^2 log B)` statement to an explicit asymptotic:

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

Directionwise, for `q in {ab,ac,bc}`,

\[
M_{1,q}(B)\sim \frac{6I_q}{\pi^4}B^2\log B.
\]

Stage17 supplies

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\]

and its directional interface uses the same chamber factors `I_q`:

\[
N_{1,q}(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

These stronger interfaces are inputs for checkpoint30 and are not yet promoted to a transition theorem at checkpoint10.

```text
REPO_REUSE_PREFLIGHT=PASS
DIRECT_TERM_SEARCH=PASS
SYNONYM_NOTATION_SEARCH=PASS
STRUCTURAL_SIGNATURE_SEARCH=PASS
DEPENDENCY_NEIGHBOR_SEARCH=PASS
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
STRONGER_SOURCE_INTERFACE=E-1e_PR128
STAGE16S_BASELINE_READY=true
TRANSITION_FORMULA_IS_STARTING_POINT_NOT_DEFAULT_STOP=true
```

## Research boundary

Stage21 will not stop at the first quotient formula. Checkpoints30-60 must also test, where rigorous inputs permit: leading constants, directional cancellation, intrinsic-baseline enhancement/suppression, alternate-path comparisons, and arithmetic mechanisms without double charging. If an upstream premise is found false or materially insufficient, Stage21 must return to the source stage under the roadmap reinvestigation rule.

No perfect-cuboid endpoint is introduced.

```text
NEXT_CHECKPOINT=20
NEXT_EXPECTED_COMMAND=Stage21-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
