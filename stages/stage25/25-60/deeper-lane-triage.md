# Stage25-60 deeper-lane triage

STATUS=R503_AUDITED_PASS_EXTERNAL_OR_BASE_CHANGE_GATE

The route IDs below are persistent allocations inherited from checkpoint50. They are not audit-round numbers and must not be renamed between audits.

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

## R501 / R502 / R507 — audited quarter-power families and rigidity

R501 and R502 are both audited family-specific `Theta(B^(1/4))` constructions. Their primitive-height loopholes are closed by exact bounded gcd certificates.

```text
R501_STATUS=PROVED_AUDITED_Theta_B_QUARTER
R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R507_STATUS=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
R502_EXACT_FAMILY_GROWTH=Theta(B^(1/4))
R502_GCD_GLOBAL_BOUND=2592
```

Historical checkpoint60 verifier compatibility markers describe the prior submission state only:

```text
HISTORICAL_R502_SUBMISSION_MARKER=R502_STATUS=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
HISTORICAL_R503_GATE_MARKER=R503_UNIFORM_VARYING_FIBER_HEIGHT_COUNT=NOT_PROVED
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
```

Neither family-specific `Theta(B^(1/4))` result is a global upper bound for `N2`.

## R503 — Yoshida uniform varying-fiber height

R503 has passed hostile fresh audit.

Yoshida's family

\[
E_{1,s}:y^2=x(x-(2s)^2)(x+(s^2-1)^2)
\]

is exactly the plus-sign Pythagorean/Frey family after

\[
(a,b,c)=(2s,s^2-1,s^2+1).
\]

The audited geometric Mordell-Weil input gives generic rank zero for this family over `Qbar(s)`. Therefore the original Yoshida surface has no non-torsion generic section.

Yoshida's explicit fixed-fiber infinitude construction starts from `s=5/3` and multiples `[n]P` of one non-torsion point. The source map from `alpha_n=x([n]P)` to the cuboid parameter `t_n` is Möbius, so fixed-curve canonical height gives

\[
h(t_n)=\Theta(n^2).
\]

The primitive cuboid contains the degree-two ratio `2t/(t^2-1)`, hence primitive physical height `<=B` forces

\[
n=O(\sqrt{\log B}).
\]

Likewise Yoshida's displayed sequence of infinitely many positive-rank `s` is a Möbius transform of the same `alpha_n`, hence only `O(sqrt(log X))` displayed parameters have rational height at most `X`.

Thus the paper's explicit infinitude mechanism is not a hidden polynomial-height population and cannot itself improve the current global `B^(1/4)` lower.

The route is not declared dead. It is reduced to a precise base-change/external theorem gate: a successful continuation must produce a low-degree multisection/base change with controlled physical height, or a quantitative theorem giving polynomially many exceptional positive-rank fibers carrying uniformly small non-torsion points.

```text
R503_STATUS=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R503_GENERIC_GEOMETRIC_MW_RANK=0
R503_NONTORSION_GENERIC_SECTION_EXISTS=false
R503_DIRECT_GENERIC_SECTION_ROUTE=CLOSED
R503_YOSHIDA_FIXED_FIBER_ORBIT_COUNT_UPPER=O(sqrt(log B))
R503_YOSHIDA_DISPLAYED_S_SEQUENCE_COUNT_UPPER=O(sqrt(log X))
R503_BASE_CHANGE_MULTISECTION_ROUTE=OPEN_GATE
R503_QUANTITATIVE_EXCEPTIONAL_FIBER_ROUTE=OPEN_GATE
R503_UNIFORM_SMALL_POINT_ROUTE=OPEN_GATE
R503_EXPONENT_UPGRADE_PROVED=false
```

See `r503-yoshida-generic-rank-zero-gate.md`, `r503-discovery-ledger.md`, and `r503-audit.md`.

## R504 — symmetric-k aggregation

The symmetric receiver

\[
p^4+q^4=(k^4+1)Z^2
\]

still has the previously accepted generic non-torsion moving section. An explicit rational section obtained from the third multiple is

\[
t_3(k)=\frac{k(k^8-6k^4-3)}{3k^8+6k^4-1},
\qquad
z_3(k)=\frac{k^{16}+28k^{12}+6k^8+28k^4+1}{(3k^8+6k^4-1)^2}.
\]

The current certified section does not beat exponent `1/4`, but R504 remains the highest-value repo-native route after R503's generic-section obstruction.

```text
R504_STATUS=LIVE_STRUCTURAL_NO_EXPONENT_UPGRADE_YET
R504_GENERIC_NONTORSION_SECTION_PROVED=true
R504_CURRENT_SECTION_BEATS_QUARTER=false
R504_RESEARCH_CONTINUES_AFTER_R503_AUDIT=true
```

## R505 — common squarefree core

The exact Stage19 squareclass receiver remains structurally correct, but no independent parameter dimension with polynomial physical-height bound and bounded multiplicity has yet been closed.

```text
R505_STATUS=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R505_RESEARCH_CONTINUES_AFTER_R503_AUDIT=true
```

## R506 — common-leg plus space

The common-leg divisor construction remains compatible. Successful low-dimensional specializations overlap known C17/R501-type mechanisms; no independent bulk count improving the global exponent has yet been certified.

```text
R506_STATUS=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R506_RESEARCH_CONTINUES_AFTER_R503_AUDIT=true
```

## Current boundary

```text
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
R503_FRESH_AUDIT_REQUIRED=false
LIVE_REPO_NATIVE_HIGH_VALUE_ROUTES_AFTER_R503=R504,R505,R506
CHECKPOINT60_SINGLE_SHOT=false
AUDIT_PASS_DOES_NOT_CLOSE_LIVE_ROUTES=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```
