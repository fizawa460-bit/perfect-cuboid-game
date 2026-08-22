import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    return json.loads((ROOT / name).read_text())


def main():
    ledger = load("active-kernel-ledger.json")
    inactive = load("inactive-inventory.json")
    routes = load("route-portfolio.json")
    controller = load("controller-delta.json")
    audit = load("audit-state.json")

    assert ledger["source_receiver_or_terminal_frontier_count"] == 46
    assert ledger["source_class_counts"] == {"1": 6, "2": 13, "3": 11, "4": 16}
    assert ledger["active_source_entry_count"] == 24
    assert ledger["compressed_kernel_count"] == 13
    assert ledger["compressed_kernel_class_counts"] == {"2": 4, "3": 9}
    assert ledger["mixed_execution_class_kernel_count"] == 0

    expected_c2 = {
        "R29-LG2", "R29-LG2-EFF", "R29-LG2-MB", "R29-CAMP4",
        "R29-KUM5", "R29-K3-RULED2", "R29-BR0A", "R29-BR0B",
        "R29-BR0G", "R29-BR2A", "R29-BR2B", "R29-NF-PHYS2",
        "R29-EXT-CHANG-E",
    }
    expected_c3 = {
        "R29-PI1-OPEN", "R29-CAMP2", "R29-BEAU1C", "R29-BEAU2",
        "R29-BEAU3", "R29-QWEB-CLIFFORD", "R29-KUM-LOC3",
        "R29-PESCH-E1", "R29-FIB2", "R29-EXT-CHANG-C",
        "TERMINAL-P-OVER-M3",
    }

    mapped_c2 = []
    for k in ledger["class2_kernels"]:
        assert k["execution_class"] == 2
        mapped_c2.extend(k["children"])
    mapped_c3 = []
    for k in ledger["class3_kernels"]:
        assert k["execution_class"] == 3
        mapped_c3.extend(k["children"])

    assert len(mapped_c2) == len(set(mapped_c2)) == 13
    assert len(mapped_c3) == len(set(mapped_c3)) == 11
    assert set(mapped_c2) == expected_c2
    assert set(mapped_c3) == expected_c3
    assert set(mapped_c2).isdisjoint(mapped_c3)

    assert len(inactive["closed_class1"]) == 6
    assert len({x["id"] for x in inactive["closed_class1"]}) == 6
    assert len(inactive["dormant_class4"]) == 16
    assert len({x["id"] for x in inactive["dormant_class4"]}) == 16
    assert all(x.get("reactivate_if") for x in inactive["dormant_class4"])

    assert routes["attack_route_count_retained"] == 11
    assert routes["route_colors"] == {"green": 1, "amber": 10, "red": 0, "merged": 0}
    assert routes["independent_execution_owner_route_count"] == 9
    assert routes["merged_support_route_count"] == 2
    assert set(routes["merged_support_routes"]) == {"G10-K3-SIGN", "J12-JOINT-V4"}
    assert len(routes["routes"]) == 11
    assert len({r["route"] for r in routes["routes"]}) == 11

    assert audit["audit_verdict"] == "PASS_AFTER_BOUNDED_SEMANTIC_REPAIR"
    assert audit["active_source_entry_unmapped_count"] == 0
    assert audit["active_source_entry_duplicate_mapping_count"] == 0
    assert audit["mixed_execution_class_kernel_count"] == 0
    assert audit["hidden_class1_pending_count"] == 0
    assert audit["dormant_reactivation_trigger_missing_count"] == 0
    assert audit["brauer_kernel"]["internal_dependency_shape"] == "DAG_NOT_LINEAR_CHAIN"
    assert audit["route_portfolio"]["independence_scope"] == "CURRENT_SCHEDULING_OWNERSHIP_ONLY_NOT_MATHEMATICAL_OR_STATISTICAL_INDEPENDENCE"

    c = controller["stage29_16"]
    assert c["source_receiver_or_terminal_frontier_count"] == 46
    assert c["active_source_entry_count"] == 24
    assert c["compressed_kernel_count"] == 13
    assert c["compressed_kernel_class_counts"] == {"2": 4, "3": 9}
    assert c["attack_route_count"] == 11
    assert c["green_route_count"] == 1
    assert c["amber_route_count"] == 10
    assert c["audit_required"] is False
    assert c["audit_verdict"] == "PASS_AFTER_BOUNDED_SEMANTIC_REPAIR"
    assert c["merge_allowed"] is True
    assert c["advance_allowed"] is True
    assert c["hidden_class1_pending_count"] == 0
    assert c["P_over_M3_scale_known"] is False
    assert c["perfect_cuboid_existence_claim"] is False
    assert c["perfect_cuboid_nonexistence_claim"] is False

    print("Stage29-16 audited compression verifier: PASS")
    print("46 = 6 closed + 13 class2 + 11 class3 + 16 dormant")
    print("24 active entries -> 13 kernels = 4 class2 + 9 class3")
    print("11 historical routes -> 9 scheduling owners + 2 merged-support routes")
    print("Brauer internal dependency shape = DAG, not strict linear chain")


if __name__ == "__main__":
    main()
