# Stage32-18C b10 exact aggregate recovery

This companion recovery branch exists only because the original Stage32-18C aggregate intentionally required equality with the now-falsified floating fast preview. All 16 exact b10 shards from run `32820893492` completed successfully and are reused byte-for-byte; no exact shard is recomputed here.

The recovery aggregate:

- downloads the 16 immutable exact shard artifacts from run `32820893492`;
- checks source locks, shard coverage, disjoint canonical records, and traversal-completeness flags;
- enforces the hostile-audited b8 predecessor histogram `{0:1,2:1,4:7,6:28,8:223}`;
- constructs the authoritative exact b10 aggregate independently of the broken baseline fast set;
- independently verifies the aggregate under full Aut order 1536;
- compares the exact set against scout2's snapshot-restored fast candidate from run `32830210774` only as a cross-check, not as the source of numerical credit.

Firewall remains:

```text
AUDIT_STATUS=PENDING
FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED=false
SNAPSHOT_FAST_GLOBAL_COMPLETENESS_CERTIFIED=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```

No Stage32-18C heavy traversal source or controller is modified by this companion PR.
