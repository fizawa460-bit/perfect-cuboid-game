# Stage25-10 fresh re-audit

Status: **PASS**

## Re-audit scope

This audit re-checks the narrow repair after the previous checkpoint10 FAIL. The earlier audit already accepted the mathematics and transition contract; the repair scope was limited to mandatory Stage21-28 repository-reuse/discovery evidence and controller taxonomy.

## Mathematics retained and accepted

- Source `M1(B)` is the primitive/canonical exactly-one-face population with no space requirement under `R<=B`.
- Target `N2(B)` is the primitive/canonical exactly-two-face population with integral `R=d` under the same cutoff.
- The endpoint masks are disjoint, so `N2/M1` is a matched population-size ratio, not literal objectwise survival.
- The audited source interface is
  `M1(B)~3/(4*pi^2) B^2 log B`.
- The current target interface is
  `N2(B)>>sqrt(log B)` and `N2(B)<<_epsilon B^(1/2+epsilon)`.
- The identities
  `N2/M1=(M2/M1)(N2/M2)=(N1/M1)(N2/N1)`
  are exact count-ratio identities when the intermediate counts are nonzero; no probabilistic independence is inferred.
- The double-charge firewall remains correct.

No theorem, count, endpoint definition, or finite census was changed by the repair.

## Previous FAIL items repaired

### 1. Repository-reuse handoff

The checkpoint now materializes the normative handoff:

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10_CONTRACT_FREEZE
```

The stronger prior results are correctly identified as the audited Stage21 exact `M1` source asymptotic and the Stage24-50 supersession `N2(B)>>sqrt(log B)`.

### 2. Concrete Stage21-28 discovery evidence

The repaired discovery ledger now records all required fields:

```text
DISCOVERY_CHECKPOINT=Stage25-10
SEARCHED_PATHS=...
SEARCH_TERMS=...
STRUCTURAL_SIGNATURES=...
DEPENDENCY_NEIGHBORS=...
CANDIDATES_FOUND=...
CANDIDATES_ACCEPTED=...
CANDIDATES_REJECTED_WITH_REASON=...
POPULATION_ADAPTERS_PROVED=...
DISCOVERY_LEDGER_STATUS=COMPLETE
```

The ledger explicitly checks Stage21/22/23/24 current interfaces, the Stage19 post-Stage24 lower supersession, Stage14 NUM reuse, the Stage14/15 824-record attack map, and the curated deep-review queue. Accepted and rejected `S1415-ATTACK-*` IDs are recorded with scope reasons.

The apparent reuse of `S1415-ATTACK-0817` in both Q10 and Q11 is not a ledger contradiction: the curated deep-review queue itself places `0817` at the end of Q10 and at the start of Q11. The Stage25 ledger's classification is therefore consistent with the canonical queue.

### 3. Population adapters

The repaired ledger explicitly records the exact/matched semantics for the four comparison edges and the finite NUM adapters. In particular, `NUM-R01` is an exact finite target adapter after the exactly-two mask, while `NUM-R06/R07` remain diagnostic-only and are not promoted to a direct Stage25 denominator oracle.

### 4. Controller taxonomy

`parent_class` is normalized to the established Stage16-28 taxonomy:

```text
parent_class=transition
```

No new controller enum is introduced.

### 5. Deterministic verifier

`contract_audit.py` now checks the mandatory reuse/discovery markers and taxonomy. The repaired submission CI run `31854877640` completed successfully. During this re-audit the verifier was additionally made audit-state aware so it can validate both the pre-audit repair state and the post-audit certified state without weakening any mathematical or discovery checks.

## Discovery audit verdict

The mandatory discovery evidence is now complete enough for checkpoint10. No stronger compatible whole-population Stage25 endpoint theorem was found beyond the already-audited interfaces used here. The rejected Q02/Q05/Q06/Q07-Q11 candidates are scoped conservatively and are not used to manufacture an extra saving.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
MATHEMATICS_CONTRACT_ACCEPTED=true
PATH_IDENTITIES_ACCEPTED=true
DOUBLE_CHARGE_FIREWALL_ACCEPTED=true
UPSTREAM_INTERFACE_CHECK=PASS
EXPLORATION_EVIDENCE_COMPLETE=true
REPO_REUSE_HANDOFF_COMPLETE=true
DISCOVERY_EVIDENCE_BLOCK_COMPLETE=true
PARENT_CLASS_NORMALIZED=true
COUNTS_RECOMPUTE_REQUIRED=false
MATHEMATICS_REOPEN_REQUIRED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=20
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
REPAIR_STATUS=COMPLETE_AUDITED_PASS
NEXT_EXPECTED_COMMAND=merge PR #980; then Stage25-main-batch
```
