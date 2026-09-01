#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from pairing_prefix_engine import close_permutation_group


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load module {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def neg(v: list[int]) -> list[int]:
    return [-int(x) for x in v]


def neg_c(point: list[list[int]]) -> list[list[int]]:
    if len(point) != 7 or any(len(v) != 4 for v in point):
        raise ValueError("ambient P6/L-basis point shape regression")
    out = [[int(x) for x in v] for v in point]
    out[6] = neg(out[6])
    return out


def pm_equal(a: list[list[int]], b: list[list[int]]) -> bool:
    if a == b:
        return True
    return a == [neg(v) for v in b]


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--tangent", type=Path, required=True)
    p.add_argument("--marking", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    tangent = json.loads(args.tangent.read_text())
    marking = load_module(args.marking, "stage32_post1473_sigma_c_marking").load()

    models = tangent["exceptional_models"]
    if len(models) != 48 or tangent.get("exceptional_count") != 48:
        raise ValueError("48-exceptional tangent lock regression")
    ids = [m["exceptional_id"] for m in models]
    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if ids != expected_ids:
        raise ValueError("exceptional model ordering is not EXC_001..EXC_048")
    points = [m["node_point_ambient_P6_L_basis"] for m in models]

    zero_c = [i for i, q in enumerate(points) if all(int(x) == 0 for x in q[6])]

    sigma_exc = []
    ambiguous = []
    missing = []
    for i, q in enumerate(points):
        target = neg_c(q)
        hits = [j for j, r in enumerate(points) if pm_equal(target, r)]
        if len(hits) == 1:
            sigma_exc.append(hits[0])
        elif len(hits) == 0:
            sigma_exc.append(-1)
            missing.append(i)
        else:
            sigma_exc.append(-1)
            ambiguous.append({"source_0based": i, "hits_0based": hits})

    aut = marking.get("aut_action", {})
    generators = aut.get("permutations_1based", [])
    if not isinstance(generators, list) or not generators:
        raise ValueError("retained marking missing Aut140 generators")
    curve_labels = aut.get("curve_labels")
    exc_payload = marking.get("exceptionals", {})
    exc_labels = exc_payload.get("curve_labels") if isinstance(exc_payload, dict) else None

    full_group = close_permutation_group(generators)
    if len(full_group) != 1536:
        raise ValueError(f"retained Aut group order regression: {len(full_group)}")
    candidates = []
    if not missing and not ambiguous:
        for gi, g in enumerate(full_group):
            if len(g) != 140:
                raise ValueError("Aut permutation degree regression")
            if all(g[92 + i] == 92 + sigma_exc[i] for i in range(48)):
                candidates.append({
                    "closed_group_index": gi,
                    "permutation_1based": [int(x) + 1 for x in g],
                    "permutation_sha256": csha([int(x) + 1 for x in g]),
                })

    cert = {
        "schema": "STAGE32_POST1473_SIGMA_C_EXCEPTIONAL_REPLAY_V2",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_SIGMA_C_EXCEPTIONAL_REPLAY",
        "mode": "DIRECT_C_SIGN_ON_RETAINED_48_NODE_COORDINATES_MATCHED_TO_RETAINED_AUT140_LAST48_ORDER",
        "source_locks": {
            "tangent_canonical_sha256": tangent.get("canonical_sha256"),
            "marking_canonical_sha256": marking.get("canonical_sha256"),
            "marking_aut_sha256": marking.get("stage32_aut_action_sha256"),
        },
        "coordinate_order": ["a1", "a2", "a3", "b1", "b2", "b3", "c"],
        "exceptional_model_order_exact": True,
        "exceptional_model_ids": ids,
        "retained_marking_exceptional_keys": sorted(exc_payload.keys()) if isinstance(exc_payload, dict) else [],
        "retained_aut_keys": sorted(aut.keys()),
        "retained_aut_curve_label_count": len(curve_labels) if isinstance(curve_labels, list) else None,
        "retained_exceptional_curve_label_count": len(exc_labels) if isinstance(exc_labels, list) else None,
        "marking_exceptional_curve_labels": exc_labels,
        "marking_exceptionals_equal_last48_aut_labels": (
            isinstance(exc_labels, list) and isinstance(curve_labels, list) and exc_labels == curve_labels[92:]
        ),
        "last48_order_source_lock": "aut_equivariant_pairing_adapter.py: Stoll source defines 92 known curves followed by 48 exceptional divisors; retained Aut permutations act on that ordered set",
        "c_zero_exceptional_indices_0based": zero_c,
        "c_zero_exceptional_ids": [ids[i] for i in zero_c],
        "c_zero_exceptional_count": len(zero_c),
        "direct_pm_node_match_complete": not missing and not ambiguous,
        "direct_pm_node_match_missing_0based": missing,
        "direct_pm_node_match_ambiguous": ambiguous,
        "sigma_c_exceptional_permutation_0based": sigma_exc if not missing and not ambiguous else None,
        "retained_aut_generator_count": len(generators),
        "retained_aut_group_order": len(full_group),
        "aut140_candidates_matching_exceptional_c_sign_count": len(candidates),
        "aut140_candidates_matching_exceptional_c_sign": candidates,
        "firewalls": {
            "fixed_z_class_excluded": False,
            "integral_irreducible_low_genus_curve_proved": False,
            "endpoint_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "full178_closed": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "success": True,
        "c_zero_count": len(zero_c),
        "direct_pm_complete": cert["direct_pm_node_match_complete"],
        "aut_candidate_count": len(candidates),
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
