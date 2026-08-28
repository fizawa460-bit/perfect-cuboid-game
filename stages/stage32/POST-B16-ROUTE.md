# Stage32 post-b16 route — search-space reduction first

This note ports the Stage33 #1445 route discipline into Stage32 so the controller does not spend time scanning a large target surface after the d16/b16 calibration closes.

## Priority rule

After audited d16/b16 closure, Stage32 must reduce the set of things worth reading before doing broad literature or production work.

Required order:

1. Freeze the exact 183-row Stage32 population and all currently known structural invariants.
2. Build a compact candidate mask from invariants already present in the repository (degree/genus bounds, node/singularity pattern, symmetry/Aut data, Picard/lattice data, previously audited low-degree closures, and route-specific hypotheses).
3. Run cheap exact eliminators and classification checks first.
4. Only then search literature against the surviving rows/hypothesis profiles.
5. Only source-lock and adapt theorems that match at least one surviving receiver profile.
6. Hostile-audit the resulting residual mask.
7. Run expensive production only on the hostile-audited residual population.

The objective is not to prove less. It is to minimize the number of rows, hypotheses, papers, and adapters that need human/AI attention before the correct route becomes visible.

## Compact receiver views

The post-b16 literature phase must maintain at least these progressively smaller views:

- `ALL_183`: immutable full audit universe.
- `STRUCTURALLY_LIVE`: rows not eliminated by already-audited repository facts.
- `LITERATURE_RELEVANT`: structurally live rows grouped by theorem-hypothesis signature.
- `SOURCE_LOCK_REQUIRED`: theorem/receiver pairs with a concrete plausible match.
- `AUDITED_RESIDUAL`: only rows/subpopulations still live after hostile theorem-adapter audit.

Broad searches over `ALL_183` are forbidden once a smaller exact view is available.

## Literature families

The existing Stage32 families remain valid starting points:

- `LIT32-FSM`
- `LIT32-GF`
- `LIT32-BTVA`
- `LIT32-TS`

They are seeds, not a mandatory exhaustive reading list. Search expansion must be driven by the surviving receiver signatures, not by author/title breadth.

## Firewalls

- A compact mask never deletes a row unless the underlying elimination is already exact/audited.
- Heuristics may rank what to inspect first but may not grant mathematical credit.
- A theorem matching only a subpopulation may not delete a whole row.
- Source lock + explicit hypothesis adapter + hostile audit remain mandatory before theorem/receiver credit.
- No expensive 183-row production campaign may start before the compact residual view is frozen and audited.

Expected post-b16 order:

`audited b16 -> compact structural mask -> targeted literature receiverization -> hostile residual audit -> residual feasibility gate -> residual production`
