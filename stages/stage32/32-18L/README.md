# Stage32-18L — final rescue-aware d16 b12 production aggregate

This stage is the final exact integration boundary for the d16 `b=12` census.

Coverage is assembled without rerunning completed work:

- 63 ordinary Stage32-18E 64-way shards (`all except 26`);
- Stage32-18F exact 256-way children `90,154,218` inside parent residue `26 mod 64`;
- Stage32-18G completed exact 1024-way children `282,538,794` retained from the now-retired/cancelled deep-rescue run;
- Stage32-18K exact logical `26/1024`, itself synthesized from the complete coordinate-45 partition, with the slow secondary5 independently reproduced by Stage32-18J.

The arithmetic partitions are checked exactly:

`{r<256 : r mod 64 = 26} = {26,90,154,218}`

`{r<1024 : r mod 256 = 26} = {26,282,538,794}`.

The final aggregate must match the hostile-audited b10 canonical predecessor set byte-for-byte for norm `<=10`, then pass independent full-Aut order-1536 verification.

Execution-work counters from nested rescues are not reconstructed as a hypothetical single-run global node/trial count.

All numerical/theorem/receiver/controller credit remains false until hostile audit. The workflow is dormant until an explicit run key is added after Stage32-18K succeeds.
