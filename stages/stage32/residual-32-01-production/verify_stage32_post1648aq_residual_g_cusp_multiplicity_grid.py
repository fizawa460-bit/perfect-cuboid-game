#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648aq-residual-g-cusp-multiplicity-grid.json"
NOTE = HERE / "post1648aq-residual-g-cusp-multiplicity-grid-source-note.md"
DIAG = HERE / "diagnose_stage32_post1648aq_residual_g_action_preflight.py"
AP = HERE / "post1648ap-factor-pair-birational-conductor-demand.json"
AO = HERE / "post1648ao-special-fibre-hurwitz-budget.json"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"


def canonical_sha(obj: dict) -> str:
    y = dict(obj)
    y.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(y, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    assert cert["canonical_sha256_without_this_field"] == "1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e"
    assert canonical_sha(cert) == cert["canonical_sha256_without_this_field"]

    locks = cert["source_locks"]
    assert hashlib.sha256(NOTE.read_bytes()).hexdigest() == locks["source_note_sha256"]
    assert git_blob_sha1(NOTE) == locks["source_note_blob_sha1"]
    assert git_blob_sha1(DIAG) == locks["diagnostic_script_blob_sha1"]

    ap = json.loads(AP.read_text())
    ao = json.loads(AO.read_text())
    v6 = json.loads(V6.read_text())
    assert ap["canonical_sha256_without_this_field"] == cert["parent"]["ap_canonical"]
    assert ao["canonical_sha256_without_this_field"] == cert["parent"]["ao_canonical"]
    assert v6["canonical_sha256_without_this_field"] == cert["parent"]["v6_canonical"]

    proc = subprocess.run([sys.executable, "-B", str(DIAG)], cwd=ROOT, check=True, capture_output=True, text=True)
    x = json.loads(proc.stdout)
    assert x["mode"] == "SCRATCH_POST1648AQ_RESIDUAL_G_CUSP_MULTIPLICITY_GRID"
    assert x["full_retained_group"]["order"] == cert["residual_group"]["full_aut_order"] == 1536
    assert x["boundary_anchor"]["pointwise_stabilizer_order"] == cert["residual_group"]["pointwise_stabilizer_order"] == 8
    assert x["boundary_anchor"]["pointwise_stabilizer_element_order_histogram"] == cert["residual_group"]["pointwise_order_histogram"]
    assert x["boundary_anchor"]["labels_1based"] == cert["residual_group"]["boundary_labels"]
    assert x["aut_action_canonical"] == locks["retained_aut_action_canonical"]

    o = x["v6_residual_orbit"]
    co = cert["v6_orbit"]
    assert o["class_orbit_size"] == co["orbit_size"] == 8
    assert o["nontrivial_C_dot_gC_sorted"] == co["nontrivial_C_dot_gC"]
    assert o["sum_nontrivial_C_dot_gC"] == co["sum_nontrivial"] == 9286
    assert o["orbit_sum_square"] == co["S_square"] == 80352
    assert o["C_dot_orbit_sum"] == co["C_dot_S"] == 10044

    p = x["factor_pullback"]
    cp = cert["factor_pullback"]
    assert p["dir81_boundary_labels"] == cp["dir81_labels"]
    assert p["dir105_boundary_labels"] == cp["dir105_labels"]
    assert p["image_bidegree"] == cp["D_bidegree"] == [81, 105]
    assert p["image_square"] == cp["D_square"] == 17010
    assert p["P_square"] == cp["P_square"] == 136080
    assert p["C_dot_P"] == cp["C_dot_P"] == 17010

    e = x["exceptional_correction"]["correct_orientation"]
    ce = cert["exceptional_correction"]
    assert e["in_exceptional_span"] and e["unique"] and e["integral"] and e["nonnegative"]
    assert e["coefficients_exceptional_labels_93_to_140"] == ce["coefficients"]
    assert e["coefficient_sum"] == ce["sum"] == 1064
    assert e["coefficient_max"] == ce["max"] == 35
    assert e["positive_support"] == ce["support"] == 48
    assert e["C_dot_exceptional_correction_direct"] == ce["C_dot_T"] == 6966
    assert e["T_square"] == ce["T_square"] == -55728
    assert e["S_dot_T"] == ce["S_dot_T"] == 55728
    assert x["exceptional_correction"]["same_orientation_control"]["in_exceptional_span"] is False

    g = x["target_cusp_grid"]
    cg = cert["target_cusp_grid"]
    assert g["candidate_target_point_count"] == cg["target_points"] == 12
    assert [r["orbit_size"] for r in g["rows"]] == cg["orbit_sizes"]
    assert [r["image_multiplicity"] for r in g["rows"]] == cg["image_multiplicities"]
    assert g["sum_distinct_target_multiplicities"] == cg["sum_multiplicities"] == 266
    assert g["first_blowup_delta_lower_bound_sum"] == cg["first_blowup_delta_lower_bound"] == 3350
    assert g["D_total_delta"] == cg["D_total_delta"] == 8319
    assert g["dir81_fibre_multiplicity_sums"] == cg["dir81_fibre_sums"]
    assert g["dir105_fibre_multiplicity_sums"] == cg["dir105_fibre_sums"]
    assert g["violates_factor_fibre_intersection_budget"] == cg["factor_fibre_budget_violated"] is False

    c = x["conductor_decomposition"]
    cc = cert["conductor"]
    assert c["sum_nontrivial_C_dot_gC"] == cc["pairwise_sum"] == 9286
    assert c["C_dot_T"] == cc["C_dot_T"] == 6966
    assert c["canonical_discrepancy_intersection"] == cc["canonical_difference"] == 558
    assert c["half_corrected_sum"] == cc["required"] == 7847

    b = cert["branch_count"]
    assert b["exceptional_mass"] - b["AO_min_node_preimages"] == b["max_excess"] == 28
    assert b["AO_min_node_preimages"] - b["max_excess"] == b["min_transverse_node_branches"] == 210

    assert cert["residual_group"]["semantic_identification_granted"] is True
    assert cert["decision"]["v6_carrier_excluded"] is False
    assert cert["decision"]["Q602_excluded"] is False
    assert cert["decision"]["O210_excluded"] is False
    assert cert["decision"]["O212_plus_advance_allowed"] is False
    assert cert["guardrails"]["scratch_only"] is True
    assert cert["guardrails"]["shared_MAIN_STATE_unchanged"] is True
    assert cert["guardrails"]["shared_authority_unchanged"] is True

    print("PASS stage32 post1648AQ residual-G cusp multiplicity grid")
    print(json.dumps({
        "canonical": cert["canonical_sha256_without_this_field"],
        "residual_G_order": cert["residual_group"]["pointwise_stabilizer_order"],
        "target_points": cg["target_points"],
        "cusp_delta_lb": cg["first_blowup_delta_lower_bound"],
        "conductor": cc["required"],
        "min_transverse_node_branches": b["min_transverse_node_branches"],
        "v6_excluded": cert["decision"]["v6_carrier_excluded"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
