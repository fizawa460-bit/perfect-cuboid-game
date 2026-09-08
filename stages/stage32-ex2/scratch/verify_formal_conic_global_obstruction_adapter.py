#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ADAPTER = ROOT / "stages/stage32-ex2/scratch/formal-conic-global-obstruction-adapter.json"
NOTE = ROOT / "stages/stage32-ex2/scratch/independent-formal-conic-obstruction.md"
SOURCE = ROOT / "stages/stage32-ex2/EX2-03/remaining-five-conic-restriction-preflight.json"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    a = json.loads(ADAPTER.read_text())
    s = json.loads(SOURCE.read_text())

    assert a["schema"] == "STAGE32EX2_SCRATCH_FORMAL_CONIC_GLOBAL_OBSTRUCTION_ADAPTER_V1"
    assert a["status"] == "SCRATCH_PROVISIONAL_INDEPENDENT_NOT_HOSTILE_AUDITED"
    assert a["base_pr"] == 1709
    assert a["base_pr_head"] == "2f0bfe9e4c815dd20a1d95c386221d6a8926ecf8"

    assert git_blob_sha1(NOTE) == a["proof_note"]["blob_sha1"]
    assert git_blob_sha1(SOURCE) == a["source_lock"]["blob_sha1"]
    assert s["canonical_sha256_without_this_field"] == a["source_lock"]["canonical_sha256"]

    g = a["input_geometry_over_Qbar"]
    assert g["labels_1based"] == s["remaining_labels_1based"] == [21, 24, 25, 30, 31]
    assert g["pairwise_disjoint"] is True and s["exact_geometry"]["pairwise_disjoint"] is True
    assert g["each_self_intersection"] == s["exact_geometry"]["all_five_self_intersection"] == -4
    assert g["V6_dot_each"] == s["exact_geometry"]["V6_dot_each_curve"] == 0
    assert s["restriction_reduction"]["target_space_dimension"] == 1

    f = a["formal_neighbourhood_reduction"]
    for n in range(1, 101):
        assert sum(4*j + 1 for j in range(n)) == 2*n*n - n
        assert 5 * sum(4*j + 1 for j in range(n)) == 5 * (2*n*n - n)
    assert f["H1_kernel_vanishes_for_all_n_ge_1"] is True
    assert f["formal_completion_trivial_along_each_C"] is True
    assert f["local_jet_search_alone_can_create_new_obstruction"] is False

    r = a["global_obstruction_reduction"]
    assert r["connecting_map"] == "delta_1: k^5 -> H1(S,L(-Z))"
    assert "rank(Delta)=rank(Delta_without_column_i)" in r["rank_deletion_criterion"]
    assert r["trivialization_rescaling_invariant"] is True

    c = a["ex2_04_consumption_contract"]
    assert c["complete_H0_basis_required_before_fixedness_test"] is False
    assert c["certified_H0_subspace_can_certify_nonfixedness"] is True
    assert c["certified_H0_subspace_miss_can_certify_fixedness"] is False
    assert c["rank_deletion_test_can_classify_each_of_the_five_once_Delta_is_exact"] is True

    fw = a["credit_firewall"]
    assert all(v is False for v in fw.values())

    print("PASS: scratch formal-conic global-obstruction adapter is source-locked and EX2-04 consumption semantics are intact")


if __name__ == "__main__":
    main()
