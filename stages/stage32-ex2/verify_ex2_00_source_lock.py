#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json"
SURFACE = ROOT / "stages/stage29/29-02a/source-lock.md"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
GAP = ROOT / "stages/stage32/residual-32-01-production/post1648ae-v6-carrier-member-source-gap.json"
K140 = ROOT / "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json"
S32 = ROOT / "stages/stage32/MAIN-STATE.json"

BASE = "0134d5f42df5aa290f5514cc48822e80a34d083c"
LOCKS = {
    SURFACE: "2f7dc59bcc14fb89bdd6785074c2362fed0a98b4",
    V6: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    GAP: "989a801badac79d897c981bab70d55f007ac03a3",
    K140: "e0bbe443919d1ec5424bffa84c1c5a79befbdf1e",
    S32: "05e2942b4c893044688f16926b5e9837e59d8e9d",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    for path, expected in LOCKS.items():
        actual = blob(path)
        assert actual == expected, (path, actual, expected)

    c = json.loads(CERT.read_text())
    v6 = json.loads(V6.read_text())
    gap = json.loads(GAP.read_text())
    k140 = json.loads(K140.read_text())
    surface = SURFACE.read_text()

    assert c["schema"] == "STAGE32EX2_EX2_00_V6_SOURCE_LOCK_TARGET_CONTRACT_V1"
    assert c["status"] == "EXACT_SOURCE_LOCK_COMPLETE_PROVISIONAL_NO_MEMBER_CREDIT"
    assert c["base_main_sha"] == BASE

    assert "geometric Picard rank `64`" in surface
    assert "48` isolated `A1` singularities" in surface
    assert "`K^2=16`, `p_g=7`, `q=0`" in surface
    assert "canonical divisor big and nef" in surface
    assert "PROJECTIVE_ENDPOINT_MODEL_MATCH=true" in surface
    assert "COORDINATE_ADAPTER=RENAMING_ONLY" in surface

    target = c["V6_target"]
    assert target["picard_rank"] == 64
    assert target["picard_coordinates"] == v6["witness"]["picard_coordinates"]
    assert target["picard_coordinates_sha256"] == v6["witness"]["picard_coordinates_sha256"]
    assert target["D_square"] == v6["witness"]["self_intersection"] == 758
    assert target["K_dot_D"] == gap["exact_effective_divisor_replay"]["K_dot_C"] == 186
    assert target["arithmetic_genus"] == (target["D_square"] + target["K_dot_D"]) // 2 + 1 == 473
    assert target["required_total_genus_defect_if_integral_genus1"] == 472

    rr = c["riemann_roch_scope"]
    assert rr["chi_O_S"] == 8
    assert rr["K_square"] == 16
    assert rr["K_dot_K_minus_D"] == 16 - 186 == -170
    assert rr["chi_O_D"] == 8 + (758 - 186) // 2 == 294
    assert rr["h0_lower_bound"] == gap["exact_effective_divisor_replay"]["h0_lower_bound"] == 294
    assert rr["h2_O_D"] == 0
    assert rr["effective_divisor_exists_in_V6_class"] is True

    assert k140["exact_reduction"]["v6_retained_picard64_coordinates"] == target["picard_coordinates"]
    known = c["known140_scope"]
    retained = k140["known140_monoid"]
    assert retained["membership"] is True
    assert known["nonzero_term_count"] == retained["nonzero_term_count"] == 61
    assert known["total_multiplicity"] == retained["total_multiplicity"] == 155
    assert known["normal_curve_multiplicity"] == retained["normal_curve_multiplicity"] == 73
    assert known["exceptional_curve_multiplicity"] == retained["exceptional_curve_multiplicity"] == 82
    assert known["this_is_the_fixed_part_of_complete_linear_system"] is False
    assert known["this_spans_complete_H0"] is False

    assert c["ambient_model"]["picard_field_semantics"] == "GEOMETRIC_PICARD_GROUP_OVER_QBAR_CONTEXT"
    assert c["ambient_model"]["V6_class_Q_descent_asserted"] is False
    assert c["ambient_model"]["actual_member_field_asserted"] is False

    adapters = c["representation_adapters"]
    assert adapters["stage29_projective_box_to_testa_stoll_surface"]["status"] == "SOURCE_BOUND"
    assert adapters["retained_picard64_to_known140_class_sum"]["status"] == "SOURCE_BOUND_EXACT_CLASS_EQUALITY"
    for key in [
        "retained_picard64_to_ambient_projective_section",
        "retained_picard64_to_modular_or_theta_form",
        "retained_picard64_to_cox_or_graded_ring_section",
        "retained_picard64_to_ideal_or_syzygy_presentation",
        "geometric_picard_class_to_Q_defined_actual_member",
    ]:
        assert adapters[key]["status"] == "MISSING"
        assert adapters[key]["use_before_adapter"] is False

    assert c["exit"]["EX2_00_source_lock_complete"] is True
    assert c["exit"]["next_leaf"] == "EX2-01_LINE_BUNDLE_REALIZATION_AND_SECTION_SOURCE_INVENTORY"
    assert c["exit"]["parallel_lanes_unlocked"] is True
    assert c["exit"]["claim_dag_sync_triggered"] is True
    assert c["exit"]["claim_dag_sync_trigger"] == "RETAINED_CONSOLIDATION"

    for key, value in c["credit_firewall"].items():
        assert value is False, (key, value)

    print("Stage32EX2 EX2-00 source lock: PASS; retained consolidation triggers claim-DAG sync; no member or Stage32 credit.")


if __name__ == "__main__":
    main()
