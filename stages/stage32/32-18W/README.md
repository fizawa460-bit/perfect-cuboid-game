# Stage32-18W — post-b14 b16 descendant-work profile

Stage32-18R has hostile-audited the exact bounded d16 b14 census. This leaf does **not** launch b16 production and does not enumerate b16 leaves. It reuses the already calibrated Stage32-18N descendant-work profiler to measure the next wall before choosing a packet geometry.

Accepted predecessor lock:

- b14 canonical survivors including zero: `44,450`;
- b14 canonical dump SHA256: `4d4680a87fab0c01ac8b54bcf404eecaa707cf5db782b31d5fa7357a52249d8a`;
- Aut group order: `1536`;
- breaker count: `256`;
- parent split coordinate/modulus: `54 / 1024`.

The Stage32-18N calibration already established that raw coordinate-54 population is a poor runtime proxy and that descendant work at probe coordinates 50 and 48 detects the known historical pathology. Therefore 18W tests only the two useful depths:

- `b16-p50`, node cap `160,000,000`;
- `b16-p48`, node cap `320,000,000`.

Both jobs stop at their probe coordinate, before canonical leaves. They record per-`h54 mod 1024` descendant nodes, trials, exact constraint/symmetry prunes and surviving probe prefixes, plus mod-256/mod-64 folded views. At most two heavy jobs run concurrently.

If p50 completes it is the preferred cheap production-design signal. p48 is retained as a safety-side strengthening when it also completes. A resource wall is evidence only for redesign; it is not evidence about existence/nonexistence or the b16 census.

Credit firewall:

```text
D16_B16_NUMERICAL_CREDIT=false
FULL_BOUND_TRAVERSAL_COMPLETE=false
FULL_D16_G0_ROW_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
CONTROLLER_MODIFIED=false
```
