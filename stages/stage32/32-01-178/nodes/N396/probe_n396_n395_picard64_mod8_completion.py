#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import sys
from collections import Counter
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

WIDTH = 113
N395_AUDITED_HEAD = "604780ed17dbbb575f53a632a317a1308036157d"
N395_AUDIT_REVIEW = 5194942683
N395_AUDIT_BLOB = "f275121084b2b84f978f1ac542b665aca0dc74c1"
N395_AUDIT_CANONICAL = "27de1189c34716362d430c7b3631c02c9341894b1e7116a8de09f71a21fb22cd"
N395_RESULT_BLOB = "02adab67a764a373c59cd42e2e404318f2d7488c"
N395_RESULT_CANONICAL = "0a9ef6ccd8be8e3f270694d155bc7d4ebbd19cc9eab79906c34808440aa7441b"
N395_VERIFIER_BLOB = "6168055224172a961c6caf39a40b107d0a576368"
N394_PROBE_BLOB = "042bb940a6c586092f6b31312d3b16551e566a58"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"

INTERFACE_BLOB = "8a30e3aa30777460f344eb19836dc725dd442329"
INTERFACE_CANONICAL = "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6"
PAIRING_PREFIX_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
PICARD_BUNDLE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
PICARD_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"

ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def checked(path: Path, expected_blob: str, expected_canonical: str) -> dict:
    req(path.is_file(), f"missing source: {path}")
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    req(claimed == expected_canonical, f"stored canonical drift: {path}")
    req(csha(body) == expected_canonical, f"canonical drift: {path}")
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


def integer_stream_sha(values: list[int]) -> str:
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def hnf_contains(H: Matrix, b: Matrix) -> bool:
    n = H.rows
    req(H.cols == n and b.rows == n and b.cols == 1, "HNF shape drift")
    y = [0] * n
    for i in range(n - 1, -1, -1):
        rhs = int(b[i, 0])
        for j in range(i + 1, n):
            rhs -= int(H[i, j]) * y[j]
        diag = int(H[i, i])
        req(diag > 0, f"non-positive HNF diagonal at {i}")
        if rhs % diag:
            return False
        y[i] = rhs // diag
    return True


def main() -> None:
    repo = Path(__file__).resolve().parents[5]
    n395 = repo / "stages/stage32/32-01-178/nodes/N395"
    n394 = repo / "stages/stage32/32-01-178/nodes/N394"
    residual = repo / "stages/stage32/residual-32-01-production"
    bundle_dir = repo / "stages/stage33/33-07"
    interface_path = repo / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"

    audit395 = checked(n395 / "AUDIT-PASS.json", N395_AUDIT_BLOB, N395_AUDIT_CANONICAL)
    req(audit395["hostile_audit_verdict"] == "PASS", "N395 hostile audit verdict drift")
    req(audit395["audited_exact_head"] == N395_AUDITED_HEAD, "N395 audited head drift")
    req(int(audit395["hostile_audit_review_id"]) == N395_AUDIT_REVIEW, "N395 review drift")

    result395 = checked(n395 / "RESULT.json", N395_RESULT_BLOB, N395_RESULT_CANONICAL)
    req(result395["route_control"]["outcome"] == "TERMINAL_RELATION_TRANSPORT_VERIFIED_NO_PRUNING", "N395 outcome drift")
    req(result395["scope"]["terminal_identity_count"] == 10961, "N395 terminal count drift")
    req(result395["scope"]["assignment_order"] == ASSIGNMENT_ORDER, "N395 assignment order drift")
    verifier395 = n395 / "verify_n395_n394_relation_terminal_transport.py"
    req(blob(verifier395) == N395_VERIFIER_BLOB, "N395 verifier blob drift")

    probe394_path = n394 / "probe_n394_cross_mass_affine_structure.py"
    req(blob(probe394_path) == N394_PROBE_BLOB, "N394 probe blob drift")
    probe394 = load_module(probe394_path, "n396_n394_probe")
    req(list(probe394.ASSIGNMENT_ORDER) == ASSIGNMENT_ORDER, "N394 assignment order drift")
    req(int(probe394.WIDTH) == WIDTH, "N394 width drift")
    n391 = probe394.checked(
        repo / "stages/stage32/32-01-178/nodes/N391/RESULT.json",
        probe394.EXPECTED["n391_result_blob"],
        probe394.EXPECTED["n391_result_canonical"],
    )

    idx_path = residual / "compressed_terminal_indexer.py"
    req(blob(idx_path) == INDEXER_BLOB, "compressed indexer blob drift")
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == WIDTH, "terminal width drift")

    blocks: list[int] = []
    for wave in probe394.WAVES:
        blocks.extend(map(int, n391["waves"][wave]["residual_blocks"]))
    req(len(blocks) == 97 and len(set(blocks)) == 97, "N391 residual block union drift")

    interface = checked(interface_path, INTERFACE_BLOB, INTERFACE_CANONICAL)
    tmap = interface["terminal_to_picard64_map"]
    req(interface["stored_10_exceptional_coordinate_identity"]["terminal_assignment_order_1based"] == ASSIGNMENT_ORDER, "Picard interface assignment order drift")
    req(tmap["terminal_assignment_labels_1based"] == ASSIGNMENT_ORDER, "Picard terminal label drift")
    req(tmap["inverse_denominator"] == 8, "Picard inverse denominator drift")

    prefix_path = residual / "pairing_prefix_engine.py"
    bundle_path = bundle_dir / "picard_base_rows_retained.py"
    req(blob(prefix_path) == PAIRING_PREFIX_BLOB, "pairing-prefix engine blob drift")
    req(blob(bundle_path) == PICARD_BUNDLE_BLOB, "Picard retained bundle blob drift")

    sys.path.insert(0, str(bundle_dir))
    from pairing_prefix_engine import RetainedBasisPairingTransform
    import picard_base_rows_retained as retained_bundle

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == PICARD_BUNDLE_CANONICAL, "Picard retained bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    req(labels == tmap["selected_pairing_coordinate_order_1based"], "selected64 label order drift")
    req(int(transform.den) == 8, "selected64 denominator drift")

    fixed_positions = [labels.index(label) for label in ASSIGNMENT_ORDER]
    free_positions = [i for i in range(64) if i not in fixed_positions]
    req(fixed_positions == tmap["terminal_fixed_selected_positions_0based"], "fixed selected64 positions drift")
    req(free_positions == tmap["free_selected_positions_0based"], "free selected64 positions drift")

    B = transform.inverse_integer
    B_fixed = B.extract(list(range(64)), fixed_positions)
    B_free = B.extract(list(range(64)), free_positions)
    req(csha(matrix_list(B)) == tmap["inverse_integer_matrix_sha256"], "inverse integer matrix hash drift")
    req(csha(matrix_list(B_fixed)) == tmap["terminal_fixed_coefficient_matrix_sha256"], "fixed coefficient matrix hash drift")
    req(csha(matrix_list(B_free)) == tmap["free_completion_coefficient_matrix_sha256"], "free coefficient matrix hash drift")

    lattice = B_free.row_join(8 * Matrix.eye(64))
    H = hermite_normal_form(lattice)
    req(H.shape == (64, 64), "free completion HNF rank drift")
    req(all(H[i, j] == 0 for i in range(64) for j in range(i)), "HNF triangularity drift")
    hdiag = [abs(int(H[i, i])) for i in range(64)]
    req(all(v in (1, 2, 4, 8) for v in hdiag), "unexpected HNF invariant outside modulus 8")
    lattice_index = math.prod(hdiag)
    req(lattice_index > 0 and (lattice_index & (lattice_index - 1)) == 0, "lattice index is not a power of two")

    D = smith_normal_form(H, domain=ZZ)
    smith_diag = [abs(int(D[i, i])) for i in range(64)]
    req(math.prod(smith_diag) == lattice_index, "Smith/HNF index mismatch")
    smith_distribution = dict(sorted(Counter(smith_diag).items()))

    rank_stream: list[int] = []
    unsat_ranks: list[int] = []
    sat_ranks: list[int] = []
    residue_cache: dict[tuple[int, ...], bool] = {}
    block_mask_distribution: Counter[int] = Counter()
    full_sat_blocks = 0
    partial_blocks = 0
    full_unsat_blocks = 0

    for block in blocks:
        start = block * WIDTH
        base = tuple(int(v) for v in idx.unrank(start))
        req(base[4] == 0 and idx.rank(base) == start, f"block base drift {block}")
        residue_status: dict[int, bool] = {}
        local_sat = 0
        local_unsat = 0
        for offset in range(WIDTH):
            rank = start + offset
            terminal = tuple(int(v) for v in idx.unrank(rank))
            req(idx.rank(terminal) == rank, f"terminal rank/unrank drift block={block} offset={offset}")
            req(all(terminal[i] == base[i] for i in range(11) if i != 4), f"non-x49 terminal drift block={block} offset={offset}")
            req(terminal[4] == offset, f"x49 offset semantics drift block={block} offset={offset}")
            rank_stream.append(rank)

            key = tuple(v % 8 for v in terminal)
            if key not in residue_cache:
                x = Matrix(list(terminal))
                rhs = -(B_fixed * x)
                residue_cache[key] = hnf_contains(H, rhs)
            sat = residue_cache[key]
            r = terminal[4] % 8
            if r in residue_status:
                req(residue_status[r] == sat, f"mod8 completion status inconsistency block={block} residue={r}")
            residue_status[r] = sat
            if sat:
                sat_ranks.append(rank)
                local_sat += 1
            else:
                unsat_ranks.append(rank)
                local_unsat += 1

        req(set(residue_status) == set(range(8)), f"missing x49 residues block={block}")
        mask = sum((1 << r) for r, sat in residue_status.items() if sat)
        block_mask_distribution[mask] += 1
        if local_unsat == 0:
            full_sat_blocks += 1
        elif local_sat == 0:
            full_unsat_blocks += 1
        else:
            partial_blocks += 1

    req(len(rank_stream) == 10961, "N396 terminal replay count drift")
    req(integer_stream_sha(rank_stream) == result395["transport_result"]["terminal_rank_stream_sha256"], "N395 terminal rank stream drift")
    req(len(sat_ranks) + len(unsat_ranks) == len(rank_stream), "completion partition mismatch")

    outcome = (
        "PICARD64_INTEGRAL_COMPLETION_OBSTRUCTION_CANDIDATE"
        if unsat_ranks
        else "PICARD64_INTEGRAL_COMPLETION_TOTAL_ON_N395_TERMINALS_NO_PRUNING"
    )
    payload = {
        "semantics": "EXACT_N395_TERMINAL_TO_UNIVERSAL_SELECTED64_PICARD_INTEGRAL_COMPLETION_MOD8; NO_EFFECTIVITY_OR_ENDPOINT_CREDIT",
        "source_n395_audited_head": N395_AUDITED_HEAD,
        "source_n395_hostile_audit_review": N395_AUDIT_REVIEW,
        "source_picard_interface_blob": INTERFACE_BLOB,
        "source_picard_interface_canonical": INTERFACE_CANONICAL,
        "population_bridge": {
            "uses_hpadj_population_membership": False,
            "mechanism": "DIRECT_REPLAY_OF_UNIVERSAL_SELECTED64_INVERSE_INTEGER_MAP_ON_IDENTICAL_11_TERMINAL_PAIRING_LABELS",
            "selected64_denominator": 8,
            "terminal_assignment_labels": ASSIGNMENT_ORDER,
        },
        "scope": {
            "row_id": "g1-d008",
            "g": 1,
            "d": 8,
            "e": 8,
            "block_count": len(blocks),
            "block_width": WIDTH,
            "terminal_identity_count": len(rank_stream),
        },
        "free_completion_lattice": {
            "free_variable_count": 53,
            "ambient_coordinate_count": 64,
            "modulus": 8,
            "hnf_sha256": csha(matrix_list(H)),
            "smith_diagonal_distribution": {str(k): v for k, v in smith_distribution.items()},
            "obstruction_quotient_order": lattice_index,
            "obstruction_quotient_log2": lattice_index.bit_length() - 1,
            "free_mod8_image_log2": 192 - (lattice_index.bit_length() - 1),
        },
        "completion_result": {
            "sat_terminal_count": len(sat_ranks),
            "unsat_terminal_count": len(unsat_ranks),
            "full_sat_block_count": full_sat_blocks,
            "partial_block_count": partial_blocks,
            "full_unsat_block_count": full_unsat_blocks,
            "unique_terminal_mod8_class_count": len(residue_cache),
            "allowed_x49_residue_mask_distribution": {
                f"0x{mask:02x}": count for mask, count in sorted(block_mask_distribution.items())
            },
            "sat_terminal_rank_stream_sha256": integer_stream_sha(sat_ranks),
            "unsat_terminal_rank_stream_sha256": integer_stream_sha(unsat_ranks),
        },
        "outcome": outcome,
        "credit": {
            "candidate_pruning_terminals": len(unsat_ranks),
            "main_pruning_credit": False,
            "full178_complete": False,
            "effectivity_final": False,
            "integral_carrier_obstruction_promoted": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "heavy_compute_authorized": False,
            "merge_authorized": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)

    print("PASS_N396_N395_PICARD64_MOD8_COMPLETION")
    print(
        f"terminals={len(rank_stream)} sat={len(sat_ranks)} unsat={len(unsat_ranks)} "
        f"blocks_full_sat={full_sat_blocks} blocks_partial={partial_blocks} blocks_full_unsat={full_unsat_blocks}"
    )
    print("N396_PROBE_JSON=" + json.dumps(payload, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
