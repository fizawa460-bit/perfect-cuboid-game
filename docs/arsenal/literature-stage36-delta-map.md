# Stage36 Delta Literature Map & Triage — Phase 1

Status: **DISCOVERY ONLY — Stage36 delta only**

```text
STAGE36_DELTA_ONLY=true
ARSENAL_BASE_MAIN=386b6a52d7bfec2e8903412c7ca56976b46c288b
STAGE36_ARSENAL_SOURCE_HEAD=2fc3f4b8afb28bb23765bd861cbd7c52aafd6563
STAGE36_HARVEST_SNAPSHOT_HEAD=07a465cb5025e7c0188fb63610bb40e4b54e7a84
STAGE36_DISCOVERY_DEDUP_EXACT_HEAD=0ad4a2fc78ebd3ee55c47d9bf5100d8e4cee3b66
STAGE36_IMPLEMENTATION_PR=1675
STAGE36_IMPLEMENTATION_AUDITED_HEAD=2fc3f4b8afb28bb23765bd861cbd7c52aafd6563
LITERATURE_DISCOVERY_ONLY=true
NO_STAGE30_35_LITERATURE_RESEARCH_REPEAT=true
ARSENAL_BODY_CHANGED=false
INDEX_CHANGED=false
GENERATED_CARD_CHANGED=false
STABLE_ID_CREATED=false
STAGE36_MAIN_CHANGED=false
STAGE36_MATHEMATICAL_CREDIT_CHANGE=0
MERGE_AUTHORIZED=false
```

The machine map is `docs/arsenal/literature-stage36-delta-map.json`; it carries the exact reusable contracts, hypotheses, outputs, `DO_NOT_USE_FOR`, nearest Arsenal cards, cluster routing, bibliography, negative boundaries, and Phase-2 handoff for every accepted Stage36 delta entry.

## Authority / frozen scope

`docs/arsenal/index.json` is the machine authority. At the frozen live main above it exposes exactly seven active Stage36 provisional weapons, `S36-PW01` through `S36-PW07`, and zero active Stage36 workflow IDs. The accepted existing-card extensions are `DISC-S36-B01 -> S30-W01`, `B02 -> S35-PW02`, `B04 -> S34-W03`, `B08 -> S31-W01`, and `B12 -> S34-W02`.

Stage36 Arsenal discovery/dedup is PR #1673 at hostile-audited exact head `0ad4a2fc78ebd3ee55c47d9bf5100d8e4cee3b66`. Stage36 Arsenal implementation is PR #1675 at hostile-re-audited exact head `2fc3f4b8afb28bb23765bd861cbd7c52aafd6563`. The immutable initial-harvest upper bound is `07a465cb5025e7c0188fb63610bb40e4b54e7a84`; PR #1670 / 36-09AB and later Stage36 MAIN movement are not silently pulled into this literature delta.

Prior literature discovery PR #1676 is already merged and explicitly had `STAGE36_EXCLUDED=true`. Its Stage30–35 searches are not rerun here; only semantic near-neighbours are reused as comparison inputs.

## Phase-1 triage

| Entry | Priority | Class | Nearest Arsenal | Main literature route |
|---|---|---|---|---|
| `S36-PW01` character-quotient genus inventory | P1 | `LIT-GENERALIZE` | `S30-W01`, `S31-W01` | Pardini abelian-cover building data / character eigenspaces + Riemann–Hurwitz |
| `S36-PW02` V4 Jacobian decomposition | **P0** | `LIT-DIRECT` | `S31-W01`, `S34-W03` | Kani–Rosen idempotent relations / Jacobian factors |
| `S36-PW03` anti-invariant twist growth gate | **P0** | `LIT-GENERALIZE` | `S30-W02`, `S34-W02` | quadratic-twist eigenspaces + specialization/rank-jump theory |
| `S36-PW04` pointwise elementary-2 torsor lift class | P1 | `LIT-ADAPTER` | `S35-PW03`, `S33-PW09` | torsor `H^1` / Kummer squareclass descent |
| `S36-PW05` split-full-2 order-4 / 2-isogeny normalization | P2 | `LIT-SOURCE-ANCHOR` | `S31-W01`, `S34-W02` | classical 2-isogeny / halving / Kummer maps |
| `S36-PW06` relative 2-isogeny specialization baseline | **P0** | `LIT-DIRECT` | `S34-W02`, `S31-WF01`, `S31-W01` | Silverman specialization + Gusić–Tadić effective injectivity |
| `S36-PW07` directional prime-reservoir local matrix | P1 | `LIT-ADAPTER` | `S35-PW01`, `S35-PW05`, `S33-PW07` | Hilbert symbols, quadratic reciprocity, local Selmer/Kummer conditions, Gaussian prime support |
| `B01 -> S30-W01` field-separated kernel invariants | P2 | `LIT-SOURCE-ANCHOR` | `S30-W01`, `S30-W02` | quadratic/symplectic modules, radical/Arf-type invariants |
| `B02 -> S35-PW02` one-way boundary preflight | P3 | `REPO-SPECIFIC` | `S35-PW02`, `S30-WF03` | quotient/ramification vocabulary; converse remains repo adapter |
| `B04 -> S34-W03` proof-capability preflight | P4 | `NO-PRIORITY` | `S34-W03` | proof-engineering gate, not a literature theorem target |
| `B08 -> S31-W01` successive-cover genus preflight | P2 | `LIT-SOURCE-ANCHOR` | `S31-W01` | Riemann–Hurwitz / double-cover branch theory |
| `B12 -> S34-W02` specialization-growth preflight | **P0** | `LIT-GENERALIZE` | `S34-W02`, `S34-W03` | specialization + rank-jump loci / Hilbert property |

Priority counts over these 12 accepted contracts: **P0=4, P1=3, P2=3, P3=1, P4=1**. Classification counts: `LIT-DIRECT=2`, `LIT-ADAPTER=2`, `LIT-TERMINAL=0`, `LIT-GENERALIZE=3`, `LIT-SOURCE-ANCHOR=3`, `REPO-SPECIFIC=1`, `NO-PRIORITY=1`.

## Cluster routing A–H

- **A finite kernel / stabilizer / radical / squareclass:** primary `B01->S30-W01`; secondary `PW02`, `PW05`. Stage36 adds exact field-separated finite invariants, not a new existence theorem.
- **B reciprocal / birational / reconstruction:** primary `B02->S35-PW02`, `B08->S31-W01`; secondary `PW04`. No separate reciprocal Stage36 card survived hostile dedup: A03/A04/A07 were absorbed by Stage35 contracts.
- **C character / squareclass linearization:** `PW01`, `PW04`, `PW07`, plus B01. B05's pure F2 row-span was correctly rejected as duplicate of Stage35/34 squareclass linear algebra.
- **D Hilbert / reciprocity / local-global:** primary `PW07`; secondary `PW03`, `PW04`, `PW06`. Negative boundaries E06/E07 are load-bearing: product formula is a checksum, and local admissibility is not a global point.
- **E quadratic twists / rank jump / MW:** `PW03`, `PW06`, and `B12->S34-W02` are the densest P0 group; `PW05/PW02` are supporting routes.
- **F finite-field / exceptional primes:** there is no new positive Stage36 card equivalent to `S35-PW05`. `PW07` explicitly forbids finite exceptional-prime credit. `PW01` could feed Weil bounds only through a new exact adapter.
- **G Gaussian / norm / prime support:** `PW07` is the positive Stage36 endpoint for this cluster; its Gaussian directional-support source is supporting provenance, not a separate stable card.
- **H workflows:** machine authority has **zero** Stage36 workflow IDs. B02/B04 are workflow-like existing-card extensions; C01/C02/C03 were deduped into S30 / Research OS workflow discipline.

## Literature-relevant negative boundaries

The Stage36 negative ledger is retained rather than converted into literature claims: `B07` bounded character-linear exhaustion is anti-loop evidence only; `E01/E04` moving or shared prime support blocks unjustified fixed-S descent; `E02` literature cannot repair a missing Brauer source adapter; `E03` character restatement can be endpoint-circular; `E05` high genus alone is not rational-point emptiness; `E06` Hilbert reciprocity alone is not an obstruction; `E07` locally admissible Kummer classes block pure-local closure; `E08` rank-jump witnesses do not imply receiver compatibility/full MW; `E09` failed known lifts are samples, not whole-fiber emptiness; `F01` literature quality cannot override repo hostile-audit maturity.

## Bibliographic reconnaissance

The strongest direct/source anchors found in this bounded Phase-1 search are:

1. Ernst Kani and Michael Rosen, *Idempotent relations and factors of Jacobians*, Math. Ann. 284 (1989), 307–328 — direct family for `S36-PW02`.
2. Ivica Gusić and Petra Tadić, *A remark on the injectivity of the specialization homomorphism*, Glasnik Mat. 47 (2012), 265–275, DOI `10.3336/gm.47.2.03`; and *Injectivity of the specialization homomorphism of elliptic curves*, J. Number Theory 148 (2015), 137–152, DOI `10.1016/j.jnt.2014.09.023` — unusually close to `S36-PW06` because they treat nonconstant `Q(t)` elliptic families with rational 2-torsion/full 2-torsion and effective injectivity criteria.
3. Joseph H. Silverman, *Heights and the specialization map for families of abelian varieties*, J. reine angew. Math. 342 (1983), 197–211, DOI `10.1515/crll.1983.342.197` — general specialization background for `PW03/PW06/B12`.
4. Daniel Loughran and Cecília Salgado, *Rank jumps on elliptic surfaces and the Hilbert property*, Ann. Inst. Fourier 72 (2022), 617–638, DOI `10.5802/aif.3457` — relevant to `PW03/B12`; under hypotheses it controls the rank-jump locus, but gives no receiver compatibility.
5. Rita Pardini, *Abelian covers of algebraic varieties*, J. reine angew. Math. 417 (1991), 191–214, DOI `10.1515/crll.1991.417.191` — source/generalization anchor for `PW01`, B02 and B08.
6. Alexei Skorobogatov, *Torsors and Rational Points*, Cambridge Tracts in Mathematics 144 (2001), DOI `10.1017/CBO9780511549588` — torsor/H1 semantics for `PW04`.
7. Jean-Pierre Serre, *A Course in Arithmetic*, GTM 7 (1973), DOI `10.1007/978-1-4684-9884-4` — Hilbert symbols, reciprocity and Hasse–Minkowski background for `PW07/E06`.
8. Cahit Arf, *Untersuchungen über quadratische Formen in Körpern der Charakteristik 2. (Teil I.)*, J. reine angew. Math. 183 (1941), 148–167, DOI `10.1515/crll.1941.183.148` — possible invariant source anchor for B01.
9. David A. Cox, *Primes of the Form x^2 + ny^2* (Wiley, 1989; later editions), DOI `10.1002/9781118032756` — Gaussian/quadratic reciprocity background for the directional-prime component of `PW07`.
10. Michael Stoll, *Descent on elliptic curves*, arXiv:math/0611694 — **supplement only**, useful for explicit Selmer/Kummer semantics; not selected as peer-reviewed theorem authority in Phase 1.

## Strongest Phase-2 targets

1. **S36-PW06:** lock the exact Gusić–Tadić 2012/2015 criterion/theorem locator and test the exact retained Stage36 Weierstrass family/specialization against every polynomial, squarefree/UFD and nondegeneracy hypothesis.
2. **S36-PW02:** lock the exact Kani–Rosen idempotent relation, field and smoothness hypotheses, quotient genera and independence condition. Preserve `Jacobian isogeny != pointwise source reconstruction`.
3. **S36-PW03 + B12:** separate standard quadratic-twist eigenspace algebra from genuine rank-jump-locus results; test Loughran–Salgado hypotheses without importing receiver/full-MW credit.
4. **S36-PW07:** bind every self/cross/dyadic/real row to exact Hilbert/Kummer local-condition formulas and test whether a genuine Selmer-local adapter exists despite dynamic support. Preserve E06/E07.
5. **S36-PW01 + PW04:** lock Pardini-style character/building-data results for PW01 and actual torsor-H1 semantics for PW04 without importing Stage33 marked Brauer/H2 semantics.

## Novelty / credit firewall

No miss in this bounded search licenses `NOVEL`, `NEW_THEOREM`, or `FIRST_RESULT`. The strongest permitted miss label is `NO_DIRECT_MATCH_FOUND_IN_THIS_BOUNDED_SEARCH`. Literature theorem provenance and repo adapter provenance remain distinct. No Stage36 receiver, rank, Mordell–Weil, Hilbert-reciprocity endpoint, local-global obstruction, theorem, closure/release, or perfect-cuboid credit is changed by this artifact.
