#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage32-ex1" / "ex1-01-global-normalization-defect-decomposition.json"

def canonical_sha256(obj):
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def git_blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def require(cond, msg):
    if not cond:
        raise AssertionError(msg)

def load_json(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)

def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(canonical_sha256(cert) == cert["canonical_sha256_without_this_field"], "certificate canonical sha256 mismatch")

    ex100 = load_json(cert["source_locks"]["ex1_00_candidate"]["path"])
    require(canonical_sha256(ex100) == cert["source_locks"]["ex1_00_candidate"]["canonical_sha256"],
            "EX1-00 candidate canonical sha mismatch")
    require(ex100["v6_target"]["D_square"] == 758, "EX1-00 D^2 mismatch")
    require(ex100["v6_target"]["K_dot_D"] == 186, "EX1-00 K.D mismatch")
    require(ex100["v6_target"]["arithmetic_genus"] == 473, "EX1-00 p_a mismatch")
    require(ex100["v6_target"]["required_total_normalization_genus_defect"] == 472, "EX1-00 delta mismatch")

    ah_lock = cert["source_locks"]["fsm_AH_candidate"]
    ah_path = ROOT / ah_lock["path"]
    require(git_blob_sha1(ah_path) == ah_lock["blob_sha1"], "AH blob mismatch")
    ah = json.loads(ah_path.read_text(encoding="utf-8"))
    require(canonical_sha256(ah) == ah_lock["canonical_sha256"], "AH canonical sha mismatch")

    note_lock = cert["source_locks"]["fsm_source_note"]
    note_path = ROOT / note_lock["path"]
    require(git_blob_sha1(note_path) == note_lock["blob_sha1"], "FSM source-note blob mismatch")

    surface_lock = cert["source_locks"]["surface_invariants"]
    surface_path = ROOT / surface_lock["path"]
    require(git_blob_sha1(surface_path) == surface_lock["blob_sha1"], "surface invariant source blob mismatch")

    pairings = ah["v6_exact_data"]["exceptional_pairings"]
    require(len(pairings) == 48, "expected 48 exceptional pairings")
    require(sum(pairings) == 266, "exceptional mass mismatch")
    require(sum(x > 0 for x in pairings) == 47, "positive support mismatch")

    zero = [i + 1 for i, x in enumerate(pairings) if x == 0]
    unit = [i + 1 for i, x in enumerate(pairings) if x == 1]
    nonunit = [i + 1 for i, x in enumerate(pairings) if x >= 2]
    require(zero == [6], "zero exceptional label mismatch")
    require(unit == [1, 2, 3, 7, 15, 20, 22, 24, 36], "unit-positive label mismatch")
    require(len(nonunit) == 38, "nonunit-positive count mismatch")

    node = cert["node_fiber_contract"]
    require(node["exceptional_pairings"] == pairings, "certificate pairing vector mismatch")
    require(node["zero_labels_1based"] == zero, "certificate zero labels mismatch")
    require(node["unit_positive_labels_1based"] == unit, "certificate unit labels mismatch")
    require(node["nonunit_positive_labels_1based"] == nonunit, "certificate nonunit labels mismatch")
    require(node["surface_node_multibranch_candidate_labels_1based"] == nonunit, "candidate node list mismatch")
    require(node["surface_node_multibranch_candidate_count"] == 38, "candidate node count mismatch")
    require(sum(x - 1 for x in pairings if x > 0) == 219, "node fibre excess arithmetic mismatch")
    require(node["node_fiber_excess_upper_bound_from_contacts"] == 219, "certificate node fibre excess bound mismatch")
    require(node["node_fiber_excess_is_not_strict_transform_delta"] is True, "node fibre/delta firewall missing")

    replay = cert["replayed_bijective_normalization_exclusion"]
    fsm = ah["fsm_refinement"]
    require(replay["degree_d"] == 186 and replay["normalization_genus"] == 1, "AH target mismatch")
    require(replay["met_surface_nodes"] == 47, "AH met-node count mismatch")
    require(replay["fsm_zero_lower_order_per_k"] == fsm["zeros_lower_order_per_k"] == 372, "AH zero-order mismatch")
    require(replay["fsm_pole_upper_order_per_k_if_all_47_minimal"] == fsm["poles_upper_order_per_k_if_all_N_minimal"] == 376,
            "AH all-minimal pole bound mismatch")
    require(replay["fsm_pole_upper_order_per_k_if_at_least_one_nonminimal"] == fsm["poles_upper_order_per_k_if_at_least_one_nonminimal"] == 368,
            "AH nonminimal pole bound mismatch")
    require(372 > 368, "AH nonminimal contradiction arithmetic failed")
    require(ah["local_A1_resolution"]["minimal_cusp_strict_transform_exceptional_intersection"] == 1,
            "minimal cusp exceptional intersection mismatch")
    require(47 * 1 == 47 and 47 != 266, "AH exceptional-mass contradiction arithmetic failed")

    partition = cert["normalization_nonbijectivity_location_partition"]
    require(partition["exhaustive"] is True, "nonbijectivity partition not marked exhaustive")
    require(partition["unidentified_third_locus"] is False, "unexpected third locus")
    require(partition["branch_1"]["candidate_node_labels_1based"] == nonunit, "node branch candidates mismatch")

    delta = cert["strict_transform_delta_ledger"]
    require(delta["arithmetic_genus"] == 473, "delta ledger p_a mismatch")
    require(delta["normalization_genus"] == 1, "delta ledger genus mismatch")
    require(delta["total_delta_on_Gamma"] == 472, "delta ledger total mismatch")
    require(delta["partition"] == "delta_E + delta_U = 472", "delta partition mismatch")

    fire = cert["firewalls"]
    forbidden_true = (
        "delta_472_identified_with_exceptional_mass_266",
        "node_fiber_excess_219_identified_with_delta",
        "global_nonbijectivity_localized_to_surface_nodes_only",
        "unit_contact_node_allowed_as_multibranch_fibre",
        "surface_node_nonbijectivity_forces_strict_transform_singularity",
        "unibranch_delta_discarded",
        "actual_v6_genus1_member_materialized",
        "stage32_main_credit",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    )
    for key in forbidden_true:
        require(fire[key] is False, f"forbidden promotion/identification: {key}")

    exit_state = cert["exit"]
    require(exit_state["global_nonbijectivity_partition_proved_candidate"] is True, "EX1-01 partition candidate missing")
    require(exit_state["surface_node_multibranch_candidate_sites_reduced_from"] == 47, "wrong site-reduction source count")
    require(exit_state["surface_node_multibranch_candidate_sites_reduced_to"] == 38, "wrong site-reduction target count")
    require(exit_state["surface_node_multibranch_branch_closed"] is False, "node branch falsely closed")
    require(exit_state["smooth_ambient_curve_singularity_branch_closed"] is False, "smooth branch falsely closed")
    require(exit_state["credit_ceiling"] == "NECESSARY_CONDITION_ONLY_UNAUDITED", "wrong credit ceiling")
    require(exit_state["branch_exclusion_credit"] is False, "branch exclusion credit incorrectly granted")
    require(exit_state["full_target_closure"] is False, "full target closure incorrectly granted")
    require(exit_state["next_leaf"] == "EX1-02_SURFACE_NODE_MULTIBRANCH_CLOSURE", "wrong next leaf")

    print("PASS_STAGE32EX1_EX1_01_GLOBAL_NORMALIZATION_DEFECT_DECOMPOSITION")

if __name__ == "__main__":
    main()
