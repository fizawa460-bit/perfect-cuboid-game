# Stage32-18M — post-b12 next bounded production design

Accepted predecessor: hostile-audited exact d16 b12 census from PR #1397 / controller V20.

This leaf does **not** enumerate a new full bound and grants no new numerical credit. It profiles exact symmetry-pruned DFS frontiers before leaf enumeration so that the next production wall and partition geometry are selected from measured resource evidence rather than extrapolated from b12 counts.

Profiles are exact prefix enumerations under the source-locked 256-breaker certifier. Floating arithmetic only schedules exact rational Cauchy–Schwarz prune checks; it cannot reject a branch. At the selected frontier coordinate the profiler hashes every surviving prefix into all 1024 residues in one traversal and stops, so no canonical leaf census is inferred.

The profile set is:

- b12 / coordinate 54: historical anchor; residue 26/1024 was the known b12 runtime outlier and must be checked against the proxy ranking.
- b14 / coordinates 54, 50, 46: candidate partition-depth tradeoff.
- b16 / coordinate 54: shallow growth comparator only; it does not authorize skipping b14.

If the historical b12 hot residue is not ranked as heavy by frontier population, raw frontier counts are declared an insufficient load proxy and the next main leaf must use a depth-aware descendant-work profile before b14 production. If the proxy is informative, b14 is the immediate next norm wall and the measured split-depth distribution is used to choose a resource-safe exact production layout.

Firewalls:

```text
D16_B12_NUMERICAL_CREDIT=true   # inherited audited predecessor only
D16_B14_NUMERICAL_CREDIT=false
D16_B16_NUMERICAL_CREDIT=false
FRONTIER_PROFILE_ONLY=true
FULL_BOUND_TRAVERSAL_COMPLETE=false
FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED=false
SNAPSHOT_FAST_GLOBAL_COMPLETENESS_CERTIFIED=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```

The workflow also uses a commit-range run-key gate: on PR synchronize events, heavy/profile jobs run only when the run-key file changed between the previous and current PR heads. This repairs the operational weakness discovered by the Stage32-18L audit where a path filter alone could retrigger after unrelated audit/bookkeeping commits.
