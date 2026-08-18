# StructureRadar literature ledger — search batch 03

SEARCH_TASK=SR-SEARCH-01
BATCH_ID=SR-BATCH-LITERATURE_SEARCH-03-R01
SEARCH_DATE=2026-08-19
STRUCTURES=SR-STR-013,SR-STR-015,SR-STR-017,SR-STR-018,SR-STR-019,SR-STR-020
EVIDENCE_POLICY=repo arsenal first; primary sources only for external theorem claims
NOVELTY_BY_SEARCH_ABSENCE=false

## SR-STR-013 — Primitive-first Möbius reindexing
`AR-032` is PROVED_CANONICAL but BACKGROUND_REUSABLE / REUSE_AFTER_EXACT_ADAPTER. The exact finite reindexing needs no external upgrade; reuse requires a unique common scale and homogeneous cutoff. Decision: `PARKED`.

## SR-STR-015 — R504 exceptional Prym locus gate
The audited generic statement is only `Hom_K(P_eta,E0_K)=0`; the rational exceptional Prym/E0-isogeny locus is not proved empty, finite, or bounded in isogeny degree. Primary split-Jacobian literature describes fixed-degree elliptic-subcover loci `L_n` (T. Shaska, arXiv:1209.3187; arXiv:2608.16426) but does not give a uniform finiteness theorem for the intersection of the specific R504 family with the union over unbounded isogeny degree. Decision: `EXTERNAL_GATE` retained.

## SR-STR-017 — Euler third-face local blocker law and dimension-two sieve
Repo local law: `delta_2=2/9` and `delta_p=2(p-chi_4(p))/(p^2+6p+1)=2/p+O(p^-2)`. Existing audited `S20-W03` / `S26-W03` use the exact local blocker plus a separate growing-prime Selberg-sieve interface. Quadratic-congruence root literature (H. T. Ngo, arXiv:2107.13301) is method-adjacent, not a stronger same-population theorem. Do not multiply the local-sieve and K3 thin-cover savings. Decision: `ACTIVE`.

## SR-STR-018 — Matched face-space population cross-ratio invariant
`I=(N2/M2)/(N1/M1)=N2*M1/(M2*N1)` on matched populations, with audited `I >> B^(1/4)(log B)^(-7)`. Existing `S25-W02` is the exact population-interaction invariant. It is algebraic ratio cancellation, not stochastic independence. Decision: `ACTIVE`.

## SR-STR-019 — Nested divisor-root first-moment receiver
The missing theorem is an every-principal-cell first moment with nested divisors and two simultaneous moving quadratic root congruences. Ngo arXiv:2107.13301 treats a materially simpler root problem; Grimmelt--Merikoski arXiv:2508.17979 gives divisor-in-AP averaging/equidistribution and not the required pointwise nested every-cell receiver. This matches `AR-020`'s audited negative boundary. Decision: `EXTERNAL_GATE` retained.

## SR-STR-020 — Safe-range fixed-residue Gaussian-prime sector occupancy
W. Kai, arXiv:2209.11816, gives Mitsui-type prime-element counts in one residue class and thin cone while retaining a possible Siegel term, with `N(q)<exp(sqrt(log X)/O_K(1))`. For `K=Q(i)`, a fixed D4 sector and fixed-power radial headroom fit the local `AR-021` contract after the exact modulus/scale check; interval subtraction is allowed only when the main term dominates endpoint errors. `AR-021` is EXTERNAL_THEOREM_DEPENDENT but status CONSUMED after closing the safe fixed-U mechanism. Decision: `PARKED`; do not extrapolate to super-Kai `AR-022`.

## Batch decision
SEARCHES_COMPLETED=6
ARSENAL_DECISIONS_RESOLVED_FROM_PENDING=4
ACTIVE=2
PARKED=2
EXTERNAL_GATE_RETAINED=2
NEW_EXTERNAL_ACTIVE_WEAPONS=0
PERFECT_CUBOID_EXISTENCE_PROMOTED=false
PERFECT_CUBOID_NONEXISTENCE_PROMOTED=false
NOVELTY_BY_SEARCH_ABSENCE=false

## Wider-search note
`SR-STR-015` and `SR-STR-019` remain genuine unknown-theorem gates. Broader external discovery may help identify alternative Prym/Humbert terminology or a nested-divisor/moving-root first-moment theorem; any lead still requires exact transfer audit.
