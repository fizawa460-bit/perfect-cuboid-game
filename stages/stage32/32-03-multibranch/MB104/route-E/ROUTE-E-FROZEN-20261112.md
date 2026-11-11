# Route E — frozen (2026-11-12)

Owner's decision, 2026-11-12: Stage32 / 32-03 MB104 route E is **frozen**. No credit, STATE.json, ledger or credit
flag change. The core **E12 §5 stays open**.

## Where it stands
- Audited research notes on main: E01–E12 (registered), E13–E15 (#1869, notes only), E16 (this PR, notes only).
- The single open point: for a birational pair (p₁, p₂) with positive slack on both sides (after the double-cover
  reduction of E14: equal odd sets), no bound on the degrees (a, b) is known.

## What was tried and why it stops
| note | tool | why it stops |
|---|---|---|
| E09–E10 | orbifold BMY on B | needs concentration of multiplicities; factor 3 short |
| E13 | trace gap, Theorems A, B | metric comparison; rigid only at slack (0, 0) nested / clusters |
| E14 | slack formula, Theorem A′, A⁺; Proposition C | without birationality the degree is unbounded, so metric tools cannot suffice |
| E15 | Klein intersection, holonomy uniqueness, cone divisors; Theorem E; component condition | birationality used only linearly or qualitatively |
| E16 | singularity budget of the image curve | forced δ ≈ ab/6 against budget ≈ ab; implied by E15 Lemma K |

## What a restart would need
A tool that uses birationality **quantitatively**, e.g. one of the targets of E16 §4: (T0) M ≤ (1 − c)(a + b) + C
using the ramification of both legs over B; (T1) concentration Σ m_P² > (4/3)ab − …; (T2) few cheap singular points
off the 12 lines. Candidate literature (Yamanoi's truncated second main theorem with moving targets,
Corvaja–Zannier gcd bounds) must first be checked against the papers; the current estimates fall short.

Do not restart by rephrasing E13–E16.
