# Stage16S-20 — fresh audit record

Status: **PASS**

Audited submission: PR #910, head `df7989bcfe8692a7d3d956e7a862b02bf3c816b3`.

## Scope checked

- The audited Stage16S-10 population contract remains unchanged: primitive canonical `0<a<b<c`, `gcd(a,b,c)=1`, common cutoff `R<=B`, with `SPACE_AT_LEAST` requiring integral `R=d` and `SPACE_ONLY` requiring exactly zero integral face diagonals.
- The optimized enumerator uses the exact identity `a^2+b^2=d^2-c^2` and then rechecks canonical order and global primitivity. Every Stage16S object has a unique canonical `(a,b,c)` and positive `d=R`, so this join is complete for the frozen population.
- An independent audit recomputation at `B=200` found 1320 Stage16S objects and matched the direct canonical-triple brute-force set exactly.
- Independent regeneration through `B=2000` reproduced every frozen row. At `B=2000`: `SPACE_AT_LEAST=136060`, `SPACE_ONLY=134621`, `face1=1434`, `face2=5`, `face3=0`.
- At every threshold, `SPACE_AT_LEAST = SPACE_ONLY + face1 + face2 + face3` exactly.
- The frozen CSV SHA-256 recomputes to `0752d021b9df40c8035b10d1e8ed3cfd58a84086e64dca0ce0256492df63af2c`.
- The `face1` column `7,25,67,174,453,764,1077,1434` agrees exactly with the audited Stage17-20 `N1` census at all shared thresholds.
- The finite ratio `SPACE_ONLY/SPACE_AT_LEAST` remains diagnostic only. No asymptotic order, limiting density, independence, or causal claim is promoted at checkpoint 20.
- No dedicated Actions workflow is required for this checkpoint contract. The embedded deterministic verifier and independent audit recomputation supply the replay evidence; absence of a newly-added workflow is therefore non-blocking.
- Stage16S remains an auxiliary parallel lane and does not alter the numbered Stage17/18 controller.

## Verdict

The checkpoint-20 finite-data baseline is computationally consistent with the frozen Stage16S population contract and with the independent Stage17 finite interface. Checkpoint 30 may proceed after this persisted PASS.

```text
AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=30
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
```
