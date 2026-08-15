# Stage25-60 deep-stop synchronization — discovery/reuse ledger

```text
DISCOVERY_CHECKPOINT=Stage25-60-DEEP-STOP-SYNC
DEEP_RESEARCH_MODE=true
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS,STAGE14_15_ATTACK_LEDGER,PRIMARY_LITERATURE
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=false
NEW_RESEARCH_JUSTIFIED=NO_NEW_ROUTE;SYNCHRONIZE_AUDITED_ROUTE_BOUNDARIES_AND_BACKFLOW_AFTER_PR998
POPULATION_ADAPTERS_PROVED=REUSED_FROM_AUDITED_R501_R502_R504_R505_R506_ARTIFACTS
DISCOVERY_LEDGER_STATUS=COMPLETE_SUBMITTED_FOR_FRESH_AUDIT
```

## Sources actually reused

- Stage25 checkpoint50 positive-power family and backflow artifacts.
- `stages/stage25/25-60/audit-recheck.md` — R502 audited closure.
- `stages/stage25/25-60/r503-audit.md` — R503 external/base-change theorem gate.
- PR #990 and `r505-r506-audit-recheck2.md` — R505 exact receiver, R506 subsumption, completed reuse handoff, R504 growing-rank-one closure.
- PRs #992–#998 and their Stage25-60 artifacts — complete R504 degree-two descent, nonsplit rank jump, physical second section, rank-two coset/height/growing aggregation, generic Prym obstruction, exceptional Prym external gate.
- `stages/stage23/post-stage25-r01/result.md` and `stages/stage24/post-stage25-r01/result.md` — current backflow.
- `stages/stage25/25-60/continuation-policy.md` — normative stop rule.
- `stages/stage25/25-reentry-controller.json` — checkpoint70 audited-closeout gate before reentry.

## Candidate states considered

```text
CANDIDATES_FOUND=continue_R504_repo_native;reopen_R505;reopen_R506;backflow_delta;deep_stop_candidate
CANDIDATES_ACCEPTED=deep_stop_candidate;backflow_no_delta
CANDIDATES_REJECTED_WITH_REASON=continue_R504_repo_native rejected because PR998 hostile audit accepts remaining full-split Prym residual as EXTERNAL_THEOREM_GATE;reopen_R505 rejected because hostile audit accepted exact receiver/deep reuse and no mathematics reopen required;reopen_R506 rejected because exact toric subsumption accepted;backflow_delta rejected because all post-checkpoint50 deep routes record GLOBAL_STAGE25_LOWER_CHANGED=false
```

No finite census, finite-field sieve, or absence search is promoted to a global theorem. In particular, the finite-field Prym sieve from PR #998 remains evidence only; the external-gate classification rests on the audited generic obstruction plus the unbounded-complexity structure of the remaining locus and the absence of an executable same-measure repository theorem.

## Matching contract

```text
REUSE_POPULATION_MATCH=MIXED_BUT_ADAPTERS_ALREADY_AUDITED
REUSE_CUTOFF_MATCH=EXACT_FOR_GLOBAL_STAGE25_BACKFLOW
REUSE_MULTIPLICITY_MATCH=ROUTE_SPECIFIC_ALREADY_AUDITED
REUSE_MEASURE_MATCH=EXACT_FOR_STAGE19_TARGET_AND_STAGE23_24_RATIOS
REUSE_QUANTIFIER_MATCH=MIXED_WITH_SCOPE_FIREWALL_RETAINED
```

## Boundary

This ledger supports only a fresh-audit decision on checkpoint60 deep-stop. It does not self-certify Stage70.

```text
CHECKPOINT60_DEEP_STOP_RULE_CANDIDATE=true
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_STATUS=PENDING
NEXT_EXPECTED_COMMAND=Stage25-audit
```
