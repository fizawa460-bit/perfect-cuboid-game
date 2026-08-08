# Stage14-t roadmap — triple-gate side track

## Purpose

Stage14-t is the dedicated side track for the triple/perfect-cuboid correction term in the Stage14 exactly-two-face problem. It is deliberately separated from the main `14-4` Kummer/rank-jump track and from the `14-e` ambient control track so the three lines can advance independently.

For the locked Stage14 population,

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B,
\]

let `T(B)` denote the primitive canonical cuboids for which all three face diagonals are integral. The exact raw-pair identity is

\[
\boxed{E(B)=N_2(B)+3T(B)},
\]

where `E(B)` is the Stage14 raw two-face-pair count and `N_2(B)` is the exactly-two population.

Thus any eventual raw-pair growth law transfers to `N_2(B)` only after the triple correction is controlled at the relevant scale.

## Frozen upstream contract

Stage14-t does not reopen the established Stage13 or Stage14 geometry. It may import the following locked facts.

- Stage13 upstream contract: `R03 + Stage13-12ag`.
- Stage14 raw-pair identity: `E(B)=N_2(B)+3T(B)`.
- Fixed first-face triple locus has genus `5`.
- Hence each fixed first-face fiber contributes only finitely many rational triple points.
- The Stage14 space-square surface is the level-4 Kummer model from `14-4ag`.
- The `14-4ah` working branch identifies the third-square condition as a generic degree-two relative cover of that Kummer surface, but no quantitative thin-set theorem is imported into Stage14-t unless and until it is merged and audited on `main`.
- No perfect-cuboid existence or nonexistence assumption is permitted.

Current boundary:

```text
T_O_SQRT_B_PROVED=false
UNIFORM_MOVING_BASE_TRIPLE_BOUND_PROVED=false
PERFECT_CUBOID_EXISTENCE_ASSUMED=false
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
```

## 14-t1 — definition, interfaces, finite baseline, literature boundary

Status: [>] Next.

Goal: create a self-contained triple-gate research interface before attempting a new theorem.

Tasks:

1. Freeze the exact definition of `T(B)` and its multiplicity in `E(B)=N_2(B)+3T(B)`.
2. Re-derive the fixed-base genus-5 model from the canonical Stage14 parametrization and record every exceptional/degenerate fiber separately.
3. Build an independent exact finite triple census using the existing Stage14 enumeration contract, with cross-checks against the raw-pair ledger through the current verified range.
4. Record the height translation from cuboid height `d<=B` to the natural coordinates on the moving genus-5 family.
5. Perform a literature-first audit of quantitative rational-point bounds applicable to a moving family of genus `>=2` curves: determinant-method bounds, uniformity results, gonality/degree methods, thin-cover counting, and any results specific to Euler/perfect cuboids.
6. State precisely which available theorem hypotheses are verified, which fail, and which missing uniformity statement would suffice for a useful bound on `T(B)`.
7. Do not promote a power saving from finite data.

Exit criterion: a reproducible triple census, a canonical family/height specification, and a theorem-gap ledger sufficient to choose the first quantitative attack.

## 14-t2 — moving-family quantitative attack

Status: [ ] Pending 14-t1.

Use the 14-t1 family and height audit to obtain the strongest unconditional global upper bound available for `T(B)`. Prefer a theorem whose constants/dependence on the moving base can be made explicit or uniformly controlled.

Targets, strongest first:

\[
T(B)\ll B^{1/2-\delta+o(1)}\quad(\delta>0),
\]

or at minimum

\[
T(B)=o(\sqrt B).
\]

If neither follows from current methods, prove the strongest weaker bound available and isolate the exact missing uniformity input.

## 14-t3 — exceptional fibers and low-degree subfamilies

Status: [ ] Pending 14-t2.

Classify parameter values where the generic genus-5 picture degenerates, acquires extra automorphisms, splits through lower-genus quotients, or admits low-degree maps capable of dominating the global triple count. Count these strata separately under the physical height.

This stage must distinguish genuine accumulating arithmetic subfamilies from coordinate/parametrization boundary artifacts.

## 14-t4 — Kummer-cover comparison

Status: [ ] Pending 14-t3 and merged 14-4ah/descendants.

Compare the moving genus-5 formulation with the relative degree-two third-square cover of the Stage14 Kummer surface. Determine whether the Kummer height and its accumulating curves provide a sharper global triple bound than the fiberwise approach.

In particular, audit the restriction of the third-square cover to any low-degree physical rational curves identified by the main `14-4` track.

## 14-t5 — transfer theorem to exactly-two count

Status: [ ] Pending a sufficient triple bound and a main-track raw-pair law.

Combine the strongest proved estimate for `T(B)` with

\[
N_2(B)=E(B)-3T(B).
\]

If the main track proves a `sqrt(B)`-scale raw-pair law and Stage14-t proves `T(B)=o(sqrt(B))`, transfer the leading growth law to the exactly-two population. If the triple term survives at the same scale, compute or bound its contribution instead of discarding it.

## Scope boundary

Stage14-t is not a search for a single perfect cuboid and is not permitted to infer nonexistence from a zero finite census. Its purpose is quantitative control of the entire triple population under the same primitive canonical physical height used by Stage14.

It also does not duplicate `14-e8`: `14-e8` studies the Euler-brick thin set in the ambient control population, while Stage14-t studies the triple correction inside the integer-space-diagonal Stage14 population.

```text
STAGE14_T_TRACK=DEFINED
STAGE14_T1=NEXT
TRIPLE_GATE_IDENTITY=E(B)=N2(B)+3T(B)
PRIMARY_TARGET=T(B)=o(sqrt(B))
STRONG_TARGET=T(B)<<B^(1/2-delta+o(1))
FINITE_ZERO_IMPLIES_NONEXISTENCE=false
NEXT=Stage14-t1 definition/interfaces/finite baseline/literature boundary
```
