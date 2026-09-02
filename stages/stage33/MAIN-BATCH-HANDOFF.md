# Stage33 MAIN batch handoff

status: ORDER4_CORRECTION_TORSOR_EXACT_NAMED_SELECTOR_MISSING
pr: #1485
branch: stage33-post1483-order4-pullback-two-row-extraction
merge: FORBIDDEN
heavy_compute: FORBIDDEN

MAIN-STATE remains V11. No mathematical state promotion occurred, so this handoff records only the new unresolved delta.

## Current exact delta

The v18 all-row numerator is source-locked. Its integrality defect is now solved exactly rather than treated as an unspecified normalization failure.

For a correction `r in Pic(S)/2`, the required condition is
`(n4+2r)G_S = 0 mod 4`, equivalently `rG_S=(n4G_S/2) mod 2`.
The exact system has rank 50, affine dimension 14, and exactly 16384 solutions.

These corrections give 16384 distinct integral mixed-Smith order-4 half-lifts, all doubling to locked semantic `u1`. They induce exactly 16 proper14 functionals, 1024 corrections per functional. The joint cc/ct-fixed functionals are exactly the already locked retained10 masks `[4,5,6,7]`; no candidate is selected.

Certificate:
`stages/stage33/33-12/j2-order4-integral-correction-torsor-v19.json`

Canonical SHA256:
`3ee11e0ecdc855083a4260c2ae4f24ef4c160a7e26a48fd3872369d117118576`

Network-free replay:
`stages/stage33/33-12/verify_j2_order4_integral_correction_torsor_v19.py`

## Anti-repeat boundary

Do not reacquire any row or rerun the correction/half-lift enumeration. Do not reopen qPic, Smith, sign census, S3 enumeration, target compatibility, historical mask6, or rep88. The exact ambiguity is now the named selector inside the locked 14D correction torsor.

## Next exact action

Source-lock one 14-bit correction selector, equivalently the labeled image of semantic Kc `t1/4` in the actual index-512 glue `T(S)/L0` or an equivalent marked NS-T anti-isometry. Only that source-first datum may choose among retained masks `[4,5,6,7]` and permit the named 75D relation/column step.
