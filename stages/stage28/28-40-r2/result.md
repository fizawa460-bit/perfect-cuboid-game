# Stage28-40-r2 — maximal post-merge deepening result

```text
TASK_ID=Stage28-40-r2
CHECKPOINT=40
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=REPAIRED_PENDING_FRESH_REAUDIT
PRIOR_CHECKPOINT40_PR=1276
PRIOR_CHECKPOINT40_MERGE=deddf8c0917fc30f46d6701ef790e6872186c61b
PRIOR_R2_AUDIT=FAIL_REPAIR_REQUIRED_ON_HEAD_c59a9e7028b70599eba3cdacad193940e06e58fa
REPAIR_RECORD=stages/stage28/28-40-r2/repair.md
```

## 1. Strongest numerical bridge upper is unchanged

The current certified Stage28 upper corridor remains

\[
\boxed{
\frac{M_3(B)}{N_2(B)}
=o\!\left(B^{3/4}(\log B)^{5-\delta}\right)
}
\qquad(0<\delta<1/46).
\]

No r2 route improves this numerical theorem or resolves the asymptotic ordering.

```text
CHECKPOINT40_R2_NUMERIC_UPPER_IMPROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
```

## 2. New theorem: exact geometric branch profiles differ

On the same `Y=Bl_4(P1xP1)` base, both completion covers have degree `2` and total branch class `-2K_Y`, but r2 proves the geometric decompositions

\[
\boxed{D_{\rm sp}=C_1+C_2+C_3+C_4,\quad g(C_j)=0}
\]

versus

\[
\boxed{D_{\rm face}=E_1+E_2,\quad g(E_j)=1.}
\]

The U10 proof has been repaired after hostile audit: the Stage19 branch factorization is now explicitly the product of all four bilinear factors, and direct expansion recovers exactly `F_sp/4`.  The old false `+` display is not used on the repaired head.

```text
SPACE_BRANCH_PROFILE=4x_rational_1_1
THIRD_FACE_BRANCH_PROFILE=2x_genus1_anticanonical
BASE_AUTOMORPHISM_IDENTIFICATION=false
U10_FACTORISATION_REPAIRED=true
U10_EXACT_EXPANSION_CHECK=PASS
```

Moreover the two radicands represent different squareclasses in `Qbar(Y)^*/Qbar(Y)^{*2}`, so the two quadratic covers are not the same extension over the fixed base and are not base-preservingly birational.  U13 was reread after the U10 repair and requires no claim change.

## 3. New theorem: exact local quotient has only finite Euler-product bias

The exact local acceptances satisfy

\[
\frac{\alpha_p}{\beta_p}
=(1-\chi_4(p)/p)^2(1+O(p^{-2})).
\]

After the `L(1,chi_4)^{-2}` factor and fixed bad-prime correction are removed, the remaining relative Euler product converges absolutely to a positive finite constant.

Hence the known good-prime marginal laws differ only by a finite local constant after the quadratic-character oscillation is normalized:

```text
RELATIVE_LOCAL_POLYNOMIAL_DRIFT=0
RELATIVE_LOCAL_FIRST_ORDER_LOG_DRIFT=0
RELATIVE_LOCAL_EULER_CONSTANT_EXISTS=true
```

A truncation through `p<=10^6` gives a diagnostic quotient near `2.1123`; this is not a global Stage28 constant and is not used for ordering.

## 4. New literature adaptation: Stage19 gets the same explicit Huang thin-cover eta range

Huang v3 Theorem 1.6(1), using the actual Stage19 degree-two space cover over the common toric base with `r=6`, `dim=2`, gives for every fixed

\[
0<\eta<1/46
\]

\[
\boxed{N_2(B)\ll_\eta B(\log B)^{5-\eta}.}
\]

Stage20 already has the same range

\[
\boxed{M_3(B)\ll_\eta B(\log B)^{5-\eta}}
\qquad(0<\eta<1/46)
\]

from Stage14-e11 / PR #188.

Thus even the explicit generic degree-two thin-cover theorem sees no exponent-level distinction between the two completions.

This is an independent, weaker Stage19 upper and does not replace

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

## 5. Kummer route remains blocked at the exact physical height

The space cover is the merged Stage14 Kummer model, but its exact physical line bundle is big and nef, not ample.  McKinnon's Kummer counting theorem assumes an ample height, so the sharper branch decomposition does not legalize direct transfer.

```text
KUMMER_STRUCTURE_RELEVANT=true
MCKINNON_DIRECT_TRANSFER=false
AMPLENESS_ADAPTER_FOUND=false
```

## 6. What checkpoint40 has now localized

The Stage19/Stage20 difference is **not currently explained by**:

- independent endpoint upper bounds;
- finite data;
- first-order local sieve dimension;
- growing-prime local sieve availability;
- a local power or log-power Euler-product drift;
- cover degree;
- total branch divisor class;
- K3 canonical type;
- Huang's generic degree-two thin-cover exponent range;
- a hidden equality of the two quadratic extensions over the base.

The first sharp geometric difference now appears at the branch-component level:

```text
Stage19 space: 4 rational components
Stage20 third face: 2 genus-one components
```

Turning that difference into a physical-height count comparison requires a genuinely new global arithmetic theorem.

## 7. Final r2 receiver

```text
OPEN_GATE_40_R2=DistinctBranchProfileDoubleCoverMarginalComparison
COMMON_HOST=Y=Bl_4(P1xP1)
SOURCE_MARGINAL=N2
TARGET_MARGINAL=M3
CUTOFF=R<=B
SPACE_BRANCH_PROFILE=4x_genus0
THIRD_FACE_BRANCH_PROFILE=2x_genus1
REQUIRED_STRENGTH=strictly_improve_bridge_upper_or_resolve_asymptotic_ordering
ENDPOINT_COUNT_FORBIDDEN=true
RESEARCH_REQUEST_READY=true
```

Acceptable future theorem species include a physical-height rational-lift comparison sensitive to branch-component arithmetic, a cover-specific dispersion theorem, or a marginal energy theorem that avoids inserting the perfect-cuboid joint count.

## 8. Stop reason and audit state

U1-U14 cover the materially distinct repo-native checkpoint40 lanes presently available.  The hostile audit agreed conditionally with the maximal-bounded-exploration and research-request-ready claims, but failed the old head only because U10 displayed the wrong algebraic operation.  That display has now been repaired without changing the mathematical claims.

The repaired head does not self-award audit PASS.

```text
MATERIALLY_DISTINCT_ROUTES_TOTAL=14
CHECKPOINT40_MAXIMAL_BOUNDED_EXPLORATION_CLAIM=SUBMITTED_FOR_REAUDIT
U10_REPAIR_COMPLETED=true
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING_FRESH_REAUDIT_AFTER_REPAIR
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=50
NEXT_EXPECTED_COMMAND=Stage28-audit
PERFECT_CUBOID_CONCLUSION=NONE
```
