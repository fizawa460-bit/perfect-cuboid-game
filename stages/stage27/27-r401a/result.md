# Stage27-r401a — localization of the half-power upper to the critical wall

```text
TASK_ID=Stage27-r401a
SUBLANE_ID=Stage27-r401a
OWNER_STAGE=Stage27
RESEARCH_LOCATION=LOCAL
AFFECTED_SOURCE_STAGE=NONE
AFFECTED_SOURCE_STAGES=NONE
TRIGGER_CHECKPOINT=40
ROUTE_SERIAL=01
RESEARCH_QUESTION=Where can the Stage14 half-power host actually saturate?
INPUTS=Stage14 Proposition 3.3 and Proposition 3.6; Stage27-40 audited bottleneck ledger
EXPECTED_OUTPUT=Same-measure critical-band localization or a strict sub-half theorem
STOP_CONDITION=Critical band isolated with exact sufficient next theorem contract
AUDIT_REQUIRED=true
DOWNSTREAM_REAUDIT_REQUIRED=Stage27
```

## Authorization

PR #1025 merged checkpoint40 hostile-audit PASS at `b76ebce08c5a90ed23bbd92762960ce719d3c718`. This route remains inside checkpoint40 and does not authorize checkpoint50.

## Fixed-width localization

In the nonproportional balanced packet Stage14 gives

\[
E_k\le 3\theta-\frac14\quad(\theta\le1/4),
\qquad
E_{\rm RRF}\le1-2\theta\quad(\theta\ge1/4,\ \chi\le1/4),
\]

while `chi>1/4` cells are empty and the proportional branch has exponent at most `7/16`.

Fix \(0<\gamma<1/16\). If \(\theta\le1/4-\gamma\), then

\[
E_k\le\frac12-3\gamma.
\]

If \(\theta\ge1/4+\gamma\), then every nonempty cell has

\[
E_{\rm RRF}\le\frac12-2\gamma.
\]

Consequently the union of all cells outside the critical band

\[
\left|\theta-\frac14\right|<\gamma
\]

satisfies the already available fixed-power bound

\[
\boxed{N_{2,\mathrm{off}(\gamma)}(B)\ll B^{1/2-2\gamma+o(1)}}.
\]

This uses no new sieve, independence assumption, or changed measure. The `B^{o(1)}` number of decorated/dyadic cells is absorbed after fixed \(\gamma\).

## Exact critical wall

At \(\theta=1/4\), the feasible-domain inequalities force

\[
\frac18\le\phi\le\frac14,
\qquad
\chi=2\phi-\frac14\in[0,1/4].
\]

Moreover

\[
\alpha,\beta,\gamma,\delta=B^{1/4+o(1)}.
\]

Thus the obstruction is not the full Stage14 host: it is the fully balanced four-coefficient wall, across the remaining physical interval \(1/8\le\phi\le1/4\). On this wall all three available complete-host estimates saturate:

\[
E_k=\frac12,
\qquad
E_{\rm RRF}=\frac12,
\qquad
E_s=\max(2\theta,1-2\theta)=\frac12.
\]

Taking the minimum of existing hosts therefore gives no further gain. A strict global sub-square-root theorem is reduced to a same-measure fixed-power deficit on arbitrarily thin fixed neighborhoods of this wall.

## Exact next theorem contract

It is sufficient to prove that some fixed \(\gamma,\delta>0\) satisfy

\[
N_{2,\,|\theta-1/4|<\gamma}(B)
\ll_\varepsilon B^{1/2-\delta+\varepsilon}.
\]

Combined with the off-wall theorem above, this would give

\[
N_2(B)\ll_\varepsilon
B^{1/2-\min(2\gamma,\delta)+\varepsilon}.
\]

The next attack must therefore exploit an arithmetic correlation specific to the fully balanced wall—such as the common-core/root-line/reduced-column coupling on the same decorated physical cells—not improve a generic vertical fiber or reuse the logarithmic local tensor alone.

```text
CHECKPOINT_ADVANCED_TO_50=false
CRITICAL_WALL=theta=1/4
CRITICAL_PHI_INTERVAL=[1/8,1/4]
CRITICAL_CHI_INTERVAL=[0,1/4]
ALL_FOUR_COEFFICIENT_FACTORS_BALANCED=true
OFF_WALL_FIXED_POWER_SAVING_PROVED=true
OFF_WALL_EXPONENT=1/2-2gamma+o(1)
EXISTING_HOST_MINIMUM_IMPROVES_CRITICAL_WALL=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
NEXT_ROUTE_RECEIVER=FULLY_BALANCED_WALL_COMMON_CORE_ROOT_LINE_COLUMN_CORRELATION
FINITE_DATA_USED_AS_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage27-audit
```
