# Stage33 MAIN batch handoff

status: RECOVERED_UNPROMOTED_DELTA_AFTER_ABORTED_BATCH
branch: stage33-post1485-v20-audit-pass-two-bit-source-lock
merge: FORBIDDEN
heavy_compute: FORBIDDEN
authority: TRANSIENT_OPERATIONAL_RECOVERY_ONLY_NOT_PROOF

The previous MAIN interaction advanced beyond the current promoted `MAIN-STATE.json` but ended before proof compaction / replay / state writeback / push. This note exists solely to prevent the next batch from restarting the same origin search.

## Recovered unpromoted narrowing

- A source-first derivation had reached retained10 mask `6` for the named source candidate. This is **not promoted authority** and MUST NOT be treated as source-locked merely because it is written here.
- The subsequent source -> target check had narrowed the mismatch to H1 coordinate `41`: the source-reachable 13D side gave `0` there while the locked target gave `1`.
- The raw ct Pic/2 side of that discrepancy had been narrowed to support indices `[9,11,19]`.
- Work stopped before the corresponding proof was compacted, replayed, committed, or pushed.

## Anti-repeat guard

- DO NOT restart historical origin discovery, broad repo/history search, rows 20/67 acquisition, qPic/Smith/sign/S3 reconstruction, correction/half-lift enumeration, or the four-mask two-bit enumeration.
- DO NOT infer named J2 = mask 6 from symmetry, this handoff, or remembered chat state.
- DO NOT discard the H1 `41` / raw ct `[9,11,19]` narrowing and start again from the v20 two-bit plane.

## Next exact action

Reconstruct only the smallest exact certificate/replay needed to validate or reject the recovered source-first mask-6 derivation and the H1-coordinate-41 / raw-ct-[9,11,19] blocker from the current locked leaf inputs. If validated, materialize the result, update detailed state, sync `MAIN-STATE.json`, then reset this handoff under the mandatory reset law. If any recovered detail fails exact replay, replace this note with the corrected narrow blocker; do not broaden into an origin/history search.
