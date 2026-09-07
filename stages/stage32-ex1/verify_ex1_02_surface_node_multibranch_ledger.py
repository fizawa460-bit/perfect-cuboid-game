#!/usr/bin/env python3
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage32-ex1" / "ex1-02-surface-node-multibranch-ledger.json"


def load_json(rel):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)


def canonical_sha256(obj):
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


def partition_number(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for s in range(k, n + 1):
            dp[s] += dp[s - k]
    return dp[n]


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(canonical_sha256(cert) == cert["canonical_sha256_without_this_field"], "certificate canonical sha256 mismatch")

    ex1_01 = load_json(cert["source_locks"]["ex1_01_candidate"]["path"])
    require(canonical_sha256(ex1_01) == cert["source_locks"]["ex1_01_candidate"]["canonical_sha256"], "EX1-01 canonical mismatch")

    pairings = cert["v6_contact_inventory"]["exceptional_pairings"]
    require(pairings == ex1_01["node_fiber_contract"]["exceptional_pairings"], "pairing vector mismatch with EX1-01")
    require(len(pairings) == 48, "wrong exceptional count")
    require(sum(pairings) == 266, "wrong total exceptional mass")
    require(sum(x > 0 for x in pairings) == 47, "wrong positive support count")

    zero = [i + 1 for i, x in enumerate(pairings) if x == 0]
    unit = [i + 1 for i, x in enumerate(pairings) if x == 1]
    nonunit = [i + 1 for i, x in enumerate(pairings) if x >= 2]
    require(zero == cert["v6_contact_inventory"]["zero_labels_1based"] == [6], "zero labels mismatch")
    require(unit == cert["v6_contact_inventory"]["unit_labels_1based"], "unit labels mismatch")
    require(len(unit) == cert["v6_contact_inventory"]["unit_count"] == 9, "unit count mismatch")
    require(nonunit == cert["v6_contact_inventory"]["nonunit_labels_1based"], "nonunit labels mismatch")
    require(len(nonunit) == cert["v6_contact_inventory"]["nonunit_count"] == 38, "nonunit count mismatch")

    dist = Counter(x for x in pairings if x >= 2)
    dist_json = {str(k): dist[k] for k in sorted(dist)}
    require(dist_json == cert["v6_contact_inventory"]["contact_mass_distribution_on_nonunit_nodes"], "contact mass distribution mismatch")

    ledger = cert["parameterized_residual_ledger"]
    counts = {str(k): partition_number(k) - 1 for k in sorted(dist)}
    require(counts == ledger["multibranch_partition_count_by_contact_mass"], "partition count table mismatch")
    require(dist_json == ledger["labeled_node_count_by_contact_mass"], "labeled node distribution mismatch")
    weighted = {str(k): dist[k] * (partition_number(k) - 1) for k in sorted(dist)}
    require(weighted == ledger["labeled_node_local_multibranch_type_count_by_contact_mass"], "weighted local type table mismatch")
    require(sum(weighted.values()) == ledger["total_labeled_node_local_multibranch_contact_types"] == 1188, "wrong total local contact types")

    excess = sum(max(x - 1, 0) for x in pairings)
    require(excess == 219, "node fibre excess capacity mismatch")
    require(ledger["global_node_fiber_excess_upper_bound"] == 219, "certificate fibre excess bound mismatch")
    require(ledger["surface_node_candidate_count"] == 38, "surface node candidate count mismatch")

    delta = cert["delta_interface"]
    require(delta["unit_contact_nodes_contribute_delta_E"] == 0, "unit-contact delta firewall missing")
    require(delta["delta_E_not_determined_by_contact_partition"] is True, "contact/delta separation missing")
    require(delta["no_finite_delta_upper_bound_from_fixed_contact_mass"] is True, "fixed-contact delta-bound firewall missing")
    local = delta["local_counterexample"]
    require(local["intersection_with_E"] == 2, "local counterexample contact mismatch")
    require(local["irreducible_unibranch"] is True, "local counterexample branch type mismatch")
    require(local["scope_firewall"].startswith("This is a local analytic counterexample"), "local counterexample scope firewall missing")

    status = cert["branch_status"]
    require(status["surface_node_multibranch_excluded"] is False, "surface-node branch falsely excluded")
    require(status["surface_node_multibranch_exactly_accounted_at_contact_partition_layer"] is True, "contact-layer residual ledger not marked accounted")
    require(status["next_leaf"] == "EX1-03_SMOOTH_AMBIENT_CURVE_SINGULARITY_CLOSURE", "wrong next leaf")

    exit_ = cert["exit"]
    require(exit_["surface_node_multibranch_branch_closed"] is False, "branch closed too strongly")
    require(exit_["surface_node_multibranch_branch_exactly_accounted_candidate"] is True, "exact-accounting candidate missing")
    require(exit_["surface_node_residual_ledger_complete_at_contact_layer"] is True, "residual ledger incomplete")
    require(exit_["branch_exclusion_credit"] is False, "branch exclusion credit must remain false")
    require(exit_["credit_ceiling"] == "NECESSARY_CONDITION_ONLY_UNAUDITED", "wrong credit ceiling")

    fire = cert["firewalls"]
    for key in (
        "contact_partition_promoted_to_geometric_realization",
        "node_fiber_excess_identified_with_delta",
        "exceptional_mass_identified_with_delta",
        "fixed_contact_mass_assumed_to_bound_delta",
        "local_counterexample_promoted_to_v6_member",
        "surface_node_nonbijectivity_assumed_strict_transform_singularity",
        "surface_node_branch_claimed_excluded",
        "stage32_main_credit",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ):
        require(fire[key] is False, f"forbidden promotion/claim: {key}")

    print("PASS_STAGE32EX1_EX1_02_SURFACE_NODE_MULTIBRANCH_LEDGER")


if __name__ == "__main__":
    main()
