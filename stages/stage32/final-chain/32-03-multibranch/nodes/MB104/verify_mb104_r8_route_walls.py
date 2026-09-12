#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT = Path(__file__).with_name("R8-ROUTE-WALLS-CERTIFICATE.json")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def main() -> None:
    c = json.loads(CERT.read_text())
    require(c["schema"] == "STAGE32_MB104_R8_ROUTE_WALLS_V1", "schema")
    require(c["status"] == "RETAINED_ROUTE_WALLS_MB104_INCOMPLETE", "status")
    require(c["receiver"] == "R29-LG2-MB", "receiver")

    loc = c["local_a1_wall"]
    require(loc["minimal_cusp_type"] == "(A,B)=(1,1)", "minimal type")
    require(loc["exceptional_multiplicity"] == 1, "minimal multiplicity")
    require(loc["distinct_lambda_can_separate_after_resolution"] is True, "landing separation")
    require(loc["local_data_imply_absolute_R8_bound"] is False, "no local R8 cap")

    gfu = c["gfu_wall"]
    require(gfu["symmetric_differential_degree"] == "-d+M+4g-4", "GFU degree")
    require(gfu["smooth_at_nodes_corollary"] == "d<=4g+44", "GFU smooth bound")
    require(gfu["supplies_R8_upper_slope_lt_one_quarter"] is False, "GFU wall")

    fib = c["rank3_fibration_wall"]
    require(fib["rank3_quadric_count"] == 6, "six rank3 quadrics")
    require(fib["base_nodes_per_quadric"] == 8, "eight base nodes")
    require(fib["singular_node_count"] == 48, "48 nodes")
    require(fib["rank3_quadric_count"] * fib["base_nodes_per_quadric"] == fib["singular_node_count"],
            "partition cardinality")
    require(fib["base_sets_partition_48_nodes"] is True, "partition")
    require(fib["fiber_class_formula"] == "2F_Q=H-sum_{i in B_Q}E_i", "fiber formula")
    require(fib["nef_block_inequality"] == "sum_{i in B_Q}M_i<=d", "block inequality")
    require(fib["summed_inequality"] == "M<=6d", "summed inequality")
    require(fib["R8_consequence"] == "R8<=R<=M<=6d", "R8 consequence")
    require(fib["slope"] == 6, "slope")
    require(fib["required_slope_strictly_less_than"] == 0.25, "required slope")
    require(fib["slope"] >= fib["required_slope_strictly_less_than"], "route is too weak")
    require(fib["closes_MB104"] is False, "no closure")

    full = c["full_28_fibration_firewall"]
    require(full["genus5_fibration_count"] == 28, "28 fibrations")
    require(full["decomposition"] == "6 rank3 + 2*11 rank4", "28 decomposition")
    require(full["simple_fiber_or_base_locus_intersection_closes_R8"] is False,
            "no simple 28-fibration closure")
    require(full["new_branchwise_ramification_or_tangent_charging_lemma_required"] is True,
            "new branchwise lemma required")

    lit = c["literature_ceiling"]
    require(lit["stoll_testa_2026_low_genus_classification_question_open"] is True,
            "current literature ceiling")
    require(lit["rational_nonconic_lower_exceptional_incidence"] == 8, "rational lower incidence")
    require(lit["genus1_lower_exceptional_incidence"] == 4, "genus1 lower incidence")
    require(lit["btva_distinct_node_support_results_bound_R8_multiplicity"] is False,
            "node support/R8 firewall")

    for lock in c["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    fw = c["credit_firewall"]
    for key, val in fw.items():
        require(val is False, f"credit firewall {key}")

    print("PASS: MB104 R8 route walls retained; simple local/GFU/rank3-fibration routes do not close finite window")


if __name__ == "__main__":
    main()
