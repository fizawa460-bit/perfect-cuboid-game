# Stage33 MAIN batch handoff

status: ORDER4_NAMED_COLUMN_QUOTIENT_EXACT_TWO_BITS_MISSING
pr: #1485
branch: stage33-post1483-order4-pullback-two-row-extraction
merge: FORBIDDEN
heavy_compute: FORBIDDEN

MAIN-STATE remains V11. No mathematical state promotion occurred, so this handoff records only the new unresolved delta.

## Current exact delta

The v18 all-row numerator and v19 correction torsor are source-locked. For the named 75D matrix column, the v19 14-bit correction selector is more information than is required.

The 16384 corrections induce 16 proper14 functionals, with exactly 1024 corrections per functional. After imposing the already locked cc/ct fixed condition, the named-column-relevant quotient is the exact affine plane
`(a,b,1,0,0,0,0,0,0,0)` in retained10 coordinates. It contains masks `[4,5,6,7]` and therefore has dimension 2, not 14.

The actual S3 action has exact orbits `[6]` and `[4,5,7]`. Mask 6 remains only the unique joint-fixed candidate: it is not the named J2 source unless order-4 joint fixedness is independently source-locked. No candidate is selected.

Certificate:
`stages/stage33/33-12/j2-order4-named-functional-quotient-v20.json`

Canonical SHA256:
`1b53db254c381721c0c648bab41c276ec79f69f6e1f81235993936df3e25232e`

Network-free replay:
`stages/stage33/33-12/verify_j2_order4_named_functional_quotient_v20.py`

## Anti-repeat boundary

Do not reacquire any row or rerun the correction/half-lift enumeration. Do not reopen qPic, Smith, sign census, S3 enumeration, target compatibility, historical mask6, or rep88. For the named matrix column, the ten-bit correction fiber is proved invisible and must not be reopened.

## Next exact action

Source-lock the two-bit quotient value `(a,b)`, equivalently the actual swap12/swap13 behavior of the named semantic Kc `t1/4` lift on the four-element affine plane. A source proof that the named order-4 lift is fixed by both swaps forces mask 6; otherwise labeled nonfixed swap images identify one of masks 4,5,7. Only this source-first datum permits the named 75D relation/column step.
