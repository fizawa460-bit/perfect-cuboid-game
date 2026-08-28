# Stage32-18AR — b16 frontier cost planner

18AQ showed why the earlier first-N replay scout was not representative: the first 64 cut39 frontier states were light, while later states drove the full run into the 18M node cap. 18AR therefore measures the workload distribution before any further production partition is chosen.

For every one of the exact 4,103 cut39 frontier states of p436/s5, the ordinary exact lower DFS is entered with a local probe budget of 2,048 DFS nodes. If the subtree finishes inside that budget, its exact lower-node cost is recorded. If it does not, the frontier is marked `capped/heavy`; no numerical conclusion is taken from the partial subtree.

The planner emits one row per frontier and computes cost quantiles/histograms for completed probes, the complete/capped counts, heavy frontier IDs, and a balanced 12-bin plan for the measured light states. Heavy states are not silently averaged into the light estimate: they are isolated for either a second-tier probe or singleton/small-batch production.

This is analogous to a query-planner/COUNT pass before the expensive query. It is architecture and workload evidence only. The frozen x1024 ownership boundary and coordinates 48..62 are unchanged, `allow_finer_split=false`, and all numerical/global/theorem/receiver/controller firewalls remain false.
