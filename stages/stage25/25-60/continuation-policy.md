# Stage25 checkpoint60 continuation policy

STATUS=NORMATIVE_FOR_STAGE25_60_CONTINUATION

Checkpoint60 is iterative. A fresh audit PASS certifies the submitted checkpoint60 claims, but does **not** by itself close checkpoint60 while assigned high-value research routes remain live.

## Naming invariant — preserve the assigned route IDs

Research-route IDs are persistent identities, not audit-round numbers and not checkpoint-local counters.

The existing allocation is:

- `R501` — Meskhishvili first parametrization / audited positive-power family;
- `R502` — Meskhishvili third parametrization fallback;
- `R503` — Yoshida varying-fiber / uniform-height route;
- `R504` — symmetric-k aggregation / moving elliptic section route;
- `R505` — common squarefree-core route;
- `R506` — common-leg + space receiver;
- `R507` — primitive-height rigidity of R501.

These IDs MUST NOT be renamed merely because work continues at checkpoint60 or because another audit/PR is opened.

```text
ROUTE_ID_IS_PERSISTENT=true
AUDIT_ROUND_IS_NOT_ROUTE_ID=true
CHECKPOINT_NUMBER_DOES_NOT_RENUMBER_EXISTING_ROUTE=true
R501_R507_ALLOCATIONS_FROZEN=true
```

If a genuinely new mathematically distinct route is created after R507, allocate the next unused route ID (`R508`, then `R509`, ...). A refinement of an existing route keeps its existing ID.

## Operating rule

After each audited checkpoint60 submission:

1. merge the audited PR if allowed;
2. continue checkpoint60 when any assigned high-value route remains actionable;
3. preserve prior checkpoint60 audit records as historical provenance;
4. continue work under the original route ID;
5. do not overwrite or weaken an earlier audited theorem merely because a later route fails;
6. move to checkpoint70 only after the stop rule below is satisfied.

## Audit placement rule

Fresh audit is required whenever a checkpoint60 submission does one of the following:

- proves a stronger global lower or upper exponent;
- proves a new infinite family or moving-family theorem;
- changes an interaction sign/classification;
- closes a previously named OPEN_GATE or changes a route to an external/base-change theorem gate;
- makes a strongest-certified / no-known-route claim;
- introduces a new external theorem species as load-bearing input.

A negative exploratory submission may be audited and merged if it materially certifies a route boundary, but it does not close unrelated live routes.

## Stop rule for checkpoint60

`CHECKPOINT60_DEEP_STOP_RULE=SATISFIED` only when all of the following hold:

- each assigned high-value route R502-R506 and any later allocated route is `CLOSED_PROVED`, `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`, or `EXTERNAL_THEOREM_GATE`;
- no repo-native attack compatible with the Stage14/15 deep-review reopen conditions remains live;
- any theorem-class-changing result has received fresh audit;
- current global envelope and interaction classification are synchronized across Stage23/24/25 backflow artifacts;
- remaining open items require genuinely new external mathematics, not another unexecuted repo-native mutation.

Only then may checkpoint60 set `NEXT_CHECKPOINT=70`.

## Audited history through R504

PR #985, #986, and the R504 hostile audit are PASS for their submitted scopes.

```text
R501=PROVED_AUDITED_Theta_B_QUARTER
R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R504=ORIGINAL_SURFACE_SECTION_ROUTE_CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R507=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
```

Historical verifier compatibility marker:

```text
HISTORICAL_R502_SUBMISSION_MARKER=R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
```

R503 closes only the direct generic-section route; low-degree base changes and exceptional positive-rank fibers remain theorem gates.

R504 now has a hostile-audited source-level classification of the original `Q(k)` section lattice. The symmetric quartic receiver has Jacobian

\[
Y^2=X^3-4(k^4+1)^2X,
\]

and anti-invariant descent on the twist cover gives free `Q(k)` rank one. Thus there is no second independent section on the original base.

The first nondegenerate 3P section has degree-20 physical height after homogenization, exact primitive gcd at most `128`, finite genus-15 third-face exceptions, and bounded parameter multiplicity. Its exact family growth is

\[
N_{R504,3P}(B)=\Theta(B^{1/10}).
\]

This does not improve the audited global `B^(1/4)` lower.

The audit does not claim rank-one persistence after finite base change. Low-degree base-change, multisection, and growing-multiple aggregation remain open inside R504.

```text
R504_GENERIC_QK_RANK=1
R504_SECOND_INDEPENDENT_QK_SECTION_EXISTS=false
R504_3P_EXACT_FAMILY_GROWTH=Theta(B^(1/10))
R504_3P_PRIMITIVE_GCD_BOUND=128
R504_LOW_DEGREE_BASE_CHANGE_ROUTE=OPEN_GATE
R504_MULTI_SECTION_ROUTE=OPEN_GATE
R504_GROWING_MULTIPLE_UNIFORM_AGGREGATION=OPEN_GATE
R505=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
R506=LIVE_NO_CLOSED_DIMENSION_HEIGHT_COUNT
CHECKPOINT60_CLOSED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
NEXT_AFTER_R504_AUDIT_PASS=MERGE_AND_CONTINUE_CHECKPOINT60_WITH_R505_R506
```
