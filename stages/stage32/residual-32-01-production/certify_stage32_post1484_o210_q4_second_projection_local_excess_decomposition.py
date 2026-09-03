#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CERT = Path("stages/stage32/residual-32-01-production/post1484-o210-q4-second-projection-local-excess-decomposition.json")


def load_json(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)


def blob_sha1(rel):
    data = (ROOT / rel).read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def canonical_sha256_obj(obj):
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def require(cond, message):
    if not cond:
        raise AssertionError(message)


def verify_source_lock(lock):
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
    require(cert["schema"] == "STAGE32_POST1484_O210_Q4_SECOND_PROJECTION_LOCAL_EXCESS_DECOMPOSITION_V1", "schema")
    require(cert["fixed_target"] == {"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32]}, "fixed target")

    for lock in cert["source_locks"].values():
        verify_source_lock(lock)

    bidegree = load_json(Path(cert["source_locks"]["audited_bidegree"]["path"]))
    local = load_json(Path(cert["source_locks"]["local_parity_adapter"]["path"]))
    accounting = load_json(Path(cert["source_locks"]["second_projection_accounting"]["path"]))
    common = load_json(Path(cert["source_locks"]["common_cover_cartesian"]["path"]))

    require([bidegree["modular_factor_bidegree"]["first_z"], bidegree["modular_factor_bidegree"]["second_w"]] == [105,81], "modular bidegree")
    require(bidegree["O210_extremal_profile"]["descended_projection_ramification_totals"] == [0,48], "descended ramification")
    h = bidegree["O210_extremal_profile"]["forced_contact_histogram"]
    require((h["m1_odd"], h["m2_even"], h["B"]) == (210,28,238), "O210 histogram")
    require(210 + 2*28 == 266, "exceptional mass")

    rows = bidegree["resolved_cusp_fiber_intersections"]
    first_CL = sum(r["C_dot_L"] for r in rows if r["factor"] == "first_z")
    second_CL = sum(r["C_dot_L"] for r in rows if r["factor"] == "second_w")
    require((first_CL, second_CL) == (182,110), "strict-boundary totals")
    for r in rows:
        require(r["C_dot_resolved_cusp_fiber"] == r["incident_exceptional_mass"] + 2*r["C_dot_L"], f"resolved fiber identity boundary {r['boundary_label']}")

    adapter = local["local_adapter"]
    require("same parity" in adapter["parity"], "local parity adapter")
    require(adapter["odd_contact"]["projection_local_degree"] == "e_i=A_i on each Y lift.", "odd local degree adapter")
    require(adapter["even_contact"]["projection_local_degree"] == "e_i=A_i/2 on each Y lift.", "even local degree adapter")

    require(common["carrier_consequence"]["same_quadratic_extension"] is True, "common quadratic cover")
    require(accounting["audited_inputs"]["second_factor_ramification_Y_to_C0"] == 48, "second accounting ramification")
    require(accounting["derivation"]["T_range"] == [86,110], "T range")

    audited = cert["audited_inputs"]
    require(audited["modular_factor_degrees_N_to_X4"] == [105,81], "certificate degrees N")
    require(audited["descended_projection_degrees_Y_to_C0"] == [105,81], "certificate degrees Y")
    require(audited["descended_projection_ramification_totals"] == [0,48], "certificate ramification")
    require(audited["exceptional_contact_histogram"] == {"m1":210,"m2":28,"B":238,"mass":266}, "certificate histogram")
    require(audited["first_factor_C_dot_L_total"] == first_CL, "certificate first C.L")
    require(audited["second_factor_C_dot_L_total"] == second_CL, "certificate second C.L")

    rigid = cert["first_projection_rigidity"]
    require(rigid["odd_m1"]["etale_forces_A1"] == 1, "m1 rigidity")
    require(rigid["even_m2"]["etale_forces_A1"] == 2, "m2 rigidity")
    require(rigid["first_exceptional_endpoint_excess_units"] == 0, "first endpoint excess")
    require(rigid["first_strict_boundary_intersections_transverse"] is True, "first strict transversality")
    require(rigid["first_strict_boundary_distinct_points"] == 182, "first strict point count")

    budget = cert["global_unit_budget"]
    require(budget["total_descended_second_ramification"] == 48, "budget ramification")
    require(budget["unit_budget"] == 24, "24-unit budget")
    require(budget["T_refinement"]["T_min"] == 86 and budget["T_refinement"]["T_max"] == 110, "certificate T bounds")

    replay = []
    for T in range(86,111):
        cusp_units = 110 - T
        away_units = T - 86
        require(cusp_units >= 0 and away_units >= 0, f"nonnegative units T={T}")
        require(cusp_units + away_units == 24, f"unit sum T={T}")
        cusp_ram = 2*cusp_units
        away_ram = 2*away_units
        require(cusp_ram == 220 - 2*T, f"cusp ramification T={T}")
        require(away_ram == 2*T - 172, f"away ramification T={T}")
        require(cusp_ram + away_ram == 48, f"total ramification T={T}")
        replay.append((T,cusp_units,away_units))

    require(cert["decision"]["O210_excluded"] is False, "firewall O210")
    require(cert["decision"]["standalone_scalar_budget_excludes"] is False, "scalar firewall")
    require(cert["decision"]["exact_localization_complete"] is True, "localization result")
    for key in ["O188_reopened","old_93_93_odd_etale_route_reopened","carrier_existence_proved","full178_authorized","receiver_credit","route_credit","theorem_credit","endpoint_credit","perfect_cuboid_claim"]:
        require(cert["firewalls"][key] is False, f"firewall {key}")

    expected = cert["canonical_sha256_without_this_field"]
    actual = canonical_sha256_obj(cert)
    require(actual == expected, "certificate canonical sha256")

    print(json.dumps({
        "ok": True,
        "canonical_sha256": actual,
        "source_locks": len(cert["source_locks"]),
        "first_C_dot_L": first_CL,
        "second_C_dot_L": second_CL,
        "T_values_replayed": len(replay),
        "unit_budget": 24,
        "result": cert["decision"]["result"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
