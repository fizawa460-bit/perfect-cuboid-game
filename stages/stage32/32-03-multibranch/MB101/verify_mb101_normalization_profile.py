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
    require(cert["schema"] == "STAGE32_MB101_NORMALIZATION_PROFILE_V1", "schema")
    require(cert["status"] == "RETAINED_NO_CREDIT", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    pop = cert["population"]
    require(pop["exceptional_node_count"] == 48, "48-node population")
    require(pop["multibranch_membership"] == "exists node i with r_i>=2", "multibranch semantics")
    require(pop["unibranch_degree_cap_imported"] is False, "no 176/192 cap import")
    require(pop["finite_degree_window_proved"] is False, "no premature finite window")

    branch = cert["branch_contract"]
    require(branch["A_positive_integer"] and branch["B_positive_integer"], "positive branch exponents")
    require(branch["A_plus_B_even"], "FSM parity")
    require(branch["exceptional_intersection_multiplicity"] == "m=min(A,B)", "A1 multiplicity adapter")
    require(branch["m_lower_bound"] == 1, "positive multiplicity")

    node = cert["node_contract"]
    require(node["M_i"] == "sum_j m_ij = D.E_i", "exceptional mass identity")
    require(node["when_M_i_positive"] == "1<=r_i<=M_i", "preimage/contact inequality")
    require(node["normalization_preimage_count_equals_exceptional_mass"] is False, "preimage/contact separation")
    require(node["branch_excess_equals_delta"] is False, "delta firewall")

    rels = set(cert["global_profile_contract"]["necessary_relations"])
    expected = {
        "N<=R",
        "R<=M",
        "N_MB<=N",
        "R-N=sum_{i:r_i>0}(r_i-1)",
    }
    require(expected <= rels, "global profile identities")

    delta = cert["delta_firewall"]
    require(delta["delta_determined_by_r_i_M_i"] is False, "delta not inferred from counts")
    require(delta["resolved_landing_partition_required"], "landing partition retained")
    require(delta["next_owner"] == "MB102", "MB102 routing")

    for lock in cert["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    fw = cert["credit_firewall"]
    require(fw["mb101_retained"] is True, "MB101 checkpoint")
    for key in [
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
    require(cert["next_node"] == "MB102", "next node")

    print("PASS: MB101 exact normalization-profile adapter retained with zero receiver credit")


if __name__ == "__main__":
    main()
