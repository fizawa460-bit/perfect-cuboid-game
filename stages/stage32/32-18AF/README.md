# Stage32-18AF — b16 tail algorithm redesign

18AE exhausted simple geometric splitting: 12 unresolved logical x16 cells entered x1024 and all 12 remained unresolved. Each cell split into one COMPLETE child and one `RESOURCE_WALL_NODE_CAP` child, so x2048 is explicitly not authorized.

18AF attacks the search tree rather than the partition. A representative hard child (`p436/s176`) reaches the 18,000,000 node cap in 1490.56 s, while its sibling (`p436/s688`) completes with zero survivors in 219,602 nodes and 10.54 s. This ~82x node asymmetry rules out a mere near-cap miss.

The first redesign targets the symmetry-prune scheduling heuristic. The certifier currently uses floating arithmetic only to decide whether to attempt an exact rational Cauchy–Schwarz impossibility proof; floating arithmetic never rejects a branch. The historical scheduler attempts a symmetry proof only when `-center > 1.25 * reach`. 18AF changes only this scheduling threshold to `1.0 * reach`. Every actual prune remains guarded by the same exact rational inequality, so mathematical exactness is unchanged; the hypothesis is that the 1.25 margin is postponing exact symmetry rejections and allowing the hard-side trees to explode.

The pilot reruns exactly the 12 frozen x1024 wall shards, with no further shard splitting and the same 18,000,000 node cap. Outcomes are diagnostic only; all Stage32 numerical/global/theorem/receiver firewalls remain false.

If all 12 close, proceed to resource-safe exact b16 production design. If only some close, keep the reduced wall set and try a second algorithmic redirection. If none close, reject this hypothesis and move to a different redesign (ordering / stronger exact bound propagation), not x2048.
