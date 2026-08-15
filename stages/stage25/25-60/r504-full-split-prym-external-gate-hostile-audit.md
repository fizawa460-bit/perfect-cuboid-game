# Stage25-60 R504 exceptional Prym external-gate hostile audit

Status: **PASS; EXTERNAL THEOREM GATE CLASSIFICATION ACCEPTED; CHECKPOINT60 CONTINUES**

ROUTE=R504
CHECKPOINT=60
PR=998

## Verdict

The submission is accepted as a boundary/gate classification, not as a theorem that the exceptional Prym/E0 locus is empty or finite.

The previous audited result `Hom_K(P_eta,E0_K)=0` removes a generic K-defined E0 factor. For each fixed bounded homomorphism/isogeny complexity, the corresponding factor condition is therefore a proper algebraic locus. The remaining rational exceptional set is an unbounded union over such complexities. No repository-native argument currently supplies a global isogeny-degree bound or uniform rational-point theorem for that union.

The effective two-dimensional moduli reduction is accepted at the level needed for gate classification: projective matrix parameters have dimension three and source scaling removes one generic dimension. This does not by itself prove an unlikely-intersection theorem.

The finite-field census at p=7 and p=11 is accepted only as exact hostile evidence. The dedicated workflow passes on head `861a00ab1af75de6d685ce366eedadc0f45150ed`, reproducing 336/36 and 1320/80 and verifying all tested E0-factor hits lie on the reciprocal divisor. It is explicitly not used as characteristic-zero proof.

## Scope firewall

Accepted:
- the remaining full-split rational Prym/E0 problem is an external-theorem/global-degree-bound gate;
- finite bounded-degree searches cannot close the unbounded union;
- the known rank-two and generic-Prym results remain closed/audited.

Not accepted or claimed:
- `Hom_Kbar(P_eta,E0)=0`;
- emptiness or finiteness of exceptional rational specializations;
- a uniform isogeny-degree bound;
- that currently cited curve-level unlikely-intersection theorems automatically settle this two-dimensional image;
- any improvement of the Stage25 lower bound.

Checkpoint60 therefore remains open for the prescribed deep-stop/backflow synchronization. Stage70 is not yet allowed by this audit alone.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_FULL_SPLIT_PRYM_ROUTE=EXTERNAL_THEOREM_GATE_AUDITED_PASS
R504_FULL_SPLIT_EXCEPTIONAL_PRYM_E0_ISOGENY_LOCUS=OPEN_EXTERNAL
R504_FULL_SPLIT_EXCEPTIONAL_ISOGENY_DEGREE_BOUND=UNKNOWN
R504_PRYM_EXCEPTIONAL_FINITE_FIELD_SIEVE_IS_PROOF=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #998; then Stage25-main-batch at checkpoint60
```
