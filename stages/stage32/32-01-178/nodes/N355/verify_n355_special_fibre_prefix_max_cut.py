#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
N230 = HERE.parent / "N230"
N345_PATH = HERE.parent / "N345/verify_n345_kernel14_integral_self_square.py"
CONTRACT = HERE / "SPECIAL_FIBRE_PREFIX_MAX_CUT_CONTRACT.md"
N351_CONTRACT = HERE.parent / "N351/GENERAL_FACTOR_HURWITZ_MASS_CAP_CONTRACT.md"
N352_CONTRACT = HERE.parent / "N352/DEGREE_SUM_SCALAR_HURWITZ_CONTRACT.md"
N354_RECEIPT = HERE.parent / "N354/HOSTILE-AUDIT-PASS.json"

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(N230))
from compressed_terminal_family import terminal_predicate
from n220_filtered_terminal_indexer import N220FilteredTerminalIndexer

EXPECTED_CONTRACT_BLOB = "8a20e8f02c36907e0d3370d1cbd5250b86440932"
EXPECTED_N351_BLOB = "377c2c43b3c80644c5913586cee42e9a6ec1138d"
EXPECTED_N352_BLOB = "60295a86297330d83370cf32016c75a8244a2aa4"
EXPECTED_N354_RECEIPT_BLOB = "0394b088349780b6cddf7bcb9d207b3889679e1e"
EXPECTED_N354_REVIEW = 5164850548
EXPECTED_N354_HEAD = "e82a1d2ae6ed3693e5e5e81adfd95b83a6c317b6"
EXPECTED_BUNDLE = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
BOUNDARY_PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
KNOWN_EXCEPTIONAL = [x for x in ASSIGNMENT_LABELS if x != 49]
WITNESS = (0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 1)


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def row_sum(coords: Matrix, labels) -> Matrix:
    out = Matrix.zeros(1, coords.cols)
    for label in labels:
        out += coords.row(label - 1)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    for path, expected in [
        (CONTRACT, EXPECTED_CONTRACT_BLOB),
        (N351_CONTRACT, EXPECTED_N351_BLOB),
        (N352_CONTRACT, EXPECTED_N352_BLOB),
        (N354_RECEIPT, EXPECTED_N354_RECEIPT_BLOB),
    ]:
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual} != {expected}")

    receipt = json.loads(N354_RECEIPT.read_text())
    if receipt["status"] != "PASS" or receipt["review_id"] != EXPECTED_N354_REVIEW:
        raise ValueError("N354 hostile-audit receipt regression")
    if receipt["audited_exact_head"] != EXPECTED_N354_HEAD:
        raise ValueError("N354 audited exact-head regression")
    if receipt["consumed_counts"]["remaining_strata"] != 17128:
        raise ValueError("N354 survivor-strata regression")
    if receipt["consumed_counts"]["remaining_terminals"] != 38560956534397137634780102:
        raise ValueError("N354 survivor-terminal regression")

    n345 = load_module(N345_PATH, "s32_n355_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n355_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n355_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE:
        raise ValueError("retained Picard bundle regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise ValueError("retained marking regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    pack_data = []
    membership = {label: [] for label in KNOWN_EXCEPTIONAL}
    for factor_index, pack in enumerate(BOUNDARY_PACKS, start=1):
        seen = []
        blocks = []
        fibre_class = None
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"boundary incidence regression label={boundary}")
            seen.extend(inc)
            known = [j for j in inc if j in KNOWN_EXCEPTIONAL]
            for label in known:
                membership[label].append((factor_index, boundary))
            F = 2 * coords.row(boundary - 1) + row_sum(coords, inc)
            if fibre_class is None:
                fibre_class = F
            elif F != fibre_class:
                raise ValueError(f"factor {factor_index} fibre-class regression")
            blocks.append({"boundary_label": boundary, "exceptional_labels": inc, "known_prefix_labels": known})
        if sorted(seen) != list(range(93, 141)):
            raise ValueError(f"factor {factor_index} exceptional partition regression")
        pack_data.append({"factor": factor_index, "boundary_pack": pack, "blocks": blocks})

    for label, memberships in membership.items():
        if len(memberships) != 2 or {x[0] for x in memberships} != {1, 2}:
            raise ValueError(f"known exceptional membership regression label={label}: {memberships}")

    label_to_value = {label: WITNESS[pos] for pos, label in enumerate(ASSIGNMENT_LABELS)}
    factor_maxima = []
    factor_partial_sums = []
    for pdata in pack_data:
        sums = []
        for block in pdata["blocks"]:
            sums.append(sum(label_to_value[label] for label in block["known_prefix_labels"]))
        factor_partial_sums.append(sums)
        factor_maxima.append(max(sums))

    genus, degree, e = 0, 8, 12
    n354_pass = (e % 2 == 0) and (2 * ((e + 5) // 6) <= degree <= e + 4 * genus - 4)
    base_pass = terminal_predicate(WITNESS, e=e, d=degree)
    filtered = N220FilteredTerminalIndexer(genus, degree, e)
    n220_pass = filtered.accepts(WITNESS)
    filtered_rank = filtered.rank(WITNESS)
    diagonal_failure = label_to_value[99] > degree // 2
    max_cut_failure = sum(factor_maxima) > degree
    if not (n354_pass and base_pass and n220_pass and diagonal_failure and max_cut_failure):
        raise ValueError("strictness witness regression")

    result = {
        "schema": "STAGE32_32_01_178_N355_SPECIAL_FIBRE_PREFIX_MAX_CUT_PREFLIGHT_V1",
        "node_id": "N355",
        "status": "AUDIT_CANDIDATE_PREFIX_NECESSARY_CUT_NO_GLOBAL_CENSUS",
        "source_locks": {
            "contract_blob_sha1": EXPECTED_CONTRACT_BLOB,
            "n351_contract_blob_sha1": EXPECTED_N351_BLOB,
            "n352_contract_blob_sha1": EXPECTED_N352_BLOB,
            "n354_audit_receipt_blob_sha1": EXPECTED_N354_RECEIPT_BLOB,
            "n354_audit_review_id": EXPECTED_N354_REVIEW,
            "n354_audited_exact_head": EXPECTED_N354_HEAD,
            "retained_bundle_canonical": EXPECTED_BUNDLE,
            "retained_marking_canonical": EXPECTED_MARKING,
        },
        "current_authority": {
            "post_n354_strata": 17128,
            "post_n354_terminals": 38560956534397137634780102,
            "full178_complete": False,
        },
        "terminal_prefix": {
            "assignment_labels": ASSIGNMENT_LABELS,
            "known_exceptional_labels": KNOWN_EXCEPTIONAL,
            "normal_label": 49,
        },
        "fibre_geometry": {
            "boundary_packs": BOUNDARY_PACKS,
            "pack_data": pack_data,
            "every_known_exceptional_has_one_block_per_factor": True,
        },
        "necessary_cut": {
            "per_fibre_identity": "n_i=2*q_i,b+e_i,b",
            "q_nonnegative": True,
            "partial_block_bound": "s_i,b<=e_i,b<=n_i",
            "factor_max_definition": "A_i=max_b(s_i,b)",
            "degree_sum_input": "n1+n2=d",
            "max_cut": "A1+A2<=d",
            "equivalent_pairwise_cut": "s_1,b+s_2,c<=d for all 36 block pairs",
            "diagonal_consequence": "known exceptional pairing x_j<=floor(d/2) for each of 10 known exceptional labels",
        },
        "strictness_witness": {
            "genus": genus,
            "degree": degree,
            "e": e,
            "values": list(WITNESS),
            "base_terminal_pass": base_pass,
            "n220_pass": n220_pass,
            "n220_filtered_rank": filtered_rank,
            "n354_scalar_pass": n354_pass,
            "known_label_99_value": label_to_value[99],
            "diagonal_limit": degree // 2,
            "factor_partial_sums": factor_partial_sums,
            "factor_maxima": factor_maxima,
            "maxima_sum": sum(factor_maxima),
            "n355_reject": True,
        },
        "semantics": {
            "strictly_stronger_than_n354_at_terminal_prefix_level": True,
            "exact_global_rejected_terminal_count_known": False,
            "authoritative_n354_aggregate_unchanged": True,
            "main_pruning_count_credit": False,
            "n350_producer_registered": False,
            "heavy_compute_authorized": False,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N355_SPECIAL_FIBRE_PREFIX_MAX_CUT_PREFLIGHT",
        "canonical": result["canonical_sha256_without_this_field"],
        "known_membership": {str(k): v for k, v in sorted(membership.items())},
        "witness_factor_maxima": factor_maxima,
        "witness_filtered_rank": filtered_rank,
        "main_pruning_count_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
