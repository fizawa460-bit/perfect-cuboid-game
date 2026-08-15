# Stage25-10 fresh audit

Status: **FAIL — bounded workflow/evidence repair required**

## Accepted mathematics and transition contract

The Stage25 endpoint contract is mathematically sound.

- Source `M1(B)` is the primitive/canonical exactly-one-face population with no space requirement under `R<=B`.
- Target `N2(B)` is the primitive/canonical exactly-two-face population with integral `R=d` under the same cutoff.
- Because the face masks are disjoint, `N2/M1` is correctly treated as a matched population-size ratio rather than literal objectwise survival.
- The frozen source interface `M1(B)~3/(4*pi^2) B^2 log B` matches the audited Stage21/Stage22 source population.
- The current target interface `N2(B)>>sqrt(log B)` and `N2(B)<<_epsilon B^(1/2+epsilon)` correctly consumes the audited Stage24 lower supersession while retaining the Stage19 upper.
- Both path identities
  `N2/M1=(M2/M1)(N2/M2)=(N1/M1)(N2/N1)`
  are exact count-ratio identities whenever the intermediate counts are nonzero. They do not require or imply probabilistic independence.
- The double-charge firewall is correctly stated.

The deterministic contract CI on the submitted head also passed.

## Blocking defect — mandatory repository-reuse / discovery evidence is incomplete

`docs/stage16-28-reuse-preflight.md` is normative for every Stage16-28 checkpoint. Its required handoff includes

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=<IDs/paths/PRs or NONE>
REUSE_MATCH_STATUS=EXACT|ADAPTER_PROVED|MIXED|NO_MATCH
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true|false
NEW_RESEARCH_JUSTIFIED=<reason or NOT_REQUIRED>
```

For Stage21-28 it additionally requires checkpoint-specific concrete evidence

```text
DISCOVERY_CHECKPOINT=
SEARCHED_PATHS=
SEARCH_TERMS=
STRUCTURAL_SIGNATURES=
DEPENDENCY_NEIGHBORS=
CANDIDATES_FOUND=
CANDIDATES_ACCEPTED=
CANDIDATES_REJECTED_WITH_REASON=
POPULATION_ADAPTERS_PROVED=
DISCOVERY_LEDGER_STATUS=COMPLETE|INCOMPLETE
```

The submitted `25-10/discovery-ledger.md` records direct terms, notation synonyms, structural signatures, dependency neighbors, and several accepted conclusions, but it does **not** materialize the required repository-reuse handoff or the required concrete candidate/search-path classification block. Under the Stage21-28 exploration enforcement gate, this is a workflow blocker even though the mathematical theorem/interface is otherwise correct.

Therefore checkpoint10 cannot advance yet.

## Secondary controller normalization

The Stage16-28 roadmap places Stage25 under **Transition / thinning stages**, while neighboring Stage22 and Stage24 transition controllers use `parent_class="transition"`. The submitted controller introduces `parent_class="combined_transition"`. This does not invalidate the mathematics, but it should be normalized to the established transition taxonomy during the same repair unless a repository schema explicitly adds that new enum.

## Required bounded repair

No theorem recomputation and no new large census are required.

1. Add the normative `REPO_REUSE_PREFLIGHT` handoff to the checkpoint10 result/controller/ledger as appropriate.
2. Add the concrete Stage21-28 discovery-evidence fields, naming searched repository surfaces, accepted candidates, rejected candidates with reasons (or `NONE` where genuinely none), and population adapters.
3. Ensure the evidence names the actual Stage21/22/23/24 interfaces and the Stage14 numerical reuse assets already used.
4. Normalize `parent_class` to `transition` unless an explicit controller-schema extension is supplied.
5. Extend `contract_audit.py` so it fails when these mandatory checkpoint10 evidence markers are missing.

```text
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=FAIL
MATHEMATICS_CONTRACT_ACCEPTED=true
PATH_IDENTITIES_ACCEPTED=true
DOUBLE_CHARGE_FIREWALL_ACCEPTED=true
UPSTREAM_INTERFACE_CHECK=PASS
EXPLORATION_EVIDENCE_COMPLETE=false
REPO_REUSE_HANDOFF_COMPLETE=false
DISCOVERY_EVIDENCE_BLOCK_COMPLETE=false
PARENT_CLASS_NORMALIZATION_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=10
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
COUNTS_RECOMPUTE_REQUIRED=false
MATHEMATICS_REOPEN_REQUIRED=false
REPAIR_SCOPE=REUSE_DISCOVERY_EVIDENCE_AND_CONTROLLER_TAXONOMY_ONLY
NEXT_EXPECTED_COMMAND=Stage25-main-batch
```