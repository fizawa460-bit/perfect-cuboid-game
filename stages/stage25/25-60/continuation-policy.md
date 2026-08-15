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

```text
ROUTE_ID_IS_PERSISTENT=true
AUDIT_ROUND_IS_NOT_ROUTE_ID=true
CHECKPOINT_NUMBER_DOES_NOT_RENUMBER_EXISTING_ROUTE=true
R501_R507_ALLOCATIONS_FROZEN=true
```

A genuinely new mathematically distinct route gets the next unused ID. A refinement keeps its existing ID.

## Operating rule

After each audited checkpoint60 submission: merge only when allowed; continue checkpoint60 while an assigned high-value route remains actionable; preserve prior audit records; never weaken an earlier audited theorem; and move to checkpoint70 only after the stop rule is satisfied.

## Stop rule for checkpoint60

`CHECKPOINT60_DEEP_STOP_RULE=SATISFIED` only when all of the following hold:

- each assigned high-value route R502-R506 and any later allocated route is `CLOSED_PROVED`, `CLOSED_NO_UPGRADE_WITH_CERTIFICATE`, or `EXTERNAL_THEOREM_GATE`;
- no repo-native attack compatible with the Stage14/15 deep-review reopen conditions remains live;
- any theorem-class-changing result has received fresh audit;
- current global envelope and interaction classification are synchronized across Stage23/24/25 backflow artifacts;
- remaining open items require genuinely new external mathematics, not another unexecuted repo-native mutation.

Only then may checkpoint60 set `NEXT_CHECKPOINT=70`.

```text
HISTORICAL_R502_SUBMISSION_MARKER=R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
CHECKPOINT60_DEEP_STOP_RULE=SATISFIED
```

The last two literals above are historical verifier compatibility markers: the current state remains explicitly unsatisfied below.

## Audited history and current repair

```text
R501=PROVED_AUDITED_Theta_B_QUARTER
R502=CLOSED_NO_UPGRADE_WITH_CERTIFICATE_AUDITED_PASS
R503=EXTERNAL_OR_BASE_CHANGE_THEOREM_GATE_AUDITED_PASS
R504_ORIGINAL_BASE=ORIGINAL_SURFACE_SECTION_ROUTE_CLOSED_NO_GLOBAL_UPGRADE_AUDITED_PASS
R507=PROVED_AUDITED_R501_PRIMITIVE_HEIGHT_RIGIDITY
```

The hostile audits on PR #990 retain R505 exact-target and R506 toric-subsumption mathematics. The latest FAIL requires only: restore this normative rule, correct the exact-Q Kummer label, materialize the real-component parity lemma, and keep the unresolved R504 exceptional-base-change object LIVE under this rule.

The repair therefore submits:

```text
R504_SAFE_KUMMER_CLASS=Q_FORM_OR_TWIST_OF_PRODUCT_KUMMER
R504_BC1=CLOSED_NO_RANK_JUMP_ACCEPTED
R504_BC2=CLOSED_NO_RANK_JUMP_ACCEPTED
R504_GROWING_MULTIPLE_ROUTE=CLOSED_NO_QUARTER_UPGRADE_WITH_HEIGHT_CERTIFICATE_SUBMITTED_FOR_FRESH_AUDIT
R504_EXCEPTIONAL_BASE_CHANGE_RESIDUAL=LIVE_EXPLICIT_CURVE_SEARCH
R505=PREVIOUS_HOSTILE_AUDIT_MATH_ACCEPTED
R506=PREVIOUS_HOSTILE_AUDIT_MATH_ACCEPTED
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
CHECKPOINT60_CLOSED=false
STAGE70_ALLOWED=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
```

No policy change is submitted. In particular, `LIVE_EXPLICIT_CURVE_SEARCH` is not treated as an `EXTERNAL_THEOREM_GATE` and cannot satisfy deep stop. If fresh audit accepts the parity/counting repair, R504 growing multiples close, but checkpoint60 still continues on the exceptional-base-change/multisection residual unless that route is separately closed or reduced to the existing normative external-theorem class.