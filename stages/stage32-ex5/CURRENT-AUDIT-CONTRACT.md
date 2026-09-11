# Stage32EX5 current hostile-audit contract

This is the mutable current audit contract. Historical audit contracts remain provenance. PR #1776 remains open/draft/unmerged. BC2-27 hostile re-audit **PASS** is exact head `b70bc51909f5ed78641ee3b727a2258382ef950c`, review `5179488973`.

## BC2-28 retained candidate boundary

BC2-28 boundary38 executed exactly once at head `47c522ae4ee93e6fff19339048f982f48f932bab`, workflow run `34609454583`, authorize job `103295985357`, integrity job `103295985700`, compute job `103296259426`, artifact `10268117064`. Artifact digest is `d23645cca6e4bcf011ae1b0626934feaa2dafebf2563c2ced3d6c804cd89931c`; artifact raw JSON sha256 is `768c4209d2162cd85a2c93a3bfcb3a71e8ea9a600e62b1323b8f7b372139f843`; raw canonical is `f77cad8d03035514e43e992ccdee25c1d4f6a386789fac33e488e198c35a998d`; retained checkpoint canonical is `52138e7c417d69814d5007479420b56fcc27031679bf88f432916e6c89c77ec4`.

The bounded result checked all 42 p38 leaves: 38 UNSAT / 4 UNKNOWN / 0 SAT. New parent UNSAT set is `[1000,1003,1014,1198,1243]`; retained UNKNOWN parents are `[1048,1050,1064,1103]`; known parent-UNSAT lower bound is `7160`; the other `172` BC2-19 UNKNOWN identities remain uninferred. This retained result is **not hostile-audited yet** and grants no Stage32 MAIN/N350/FULL178/theorem/effectivity/receiver/endpoint/Perfect Cuboid or merge credit.

The authoritative raw provenance is the exact workflow/artifact receipt plus artifact ZIP digest, raw JSON sha256 and raw canonical recorded in the retained checkpoint/runkey. The malformed repository raw mirror was removed and is explicitly non-authoritative; no mathematical credit depends on it. The generation-1 runkey is consumed/disarmed. The temporary executor and the duplicate BC2-28 heavy execution path in `stage32-ex5-main.yml` are removed; the active integrity workflow only replays the retained BC2-28 verifier and cannot rerun BC2-28 computation.

BC2-29 is blocked until a later `stage32ex5-audit` PASS on this exact retained boundary. Merge authorization remains false and independent.
