# stage33kummer-d

Role: cheap-column scouting and non-e3 seed construction for the Stage33-07 repair 75x10 finite-V4 Kummer matrix.

Source lock: branch starts from Stage33 MAIN exact head `fa7949deee5e134eddc45aff7bc1d6e608e1f286`. Scratch/noncredit only. Do not edit Stage33 authority, controller, MAIN-STATE, claim registry, or MAIN R5B artifacts.

Startup:
1. `AGENTS.md`
2. `stages/stage33/MAIN-START-HERE.md`
3. `stages/stage33/33-07/ROADMAP-REPAIR-BAND.md`
4. `stages/stage33/MAIN-STATE.json`
5. this file
6. exact source-specific retained assets discovered search-first

Question: among the remaining adapted labels `e3,e1,e4,e5,e6,e7,e8,e9,e10`, which source has the shortest exact path to a genuine full-surface H2(mu2) lift and Kummer column? The current MAIN e3/A2_02 route is not assumed to be the cheapest next column.

Required work: construct a source-by-source cost/evidence table using exact existing assets; exclude e3/R5B from duplication; select the best non-e3 candidate; then push that candidate to a real column checkpoint rather than stopping at ranking. Re-rank after every new exact blocker.

## Exact checkpoint reached — B

Evidence: `parallel/lane-d/cheap-non-e3-source-checkpoint.json`.

The locked proper-invariant source rows give the following deterministic first-pass coordinate weights for lane-d candidates:

| source | weight |
|---|---:|
| `e1` | 1 |
| `e5` | 2 |
| `e8` | 2 |
| `e4` | 3 |
| `e6` | 3 |
| `e9` | 3 |
| `e10` | 3 |
| `e7` | 4 |

This weight is only a source-coordinate complexity proxy; it is not a theorem about geometric lift cost. It nevertheless makes `e1` the unique cheapest exact source to push first.

For `e1`, the source is now locked literally as the proper-Br2 14D row

`[0,1,0,0,0,0,0,0,0,0,0,0,0,0]`.

The exact first blocker is not linear algebra. `full-surface-pic2-kummer-target.json` already fixes the 75-dimensional target quotient and states `kummer_extension_class_missing=true`; the Kummer contract requires a genuine full-surface H2(mu2) lift (or equivalent exact glue datum) before the action difference can be localized into a 75-vector. The V36 reuse-first locator explicitly reports that no locator-registered positive asset directly supplies such a standalone lift for any remaining adapted source, including `e1`.

This is deliberately weaker than a repository-absence or mathematical-nonexistence claim. The V36 anti-inference firewall says a locator miss does not prove repository absence. The exact lane-d blocker is therefore: **the locked `e1` source has no currently registered source-bound positive lift capable of instantiating the Kummer defect map; a new literal full-surface mu2/Čech/Gersten lift datum must be derived before any `e1` 75-vector can be materialized.**

The read-only e3/R5B preflight confirms the level of data required: even after source-bound common-refinement/orbit-difference attachment, it still withholds H2 credit until literal cover-indexed unit/cochain formulas and the overlap identities exist. Lane-d did not modify any e3/R5B file.

Next tier: `e5` and `e8`, both source-row weight 2. No registered positive-lift asset currently breaks that tie, so the deterministic fallback order is `e5` then `e8`, unless a newly derived/registered source-bound positive lift appears first for one of them.

Checkpoint B is satisfied: the uniquely cheapest non-e3 source has been pushed past ranking to an explicit source-bound missing geometric object, and the next-best tier is justified without guessing a Kummer column.

Checkpoint: either (A) at least one non-e3 adapted Kummer column is materialized exactly, or (B) the cheapest candidates are each reduced to explicit source-bound blockers with a justified next-best candidate.

Firewall: no search-miss-to-absence claim; no guessed column; no R5B subtask cloning; no authority/progress promotion; no merge. NONCREDIT / NO-MERGE.
