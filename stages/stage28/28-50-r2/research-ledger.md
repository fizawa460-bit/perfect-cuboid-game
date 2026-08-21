# Stage28-50-r2 — post-merge construction deepening ledger

```text
TASK_ID=Stage28-50-r2
CHECKPOINT=50
MODE=OPERATOR_REQUESTED_POSTMERGE_DEEPENING
PARENT_PR=1278
PARENT_AUDIT=PASS
PARENT_MERGE=2a770e900e9c2e6b4b194c52d49f897ca0d3b2b8
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
```

The first checkpoint50 batch tested seven materially distinct lower lanes and proved the epsilon-free target lower `M3(B)>>B^(1/3)`.  The operator requested additional bounded exploration before checkpoint60.  This r2 ledger adds only materially new lanes.

## L8 — injective Saunderson cone and explicit coefficient — SUCCESS CANDIDATE

The exact physical space height satisfies `R<=8r^6`, improving the old sufficient `72T^6` constant.  On the positive-density cone

```text
1/8 <= s/r <= 4/5
```

`w^3` is the unique smallest physical face diagonal, so the physical output identifies the Euclid input uniquely.  Primitive opposite-parity lattice density then gives

\[
\liminf_{B\to\infty} M_3(B)/B^{1/3}\ge 27/(40\pi^2).
\]

This is stronger than the parent `M3>>B^(1/3)` statement but does not change its exponent.

## L9 — classical polynomial-family degree inventory — CLOSED NO UPGRADE

- Saunderson: degree `6` in two Euclid parameters, efficiency `2/6=1/3`.
- Rule-1 Saunderson transform: degree `8`, efficiency at most `1/4`.
- Lenhart/Piezas conic families: degree `8` after two-parameter conic substitution, efficiency `1/4`.
- Bremner 1988 supplies many higher-degree rational-cuboid parametrizations; no checked closed-form family of lower degree than Saunderson yields a target improvement.

No global minimal-degree theorem is claimed.

## L10 — Himane T1/T2/T3 free-dimension test — CLOSED NO UPGRADE

Himane's templates use two primitive Pythagorean triples but impose an additional mixed square equation.  The two triples therefore cannot be counted as four free parameters.  The paper supplies examples and open problems, not a positive-density count of coupled pairs.  No `kappa/h>1/3` family follows.

## L11 — Peschmann Mordell-Weil bounded-height conversion — OPEN PRECISE EXTERNAL RECEIVER

The 2026 generator produces over one million finite Master-Hits, mostly outside classical closed-form families, but no matched `R<=B` polynomial lower.  The missing theorem is now localized to a uniform moving-fibre physical-height estimate plus a count of points for which the lift function `tau(P)` is a positive rational square.

```text
RECEIVER=UniformMovingEllipticFibreSquareLiftHeightCount
REQUIRED_STRENGTH=M3(B)>>B^(1/3+delta) for some delta>0, or direct strict marginal lower comparison
```

## L12 — rational branch components as Stage19 construction — CLOSED NO-GO

The four geometric rational branch components of the Stage19 space cover do not meet the positive physical real torus.  On that torus the exact branch polynomial is a product of two strictly positive sums of squares.  Therefore branch rationality itself supplies no physical `N2` lower family.

## L13 — current Arsenal / strongest-selector rematch — SUPERSESSION CANDIDATE ONLY

`docs/research-arsenal-index.md` currently routes:

```text
S25-W01: N2(B)>>B^(1/4)
S26-W01: M3(B)>>_epsilon B^(1/3-epsilon)
```

The Stage28-50 audited theorem already supersedes the displayed S26-W01 lower by `M3(B)>>B^(1/3)`, and r2 proposes an explicit positive liminf coefficient.  The central Arsenal is deliberately not mutated inside this unaudited derived checkpoint.  If r2 passes, Stage28-70 should decide the formal promotion/backflow.

## L14 — finite-generator/database cardinality as a lower theorem — REJECTED

Peschmann's `1,284,670` Master-Hit database and family-tag counts are generator-bound finite data, not counts under the common physical Euclidean cutoff.  They are valuable route evidence but cannot be promoted to an asymptotic lower or a population ordering.

## Combined checkpoint50 exploration status

Parent batch routes: `7`.

New r2 routes: `7` (`L8-L14`).

```text
MATERIALLY_DISTINCT_LOWER_ROUTES_TOTAL=14
NEW_R2_SUCCESS_CANDIDATES=1
NEW_R2_NEGATIVE_OR_BOUNDARY_CERTIFICATES=6
M3_EXPONENT_ABOVE_ONE_THIRD_PROVED=false
N2_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
FULL_M3_VS_N2_ORDERING_PROVED=false
PERFECT_CUBOID_ENDPOINT_USED=false
```

The remaining lower gate after r2 is narrower than at first submission:

```text
OPEN_GATE_50_R2=HigherEfficiencyOffBranchPhysicalConstructionOrUniformMovingEllipticSquareLiftCount
M3_PROGRESS_GATE=kappa/h>1/3
N2_PROGRESS_GATE=kappa/h>1/4
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```
