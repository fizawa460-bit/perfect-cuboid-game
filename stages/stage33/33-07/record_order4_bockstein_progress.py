#!/usr/bin/env python3
"""Record the exact #1419 order-four Bockstein progress in handoff/result."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
HANDOFF = HERE / "handoff.json"
RESULT = HERE / "result.md"
NORMAL = HERE / "order2-raw-extension-normal-form.json"
COMPACT = HERE / "order2-quotient-raw-order4-bockstein-compact.json"

n = json.loads(NORMAL.read_text(encoding="utf-8"))
c = json.loads(COMPACT.read_text(encoding="utf-8"))
h = json.loads(HANDOFF.read_text(encoding="utf-8"))

h["schema"] = "STAGE33_07_REAUDIT_BLOCKED_HANDOFF_V9_MIXED_ORDER_GLOBAL_GERSTEN_GAP"
h["smallest_current_exact_kernel"] = n["new_smallest_exact_kernel"]
h["retained_exact_prefix"]["mixed_order2_order4_boundary_first_residue_models_exact"] = True
h["retained_exact_prefix"]["quotient_to_raw_bockstein_extension_normal_form_exact"] = True
h["repair_exact_reduction"].update({
    "raw_order2_first_residue_functions_materialized": 17,
    "raw_order4_first_residue_functions_materialized": 9,
    "all_26_boundary_first_residue_models_materialized_mixed_order": True,
    "all_26_boundary_first_residue_models_are_order2_squareclasses": False,
    "quotient_to_raw_double_obstruction_rank_f2": 9,
    "quotient_to_raw_extension_exact_group": "(Z/4)^9 direct_sum (Z/2)^52",
    "quotient_to_raw_extension_group_order_log2": 70,
    "quotient_to_raw_bockstein_normal_form_closed": True,
    "global_geometric_Gersten_lifts_materialized": 0,
    "global_geometric_Gersten_lifts_required": 26,
})
h["order4_bockstein_evidence"] = {
    "producer": "certify_order2_quotient_raw_order4_bockstein.py",
    "compact_producer": "compact_order2_quotient_raw_order4_bockstein.py",
    "normal_form_producer": "certify_order2_raw_extension_normal_form.py",
    "full_certificate_sha256": c["full_certificate_sha256"],
    "compact_certificate_sha256": c["canonical_sha256"],
    "normal_form_certificate_sha256": n["canonical_sha256"],
    "raw_extension_exact_group": n["raw_extension_invariant_factors"]["exact_group"],
    "raw_order2_directions": 17,
    "raw_order4_directions": 9,
    "bockstein_image_rank_f2": 9,
    "complex_conjugation_on_nine_z4_factors": "inversion",
    "actions_validation": "PASS",
}
h["order2_localization_missing_exact_inputs"].update({
    "nine_quotient_order2_sources_lifted_to_raw_order2_residues": False,
    "nine_quotient_order2_sources_materialized_as_raw_order4_first_residue_functions": True,
    "quotient_to_raw_bockstein_extension_normal_form_closed": True,
    "global_geometric_Gersten_lifts_for_17_order2_sources": False,
    "global_geometric_Gersten_lifts_for_9_order4_sources": False,
    "global_geometric_Gersten_lifts_for_all_26_sources": False,
    "cc_action_on_chosen_global_geometric_lifts": False,
    "ct_action_on_chosen_global_geometric_lifts": False,
    "global_lift_differences_in_proper_br2_coordinates": False,
})
h["next_item"] = n["next_exact_leaf"]
h["stage33_progress"] = "6/11"
h["stage33_08_released"] = False
h["theorem_credit"] = False
h["endpoint_credit"] = False
HANDOFF.write_text(json.dumps(h, indent=2, sort_keys=True) + "\n", encoding="utf-8")

section = f"""

## PR #1419 raw-order4 Bockstein normal form

The nine quotient-order-two directions that failed the raw order-two test in
PR #1414 have now been retained at their correct raw order four rather than
being forced into Kummer squareclasses. Exact mod-4 divisor checks on all 72
boundary P1 components produce deterministic order-four first-residue function
models for all nine directions. Together with the 17 retained raw-order-two
models, all 26 boundary first-residue directions are therefore materialized in
mixed order `17 x order2 + 9 x order4` form.

The nine nonzero doubles are independent in the 44-dimensional U44 kernel.
Taking those doubles as the first nine vectors of a new U44 basis gives the
exact raw extension normal form

```text
RAW_EXTENSION_GROUP=(Z/4)^9 direct_sum (Z/2)^52
RAW_EXTENSION_ORDER=2^70
RAW_ORDER2_FIRST_RESIDUE_DIRECTIONS=17
RAW_ORDER4_FIRST_RESIDUE_DIRECTIONS=9
BOCKSTEIN_IMAGE_RANK_F2=9
COMPLEX_CONJUGATION_ON_EACH_ORDER4_FACTOR=inversion
FULL_ORDER4_BOCKSTEIN_CERTIFICATE_SHA256={c['full_certificate_sha256']}
COMPACT_ORDER4_BOCKSTEIN_CERTIFICATE_SHA256={c['canonical_sha256']}
RAW_EXTENSION_NORMAL_FORM_CERTIFICATE_SHA256={n['canonical_sha256']}
QUOTIENT_TO_RAW_BOCKSTEIN_NORMAL_FORM_CLOSED=true
GLOBAL_GEOMETRIC_GERSTEN_LIFTS_MATERIALIZED=0/26
PROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false
ABSOLUTE_DELTA_LOC_COMPUTED=false
ARITHMETIC_HS_CLOSED=false
STAGE33_PROGRESS_EFFECTIVE=6/11
STAGE33_08_RELEASED=false
```

This closes the finite quotient-to-raw Bockstein structure itself. It does not
close the global residue-lift problem: the 17 order-two boundary packages and
the 9 order-four boundary packages all still need genuine global geometric
Gersten lifts before their Galois differences can be computed. The corrected
smallest exact kernel is therefore

```text
{n['new_smallest_exact_kernel']}
```

No finite boundary calculation is promoted to a global Q-defined lift here.
"""

text = RESULT.read_text(encoding="utf-8")
marker = "## PR #1419 raw-order4 Bockstein normal form"
if marker in text:
    text = text[:text.index(marker)].rstrip() + section
else:
    text = text.rstrip() + section
RESULT.write_text(text.rstrip() + "\n", encoding="utf-8")

print(json.dumps({
    "success": True,
    "smallest_current_exact_kernel": h["smallest_current_exact_kernel"],
    "next_item": h["next_item"],
    "global_geometric_Gersten_lifts": "0/26",
    "stage33_progress": h["stage33_progress"],
}, indent=2, sort_keys=True))
