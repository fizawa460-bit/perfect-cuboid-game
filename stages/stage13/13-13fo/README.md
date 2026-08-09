# Stage13-13fo — immutable R06 review bundle

This stage freezes the merged `13-13fn` R06 canonical proof into a byte-for-byte self-contained HTML review target.

```text
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R06
SOURCE_SNAPSHOT_COMMIT=103dbc9bf241f8c306befc8dab0175e3ca4fb0f2
R06_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R05_VERDICTS_CARRY_FORWARD_TO_R06=false
PROMOTE_TO_13_13G=false
NEXT=13-13fp
```

The builder reads all embedded sources from the fixed source snapshot with `git show`. The generated HTML, manifest, and result are committed by the dedicated PR workflow after hash validation.
