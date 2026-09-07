#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

BASE = 'e758e05953df2cf8cd4ab26ac1e9d72374e99760'
CONTRACT_BLOB = '6fc62623ee59b4aaf1fc053ad42df2dcbba0855b'
VERIFIER_BLOB = 'ee066a55f95184916c02dc1f1bbd9f07d1840dc8'
FREEZE_BLOB = 'd3f90093c0a6655da9874c9141b15ab4682c4409'

idx_path = Path('docs/arsenal/index.json')
contract_path = Path('docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json')
verifier_path = Path('docs/arsenal/verify_lit_wf02_global_h1_localization_reciprocity.py')
promo_path = Path('docs/stage36-literature-strengthening-promotion.md')

contract_blob = subprocess.check_output(['git', 'hash-object', str(contract_path)], text=True).strip()
verifier_blob = subprocess.check_output(['git', 'hash-object', str(verifier_path)], text=True).strip()
assert contract_blob == CONTRACT_BLOB, (contract_blob, CONTRACT_BLOB)
assert verifier_blob == VERIFIER_BLOB, (verifier_blob, VERIFIER_BLOB)

idx = json.loads(idx_path.read_text())
s = idx['stage36_literature_strengthening']
wf = s['workflow_metadata']['LIT-WF02']
wf['support_artifact_blob_sha'] = contract_blob
wf['verifier_blob_sha'] = verifier_blob
wf['repo_adapter_contract'] = (
    'STAGE36_SOURCE_RESULT -> IMMUTABLY_BOUND_GLOBAL_CLASS_CONSTRUCTION + '
    'REQUIRED_PLACE_INVENTORY + EACH_LOCALIZATION + SERRE/MILNE_HYPOTHESIS_EVIDENCE -> '
    'EXECUTE_EACH_BOUND_MATHEMATICAL_VERIFIER_AT_EXACT_GIT_BLOB -> TYPED_GLOBAL_LOCAL_PACKAGE; '
    'any missing/mismatched/unexecuted obligation fails closed'
)
wf['adapter_source_verifier'] = (
    'no Stage36 adapter PASS evidence is registered; a future PASS package must bind and execute '
    'method-specific global-class/localization/adapter verifiers with immutable evidence'
)
wf['output'] = (
    'PASS only after exact Git-object resolution plus executable immutable mathematical evidence chain; '
    'otherwise first FAIL_CLOSED obligation'
)
wf['adapter_status'] = 'FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE'
wf['package_schema'] = 'LIT-WF02-GLOBAL-H1-LOCALIZATION-PACKAGE-V2'
wf['immutable_pass_evidence_schema'] = 'LIT-WF02-IMMUTABLE-MATHEMATICAL-PASS-EVIDENCE-V1'
wf['self_check_is_applicability_pass'] = False
wf['boolean_flags_are_proof_evidence'] = False
idx_path.write_text(json.dumps(idx, indent=2, ensure_ascii=False) + '\n')

promo = promo_path.read_text()
start = promo.index('## LIT-WF02 GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW')
end = promo.index('## Rejected duplicates and research gap', start)
section = f'''## LIT-WF02 GLOBAL_H1_LOCALIZATION_RECIPROCITY_APPLICABILITY_WORKFLOW

**Maturity recommendation:** PROVISIONAL. **Kind:** workflow, not a theorem or selector.

Reusable workflow contract:

```text
repo local rows/charts
-> bind one fixed global H1/Kummer module/class to immutable construction evidence
-> execute the bound construction verifier at its exact Git blob/head
-> bind every retained local row/chart to immutable localization evidence
-> execute every bound localization verifier at its exact Git blob/head
-> independently verify the complete required-place inventory and exact place-set equality
-> certify field, finite-support-if-used, dyadic and real normalization
-> bind Serre/Milne exactly to the Phase3 freeze and execute theorem-hypothesis verifiers
-> execute the separately bound global adapter mathematical verifier
-> emit PASS only if every obligation succeeds; otherwise FAIL_CLOSED at the first gap
```

`path`, a syntactically valid 40-character SHA, `required_places_complete=true`, `dyadic_handled=true`, `real_places_handled=true`, or a theorem `hypotheses_checked=true` flag is **never proof evidence by itself**. Every claimed `path/blob_sha/exact_head` is resolved against Git; every proof-bearing verifier is materialized from its claimed immutable blob and executed against immutable JSON evidence. The verifier/evidence pair must emit the frozen `LIT-WF02-IMMUTABLE-MATHEMATICAL-PASS-EVIDENCE-V1` JSON PASS record with matching subject/path/blob/head fields.

The Phase3 literature binding is also executable/fail-closed: discovery head `f1a2d3074e802b0fd4555cb827e165c3de2bdfc9`, `docs/arsenal/literature-stage36-hostile-freeze.json`, blob `{FREEZE_BLOB}` is read from Git and the workflow candidate plus Serre/Milne theorem locators must match it exactly. Literature anchors remain Serre, *A Course in Arithmetic*, Chapter III Theorems 2-4, DOI `10.1007/978-1-4684-9884-4`; Milne, *Arithmetic Duality Theorems*, Theorem I.4.10, https://www.jmilne.org/math/Books/ADTnot.pdf.

Current Stage36 applicability is **`FAIL_CLOSED_MISSING_GLOBAL_CLASS_AND_LOCALIZATION_ADAPTER_EVIDENCE`**. Phase3 already records the missing `POINTWISE_CHART_TUPLE_TO_GLOBAL_KUMMER_OR_TORSOR_CLASS` and `DYNAMIC_RESERVOIR_ROWS_TO_GLOBAL_KUMMER_LOCALIZATION_SYSTEM`; #1692 does not manufacture either and registers no Stage36 LIT-WF02 PASS package. `--self-check` emits only `SELF_CHECK_OK` after contract/freeze/provenance and adversarial fake-SHA checks; it is explicitly **not** applicability PASS.

HYPOTHESES: named global finite module/class with immutable construction evidence; exact source binding; independently verified required-place inventory; immutable evidence and executable verifier for every localization; finite-support proof when used; explicit field-change semantics; exact Phase3 Serre/Milne binding plus executable theorem-hypothesis evidence; separately proved adapter verifier/evidence. APPLICABILITY: any repo branch attempting to upgrade local character/Kummer data to reciprocity, Selmer or global-duality input. DO_NOT_USE_FOR: constructing the missing global class; accepting metadata/boolean declarations as proof; treating Hilbert reciprocity as a contradiction; converting local admissibility into a rational point; granting theorem/receiver/local-global/endpoint credit.

Workflow support artifact: `docs/arsenal/lit-wf02-global-h1-localization-reciprocity-contract.json`, blob `{contract_blob}`. Fail-closed applicability verifier: `docs/arsenal/verify_lit_wf02_global_h1_localization_reciprocity.py`, blob `{verifier_blob}`. Mathematical credit remains zero.

'''
promo_path.write_text(promo[:start] + section + promo[end:])
print('PASS: LIT-WF02 fail-close documentation and registry metadata materialized')
print('CONTRACT_BLOB=' + contract_blob)
print('VERIFIER_BLOB=' + verifier_blob)
