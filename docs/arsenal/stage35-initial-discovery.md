# Stage35 / Stage35-EX Arsenal initial harvest discovery ledger

Status: `DISCOVERY_ONLY_NOT_ARSENAL_PROMOTION`

This file is the human-readable companion to `docs/arsenal/stage35-initial-discovery.json`. The JSON is the machine-readable candidate ledger and contains the full per-candidate fields requested for Harvest 1.

## Firewalls

This PR is discovery only. It does **not**:

- modify `docs/arsenal/index.json`;
- modify generated Arsenal cards or catalog;
- assign final/stable PW/WF IDs;
- modify Stage35 MAIN state;
- modify Stage35-EX authority;
- add theorem, receiver, endpoint, R29/FIB2/J12, E1, or Stage35 closure credit;
- authorize merge.

No negative route is promoted as a mathematical weapon.

## Frozen harvest boundary

Harvest 1 has no earlier Stage35 Arsenal checkpoint, so the lower bound was reconstructed from Git/main history rather than from a working-branch `SOURCE_HEAD`.

- Stage35 canonical inception: `43b5cc4a655cf68e9bdefad22800071d6f8d9fa0`, merge of PR `#1506` (`[Stage35] Sharpen moving-fiber arithmetic Class3 wall`). This is the first authoritative main introduction of the Stage35 35-01..09 corpus.
- Stage35-EX canonical inception: `7423eab4043f2846ca54d02c4323dce40eaac105`, the oldest authoritative main-path commit introducing the bounded Stage35-EX startup charter.
- Harvest upper bound / current main at Harvest start: `9184c7ab694415592cc428a675c0ebed27cac510`.
- Scope: union of Stage35 inception -> upper bound and Stage35-EX inception -> upper bound.
- Old Stage35/EX working-branch `SOURCE_HEAD` values were **not** used as ancestry premises.
- The upper bound remains frozen for this Harvest 1 continuation even if `main` advances later.

## Arsenal lookup discipline

The lookup order was:

1. `docs/arsenal/index.json` at the frozen upper bound;
2. only semantic near-neighbor generated cards.

The strongest current near-neighbors are:

- `S34-W01` — successive exact factor/squareclass descent;
- `S34-W03` — receiver-specific/local intersection closure;
- `S34-WF01` — Class3 receiver replacement theorem pipeline;
- `S33-PW04` — exact marked-source adapter;
- `S33-PW07` — Brauer/torsor/cohomological semantics.

The Stage35 harvest therefore treats squareclass and proper Picard/Brauer candidates conservatively: resemblance to a Stage35 leaf is not enough for `NEW_WEAPON` classification.

## Discovery totals

| Class | Meaning | Count |
|---|---|---:|
| A | probable `NEW_WEAPON` | 11 |
| B | probable `EXTEND_EXISTING` | 7 |
| C | probable `NEW_WORKFLOW` | 6 |
| D | `STAGE35_SPECIFIC` | 3 |
| E | `HISTORICAL_OR_NEGATIVE` | 6 |
| F | unresolved | 3 |
| **Total** |  | **36** |

These are temporary classifications only. No stable Arsenal ID is assigned.

## A — probable NEW_WEAPON

| Temporary ID | Candidate | Main reusable contract | Nearest overlap / boundary |
|---|---|---|---|
| `DISC-S35-A01` | Primitive counterexample -> double Pythagorean product rectangle | gcd normalization -> two primitive Pythagorean branches -> cross-equation -> coprime product rectangle | upstream of `S34-W01`; no factorwise-square or endpoint credit |
| `DISC-S35-A02` | Pairwise gcd reservoir support decomposition | exact pairwise gcd support + 2-adic bookkeeping for four-factor branches | `S34-W01` precondition extension; dynamic primes remain |
| `DISC-S35-A03` | Complete bridge squareclass graph | one auditable graph containing all factor-sharing channels and reservoirs | not finite exhaustive squareclass descent |
| `DISC-S35-A04` | Dual-orientation Gaussian squareclass coupling | intersect squareclass information from two Gaussian orientations after unit/conjugation control | useful only when second orientation is genuinely independent |
| `DISC-S35-A05` | Base-involution receiver descent | invariant quotient plus exact converse/orbit accounting | quotient/fixed-locus adapter; no emptiness theorem |
| `DISC-S35-A06` | Rational-source Kummer normal form | rational source -> explicit Kummer receiver with forward/converse maps | source semantics overlap `S33-PW04`, construction differs |
| `DISC-S35-A07` | Full rational-source Kummer completion | partial Kummer receiver -> complete finite K1-K4 receiver | complete model, not MW/point-set closure |
| `DISC-S35-A08` | Reciprocal common-factor Kummer compression | K1-K4 reciprocal system -> smaller shared-factor equivalent receiver | new compression candidate, not contradiction |
| `DISC-S35-A09` | Primitive edge-gcd six-variable decomposition | `A=xy a, B=xz b, C=yz c` with exact justified coprimality/parity dictionary | `S34-W01` preparation only; not universal torsor |
| `DISC-S35-A10` | Exceptional-prime classification by census + Weil completion | exact small-prime census + auxiliary-curve Weil bound -> finite exceptional-prime set | local classification only; nearest `S34-W03` |
| `DISC-S35-A11` | p-adic valuation cone / cross-face gap coupling | valuation rules + `(W-D)(W+D)=A_i^2` signed-gap coupling | p-specific hypotheses; no global closure |

Particularly strong provisional candidates are A01, A04, A05-A10. A06-A08 form a coherent but separable Kummer chain and should not be merged merely because they occurred consecutively.

## B — probable EXTEND_EXISTING

| Temporary ID | Candidate | Probable target |
|---|---|---|
| `DISC-S35-B01` | Four-bilinear-factor product-square receiver | `S34-W01` |
| `DISC-S35-B02` | Direct full-endpoint genus-5 reconstruction adapter | `S34-WF01` / receiver-replacement adapter discipline |
| `DISC-S35-B03` | Full marked proper Picard/Galois adapter | `S33-PW04` |
| `DISC-S35-B04` | Proper `H^1(G,Pic)` -> algebraic Brauer computation | `S33-PW07` or adjacent Brauer card |
| `DISC-S35-B05` | Finite forced-prime support receiver | `S34-W01` precondition/routing extension |
| `DISC-S35-B06` | Primitive source-marking endpoint equivalence | `S33-PW04` |
| `DISC-S35-B07` | Elliptic quotient structure inventory for diagonal genus-5 family | existing elliptic/genus-one routing if exact semantic match exists |

The most important dedup firewall is B03/B04: the harvested calculation is for the **proper** model. It must not be silently transferred to the open receiver.

## C — probable NEW_WORKFLOW

| Temporary ID | Workflow | Contract |
|---|---|---|
| `DISC-S35-C01` | Post-new-receiver breadth re-audit | every materially new receiver forces a fresh route census before further narrowing |
| `DISC-S35-C02` | Negative-route ledger / anti-loop freeze | record exact blocker, non-claim, and explicit reopen condition |
| `DISC-S35-C03` | Source-lock validation chain | exact locator -> minimal adapter -> verifier -> immutable blob/head provenance |
| `DISC-S35-C04` | Receiver replacement discipline | freeze receiver quantifiers before replacing a named theorem species |
| `DISC-S35-C05` | Endpoint gauge return firewall | prevent circular reuse of endpoint assumptions after long quotient/reconstruction chains |
| `DISC-S35-C06` | Exact-head hostile-audit provenance discipline | pin exact head/base/CI/certificates before promotion |

C04 is probably an extension/application of `S34-WF01`; C03 is close to the provenance/failure contract already embodied by `S33-PW04`. Harvest 2 must check whether C01/C02/C05/C06 already exist elsewhere in Research OS before assigning any new workflow role.

## D — Stage35-specific

- `DISC-S35-D01`: the specific Testa-Stoll `TS-S-R3-Q1` full-endpoint genus-5 route.
- `DISC-S35-D02`: the specific proper Stage35 compactification algebraic-Brauer result.
- `DISC-S35-D03`: the three explicit Stage35 face Gaussian factorizations. The generic factorization method is classical; the formulas are source-specific.

These are useful provenance or worked examples, not standalone Arsenal weapons in their current form.

## E — historical / negative route ledger

| Temporary ID | Negative result | Exact non-claim |
|---|---|---|
| `DISC-S35-E01` | Dynamic support blocks current fixed-S S-unit/Thue closure | does not rule out a later reservoir-collapse lemma |
| `DISC-S35-E02` | Naive bridge factorwise descent does not close the complete squareclass receiver | new gcd/support input may reopen it |
| `DISC-S35-E03` | Tested v2/product-hypotenuse transformation does not give strict self-descent | not an impossibility theorem for all descents |
| `DISC-S35-E04` | Genus-one/elliptic quotient structure does not imply all-`t` moving-family closure | stronger specialization theorem could reopen |
| `DISC-S35-E05` | No certified globally exhaustive finite-fiber reduction | future global reduction is not excluded |
| `DISC-S35-E06` | Fourth-square condition is automatic over `Q_2` under the retained parity dictionary | says nothing about odd primes or global fourth-square redundancy |

These should remain searchable negative assets but **must not** become `NEW_WEAPON` cards.

## F — unresolved

- `DISC-S35-F01`: open-receiver boundary Picard/Brauer adapter. This is the main unresolved global-surface candidate. Proper Picard/Brauer results are insufficient without an exact boundary-divisor/open sequence.
- `DISC-S35-F02`: forced-prime support -> squareclass parity lift. Potentially important for `S34-W01`, but arbitrary-prime parity control and audit authority are not yet resolved.
- `DISC-S35-F03`: joint local Hilbert reciprocity / vertical Brauer source lock. No obstruction credit until an exact unramified class and nonconstant local evaluation are obtained.

## Strongest Harvest 1 candidates

The 10 candidates worth revalidating first are:

1. `DISC-S35-A01` — double-Pythagorean / product-rectangle reduction chain.
2. `DISC-S35-A04` — dual-orientation Gaussian squareclass coupling.
3. `DISC-S35-A05` — base-involution receiver descent.
4. `DISC-S35-A06` — rational-source Kummer normal form.
5. `DISC-S35-A07` — full rational-source Kummer completion.
6. `DISC-S35-A08` — reciprocal common-factor Kummer compression.
7. `DISC-S35-A09` — primitive edge-gcd six-variable decomposition.
8. `DISC-S35-A10` — exact exceptional-prime classification via finite census + Weil completion.
9. `DISC-S35-C01` — post-new-receiver breadth re-audit workflow.
10. `DISC-S35-C05` — endpoint gauge return firewall.

A02/A03/B01/B05 are mathematically useful, but their relationship to `S34-W01` is so close that Harvest 2 should default to `EXTEND_EXISTING` unless a genuinely different contract survives semantic comparison.

## Provenance notes

The machine-readable ledger records for each candidate:

- source cluster;
- reusable input/output;
- hypotheses and quantifiers;
- field;
- exact reduction/construction;
- applicability and failure boundary;
- semantic credit boundary;
- nearest Arsenal card and suspected overlap;
- source PR where resolved;
- exact source snapshot/head/commit;
- certificate path;
- verifier where resolved;
- Git blob SHA;
- canonical SHA256 where source-published;
- hostile-audit status;
- positive / negative / workflow / unresolved type.

A missing source canonical SHA256 or exact historical verifier is recorded as `null`/unresolved rather than fabricated. The exact Git object SHA and frozen source snapshot remain available for Harvest 2 provenance repair.

## Harvest 2 handoff

Keep the Harvest 1 mathematical range frozen at `9184c7ab694415592cc428a675c0ebed27cac510`. Do not widen discovery to later main commits while deduplicating this batch.

Harvest 2 should:

1. Revalidate missing source PR/head/review/verifier/canonical-digest fields only for retained A/B/C and unresolved F candidates.
2. Perform exact semantic dedup against `S34-W01`, `S34-W03`, `S34-WF01`, `S33-PW04`, and `S33-PW07`.
3. Keep the Kummer chain A05-A08 split unless two adjacent leaves have the same reusable input/output contract after Stage35 notation is removed.
4. Test whether A10's finite-census + Weil-completion technique survives removal of the perfect-cuboid polynomial family; if not, demote to Stage35-specific.
5. Treat B03/B04 and F01 as separate proper-vs-open questions. No proper-model result may supply open-receiver credit by relabeling.
6. Keep E01-E06 as historical/negative assets only.
7. Determine whether C01/C02/C05/C06 are new Research OS workflows or duplicates of existing policy assets.
8. Do not edit Arsenal index/cards/catalog or assign stable IDs during Harvest 2 unless a later explicit promotion pass is requested.

No merge is authorized by this ledger.
