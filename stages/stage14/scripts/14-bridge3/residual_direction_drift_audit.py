#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

DIAG4 = ROOT / "stages/stage14/data/14-num-alpha11-diag4/arithmetic_summary.json"
DIAG5 = ROOT / "stages/stage14/data/14-num-alpha11-diag5/cluster_summary.json"
DIAG10 = ROOT / "stages/stage14/data/14-num-alpha11-diag10/finite_count_summary.json"
BRIDGE2 = ROOT / "stages/stage14/data/14-bridge2/p7_row_packet_summary.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    d4 = load(DIAG4)
    d5 = load(DIAG5)
    d10 = load(DIAG10)
    b2 = load(BRIDGE2)

    # Frozen-source regression locks.
    assert d4["source_rows"] == 3495
    assert d5["source_rows"] == 3495
    assert b2["source"]["b500m_rows"] == 3495
    assert d4["global_direction_counts"] == {"a": 1374, "b": 1371, "c": 750}
    assert d5["global_direction_counts"] == {"a": 1374, "b": 1371, "c": 750}

    # Arithmetic mixtures do not reconstruct the observed late-shell jump.
    mix = d4["late_shell_mixture"]
    assert mix["fully_explained_by_tested_class_mixture"] is False
    assert mix["best_mixture_explained_fraction_l2"] < 0.05

    # Same-d and primitive-face graph reweighting do not attenuate the jump.
    same_d_ratio = d5["same_diagonal"]["late_equal_group_to_object_shift_l2_ratio"]
    comp_ratio = d5["face_graph_component"]["late_equal_group_to_object_shift_l2_ratio"]
    assert same_d_ratio > 1.0
    assert comp_ratio > 1.0
    assert d5["decision"]["LATE_SHIFT_MATERIALLY_ATTENUATED_BY_EQUAL_DIAGONAL_WEIGHTING_RATIO_LE_0P75"] is False
    assert d5["decision"]["LATE_SHIFT_MATERIALLY_ATTENUATED_BY_EQUAL_FACE_COMPONENT_WEIGHTING_RATIO_LE_0P75"] is False

    # But after shell-size calibration, the residual movement is compatible with finite-count noise.
    cp = d10["conditional_permutation"]["mc_p"]
    sp = d10["source_adjusted_plugin_mc"]["mc_p"]
    assert cp["pearson"] > 0.05
    assert cp["g"] > 0.05
    assert cp["max_pair_l1"] > 0.05
    assert cp["survival_shape_rms_N2_weighted"] > 0.05
    assert sp["survival_shape_rms_N2_weighted"] > 0.05
    assert d10["decision"]["FINITE_COUNT_SAMPLING_NOISE_SUFFICIENT_EXPLANATION_AT_CURRENT_B1M_PANEL"] is True
    assert d10["decision"]["ARITHMETIC_SHELL_HETEROGENEITY_DETECTED"] is False

    # p=7 remains a real finite direction-associated packet, but bridge2 itself explicitly
    # does not claim that its row-packet mixture explains the direction bias.
    p7_rates = {q: b2["by_direction"][q]["shared7_rate"] for q in ("a", "b", "c")}
    assert p7_rates["a"] < p7_rates["b"]
    assert p7_rates["a"] < p7_rates["c"]
    assert b2["boundary"]["row_packet_mixture_explains_direction_bias_proved"] is False

    report = {
        "stage": "14-bridge3",
        "classification": "RESIDUAL_DIRECTION_DRIFT_CONTROL_GATE_AND_BRIDGE_CLOSURE",
        "sources": {
            "diag4": "merged arithmetic/local partition control",
            "diag5": "merged same-diagonal and graph-component dependence control",
            "diag10": "merged finite-count shell heterogeneity calibration",
            "bridge2": "merged p=7 local-row packet translation",
        },
        "frozen_numbers": {
            "diag4_observed_late_shift_l2": mix["observed_shift_l2"],
            "diag4_best_known_mixture_explained_fraction_l2": mix["best_mixture_explained_fraction_l2"],
            "same_d_equal_weight_shift_ratio": same_d_ratio,
            "face_component_equal_weight_shift_ratio": comp_ratio,
            "diag10_conditional_pearson_p": cp["pearson"],
            "diag10_conditional_max_pair_l1_p": cp["max_pair_l1"],
            "diag10_conditional_survival_rms_p": cp["survival_shape_rms_N2_weighted"],
            "p7_shared_rates_abc": [p7_rates[q] for q in ("a", "b", "c")],
        },
        "evidence_gate": {
            "RAW_LATE_SHIFT_EXACT_FINITE": True,
            "KNOWN_ARITHMETIC_MIXTURE_EXPLAINS_LATE_SHIFT": False,
            "SAME_DIAGONAL_DEPENDENCE_EXPLAINS_LATE_SHIFT": False,
            "GRAPH_COMPONENT_DEPENDENCE_EXPLAINS_LATE_SHIFT": False,
            "RESIDUAL_SHELL_DRIFT_EXCEEDS_FINITE_COUNT_NOISE_AT_5PCT": False,
            "RESIDUAL_SHELL_DRIFT_PROMOTED_TO_L2": False,
            "NEW_EXACT_PARAMETER_INVARIANT_ISOLATED": False,
            "NEW_PROOF_RECEIVER_REQUIRED": False,
        },
        "routing": {
            "stable_cumulative_second_face_ordering": "already owned by Stage14-bridge1 / Stage14-4 chamber-local-density diagnostic",
            "stable_p7_direction_association": "already owned by Stage14-bridge2 row-packet test",
            "late_shell_residual": "finite diagnostic only; no new theorem-side handoff",
            "conditional_future_receiver": "Stage14-4 / Stage14-s6 chamber-conditioned global-small-point witness count, only after a new merged control-surviving trigger",
        },
        "decision": {
            "STAGE14_BRIDGE3_COMPLETE": True,
            "DURABLE_NO_NEW_MECHANISM_YET_CLOSURE": True,
            "BRIDGE_SEQUENCE_PARKED": True,
            "BRIDGE4_PREEMPTIVELY_CREATED": False,
            "ASYMPTOTIC_DIRECTION_CLAIM": False,
            "FINITE_ZERO_NONEXISTENCE_CLAIM": False,
            "NEXT": "NONE_UNTIL_NEW_MERGED_CONTROL_SURVIVING_DIRECTIONAL_OR_FAMILY_TRIGGER",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
