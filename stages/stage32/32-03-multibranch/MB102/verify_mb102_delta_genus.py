#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT_PATH = Path(__file__).with_name("CERTIFICATE.json")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB102_DELTA_GENUS_LEDGER_V1", "schema")
    require(cert["status"] == "RETAINED_NO_CREDIT", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    local = cert["local_delta_contract"]
    require(local["resolved_point_formula"] == "delta_P=sum intrinsic_branch_delta + sum pairwise_intersection_multiplicity", "delta decomposition")
    require(local["different_resolved_points_have_no_pairwise_local_term"], "resolved-point separation")
    for key in [
        "exceptional_delta_equals_exceptional_mass",
        "exceptional_delta_equals_normalization_preimage_count",
        "exceptional_delta_equals_branch_excess",
        "delta_i_equals_M_i_minus_r_i",
        "delta_i_equals_choose_r_i_2",
    ]:
        require(local[key] is False, key)

    global_contract = cert["global_genus_contract"]
    require(global_contract["H_equals_K_S"], "H=K_S")
    require(global_contract["arithmetic_genus"] == "p_a(D)=1+(D^2+d)/2", "adjunction")
    require(global_contract["normalization_genus_relation"] == "p_a(D)-g=Delta_total", "normalization genus")
    require(global_contract["delta_split"] == "Delta_total=Delta_exc+Delta_off", "delta split")
    require(global_contract["exact_identity"] == "D^2+d=2g-2+2*Delta_total", "global correction identity")
    require(global_contract["g0_specialization"] == "D^2=-d-2+2*Delta_total", "g=0 specialization")
    require(global_contract["g1_specialization"] == "D^2=-d+2*Delta_total", "g=1 specialization")
    require(global_contract["finite_degree_bound_implied"] is False, "no finite degree claim")

    fields = set(cert["node_ledger_fields"])
    expected = {
        "r_i",
        "M_i",
        "resolved_landing_partition_L_i",
        "intrinsic_branch_deltas",
        "pairwise_intersection_multiplicities",
        "Delta_i_exc",
    }
    require(expected <= fields, "complete node ledger fields")

    off = cert["off_exceptional_firewall"]
    require(off["Delta_off_forced_zero"] is False, "off-exceptional delta firewall")
    require(off["MB101_counts_bound_Delta_off"] is False, "MB101 counts do not bound Delta_off")

    for lock in cert["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    fw = cert["credit_firewall"]
    require(fw["mb101_retained"] and fw["mb102_retained"], "retained parent/current nodes")
    for key in [
        "finite_picard_enumeration_released",
        "r29_lg2_mb_discharged",
        "receiver_credit",
        "effectivity_credit",
        "final_milestone_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ]:
        require(fw[key] is False, f"credit firewall {key}")
    require(cert["next_node"] == "MB103", "next node")

    print("PASS: MB102 exact local-delta/global-genus ledger retained with zero receiver credit")


if __name__ == "__main__":
    main()
