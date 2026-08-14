# Stage21-30 — leading transition law and intrinsic interaction comparison

EVIDENCE_LEVEL=PROVED
CHECKPOINT=30
STATUS=PROVED_CANDIDATE_PENDING_FRESH_AUDIT

## 1. Leading conditional survival law

The strongest literal source interface recovered at Stage21-10 is

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

The audited Stage17 target law is

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3.
\]

The populations, multiplicities and cutoff are exact matches, so direct division gives

\[
\boxed{\frac{N_1(B)}{M_1(B)}\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}}.
\]

Thus Stage17's earlier Theta survival law is strengthened to a full leading-constant asymptotic.

## 2. Directionwise law

For each unique-face chamber `q in {ab,ac,bc}`, the matched upstream interfaces are

\[
M_{1,q}(B)\sim \frac{6I_q}{\pi^4}B^2\log B,
\qquad
N_{1,q}(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

Since the same positive chamber factor `I_q` occurs in numerator and denominator,

\[
\boxed{\frac{N_{1,q}(B)}{M_{1,q}(B)}\sim
\frac{\kappa\pi}{18}\frac{(\log B)^2}{B}}
\]

for every `q`. Hence the leading conditional space-diagonal survival law is direction-independent across the three unique-face chambers. This is an asymptotic statement about the matched chamber populations, not a finite-sample equality.

## 3. Intrinsic ambient baseline

Stage16S proves for the ambient primitive/canonical population `U(B)`

\[
\frac{N_S^{all}(B)}{U(B)}\sim
C_S B^{-1},\qquad
C_S=\frac{9\zeta(3)}{8\pi G}>0.
\]

Compare this with the exactly-one conditional survival law. Their quotient is

\[
\frac{N_1(B)/M_1(B)}{N_S^{all}(B)/U(B)}
\sim
\frac{\kappa\pi/18}{9\zeta(3)/(8\pi G)}(\log B)^2
=
\boxed{\frac{4\kappa\pi^2G}{81\zeta(3)}(\log B)^2}.
\]

Therefore

\[
\boxed{\frac{N_1/M_1}{N_S^{all}/U}\to\infty}.
\]

The polynomial cost is the same `B^{-1}` in the ambient and exactly-one populations, but conditioning on exactly one integral face enhances space-diagonal survival by an unbounded logarithmic factor of exact order `(log B)^2` relative to the intrinsic ambient baseline.

## 4. Interaction classification

This rules out asymptotic independence in the natural ratio sense

\[
N_1/M_1 \sim N_S^{all}/U,
\]

because the quotient of those probabilities tends to infinity rather than 1.

The rigorous classification at this checkpoint is therefore:

```text
POLYNOMIAL_SPACE_COST_AMBIENT=B^-1
POLYNOMIAL_SPACE_COST_GIVEN_EXACTLY_ONE_FACE=B^-1
POLYNOMIAL_COST_MATCH=true
LOGARITHMIC_PROFILE_MATCH=false
CONDITIONAL_ENHANCEMENT_FACTOR~=(4*kappa*pi^2*G/(81*zeta(3)))*(log B)^2
ENHANCEMENT_DIVERGES=true
ASYMPTOTIC_INDEPENDENCE_IN_RATIO_SENSE=false
INTERACTION_CLASSIFICATION=POSITIVE_LOGARITHMIC_ENHANCEMENT
```

This does **not** assert stochastic independence of individual arithmetic events in any stronger probabilistic model, nor does it factor the logarithmic enhancement into independent local probabilities. It is a theorem-level population comparison under the common cutoff.

## 5. Finite-data relation

Stage21-20 observed decreasing `N1/M1` and exact cross-enumerator equality between Stage17 `N1` and Stage16S `face1` at all shared thresholds. Those data remain diagnostics only. The formulas above are derived solely from proved asymptotic interfaces.

## 6. Exploration continuation

Checkpoint30 is not the Stage21 stop. Under the Stage21-28 exploration policy, checkpoints40-60 should investigate the arithmetic source of the `(log B)^2` enhancement, including whether the shared Pythagorean extension, local/squareclass structure, or an alternate path gives a sharper mechanistic statement. No product of heuristic local factors may be promoted without proof, and double charging must be avoided.

```text
UPSTREAM_PREMISE_CHECK=PASS
FINITE_DATA_USED_AS_PROOF=false
DOUBLE_CHARGE_CHECK=PASS
NEW_RESEARCH_JUSTIFIED=interaction mechanism remains unresolved after exact transition classification
NEXT_CHECKPOINT=40
NEXT_EXPECTED_COMMAND=Stage21-audit
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CODEX_REQUIRED=false
```
