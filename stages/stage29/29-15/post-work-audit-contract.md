# Stage29-15 — post-Work re-audit contract

This contract is additive to `audit-contract.md` and takes priority where the earlier audit predates the external Work rematch.

## Mandatory fresh-base check

Audit the current PR head, not the previous audited head. The earlier `PASS_AFTER_MATERIAL_POSITIVE_REPAIR` is superseded until this contract passes.

## A. Cao–Demarche–Xu / Cao route compression

Source-check:

1. Cao–Demarche–Xu, Theorem 1.5 / 7.5: smooth quasi-projective geometrically integral `X/k` gives `X(A)^descent = X(A)^{et,Br}`.
2. Cao, Corollary 1.2: `X(A)^{descent,descent} = X(A)^descent` in the same smooth quasi-projective geometrically integral scope.

Verify the audited physical open `U/Q` satisfies the hypotheses.

Required disposition:

```text
ITERATED_DESCENT_ON_PHYSICAL_OPEN=MERGED_NOT_INDEPENDENT_ROUTE
ONE_STEP_DESCENT_ETALE_BRAUER_COMPUTED=false
FINITE_OPEN_TWIST_SET_INFERRED=false
```

Do not interpret equality of obstruction species as emptiness or effectivity.

## B. R29-BR-LINE9 — class-1 hostile audit

Read the exact Ford primary theorem used by the Work report. Confirm:

- theorem applies to the projective seven-line arrangement complement in the asserted `d=2` form;
- the relevant incidence graph is the correct graph for the theorem;
- concurrence relations are handled exactly as stated by Ford.

Independently run/reproduce `verify_brauer_line9.py` and check:

```text
TRIPLE_POINTS=6
DOUBLE_POINTS=3
V=16
E=24
CONNECTED=true
B1=9
```

Only after the source theorem is verified may the audit promote the geometric precursor to the asserted nine-dimensional 2-symbol space.

No promotion to `Br(U)/Br(Q)` or a Brauer–Manin obstruction is allowed.

## C. R29-K3-RULED2 — mandatory class challenge

Read Creutz–Viray, especially the finite presentation theorem for double covers of geometrically ruled surfaces with reduced flat branch and simple singularities.

Then inspect the exact Stage29 K_c equations and Stage28/29-07 model.

The audit must decide one of:

```text
1 EXECUTE_NOW_BOUNDED
2 CURRENT_TOOL_LIMIT_EXECUTED
4 DORMANT_NONDECISIVE
```

Class 3 is forbidden unless the first missing input is genuinely a theorem rather than explicit geometry/CAS work.

If a ruled model can be obtained by a bounded birational contraction/transformation from existing equations, promote to class 1 and execute the finite Creutz–Viray presentation on this same PR before PASS.

If it remains class 2, state the exact missing transformation/equations/CAS output. `Bl_4(P1xP1)` may not be called geometrically ruled without an explicit valid model.

## D. Other Work matches — anti-proliferation screen

Audit the external Work leads:

- Dimitrov–Gao–Habegger uniform Mordell–Lang;
- de Grey–Gibbs–Helm aspect-ratio filters;
- Luca + Li square-Heron/bisector model;
- Balestrieri–Johnson–Newton singular-K3 Brauer effectivity;
- Creutz–Viray Kummer two-primary sufficiency;
- Stoll proper finite descent;
- Bauer–Stoll Burniat/etale-product theorem;
- Browning–Loughran/Huang ambient sieve.

Do not create a new OPEN receiver merely because a model or theorem is interesting. Create one only if it adds a distinct executable or theorem-level endpoint task not already represented by the current 46-item provisional census.

Any newly created finite tractable receiver is class 1 and must be executed before PASS.

## E. Census target

The current provisional census is

```text
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=46
CLASS1_IDENTIFIED_COUNT=6
CLASS1_EXECUTED_COUNT=6
CLASS1_PENDING_COUNT=0
CLASS2_COUNT=13
CLASS3_COUNT=11
CLASS4_COUNT=16
```

These numbers are not assumed correct. Reconstruct them independently.

## F. Required final output delta

In addition to the original audit output, report:

```text
POST_WORK_INPUT_AUDITED=true|false
R29_BR_LINE9=<disposition>
FORD_B1_GAMMA=9|INVALID
R29_K3_RULED2=<class/disposition>
ITERATED_DESCENT_ON_PHYSICAL_OPEN=MERGED|NOT_MERGED|INVALID
ONE_STEP_DESCENT_ETALE_BRAUER_EQUIVALENCE=VERIFIED|INVALID
NEW_WORK_RECEIVER_COUNT=<integer>
RECEIVER_OR_TERMINAL_FRONTIER_COUNT=<integer>
CLASS1_IDENTIFIED_COUNT=<integer>
CLASS1_EXECUTED_COUNT=<integer>
CLASS1_PENDING_COUNT=<integer>
CLASS2_COUNT=<integer>
CLASS3_COUNT=<integer>
CLASS4_COUNT=<integer>
VAGUE_AMBER_WITHOUT_EXECUTION_CLASS_COUNT=<integer>
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

PASS still requires `CLASS1_PENDING_COUNT=0` and zero vague AMBER entries.
