#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CERT = Path("stages/stage32/residual-32-01-production/post1484-o210-q4-abel-jacobi-equivalent-theorem-closure.json")

def load_json(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)

def blob_sha1(rel):
    data = (ROOT / rel).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()

def canonical_sha256_obj(obj):
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()

def require(cond, message):
    if not cond:
        raise AssertionError(message)

def verify_lock(lock):
    rel = Path(lock["path"])
    require(blob_sha1(rel) == lock["blob_sha1"], f"blob lock mismatch: {rel}")
    obj = load_json(rel)
    require(obj.get("canonical_sha256_without_this_field") == lock["canonical_sha256"], f"stored canonical mismatch: {rel}")
    require(canonical_sha256_obj(obj) == lock["canonical_sha256"], f"canonical replay mismatch: {rel}")
    return obj

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path, default=DEFAULT_CERT)
    args = parser.parse_args()

    cert = load_json(args.check)
    require(cert["schema"] == "STAGE32_POST1484_O210_Q4_ABEL_JACOBI_EQUIVALENT_THEOREM_CLOSURE_V1", "schema")
    target = {"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32]}
    require(cert["fixed_target"] == target, "fixed target")

    red = verify_lock(cert["source_locks"]["abel_jacobi_reduction"])
    cart = verify_lock(cert["source_locks"]["common_double_cover_cartesian_identity"])
    require(red["fixed_target"] == target and cart["fixed_target"] == target, "source target alignment")

    dcr = red["divisor_class_reduction"]
    require(dcr["exact_linear_equivalence"] == "2E ~ R_z - R_w", "exact linear equivalence")
    require(dcr["origin_free_pic0_condition"] == "[2E - R_z + R_w] = 0 in Pic^0(N)", "source Pic0 conclusion")
    require(dcr["degree_zero_check"] == "2*24-210+162=0", "degree-zero check")
    require(red["decision"]["O210_excluded"] is False, "source nonexclusion firewall")

    cc = cert["coordinate_free_closure"]
    require(cc["source_locked_linear_equivalence"] == dcr["exact_linear_equivalence"], "closure relation")
    require(cc["decision_divisor"] == "2E - R_z + R_w", "decision divisor")
    require(cc["origin_free_conclusion"] == dcr["origin_free_pic0_condition"], "closure Pic0 conclusion")
    require(cc["normalization_model_required_for_zero_test"] is False, "model not required")
    require(cc["support_point_coordinates_required_for_zero_test"] is False, "support coordinates not required")

    rel = cert["relation_to_closure_contract"]
    require(rel["contract_instance_required_for_this_zero_verdict"] is False, "contract instance firewall")
    require(rel["contract_remains_valid_as_generic_replay_interface"] is True, "generic contract retention")
    require(rel["contract_cannot_supply_new_exclusion_for_this_exact_class"] is True, "same-class exclusion firewall")

    verdict = cert["verdict"]
    require(verdict["abel_jacobi_class_zero"] is True, "class zero")
    require(verdict["O210_excluded"] is False, "O210 nonexclusion")
    require(verdict["this_obstruction_closed"] is True, "obstruction closed")
    require(verdict["row_status"] == "OPEN", "row remains open")
    require(verdict["next_exact_leaf"] == "O210_Q4_SIMULTANEOUS_105_81_CORRESPONDENCE_GEOMETRY", "next leaf")
    geom = verdict["next_geometry"]
    require(geom["first_map"] == {"degree":105,"etale":True}, "105 etale map")
    require(geom["second_map"] == {"degree":81,"ramification_total":48}, "81 ramified map")

    require(cart["verdict"]["next_exact_leaf"] == verdict["next_exact_leaf"], "Cartesian frontier alignment")
    require(cart["carrier_consequence"]["same_quadratic_extension"] is True, "same Beauville pullback")
    require(cart["verdict"]["O210_excluded"] is False, "Cartesian nonexclusion")

    anti = cert["anti_loop"]
    require(anti["repeat_same_pic0_coordinate_search_for_exclusion"] is False, "Pic0 anti-loop")
    require(anti["use_incomplete_marked_fiber_principal_relation_quotient_for_nonprincipality"] is False, "relation quotient firewall")
    require(anti["reopen_O186_or_O188"] is False, "O186/O188 firewall")

    for key in ["carrier_existence_proved","full178_authorized","receiver_credit","route_credit","theorem_credit","endpoint_credit","perfect_cuboid_claim"]:
        require(cert["firewalls"][key] is False, f"firewall {key}")

    actual = canonical_sha256_obj(cert)
    require(actual == cert["canonical_sha256_without_this_field"], "certificate canonical sha256")
    print(json.dumps({
        "ok": True,
        "canonical_sha256": actual,
        "class_zero": True,
        "O210_excluded": False,
        "next_exact_leaf": verdict["next_exact_leaf"],
        "reason": "source-locked exact linear equivalence makes the decision divisor principal"
    }, sort_keys=True))

if __name__ == "__main__":
    main()
