#!/usr/bin/env python3
"""Exact K_c replay with an explicit Testa--Stoll -> Stage32 exceptional ordering adapter.

V8 established the correct historical c-sign matrix lock semantics.  The next
fail-closed wall showed that Testa--Stoll's current `pts` enumeration must not
be identified with the Stage32 all140 exceptional suffix by array index.  This
wrapper identifies each materialized E_pi class by its exact 64-entry pairing
fingerprint against the retained Picard basis and requires a unique match in
the Stage32 all140 pairing matrix before using the V6 all140 value.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from sympy import Matrix

import diagnose_stage32_post1473_kc_pinned_replay_v7 as v7
import diagnose_stage32_post1473_kc_pinned_replay_v8 as v8


def exact_pushforward_with_order_adapter(repo: Path, geo: dict) -> dict:
    witness = json.loads(
        (repo / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json").read_text()
    )
    wb = dict(witness)
    wc = wb.pop("canonical_sha256_without_this_field", None)
    if wc != v7.v6.base.WITNESS_EXPECTED or v7.v6.base.csha(wb) != v7.v6.base.WITNESS_EXPECTED:
        raise ValueError("V6 recovered witness lock moved")
    w = witness["witness"]
    x = [int(a) for a in w["picard_coordinates"]]
    all140 = [int(a) for a in w["all140_pairings"]]
    if v7.v6.base.csha(x) != v7.v6.base.WITNESS_PICARD_EXPECTED:
        raise ValueError("V6 Picard-coordinate hash moved")
    if v7.v6.base.csha(all140) != v7.v6.base.WITNESS_ALL140_EXPECTED:
        raise ValueError("V6 all140-pairing hash moved")

    wall = repo / "stages/stage32/residual-32-01-production/post1473-specific-class-kc-adapter-wall.md"
    if v7.v6.base.git_blob_sha1(wall) != v7.v6.base.KC_WALL_GIT_BLOB_SHA1:
        raise ValueError("K_c theorem wall moved")
    wt = wall.read_text()
    for phrase in (
        "pi^*pi_*C = C + sigma_c(C) + sum_{E in E_pi}(C.E)E",
        "(pi_*C)^2 = P^2 / 2",
        "(pi_*C)^2 >= 0",
        "degree `186/2=93`",
        "Lemma 12's even-degree condition",
    ):
        if phrase not in wt:
            raise ValueError(f"K_c theorem-wall semantic lock moved: {phrase}")

    bundle = v7.v6.base.load_module(
        repo / "stages/stage33/33-07/picard_base_rows_retained.py",
        "stage32_kc_retained_picard_v9",
    ).load()
    gram_rows = [[int(a) for a in row] for row in bundle["picard_gram_64x64"]]
    if bundle.get("upstream_git_blob_sha1") != "0422b69847f2afb97cb7b3ed02ebef91279f61b1":
        raise ValueError("retained Picard upstream blob lock moved")

    sparse_path = repo / "stages/stage33/33-07/retained-picard-base-sparse.json"
    sparse_bundle = json.loads(sparse_path.read_text())
    sparse_body = dict(sparse_bundle)
    sparse_canonical = sparse_body.pop("canonical_sha256", None)
    if sparse_canonical != v7.PICARD_BASE_SPARSE_EXPECTED or v7.v6.base.csha(sparse_body) != v7.PICARD_BASE_SPARSE_EXPECTED:
        raise ValueError("retained Picard sparse-base canonical lock moved")
    gram_object = sparse_bundle.get("objects", {}).get("gram", {})
    if gram_object.get("source_certificate_sha256") != v7.PICARD_GRAM_ROWS_EXPECTED:
        raise ValueError("historical Picard Gram source-certificate lock moved")
    sparse_rows = gram_object.get("matrix_64x64_sparse_rows_1based", [])
    sparse_dense = []
    for row in sparse_rows:
        dense_row = [0] * 64
        for pair in row:
            j1, value = int(pair[0]), int(pair[1])
            dense_row[j1 - 1] = value
        sparse_dense.append(dense_row)
    if sparse_dense != gram_rows:
        raise ValueError("retained sparse Picard Gram no longer matches dense retained Gram")
    gram = Matrix(gram_rows)

    endpoint = json.loads(
        (repo / "stages/stage33/33-07/retained-q256-geometric-sign-endpoint.json").read_text()
    )
    locks = endpoint.get("source_locks", {})
    if endpoint.get("canonical_sha256") != v7.ENDPOINT_EXPECTED:
        raise ValueError("retained geometric-sign endpoint canonical lock moved")
    if locks.get("picard_sign_rows_sha256", {}).get("c") != v8.RETAINED_C_CERTIFICATE_EXPECTED:
        raise ValueError("retained endpoint c-sign certificate lock moved")
    if locks.get("picard_gram_rows_sha256") != v7.PICARD_GRAM_ROWS_EXPECTED:
        raise ValueError("retained endpoint Picard Gram lock moved")

    # Reconstruct the exact Stage32 140x64 pairing matrix used by V6.  Its rows
    # are the authoritative Stage32 all140 labels; no Testa--Stoll array-index
    # equality is assumed here.
    marking = v7.v6.base.load_module(
        repo / "stages/stage33/33-07/stage32_picard_marking_retained.py",
        "stage32_kc_marking_v9",
    ).load()
    adapter_mod = v7.v6.base.load_module(
        repo / "stages/stage32/residual-32-01-production/aut_equivariant_pairing_adapter.py",
        "stage32_kc_all140_adapter_v9",
    )
    adapter = adapter_mod.AutEquivariantPairingAdapter.from_retained(marking, bundle)
    stage32_pairing = adapter.pairing_matrix
    if stage32_pairing.shape != (140, 64):
        raise ValueError("Stage32 retained all140 pairing matrix shape moved")

    epi = [int(j) for j in geo["E_pi_indices_0based"]]
    mat = v7.compact_materialize(repo, epi)
    if mat["testa_stoll_git_blob_sha1"] != locks.get("testa_stoll_git_blob_sha1"):
        raise ValueError("fresh pinned Testa-Stoll blob differs from retained endpoint")
    if mat["sigma_exceptional_permutation_1based"] != geo["sigma_exceptional_1based"]:
        raise ValueError("pinned Magma c-sign permutation disagrees with direct node replay")

    sigma = Matrix(mat["sigma_rows"])
    C = Matrix(x)
    C2 = int((C.T * gram * C)[0, 0])
    if C2 != 758 or int(w["self_intersection"]) != 758:
        raise ValueError(f"V6 C^2 regression: {C2}")
    sigmaC = sigma.T * C
    if sigma.T * sigmaC != C:
        raise ValueError("sigma_c Picard64 failed involution on V6 class")
    sigmaC2 = int((sigmaC.T * gram * sigmaC)[0, 0])
    if sigmaC2 != C2:
        raise ValueError("sigma_c Picard64 failed isometry on V6 class")

    # Identify each fresh E_pi by the exact basis-pairing fingerprint E^T*Gram.
    # Restrict matches to Stage32 exceptional labels 93..140 and require a
    # bijection on the 24 materialized E_pi classes.
    mapping = {}
    used_stage32 = set()
    correction = Matrix.zeros(64, 1)
    terms = []
    for source_j in epi:
        E = Matrix(mat["E_pi_rows"][source_j])
        if int((E.T * gram * E)[0, 0]) != -2:
            raise ValueError(f"E_pi exceptional source index {source_j} ceased to be a (-2)-class")
        if sigma.T * E != E:
            raise ValueError(f"E_pi exceptional source index {source_j} not fixed by full Picard64 sigma_c")
        fingerprint = [int((E.T * gram)[0, k]) for k in range(64)]
        matches = [
            label0 for label0 in range(92, 140)
            if [int(stage32_pairing[label0, k]) for k in range(64)] == fingerprint
        ]
        if len(matches) != 1:
            raise ValueError(
                f"Testa-Stoll E_pi -> Stage32 exceptional fingerprint match count at source {source_j}: {len(matches)}"
            )
        label0 = matches[0]
        if label0 in used_stage32:
            raise ValueError("Testa-Stoll E_pi -> Stage32 exceptional adapter is not injective")
        used_stage32.add(label0)
        mapping[source_j] = label0
        ce = int((C.T * gram * E)[0, 0])
        if ce != all140[label0]:
            raise ValueError(
                f"V6/Stage32 exact exceptional pairing mismatch after fingerprint adapter: source={source_j}, label={label0}, {ce} vs {all140[label0]}"
            )
        correction += ce * E
        terms.append({
            "testa_stoll_exceptional_index_0based": source_j,
            "stage32_all140_index_0based": label0,
            "stage32_exceptional_index_0based": label0 - 92,
            "C_dot_E": ce,
            "basis_pairing_fingerprint_sha256": v7.v6.base.csha(fingerprint),
            "picard_coordinates_sha256": v7.v6.base.csha(v7.v6.base.matrix_vector(E)),
        })
    if len(mapping) != 24 or len(used_stage32) != 24:
        raise ValueError("E_pi ordering adapter cardinality regression")

    P = C + sigmaC + correction
    P2 = int((P.T * gram * P)[0, 0])
    if P2 % 2:
        raise ValueError(f"Lemma11 P^2 not divisible by quotient degree 2: {P2}")
    push2 = P2 // 2
    if push2 % 2:
        raise ValueError(f"K3 pushforward square is not even: {push2}")
    negative = push2 < 0
    mapping_rows = [[src, mapping[src]] for src in sorted(mapping)]

    result = {
        "mode": "EXACT_COMPACT_PINNED_TESTA_STOLL_SIGMA_C_LEMMA11_SINGLE_V6_CLASS_REPLAY_WITH_ORDER_ADAPTER",
        "formula": "P=C+sigma_c(C)+sum_{E in E_pi}(C.E)E=pi^*pi_*C; (pi_*C)^2=P^2/2",
        "source_locks": {
            "v6_witness_canonical_sha256": wc,
            "v6_picard_coordinates_sha256": v7.v6.base.WITNESS_PICARD_EXPECTED,
            "v6_all140_pairings_sha256": v7.v6.base.WITNESS_ALL140_EXPECTED,
            "kc_wall_git_blob_sha1": v7.v6.base.KC_WALL_GIT_BLOB_SHA1,
            "retained_picard_bundle_canonical_sha256": bundle.get("canonical_sha256"),
            "retained_picard_base_sparse_canonical_sha256": sparse_canonical,
            "retained_geometric_sign_endpoint_canonical_sha256": v7.ENDPOINT_EXPECTED,
            "retained_sigma_c_bundle_canonical_sha256": mat.get("retained_sigma_c_bundle_canonical_sha256"),
            "retained_sigma_c_certificate_canonical_sha256": mat.get("retained_sigma_c_certificate_canonical_sha256"),
            "testa_stoll_git_blob_sha1": mat["testa_stoll_git_blob_sha1"],
            "sigma_c_picard64_bare_rows_sha256": mat["sigma_rows_sha256"],
            "picard_gram_source_certificate_sha256": v7.PICARD_GRAM_ROWS_EXPECTED,
            "E_pi_picard64_rows_sha256": mat["E_pi_rows_sha256"],
            "stage32_all140_pairing_adapter_canonical_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "E_pi_order_adapter_sha256": v7.v6.base.csha(mapping_rows),
            "submitted_magma_code_sha256": mat["submitted_code_sha256"],
        },
        "materialization": {
            "source_fetch_attempt": mat["source_fetch_attempt"],
            "magma_request_attempt": mat["magma_request_attempt"],
            "picard_gram_historical_certificate_matches_sparse_retained_source": True,
            "picard_gram_sparse_retained_matches_dense_retained": True,
            "sigma_c_picard64_matches_retained_matrix_literally": True,
            "sigma_c_exceptional_permutation_matches_direct_node_replay": True,
            "E_pi_order_adapter_method": "UNIQUE_EXACT_64_ENTRY_BASIS_PAIRING_FINGERPRINT_MATCH_IN_STAGE32_EXCEPTIONAL_LABELS_93_TO_140",
            "E_pi_order_adapter_injective": True,
            "all_24_E_pi_classes_are_minus2_and_sigma_c_fixed": True,
            "all_24_E_pi_pairings_match_recovered_V6_all140_after_exact_order_adapter": True,
        },
        "C_square": C2,
        "sigma_C_square": sigmaC2,
        "C_dot_sigma_C": int((C.T * gram * sigmaC)[0, 0]),
        "class_sigma_c_invariant": bool(sigmaC == C),
        "sigma_C_picard_coordinates_sha256": v7.v6.base.csha(v7.v6.base.matrix_vector(sigmaC)),
        "E_pi_count": len(epi),
        "E_pi_order_adapter_testastoll_to_stage32_all140_0based": mapping_rows,
        "E_pi_correction_terms": terms,
        "E_pi_correction_picard_coordinates_sha256": v7.v6.base.csha(v7.v6.base.matrix_vector(correction)),
        "E_pi_correction_square": int((correction.T * gram * correction)[0, 0]),
        "C_plus_sigma_C_dot_E_pi_correction": int(((C + sigmaC).T * gram * correction)[0, 0]),
        "P_picard_coordinates_sha256": v7.v6.base.csha(v7.v6.base.matrix_vector(P)),
        "P_square": P2,
        "pi_pushforward_C_square": push2,
        "noninvariant_integral_genus1_carrier_necessary_condition": "(pi_*C)^2>=0",
        "noninvariant_integral_genus1_carrier_excluded_by_negative_square": negative,
        "invariant_curve_case_source_locked_even_degree_obstruction": True,
        "invariant_curve_image_degree": 93,
        "specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies": negative,
        "scope": "SINGLE_V6_SUPPORT47_CLASS_ONLY",
    }
    result["canonical_sha256_without_this_field"] = v7.v6.base.csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tangent", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    v8.install_retained_sigma_c_lock()
    tangent = json.loads(args.tangent.read_text())
    marking = v7.v6.base.load_module(args.marking, "stage32_kc_marking_v9_main").load()
    geo = v7.v6.geometry(tangent, marking)
    repo = Path(__file__).resolve().parents[3]
    kc = exact_pushforward_with_order_adapter(repo, geo)
    cert = {
        "schema": "STAGE32_POST1473_KC_PINNED_REPLAY_V9",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_SIGMA_C_EPI_KC_PUSHFORWARD_REPLAY",
        "geometry": geo,
        "kc_pushforward_replay": kc,
        "three_required_locks": {
            "full_integral_picard64_sigma_c_locked": True,
            "E_pi_exactly_extracted_from_c_zero_nodes": True,
            "lemma11_P_square_over_2_exactly_replayed": True,
        },
        "firewalls": {
            "full178_closed": False,
            "general_low_genus_classification_closed": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = v7.v6.base.csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "success": True,
        "E_pi_count": kc["E_pi_count"],
        "class_sigma_c_invariant": kc["class_sigma_c_invariant"],
        "P_square": kc["P_square"],
        "pi_pushforward_C_square": kc["pi_pushforward_C_square"],
        "specific_class_genus1_excluded": kc["specific_class_integral_genus1_carrier_excluded_if_source_locked_case_split_applies"],
        "order_adapter_sha256": kc["source_locks"]["E_pi_order_adapter_sha256"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
