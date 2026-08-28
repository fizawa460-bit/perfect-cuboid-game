# Stage32-18AO — b16 block-frontier architecture scout

This is a separate architectural scout on the single frozen wall `p436/s5`. It does not modify or consume Stage32-18AN results.

Purpose: measure whether the exact DFS can be cut below the x1024 ownership boundary into a manageable set of independently resumable lower-coordinate blocks. This is the first MITM/block-enumeration redirection after repeated local-pruning and basis-change failures.

Three lower cuts are profiled in parallel: 39, 31, 23. Coordinates 48..62 and the existing x1024 shard identity are untouched. For each cut, the normal exact cap and 256 symmetry-breaker pruning is run through the upper coordinates and traversal stops exactly when the remaining coordinate index reaches the selected cut. Every surviving upper assignment is one exact frontier state for a future lower-block certifier.

The scout records frontier width, traversal nodes, and a conservative serialized-state storage estimate. A cut is `PROMISING_FRONTIER` only if the complete upper traversal reaches the cut within the scout node cap and its estimated frontier storage is <= 500 MB. Resource exits are evidence about frontier width only; they are not numerical completion and cannot close any b16 wall.

This is not yet a full meet-in-the-middle join. Its job is to determine whether exact resumable/block certification has a tractable frontier before implementing the lower-half join/enumerator.

Firewalls: no finer shard split, no b16 numerical credit, no global aggregation credit, no theorem/receiver/controller credit.
