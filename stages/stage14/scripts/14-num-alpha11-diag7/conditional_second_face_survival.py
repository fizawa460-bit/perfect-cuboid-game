#!/usr/bin/env python3
from __future__ import annotations

import base64
import bz2
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STAGE13 = ROOT / "stages/stage13/data/13-3/raw_incidence_report.json"
STAGE14 = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"

FACES = ("ab", "ac", "bc")
PAIR_NAMES = ("a", "b", "c")
STAGE13_LIMIT = {
    "ab": 0.5347369332313988,
    "ac": 0.24535917783225203,
    "bc": 0.21990388893634913,
}
PAIR_221 = {"a": 0.4, "b": 0.4, "c": 0.2}
ENDPOINT_433 = {"ab": 0.4, "ac": 0.3, "bc": 0.3}
FINITE_211 = {"ab": 0.5, "ac": 0.25, "bc": 0.25}


def normalize(d):
    s = sum(d.values())
    return {k: d[k] / s for k in d} if s else {k: None for k in d}


def l1(p, q):
    return sum(abs(p[k] - q[k]) for k in p)


def ratio_to_bc(d):
    z = d["bc"]
    if z == 0:
        return {k: None for k in FACES}
    return {k: d[k] / z for k in FACES}


def required_survival_profile(source_distribution):
    raw = {q: ENDPOINT_433[q] / source_distribution[q] for q in FACES}
    return {
        "normalized_shape": normalize(raw),
        "relative_to_bc": ratio_to_bc(raw),
    }


def load_stage14_rows():
    encoded = "".join(STAGE14.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    rows = [tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")) for r in csv.DictReader(io.StringIO(raw))]
    if len(rows) != 3495 or len(set(rows)) != 3495:
        raise ArithmeticError(f"Stage14 B500 source regression failed: {len(rows)}")
    return rows


def stage14_pair_counts(rows, bound):
    out = {"a": 0, "b": 0, "c": 0}
    triple = 0
    for a, b, c, d, mask in rows:
        if d > bound:
            continue
        if mask == 0b011:
            out["a"] += 1
        elif mask == 0b101:
            out["b"] += 1
        elif mask == 0b110:
            out["c"] += 1
        elif mask == 0b111:
            triple += 1
        else:
            raise ArithmeticError(f"unexpected mask in exactly-two source: {mask}")
    return out, triple


def endpoint_load(pair):
    return {
        "ab": pair["a"] + pair["b"],
        "ac": pair["a"] + pair["c"],
        "bc": pair["b"] + pair["c"],
    }


def destination_mix(pair):
    ep = endpoint_load(pair)
    return {
        "from_ab": {
            "to_ac": pair["a"] / ep["ab"] if ep["ab"] else None,
            "to_bc": pair["b"] / ep["ab"] if ep["ab"] else None,
        },
        "from_ac": {
            "to_ab": pair["a"] / ep["ac"] if ep["ac"] else None,
            "to_bc": pair["c"] / ep["ac"] if ep["ac"] else None,
        },
        "from_bc": {
            "to_ab": pair["b"] / ep["bc"] if ep["bc"] else None,
            "to_ac": pair["c"] / ep["bc"] if ep["bc"] else None,
        },
    }


def transition_rates(pair, raw):
    return {
        "ab_to_ac": pair["a"] / raw["ab"],
        "ab_to_bc": pair["b"] / raw["ab"],
        "ac_to_ab": pair["a"] / raw["ac"],
        "ac_to_bc": pair["c"] / raw["ac"],
        "bc_to_ab": pair["b"] / raw["bc"],
        "bc_to_ac": pair["c"] / raw["bc"],
    }


def cumulative_row(r13, rows14):
    B = r13["B"]
    raw = {q: r13["raw_incidence"][q] for q in FACES}
    one = {q: r13["exact_one"][q] for q in FACES}
    pair, t14 = stage14_pair_counts(rows14, B)
    t13 = r13["overlap"]["three_face"]
    from13 = {
        "a": r13["overlap"]["ab_ac"] - t13,
        "b": r13["overlap"]["ab_bc"] - t13,
        "c": r13["overlap"]["ac_bc"] - t13,
    }
    if pair != from13:
        raise ArithmeticError(f"pair cross-source mismatch B={B}: {pair} != {from13}")
    if t13 != 0 or t14 != 0:
        raise ArithmeticError(f"diag7 matched window assumes no triples, found B={B}: {t13},{t14}")

    ep = endpoint_load(pair)
    removed = {q: raw[q] - one[q] for q in FACES}
    if removed != ep:
        raise ArithmeticError(f"raw-exact-one != exact-two endpoint load B={B}: {removed} != {ep}")

    survival = {q: ep[q] / raw[q] for q in FACES}
    survival_shape = normalize(survival)
    return {
        "B": B,
        "raw_face_incidence": raw,
        "exactly_one": one,
        "exactly_two_pair_counts": pair,
        "exactly_two_endpoint_load": ep,
        "raw_face_proportion": normalize(raw),
        "exactly_two_endpoint_proportion": normalize(ep),
        "second_face_survival_rate": survival,
        "second_face_survival_profile_relative_to_bc": ratio_to_bc(survival),
        "second_face_survival_shape": survival_shape,
        "transition_rate_per_raw_source": transition_rates(pair, raw),
        "destination_mix_given_survival": destination_mix(pair),
        "N2": sum(pair.values()),
        "endpoint_incidence_total": sum(ep.values()),
        "endpoint_total_equals_2N2": sum(ep.values()) == 2 * sum(pair.values()),
        "raw_minus_exact_one_equals_endpoint_load": True,
    }


def main():
    s13 = json.loads(STAGE13.read_text(encoding="utf-8"))
    rows13 = s13["rows"]
    rows14 = load_stage14_rows()
    cumulative = [cumulative_row(r, rows14) for r in rows13]

    target_stage13 = required_survival_profile(STAGE13_LIMIT)
    target_finite211 = required_survival_profile(FINITE_211)
    b100 = cumulative[-1]
    b100_shape_l1 = l1(b100["second_face_survival_shape"], target_stage13["normalized_shape"])

    pair500, triple500 = stage14_pair_counts(rows14, 500_000_000)
    if triple500 != 0:
        raise ArithmeticError(f"unexpected B500m triple count: {triple500}")
    ep500 = endpoint_load(pair500)
    pair500_prop = normalize(pair500)
    ep500_prop = normalize(ep500)

    report = {
        "stage": "14-num-alpha11-diag7",
        "classification": "CONDITIONAL_SECOND_FACE_SURVIVAL_AND_ENDPOINT_FLATTENING_DIAGNOSTIC",
        "sources": {
            "stage13_raw_exact_one_overlap_panel": str(STAGE13.relative_to(ROOT)),
            "stage14_exactly_two_B500m": str(STAGE14.relative_to(ROOT)),
        },
        "identity": {
            "pair_axes": "a=ab&ac, b=ab&bc, c=ac&bc",
            "endpoint_load": "E_ab=a+b, E_ac=a+c, E_bc=b+c",
            "matched_window_exact_identity": "A_q-N1_q=E_q because T=0",
            "pair_2_2_1_implies_endpoint_4_3_3": True,
        },
        "conditional_bridge_targets": {
            "if_source_is_finite_2_1_1_and_pair_limit_is_2_2_1": target_finite211,
            "if_source_is_Stage13_theorem_limit_and_pair_limit_is_2_2_1": target_stage13,
            "interpretation": "These are required relative second-face survival profiles, not proved Stage14 limits.",
        },
        "matched_cumulative": cumulative,
        "B100k_snapshot": {
            **b100,
            "survival_shape_L1_to_Stage13_limit_plus_2_2_1_required_profile": b100_shape_l1,
        },
        "B500m_exactly_two_numerator_only": {
            "raw_face_denominators_available": False,
            "pair_counts_a_b_c": pair500,
            "pair_proportion": pair500_prop,
            "pair_L1_to_2_2_1": l1(pair500_prop, PAIR_221),
            "endpoint_load_ab_ac_bc": ep500,
            "endpoint_proportion": ep500_prop,
            "endpoint_L1_to_4_3_3": l1(ep500_prop, ENDPOINT_433),
            "endpoint_ratio_to_bc": ratio_to_bc(ep500),
            "destination_mix_given_survival": destination_mix(pair500),
        },
        "decision": {
            "MATCHED_SECOND_FACE_SURVIVAL_DECOMPOSITION_COMPLETE": True,
            "RAW_MINUS_EXACT_ONE_EQUALS_EXACT_TWO_ENDPOINT_LOAD_AT_EVERY_MATCHED_CUTOFF": True,
            "B100K_AB_SECOND_FACE_SURVIVAL_LOWER_THAN_AC_AND_BC": (
                b100["second_face_survival_rate"]["ab"] < b100["second_face_survival_rate"]["ac"]
                and b100["second_face_survival_rate"]["ab"] < b100["second_face_survival_rate"]["bc"]
            ),
            "PAIR_2_2_1_EQUIVALENT_TO_ENDPOINT_4_3_3": True,
            "B500M_ENDPOINT_MIX_CLOSE_TO_4_3_3": l1(ep500_prop, ENDPOINT_433) < 0.02,
            "B500M_RAW_DENOMINATORS_AVAILABLE": False,
            "ASYMPTOTIC_SECOND_FACE_SURVIVAL_PROFILE_CLAIM": False,
            "ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM": False,
            "NEXT": "Stage14-num-alpha11-diag8 extend the matched raw-face denominator census beyond B=100k before inferring persistence of the conditional survival profile",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
