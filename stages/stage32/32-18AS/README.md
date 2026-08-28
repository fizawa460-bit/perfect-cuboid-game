# Stage32-18AS — b16 heavy frontier tier-2 cost planner

18AR measured all 4,103 cut39 frontier states with a 2,048-node local exact probe. 3,421 states completed within that probe; 682 were capped and are the only targets here.

18AS does not run production. It imports the immutable 18AR plan artifact and probes exactly those 682 heavy frontier IDs with a larger 32,768-node local exact budget. IDs that finish receive an exact lower-subtree cost. IDs that still exceed the cap are retained as tier-3 monster candidates rather than blended into an average.

The output merges the exact 18AR light costs with newly resolved tier-2 costs, reports tier-2 quantiles and the unresolved monster list, and builds a balanced weighted plan for all resolved states. This is a query-planner phase: measure workload distribution first, then choose production partitions.

The logical owner remains p436/s5 in the frozen x1024 partition. Frontier IDs are an internal resumable work queue only, not a new canonical shard partition. No b16 numerical credit, global aggregation credit, theorem credit, receiver credit, or controller modification is allowed here.
