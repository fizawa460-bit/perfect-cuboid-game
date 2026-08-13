# Stage16-10 fresh audit

Status: **PASS**

## Audited submission

- Parent stage: `Stage16`
- Checkpoint: `Stage16-10`
- Submitted result: `stages/stage16/16-10/result.md`
- Submitted/controller head audited: `63ae1802cd2c8b74ce4e0ab471f77be1a23177e4`
- Population class: primitive canonical cuboids with exactly one integral face diagonal and no space-diagonal integrality requirement

## Audit checks

### 1. Primitive/canonical normalization — PASS

The submitted population uses positive integer edges with the unique canonical representative `0<a<b<c`, `gcd(a,b,c)=1`. This removes scale copies and permutation copies before counting and matches the Stage16-28 common population contract. `AR-001` is therefore a direct reuse.

### 2. Exactly-one face multiplicity — PASS

The contract imposes exactly one of `a^2+b^2`, `a^2+c^2`, `b^2+c^2` being a square. Exactly-two and exactly-three face populations are excluded rather than counted with multiplicity. This matches the roadmap definition of Stage16.

### 3. Common cutoff and Stage17/21 adapter — PASS

The height is `R(a,b,c)=sqrt(a^2+b^2+c^2)` with cutoff `R<=B`, and no integrality condition is imposed on `R`. On the subpopulation with integral space diagonal `d`, positivity and `d^2=a^2+b^2+c^2=R^2` give the exact identity `d=R`, hence `R<=B iff d<=B`. The Stage16/17 and future Stage21 comparison interface is exact and introduces no cutoff drift.

### 4. Roadmap compatibility — PASS

Stage16 is the exactly-one-face population state without an integral-space-diagonal requirement. Checkpoint 10 is the population-contract checkpoint. The submission stops before finite-data checkpoint 20, which is the correct independent-audit boundary.

### 5. Notation / historical-population separation — PASS

The Stage16 ambient count is `M_1(B)=#B_1(B)`. Historical exactly-one families that additionally impose integral space diagonal use a narrower population. In particular `AR-039` constructs such an integral-space-diagonal exactly-one subfamily and yields a lower bound for the historical `N_1(B)` population. Stage16-10 correctly does not charge that lower bound at checkpoint 10.

### 6. Reuse and evidence ledger — PASS

- `AR-001`: direct reuse for primitive/canonical normalization and exact face-multiplicity separation.
- `AR-002`: direct pointwise Euclid certificate for the single integral face; it is not promoted into a count.
- `AR-039`: correctly parked for a later lower-bound checkpoint after population/cutoff compatibility is invoked.
- `EVIDENCE_LEVEL=PROVED` is explicitly limited to the exact normalization and `R=d` adapter. No asymptotic, ratio, upper-bound, lower-bound, or causal theorem is claimed at Stage16-10.

### 7. Merge safety / stale Stage15 verifier — PASS

The prior audit failure was repository-only: the frozen Stage15-8 verifier incorrectly required the mutable successor pointer `NEXT_RESEARCH_PROGRAM=UNDEFINED`.

Commit `63ae1802cd2c8b74ce4e0ab471f77be1a23177e4` removes only that stale successor-value freeze while retaining the Stage15 closure/R02 checks. GitHub Actions run `31700486740`, job `94448162590`, executed `python stages/stage15/replay/verify_stage15_8_html.py` and completed with conclusion `success`.

The Stage16 mathematical submission was not changed by that repair.

## Audit decision

Stage16-10 is certified. The controller may advance to the next unresolved checkpoint, Stage16-20, after the audited PR is merged.

```text
AUDIT_VERDICT=PASS
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=20
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
```
