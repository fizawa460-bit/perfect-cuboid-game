# Stage30 Codex handoff contract

This file defines how Stage30 delegates finite implementation/computation work to Codex without adding a third user-facing Stage30 command.

## Command surface

The only Stage30 commands are:

```text
Stage30-main-batch
Stage30-audit
```

When `Stage30-main-batch` reaches a Codex-owned unit, it must create the exact handoff prompt and set the controller to a waiting state.  The user then gives that prompt to Codex.  When Codex work is present in the repository, the next `Stage30-main-batch` or `Stage30-audit` continues from the repository state.

## Prompt requirements

Every Codex prompt must be complete enough to run without reconstructing Stage30 from chat history.  It must include:

1. repository and exact Stage30 target;
2. exact prerequisite source files to read;
3. explicit statement that all prior results are authoritative only within their audited scope;
4. exact input labels/generator conventions/manifests from the preceding audited substage;
5. required outputs and filenames;
6. exact integer/finite arithmetic requirements;
7. reproducibility and deterministic ordering requirements;
8. independent checker requirement;
9. prohibited shortcuts;
10. scope/firewall statements;
11. final machine-readable status block.

## General Codex prohibitions

Codex must not:

- replace a concrete action by the statement `S4 is isomorphic to S4`;
- silently relabel objects without an explicit bijection table;
- infer Q-defined data from a Q(i)-defined object without a checked descent step;
- infer an arithmetic impossibility from orbit membership alone;
- promote a generic moduli map to an everywhere finite compactified map;
- treat ordinary 8-congruence as an endpoint rarity theorem;
- use floating-point arithmetic for finite group/action/cocycle certification;
- grant theorem credit to an external source without stable locator and exact hypothesis match;
- rewrite audited Stage29 claims merely to simplify implementation.

## Codex Task A — action extraction

Prompt generated at Stage30-02P.

Minimum required deliverables:

```text
stages/stage30/work/action-input-manifest.json
stages/stage30/work/arrangement-action.json
stages/stage30/work/modular-action.json
stages/stage30/work/orbit-stabilizer.json
stages/stage30/work/verify_actions.py
stages/stage30/work/codex-A-result.md
```

The verifier must check group relations, order, faithfulness where claimed, object coverage, orbit partitions, stabilizers, and manifest-label consistency.

## Codex Task B — equivariant identification

Prompt generated at Stage30-04P only after Task A has passed Stage30-03 audit.

Minimum deliverables:

```text
stages/stage30/work/equivariant-candidates.json
stages/stage30/work/marked-compatibility.json
stages/stage30/work/rejected-candidates.json
stages/stage30/work/verify_equivariant_candidates.py
stages/stage30/work/codex-B-result.md
```

The search must be exhaustive over the finite candidate space specified by the audited input manifest.  Every survivor must have an explicit witness; every rejected candidate must have a deterministic failing condition.

## Codex Task C — Galois cocycle + eight defects

Prompt generated at Stage30-06P only after ChatGPT has fixed the exact mathematical cocycle relation.

Minimum deliverables:

```text
stages/stage30/work/galois-cocycle.json
stages/stage30/work/defect-classification.json
stages/stage30/work/verify_cocycle_and_defects.py
stages/stage30/work/codex-C-result.md
```

The eight-defect output must cover all 8 `K8` elements exactly once and record their ordinary conjugacy class, concrete S4 action data, sigma image, adapter image, descent status, and arithmetic-equivalence status.  A classification is not an elimination theorem.

## Codex Task D — final certificate

Prompt generated at Stage30-09P.

Minimum final surface:

```text
stages/stage30/certificates/input-manifest.json
stages/stage30/certificates/action-tables.json
stages/stage30/certificates/equivariant-map.json
stages/stage30/certificates/galois-cocycle.json
stages/stage30/certificates/defect-classification.json
stages/stage30/certificates/verify_stage30.py
```

The final verifier should be independent in structure from the construction scripts wherever practical.  It must fail closed on missing labels, duplicate objects, unmapped marked objects, relation failure, cocycle failure, or field-of-definition ambiguity.

## Result status

Every Codex result must end with a block of the form

```text
CODEX_TASK=<A|B|C|D>
INPUT_SOURCE_LOCK_COMPLETE=true|false
EXACT_ARITHMETIC_ONLY=true|false
OBJECT_COVERAGE_COMPLETE=true|false
CHECKER_PRESENT=true|false
CHECKER_PASS=true|false
UNRESOLVED_ASSUMPTION_COUNT=<integer>
NEW_THEOREM_ASSUMED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

A `CHECKER_PASS=true` result is still unverified external computational input until Stage30 audit consumes it.
