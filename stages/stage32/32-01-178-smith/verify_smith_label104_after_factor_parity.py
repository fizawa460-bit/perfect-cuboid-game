#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FACTOR = HERE / "verify_smith_current_factor_parity_reduction.py"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_factor_module():
    spec = importlib.util.spec_from_file_location("s32_smith_factor_parity", FACTOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot import factor parity verifier")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_smith_label104_after_factor_parity.py FACTOR_JSON")
    factor = json.loads(Path(sys.argv[1]).read_text())
    alg = factor["current_observable_algebra"]
    if alg["residual_pair_mass_rank_after_factor_parity"] != 1:
        raise ValueError("factor-parity residual rank regression")
    if [2] not in alg["minimal_group_subsets_0based"]:
        raise ValueError("pair-group index 2 is no longer a one-group completion")

    mod = load_factor_module()
    pair_index = 2
    key = mod.PAIR_KEYS[pair_index]
    labels = sorted(mod.PAIR_EXCEPTIONAL_LABELS[key])
    prefix = set(mod.CURRENT_EXCEPTIONAL_PREFIX)
    known = sorted(set(labels) & prefix)
    missing = sorted(set(labels) - prefix)
    if labels != [101, 102, 103, 104]:
        raise ValueError(f"pair-group 2 label regression: {labels}")
    if known != [101, 102, 103] or missing != [104]:
        raise ValueError(f"current-prefix exposure regression: known={known} missing={missing}")

    body = {
        "schema": "STAGE32_32_01_178_SMITH_LABEL104_AFTER_FACTOR_PARITY_V1",
        "status": "PROVISIONAL_EXACT_DATA_EXPOSURE_REDUCTION_NO_MAIN_CREDIT",
        "source": {
            "factor_parity_canonical": factor["canonical_sha256_without_this_field"],
            "factor_parity_residual_pair_mass_rank": alg["residual_pair_mass_rank_after_factor_parity"],
        },
        "exact_result": {
            "target_pair_group_index_0based": pair_index,
            "target_pair_key": key,
            "target_pair_group_labels": labels,
            "already_stored_current_prefix_labels": known,
            "additional_individual_exceptional_labels_needed_after_factor_parity": missing,
            "minimum_additional_individual_exceptional_pairings_after_factor_parity": 1,
            "label104_alone_materializes_a_complete_remaining_pair_group": True,
            "full_pair_mass_signature_determined_after_factor_parity_and_label104": True,
        },
        "scope": {
            "general_frontier": "requires factor-degree parity plus label104",
            "hurwitz_equality_subfrontier": "factor-degree parity is forced by n1=n2=d/2, so label104 is the only additional individual exceptional pairing needed for the exact pair-mass signature",
            "pruning_count_established": False,
        },
        "credit": {
            "main_pruning_credit": False,
            "n350_producer_registration": False,
            "full178_completion": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_claim": False,
            "merge_authorized": False,
        },
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    print(json.dumps(body, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
