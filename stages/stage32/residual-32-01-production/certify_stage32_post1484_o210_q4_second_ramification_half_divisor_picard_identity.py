#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CERT = Path("stages/stage32/residual-32-01-production/post1484-o210-q4-second-ramification-half-divisor-picard-identity.json")


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
    require(cert["schema"] == "STAGE32_POST1484_O210_Q4_SECOND_RAMIFICATION_HALF_DIVISOR_PICARD_IDENTITY_V1", "schema")
    require(cert["fixed_target"] == {"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32]}, "fixed target")

    for lock in cert["source_locks"].values():
        verify_lock(lock)

    local = load_json(Path(cert["source_locks"]["local_excess_decomposition"]["path"]))
    common = load_json(Path(cert["source_locks"]["common_cover_cartesian"]["path"]))
    v4 = load_json(Path(cert["source_locks"]["v4_cusp_quotient"]["path"]))
    bidegree = load_json(Path(cert["source_locks"]["audited_bidegree"]["path"]))

    require(local["global_unit_budget"]["unit_budget"] == 24, "local 24-unit budget")
    require(local["global_unit_budget"]["total_descended_second_ramification"] == 48, "local second ramification")
    require(local["first_projection_rigidity"]["first_exceptional_endpoint_excess_units"] == 0, "first endpoint rigidity")
    require(common["carrier_consequence"]["same_quadratic_extension"] is True, "common quadratic cover")

    q = v4["quotient_geometry"]
    require(q["genus_C0"] == 2, "genus C0")
    require(q["C0_to_X4_degree"] == 2, "degree C0/X4")
    require(q["C0_to_X4_total_fixed_points"] == 6, "six branch points")
    require(q["six_quotient_cusps_are_Weierstrass_points"] is True, "Weierstrass marking")

    degrees = [bidegree["modular_factor_bidegree"]["first_z"], bidegree["modular_factor_bidegree"]["second_w"]]
    ram = bidegree["O210_extremal_profile"]["descended_projection_ramification_totals"]
    hist = bidegree["O210_extremal_profile"]["forced_contact_histogram"]
    require(degrees == [105,81], "bidegree")
    require(ram == [0,48], "descended ramification")
    require(hist["m1_odd"] == 210 and hist["m2_even"] == 28, "O210 parity histogram")

    g = cert["geometry"]
    require(g["pi"] == {"map":"Y->N","degree":2,"connected":True,"ramified":True,"branch_points":210}, "pi geometry")
    require(g["first_descended"]["degree"] == 105 and g["first_descended"]["ramification_degree"] == 0 and g["first_descended"]["etale"] is True, "first descended map")
    require(g["second_descended"]["degree"] == 81 and g["second_descended"]["ramification_degree"] == 48, "second descended map")
    require(g["hyperelliptic_quotient"]["genus_C0"] == 2 and g["hyperelliptic_quotient"]["degree"] == 2, "hyperelliptic quotient")
    require(g["hyperelliptic_quotient"]["canonical_bundle"] == "K_C0 ~= h^*O_P1(1)", "canonical pencil")

    half = cert["half_ramification_divisor"]
    require(half["effective"] is True and half["degree"] == 24, "effective half divisor")
    require(half["ramification_divisor_identity"] == "R_f2=pi^*E", "ramification pullback identity")
    require(len(half["local_pullback_checks"]) == 4, "four local pullback types")

    require(cert["picard_pullback_injectivity"]["holds"] is True, "Picard pullback injectivity")
    pic = cert["picard_identity"]
    require(pic["identity"] == "O_N(E) ~= z^*O_P1(1) tensor w^*O_P1(-1)", "Picard identity")
    require(pic["degree"] == degrees[0] - degrees[1] == 24, "Picard degree")

    rr = cert["genus_one_effectivity_firewall"]
    require(rr["abstract_degree24_effectivity_automatic"] is True, "genus-one effectivity")
    require(rr["riemann_roch_h0"] == 24, "genus-one Riemann-Roch h0")
    require(rr["standalone_picard_degree_excludes"] is False, "Picard firewall")

    require(cert["decision"]["O210_excluded"] is False, "O210 firewall")
    require(cert["decision"]["exact_global_picard_class_identified"] is True, "global Picard result")
    for key in ["O188_reopened","old_93_93_odd_etale_route_reopened","carrier_existence_proved","full178_authorized","receiver_credit","route_credit","theorem_credit","endpoint_credit","perfect_cuboid_claim"]:
        require(cert["firewalls"][key] is False, f"firewall {key}")

    actual = canonical_sha256_obj(cert)
    require(actual == cert["canonical_sha256_without_this_field"], "certificate canonical sha256")

    print(json.dumps({
        "ok": True,
        "canonical_sha256": actual,
        "degree_pair": degrees,
        "ramification_pair": ram,
        "pi_branch_points": 210,
        "half_ramification_degree": 24,
        "picard_identity": pic["identity"],
        "result": cert["decision"]["result"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
