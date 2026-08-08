# Stage14-t roadmap — triple-gate side track

## Purpose

Stage14-t is the dedicated side track for quantitative control of the triple/perfect-cuboid correction term in the Stage14 exactly-two-face problem. It is separate from the main `14-4` Kummer/rank-jump track and from the `14-e` ambient control track.

For the locked primitive canonical Stage14 population,

\[
\boxed{E(B)=N_2(B)+3T(B)},
\]

where `T(B)` counts objects with all three integral face diagonals. A main-track raw-pair law transfers to `N_2(B)` only after `T(B)` is controlled at the same scale.

## Frozen upstream contract

Stage14-t may use the frozen `R03 + Stage13-12ag` contract, the Stage14 exact pair interface, the fixed-base genus-5 geometry, and merged Stage14 results. It does not assume perfect-cuboid existence or nonexistence.

```text
T_O_SQRT_B_PROVED=false
UNIFORM_MOVING_BASE_TRIPLE_BOUND_PROVED=false
PERFECT_CUBOID_EXISTENCE_ASSUMED=false
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
```

## 14-t1 — definition, interfaces, finite baseline, literature boundary

Status: [x] Complete.

Locked results:

- exact triple multiplicity `E(B)=N2(B)+3T(B)`;
- fixed physical base model
  \[
  W^2=q^4+2Aq^2+1,\quad R^2=q^4+2Cq^2+1,
  \]
  with `A=(1-t^2)/(1+t^2)`, `C=2/t^2-1`;
- `A-C=-2/(t^2(1+t^2))`, so the two branch sets are disjoint on genuine physical bases;
- connected `(Z/2)^2` degree-4 cover with eight simple branch values, hence genus `5` by Riemann--Hurwitz;
- complex/projective exceptional base set `0, infinity, ±1, ±i`, avoided by genuine positive primitive Pythagorean faces;
- physical one-fiber height `v asymp sqrt(Bg/S1)`;
- two independent exact Stage14-2 generation routes give `T(B)=0` at all 11 audited cutoffs through `B=2,000,000`; no nonexistence inference is made;
- literature boundary: Faltings gives fixed-fiber finiteness; determinant-method work of Browning--Heath-Brown--Salberger and Liu is the first unconditional quantitative route to audit; fixed-genus uniform cardinality is not imported from conditional Lang-type uniformity; Peschmann 2026 is directly adjacent perfect-cuboid genus-cover work.

Artifacts:

```text
stages/stage14/14-t1/result.md
stages/stage14/14-t1/literature-triple-audit.md
stages/stage14/scripts/14-t1/triple_gate_baseline.py
stages/stage14/data/14-t1/triple_gate_baseline.json
.github/workflows/stage14-t1-triple-gate.yml
```

Decision:

```text
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
TRIPLE_FIXED_BASE_GENUS=5
FINITE_TRIPLE_CENSUS_MAX_B=2000000
FINITE_TRIPLE_COUNT_AT_MAX_B=0
FINITE_ZERO_IMPLIES_NONEXISTENCE=false
T_O_SQRT_B_PROVED=false
```

## 14-t2 — moving-family quantitative attack

Status: [>] Next.

Build a fixed-degree projective model of the genus-5 fiber with explicit coefficient height, compare its projective point height uniformly with the physical `(t,q)` height, then apply the strongest unconditional determinant-method bound that survives summation over primitive Pythagorean bases.

Targets, strongest first:

\[
T(B)\ll B^{1/2-\delta+o(1)}\quad(\delta>0),
\]

or at minimum

\[
T(B)=o(\sqrt B).
\]

If neither follows, t2 must prove the strongest unconditional weaker bound and identify the exact obstruction quantitatively rather than replacing it by a heuristic.

## 14-t3 — exceptional fibers and low-degree subfamilies

Status: [ ] Pending t2.

Classify degenerations, lower-genus quotients, extra automorphisms and low-degree subfamilies capable of accumulating triple points, and count them separately under the physical height.

## 14-t4 — Kummer-cover comparison

Status: [ ] Pending t3 and the relevant merged `14-4` descendants.

Compare the moving genus-5 formulation with the relative degree-two third-square cover of the Stage14 Kummer surface, especially on low-degree physical rational curves found by the main track.

## 14-t5 — transfer theorem to exactly-two count

Status: [ ] Pending a sufficient triple bound and a main-track raw-pair law.

Combine

\[
N_2(B)=E(B)-3T(B)
\]

with the strongest proved estimates. If `E(B)` has a `sqrt(B)` leading law and `T(B)=o(sqrt(B))`, transfer that law to the exactly-two population; otherwise retain the triple contribution explicitly.

## Scope boundary

Stage14-t is a population-counting track, not a finite search proof of nonexistence. It also does not duplicate `14-e8`, which studies Euler bricks in the ambient no-space-square control population.

```text
STAGE14_T_TRACK=ACTIVE
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
PRIMARY_TARGET=T(B)=o(sqrt(B))
STRONG_TARGET=T(B)<<B^(1/2-delta+o(1))
NEXT=Stage14-t2 quantitative moving-family attack
```
