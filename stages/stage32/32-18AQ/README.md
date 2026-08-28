# Stage32-18AQ — p436/s5 cut39 full block production

18AO measured an exact cut39 frontier of 4,103 states. 18AP replayed up to 64 of those lower subtrees and produced a strong structural signal. 18AQ is the first production confirmation: every cut39 frontier state must be replayed through the ordinary exact DFS.

Two independent deterministic executions are required. A run is COMPLETE only when upper traversal finishes without a resource exit and `replay_started == replay_completed == frontier_states == 4103`. The two executions must agree on exact survivor count and core traversal counters before p436/s5 receives numerical completion credit.

This is not a finer x1024 split and does not change coordinates 48..62. The immutable Stage32 exact source artifact and 18AF symmetry schedule remain source locked. MITM is not claimed; this is resumable/block execution of the same exact search tree.

Firewalls: only the single-wall numerical completion flag may become true after both exact confirmations. Global b16 aggregation, full d16 row, theorem, receiver, and controller credits remain false.
