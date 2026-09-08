#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = ROOT / "stages/stage32/scratch/ex1-ex4-krr-conjugator-torsor-no-go-20260908.json"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def load_locked(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], (path, blob_sha1(path), lock["blob_sha1"])
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert cert["schema"] == "STAGE32_MAIN_SCRATCH_EX1_EX4_KRR_CONJUGATOR_TORSOR_NO_GO_V1"
    assert cert["status"] == "SCRATCH_EXACT_UNAUDITED_BOUNDED_SOURCE_PACKAGE_NO_GO"

    locks = cert["repository_source_locks"]
    gauge = load_locked(locks["marked_gauge_orbit"])
    order8 = load_locked(locks["order8_fixed_line_reentry"])
    deraux = load_locked(locks["deraux_R123_adapter"])

    action = gauge["mod2_W_action"]
    assert action["b3_line_permutation"] == "L1->L3->L2->L1"
    assert action["generated_line_action_order"] == 6
    assert action["transitive_on_nonzero_W_lines"] is True
    assert gauge["residue_conjugation"]["orbit"] == [73,97,235]
    assert gauge["residue_conjugation"]["single_orbit"] is True

    assert order8["retained_order8_representative"]["unique_fixed_W_line"] == "L2"
    assert order8["retained_order8_representative"]["conditional_residue_if_B9_equals_this_marked_element"] == 97
    assert order8["finite_ambiguity"]["delta0inf_image_distribution_over_retained_W_lines"] == {"L1":8,"L2":8,"L3":8}
    assert order8["decision"]["absolute_delta0inf_retained_W_line_identified_now"] is False

    assert deraux["mod2_fixed_line"]["unique_fixed_W_line"] == "L1"
    assert deraux["mod2_fixed_line"]["corresponding_Q602_residue"] == 73
    assert deraux["semantic_boundary"]["curve_B9_to_Deraux_labelled_R123_closed"] is False

    witnesses = cert["explicit_ambiguity_witnesses"]
    assert witnesses["Deraux_labelled_R123"]["unique_fixed_line"] == "L1"
    assert witnesses["Cecotti_plus_r_representative_S_T_inverse"]["unique_fixed_line"] == "L2"
    assert witnesses["conjugate_of_Deraux_R123_by_retained_b3"]["unique_fixed_line"] == "L3"
    assert witnesses["all_three_lines_realized_within_allowed_unmarked_conjugacy"] is True

    # KRR only gives existence of a conjugator g. If H=gGg^{-1}, then gk is
    # another conjugator for every k in G. Coordinate transport H->G changes
    # from g^{-1} to k^{-1}g^{-1}; the retained G-action is transitive on the
    # three nonzero W-lines, so an unmarked conjugator cannot select a line.
    assert cert["decision"]["result"] == "KRR_UNMARKED_CONJUGACY_AND_PERIOD_LATTICE_DATA_CANNOT_SELECT_ABSOLUTE_DELTA0INF_W_LINE"
    assert cert["decision"]["bounded_to_source_package"] is True
    assert cert["decision"]["uniform_EX1_residues_remaining"] == [73,97,235]
    assert cert["decision"]["authority_changed"] is False
    assert cert["decision"]["claim_dag_changed"] is False
    assert cert["decision"]["Q602_excluded"] is False
    assert cert["decision"]["O210_excluded"] is False
    assert cert["decision"]["Stage32_closed"] is False

    print("PASS scratch KRR conjugator-torsor no-go")
    print("unmarked_conjugacy_images=L1,L2,L3 residues=73,97,235")
    print("absolute_line=UNSELECTED authority=SCRATCH_UNAUDITED")


if __name__ == "__main__":
    main()
