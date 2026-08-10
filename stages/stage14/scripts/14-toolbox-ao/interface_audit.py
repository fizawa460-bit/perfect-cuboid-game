from pathlib import Path

root = Path(__file__).resolve().parents[4]
interface = (root / "docs/stage14-toolbox/collision-dispersion-interface.md").read_text()
result = (root / "stages/stage14/14-toolbox-ao/result.md").read_text()

required_interface = (
    "Common coefficient space",
    "diagonal-subtraction dictionary",
    "DualSplitKCenteredDispersion",
    "principal squareclass coherence",
    "signed common-refinement aggregation",
    "shared U/V",
    "divisor hyperbola",
    "physical selectors",
    "does not block toolbox main",
)
assert all(token in interface for token in required_interface)

required_result = (
    "STAGE14_TOOLBOX_AO=COMPLETE",
    "EXACT_STATE_DIAGONAL_DISTINCT_FROM_RESIDUE_DIAGONAL=true",
    "RESIDUE_DIAGONAL_DISTINCT_FROM_PRINCIPAL_SQUARECLASS_COHERENCE=true",
    "ANGULAR_COMPLETION_BEFORE_PAIR_COLLAPSE=true",
    "CENTERED_XI_K_DISPERSION_PROVED=false",
    "GLOBAL_PRINCIPAL_KUMMER_INCIDENCE_PROVED=false",
    "NONPRINCIPAL_SELECTOR_DISPERSION_PROVED=false",
    "TOOLBOX_H_REQUIRED_FOR_TOOLBOX_MAIN=false",
    "TOOLBOX_MAIN_BLOCKED_BY_H=false",
    "NEXT=Stage14-toolbox-ap",
)
assert all(token in result for token in required_result)

# Guard against accidental theorem promotion.
assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8" in result
assert "NEW_WHOLE_FAMILY_POWER_SAVING_OWNED_BY_TOOLBOX_AO=false" in result
assert "TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false" in result

print("Stage14-toolbox-ao interface audit: OK")
