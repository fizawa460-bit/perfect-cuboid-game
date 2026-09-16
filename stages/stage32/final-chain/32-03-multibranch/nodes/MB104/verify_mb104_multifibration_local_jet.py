#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT = Path(__file__).with_name("MULTIFIBRATION-LOCAL-JET-CERTIFICATE.json")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    c = json.loads(CERT.read_text())
    require(c["schema"] == "STAGE32_MB104_MULTIFIBRATION_LOCAL_JET_WALL_V1", "schema")
    require(c["status"] == "RETAINED_LOCAL_WALL_MB104_INCOMPLETE", "status")
    require(c["receiver"] == "R29-LG2-MB", "receiver")

    fib = c["rank3_fibration_contract"]
    require(fib["fiber_class_formula"] == "2F_Q=H-sum_{i in B_Q}E_i", "fiber formula")
    require(fib["H_dot_E_i"] == 0, "H.E")
    require(fib["E_i_squared"] == -2, "E^2")
    require(fib["pairwise_exceptionals_disjoint"] is True, "disjoint exceptionals")
    # Exact intersection replay for a node contained in the base block:
    # 2F.E = H.E - E^2 = 0 - (-2) = 2.
    require((fib["H_dot_E_i"] - fib["E_i_squared"]) // 2 == 1, "F.E=1 replay")
    require(fib["for_i_in_base_block_F_dot_E_i"] == 1, "section degree")
    require(fib["generic_exceptional_is_local_section"] is True, "generic section")

    jet = c["minimal_cusp_jet_contract"]
    require(jet["cusp_type"] == "(A,B)=(1,1)", "minimal cusp")
    require(jet["exceptional_multiplicity"] == 1, "transverse multiplicity")
    require(jet["lambda_nonzero"] is True, "nonzero landing")
    require(jet["c_is_free_in_retained_local_packet"] is True, "free tangential jet")
    require(jet["downstairs_orders_remain_1_1_1"] is True, "cusp order preservation")

    ram = c["ramification_contract"]
    require(ram["unramified_if_cprime_nonzero"] is True, "generic unramified jet")
    require(ram["minimal_cusp_alone_forces_ramification"] is False, "no automatic ramification")
    require(ram["extra_first_jet_equation_required_for_ramification"] is True, "ramification jet equation")

    route = c["route_consequence"]
    require(route["fibration_count_alone_multiply_charges_R8"] is False, "no count-only multi-charge")
    require(route["global_tangent_or_jet_constraint_required"] is True, "global jet constraint required")
    require(route["such_global_constraint_proved_impossible"] is False, "do not overclaim")
    require(route["finite_R8_bound_proved"] is False, "no R8 bound")
    require(route["MB104_complete"] is False, "MB104 open")

    for lock in c["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    for key, val in c["credit_firewall"].items():
        require(val is False, f"credit firewall {key}")

    print("PASS: MB104 minimal cusp packet does not by itself force fibration ramification; global jet input still required")


if __name__ == "__main__":
    main()
