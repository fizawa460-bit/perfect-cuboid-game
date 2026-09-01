#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp

from pairing_prefix_engine import close_permutation_group


TANGENT_EXPECTED = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
I = sp.I


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load module {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def clean(x):
    return sp.cancel(sp.expand(x))


def is_zero(x) -> bool:
    return clean(x) == 0


def decode_element(v: list[int]):
    if len(v) != 4:
        raise ValueError("Q(i) encoded element shape regression")
    an, ad, bn, bd = (int(x) for x in v)
    if ad == 0 or bd == 0:
        raise ValueError("Q(i) encoded denominator is zero")
    return clean(sp.Rational(an, ad) + I * sp.Rational(bn, bd))


def decode_point(point: list[list[int]]):
    if len(point) != 7:
        raise ValueError("ambient P6 point length regression")
    return tuple(decode_element(v) for v in point)


def projective_normalize(v):
    values = [clean(x) for x in v]
    pivot = next((x for x in values if not is_zero(x)), None)
    if pivot is None:
        raise ValueError("zero projective vector")
    return tuple(clean(x / pivot) for x in values)


def quadrics(v):
    a1, a2, a3, b1, b2, b3, c = v
    return (
        clean(a1 * a1 + a2 * a2 - b3 * b3),
        clean(a2 * a2 + a3 * a3 - b1 * b1),
        clean(a1 * a1 + a3 * a3 - b2 * b2),
        clean(a1 * a1 + a2 * a2 + a3 * a3 - c * c),
    )


def neg_c(v):
    out = list(v)
    out[6] = clean(-out[6])
    return tuple(out)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--tangent", type=Path, required=True)
    p.add_argument("--marking", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    tangent = json.loads(args.tangent.read_text())
    tangent_claimed = tangent.get("canonical_sha256")
    tangent_body = dict(tangent)
    tangent_body.pop("canonical_sha256", None)
    tangent_actual = csha(tangent_body)
    if tangent_claimed != TANGENT_EXPECTED or tangent_actual != TANGENT_EXPECTED:
        raise ValueError(
            f"retained tangent source lock moved: claimed={tangent_claimed} actual={tangent_actual}"
        )

    marking = load_module(args.marking, "stage32_post1473_sigma_c_marking").load()

    models = tangent["exceptional_models"]
    if len(models) != 48 or tangent.get("exceptional_count") != 48:
        raise ValueError("48-exceptional tangent lock regression")
    ids = [m["exceptional_id"] for m in models]
    expected_ids = [f"EXC_{i:03d}" for i in range(1, 49)]
    if ids != expected_ids:
        raise ValueError("exceptional model ordering is not EXC_001..EXC_048")

    # The upstream Stage33 producer constructs p directly in the ambient
    # coordinate order (a1,a2,a3,b1,b2,b3,c) and only *encodes coefficients*
    # in the Q(i) coefficient basis [Re.num, Re.den, Im.num, Im.den].  The old
    # diagnostic incorrectly treated each encoded coefficient as an integer
    # four-vector; in particular encoded zero is [0,1,0,1], not [0,0,0,0].
    encoded_points = [m["node_point_ambient_P6_L_basis"] for m in models]
    points = [decode_point(q) for q in encoded_points]
    normalized_points = [projective_normalize(q) for q in points]
    if len(set(normalized_points)) != 48:
        raise ValueError("retained exceptional nodes are not 48 distinct projective points")
    surface_failures = [
        i for i, q in enumerate(points)
        if any(not is_zero(x) for x in quadrics(q))
    ]
    if surface_failures:
        raise ValueError(f"decoded node escaped ambient cuboid surface: {surface_failures}")

    zero_c = [i for i, q in enumerate(points) if is_zero(q[6])]
    if not zero_c:
        raise ValueError("decoded ambient c=0 exceptional set is empty")

    point_by_normalized = {q: i for i, q in enumerate(normalized_points)}
    sigma_exc = []
    missing = []
    for i, q in enumerate(points):
        target = projective_normalize(neg_c(q))
        j = point_by_normalized.get(target)
        if j is None:
            sigma_exc.append(-1)
            missing.append(i)
        else:
            sigma_exc.append(j)
    if missing:
        raise ValueError(f"ambient c-sign failed to permute retained 48 nodes: {missing}")
    if sorted(sigma_exc) != list(range(48)):
        raise ValueError("ambient c-sign node action is not a permutation")
    if any(sigma_exc[sigma_exc[i]] != i for i in range(48)):
        raise ValueError("ambient c-sign node action is not an involution")
    if any(sigma_exc[i] != i for i in zero_c):
        raise ValueError("ambient c=0 exceptional node is not fixed by c-sign")

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
    for gi, g in enumerate(full_group):
        if len(g) != 140:
            raise ValueError("Aut permutation degree regression")
        if all(g[92 + i] == 92 + sigma_exc[i] for i in range(48)):
            candidates.append({
                "closed_group_index": gi,
                "permutation_1based": [int(x) + 1 for x in g],
                "permutation_sha256": csha([int(x) + 1 for x in g]),
            })
    if len(candidates) != 1:
        raise ValueError(f"retained Aut140 c-sign match is not unique: {len(candidates)}")

    cert = {
        "schema": "STAGE32_POST1473_SIGMA_C_EXCEPTIONAL_REPLAY_V3",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_SIGMA_C_EXCEPTIONAL_REPLAY",
        "mode": "EXACT_QI_DECODE_DIRECT_AMBIENT_C_SIGN_ON_RETAINED_48_NODES_MATCHED_TO_RETAINED_AUT140_LAST48_ORDER",
        "source_locks": {
            "tangent_canonical_sha256": tangent_claimed,
            "tangent_canonical_recomputed": tangent_actual,
            "tangent_producer": "stages/stage33/33-07/certify_exceptional_p1_tangent_coordinates.py",
            "tangent_producer_origin_commit": "8d8a455a02df891d45e9ad36c1e0a93cab3d3812",
            "coefficient_encoding": "[Re.numerator,Re.denominator,Im.numerator,Im.denominator] over Q(i)",
            "marking_canonical_sha256": marking.get("canonical_sha256"),
            "marking_aut_sha256": marking.get("stage32_aut_action_sha256"),
        },
        "coordinate_order": ["a1", "a2", "a3", "b1", "b2", "b3", "c"],
        "decoded_nodes_satisfy_all_four_ambient_quadrics": True,
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
        "direct_projective_node_match_complete": True,
        "sigma_c_exceptional_permutation_0based": sigma_exc,
        "sigma_c_exceptional_permutation_1based": [x + 1 for x in sigma_exc],
        "sigma_c_exceptional_permutation_sha256": csha([x + 1 for x in sigma_exc]),
        "retained_aut_generator_count": len(generators),
        "retained_aut_group_order": len(full_group),
        "aut140_candidates_matching_exceptional_c_sign_count": len(candidates),
        "sigma_c_aut140": candidates[0],
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
        "direct_projective_match_complete": True,
        "aut_candidate_count": len(candidates),
        "sigma_c_aut140_sha256": candidates[0]["permutation_sha256"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
