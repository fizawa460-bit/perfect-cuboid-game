# Stage14-s roadmap — Selmer / rank-jump arithmetic track

## Purpose

Stage14-s is the arithmetic side track for the positive-rank specialization and first-small-point bottlenecks in the Stage14 exactly-two-face problem. It is separate from:

- main `14-4`: Kummer / low-degree rational-curve geometry;
- `14-t`: triple/perfect-cuboid correction;
- `14-e`: ambient no-space-square control.

For a genuine Pythagorean first-face state `F`, merged Stage14 gives

\[
\mu(F)<\infty\iff \operatorname{rank}E_F(\mathbf Q)>0,
\]

with

\[
E_t:Y^2=X(X-1)(X+t^2),\qquad t=\frac{2r}{1-r^2}.
\]

The finite active count still shows the unresolved square-root signal

```text
B           V(B)     V(B)/sqrt(B)
200,000      155      0.34659
500,000      254      0.35921
1,000,000    347      0.34700
2,000,000    490      0.34648
```

Stage14-s must separate two gates:

1. frequency of positive Mordell--Weil rank on the Pythagorean base;
2. frequency of a first non-torsion point small enough to satisfy `mu(F)<=B`.

No square-root law is assumed.

## Frozen upstream contract

Stage14-s may use merged Stage14 through `14-4ah`, including the exact two-face parametrization, physical fiber height, generic rank-zero Pythagorean-base K3, nonphysical torsion, active rank-jump graph, raw-edge/active-vertex exponent equivalence, and exact physical Kummer height `H_M=d`.

It may also use frozen Stage13 `R03 + Stage13-12ag` where relevant, but it must not import unproved Selmer independence, parity, BSD, or generic-family density heuristics.

```text
POSITIVE_RANK_SPECIALIZATION_FREQUENCY_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
UNIFORM_SMALL_POINT_DISTRIBUTION_PROVED=false
ROOT_NUMBER_PARITY_USED_AS_RANK_EQUALITY=false
SELMER_RANK_USED_AS_MW_RANK_EQUALITY=false
```

## 14-s1 — exact descent interface and finite Selmer/rank-bound audit

Status: [x] Complete.

For a primitive oriented Pythagorean face

\[
F=(S,X,H),\qquad S^2+X^2=H^2,
\]

s1 locks the integral full-2-torsion model

\[
\boxed{E_F:Y^2=Z(Z-S^2)(Z+X^2)}.
\]

The exact split Kummer interface is

\[
[P]\mapsto(Z,Z-S^2,Z+X^2)
\in(\mathbf Q^*/\mathbf Q^{*2})^3,
\]

with covering equations

\[
\boxed{d_1u_1^2-d_2u_2^2=S^2},
\qquad
\boxed{d_3u_3^2-d_1u_1^2=X^2},
\]

and `d1*d2*d3` square. The integral discriminant is

\[
\boxed{\Delta=16S^4X^4H^4},
\]

so only infinity and primes dividing `2SXH` enter nontrivial local 2-cover analysis.

The deterministic finite audit uses PARI/GP `ellrank(E,0)` on a height-stratified sample of 96 active and 96 inactive-control fibers through `B=2,000,000`. For full rational 2-torsion, PARI's documented relation gives

\[
\dim Sel_2(E)=r_2+2+s,
\]

where `[r1,r2,s,L]` is the unconditional `ellrank` output.

Finite summary:

```text
                         active  inactive control
sample size                 96        96
exact rank interval          92        85
certified positive rank      95        54
certified rank zero           0        33
Sel_2 rank > torsion          96        80
root number -1               60        50
mean Sel_2 rank            3.8125    3.4166666667
mean rank upper bound      1.4583    0.8333333333
```

The key finite diagnostic is that 80/96 inactive controls still have nontrivial 2-Selmer beyond torsion, and 54/96 already have certified positive Mordell--Weil rank while no physical partner appears below `2m`. Therefore local/Selmer survival alone does not explain activity in this finite sample; the first-small-point gate is high priority. This is finite evidence only.

Artifacts:

```text
stages/stage14/14-s1/result.md
stages/stage14/14-s1/literature-selmer-audit.md
stages/stage14/scripts/14-s1/selmer_interface_audit.py
stages/stage14/data/14-s1/selmer_interface_audit.json
.github/workflows/stage14-s1-selmer-interface.yml
```

Decision:

```text
STAGE14_S1=COMPLETE_EXACT_DESCENT_INTERFACE_AND_FINITE_PARIRANK_AUDIT
EXACT_FULL_2_TORSION_DESCENT_INTERFACE_LOCKED=true
PARI_UNCONDITIONAL_RANK_BOUNDS_AUDITED=true
FINITE_ACTIVE_INACTIVE_SELMER_AUDIT_COMPLETE=true
FINITE_SELMER_ONLY_GATE_SEPARATES_ACTIVITY=false
FINITE_POSITIVE_RANK_INACTIVE_CONTROLS=54_OF_96
FINITE_SMALL_POINT_GATE_PRIORITY=HIGH
SELMER_RANK_USED_AS_MW_RANK_EQUALITY=false
ROOT_NUMBER_PARITY_USED_AS_RANK_EQUALITY=false
POSITIVE_RANK_DENSITY_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

## 14-s2 — Pythagorean-base Selmer and local-density sieve

Status: [>] Next.

Use the exact s1 local support and covering interface to count or bound primitive Pythagorean bases surviving the necessary local conditions.

Targets:

- compute the prime-by-prime local states at `2` and primes dividing `SXH`;
- derive the strongest unconditional upper bound for Selmer-admissible Pythagorean bases under the physical first-face height;
- determine whether local conditions alone give any power/logarithmic saving;
- verify every hypothesis before importing an average-2-Selmer theorem for this thin/base-changed family;
- classify exceptional congruence families separately;
- retain the s1 warning that nontrivial Selmer, and even positive rank, need not imply `mu(F)<=B`.

A successful s2 produces a theorem-level bound on a rank-jump candidate set, never an equality between Selmer survival and positive Mordell--Weil rank.

## 14-s3 — first-small-point / regulator gate

Status: [ ] Pending s2.

Translate

\[
\mu(F)\le B
\]

into descent coordinates, canonical height, regulator and/or first-generator height.

Targets:

- uniform inequalities connecting physical `q`-height and canonical height;
- quantify positive-rank fibers whose first non-torsion point lies below the Stage14 cutoff;
- explain the s1 observation that many positive-rank inactive controls remain physically inactive through `2m`;
- prove the strongest unconditional upper/lower envelope for `V(B)` from s1+s2+s3.

## 14-s4 — compare with the `M`-degree-4 bisection mechanism

Status: [ ] Pending relevant merged `14-4ai+` and s3.

Identify the descent/Selmer classes traced by every physical `M`-degree-4 bisection found by the main track. Test whether finitely many bisection classes dominate any surviving `B^(1/2)` first-hit population or whether equal-order rank-jump fibers remain outside them.

## 14-s5 — rank-jump counting synthesis

Status: [ ] Pending s4.

Combine the arithmetic and geometric results into a theorem-level statement for

\[
V(B)=\#\{F:\mu(F)\le B\}.
\]

Possible outcomes remain a proved `B^{1/2+o(1)}` order, a sharper accumulating-class asymptotic, a different exponent, or a rigorous upper/lower envelope explaining the unresolved square-root signal.

## Proof discipline

Every s-stage must distinguish theorem from finite evidence and audit primary sources before using explicit descent formulas, average Selmer results, root-number/parity claims, rank-distribution theorems, specialization theorems, or canonical-height/regulator estimates.

In particular, root number is never silently converted into Mordell--Weil rank parity, and `Sel_2` dimension is never identified with Mordell--Weil rank unless the Tate--Shafarevich contribution is controlled.

## Scope boundary

Stage14-s does not duplicate `14-t`; it studies non-torsion points on raw-pair elliptic fibers, not the genus-5 triple correction. It does not duplicate `14-4ai`; the main track classifies low-degree Kummer curves, while Stage14-s studies arithmetic specialization frequency and first-small-point height. They meet at s4.

```text
STAGE14_S_TRACK=ACTIVE
STAGE14_S1=COMPLETE_EXACT_DESCENT_INTERFACE_AND_FINITE_PARIRANK_AUDIT
PRIMARY_OBJECT=ACTIVE_PYTHAGOREAN_BASES
PRIMARY_COUNT=V(B)
S2_TARGET=PYTHAGOREAN_BASE_LOCAL_SELMER_SIEVE
S3_TARGET=FIRST_SMALL_POINT_GATE
S4_TARGET=BISECTION_SELMER_CLASS_COMPARISON
S5_TARGET=RANK_JUMP_COUNTING_SYNTHESIS
NEXT=Stage14-s2 Pythagorean-base Selmer/local-density sieve
```
