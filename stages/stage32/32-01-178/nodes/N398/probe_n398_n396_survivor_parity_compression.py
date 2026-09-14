#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

WIDTH = 113
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
FIXED_LABELS = [label for label in ASSIGNMENT_ORDER if label != 49]
X49_POSITION = ASSIGNMENT_ORDER.index(49)

N397_AUDIT_BLOB = "6855397e01b3ab7f85375bbd14acffea3f2970bc"
N397_AUDIT_CANONICAL = "c39d19dcfb71435c4529a0c807469ba046b214e56de8307228111191c0a77d01"
N397_AUDIT_REVIEW = 5195892621
N396_RESULT_BLOB = "971f1665c8be4c22eef549020046dd0830028dff"
N396_RESULT_CANONICAL = "e34e23e2b17063c2f51d9862af1c2a958002fdb0327e43b5e52d85bcb1a83cd1"
N396_PROBE_BLOB = "4db03f296183c6655fafa9bdb5418dd82a17a733"
N394_PROBE_BLOB = "042bb940a6c586092f6b31312d3b16551e566a58"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"
INTERFACE_BLOB = "8a30e3aa30777460f344eb19836dc725dd442329"
INTERFACE_CANONICAL = "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6"
PAIRING_PREFIX_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
PICARD_BUNDLE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
PICARD_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def checked(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing source: {path}")
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected_canonical and csha(body) == expected_canonical, f"canonical drift: {path}")
    return obj


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def stream_sha(values: list[int]) -> str:
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def row_stream_sha(rows: list[list[int]]) -> str:
    return hashlib.sha256("".join(",".join(map(str, row)) + "\n" for row in rows).encode()).hexdigest()


def hnf_contains(H: Matrix, b: Matrix) -> bool:
    n = H.rows
    req(H.cols == n and b.rows == n and b.cols == 1, "HNF shape drift")
    y = [0] * n
    for i in range(n - 1, -1, -1):
        rhs = int(b[i, 0]) - sum(int(H[i, j]) * y[j] for j in range(i + 1, n))
        diag = int(H[i, i])
        req(diag > 0, f"non-positive HNF diagonal at {i}")
        if rhs % diag:
            return False
        y[i] = rhs // diag
    return True


def min_affine_rule(features: list[list[int]], targets: list[int]) -> list[int] | None:
    n = len(features[0]) + 1
    req(n <= 16, "affine feature count unexpectedly large")
    best = None
    for mask in range(1 << n):
        coeff = [(mask >> i) & 1 for i in range(n)]
        if all((coeff[0] ^ sum(c & x for c, x in zip(coeff[1:], row)) % 2) == target for row, target in zip(features, targets)):
            if best is None or (sum(coeff), coeff) < (sum(best), best):
                best = coeff
    return best


def gf2_rowspace_basis(rows: list[list[int]], probe394) -> list[list[int]]:
    if not rows:
        return []
    rref, pivots = probe394.rref_mod(rows, 2)
    return [list(map(int, row)) for row in rref[: len(pivots)]]


def rowspace_vectors(basis: list[list[int]]) -> list[list[int]]:
    req(len(basis) <= 16, "unexpected GF2 relation rank")
    width = len(basis[0]) if basis else len(ASSIGNMENT_ORDER)
    out = []
    for mask in range(1 << len(basis)):
        row = [0] * width
        for i, b in enumerate(basis):
            if (mask >> i) & 1:
                row = [x ^ y for x, y in zip(row, b)]
        out.append(row)
    return out


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    residual = repo / "stages/stage32/residual-32-01-production"
    bundle_dir = repo / "stages/stage33/33-07"
    n394 = repo / "stages/stage32/32-01-178/nodes/N394"
    n396 = repo / "stages/stage32/32-01-178/nodes/N396"
    n397 = repo / "stages/stage32/32-01-178/nodes/N397"

    audit397 = checked(n397 / "AUDIT-PASS.json", N397_AUDIT_BLOB, N397_AUDIT_CANONICAL)
    req(audit397["hostile_audit_verdict"] == "PASS", "N397 hostile audit drift")
    req(int(audit397["hostile_audit_review_id"]) == N397_AUDIT_REVIEW, "N397 review drift")
    req(audit397["continuation"]["allowed"] is True, "N397 continuation closed")
    req(audit397["continuation"]["main_authority_subtraction_owned_by_178"] is False, "N397 ownership firewall drift")

    result396 = checked(n396 / "RESULT.json", N396_RESULT_BLOB, N396_RESULT_CANONICAL)
    req(blob(n396 / "probe_n396_n395_picard64_mod8_completion.py") == N396_PROBE_BLOB, "N396 probe drift")
    req(result396["completion_result"]["sat_terminal_count"] == 5459, "N396 SAT count drift")
    req(result396["completion_result"]["unsat_terminal_count"] == 5502, "N396 UNSAT count drift")
    req(result396["completion_result"]["allowed_x49_residue_mask_distribution"] == {"0x55": 27, "0xaa": 70}, "N396 masks drift")

    probe394_path = n394 / "probe_n394_cross_mass_affine_structure.py"
    req(blob(probe394_path) == N394_PROBE_BLOB, "N394 probe drift")
    probe394 = load_module(probe394_path, "n398_n394_probe")
    req(list(probe394.ASSIGNMENT_ORDER) == ASSIGNMENT_ORDER, "N394 assignment drift")
    req(list(probe394.FIXED_LABELS) == FIXED_LABELS, "N394 fixed-label drift")
    n391 = probe394.checked(
        repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json",
        probe394.EXPECTED["n391_result_blob"], probe394.EXPECTED["n391_result_canonical"],
    )

    idx_path = residual / "compressed_terminal_indexer.py"
    req(blob(idx_path) == INDEXER_BLOB, "compressed indexer drift")
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer
    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "terminal width drift")

    blocks = [int(b) for wave in probe394.WAVES for b in n391["waves"][wave]["residual_blocks"]]
    req(len(blocks) == 97 and len(set(blocks)) == 97, "N391 block union drift")

    interface_path = repo / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
    interface = checked(interface_path, INTERFACE_BLOB, INTERFACE_CANONICAL)
    tmap = interface["terminal_to_picard64_map"]
    req(tmap["terminal_assignment_labels_1based"] == ASSIGNMENT_ORDER, "Picard terminal labels drift")
    req(tmap["inverse_denominator"] == 8, "Picard denominator drift")

    prefix_path = residual / "pairing_prefix_engine.py"
    bundle_path = bundle_dir / "picard_base_rows_retained.py"
    req(blob(prefix_path) == PAIRING_PREFIX_BLOB, "pairing-prefix drift")
    req(blob(bundle_path) == PICARD_BUNDLE_BLOB, "Picard bundle drift")
    sys.path.insert(0, str(bundle_dir))
    from pairing_prefix_engine import RetainedBasisPairingTransform
    import picard_base_rows_retained as retained_bundle
    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == PICARD_BUNDLE_CANONICAL, "Picard bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    req(labels == tmap["selected_pairing_coordinate_order_1based"], "selected64 labels drift")
    req(int(transform.den) == 8, "selected64 denominator drift")

    fixed_positions = [labels.index(label) for label in ASSIGNMENT_ORDER]
    free_positions = [i for i in range(64) if i not in fixed_positions]
    B = transform.inverse_integer
    B_fixed = B.extract(list(range(64)), fixed_positions)
    B_free = B.extract(list(range(64)), free_positions)
    req(csha(matrix_list(B_fixed)) == tmap["terminal_fixed_coefficient_matrix_sha256"], "B_fixed drift")
    req(csha(matrix_list(B_free)) == tmap["free_completion_coefficient_matrix_sha256"], "B_free drift")
    H = hermite_normal_form(B_free.row_join(8 * Matrix.eye(64)))
    req(H.shape == (64, 64), "HNF shape drift")
    req(csha(matrix_list(H)) == result396["completion_lattice"]["hnf_sha256"], "N396 HNF drift")

    # Diagnostic: relations visible already after direct mod-2 reduction of the free image.
    bfree_t_mod2 = [[int(B_free[i, j]) & 1 for i in range(64)] for j in range(B_free.cols)]
    left_null = probe394.nullspace_mod(bfree_t_mod2, 2)
    induced_rows = []
    for y in left_null:
        row = [sum((y[i] & 1) * (int(B_fixed[i, j]) & 1) for i in range(64)) & 1 for j in range(11)]
        if any(row):
            induced_rows.append(row)
    direct_basis = gf2_rowspace_basis(induced_rows, probe394)

    features, parities, masks, status_rows = [], [], [], []
    mask_distribution = Counter()
    for block in blocks:
        base = list(map(int, idx.unrank(block * WIDTH)))
        req(base[X49_POSITION] == 0 and idx.rank(tuple(base)) == block * WIDTH, f"block base drift {block}")
        features.append([base[i] & 1 for i in range(11) if i != X49_POSITION])
        statuses = []
        for residue in range(8):
            x = list(base)
            x[X49_POSITION] = residue
            statuses.append(1 if hnf_contains(H, -(B_fixed * Matrix(x))) else 0)
        mask = sum((1 << r) for r, sat in enumerate(statuses) if sat)
        req(mask in (0x55, 0xAA), f"non-parity N396 replay mask block={block}: 0x{mask:02x}")
        parity = 0 if mask == 0x55 else 1
        req(all(bool(statuses[r]) == ((r & 1) == parity) for r in range(8)), f"parity replay drift block={block}")
        parities.append(parity)
        masks.append(mask)
        status_rows.append(statuses)
        mask_distribution[mask] += 1
    req(mask_distribution == Counter({0x55: 27, 0xAA: 70}), "N396 mask distribution replay drift")

    rule = min_affine_rule(features, parities)
    direct_relation = None
    if direct_basis:
        candidates = []
        for relation in rowspace_vectors(direct_basis):
            if relation[X49_POSITION] != 1:
                continue
            ok = True
            for block, target in zip(blocks, parities):
                base = list(map(int, idx.unrank(block * WIDTH)))
                predicted = sum((relation[i] & 1) * (base[i] & 1) for i in range(11) if i != X49_POSITION) & 1
                if predicted != target:
                    ok = False
                    break
            if ok:
                candidates.append(relation)
        if candidates:
            direct_relation = min(candidates, key=lambda row: (sum(row), row))

    sat_count = sum(57 if p == 0 else 56 for p in parities)
    unsat_count = 97 * WIDTH - sat_count
    req((sat_count, unsat_count) == (5459, 5502), "N396 parity-count reconstruction drift")

    verified_affine = rule is not None
    if verified_affine:
        for row, target in zip(features, parities):
            pred = rule[0] ^ (sum(c & x for c, x in zip(rule[1:], row)) & 1)
            req(pred == target, "affine rule replay drift")

    feature_names = ["const"] + FIXED_LABELS
    payload = {
        "semantics": "EXACT_BOUNDED_N396_97_BLOCK_X49_PARITY_REPLAY_AND_AFFINE_COMPRESSION_TEST; NO_NEW_PRUNING_OR_MAIN_CREDIT",
        "source": {
            "n397_hostile_audit_review_id": N397_AUDIT_REVIEW,
            "n397_audit_blob_sha1": N397_AUDIT_BLOB,
            "n397_audit_canonical_sha256": N397_AUDIT_CANONICAL,
            "n396_result_blob_sha1": N396_RESULT_BLOB,
            "n396_result_canonical_sha256": N396_RESULT_CANONICAL,
            "n396_probe_blob_sha1": N396_PROBE_BLOB,
        },
        "scope": {"row_id": "g1-d008", "g": 1, "d": 8, "e": 8, "block_count": 97, "block_width": WIDTH, "source_terminal_count": 10961, "n396_survivor_terminal_count": 5459, "n396_rejected_terminal_count": 5502},
        "exact_parity_replay": {
            "allowed_mask_distribution": {"0x55": mask_distribution[0x55], "0xaa": mask_distribution[0xAA]},
            "even_required_block_count": parities.count(0), "odd_required_block_count": parities.count(1),
            "block_stream_sha256": stream_sha(blocks), "required_parity_stream_sha256": stream_sha(parities),
            "mask_stream_sha256": stream_sha(masks), "status_97x8_stream_sha256": row_stream_sha(status_rows),
            "sat_count_reconstructed_from_parity": sat_count, "unsat_count_reconstructed_from_parity": unsat_count,
        },
        "affine_parity_compression": {
            "verified": verified_affine,
            "feature_coordinate_order": feature_names,
            "minimum_hamming_then_lexicographic_coefficients_gf2": rule,
            "active_terms": [feature_names[i] for i, c in enumerate(rule or []) if c],
            "compressed_family_count": 97 if verified_affine else None,
            "interpretation": "If verified, the unique N396-allowed x49 parity on every retained block is one affine GF(2) functional of the other ten fixed N394 signature coordinates.",
        },
        "direct_free_image_mod2_diagnostic": {
            "left_nullspace_dimension": len(left_null), "induced_fixed_relation_rank": len(direct_basis),
            "has_direct_relation_matching_all_97_exact_parities": direct_relation is not None,
            "minimum_matching_relation_coefficients_in_assignment_order": direct_relation,
            "assignment_order": ASSIGNMENT_ORDER,
            "scope_note": "Diagnostic only: higher 2-adic lifting constraints may create parity restrictions invisible in the naive mod-2 reduction.",
        },
        "route_control": {
            "outcome": "N396_SURVIVOR_AFFINE_PARITY_COMPRESSION_CANDIDATE" if verified_affine else "N396_PARITY_REPLAY_VERIFIED_NO_AFFINE_GF2_COMPRESSION",
            "additional_pruning_terminals": 0, "main_authority_subtraction_performed": False,
            "next_gate": "HOSTILE_AUDIT_N398_N396_SURVIVOR_PARITY_COMPRESSION" if verified_affine else "STOP_N398_AFFINE_AXIS_OR_REQUIRE_NEW_2ADIC_FEATURE_MECHANISM",
            "freeze": "Do not repeat the same 97x8 parity census without a stronger transport or new independent obstruction on the 5,459 survivors.",
        },
        "credit_firewall": {
            "bounded_terminal_family_compression_candidate": verified_affine, "numerical_leaf_compression_credit": False,
            "additional_pruning_credit": False, "main_pruning_credit": False, "full178_complete": False,
            "integral_carrier_obstruction_promoted": False, "effectivity_final": False, "receiver_credit": False,
            "theorem_credit": False, "endpoint_credit": False, "stage32_closed": False,
            "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False,
            "heavy_compute_authorized": False, "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    print("PASS_N398_N396_SURVIVOR_PARITY_COMPRESSION_PROBE")
    print(f"blocks=97 even={parities.count(0)} odd={parities.count(1)} sat={sat_count} unsat={unsat_count} affine={verified_affine} direct_mod2={direct_relation is not None}")
    print("N398_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
