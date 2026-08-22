# Stage16-28 Stage70 promotion materialization gate

Status: candidate operational repair discovered during Stage21-70 closeout.

A Stage70 declaration is an obligation, not a classification-only marker.

If `SELF_CONTAINED_BUNDLE_REQUIRED=YES`, the bundle must physically exist before final Stage70 PASS. If `ARSENAL_PROMOTION_REQUIRED=YES`, every declared candidate must be materialized as a portable repository contract before final Stage70 PASS. `YES` plus candidate names is not completion.

Required closeout markers:

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES|NO
SELF_CONTAINED_BUNDLE_PRESENT=true|false|NOT_REQUIRED
SELF_CONTAINED_BUNDLE_PATH=
ARSENAL_PROMOTION_REQUIRED=YES|NO
ARSENAL_PROMOTION_PRESENT=true|false|NOT_REQUIRED
ARSENAL_PROMOTION_PATHS=
ARSENAL_PROMOTION_IDS=
MANIFEST_PRESENT=true|false
```

The controller must not permit parent-stage advancement while a required artifact is missing. Preferred ordering is Stage70 main-batch materialization followed by one audit of the complete closeout surface.

Earlier closed Stage16-20 stages should be scanned separately for `ARSENAL_PROMOTION_REQUIRED=YES` without a materialized artifact. Such cases are promotion debt and do not invalidate already-audited mathematics.
