# Stage13-13fo — R06 review manifest

```text
STAGE13_13FO=COMPLETE_R06_REVIEW_BUNDLE
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R06
SOURCE_SNAPSHOT_COMMIT=103dbc9bf241f8c306befc8dab0175e3ca4fb0f2
CONTENT_SHA256=ff75730393f8d9895ab85c44313d7bc1b3439697948754e6dc5030c5614bb0c8
BUNDLE_PATH=review/STAGE13-FINAL-SELF-CONTAINED-20260809-R06.html
R06_IMMUTABLE=true
R05_IMMUTABLE=true
R06_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R05_VERDICTS_CARRY_FORWARD_TO_R06=false
R06_INDEPENDENT_CLOSED_VERDICTS=0
R06_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2
R06_RECORDED_THEOREM_LEVEL_OBJECTIONS=0
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
PROMOTE_TO_13_13G=false
NEXT=13-13fp
```

## Review target

The byte-for-byte review target is `review/STAGE13-FINAL-SELF-CONTAINED-20260809-R06.html` with SHA-256 `ff75730393f8d9895ab85c44313d7bc1b3439697948754e6dc5030c5614bb0c8`.
Every embedded source is read from the fixed merged R06 synthesis snapshot `103dbc9bf241f8c306befc8dab0175e3ca4fb0f2`.
R06 is never edited in place; any substantive repair creates R07 or later.

## Included fixed-snapshot sources

- `stages/stage13/13-13fn/stage13-r06-canonical-proof.md` — SHA-256 `fd60e84375ded9cdf0beece24302b417f71208798d0c466da1440ad368139776`
- `stages/stage13/13-13fb/wiener-bound-lemma.md` — SHA-256 `a3df9ee183a1cc70da489c232a710fdf2b0f8be2c91037093c53acec5b943d1f`
- `stages/stage13/13-13fl/gaussian-hecke-normalization.md` — SHA-256 `d7c6bd0768e5d121ef0f42f388bfb5d1737bdbb2a5e5c0631566eb6a1150dcd2`
- `stages/stage13/13-13fm/principal-pole-sector-closure.md` — SHA-256 `aecd3a7e963ab0ff8e9e98dada1abd97fe2a2355542b7b8739f9335a6cc6098e`
- `stages/stage13/13-13fj/r06-repair-plan.md` — SHA-256 `b18a55fad98189cbee1d03cc273494791ed6d999fa32337e08b26da9da1e4fe0`
- `stages/stage13/13-13fn/result.md` — SHA-256 `567d902d3905cddc0e7ef60c76a11c3b9d2af93caacec1726fdcd5f40b0a9c5f`

## Review policy

R06 begins from zero independent `CLOSED` verdicts. R05 verdicts are provenance only and do not count toward R06.
Final Stage13 freeze remains blocked until an immutable final bundle obtains at least two independent `CLOSED` verdicts and zero unresolved theorem-level objections.
