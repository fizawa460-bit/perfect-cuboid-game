# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

for integer-space-diagonal cuboids.

## Current review state

The R01 review found a genuine circularity in the old raw direction-neutrality
argument and an under-derived fixed-modulus overlap step. Stage13-12aa and
13-12ab repaired the proof architecture, and Stage13-12ac published a neutral
R02 single-file bundle.

R02 then received two independent evaluations:

```text
Grok   = OPEN
Claude = REPAIRABLE
```

They substantially agreed on the mathematical diagnosis. The R01 circularity
was structurally repaired, but the R02 proof still needed a quantitative
`j=0` Wiener/curved-region/harmonic closure. Grok additionally kept two
p-adic overlap-side issues open.

Stage13-12ad now addresses the common analytic objections with explicit
all-prime/all-harmonic constants and a fixed error budget.

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_EXTERNAL_REVIEW_R01=OPEN
STAGE13_EXTERNAL_REVIEW_R02_GROK=OPEN
STAGE13_EXTERNAL_REVIEW_R02_CLAUDE=REPAIRABLE

STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
STAGE13_12AB=COMPLETE_FIXED_LOCAL_OVERLAP_REPAIR
STAGE13_12AC=COMPLETE_R02_REVIEW_RESYNTHESIS
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE

CLAUDE_R02_WEIGHTED_L1_UNIFORMITY=REPAIRED
CLAUDE_R02_NONZERO_HARMONIC_LOWER_ORDER=REPAIRED
GROK_R02_ZERO_MODE_CURVED_TRANSFER=REPAIRED

P_ADIC_POSITIVE_VALUATION_TAIL=PENDING_13_12AE
LOCAL_STATE_REFINEMENT_COMPLETENESS=PENDING_13_12AE
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
NEXT_STAGE13_TASK=Stage13-12ae
```

Stage13 is deliberately not self-declared externally `CLOSED`.

## R02 and post-R02 precedence

R02 itself is an immutable review snapshot:

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
```

Its proof map is

```text
stages/stage13/13-12ac/current-proof.md
```

For work after the R02 verdicts, the active repair precedence is

```text
13-12ad/result.md
-> 13-12aa/result.md
-> 13-12ab/result.md
-> 13-12ac/current-proof.md
-> historical main.md and audit assets
```

## 13-12aa — non-circular raw common factor

The old 7jb presentation seeded

\[
D_q=\frac{\kappa I_q}{3\pi^3}
\]

before checking common amplification. 13-12aa instead first derives the form

\[
A_q(B)\sim\Theta J_qB(\log B)^3
\]

with one unknown common `Theta`, and only afterwards uses the frozen Stage12
total theorem to calibrate

\[
\Theta=\frac{\kappa}{6\pi^2}.
\]

That removes the R01 circularity at the structural level.

## 13-12ad — quantitative analytic closure

R02 correctly noted that the common-factor architecture still depended on two
analytic statements that were written too compactly. 13-12ad fixes

\[
\delta=\frac18,\qquad \sigma=\frac58
\]

and proves coefficientwise, for every split prime `q>=13` and every angular
phase,

\[
\boxed{
\|C_{\ell,q}-1\|_{5/8}\le529q^{-5/4}.
}
\]

The lone smaller split prime `q=5` is a finite Euler factor. Thus the global
mixed correction is uniformly weighted-`l1` over the full retained harmonic
range; no finite prime sampling is used.

The curved-region/harmonic proof then fixes

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
finite-order A = 48
```

and obtains the explicit lower-order ledger

```text
small height                 O(B (log B)^(9/4))
small coordinate             O(B (log B)^(5/2))
mixed log shifts             O(B (log B)^2)
rectangle power tails        B (log B)^C exp(-c (log B)^(1/4))
curved boundary / mesh       O(B (log B)^(-5))
Vaaler excess                O(B (log B)^(-1))
all retained harmonics core  O(B (log B)^(-6))
```

so every error is `o(B(log B)^3)`.

The external Hecke input is also stated with its actual angular-conductor
dependence rather than hidden behind “same machinery”: nonzero Gaussian
angular characters have the standard Landau--Page zero-free region with
`log((2+|t|)(2+|k|))` dependence and no exceptional real zero for `k!=0`;
with `k=8ell` and `ell<=log(B)^4`, finite-order Selberg--Delange is uniform for
the fixed budget above.

Therefore the raw analytic core again gives, before Stage12 calibration,

\[
A_q(B)\sim\Theta J_qB(\log B)^3
\]

with common `Theta`.

Assets:

```text
stages/stage13/13-12ad/result.md
stages/stage13/scripts/13-12ad/j0_quantitative_closure_audit.py
stages/stage13/data/13-12ad/j0_quantitative_closure_audit_report.json
```

## What remains open

Stage13-12ad intentionally does not claim to repair the two remaining
R02/Grok overlap-side objections:

1. derive the inert-prime positive-valuation local tail with an explicit
   absolute constant rather than the phrase `O(1/p)`;
2. enumerate the full local-state refinement across valuation, parity and
   primitivity strata so the pair-overlap majorization can be checked directly.

Those are the sole targets of Stage13-12ae. Until then the exactly-one theorem
remains externally `OPEN` even though the raw `j=0` analytic core has been
quantitatively repaired.

## Logical scope

Stage13 does not claim existence or nonexistence of a perfect cuboid, an
explicit convergence threshold/rate, monotonicity of directional ratios,
publication-grade peer review, or a certified enclosure for `kappa`.
Stage12 R09 remains a declared frozen prior input.
