# Stage32-18I — two-stage rescue inside the pathological b12 prefix

Stage32-18G isolated the remaining heavy region to primary residue `h54 % 1024 == 26`. Three sibling residues completed quickly while residue 26 remained an outlier. This stage keeps that primary gate exact and adds a second exact FNV64 partition only after DFS reaches coordinate 45.

Primary gate: split coordinate 54, residue 26 of 1024. Secondary gate: split coordinate 45, 32 disjoint shards. This is a true subdivision inside the heavy prefix, not another modulo refinement at coordinate 54.

All census/theorem/controller credit remains false pending complete synthesis and hostile audit.
