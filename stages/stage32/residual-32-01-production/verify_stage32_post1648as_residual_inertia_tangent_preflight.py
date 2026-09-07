#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648as-residual-inertia-tangent-preflight.json"
NOTE = HERE / "post1648as-residual-inertia-tangent-preflight-source-note.md"
DIAG = HERE / "diagnose_stage32_post1648as_residual_inertia_tangent_preflight.py"
AQ = HERE / "post1648aq-residual-g-cusp-multiplicity-grid.json"
AR = HERE / "post1648ar-two-factor-slack-minimal-branches.json"


def canonical_sha(obj: dict) -> str:
    y = dict(obj)
    y.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(y, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    expected = "3211e758e5b4ec4e96e91b8844a0de429f08fb031e1fd99ba01ac0f9ccea5907"
    assert cert["canonical_sha256_without_this_field"] == expected
    assert canonical_sha(cert) == expected

    locks = cert["source_locks"]
    assert hashlib.sha256(NOTE.read_bytes()).hexdigest() == locks["source_note_sha256"]
    assert git_blob_sha1(NOTE) == locks["source_note_blob_sha1"]
    assert git_blob_sha1(DIAG) == locks["diagnostic_script_blob_sha1"]

    aq = json.loads(AQ.read_text())
    ar = json.loads(AR.read_text())
    assert aq["canonical_sha256_without_this_field"] == cert["parent"]["aq_canonical"]
    assert ar["canonical_sha256_without_this_field"] == cert["parent"]["ar_canonical"]

    proc = subprocess.run([sys.executable, "-B", str(DIAG)], cwd=ROOT, check=True, capture_output=True, text=True)
    x = json.loads(proc.stdout)
    assert x["mode"] == "SCRATCH_POST1648AS_RESIDUAL_INERTIA_TANGENT_PREFLIGHT"
    assert x["residual_group"]["order"] == cert["residual_group"]["order"] == 8
    assert x["residual_group"]["nontrivial_element_count"] == cert["residual_group"]["nontrivial_element_count"] == 7

    inertia = x["node_stabilizers"]["inertia_rows"]
    assert len(inertia) == cert["residual_group"]["node_inertia_element_count"] == 3
    assert x["node_stabilizers"]["distinct_nontrivial_stabilizer_count"] == 3
    assert x["node_stabilizers"]["exceptional_orbit_count"] == cert["exceptional_orbits"]["count"] == 12
    assert x["node_stabilizers"]["exceptional_orbit_sizes"] == cert["exceptional_orbits"]["sizes"] == [4] * 12

    for got, want in zip(inertia, cert["node_inertia"]):
        for k in ("fingerprint", "C_dot_gC", "fixed_exceptional_count", "boundary_inertia_labels_1based", "target_cusp_mass_list", "target_cusp_mass_sum", "target_cusp_orbit_count"):
            assert got[k] == want[k]
    assert sum(r["C_dot_gC"] for r in inertia) == cert["residual_group"]["node_inertia_C_dot_gC_sum"] == 4144

    nonnode = x["node_stabilizers"]["non_node_element_rows"]
    assert len(nonnode) == cert["residual_group"]["non_node_element_count"] == 4
    for got, want in zip(nonnode, cert["non_node_elements"]):
        for k in ("fingerprint", "C_dot_gC", "fixed_exceptional_count", "fixed_nonboundary_normal_count"):
            assert got[k] == want[k]
    assert sum(r["C_dot_gC"] for r in nonnode) == cert["residual_group"]["non_node_C_dot_gC_sum"] == 5142
    assert 4144 + 5142 == cert["residual_group"]["total_nontrivial_C_dot_gC_sum"] == 9286

    local = x["local_source_model"]
    clocal = cert["local_tangent_action"]
    assert local["target_map"] == clocal["target_map"]
    assert local["node_stabilizer_action"] == clocal["node_inertia_action"]
    assert local["resolution_exceptional_coordinate_action"] == clocal["exceptional_coordinate_action"]
    assert local["exceptional_fixed_landings"] == clocal["fixed_landings"]
    assert local["FSM_minimal_landing"] == clocal["FSM_minimal_landing"]
    assert local["FSM_minimal_branch_fixed_by_node_stabilizer"] is False

    pressure = x["AR_minimal_branch_pressure"]
    cp = cert["minimal_branch_pressure"]
    assert pressure["minimum_FSM_minimal_branches"] == cp["minimum_FSM_minimal_branches"] == 186
    assert pressure["minimum_on_some_target_cusp_by_12_point_pigeonhole"] == cp["minimum_on_some_target_cusp_orbit"] == 16
    assert pressure["minimum_on_some_exceptional_curve_by_48_curve_pigeonhole"] == cp["minimum_on_some_exceptional_curve"] == 4
    assert pressure["retained_lambda_or_jet_constraints_available"] is False
    assert cp["opposite_landing_collision_forced"] is False

    assert cert["decision"]["v6_carrier_excluded"] is False
    assert cert["decision"]["Q602_excluded"] is False
    assert cert["decision"]["O210_excluded"] is False
    assert cert["decision"]["O212_plus_advance_allowed"] is False
    assert cert["guardrails"]["scratch_only"] is True
    assert cert["guardrails"]["shared_MAIN_STATE_unchanged"] is True
    assert cert["guardrails"]["shared_authority_unchanged"] is True

    print("PASS stage32 post1648AS residual inertia tangent preflight")
    print(json.dumps({
        "canonical": expected,
        "node_inertia_C_dot_gC": [r["C_dot_gC"] for r in inertia],
        "non_node_C_dot_gC": [r["C_dot_gC"] for r in nonnode],
        "minimum_FSM_minimal_branches": 186,
        "opposite_landing_collision_forced": False,
        "v6_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
