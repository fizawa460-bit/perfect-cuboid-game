# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

for integer-space-diagonal cuboids.

## Current review state

The Stage13 R01 single-file review returned `OPEN` with two substantive findings.

1. The old Stage13-7jb raw `j=0` direction-neutrality check was circular.
2. The old Stage13-7jf fixed-modulus overlap transfer was stated too quickly.

Both identified proof gaps now have explicit repair steps:

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_1_THROUGH_10=HISTORICALLY_COMPLETE
STAGE13_EXTERNAL_REVIEW_R01=OPEN

STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
CLAUDE_FATAL_DIRECTION_NEUTRALITY=REPAIRED
RAW_DIRECTIONAL_ASYMPTOTIC=RESTORED_NON_CIRCULARLY

STAGE13_12AB=COMPLETE_FIXED_LOCAL_OVERLAP_REPAIR
CLAUDE_MAJOR_FIXED_MODULUS_TRANSFER=REPAIRED
PAIR_OVERLAP_LOWER_ORDER=RESTORED
TRIPLE_OVERLAP_LOWER_ORDER=RESTORED
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=RESTORED

STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
NEXT_STAGE13_TASK=Stage13-12ac R02 review-bundle resynthesis
```

Stage13 is not self-declared externally `CLOSED`. The repaired proof should be
reviewed again independently.

## Active repair sources

```text
stages/stage13/13-12aa/result.md
stages/stage13/scripts/13-12aa/j0_common_factor_audit.py
stages/stage13/data/13-12aa/j0_common_factor_audit_report.json

stages/stage13/13-12ab/result.md
stages/stage13/scripts/13-12ab/fixed_local_overlap_audit.py
stages/stage13/data/13-12ab/fixed_local_overlap_audit_report.json
```

The historical exposition remains

```text
stages/stage13/main.md
```

but where its old Stage13-7jb / Stage13-7jf proof provenance conflicts with the
13-12 repair files, the 13-12 repair files have precedence for review.

## 13-12aa — raw directional repair

The old 7jb validator first set

\[
D_q=\frac{\kappa I_q}{3\pi^3}
\]

from the Stage12 total and chamber proportions and only afterwards checked a
common amplification. Because the pure-`G` constants were already proportional
to the same `I_q`, that was not an independent proof.

Stage13-12aa instead first proves

\[
\boxed{A_q(B)\sim \Theta J_q B(\log B)^3}
\]

with one unknown common arithmetic constant `Theta`, where

\[
J_q=\frac{2I_q}{\pi},\qquad \sum_qJ_q=\frac\pi4.
\]

Only afterwards is the frozen Stage12 total theorem used to determine

\[
\Theta=\frac{\kappa}{6\pi^2},
\]

hence

\[
\boxed{A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.}
\]

This restores the raw theorem without circularity.

## 13-12ab — overlap repair

For a tagged raw incidence

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2,
\]

a second integral face sharing the tag implies

\[
x^2+z^2=\square.
\]

At inert primes `p=3 mod 4`, impose the necessary local test

\[
x^2+z^2\in QR_0(\mathbf F_p).
\]

Stage13-12ab makes the previously implicit fixed-modulus transfer explicit:
a bounded condition at a fixed prime is implemented by refining the
Stage13-12aa local state by finitely many unit residues and replacing exactly
that prime's Euler factor. For a fixed finite set `S`,

\[
\mathcal D_{\ell,S}
=\mathcal D_\ell
\prod_{p\in S}\frac{L^W_{p,\ell}}{L_{p,\ell}}.
\]

Thus pole orders, the curved real kernel and the nonzero-harmonic lower-order
argument are unchanged; the zero-mode main constant is multiplied by the
finite product of local acceptance factors.

On the unit-hypotenuse inert-prime stratum the exact acceptance is

\[
\lambda_p^\times=\frac{p+1}{2(p-1)}
=\frac12+\frac1{p-1}.
\]

The positive-valuation local tail is `O(1/p)` with an absolute constant, so

\[
\lambda_p\le\frac12+O(1/p).
\]

Hence all sufficiently large inert primes satisfy `lambda_p<=3/4`.
For any fixed `k`, choose `k` such primes, take `B->infinity` with that set
fixed, and only then let `k->infinity`. This yields

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}
\]

for every pair overlap, and the triple overlap is lower order as a subset.
No growing modulus theorem is used.

## Restored exactly-one theorem pending R02 review

Combining 13-12aa with 13-12ab gives at the current project theorem boundary

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

and

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.}
\]

The corresponding normalized vector is

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

This theorem is repaired but remains `PENDING_EXTERNAL_R02`, not independently
accepted yet.

## Logical scope

Stage13 does not claim:

- existence or nonexistence of a perfect cuboid;
- an explicit convergence rate or effective threshold;
- monotonicity of the directional ratios;
- independent publication-grade peer review;
- a certified numerical enclosure for `kappa`.

Stage12 R09 remains a declared prior input and is not reopened by 13-12.