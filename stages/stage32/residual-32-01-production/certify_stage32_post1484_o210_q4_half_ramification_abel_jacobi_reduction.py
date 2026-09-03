#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CERT = Path("stages/stage32/residual-32-01-production/post1484-o210-q4-half-ramification-abel-jacobi-reduction.json")


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
    if "canonical_sha256" in lock:
        obj = load_json(rel)
        require(obj.get("canonical_sha256_without_this_field") == lock["canonical_sha256"], f"stored canonical mismatch: {rel}")
        require(canonical_sha256_obj(obj) == lock["canonical_sha256"], f"canonical replay mismatch: {rel}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path, default=DEFAULT_CERT)
    args = parser.parse_args()

    cert = load_json(args.check)
    require(cert["schema"] == "STAGE32_POST1484_O210_Q4_HALF_RAMIFICATION_ABEL_JACOBI_REDUCTION_V1", "schema")
    require(cert["fixed_target"] == {"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32]}, "fixed target")

    for lock in cert["source_locks"].values():
        verify_lock(lock)

    half = load_json(Path(cert["source_locks"]["half_ramification_picard"]["path"]))
    first = load_json(Path(cert["source_locks"]["six_cusp_first_projection"]["path"]))

    require(half["half_ramification_divisor"]["effective"] is True, "E effective")
    require(half["half_ramification_divisor"]["degree"] == 24, "degree E")
    require(half["picard_identity"]["identity"] == "O_N(E) ~= z^*O_P1(1) tensor w^*O_P1(-1)", "half Picard identity")
    require(half["geometry"]["first_descended"]["degree"] == 105, "first degree")
    require(half["geometry"]["second_descended"]["degree"] == 81, "second degree")

    maps = cert["maps_on_normalization"]
    require(maps["genus"] == 1, "genus N")
    dz = maps["z"]["degree"]
    dw = maps["w"]["degree"]
    require((dz, dw) == (105, 81), "map degrees")

    rz_degree = 2 * dz
    rw_degree = 2 * dw
    require(rz_degree == 210, "R_z RH degree")
    require(rw_degree == 162, "R_w RH degree")
    require(cert["ramification_divisors"]["R_z"]["degree"] == rz_degree, "certificate R_z degree")
    require(cert["ramification_divisors"]["R_w"]["degree"] == rw_degree, "certificate R_w degree")
    require(cert["ramification_divisors"]["R_z"]["riemann_hurwitz_line_bundle"] == "O_N(R_z) ~= z^*O_P1(2)", "R_z line bundle")
    require(cert["ramification_divisors"]["R_w"]["riemann_hurwitz_line_bundle"] == "O_N(R_w) ~= w^*O_P1(2)", "R_w line bundle")

    first_base = first["first_projection_base_change"]
    hurwitz = first["six_cusp_hurwitz_data"]
    require(first_base["riemann_hurwitz_total_ramification_N_to_X4"] == 210, "first RH total")
    require(first_base["ramification_allowed_away_from_six_branch_values"] is False, "first cusp-only support")
    require(hurwitz["strict_boundary_simple_ramification_total"] == 182, "182 first strict ramification")
    require(hurwitz["exceptional_m2_simple_ramification_total"] == 28, "28 exceptional m2 ramification")
    require(hurwitz["total_transpositions"] == 210, "210 simple first ramification")
    require(182 + 28 == rz_degree, "R_z support partition")

    inp = cert["half_ramification_input"]
    require(inp["E_effective"] is True and inp["degree_E"] == 24, "certificate E")
    require(inp["line_bundle"] == half["picard_identity"]["identity"], "certificate half identity")

    red = cert["divisor_class_reduction"]
    require(red["squared_half_ramification_identity"] == "O_N(2E) ~= z^*O_P1(2) tensor w^*O_P1(-2)", "squared half identity")
    require(red["exact_linear_equivalence"] == "2E ~ R_z - R_w", "linear equivalence")
    require(red["origin_free_pic0_condition"] == "[2E - R_z + R_w] = 0 in Pic^0(N)", "Pic0 condition")
    require(2*inp["degree_E"] - rz_degree + rw_degree == 0, "degree-zero divisor condition")
    require(red["degree_zero_check"] == "2*24-210+162=0", "stored degree-zero check")

    fw = cert["object_type_firewall"]
    require(fw["surface_picard_preflight_applicable"] is False, "surface Picard preflight firewall")
    require(fw["pi_branch_points_equal_R_z_support"] is False, "pi/R_z support firewall")
    require(fw["pi_branch_points"] == "210 odd m=1 contacts", "pi branch support")
    require(fw["R_z_support"] == "182 first strict-boundary points plus 28 exceptional m=2 contacts", "R_z support")

    gap = cert["retained_data_gap"]
    require(gap["normalization_support_pic0_coordinates_available"] is False, "Pic0 data gap")
    require(gap["one_sided_ramified_105_81_correspondence_theorem_retained"] is False, "correspondence theorem gap")

    decision = cert["decision"]
    require(decision["O210_excluded"] is False, "O210 firewall")
    require(decision["new_standalone_obstruction"] is False, "standalone obstruction firewall")
    require(decision["exact_remaining_condition_identified"] is True, "remaining condition")

    for key in ["O188_reopened","old_93_93_odd_etale_route_reopened","first_hurwitz_reopened","scalar_T_only_reopened","surface_picard_support_reused_for_E","carrier_existence_proved","full178_authorized","receiver_credit","route_credit","theorem_credit","endpoint_credit","perfect_cuboid_claim"]:
        require(cert["firewalls"][key] is False, f"firewall {key}")

    actual = canonical_sha256_obj(cert)
    require(actual == cert["canonical_sha256_without_this_field"], "certificate canonical sha256")

    print(json.dumps({
        "ok": True,
        "canonical_sha256": actual,
        "degrees": [dz, dw],
        "ramification_degrees": [rz_degree, rw_degree],
        "degree_E": inp["degree_E"],
        "degree_zero": 2*inp["degree_E"] - rz_degree + rw_degree,
        "pic0_condition": red["origin_free_pic0_condition"],
        "result": decision["result"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
