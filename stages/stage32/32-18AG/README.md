# Stage32-18AG — b16 residual-wall search-order pilot

18AF changed only the floating prefilter for an unchanged exact rational symmetry rejection. It closed 2 of the 12 frozen logical x16 walls (36/48 -> 38/48), while the other 10 remained computationally hostile; several reached the 50 minute wallclock before the 18M node cap. No finer secondary split is allowed.

18AG tests a source-minimal search-order change on the 10 residual x1024 walls. The mathematical feasible set, exact rational symmetry rejection, Aut bundle, primary/secondary partitions, node cap, and b16 firewall are unchanged. Only the DFS value ordering is changed from ascending integer candidates to a deterministic center-out ordering (small |z_i| first, tie by integer value). The hypothesis is that earlier low-norm assignments expose exact norm/symmetry impossibility sooner on the highly imbalanced residual trees.

This is a diagnostic algorithm redesign, not numerical b16 credit. Wallclock timeout is an accepted RESOURCE_WALL_WALLCLOCK result and must still upload compact evidence. If the pilot does not materially close residual logical cells, the next item is stronger exact bounding/constraint propagation rather than x2048.
