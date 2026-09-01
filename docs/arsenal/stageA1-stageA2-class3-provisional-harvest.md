# StageA1 / StageA2 provisional Arsenal harvest — Class 3 theorem construction

Status: `PROVISIONAL_HISTORICAL_METHOD_HARVEST`

This file is an Arsenal discovery record, not a formal selector and not a promotion of the StageA2 family theorem to other receivers.

## Authority and classification basis

Stage29 separates current-tool-limit computational walls from theorem walls. The authoritative Stage29-16 ledger records Class 2 kernels as concrete computational/adapter/certificate walls and Class 3 kernels as `NEW_THEOREM_REQUIRED` theorem-shaped residuals. In particular:

- `K16-C3-MOVING-FIBER-ARITHMETIC` requires a uniform arithmetic/specialization theorem or a globally exhaustive finite reduction with exact lift reconstruction;
- `K16-C3-EXT-C-PRIMITIVE-DIVISOR` / `R29-EXT-CHANG-C` requires a new all-multiples theorem, though a replacement theorem proving the same receiver closure is allowed.

Stage29-13 separately source-locks the transferable StageA2 method species as

```text
exact low-dimensional family/receiver
 -> exact algebraic reduction or squareclass split
 -> explicit cover(s)
 -> genus-one/Jacobian or other complete arithmetic closure
 -> reconstruction/boundary audit.
```

The StageA2 published `-18` family exclusion itself is not transferable.

Authoritative sources:

- `stages/stage29/29-16/active-kernel-ledger.json`, blob `5d6d4c7709b57064aea5dc0ece672c5170c39550`
- `stages/stage29/29-16/result.md`, blob `4abf29d9aa57a9e89c0e768edb6a2ee6c85fb14c`
- `stages/stage29/29-13/result.md`, blob `49a289c6acb2b46733e20338cb77778d763d88df`

Harvest snapshot main commit: `5e2d9ab1035851b40268e6cd9877d27cd1003452`.

---

## A2-C3P01 — RECEIVER_SPECIFIC_CLOSURE_THEOREM_PIPELINE

- **PRIMARY CLASSIFICATION:** `CLASS3_THEOREM_CONSTRUCTION_PRECEDENT`
- **SECONDARY:** `WORKFLOW_CANDIDATE`
- **CONCISE NAME:** receiver-specific closure theorem pipeline
- **REUSABLE PATTERN:** when no existing theorem/Arsenal card directly closes an exact receiver, construct a new receiver-specific theorem by the chain

```text
source-lock exact receiver
 -> exact factorization / algebraic compression
 -> gcd / resultant / valuation / parity analysis
 -> finite squareclass reduction
 -> finite explicit covers
 -> low-genus models
 -> exact Jacobian / Mordell-Weil control
 -> complete auxiliary rational-point classification
 -> reconstruct every finite point, pole, infinity and degenerate landmark
 -> prove complete closure only for the represented source family.
```

- **WHY THIS IS A CLASS-3 PRECEDENT:** StageA2 did not merely apply one pre-existing theorem to an already matching object. It designed a new target-specific closure statement and assembled several standard arithmetic techniques into a complete proof of that statement. This matches the later Stage29 Class-3 notion of a theorem-shaped residual, especially where a replacement theorem can close the exact receiver even if the originally named theorem species is different.
- **HYPOTHESES:** exact source object and quantifiers; complete forward/reverse algebraic reduction; finite squareclass/cover completeness; proof-capable Jacobian/MW or equivalent rational-point completeness; explicit exceptional-locus and source-family reconstruction.
- **APPLICABILITY:** low-dimensional Diophantine receivers for which algebraic factor structure can turn an infinite family into finitely many explicit covers whose rational points can be completed.
- **LIMITATIONS:** not every Class-3 receiver admits finite-cover reduction; does not replace a missing uniform theorem on genuinely higher-dimensional or uncontrolled moving families.
- **KNOWN SUCCESSFUL USE:** StageA2 published-minus18 family closure; Stage29-13 Saunderson family method transfer; Stage34-02 `R29-EXT-CHANG-C` replacement-route design.
- **POSSIBLE TARGETS:** `K16-C3-MOVING-FIBER-ARITHMETIC` when a globally exhaustive finite-cover reduction exists; `K16-C3-EXT-C-PRIMITIVE-DIVISOR` via a replacement theorem closing the same all-multiples receiver. No exact current Stage32/33 target is claimed.
- **DO_NOT_USE_FOR:** do not infer that every Class-3 problem reduces to genus one; do not transfer StageA2 numerical coefficients, rank-zero conclusion, family exclusion, or perfect-cuboid endpoint credit.
- **EXISTING ARSENAL RELATION:** uses formal components `S31-W01`, `S31-W03`, `S31-WF01`, `S30-WF02`, `S30-WF03`; distinct value is the theorem-construction orchestration layer.
- **DECISION:** `NEW_PRECEDENT_RECORD`; not a formal selector.

### StageA2 proof sources

- `stages/stageA2/A2-3/audit.md`, blob `dee7cf046d1cbca01aaf3d220d9e27211d6757c7`, audit PASS
- `stages/stageA2/A2-4/result.md`, blob `8d2c347d5f67f6d3a9a6aaa4ddf8055714b55b8a`
- `stages/stageA2/A2-4/audit.md`, blob `bf1b4ec1248caa1706c28523d199a60618564c3b`, audit `PASS_WITH_ELEMENTARY_STRENGTHENING_AND_LANDMARK_REPAIR`
- `stages/stageA2/A2-5/result.md`, blob `c1b47381d0238ebd2941522c55097b6f51ada00d`
- `stages/stageA2/A2-5/verify.py`, blob `65b69fbb49579b6e42c92e5b67190f4831181c67`
- `stages/stageA2/A2-5/audit.md`, blob `da6d832f8405dcfd5845637d1e1efc506d1b1404`, audit `PASS_WITH_CONTROLLER_HISTORY_REPAIR`

---

## A2-W01 — SUCCESSIVE_EXACT_FACTOR_SQUARECLASS_DESCENT

- **PRIMARY CLASSIFICATION:** `ARSENAL_CANDIDATE`
- **SECONDARY:** `CLASS3_THEOREM_CONSTRUCTION_PRECEDENT`
- **STATEMENT / PATTERN:** factor a reconstruction square condition into primitive low-degree binary forms; bound pairwise gcds using exact identities/resultants; force all unsupported odd valuations even; control 2-adic valuations/signs/parity; enumerate the finite common squareclasses; kill branches locally or by parity; parameterize a surviving conic and repeat the factor/squareclass step before invoking generic elliptic or higher-genus machinery.
- **HYPOTHESES:** primitive integral numerator pair after denominator clearing; exact factorization; pairwise gcd/resultant support under control; sign and valuation bookkeeping complete; every retained squareclass branch represented.
- **APPLICABILITY:** square conditions whose numerator factors into a small collection of low-degree forms with finite shared-prime support.
- **KNOWN SUCCESSFUL USE:** StageA2 A2-4; Stage34-02 has already reused this pattern.
- **STAGE34 LIVE USE:** `stages/stage34/34-02/d2-stageA2-weapon-applicability-lock.json` explicitly names this as `A2-W01`, marks it directly applicable to the matching-x reconstruction condition, and records `StageA2_factor_descent_method_reused=true`. `d2-stageA2-style-reconstruction-factor-lock.json` applies it to the factorizations `H1/H2` and routes next work through exact gcd/resultant support and squareclass branches.
- **STAGE34 SNAPSHOT:** PR `#1480`, branch `stage34-ext-c-main`, observed head `d1d356baa838f1f85561b267dffb18ebd3ce5b9c`. Active Stage34 authority must be refetched at use time.
- **LIMITATIONS:** finite support is not the same as exact branch list; local survivor is not a rational point; factor similarity is not a curve adapter.
- **DO_NOT_USE_FOR:** StageA2 coefficients, `-18` family, old `Q5` eliminations, exact delta sets, rank-zero conclusion, or StageA2 family closure.
- **EXISTING ARSENAL OVERLAP:** related to older local/squareclass techniques but no formal card currently captures this successive low-degree factor -> exact squareclass -> reparameterize -> factor-again pattern.
- **DECISION:** `NEW_CARD_CANDIDATE`; provisional only.

---

## A2-W02 — COMMON_JACOBIAN_COMPRESSION_OF_TWO_COVERS

- **PRIMARY CLASSIFICATION:** `ARSENAL_CANDIDATE`
- **SECONDARY:** `WORKFLOW_CANDIDATE`
- **PATTERN:** compute exact binary-quartic invariants for several genus-one covers; group covers sharing a Jacobian candidate; require an actual source-locked `Q`-isomorphism rather than same `j` or same invariants alone; certify full MW information once on the common Jacobian and transport only through audited maps.
- **KNOWN USE:** A2 compressed its two surviving quartics to one rank-zero Jacobian; Stage34-02 independently compresses fourteen quartics to seven common Jacobians.
- **LIMITATIONS:** common Jacobian does not imply the same rational-point subset or reconstruction image. Rank/torsion are receiver-specific.
- **DO_NOT_USE_FOR:** importing StageA2 rank `0`, torsion, eight-point list, or closure into another receiver.
- **EXISTING ARSENAL OVERLAP:** strongly overlaps `S31-W01` plus `S31-WF01`.
- **DECISION:** `MERGE_EXTEND_EXISTING_S31`; no standalone new formal card recommended.

---

## A2-W03 — COMPLETE_COVER_POINTSET_PULLBACK_WITH_LANDMARKS

- **PRIMARY CLASSIFICATION:** `ARSENAL_CANDIDATE`
- **SECONDARY:** `WORKFLOW_CANDIDATE`
- **PATTERN:** after proving a complete rational-point set on an auxiliary cover/Jacobian, reconstruct every finite point, chart pole, projective infinity, exceptional point and degenerate landmark through every prior parameterization, then grant closure only to the represented source family.
- **WHY LOAD-BEARING:** the A2-4 audit found a missing `t=infinity` landmark, repaired it, and showed it mapped to an already excluded wall. This demonstrates that exceptional-locus bookkeeping is part of completeness, not presentation polish.
- **EXISTING ARSENAL OVERLAP:** essentially the historical precursor/specialization of `S31-W03 COMPLETE_POINT_SET_PARAMETER_PULLBACK`.
- **DECISION:** `MERGE_INTO_S31-W03`; no new standalone card.
- **DO_NOT_USE_FOR:** complete auxiliary points -> parent-route/global endpoint closure without exact pullback and coverage proof.

---

## A2 family theorem — no general promotion

- **CLASSIFICATION:** `STAGE_SPECIFIC_NO_PROMOTION`
- **OBJECT:** the published equation-(6) `-18` family studied in StageA2.
- **STATUS:** audited complete family-specific closure.
- **DO_NOT_PROMOTE:** the theorem itself is not an arbitrary-perfect-cuboid theorem and does not supply global coverage.

---

# StageA1 quarantine harvest

## Mandatory source firewall

```text
SOURCE_OBJECT = auxiliary -8 curve
```

StageA1 A1-3 through A1-14 followed an erroneous `-8` auxiliary curve rather than the published equation-(6) `-18` family. The authoritative closure is:

- `stages/stageA1/A1-CLOSE-SOURCE-CORRECTION/result.md`
- blob `d8a7e1ab9681e03dfa6348399f333fcd1a903efe`

Therefore all A1 family-specific mathematical conclusions from A1-3..A1-14 are:

```text
QUARANTINED_INVALID_FOR_MAINLINE
```

They MUST NOT be cited as consequences for the published equation-(6) family, arbitrary perfect cuboids, or perfect-cuboid existence/nonexistence.

Internal arithmetic methods may be reused only after a fresh derivation on the new target object.

## A1-WF01 — CONSERVATIVE_FINITE_MW_RESIDUE_SIEVE

- **PRIMARY CLASSIFICATION:** `WORKFLOW_CANDIDATE`
- **SECONDARY:** `ARSENAL_CANDIDATE`
- **SOURCE_OBJECT:** auxiliary `-8` curve only
- **PATTERN:** with a certified MW basis/generator and explicit rational receiver functions, reduce MW multipliers modulo good primes; test necessary local residue/square conditions; conservatively retain pole/denominator and degenerate classes; combine exact allowed congruences by CRT; store the full survivor set or deterministic digest plus replay verifier.
- **SOURCE:** `stages/stageA1/A1-12/result.md`, blob `6bdaeccad76bb4537c93bd3ce1f726a41ce123d7`; `A1-12/verify.py`, blob `72cd6280d8c5355c0e1b94d5b8aecbd8a875ab8d`.
- **KNOWN SOURCE RESULT:** 384 necessary multiplier classes modulo `3416490` on the auxiliary curve; this numeric result is quarantined.
- **LIMITATIONS:** finite residue pruning is not global closure; pole classes require conservative handling.
- **DO_NOT_USE_FOR:** published `-18` family; StageA2 theorem; Stage32/33/34 receiver without fresh source-specific derivation; arbitrary perfect cuboids.
- **EXISTING ARSENAL OVERLAP:** proof-capable full MW-sieve infrastructure is broader than this historical elementary sieve; certificate replay overlaps `S30-WF02`.
- **DECISION:** preserve as a historical workflow specialization; no formal selector.

## A1-WF02 — PRIME_POWER_FORMAL_GROUP_REFINEMENT

- **PRIMARY CLASSIFICATION:** `WORKFLOW_CANDIDATE`
- **SECONDARY:** `ARSENAL_CANDIDATE`
- **SOURCE_OBJECT:** auxiliary `-8` curve only
- **PATTERN:** instead of adding unrelated good primes indefinitely, deepen an already-active prime through the formal-group filtration; use zero/pole orders of the relevant rational functions and p-adic valuation/unit square criteria to split lifts of surviving MW residue classes modulo higher prime powers.
- **SOURCES:** `stages/stageA1/A1-13/result.md`, blob `0d3c8b276e0c8263d8ee3c4ed00af53ef210d442`; audit `490f71052acb862edbe649f53c2dbe071d03f7a6`; `stages/stageA1/A1-14/result.md`, blob `eaad5c4c5216091121ac22009dfaf28bc1288566`; audit `15bb137ae7096c4e7d308bb81ccf86111fef11cb`.
- **AUDIT STATUS:** the auxiliary-curve formal-group arithmetic was independently recomputed and accepted before the later source correction quarantined mainline applicability.
- **LIMITATIONS:** a retained p-adic class is not automatically a `Q_p` point and never a `Q` point; deeper central classes may need further work.
- **DO_NOT_USE_FOR:** same strong mainline exclusions as A1-WF01.
- **DECISION:** preserve as quarantined historical workflow specialization.

## A1-WF03 — DETERMINISTIC_SURVIVOR_SET_REPLAY

- **CLASSIFICATION:** `WORKFLOW_CANDIDATE`
- **SOURCE_OBJECT:** auxiliary `-8` curve only
- **PATTERN:** exact sorted survivor classes + modulus + SHA-256 + deterministic independent replay.
- **EXISTING ARSENAL OVERLAP:** superseded at the generic level by `S30-WF02 IMMUTABLE_LAYERED_CERTIFICATE_REPLAY`.
- **DECISION:** `MERGE/SUPERSEDED_BY_S30-WF02`; no new card.

---

## Stage32 / Stage33 / Stage34 cross-check

- **Stage32:** no exact current receiver match identified. Do not claim applicability merely because finite enumeration/lattice compression exists there.
- **Stage33:** no exact current receiver match identified. Picard/Kummer/source-adapter work is a different domain.
- **Stage34:** direct positive match. The active Stage34-02 PR has already source-locked `A2-W01/W02/W03`; the A2 factor-descent method is actually reused, not merely proposed. Stage34 currently differs at the decisive arithmetic step because its seven common Jacobians have positive rank (1 or 2), so A2's rank-zero point enumeration does not transfer.

Stage34 evidence observed on PR #1480:

- `stages/stage34/34-02/d2-stageA2-weapon-applicability-lock.json`, blob at observed PR head `ae90515cbc94aa6937c5784f073e47109cbcf640`
- `stages/stage34/34-02/d2-stageA2-style-reconstruction-factor-lock.json`, blob at observed PR head `a357a6691e0be4abd4965b3f822c829864d814bf`

Live Stage34 authority overrides this snapshot and must be refetched before use.

---

## Promotion summary

| Candidate | Primary classification | Arsenal action |
|---|---|---|
| `A2-C3P01` | `CLASS3_THEOREM_CONSTRUCTION_PRECEDENT` | new provisional precedent record |
| `A2-W01` | `ARSENAL_CANDIDATE` | new-card candidate |
| `A2-W02` | `ARSENAL_CANDIDATE` | merge/extend `S31-W01` + `S31-WF01` |
| `A2-W03` | `ARSENAL_CANDIDATE` | merge into `S31-W03` |
| A2 final `-18` theorem | `STAGE_SPECIFIC_NO_PROMOTION` | no promotion |
| `A1-WF01` | `WORKFLOW_CANDIDATE` | quarantined historical specialization |
| `A1-WF02` | `WORKFLOW_CANDIDATE` | quarantined historical specialization |
| `A1-WF03` | `WORKFLOW_CANDIDATE` | generic layer superseded by `S30-WF02` |
| A1-3..A1-14 family conclusions | `QUARANTINED_INVALID_FOR_MAINLINE` | never promote |

## Credit firewall

This provisional harvest grants no formal selector, theorem, receiver, route, endpoint, or perfect-cuboid existence/nonexistence credit. Formal promotion requires a separate Arsenal promotion/audit decision.
