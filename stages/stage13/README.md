# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

for integer-space-diagonal cuboids, using Stage12 R09 as a frozen prior theorem-level input.

## Current review state

External review history:

```text
R01        OPEN
R02 Grok   OPEN
R02 Claude REPAIRABLE
R02 Qwen   REPAIRABLE
```

The R01 circular direction-neutrality construction was replaced by the non-circular Stage13-12aa architecture. R02 then isolated two remaining repair groups:

1. quantitative `j=0` Wiener / curved-region / nonzero-harmonic closure;
2. inert-prime positive-valuation and local-state completeness for overlaps.

Stage13-12ad closes group 1 with explicit uniform estimates. Stage13-12ae closes group 2 with an exact inert local factor. Stage13-12af now packages both repairs into a fresh neutral R03 review bundle.

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_12AA=COMPLETE_NONCIRCULAR_STRUCTURE
STAGE13_12AB=COMPLETE_FIXED_LOCAL_STRUCTURE
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE
STAGE13_12AE=COMPLETE_EXACT_PADIC_LOCAL_CLOSURE
STAGE13_12AF=COMPLETE_R03_REVIEW_RESYNTHESIS

EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=R03_CANDIDATE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
NEXT_STAGE13_TASK=EXTERNAL_R03_REVIEW
```

Stage13 is deliberately **not** self-declared externally `CLOSED`.

## Immutable historical review snapshots

R01 and R02 remain the exact objects previously reviewed. In particular R02 is frozen:

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
```

The new R03 target is

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260809-R03.html
```

with authoritative proof map

```text
stages/stage13/13-12af/current-proof.md
```

Current proof precedence:

```text
13-12af/current-proof.md
-> 13-12ad/result.md
-> 13-12ae/result.md
-> 13-12aa/result.md
-> 13-12ab/result.md
-> 13-12ac/current-proof.md
-> historical main.md / audit assets
```

## Quantitative `j=0` repair — Stage13-12ad

For every split prime `p>=13` and every retained angular phase,

\[
\boxed{\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}.}
\]

The finite split prime `p=5` is separated. The proof also establishes the logarithmic moments required for convolution and fixes

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
finite-order A = 48
```

with every curved-region, Vaaler and harmonic error shown to be `o(B(log B)^3)`.

## Exact inert local repair — Stage13-12ae

For inert `p=3 mod 4`, primitivity forces `v_p(h)=0`, and `(r,s)=1` leaves only

```text
U    (0,0,0)
R_b  (0,b,0), b>=1
S_c  (0,0,c), c>=1
```

as local valuation states. Hence

\[
L_{p,0}(1,1,1)=\frac{p+1}{p-1},
\qquad
\frac{T_p^+}{L_{p,0}(1,1,1)}=\frac{2}{p+1}\le\frac2p,
\]

so the formerly unspecified constant is exactly

\[
\boxed{C_0=2}.
\]

The full constrained local multiplier is

\[
\boxed{\lambda_p=\frac{p+5}{2(p+1)}=\frac12+\frac{2}{p+1}},
\]

therefore `lambda_7=3/4` and every inert `p>7` has `lambda_p<3/4`.

## R03 synthesis — Stage13-12af

R03 explicitly promotes the remaining Qwen R02 minor points into the current proof:

- the tag factor `2` is only a safe upper multiplicity;
- Stage12 total mass is used before calibration only as an error majorant for Vaaler excess;
- OE/EE is handled branchwise as finite 2-adic data;
- the relation
  \[
  \boxed{J_q=\frac{2I_q}{\pi}}
  \]
  is proved analytically by the outer-angle change of variables, not inferred from numerical quadrature.

The R03 candidate theorem is

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
}
\]

and

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.}
\]

The normalized candidate vector remains

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

## Review neutrality and scope

R03 explicitly declares that prior verdicts, internal PASS/COMPLETE labels, Git hashes and CI success are not mathematical evidence. Negative verdicts carry no extra burden.

Stage13 does not claim existence or nonexistence of a perfect cuboid, an explicit convergence threshold/rate, monotonicity of directional ratios, publication-grade peer review, or a certified numerical enclosure for `kappa`. Stage12 R09 remains a declared frozen prior input and Stage12 source is not embedded in R03.
