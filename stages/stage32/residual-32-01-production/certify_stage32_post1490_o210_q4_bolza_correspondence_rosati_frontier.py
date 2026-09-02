#!/usr/bin/env python3
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT = Path("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-correspondence-rosati-frontier.json")

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

def require(cond, msg):
    if not cond:
        raise AssertionError(msg)

def verify_lock(lock):
    if "path" not in lock:
        return
    rel = Path(lock["path"])
    require(blob_sha1(rel) == lock["blob_sha1"], f"blob lock mismatch: {rel}")
    if "canonical_sha256" in lock:
        obj = load_json(rel)
        require(obj["canonical_sha256_without_this_field"] == lock["canonical_sha256"], f"stored canonical mismatch: {rel}")
        require(canonical_sha256_obj(obj) == lock["canonical_sha256"], f"canonical replay mismatch: {rel}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, default=DEFAULT)
    args = ap.parse_args()

    obj = load_json(args.check)
    require(obj["schema"] == "STAGE32_POST1490_O210_Q4_BOLZA_CORRESPONDENCE_ROSATI_FRONTIER_V1", "schema")
    require(obj["fixed_target"] == {
        "row_id":"g1-d186","d":186,"e":266,"genus":1,
        "z":[-15,62,-44,26,32],"O":210,"qprime":4
    }, "fixed target")

    for lock in obj["source_locks"].values():
        verify_lock(lock)

    corr = obj["fixed_correspondence"]
    require(corr["target_curve"]["genus"] == 2, "target genus")
    require(corr["target_curve"]["bolza_model"] == "s^2=x(x^4-1)", "Bolza model")
    require(corr["target_curve"]["usual_model"] == "s^2=x^5-x", "Bolza expanded model")
    require(corr["source_curve"]["genus"] == 106, "source genus")
    f1, f2 = corr["maps"]["f1"], corr["maps"]["f2"]
    require((f1["degree"], f1["ramification_degree"], f1["etale"]) == (105,0,True), "f1 data")
    require((f2["degree"], f2["ramification_degree"], f2["etale"]) == (81,48,False), "f2 data")
    require(2*106-2 == 105*(2*2-2), "f1 Riemann-Hurwitz")
    require(2*106-2 == 81*(2*2-2)+48, "f2 Riemann-Hurwitz")

    lat = obj["jacobian_lattice"]
    require(lat["endomorphism_ring"] == "M_2(Z[sqrt(-2)])", "endomorphism ring")
    require(lat["z_rank"] == 8, "endomorphism lattice rank")
    require(lat["product_rosati_assumed"] is False, "product Rosati firewall")

    ce = obj["correspondence_endomorphism"]
    require(ce["definition"] == "T=(f1)_*(f2)^* in End(J(C0))", "T definition")
    require(ce["positive_semidefinite"] is True, "Rosati Gram positivity")
    require(ce["bound_scalar"] == 105*81 == 8505, "Schur scalar")
    require(ce["schur_bound"] == "T^dagger*T <= 8505", "Schur bound")
    require(ce["finite_integral_frontier_after_rosati_lock"] is True, "finite frontier")
    require(ce["sufficient_for_geometric_realization"] is False, "necessity firewall")

    dec = obj["decision"]
    require(dec["O210_excluded"] is False, "O210 firewall")
    require(dec["new_independent_correspondence_constraint"] is True, "independent frontier")
    require(dec["bolza_target_identified"] is True, "Bolza identification")
    require(dec["finite_endomorphism_frontier_reduced"] is True, "finite lattice reduction")
    require(dec["rosati_matrix_source_locked"] is False, "Rosati input gap")
    require(dec["next_exact_leaf"] == "O210_Q4_BOLZA_ROSATI_LATTICE_ENUMERATION", "next leaf")

    fw = obj["firewalls"]
    for key in [
        "O186_reopened","O188_reopened","abel_jacobi_zero_reopened",
        "old_93_93_both_etale_route_reused","product_rosati_assumed",
        "carrier_existence_proved","full178_authorized","receiver_credit",
        "route_credit","theorem_credit","endpoint_credit","perfect_cuboid_claim"
    ]:
        require(fw[key] is False, f"firewall {key}")

    actual = canonical_sha256_obj(obj)
    require(actual == obj["canonical_sha256_without_this_field"], "canonical sha256")
    print(json.dumps({
        "ok": True,
        "canonical_sha256": actual,
        "O210_excluded": False,
        "target": "Bolza genus-2 C0",
        "endomorphism_ring": lat["endomorphism_ring"],
        "rosati_bound_scalar": ce["bound_scalar"],
        "next_exact_leaf": dec["next_exact_leaf"]
    }, sort_keys=True))

if __name__ == "__main__":
    main()
