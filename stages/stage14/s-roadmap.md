# Stage14-s roadmap — Selmer / rank-jump arithmetic track

## Purpose

Stage14-s is the dedicated arithmetic side track for the positive-rank specialization bottleneck in the Stage14 exactly-two-face problem. It is separate from:

- the main `14-4` Kummer / low-degree rational-curve track;
- the `14-t` triple/perfect-cuboid correction track;
- the `14-e` ambient control track.

The main track has already reduced the raw-pair growth exponent to the growth exponent of active Pythagorean first-face states. For a genuine Pythagorean base state `F`,

\[
\mu(F)<\infty
\iff
\operatorname{rank}E_F(\mathbf Q)>0,
\]

where `mu(F)` is the least physical raw-pair height on that fiber, and

\[
E_t:\quad Y^2=X(X-1)(X+t^2),
\qquad
t=\frac{2r}{1-r^2}.
\]

Thus Stage14-s asks two distinct questions:

1. how often does this Pythagorean-base family have positive Mordell--Weil rank?;
2. among positive-rank fibers, how often is the first non-torsion point small enough to satisfy the physical cutoff `mu(F)<=B`?

The finite active-vertex data

```text
B           V(B)     V(B)/sqrt(B)
200,000      155      0.34659
500,000      254      0.35921
1,000,000    347      0.34700
2,000,000    490      0.34648
```

show a strong finite square-root signal, but Stage14-s must not assume that `sqrt(B)` is the true order.

## Frozen upstream contract

Stage14-s may use the merged Stage14 results through `14-4ah`, including:

- exact two-face parametrization and multiplicity one;
- the physical one-fiber height interface `v asymp sqrt(Bg/S1)`;
- the Pythagorean-base elliptic K3 with geometric generic Mordell--Weil rank zero;
- rational torsion `Z/2 x Z/4` on genuine physical fibers, with all torsion points nonphysical;
- the active rank-jump graph and the theorem that raw-pair edges and active vertices have the same limsup/liminf polynomial growth exponents;
- the exact physical Kummer polarization `M`, with `H_M=d` on the arithmetic open set.

It may also use the frozen Stage13 `R03 + Stage13-12ag` contract where relevant, but it must not import an unproved independence model for local Selmer conditions.

```text
POSITIVE_RANK_SPECIALIZATION_FREQUENCY_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
UNIFORM_SMALL_POINT_DISTRIBUTION_PROVED=false
ROOT_NUMBER_PARITY_USED_AS_RANK_EQUALITY=false
SELMER_RANK_USED_AS_MW_RANK_EQUALITY=false
```

## 14-s1 — exact descent interface and finite Selmer audit

Status: [>] Next.

Purpose: construct a completely explicit descent interface for

\[
E_t:Y^2=X(X-1)(X+t^2)
\]

on the actual Pythagorean base `t=2r/(1-r^2)`, and determine exactly which arithmetic data can be computed uniformly before any density argument.

Required tasks:

1. Choose and lock an explicit `2`-descent and/or pair of `2`-isogeny descents adapted to the full rational `2`-torsion.
2. Write the covering curves, square-class parameters and local-solubility conditions in a form whose coefficient heights can be bounded in terms of primitive Pythagorean base data.
3. Separate rigorously:
   - Mordell--Weil rank;
   - `2`-Selmer rank;
   - Tate--Shafarevich contribution;
   - root-number parity information.
4. Identify all automatically soluble or impossible local states at `p=2`, at primes dividing the Pythagorean parameters, and at odd primes away from the discriminant.
5. Build a deterministic finite audit over the already-frozen active/inactive first-face sample through the Stage14 ceiling. The audit should compare:
   - active status `mu(F)<infinity` from exact Stage14 enumeration;
   - computed Selmer upper bounds;
   - root numbers where available;
   - first physical point height for active fibers.
6. Determine whether the finite `sqrt(B)` signal is already visible at the level of a simple Selmer/local-solubility sieve, or whether the decisive thinning happens only at the small-point stage.
7. Refresh the primary literature before promoting any descent formula, average-Selmer theorem, parity statement or density claim.

Expected artifacts:

```text
stages/stage14/14-s1/result.md
stages/stage14/14-s1/literature-selmer-audit.md
stages/stage14/scripts/14-s1/selmer_interface_audit.py
stages/stage14/data/14-s1/selmer_interface_audit.json
.github/workflows/stage14-s1-selmer-interface.yml
```

Minimum acceptable outcome if no useful density theorem is available:

```text
STAGE14_S1=COMPLETE_EXACT_DESCENT_INTERFACE
SELMER_LOCAL_CONDITIONS_LOCKED=true
FINITE_ACTIVE_INACTIVE_SELMER_AUDIT_COMPLETE=true
POSITIVE_RANK_DENSITY_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-s2 Pythagorean-base Selmer/local-density sieve
```

## 14-s2 — Pythagorean-base Selmer and local-density sieve

Status: [ ] Pending s1.

Use the exact s1 descent interface to count or bound primitive Pythagorean bases that survive the necessary local conditions for positive rank.

Primary targets:

- derive an unconditional upper bound for the number of Selmer-admissible Pythagorean bases under the physical first-face height;
- determine whether local conditions alone give a power saving;
- if an average `2`-Selmer theorem applies to this thin/base-changed family, verify every hypothesis explicitly rather than importing a generic-family heuristic;
- classify exceptional congruence families separately.

A successful s2 should produce a theorem-level bound on a rank-jump candidate set, but must not equate nontrivial Selmer with positive Mordell--Weil rank.

## 14-s3 — first-small-point / regulator gate

Status: [ ] Pending s2.

Positive rank is only a necessary condition for an active Stage14 vertex. Translate the physical condition

\[
\mu(F)\le B
\]

into descent coordinates, canonical height and/or regulator data.

Targets:

- derive uniform inequalities connecting the first physical `q`-height to canonical height on `E_t`;
- quantify how often a positive-rank specialization has a non-torsion point below the Stage14 cutoff;
- determine whether the finite square-root signal is primarily a rank-jump-frequency phenomenon or a small-generator-height phenomenon;
- prove the strongest unconditional upper/lower envelope for `V(B)` available from the combined s1/s2/s3 machinery.

No `sqrt(B)` law is promoted unless both rank-frequency and small-point gates are controlled.

## 14-s4 — compare with the `M`-degree-4 bisection mechanism

Status: [ ] Pending the relevant merged `14-4ai+` results and s3.

The main track's extremal geometric mechanism is a `Q`-rational `M`-degree-4 bisection. Stage14-s4 will identify the descent/Selmer classes traced by every physical degree-four bisection found by the main track.

Questions:

- do finitely many explicit Selmer classes account for the dominant active vertices?;
- do degree-four bisections explain essentially all `B^(1/2)`-scale first hits, if that scale survives?;
- are there rank-jump fibers outside the bisection loci with the same polynomial order?;
- can the arithmetic and Kummer descriptions be proved equivalent on the dominant strata?

## 14-s5 — rank-jump counting synthesis

Status: [ ] Pending s4.

Combine the strongest arithmetic and geometric results into a single theorem-level statement for

\[
V(B)=\#\{F:\mu(F)\le B\}.
\]

Possible outcomes include:

- a proved `V(B)=B^{1/2+o(1)}` order;
- a sharper asymptotic with explicit accumulating classes;
- a different growth exponent;
- or a rigorous upper/lower envelope explaining exactly why the square-root candidate remains unresolved.

Any result then returns to the main Stage14 track through the already-proved edge/vertex exponent equivalence.

## Literature / proof discipline

Every s-stage must distinguish theorem from finite evidence and must audit primary sources before using:

- explicit full-`2`-torsion descent formulas;
- average Selmer results;
- root-number averages and parity conjectures;
- rank-distribution results in elliptic families;
- specialization theorems;
- canonical-height/regulator bounds.

In particular:

```text
ROOT_NUMBER=-1 => POSITIVE_RANK
```

may only be used when justified by an unconditional theorem in the precise setting; parity conjectures are not silently assumed. Likewise, `Sel_2` dimension is only an upper bound for Mordell--Weil rank unless the Tate--Shafarevich contribution is controlled.

## Scope boundary

Stage14-s does not duplicate `14-t`: it studies the occurrence and size of non-torsion points on the raw-pair elliptic fibers, not the genus-5 triple/perfect-cuboid correction.

It does not duplicate `14-4ai`: the main track classifies low-degree curves on the Kummer surface, while Stage14-s studies the arithmetic frequency of positive-rank specializations and the first-small-point gate. The tracks are designed to meet at `s4`.

```text
STAGE14_S_TRACK=DEFINED
PRIMARY_OBJECT=ACTIVE_PYTHAGOREAN_BASES
PRIMARY_COUNT=V(B)
S1_TARGET=EXACT_2_DESCENT_SELMER_INTERFACE
S2_TARGET=PYTHAGOREAN_BASE_LOCAL_SELMER_SIEVE
S3_TARGET=FIRST_SMALL_POINT_GATE
S4_TARGET=BISECTION_SELMER_CLASS_COMPARISON
S5_TARGET=RANK_JUMP_COUNTING_SYNTHESIS
NEXT=Stage14-s1 exact descent interface and finite Selmer audit
```
