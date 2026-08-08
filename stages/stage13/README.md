# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

for integer-space-diagonal cuboids.

## Current review state

The Stage13 R01 single-file review returned `OPEN` with two substantive findings:

1. the old Stage13-7jb raw `j=0` direction-neutrality check was circular;
2. the old Stage13-7jf fixed-modulus overlap transfer was stated too quickly.

Both proof gaps now have explicit repairs and Stage13-12ac has resynthesized the
repaired chain for a fresh R02 external review.

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

STAGE13_12AC=COMPLETE_R02_REVIEW_RESYNTHESIS
STAGE13_REPAIR_CHAIN=COMPLETE
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02
NEXT_STAGE13_TASK=EXTERNAL_STAGE13_R02_REVIEW
```

Stage13 is deliberately **not** self-declared externally `CLOSED`.

## R02 review entrypoint

The authoritative current proof map for R02 is

```text
stages/stage13/13-12ac/current-proof.md
```

with the two mathematical repair sources

```text
stages/stage13/13-12aa/result.md
stages/stage13/13-12ab/result.md
```

and the physical single-file review target

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260808-R02.html
```

The historical exposition remains

```text
stages/stage13/main.md
```

but its old Stage13-7jb and Stage13-7jf proof steps are superseded by
13-12aa and 13-12ab respectively. All other historical material remains
available as evidence inside the R02 bundle.

## 13-12aa — non-circular raw directional repair

The old 7jb validator first formed

\[
D_q=\frac{\kappa I_q}{3\pi^3}
\]

from the Stage12 total and chamber proportions and only afterwards checked a
common amplification. Because the comparison constants were already
proportional to the same `I_q`, that did not independently prove direction
neutrality.

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

## 13-12ab — fixed-local overlap repair

For a second integral face, Stage13-12ab works inside the explicit 13-12aa
Euler product and implements each fixed prime condition by finite local-state
refinement. For a fixed finite set `S`,

\[
\mathcal D_{\ell,S}
=\mathcal D_\ell
\prod_{p\in S}\frac{L^W_{p,\ell}}{L_{p,\ell}}.
\]

Thus a fixed local restriction replaces finitely many Euler factors without
changing the pole order, real category kernel or nonzero-harmonic argument.

For inert primes `p=3 mod 4`, the unit-layer acceptance is

\[
\frac{p+1}{2(p-1)}=\frac12+\frac1{p-1},
\]

and the positive-valuation local tail is `O(1/p)`, so all sufficiently large
inert primes satisfy `lambda_p<=3/4`.

For fixed `k`, choose `k` such primes, take `B->infinity` while the set is
fixed, and only then let `k->infinity`. This gives

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3).
\]

No growing-modulus theorem is used.

## Repaired theorem candidate pending R02

Combining 13-12aa and 13-12ab gives at the current project theorem boundary

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

The normalized candidate limit is

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

The theorem is repaired internally but remains
`STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R02`.

## R02 review neutrality

R02 explicitly instructs the reviewer that internal `PASS`/`COMPLETE` labels,
Git hashes and CI success are not mathematical evidence. The previous R01
verdict is not binding, and a negative R02 verdict carries no extra burden.
Hashes and CI exist only for source identity and deterministic regeneration.

## Logical scope

Stage13 does not claim:

- existence or nonexistence of a perfect cuboid;
- an explicit convergence rate or effective threshold;
- monotonicity of directional ratios;
- independent publication-grade peer review;
- a certified numerical enclosure for `kappa`.

Stage12 R09 remains a declared prior input and is not reopened by Stage13 R02.
