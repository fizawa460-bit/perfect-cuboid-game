# Stage32-18AF — b16 tail algorithm redesign

18AE exhausted simple coordinate-48 refinement at x1024: 12/24 new children completed, but every unresolved logical x16 cell retained exactly one x1024 node-cap child, so closure stayed 36/48.

18AF does **not** create x2048 shards. It attacks the same 12 frozen x1024 walls with a source-minimal pruning change: the floating prefilter that merely decides whether to attempt an exact symmetry impossibility proof is tightened from `1.25 * reach` to `0.5 * reach`, matching the already-audited cap-prefilter aggressiveness. The actual rejection remains the same exact rational Cauchy–Schwarz test `exact^2 > budget * dual`; floating arithmetic still cannot reject a branch.

Representative 18AE evidence shows the issue is structural rather than a marginal cap miss: for parent `(p436, x512=176)`, wall child x1024=176 hit 18,000,000 nodes in 1490.56 s, while sibling x1024=688 completed with zero survivors in 219,602 nodes / 10.54 s. This ~82x tree imbalance motivates earlier exact symmetry-prune attempts rather than further partition refinement.

The 12 frozen walls are rerun at the same x1024 partition and same 18M node cap. Any completed wall immediately closes its logical x16 parent because its sibling is already frozen COMPLETE in 18AE. Remaining walls after this experiment advance to a deeper algorithm-design leaf, not x2048.

All numerical/global/theorem/receiver/controller firewalls remain false until reconstruction and hostile audit.
