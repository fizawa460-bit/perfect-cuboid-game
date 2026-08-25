# Stage32-18G — exact deep rescue of b12 residue 26-of256

Stage32-18E run `32877018247` completed every ordinary 64-way shard except shard 26; shard 26 hit the workflow timeout after 180 minutes. Stage32-18F then refined that residue exactly from 64-way to 256-way using residues `{26,90,154,218}`. Three of those four (`90,154,218`) completed, while `26-of256` remained the heavy child.

This stage refines only that child again. The exact hash partition identity is

`h % 256 == 26  <=>  h % 1024 in {26,282,538,794}`.

The workflow reuses the immutable Stage32-18E prepared artifact `9574308138` and the same exact certifier, exact 256 Aut breakers, split coordinate 54, bound 12, and full leaf canonicalization. No already-completed 64-way or 256-way residue is recomputed.

The four 1024-way runs are exact production traversals. Their canonical records form a disjoint exact union for logical residue `26-of256`. The synthesis certificate deliberately does **not** pretend that summed node/trial/prune counters equal a hypothetical single 256-way run: each rescue run repeats traversal above split coordinate 54. Those sums are recorded only as rescue execution-work telemetry. `split_prefixes_seen` must agree across all four children and is recorded once as the logical-parent pre-split count.

Firewalls remain closed: no global b12 aggregate, no d16 b12 numerical credit, no full-row credit, no theorem/receiver credit, and hostile audit remains required.
