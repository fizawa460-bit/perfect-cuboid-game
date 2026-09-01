#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp
from sympy import Matrix

from aut_equivariant_pairing_adapter import AutEquivariantPairingAdapter
from pairing_prefix_engine import INDLIST, close_permutation_group


TANGENT_EXPECTED = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"
WITNESS_EXPECTED = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
WITNESS_PICARD_EXPECTED = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
WITNESS_ALL140_EXPECTED = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
KC_WALL_GIT_BLOB_SHA1 = "03f07ef74986ac7aede6fc5ab462b41b71435561"
I = sp.I


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


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


def integer_column(v: Matrix, label: str) -> Matrix:
    out = []
    for value in v:
        value = sp.cancel(value)
        if sp.denom(value) != 1:
            raise ValueError(f"{label} escaped integral Picard lattice: {value}")
        out.append(int(value))
    return Matrix(out)


def matrix_vector(v: Matrix) -> list[int]:
    return [int(v[i, 0]) for i in range(v.rows)]


def replay_kc_pushforward(marking: dict, sigma_cert: dict) -> dict:
    here = Path(__file__).resolve().parent
    repo = Path(__file__).resolve().parents[3]
    witness_path = repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
    retained_path = repo / "stages/stage33/33-07/picard_base_rows_retained.py"
    wall_path = here / "post1473-specific-class-kc-adapter-wall.md"

    witness = json.loads(witness_path.read_text())
    claimed = witness.get("canonical_sha256_without_this_field")
    body = dict(witness)
    body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != WITNESS_EXPECTED or actual != WITNESS_EXPECTED:
        raise ValueError(f"V6 recovered witness source lock moved: claimed={claimed} actual={actual}")
    w = witness.get("witness", {})
    x_list = [int(v) for v in w.get("picard_coordinates", [])]
    p_list = [int(v) for v in w.get("all140_pairings", [])]
    if len(x_list) != 64 or len(p_list) != 140:
        raise ValueError("V6 witness vector shape regression")
    if csha(x_list) != WITNESS_PICARD_EXPECTED or w.get("picard_coordinates_sha256") != WITNESS_PICARD_EXPECTED:
        raise ValueError("V6 Picard coordinate hash regression")
    if csha(p_list) != WITNESS_ALL140_EXPECTED or w.get("all140_pairings_sha256") != WITNESS_ALL140_EXPECTED:
        raise ValueError("V6 all140 pairing hash regression")

    if git_blob_sha1(wall_path) != KC_WALL_GIT_BLOB_SHA1:
        raise ValueError("K_c source-lock wall blob moved")
    wall = wall_path.read_text()
    required_wall_strings = (
        "pi^*pi_*C = C + sigma_c(C) + sum_{E in E_pi}(C.E)E",
        "(pi_*C)^2 = P^2 / 2",
        "(pi_*C)^2 >= 0",
        "degree `186/2=93`",
        "Lemma 12's even-degree condition",
    )
    missing = [s for s in required_wall_strings if s not in wall]
    if missing:
        raise ValueError(f"K_c source-lock semantics moved: {missing}")

    bundle = load_module(retained_path, "stage32_post1473_sigma_c_picard_bundle").load()
    gram = Matrix(bundle["picard_gram_64x64"])
    if gram.shape != (64, 64) or gram != gram.T:
        raise ValueError("retained Picard Gram regression")
    adapter = AutEquivariantPairingAdapter.from_retained(marking, bundle)
    A = adapter.pairing_matrix
    if A.shape != (140, 64):
        raise ValueError("all140 pairing adapter shape regression")

    C = Matrix(x_list)
    pairings = Matrix(p_list)
    if A * C != pairings:
        raise ValueError("V6 Picard coordinates do not reproduce retained all140 pairings")
    C2 = sp.cancel((C.T * gram * C)[0, 0])
    if C2 != 758 or int(w.get("self_intersection")) != 758:
        raise ValueError(f"V6/V7 self-intersection regression: {C2}")

    perm1 = sigma_cert["sigma_c_aut140"]["permutation_1based"]
    if len(perm1) != 140:
        raise ValueError("sigma_c Aut140 degree regression")
    g = [int(v) - 1 for v in perm1]
    if sorted(g) != list(range(140)):
        raise ValueError("sigma_c Aut140 action is not a permutation")
    inv = [-1] * 140
    for source, target in enumerate(g):
        inv[target] = source
    if any(v < 0 for v in inv):
        raise ValueError("sigma_c inverse permutation construction failed")
    if any(g[g[i]] != i for i in range(140)):
        raise ValueError("sigma_c Aut140 action is not an involution")

    sigma_pairings = Matrix([int(pairings[inv[j], 0]) for j in range(140)])
    sigma_basis_pairings = Matrix([int(sigma_pairings[label - 1, 0]) for label in INDLIST])
    gram_inv = gram.inv()
    sigma_C = integer_column(gram_inv * sigma_basis_pairings, "sigma_c(C)")
    if A * sigma_C != sigma_pairings:
        raise ValueError("recovered sigma_c(C) Picard64 coordinates fail all140 replay")
    sigma_C2 = sp.cancel((sigma_C.T * gram * sigma_C)[0, 0])
    if sigma_C2 != C2:
        raise ValueError("sigma_c failed exact Picard isometry on C")

    epi = [int(v) for v in sigma_cert["c_zero_exceptional_indices_0based"]]
    if len(epi) != 24 or len(set(epi)) != 24 or any(v < 0 or v >= 48 for v in epi):
        raise ValueError(f"E_pi retained exceptional shape regression: {epi}")
    if any(sigma_cert["sigma_c_exceptional_permutation_0based"][i] != i for i in epi):
        raise ValueError("E_pi node is not fixed by sigma_c")

    correction = Matrix.zeros(64, 1)
    correction_rows = []
    for exceptional_index in epi:
        curve_index = 92 + exceptional_index
        coefficient = int(pairings[curve_index, 0])
        basis_pairings_of_E = A[curve_index, :].T
        E = integer_column(gram_inv * basis_pairings_of_E, f"E_pi[{exceptional_index}]")
        if A[curve_index, :] != (E.T * gram):
            raise ValueError(f"exceptional Picard coordinate reconstruction failed at {exceptional_index}")
        correction += coefficient * E
        correction_rows.append({
            "exceptional_index_0based": exceptional_index,
            "exceptional_id": f"EXC_{exceptional_index + 1:03d}",
            "all140_curve_index_1based": curve_index + 1,
            "C_dot_E": coefficient,
            "picard_coordinates_sha256": csha(matrix_vector(E)),
        })

    P = C + sigma_C + correction
    P2 = sp.cancel((P.T * gram * P)[0, 0])
    if sp.denom(P2) != 1:
        raise ValueError(f"P^2 became nonintegral: {P2}")
    P2 = int(P2)
    push2 = sp.Rational(P2, 2)
    if sp.denom(push2) != 1:
        raise ValueError(f"P^2/2 became nonintegral on K_c: {push2}")
    push2 = int(push2)
    if push2 % 2:
        raise ValueError(f"K3 pushforward square is not even: {push2}")

    C_sigma_C = int((C.T * gram * sigma_C)[0, 0])
    correction2 = int((correction.T * gram * correction)[0, 0])
    base_dot_correction = int(((C + sigma_C).T * gram * correction)[0, 0])
    class_sigma_invariant = sigma_C == C
    noninvariant_excluded = push2 < 0

    result = {
        "mode": "EXACT_TESTA_STOLL_LEMMA11_PUSHFORWARD_SELFINTERSECTION_SINGLE_V6_CLASS",
        "source_locks": {
            "v6_recovered_witness_canonical_sha256": claimed,
            "v6_picard_coordinates_sha256": WITNESS_PICARD_EXPECTED,
            "v6_all140_pairings_sha256": WITNESS_ALL140_EXPECTED,
            "kc_wall_git_blob_sha1": KC_WALL_GIT_BLOB_SHA1,
            "retained_picard_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "all140_pairing_adapter_canonical_sha256": adapter.certificate.get("canonical_sha256_without_this_field"),
            "sigma_c_aut140_permutation_sha256": sigma_cert["sigma_c_aut140"]["permutation_sha256"],
            "E_pi_source": "retained ambient node coordinates with exact c=0",
        },
        "formula": "P=C+sigma_c(C)+sum_{E in E_pi}(C.E)E=pi^*pi_*C; (pi_*C)^2=P^2/2",
        "C_square": int(C2),
        "sigma_C_square": int(sigma_C2),
        "C_dot_sigma_C": C_sigma_C,
        "C_picard_coordinates_sha256": csha(matrix_vector(C)),
        "sigma_C_picard_coordinates": matrix_vector(sigma_C),
        "sigma_C_picard_coordinates_sha256": csha(matrix_vector(sigma_C)),
        "class_sigma_c_invariant": class_sigma_invariant,
        "E_pi_count": len(epi),
        "E_pi_exceptional_indices_0based": epi,
        "E_pi_exceptional_ids": [f"EXC_{i + 1:03d}" for i in epi],
        "E_pi_correction_terms": correction_rows,
        "E_pi_correction_picard_coordinates": matrix_vector(correction),
        "E_pi_correction_picard_coordinates_sha256": csha(matrix_vector(correction)),
        "E_pi_correction_square": correction2,
        "C_plus_sigma_C_dot_E_pi_correction": base_dot_correction,
        "P_picard_coordinates": matrix_vector(P),
        "P_picard_coordinates_sha256": csha(matrix_vector(P)),
        "P_square": P2,
        "pi_pushforward_C_square": push2,
        "noninvariant_integral_genus1_carrier_necessary_condition": "(pi_*C)^2>=0",
        "noninvariant_integral_genus1_carrier_excluded_by_negative_square": noninvariant_excluded,
        "invariant_curve_case_source_locked_even_degree_obstruction": True,
        "invariant_curve_image_degree": 93,
        "specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies": noninvariant_excluded,
        "scope": "SINGLE_V6_SUPPORT47_CLASS_ONLY",
        "firewalls": {
            "full178_closed": False,
            "general_low_genus_classification_closed": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result


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
        "schema": "STAGE32_POST1473_SIGMA_C_EXCEPTIONAL_KC_PUSHFORWARD_REPLAY_V4",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_SIGMA_C_EPI_KC_PUSHFORWARD_REPLAY",
        "mode": "EXACT_QI_DECODE_AMBIENT_C_SIGN_AUT140_PLUS_TESTA_STOLL_LEMMA11_SINGLE_CLASS_REPLAY",
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
    }
    cert["kc_pushforward_replay"] = replay_kc_pushforward(marking, cert)
    cert["firewalls"] = {
        "full178_closed": False,
        "general_low_genus_classification_closed": False,
        "endpoint_credit": False,
        "route_credit": False,
        "theorem_credit": False,
        "perfect_cuboid_nonexistence_claim": False,
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    kc = cert["kc_pushforward_replay"]
    print(json.dumps({
        "success": True,
        "c_zero_count": len(zero_c),
        "aut_candidate_count": len(candidates),
        "sigma_c_aut140_sha256": candidates[0]["permutation_sha256"],
        "class_sigma_c_invariant": kc["class_sigma_c_invariant"],
        "P_square": kc["P_square"],
        "pi_pushforward_C_square": kc["pi_pushforward_C_square"],
        "noninvariant_genus1_excluded": kc["noninvariant_integral_genus1_carrier_excluded_by_negative_square"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
