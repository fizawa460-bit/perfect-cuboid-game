# Stage33 MAIN batch handoff

status: ORDER4_ALL_ROWS_EXACT_DUAL_INTEGRALITY_BLOCKER
pr: #1485
branch: stage33-post1483-order4-pullback-two-row-extraction
merge: FORBIDDEN
heavy_compute: FORBIDDEN

MAIN-STATE remains V11. No mathematical state promotion occurred, so this handoff records only the new unresolved delta.

## Current exact delta

All required semantic order-4 BigK pullback rows `[2,4,9,10,20,35,39,47,49,67]` are now exact. Rows 20 and 67 were reconstructed from the v17 source lock through the retained 140-class marking and certified Stage33-09 marked64 bridge; the other eight rows replay against their existing exact authorities.

The weighted semantic numerator with coefficients
`[(2,1),(4,3),(9,3),(10,1),(20,2),(35,2),(39,2),(47,3),(49,3),(67,2)]`
is exact in both INDLIST64 and historical Magma Pic64 coordinates.

The next mandatory normalization fails exactly: `n4 * pmPic` is divisible by 2 but not by 4. Its nonzero residues modulo 4 occur at historical Picard coordinates `[3,4,10,12,55]`, all equal to 2. Therefore `z4=(n4*pmPic)/4` is not integral and no mixed-Smith order-4 class, proper-Br2 row, retained10 label, or 75D matrix column is promoted.

Certificate:
`stages/stage33/33-12/j2-order4-source-coordinate-v18.json`

Canonical SHA256:
`a0378a7d7191d537347435d11002faa3692f91781dd15f53fe3063443e9d50d1`

Network-free replay:
`stages/stage33/33-12/verify_j2_order4_source_coordinate_blocker_v18.py`

## Anti-repeat boundary

Do not reacquire or re-extract any of the ten rows. Do not reopen qPic, Smith, sign census, S3 enumeration, row39 transport, target-compatibility selection, or historical mask6. Under the locked raw pullback formula these inputs deterministically reproduce the same divisibility obstruction.

## Next exact action

Source-lock the missing normalization/correction for pulling the semantic Kc `t1/4` generator into the full-surface dual Picard lattice, or prove from an exact source that the current raw numerator formula must be replaced. The replacement must replay all ten exact rows, preserve doubling to locked semantic `u1`, and make the full-surface pairing numerator divisible by 4 before any source label is materialized.
