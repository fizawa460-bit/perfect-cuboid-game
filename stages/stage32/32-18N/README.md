# Stage32-18N — b14 descendant-work load profile

Stage32-18M shows that raw population at the coordinate-54 FNV frontier is not an adequate runtime proxy: the historical b12 pathological residue `26 mod 1024` has only 66 coordinate-54 prefixes and ranks 744/1024 by raw population.

This leaf measures actual exact DFS work **below** the coordinate-54 parent frontier. For every surviving parent prefix, the profiler keeps its `h54 mod 1024` bucket active while exact rational traversal continues to a fixed probe coordinate. It records per-parent-bucket descendant nodes, coordinate trials, exact cap prunes, exact symmetry prunes, and surviving probe prefixes. Traversal stops at the probe and never reaches canonical leaves, so no new b14 census or numerical credit is claimed.

Calibration and application are paired:

- b12 probes at coordinates 50, 48, 46 test whether descendant work recovers the known pathological residue 26;
- b14 probes at the same coordinates measure the corresponding next-wall load geometry;
- the compact profiler also folds the 1024 exact buckets into congruent mod-256 and mod-64 views, so a later production design can choose a coarse first partition and refine only genuinely heavy residues without inventing telemetry.

A probe depth is considered calibrated when residue 26 reaches the top 64 by at least one of descendant nodes, descendant trials, or surviving probe-prefix population. The shallowest calibrated depth is preferred because it is cheaper to profile while still detecting the known b12 pathology. If no tested depth calibrates, Stage32 must profile deeper before any b14 production run.

Firewalls remain closed for new bounds: `D16_B14_NUMERICAL_CREDIT=false`, `FULL_BOUND_TRAVERSAL_COMPLETE=false`, `FULL_D16_G0_ROW_COMPLETE=false`, `THEOREM_CREDIT=false`, `RECEIVER_CREDIT=false`, `CONTROLLER_MODIFIED=false`.
