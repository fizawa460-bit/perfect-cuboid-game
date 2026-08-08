#!/usr/bin/env python3

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
E2_PATH = ROOT / "stages/stage14/data/14-e2/ambient_reconnaissance.json"
E4_PATH = ROOT / "stages/stage14/data/14-e4/directional_tamagawa_audit.json"
MAIN_PATH = ROOT / "stages/stage14/main.md"
OUT_PATH = ROOT / "stages/stage14/data/14-e5/space_filter_comparison_audit.json"


def main() -> None:
    e2 = json.loads(E2_PATH.read_text())
    e4 = json.loads(E4_PATH.read_text())
    main_text = MAIN_PATH.read_text()

    rows = {int(row["B"]): row for row in e2["cutoffs"]}
    row10 = rows[10_000]
    ambient10 = tuple(int(x) for x in row10["exactly_two"])
    assert ambient10 == (12464, 18198, 11004)
    assert int(row10["E2"]) == sum(ambient10) == 41666

    # These values are frozen in the canonical main Stage14 file.
    assert "exactly-two direction                (9,11,5)" in main_text
    assert "(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80)" in main_text
    assert "N_2=356" in main_text
    assert "N_2(B)=o(B(\\log B)^3)" in main_text

    main10 = (9, 11, 5)
    main2m = (142, 134, 80)

    total_ambient10 = sum(ambient10)
    total_main10 = sum(main10)
    survival10 = tuple(main10[i] / ambient10[i] for i in range(3))
    survival_total10 = total_main10 / total_ambient10
    finite_bias10 = tuple(x / survival_total10 for x in survival10)

    p_inf = (
        float(e4["direction_limit"]["a"]),
        float(e4["direction_limit"]["b"]),
        float(e4["direction_limit"]["c"]),
    )
    assert abs(sum(p_inf) - 1.0) < 1e-14

    main2m_prop = tuple(x / sum(main2m) for x in main2m)
    main2m_to_ambient_limit = tuple(main2m_prop[i] / p_inf[i] for i in range(3))

    # Algebraic comparison of theorem scales:
    # numerator = o(B log^3 B), denominator ~ positive * B log^5 B.
    numerator_log_power = 3
    denominator_log_power = 5
    survival_log_power = numerator_log_power - denominator_log_power
    assert survival_log_power == -2

    report = {
        "metadata": {
            "stage": "14-e5",
            "track": "space-diagonal filter comparison",
            "ambient_input": "Stage14-e4",
            "main_input": "Stage13 R03 + Stage14-4af",
        },
        "theorem_scale_comparison": {
            "ambient_directionwise": "E_q(B) ~ Lambda_E*M_q*B*(log B)^5",
            "main_directionwise_upper": "N_q^(2)(B) = o(B*(log B)^3)",
            "ambient_log_power": denominator_log_power,
            "main_imported_log_power": numerator_log_power,
            "survival_conclusion": "N_q^(2)(B)/E_q(B) = o((log B)^-2)",
            "total_survival_conclusion": "N_2(B)/E_2(B) = o((log B)^-2)",
            "survival_log_power_gap": survival_log_power,
        },
        "ambient_direction_limit": {
            "a": p_inf[0],
            "b": p_inf[1],
            "c": p_inf[2],
        },
        "bias_identity": {
            "formula": "p_q^N(B)=p_q^E(B)*S_q(B)/S(B)",
            "direction_neutral_iff": "S_q(B)/S(B)->1 for q=a,b,c",
            "direction_neutrality_proved": False,
        },
        "finite_same_cutoff_B10000": {
            "main_exactly_two": list(main10),
            "ambient_exactly_two": list(ambient10),
            "main_total": total_main10,
            "ambient_total": total_ambient10,
            "direction_survival": list(survival10),
            "total_survival": survival_total10,
            "direction_survival_over_total": list(finite_bias10),
            "use": "finite diagnostic only",
        },
        "finite_main_B2000000_vs_ambient_limit": {
            "main_exactly_two": list(main2m),
            "main_total": sum(main2m),
            "main_direction_proportion": list(main2m_prop),
            "main_proportion_over_ambient_limit": list(main2m_to_ambient_limit),
            "use": "finite diagnostic only; not a same-cutoff survival comparison",
        },
        "geometry": {
            "space_square_cover": "z^2=1+t1^2+t2^2",
            "generic_degree": 2,
            "classification": "thin type II after normalization/resolution",
            "main_stage14_4af_generic_rank": 0,
            "physical_main_hit_requires_positive_rank_specialization": True,
        },
        "status": {
            "STAGE14_E5": "COMPLETE_SPACE_FILTER_COMPARISON",
            "TOTAL_SPACE_FILTER_SURVIVAL": "o(LOG^-2)",
            "DIRECTIONWISE_SPACE_FILTER_SURVIVAL": "o(LOG^-2)",
            "DIRECTION_NEUTRALITY_PROVED": False,
            "MAIN_TRUE_GROWTH_ORDER_PROVED": False,
            "MAIN_DIRECTION_LIMIT_PROVED": False,
            "E_TRACK_CONTROL_EXPERIMENT": "COMPLETE",
        },
        "pass": True,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
