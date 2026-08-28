# Stage32-18AI — parallel b16 algorithm scout

18AG (lower48 activity order) and 18AH (pairwise exact symmetry) both closed 0/6 remaining x1024 walls. 18AH reached the 45-minute wallclock on all six walls, so the next step is not another full six-wall production run.

This stage races several exact-search viewpoints inside one Actions workflow with one matrix-level `max-parallel` bound. Two representative hard walls are used for scouting: p436-s5 and p922-s13. Each algorithm gets the same x1024 shard semantics, exact source artifact, bound 16, symmetry scheduler 1.0, node cap, and wallclock budget.

Variants:

- `baseline`: the successful 18AF scheduler-1.0 certifier, used as the control.
- `pairwise-deep`: exact two-row Gram/KKT symmetry propagation, but only deep in the DFS (`last_remaining <= 20`) and only for a small severe candidate set. Floating arithmetic schedules checks only; rejection remains exact.
- `lower48-reverse`: a semantics-preserving relabeling of coordinates 0..47 while coordinates 48..62 remain fixed, giving a deliberately different elimination/tree order without changing x1024 shard identity.

The scout is comparative only. No global b16, d16, theorem, receiver, or controller credit is authorized. No finer split is authorized. A winning variant must be a non-baseline challenger that beats the baseline on both exact search progress and resource use before being promoted to all six walls. The summarizer therefore records `best_observed_algorithm` separately from `promotable_winner`; rank 1 alone is not sufficient for promotion.

## Audited frozen outcome

The existing heavy evidence is retained; no heavy rerun is required. Run `33124686161`, summary artifact `9668228265`, digest `sha256:487e3c8d5e8ef9b1947ca520f421b07415032cd170c0ceb1f6a644f039b1fb03` gives ranking `baseline > pairwise-deep > lower48-reverse`, with zero COMPLETE jobs across all six scouts. Baseline and pairwise-deep hit the 6M node cap on both representative walls; lower48-reverse hits one node cap and one 900s wallclock.

Accordingly, `best_observed_algorithm = baseline` but `promotable_winner = NONE`. Baseline is a control, not a challenger, and 18AF already establishes that the remaining six walls do not close even at the larger 18M node cap. The corrected handoff is therefore `32-18AJ-D16-B16-ALGORITHM-REDIRECTION`, not `32-18AJ-D16-B16-PROMOTE-SCOUT-WINNER`.
