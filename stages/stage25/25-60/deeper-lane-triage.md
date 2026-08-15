# Stage25-60 deeper-lane triage

STATUS=R504_SUBMITTED_FOR_FRESH_AUDIT

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

## R503 — Yoshida varying-fiber height

R503 passed hostile fresh audit and is now a precise theorem gate.

The Yoshida surface has generic geometric Mordell-Weil rank zero, so the direct generic-section route is closed. Its displayed fixed-fiber orbit and displayed positive-rank-parameter sequence are each only `O(sqrt(log))` in the relevant bounded-height variable. This does not close base changes or exceptional positive-rank fibers.

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

R504 has now been pushed through the full original-base section lattice.

The quartic receiver

\[
t^4+1=(k^4+1)z^2
\]

has Jacobian

\[
E_F:Y^2=X^3-4(k^4+1)^2X.
\]

This is the quadratic twist of the constant lemniscatic curve `v^2=u^3-4u` by `k^4+1`. The twisting cover `s^2=k^4+1` is itself `Q`-birational to that same constant elliptic curve. The deck involution becomes `Q -> T-Q`, and the anti-invariant twist descent together with `End_Q(E0)=Z` gives

\[
\boxed{\operatorname{rank}E_F(Q(k))=1.}
\]

Thus there is no second independent `Q(k)`-rational section hidden on the original symmetric-k surface.

The first nondegenerate physical section is the already accepted 3P section

\[
t_3(k)=\frac{k(k^8-6k^4-3)}{3k^8+6k^4-1},
\qquad
z_3(k)=\frac{k^{16}+28k^{12}+6k^8+28k^4+1}{(3k^8+6k^4-1)^2}.
\]

For reduced `k=u/v`, its homogenized Stage19 coordinates have degree 20 and exact primitive gcd

\[
\gcd(E,X,Y)=2^{7[u,v\text{ both odd}]}\le128.
\]

The missing third-face square condition reduces to a squarefree degree-32 hyperelliptic curve of genus 15, so only finitely many rational parameters are triple-face exceptions. A fixed physical open cone has bounded parameter multiplicity. Hence

\[
\boxed{N_{R504,3P}(B)=\Theta(B^{1/10}).}
\]

This is a genuine infinite Stage19 family but is weaker than the audited quarter-power families. Fixed higher multiples increase section degree and do not provide a lighter fixed-section route.

The original-base section route is therefore submitted for closure **as a global-upgrade route**, not as a claim that every base change is impossible.

```text
R504_STATUS=ORIGINAL_SURFACE_SECTION_ROUTE_CLOSED_NO_GLOBAL_UPGRADE_SUBMITTED_FOR_FRESH_AUDIT
R504_GENERIC_QK_RANK=1
R504_SECOND_INDEPENDENT_QK_SECTION_EXISTS=false
R504_GENERIC_NONTORSION_SECTION_PROVED=true
R504_3P_EXACT_FAMILY_GROWTH=Theta(B^(1/10))
R504_3P_PRIMITIVE_GCD_BOUND=128
R504_3P_THIRD_FACE_EXCEPTION_GENUS=15
R504_CURRENT_SECTION_BEATS_QUARTER=false
R504_FIXED_HIGHER_MULTIPLE_EXPONENT_UPGRADE=false
R504_LOW_DEGREE_BASE_CHANGE_ROUTE=OPEN_GATE
R504_MULTI_SECTION_ROUTE=OPEN_GATE
R504_GROWING_MULTIPLE_UNIFORM_AGGREGATION=OPEN_GATE
R504_FRESH_AUDIT_REQUIRED=true
```

See `r504-section-lattice.md`, `r504-discovery-ledger.md`, and `r504-iteration-controller.json`.

## R505 — common squarefree core

The exact Stage19 squareclass receiver remains structurally correct, but no independent parameter dimension with polynomial physical-height bound and bounded multiplicity has yet been closed.

```text
R505_STATUS=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R505_RESEARCH_CONTINUES_AFTER_R504_AUDIT=true
```

## R506 — common-leg plus space

The common-leg divisor construction remains compatible. Successful low-dimensional specializations overlap known C17/R501-type mechanisms; no independent bulk count improving the global exponent has yet been certified.

```text
R506_STATUS=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R506_RESEARCH_CONTINUES_AFTER_R504_AUDIT=true
```

## Current boundary

```text
HIGHER_THAN_ONE_QUARTER_LOWER_PROVED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
R503_FRESH_AUDIT_REQUIRED=false
R504_FRESH_AUDIT_REQUIRED=true
LIVE_REPO_NATIVE_HIGH_VALUE_ROUTES_AFTER_R504=R505,R506
CHECKPOINT60_SINGLE_SHOT=false
AUDIT_PASS_DOES_NOT_CLOSE_LIVE_ROUTES=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```
