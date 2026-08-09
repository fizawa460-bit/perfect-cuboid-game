# Stage14-num-alpha11-diag11 — cumulative survival uncertainty and stopping decision

This stage takes the merged diag8 cumulative denominator panel through B=1,000,000 and adds finite-sample uncertainty bands to the conditional second-face survival profile.

Primary questions:

1. Is the cumulative `ab` second-face survival rate still distinguishable from `ac` and `bc` once finite-count uncertainty is included?
2. Is the visible B=100k -> 1m cumulative drift larger than expected under the common-survival finite-count calibration used after diag10?
3. Has the numerical diagnostic branch reached diminishing returns relative to the proof-side bridge tracks?

The calculation is a finite multinomial/plugin calibration only. It does not assert IID arithmetic objects and does not prove an asymptotic exactly-two direction law.

Final numerical values will be frozen after the dedicated CI replay.
