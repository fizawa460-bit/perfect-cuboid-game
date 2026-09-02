#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE_PATH = ROOT / "stages/stage33/33-12/j2-ct-actual-integral-lattice-source-gate-v26.json"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


gate = load_json(GATE_PATH)
require(gate["schema"] == "stage33-j2-ct-actual-integral-lattice-source-gate-v26", "schema drift")
require(gate["version"] == 26, "version drift")
require(gate["status"] == "BLOCKED_ON_ACTUAL_CT_INTEGRAL_LATTICE_SOURCE", "blocker status drift")

expected_authority = {
    "beta1": [1, 0],
    "source": "mask6",
    "a": 0,
    "b": 1,
    "target_support": [2, 5],
    "lift": "lambda_D",
}
require(gate["authority"] == expected_authority, "named J2 authority drift")

expected_sources = {
    "adapter_v25": "stages/stage33/33-12/j2-genuine-h2-mu2-kummer-adapter-v25.json",
    "explicit_cech_lift": "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
    "norm_splitting": "stages/stage33/33-12/j2-corrected-ct-norm-splitting-module.json",
    "zero_defect_contract": "stages/stage33/33-12/j2-full-surface-mu2-zero-defect-contract.json",
}
require(gate["source_lock"] == expected_sources, "source-lock path drift")
loaded_sources = {name: load_json(ROOT / rel) for name, rel in expected_sources.items()}

# These are source-presence guards, not a promotion of the current Pic/2 value.
adapter_text = json.dumps(loaded_sources["adapter_v25"], sort_keys=True)
lift_text = json.dumps(loaded_sources["explicit_cech_lift"], sort_keys=True)
require("lambda_D" in adapter_text, "V25 adapter no longer names lambda_D")
require("lambda_D" in lift_text, "explicit Cech source no longer names lambda_D")

amb = gate["integral_extension_ambiguity"]
require(amb["E0"] == {
    "bundle": "O + O(-2,0)",
    "determinant_pic_mod_2_candidate": 0,
    "selected_as_actual": False,
}, "E0 candidate drift")
require(amb["E1"] == {
    "bundle": "O + O(-3,0)",
    "elementary_transform": True,
    "determinant_pic_mod_2_candidate": 1,
    "selected_as_actual": False,
}, "E1 candidate drift")
require(amb["selected"] is None, "an integral extension was selected without actual C_t lattice evidence")
require(amb["generic_norm_splitting_distinguishes"] is False, "generic norm splitting was incorrectly promoted to an integral selector")

expected_evidence = [
    "actual C_t fpqc/Cech patch cover grounded in lambda_D/AALR",
    "explicit local integral rank-2 basis on every patch",
    "explicit 2x2 overlap transition matrices",
    "triple-overlap cocycle verification",
    "determinant transition line-bundle class in Pic(S)/2",
    "explicit E0-versus-E1 integral selector",
]
require(gate["required_actual_evidence"] == expected_evidence, "actual-evidence checklist drift")

for name, value in gate["forbidden_inferences"].items():
    require(value is False, f"forbidden inference re-enabled: {name}")

require(gate["downstream"] == {
    "pic_mod_2_defect_materialized": False,
    "hs_d2_materialized": False,
    "v4_connecting_cocycle_materialized": False,
    "stage33_progress": "6/11",
    "standard_kummer_columns": "0/10",
}, "downstream firewall drift")

for name, value in gate["promotion_gate"].items():
    require(value is False, f"promotion gate opened prematurely: {name}")

print("STAGE33_J2_CT_ACTUAL_INTEGRAL_LATTICE_SOURCE_GATE_V26_PASS")
print("BLOCKED_ON_ACTUAL_CT_INTEGRAL_LATTICE_SOURCE")
print("PROOF_REPLAY_COMPLETE")
