# Stage25-60 deeper-lane triage

STATUS=ACTIVE_CHECKPOINT60_CONTINUATION

The route IDs below are persistent allocations inherited from checkpoint50. They are not checkpoint60 round numbers and must not be renamed between audits.

## Route registry

```text
R501=Meskhishvili_first_positive_power_family
R502=Meskhishvili_third_parametrization_fallback
R503=Yoshida_uniform_varying_fiber_height
R504=symmetric_k_aggregation
R505=common_squarefree_core
R506=common_leg_plus_space
R507=R501_primitive_height_rigidity
```

## R502 — Meskhishvili third parametrization

The third displayed NPC parametrization has the same maximal homogeneous degree eight as R501. The same two-dimensional reduced rational parameter count at degree-eight height can reproduce an exponent `1/4`, but without an additional cancellation, new parameter dimension, or smaller physical height it cannot improve the exponent.

```text
R502_STATUS=SAME_EXPONENT_FALLBACK
R502_EXPONENT_UPGRADE_PROVED=false
```

## R503 — Yoshida uniform varying-fiber height

This remains the highest-value live lane for an exponent above `1/4`.

The available elliptic-surface structure supplies infinitely many rational parameters with positive rank and a finite-to-one map into rational face-cuboid similarity classes. What is still missing for the exact Stage19 lower is a uniform varying-fiber rational-point count with physical height control and the primitive/canonical/exactly-two adapter.

The required theorem species must simultaneously control:

1. the height of the base parameter `s`;
2. canonical height / coordinate height of a non-torsion point on the fiber `E_s`;
3. the resulting cuboid space height `d`;
4. multiplicity of the elliptic-data-to-cuboid map;
5. exceptional third-face-square fibers/points;
6. primitive reduction without an unbounded height collapse.

Stage14/15 Q03 and Q05 show that positive rank or local solubility alone is not enough; a uniform small-point/height theorem is the missing load-bearing input.

```text
R503_STATUS=LIVE_HIGH_VALUE_EXTERNAL_THEOREM_GATE
R503_UNIFORM_VARYING_FIBER_HEIGHT_COUNT=NOT_PROVED
R503_POSITIVE_RANK_ALONE_SUFFICIENT=false
R503_RESEARCH_CONTINUES_AFTER_CURRENT_AUDIT=true
```

## R504 — symmetric-k aggregation

The symmetric receiver

\[
p^4+q^4=(k^4+1)Z^2
\]

has the rational base point `t=q/p=k`. At `k=2` this is the audited positive-rank C17 member. Specialization proves that the generic section is non-torsion.

An explicit rational section obtained from the third multiple is

\[
t_3(k)=\frac{k(k^8-6k^4-3)}{3k^8+6k^4-1},
\]

\[
z_3(k)=\frac{k^{16}+28k^{12}+6k^8+28k^4+1}{(3k^8+6k^4-1)^2},
\]

and satisfies identically

\[
t_3(k)^4+1=(k^4+1)z_3(k)^2.
\]

This proves a genuine moving non-torsion section, but the presently certified numerator/denominator degrees produce physical height growth too expensive to beat R501's exponent `1/4` with the currently available parameter count.

```text
R504_STATUS=LIVE_STRUCTURAL_NO_EXPONENT_UPGRADE_YET
R504_GENERIC_NONTORSION_SECTION_PROVED=true
R504_CURRENT_SECTION_BEATS_QUARTER=false
R504_RESEARCH_CONTINUES_AFTER_CURRENT_AUDIT=true
```

## R505 — common squarefree core

The exact Stage19 squareclass receiver is structurally correct, but no independent parameter dimension with a polynomial physical-height bound and bounded multiplicity has been closed yet.

```text
R505_STATUS=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R505_RESEARCH_CONTINUES_AFTER_CURRENT_AUDIT=true
```

## R506 — common-leg plus space

The common-leg divisor construction remains a compatible receiver. Its successful low-dimensional specializations overlap known C17/R501-type mechanisms; no independent bulk count improving the global exponent has yet been certified.

```text
R506_STATUS=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R506_RESEARCH_CONTINUES_AFTER_CURRENT_AUDIT=true
```

## R507 — R501 primitive-height rigidity

Checkpoint60 proves the exact bounded primitive gcd and the reverse parameter-height count, closing the possibility that R501 itself secretly grows faster than `B^(1/4)` after primitive reduction.

```text
R507_STATUS=SUBMITTED_FOR_FRESH_AUDIT
R501_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R501_HIDDEN_GCD_EXPONENT_UPGRADE=false
```

## Current boundary

```text
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
LIVE_HIGH_VALUE_ROUTES=R503,R504,R505,R506
CHECKPOINT60_SINGLE_SHOT=false
AUDIT_PASS_DOES_NOT_CLOSE_LIVE_ROUTES=true
STAGE70_ALLOWED=false
```
