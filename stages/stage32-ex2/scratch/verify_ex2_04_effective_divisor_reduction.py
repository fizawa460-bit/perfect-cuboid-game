#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ADAPTER = ROOT / "stages/stage32-ex2/scratch/ex2-04-effective-divisor-reduction.json"
NOTE = ROOT / "stages/stage32-ex2/scratch/ex2-04-effective-divisor-reduction.md"
EX2_00 = ROOT / "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json"
EX2_01 = ROOT / "stages/stage32-ex2/EX2-01/section-source-inventory.json"
EX2_02 = ROOT / "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json"
AG = ROOT / "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json"
FORMAL = ROOT / "stages/stage32-ex2/scratch/formal-conic-global-obstruction-adapter.json"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    a = json.loads(ADAPTER.read_text())
    s00 = json.loads(EX2_00.read_text())
    s01 = json.loads(EX2_01.read_text())
    s02 = json.loads(EX2_02.read_text())
    ag = json.loads(AG.read_text())
    formal = json.loads(FORMAL.read_text())

    assert a["schema"] == "STAGE32EX2_SCRATCH_EX2_04_EFFECTIVE_DIVISOR_REDUCTION_V1"
    assert a["status"] == "SCRATCH_PROVISIONAL_INDEPENDENT_NOT_HOSTILE_AUDITED"
    assert a["base_pr"] == 1709
    assert a["base_pr_head"] == "2f0bfe9e4c815dd20a1d95c386221d6a8926ecf8"

    locks = a["source_locks"]
    assert git_blob_sha1(NOTE) == a["proof_note"]["blob_sha1"]
    assert git_blob_sha1(EX2_00) == locks["ex2_00"]["blob_sha1"]
    assert git_blob_sha1(EX2_01) == locks["ex2_01"]["blob_sha1"]
    assert git_blob_sha1(EX2_02) == locks["ex2_02"]["blob_sha1"]
    assert git_blob_sha1(AG) == locks["known140_effective_divisor"]["blob_sha1"]
    assert git_blob_sha1(FORMAL) == locks["formal_conic_adapter"]["blob_sha1"]
    assert ag["canonical_sha256_without_this_field"] == locks["known140_effective_divisor"]["canonical_sha256"]

    assert s00["ambient_model"]["q"] == 0
    assert s00["ambient_model"]["source_geometry"].find("q=0") >= 0
    assert s00["V6_target"]["D_square"] == 758
    assert s00["known140_scope"]["exact_nonnegative_integer_decomposition_exists"] is True
    assert s01["known140_effective_divisor_section_bridge"]["input"]["effective"] is True
    assert s01["known140_effective_divisor_section_bridge"]["input"]["nonzero_term_count"] == 61

    decomp = ag["known140_monoid"]["decomposition"]
    assert len(decomp) == 61
    assert sum(int(r["multiplicity"]) for r in decomp) == 155
    assert all(1 <= int(r["known140_label_1based"]) <= 140 for r in decomp)
    assert all(int(r["multiplicity"]) > 0 for r in decomp)
    coeff = {int(r["known140_label_1based"]): int(r["multiplicity"]) for r in decomp}
    assert {z: coeff[z] for z in [21, 24, 25, 30, 31]} == {21: 3, 24: 4, 25: 4, 30: 3, 31: 5}

    scan = s02["exact_scan"]
    assert scan["negative_pairing_count"] == 0
    assert scan["negative_labels_1based"] == []
    assert scan["minimum_pairing"] == 0
    assert scan["pairing_count"] == 140

    n = a["global_nef_reduction"]
    assert n["V6_globally_nef"] is True
    assert n["V6_big"] is True
    assert n["null_locus_completely_classified"] is False
    assert n["unknown_zero_intersection_curves_excluded"] is False

    h = a["H0_curve_reduction"]
    assert h["q_zero_consequence"] == "H0(S,L)/<s_E> ~= H0(E,L|E)"
    assert h["complete_H0_reconstruction_equivalent_to_curve_problem_plus_one_line"] is True
    assert h["target_restriction_factorization_exact"] is True
    assert h["ambient_complete_H0_basis_required_for_five_fixedness_questions"] is False

    assert formal["global_obstruction_reduction"]["rank_deletion_criterion"].startswith("C_i nonfixed iff rank(Delta)=rank(Delta_without_column_i)")
    assert a["formal_neighbourhood_integration"]["finite_thickening_local_obstruction_present"] is False
    assert "SCHEME_THEORETIC_RESTRICTION_GLUING_MODEL" in a["formal_neighbourhood_integration"]["remaining_missing_interface"]

    fw = a["credit_firewall"]
    assert all(v is False for v in fw.values())

    print("PASS: EX2-04 scratch effective-divisor reduction source locks, global-nef logic inputs, q=0 H0 reduction, and credit firewalls are intact")


if __name__ == "__main__":
    main()
