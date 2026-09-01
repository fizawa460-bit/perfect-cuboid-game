#!/usr/bin/env python3
"""Replay the retained 140-curve pairing and mark each exceptional node by X(8) factor boundary."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_stage32_post21bl_full178_node_mass_census import load_module_payload
from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data

FIRST_FACTOR = (34, 35, 38, 39, 42, 43)
SECOND_FACTOR = (33, 36, 37, 40, 41, 44)
C2_ALL = tuple(range(33, 45))
EXCEPTIONAL = tuple(range(93, 141))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_module_payload(args.retained, "stage32_post1473_support_picard")
    marking = load_module_payload(args.marking, "stage32_post1473_support_marking")
    data = reconstruct_translation_data(marking, bundle)
    pairing = data["adapter"].pairing_matrix
    if pairing.rows != 140 or pairing.cols != 140:
        raise ValueError(f"unexpected pairing shape {pairing.rows}x{pairing.cols}")
    if pairing != pairing.T:
        raise ValueError("retained pairing matrix lost symmetry")

    rows = []
    factor1_counts = {str(k): 0 for k in FIRST_FACTOR}
    factor2_counts = {str(k): 0 for k in SECOND_FACTOR}
    pair_counts = {}

    for exceptional_label in EXCEPTIONAL:
        j = exceptional_label - 1
        c2_hits = [label for label in C2_ALL if int(pairing[label - 1, j]) != 0]
        factor1_hits = [label for label in FIRST_FACTOR if int(pairing[label - 1, j]) != 0]
        factor2_hits = [label for label in SECOND_FACTOR if int(pairing[label - 1, j]) != 0]
        values = {str(label): int(pairing[label - 1, j]) for label in c2_hits}
        if len(c2_hits) != 2 or len(factor1_hits) != 1 or len(factor2_hits) != 1:
            raise ValueError(
                f"exceptional {exceptional_label}: expected one hit from each factor; "
                f"C2={c2_hits}, first={factor1_hits}, second={factor2_hits}"
            )
        if any(v != 1 for v in values.values()):
            raise ValueError(f"exceptional {exceptional_label}: non-unit boundary incidence {values}")

        f1 = factor1_hits[0]
        f2 = factor2_hits[0]
        factor1_counts[str(f1)] += 1
        factor2_counts[str(f2)] += 1
        pair_key = f"{f1}:{f2}"
        pair_counts[pair_key] = pair_counts.get(pair_key, 0) + 1
        rows.append({
            "exceptional_label": exceptional_label,
            "first_factor_boundary_label": f1,
            "second_factor_boundary_label": f2,
        })

    if set(factor1_counts.values()) != {8} or set(factor2_counts.values()) != {8}:
        raise ValueError(f"boundary-node degree regression: {factor1_counts=} {factor2_counts=}")
    if sum(pair_counts.values()) != 48:
        raise ValueError("pair-count total regression")

    out = {
        "schema": "STAGE32_POST1473_X8_MARKED_EXCEPTIONAL_INCIDENCE_REPLAY_V1",
        "status": "PASS",
        "pairing_matrix_symmetric": True,
        "first_factor_labels": list(FIRST_FACTOR),
        "second_factor_labels": list(SECOND_FACTOR),
        "exceptional_labels": [93, 140],
        "rows": rows,
        "first_factor_node_counts": factor1_counts,
        "second_factor_node_counts": factor2_counts,
        "boundary_pair_counts": dict(sorted(pair_counts.items())),
        "firewall": "incidence replay only; no O=188 histogram/theorem/receiver/endpoint credit",
    }
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
