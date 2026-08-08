# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

for integer-space-diagonal cuboids.

## Current review state

An external review of the Stage13 R01 single-file bundle returned `OPEN` and
identified a real circularity in the old Stage13-7jb presentation of the raw
`j=0` direction-neutral arithmetic factor.

Stage13-12aa accepts that finding and replaces the circular check by an
independent `j=0` three-variable factorization/common-factor argument.

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_1_THROUGH_10=HISTORICALLY_COMPLETE
STAGE13_EXTERNAL_REVIEW_R01=OPEN
STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
CLAUDE_FATAL_DIRECTION_NEUTRALITY=REPAIRED
RAW_DIRECTIONAL_ASYMPTOTIC=RESTORED_NON_CIRCULARLY
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=NOT_YET_RECLOSED
PAIR_OVERLAP_FIXED_MODULUS_TRANSFER=PENDING_REAUDIT
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
NEXT_STAGE13_TASK=Stage13-12ab
```

The current repair source is

```text
stages/stage13/13-12aa/result.md
```

with audit assets

```text
stages/stage13/scripts/13-12aa/j0_common_factor_audit.py
stages/stage13/data/13-12aa/j0_common_factor_audit_report.json
```

The historical canonical exposition remains `stages/stage13/main.md`; where
its old `STAGE13_COMPLETE` status conflicts with this README and the 13-12
repair files, the 13-12 repair status has precedence until Stage13 is
re-reviewed and closed again.

## What 13-12aa repaired

The old 7jb validator first set

\[
D_q=\frac{\kappa I_q}{3\pi^3}
\]

from the Stage12 total and chamber proportions, then checked that `D_q/K_q`
was common. Since Stage13-7j already had `K_q proportional to I_q`, that was
not an independent proof of commonness.

Stage13-12aa instead proves first, without seeding any categorywise raw
constant,

\[
\boxed{
A_q(B)\sim \Theta J_q B(\log B)^3
}
\]

with one unknown arithmetic constant \(\Theta\) for all three categories and

\[
J_q=\frac{2I_q}{\pi},
\qquad
\sum_qJ_q=\frac\pi4.
\]

Only after that common-factor lemma is established is the frozen Stage12 total
used:

\[
\sum_q A_q(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

This gives

\[
\Theta=\frac{\kappa}{6\pi^2}
\]

and hence non-circularly

\[
\boxed{
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Therefore the raw normalized limit is again

```text
P_raw,inf = (0.5347369332313988,
             0.24535917783225203,
             0.21990388893634913)

A_ab:A_ac:A_bc
 -> 2.431684750178191 : 1.115756428951881 : 1
```

but this no longer relies on the circular 7jb `D_q/K_q` check.

## What remains open

The external review also challenged the fixed-modulus transfer used in the
Stage13-7jf pair-overlap sieve. The finite-field local calculation is not the
same issue as the global statement that imposing a fixed finite set of local
conditions multiplies the Stage12/Stage13 main constant by the corresponding
local factors.

Stage13-12ab will audit that transfer independently. Until that is closed, the
raw theorem above is active at the project external-theorem level, but the
exactly-one transfer

\[
N_q(B)=A_q(B)+o(B(\log B)^3)
\]

and therefore the final exactly-one directional theorem remain under reopened
review.

## Historical result under re-review

The previous Stage13 theorem was

\[
\mathbf N(B)
=
\frac{\kappa}{3\pi^3}
(I_{ab},I_{ac},I_{bc})B(\log B)^3
+o(B(\log B)^3),
\]

with

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
I_ab+I_ac+I_bc = pi^2/8
```

and normalized ratio

```text
2.431684750178191 : 1.115756428951881 : 1
```

Stage13-12aa restores the raw-incidence part of this theorem. Stage13-12ab is
required before the exactly-one version is declared closed again.

## Logical scope

Stage13 does not claim:

- existence or nonexistence of a perfect cuboid;
- an explicit convergence rate or effective threshold;
- monotonicity of the directional ratios;
- independent publication-grade peer review;
- a certified numerical enclosure for `kappa`.

The frozen Stage12 R09 theorem remains a declared prior input, not part of the
Stage13 re-review.
