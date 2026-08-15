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
- makes a strongest-certified / bounded-search route-boundary claim;
- introduces a new external theorem species as load-bearing input.

A negative exploratory submission may be audited and merged if it materially certifies a route boundary, but it does not close unrelated live routes.

## Stop rule for checkpoint60

`CHECKPOINT60_DEEP_STOP_RULE=SATISFIED` only when all of the following hold:

- each assigned high-value route R502-R506 and any later allocated route is `CLOSED_PROVED`, `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`, or `EXTERNAL_THEOREM_GATE`;
- no repo-native attack compatible with the Stage14/15 deep-review reopen conditions remains live;
- any theorem-class-changing result has received fresh audit;
- current global envelope and interaction classification are synchronized across Stage23/24/25 backflow artifacts;
- remaining open items require genuinely new external mathematics or genuinely new parametric input, not another unexecuted repo-native mutation of an existing normal form.

Only then may checkpoint60 set `NEXT_CHECKPOINT=70`.

## Audited history through R504

The audited route state entering this iteration is

```text
R501=PROVED_AUDITED_Theta_B_QUARTER
R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R504=ORIGINAL_SURFACE_SECTION_ROUTE_CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R507=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
```

Historical checkpoint60 verifier compatibility marker:

```text
HISTORICAL_R502_SUBMISSION_MARKER=R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
```

R504's original `Q(k)` section lattice has rank one and its 3P family has exact growth `Theta(B^(1/10))`, so fixed-section repetition on that base is not a hidden improvement to the global quarter-power lower.

## Current R504 residual / R505 / R506 submission

### R504 residual

Low-degree finite base change and multisection mechanisms remain mathematically possible, but the bounded repository/primary-source search did not find a ready exact-Stage19 physical-height counting adapter. Repeating fixed sections on the original base is already exhausted by the audited rank-one classification.

Candidate:

```text
R504_RESIDUAL=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
R504_NEW_EXPLICIT_BASE_CHANGE_REOPENS_ROUTE=true
```

### R505

The common-core equations

\[
A=kP^2,\qquad B=kQ^2
\]

are exactly equivalent to the Stage19 integral-space condition `sf(A)=sf(B)` in the toric two-face population. Thus R505 is the exact target receiver, not a construction by itself.

The Stage15 deep attack chain was reused through moving genus-one reduction, exact product-height, 2-covering/descent, fixed-diagonal subpolynomial fibers, codimension-two root-line/sieve analysis, blind rediscovery, channel-gcd first-moment reduction, and the repaired physical complementary-divisor switch. The surviving whole-family issue requires new physical-height uniformity/average input or a genuinely new explicit parametric family rather than another algebraic relabeling of the same receiver.

Candidate:

```text
R505=EXTERNAL_THEOREM_GATE_SUBMITTED_FOR_FRESH_AUDIT
R505_REOPEN_CONDITION=NEW_UNIFORM_PHYSICAL_HEIGHT_THEOREM_OR_NEW_EXPLICIT_PARAMETRIC_FAMILY
```

### R506

With

\[
u=mr,\ v=ns,\ w=ms,\ z=nr,
\]

we have `uv=wz` and

\[
A=u^2+v^2,\qquad B=w^2+z^2.
\]

The rank-one relation conversely reconstructs the two toric projective ratios. Therefore the common-leg + space lane is the R505 exact receiver in alternative coordinates and supplies no independent parameter dimension.

Candidate:

```text
R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
R506_SUBSUMED_BY_R505_EXACT_TORIC_RECEIVER=true
```

## Deep-stop proposal — audit required

If hostile audit accepts the three classifications above, the assigned route registry becomes:

```text
R501=PROVED_AUDITED
R502=CLOSED_AUDITED
R503=EXTERNAL_THEOREM_GATE_AUDITED
R504=ORIGINAL_BASE_CLOSED_PLUS_RESIDUAL_EXTERNAL_GATE
R505=EXTERNAL_THEOREM_GATE
R506=CLOSED_NO_INDEPENDENT_ROUTE_WITH_CERTIFICATE
R507=PROVED_AUDITED
```

At that point the bounded Stage25 rediscovery plus the reused Stage14/15 deep-review evidence exposes no remaining **unexecuted repo-native mutation of the existing normal forms**. New mathematics can still reopen a route.

Therefore this PR may submit the stop condition for audit but must not self-activate it:

```text
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
DEEP_STOP_PENDING_HOSTILE_AUDIT=true
CHECKPOINT60_CLOSED=false
STAGE70_ALLOWED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
```

If the audit rejects any route boundary, checkpoint60 remains at 60 and that route is restored to LIVE. If the audit accepts all boundaries and the backflow/envelope synchronization remains intact, the audit layer may set `CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=true` and permit checkpoint70.
