# Stage32-18R — rescue-aware exact global b14 integration

This stage is the final exact integration receiver for the current b14 production design. It does not enumerate new search space.

The old Stage32-18P production run `32915934318` remains an immutable exact source, but the final handoff is no longer hard-coded as `41 + 210`. Stage32-18T now builds a **union snapshot** from that source plus only previously successful, independently COMPLETE-certified resume units. Any still-missing units are computed in the current 18T run. 18R accepts the handoff only if the final V2 summary proves the complete source complement with no missing or extra packet IDs.

The union handoff preserves three packet-level provenances:

- `18P_frozen_snapshot`: exact COMPLETE packet artifact taken directly from the immutable Stage32-18P source run;
- `18T_prior_success_carryover`: an earlier successful Stage32-18T packet embedded byte-for-byte in the union snapshot;
- `18T_union_resume_current`: a packet completed by the final union-resume run itself.

The counts are derived from the signed-off snapshot rather than assumed in advance. Required invariants are `legacy + resume_complement = 251` and `carryover + current_resume = resume_complement`.

Fixed non-bulk inputs remain:

- Stage32-18P prepared artifact `9588229672`, ZIP SHA256 `6e4e6e5350717296f0e76e5c972e945b72a61d32e039718a535e245826b5b159`;
- Stage32-18O exact pilot packets `63,64,173` reused without recomputation;
- hostile-audited Stage32-18S logical hot parent 26: artifact `9591499652`, ZIP SHA256 `d337a178ae3b156236903aca46f12e5ad8c04348519212526b98a67b5885fd37`;
- hostile-audited Stage32-18S logical hot parent 748: artifact `9591500024`, ZIP SHA256 `c120a9c14ba8575de1df86dc02f928bfa049aa6d344ff5b969182708aaea2d4a`;
- hostile-audited Stage32-18L b12 aggregate artifact `9585370018` as predecessor lock.

The final 18T run must publish `stage32-18t-b14-source-snapshot-g2` with schema `STAGE32_18T_B14_RESUME_UNION_SNAPSHOT_V2` and `stage32-18t-b14-resume-summary-g2` with schema `STAGE32_18T_B14_OPTIMIZED_RESUME_SUMMARY_V2`, with `ready_for_18r=true`.

The aggregator requires all 256 logical packet slots and all 1024 `h54 mod 1024` residues exactly once, identical immutable source locks, no duplicate canonical records, exact equality of the complete `norm <= 12` record set with the hostile-audited b12 census, and an independent full order-1536 Aut verification.

Nested-rescue and packet execution counters are not summed into a hypothetical single-run global telemetry total because each execution repeats work above its split coordinate.

## Heavy-run safety

18R is intentionally dormant: the run-key file is absent. The workflow listens only for a `pull_request:synchronize` event that changes the run-key path. Even then, validation requires:

1. that commit range changes **only** `stages/stage32/runkeys/18r-b14-rescue-aware-global-integration.json`;
2. the exact commit subject `Stage32-18R: ARM FINAL B14 INTEGRATION`;
3. an armed generation-1 key containing the final 18T run ID, union-snapshot artifact ID/digest, and the fixed audited source IDs/digests;
4. `handoff_policy=UNION_SNAPSHOT_V2_EXACT_COMPLEMENT`.

Ordinary documentation edits, merges, PR synchronization, reopen/open events, and unrelated branch updates cannot authorize the heavy integration. The final ARM commit must be made only after Stage32-18T has completed and its V2 summary says `ready_for_18r=true`.

No b14 numerical credit is granted by this branch before final hostile audit. `D16_B14_NUMERICAL_CREDIT=false`, `THEOREM_CREDIT=false`, and `RECEIVER_CREDIT=false` remain mandatory.
