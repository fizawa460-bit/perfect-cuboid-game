#!/usr/bin/env python3
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONTRACT = Path("stages/stage32/residual-32-01-production/post1484-o210-q4-abel-jacobi-closure-contract.json")


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


def q(value):
    if isinstance(value, int):
        return Fraction(value, 1)
    if isinstance(value, str):
        return Fraction(value)
    raise AssertionError(f"unsupported rational encoding: {value!r}")


def point(value):
    if value is None:
        return None
    require(isinstance(value, list) and len(value) == 2, "point encoding")
    return (q(value[0]), q(value[1]))


def on_curve(P, A, B):
    if P is None:
        return True
    x, y = P
    return y*y == x*x*x + A*x + B


def neg(P):
    return None if P is None else (P[0], -P[1])


def add(P, Q, A):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == -y2:
        return None
    if P != Q:
        require(x1 != x2, "invalid equal-x addition")
        m = (y2-y1)/(x2-x1)
    else:
        if y1 == 0:
            return None
        m = (3*x1*x1 + A)/(2*y1)
    x3 = m*m - x1 - x2
    y3 = m*(x1-x3) - y1
    return (x3, y3)


def mul(n, P, A):
    if n < 0:
        return mul(-n, neg(P), A)
    out = None
    cur = P
    while n:
        if n & 1:
            out = add(out, cur, A)
        cur = add(cur, cur, A)
        n >>= 1
    return out


def verify_instance(instance, contract):
    require(instance["schema"] == "STAGE32_POST1490_O210_Q4_ABEL_JACOBI_PIC0_INSTANCE_V1", "instance schema")
    require(instance["contract_canonical_sha256"] == contract["canonical_sha256_without_this_field"], "contract lock")
    for lock in instance.get("source_locks", {}).values():
        verify_lock(lock)

    curve = instance["curve"]
    require(curve["profile"] == "short_weierstrass_Q_v1", "curve profile")
    A, B = q(curve["A"]), q(curve["B"])
    require(4*A*A*A + 27*B*B != 0, "singular curve")

    pts = {name: point(P) for name, P in instance["abel_jacobi_images"].items()}
    for name, P in pts.items():
        require(on_curve(P, A, B), f"point off curve: {name}")

    divisor = instance["decision_divisor"]
    require(divisor["name"] == "2E - R_z + R_w", "decision divisor name")
    terms = divisor["terms"]
    degree = sum(int(t["multiplicity"]) for t in terms)
    require(degree == 0, "decision divisor degree")
    require(divisor["degree"] == 0, "stored divisor degree")

    total = None
    for term in terms:
        name = term["point"]
        require(name in pts, f"unknown point: {name}")
        total = add(total, mul(int(term["multiplicity"]), pts[name], A), A)
    return total is None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--instance", type=Path)
    args = parser.parse_args()

    contract = load_json(args.check)
    require(contract["schema"] == "STAGE32_POST1490_O210_Q4_ABEL_JACOBI_CLOSURE_CONTRACT_V1", "schema")
    require(contract["fixed_target"] == {"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32]}, "fixed target")
    for lock in contract["source_locks"].values():
        verify_lock(lock)

    retained = contract["retained_exact_input"]
    require(retained["map_degrees"] == {"z":105,"w":81}, "map degrees")
    require(retained["degree_E"] == 24 and retained["degree_R_z"] == 210 and retained["degree_R_w"] == 162, "divisor degrees")
    require(2*retained["degree_E"] - retained["degree_R_z"] + retained["degree_R_w"] == 0, "degree-zero replay")
    require(retained["class_condition"] == "[2E - R_z + R_w] = 0 in Pic^0(N)", "Pic0 condition")

    fw = contract["coarse_relation_firewall"]
    require(fw["completeness_source_locked"] is False, "coarse completeness firewall")
    require(contract["closed_false_routes"]["coarse_quotient_nonzero_certifies_nonprincipal"] is False, "coarse quotient firewall")
    require(contract["verifier_semantics"]["target_exclusion_from_contract_only"] is False, "contract-only target firewall")

    required = contract["minimal_source_locked_instance"]["required"]
    require(len(required) == 5, "minimal instance requirements")
    require(contract["minimal_source_locked_instance"]["required_degree"] == 0, "required divisor degree")
    require(contract["decision"]["O210_excluded"] is False, "O210 firewall")
    require(contract["decision"]["exact_closure_interface_installed"] is True, "closure interface")
    require(contract["decision"]["source_locked_pic0_instance_available"] is False, "data gap")

    for key in ["O188_reopened","old_93_93_odd_etale_route_reopened","first_hurwitz_reopened","scalar_T_only_reopened","surface_picard_support_reused_for_E","carrier_existence_proved","full178_authorized","receiver_credit","route_credit","theorem_credit","endpoint_credit","perfect_cuboid_claim"]:
        require(contract["firewalls"][key] is False, f"firewall {key}")

    actual = canonical_sha256_obj(contract)
    require(actual == contract["canonical_sha256_without_this_field"], "contract canonical sha256")

    result = {
        "ok": True,
        "canonical_sha256": actual,
        "contract_only": args.instance is None,
        "O210_excluded": False,
        "result": contract["decision"]["result"],
    }
    if args.instance is not None:
        instance = load_json(args.instance)
        result["pic0_zero"] = verify_instance(instance, contract)
        result["instance_computation_only"] = True

    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
