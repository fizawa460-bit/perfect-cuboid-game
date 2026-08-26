# Stage32-18R — rescue-aware exact global b14 integration

This stage is the final exact integration receiver for the current b14 production design. It does not enumerate new search space.

The old Stage32-18P production PR is retired and closed without merge. Its run `32915934318` contributes only the **41 packet artifacts frozen as exact COMPLETE** by the Stage32-18T source snapshot. The remaining **210 bulk packets** must come from the exact Stage32-18T optimized-resume run `32925549204`; 18R refuses to proceed unless the 18T resume summary proves that this complement is complete with no missing or extra packet IDs.

Inputs are fixed by run/artifact identity:

- Stage32-18T frozen source snapshot artifact `9591372421`, ZIP SHA256 `ac2a1e41a87b0fda41adb4eea11e8e3b05d819373138bda9c91435211cb4f895`, defining the 41/210 handoff partition;
- Stage32-18P prepared artifact `9588229672`, ZIP SHA256 `6e4e6e5350717296f0e76e5c972e945b72a61d32e039718a535e245826b5b159`;
- Stage32-18T packet artifacts for exactly the 210 snapshot-missing packet IDs, gated by `stage32-18t-b14-resume-summary-g1` with `ready_for_18r=true`;
- Stage32-18O exact pilot packets `63,64,173` reused without recomputation;
- hostile-audited Stage32-18S logical hot parent 26: artifact `9591499652`, ZIP SHA256 `d337a178ae3b156236903aca46f12e5ad8c04348519212526b98a67b5885fd37`;
- hostile-audited Stage32-18S logical hot parent 748: artifact `9591500024`, ZIP SHA256 `c120a9c14ba8575de1df86dc02f928bfa049aa6d344ff5b969182708aaea2d4a`;
- hostile-audited Stage32-18L b12 aggregate artifact `9585370018` as predecessor lock.

The aggregator requires all 256 logical packet slots and all 1024 `h54 mod 1024` residues exactly once, identical immutable source locks, no duplicate canonical records, exact equality of the complete `norm <= 12` record set with the hostile-audited b12 census, and an independent full order-1536 Aut verification.

Nested-rescue and packet execution counters are not summed into a hypothetical single-run global telemetry total because each execution repeats work above its split coordinate.

## Heavy-run safety

18R is intentionally dormant: the run-key file is absent. The workflow listens only for a `pull_request:synchronize` event that changes the run-key path. Even then, validation requires:

1. that commit range changes **only** `stages/stage32/runkeys/18r-b14-rescue-aware-global-integration.json`;
2. the exact commit subject `Stage32-18R: ARM FINAL B14 INTEGRATION`;
3. an armed generation-1 key containing all frozen run/artifact IDs and digests above.

Ordinary documentation edits, merges, PR synchronization, reopen/open events, and unrelated branch updates cannot authorize the heavy integration. The final ARM commit must be made only after Stage32-18T has completed and its summary says `ready_for_18r=true`.

No b14 numerical credit is granted by this branch before final hostile audit. `D16_B14_NUMERICAL_CREDIT=false`, `THEOREM_CREDIT=false`, and `RECEIVER_CREDIT=false` remain mandatory.
