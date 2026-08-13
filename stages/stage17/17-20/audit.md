# Stage17-20 audit

Status: **PASS**

Audited submission: PR #903, head `5f3b39dd372f8c67b3d80de1b3d345d65bbc49f5`.

## Verdict

The Stage17-20 finite-data baseline is accepted under the frozen Stage17-10 population contract.

The census remains on primitive canonical triples `0<a<b<c` with `gcd(a,b,c)=1`, exactly one integral face diagonal, common cutoff `R<=B`, and integral `R` (equivalently positive integral space diagonal `d=R`). The Stage16-to-Stage17 subset/cutoff interface is unchanged.

The deterministic enumerator and frozen CSV remain `COMPUTED` evidence only. The optimized Pythagorean-face coverage path was independently cross-checked against direct canonical-triple enumeration through `B=200`; the frozen counts, face splits, and CSV hash were accepted by the fresh audit. No asymptotic order, limiting survivor ratio, decay exponent, upper/lower bound, independence statement, or causal conclusion is promoted at checkpoint 20.

Dedicated GitHub Actions validation also passed:

- workflow: `Stage17-20 finite-data`
- run: `31744471773`
- job: `94595539391`
- conclusion: `success`

Checkpoint 30 may therefore proceed after the audited checkpoint-20 PR is merged.

```text
AUDIT_VERDICT=PASS
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=30
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
```
