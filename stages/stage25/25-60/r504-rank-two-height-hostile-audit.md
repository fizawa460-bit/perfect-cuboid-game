# Stage25-60 R504 rank-two height hostile audit

Status: **FAIL; SUPERSEDED BY NARROW REPAIR PASS**

ROUTE=R504
CHECKPOINT=60
PR=995

This historical audit record is preserved unchanged in substance: it rejected only the unsupported identification of the full physical coset with `a` odd, `b` even. The Rosati/height quadratic form and the conditional physical degree formulas were accepted.

The requested repair was subsequently supplied by the explicit full-2-torsion Kummer calculation in `r504-rank-two-mod2-repair.md` and accepted by `r504-rank-two-height-audit-recheck.md`.

Historical verdict:

```text
PREVIOUS_AUDIT_VERDICT=PASS
AUDIT_VERDICT=FAIL
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
R504_ROSATI_HEIGHT_FORM_ACCEPTED=true
R504_PHYSICAL_COSET_PARITY_ACCEPTED=false
R504_RANK_TWO_MOD2_SATURATION_CERTIFICATE=false
R504_MIN_NONDEGENERATE_NORM_5_ACCEPTED=false
R504_BEST_FIXED_CLASS_EXPONENT_1_12_ACCEPTED=false
R504_P_PLUS_2R_EXACT_FAMILY_GROWTH_RETAINED=Theta(B^(1/12))
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
```

Supersession:

```text
SUPERSEDED_BY=stages/stage25/25-60/r504-rank-two-height-audit-recheck.md
SUPERSEDING_AUDIT_VERDICT=PASS
```
