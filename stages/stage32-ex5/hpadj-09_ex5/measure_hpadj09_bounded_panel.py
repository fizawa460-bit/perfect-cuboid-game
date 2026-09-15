#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"

PREFLIGHT = HERE / "PREFLIGHT.json"
RESULT = HERE / "RESULT.json"
INTERFACE = ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
MANIFEST = RESIDUAL / "full178-manifest.json"
FAMILY = RESIDUAL / "compressed_terminal_family.py"
INDEXER = RESIDUAL / "compressed_terminal_indexer.py"
PAIRING = RESIDUAL / "pairing_prefix_engine.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"

LOCKS = {
    "preflight_blob": "4fb4b22b0577c19e98aeefa43c073ba062556dff",
    "preflight_canonical": "d41612200ecf621de4d1f44bca128b721c84e73ad50bce7ce1c550f3daf87441",
    "result_blob": "e545ccdbd30e6ecc786df6fbb55ee22a3cbfc4fc",
    "result_canonical": "12fa045883e7400c58ee9b3e8376e3d008471ea7a1701fec5e54021feb11803c",
    "interface_blob": "8a30e3aa30777460f344eb19836dc725dd442329",
    "interface_canonical": "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6",
    "manifest_blob": "0a46b34e278688240656b4977e9cb7f589e90e06",
    "manifest_canonical": "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23",
    "family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
    "indexer_blob": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    "pairing_blob": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "bundle_blob": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "bundle_canonical": "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c",
    "inverse_integer_sha256": "7b4d0601585f011e168bf5c4b15086950b0e3e3e16c90826b7413cdbe183c233",
    "fixed_matrix_sha256": "e8f4a9004177fc2a2023775431505d4ef39b7b808bd41cb517787c235ab170fe",
    "free_matrix_sha256": "ad27fa86fbc98d55a97af5fd9d247fb880af9dac58d6429ca029d6b8ca4c288b",
    "free_hnf_sha256": "a5d494b72bd4fa8335fe2199df8f938851139308fb77b0253f564d959754072e",
}

ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
PANEL_SPECS = [
    {"g": 0, "d": 8, "e": 12},
    {"g": 1, "d": 8, "e": 12},
    {"g": 0, "d": 10, "e": 14},
    {"g": 1, "d": 10, "e": 14},
]
ANCHOR_COUNT = 5
PREFIXES_PER_ANCHOR = 16
MAX_SCAN_PER_ANCHOR = 4096


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(value: dict) -> str:
    body = dict(value)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def matrix_sha(m: Matrix) -> str:
    return hashlib.sha256(
        json.dumps(matrix_list(m), sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked_json(path: Path, blob_sha: str, canonical_sha: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob_sha, f"{label} blob drift")
    value = json.loads(path.read_text())
    req(value.get("canonical_sha256_without_this_field") == canonical_sha, f"{label} stored canonical drift")
    req(canon(value) == canonical_sha, f"{label} canonical drift")
    return value


def verify_source_locks() -> tuple[dict, dict, dict, dict]:
    preflight = load_locked_json(PREFLIGHT, LOCKS["preflight_blob"], LOCKS["preflight_canonical"], "preflight")
    result = load_locked_json(RESULT, LOCKS["result_blob"], LOCKS["result_canonical"], "retained quotient result")
    interface = load_locked_json(INTERFACE, LOCKS["interface_blob"], LOCKS["interface_canonical"], "HPADJ interface")
    manifest = load_locked_json(MANIFEST, LOCKS["manifest_blob"], LOCKS["manifest_canonical"], "FULL178 manifest")

    for path, expected, label in [
        (FAMILY, LOCKS["family_blob"], "compressed terminal family"),
        (INDEXER, LOCKS["indexer_blob"], "compressed terminal indexer"),
        (PAIRING, LOCKS["pairing_blob"], "pairing prefix engine"),
        (BUNDLE_SOURCE, LOCKS["bundle_blob"], "retained Picard64 bundle source"),
    ]:
        req(path.is_file(), f"missing {label}")
        req(git_blob(path) == expected, f"{label} blob drift")

    req(preflight.get("route_id") == "HPADJ-09_ex5", "preflight route drift")
    req(result.get("status") == "RETAINED_EXACT_STRICT_NONTRIVIAL_OBSTRUCTION_AUDIT_REQUIRED", "quotient result status drift")
    req(result.get("lattice", {}).get("fixed_image_size") == 2, "retained quotient image-size drift")
    req(result.get("residue_cube", {}).get("accepted_classes") == 4294967296, "retained accepted residue count drift")
    req(interface.get("terminal_identity_or_exact_rank_unrank_contract", {}).get("rank_unrank_roundtrip_exact") is True, "rank/unrank contract drift")
    deps = interface.get("dependency_source_locks", {})
    req(deps.get("compressed_terminal_family_blob_sha1") == LOCKS["family_blob"], "interface family lock drift")
    req(deps.get("compressed_terminal_indexer_blob_sha1") == LOCKS["indexer_blob"], "interface indexer lock drift")
    req(deps.get("pairing_prefix_engine_blob_sha1") == LOCKS["pairing_blob"], "interface pairing lock drift")
    req(deps.get("picard_bundle_source_blob_sha1") == LOCKS["bundle_blob"], "interface bundle lock drift")
    return preflight, result, interface, manifest


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def component_a(d: int, a: int) -> int:
    h = d // 2
    return min(13, d - a, d - 2 * a + 4, h + 5)


def component3(d: int, b: int, c: int) -> int:
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def hpadj_member(terminal_predicate, *, g: int, d: int, e: int, values: tuple[int, ...]) -> bool:
    if not terminal_predicate(values, e=e, d=d):
        return False
    if g not in (0, 1) or d < 8 or d % 2 or e % 2:
        return False
    x = tuple(int(v) for v in values)
    a = x[2] + x[3] + x[7]
    b = x[1] + x[5] + x[9]
    c = x[0] + x[6] + x[8] + x[10]
    if 8 * a * a + 8 * b * b + 6 * c * c <= 3 * d * d + 96:
        return False
    support = sum(int(x[i] > 0) for i in range(11) if i != 4)
    M = a + b + c
    K = ceil_div(d - 16 * g + 16, 4)
    ca = component_a(d, a)
    c3 = component3(d, b, c)
    if ca < 0 or c3 < 0:
        return False
    srem = min(16, d) + ca + c3
    qneed = K - support
    if qneed > 0 and srem < qneed:
        return False
    lower = max(8 if g == 0 else 4, K, d - 4 * g + 4, M, M + max(0, qneed))
    upper = min((19 * d) // 5, 3 * d, 3 * d - (b - c))
    if not lower <= e <= upper:
        return False
    e_n358 = 3 * d - (b - c)
    if b <= d // 2 - 5 and support + srem == K and e_n358 - M >= srem and e == e_n358:
        return False
    if g == 1 and d == 8 and e == 8:
        return False
    return True


def manifest_rows(manifest: dict) -> set[str]:
    rows: set[str] = set()
    for ids in manifest["m_class_rows"].values():
        rows.update(str(v) for v in ids)
    req(len(rows) == 178, "FULL178 row-set drift")
    return rows


def anchor_starts(exceptional_count: int) -> list[int]:
    E = int(exceptional_count)
    req(E > MAX_SCAN_PER_ANCHOR, "panel source exceptional population unexpectedly small")
    raw = [0, E // 4, E // 2, (3 * E) // 4, max(0, E - MAX_SCAN_PER_ANCHOR)]
    req(len(set(raw)) == ANCHOR_COUNT, "panel anchor collision")
    return raw


def main() -> None:
    _, retained_result, interface, manifest = verify_source_locks()

    # Import repository executable dependencies only after every load-bearing
    # source blob above has been checked. This is intentionally lock-before-exec.
    sys.path.insert(0, str(RESIDUAL))
    sys.path.insert(0, str(BUNDLE_DIR))
    from compressed_terminal_family import terminal_predicate
    from compressed_terminal_indexer import CompressedTerminalIndexer
    from pairing_prefix_engine import PrefixMembershipOracle, RetainedBasisPairingTransform
    import picard_base_rows_retained as retained_bundle

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == LOCKS["bundle_canonical"], "Picard64 bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    req(int(transform.den) == 8, "selected64 denominator drift")
    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    req(len(labels) == 64 and len(set(labels)) == 64, "selected64 label identity drift")
    fixed_positions = [labels.index(label) for label in ASSIGNMENT_LABELS]
    free_positions = [i for i in range(64) if i not in fixed_positions]
    B = transform.inverse_integer
    fixed = B.extract(list(range(64)), fixed_positions)
    free = B.extract(list(range(64)), free_positions)
    req(matrix_sha(B) == LOCKS["inverse_integer_sha256"], "inverse integer matrix drift")
    req(matrix_sha(fixed) == LOCKS["fixed_matrix_sha256"], "fixed matrix drift")
    req(matrix_sha(free) == LOCKS["free_matrix_sha256"], "free matrix drift")

    oracle = PrefixMembershipOracle(transform, fixed_positions)
    check = oracle.checks[-1]
    req(check.depth == 11, "kernel depth drift")
    req(check.modulus == 2, f"expected index-2 terminal kernel modulus, got {check.modulus}")
    req(check.hnf_sha256 == LOCKS["free_hnf_sha256"], "free HNF identity drift")
    coeff_rows = sorted(set(tuple(int(v) % check.modulus for v in row) for row in check.coefficients))
    req(coeff_rows, "terminal kernel has no active congruence rows")

    parity_accept = 0
    for bits in itertools.product(range(check.modulus), repeat=11):
        parity_accept += int(check.feasible(bits))
    req(parity_accept == 1024, f"unexpected accepted mod-2 classes: {parity_accept}")
    reconstructed_mod8_accept = parity_accept * (8 // check.modulus) ** 11
    req(reconstructed_mod8_accept == retained_result["residue_cube"]["accepted_classes"], "kernel does not reconstruct retained mod-8 accepted count")

    rows = manifest_rows(manifest)
    per_stratum = []
    aggregate_tested = 0
    aggregate_accepted = 0
    aggregate_rejected = 0
    aggregate_prefixes = 0
    rank_stream = hashlib.sha256()
    residue_stream = hashlib.sha256()

    for spec in PANEL_SPECS:
        g, d, e = int(spec["g"]), int(spec["d"]), int(spec["e"])
        row_id = f"g{g}-d{d:03d}"
        req(row_id in rows, f"panel row not in FULL178: {row_id}")
        idx = CompressedTerminalIndexer(e, d)
        block = idx.normal_budget + 1
        E = idx.exceptional_count
        starts = anchor_starts(E)
        selected: list[tuple[int, int]] = []
        selected_set: set[int] = set()
        anchor_records = []

        for anchor_index, start in enumerate(starts):
            found: list[int] = []
            scanned = 0
            stop = min(E, start + MAX_SCAN_PER_ANCHOR)
            for exceptional_rank in range(start, stop):
                scanned += 1
                if exceptional_rank in selected_set:
                    continue
                base_rank = exceptional_rank * block
                values = idx.unrank(base_rank)
                req(values[4] == 0, "x4-innermost rank contract drift")
                req(idx.rank(values) == base_rank, "rank/unrank roundtrip drift during prefix scan")
                if not hpadj_member(terminal_predicate, g=g, d=d, e=e, values=values):
                    continue
                selected.append((anchor_index, exceptional_rank))
                selected_set.add(exceptional_rank)
                found.append(exceptional_rank)
                if len(found) == PREFIXES_PER_ANCHOR:
                    break
            req(len(found) == PREFIXES_PER_ANCHOR, f"insufficient HPADJ prefixes in bounded anchor scan {row_id}/e={e}/anchor={anchor_index}: {len(found)}")
            anchor_records.append({
                "anchor_index": anchor_index,
                "start_exceptional_rank": start,
                "scanned_exceptional_prefixes": scanned,
                "selected_hpadj_prefixes": len(found),
                "first_selected_exceptional_rank": found[0],
                "last_selected_exceptional_rank": found[-1],
            })

        accepted = 0
        rejected = 0
        parity_hist: dict[str, list[int]] = {}
        for anchor_index, exceptional_rank in selected:
            for x4 in range(block):
                rank = exceptional_rank * block + x4
                values = idx.unrank(rank)
                req(values[4] == x4, "normal coordinate rank contract drift")
                req(idx.rank(values) == rank, "rank/unrank roundtrip drift in panel")
                req(hpadj_member(terminal_predicate, g=g, d=d, e=e, values=values), "selected prefix escaped HPADJ membership across x4 block")
                feasible = check.feasible(values)
                accepted += int(feasible)
                rejected += int(not feasible)
                rank_stream.update(f"{row_id}|{e}|{rank}|{int(feasible)}\n".encode())
                residue = "".join(str(int(v) & 1) for v in values)
                slot = parity_hist.setdefault(residue, [0, 0])
                slot[0] += 1
                slot[1] += int(feasible)
                residue_stream.update(f"{row_id}|{e}|{residue}|{int(feasible)}\n".encode())

        tested = accepted + rejected
        req(tested == len(selected) * block, "panel terminal count mismatch")
        req(rejected > 0, f"no actual HPADJ terminal rejection observed in bounded stratum panel {row_id}/e={e}")
        aggregate_tested += tested
        aggregate_accepted += accepted
        aggregate_rejected += rejected
        aggregate_prefixes += len(selected)
        per_stratum.append({
            "row_id": row_id,
            "g": g,
            "d": d,
            "e": e,
            "normal_budget": idx.normal_budget,
            "normal_block_size": block,
            "exceptional_prefix_population": E,
            "anchor_rule": "starts=[0,E//4,E//2,3E//4,E-MAX_SCAN], scan forward; first 16 HPADJ prefixes per anchor",
            "anchors": anchor_records,
            "selected_hpadj_exceptional_prefixes": len(selected),
            "tested_actual_hpadj_terminals": tested,
            "kernel_accepted_terminals": accepted,
            "kernel_rejected_terminals": rejected,
            "bounded_rejected_fraction_num": rejected,
            "bounded_rejected_fraction_den": tested,
            "observed_parity_signature_count": len(parity_hist),
        })

    req(aggregate_rejected > 0, "bounded panel produced no actual HPADJ rejection")
    out = {
        "schema": "STAGE32EX5_HPADJ09_BOUNDED_TERMINAL_PANEL_DIAGNOSTIC_V1",
        "status": "NONZERO_ACTUAL_HPADJ_TERMINAL_REJECTION_ON_BOUNDED_PANEL",
        "route_id": "HPADJ-09_ex5",
        "source": {
            "preflight_blob_sha1": LOCKS["preflight_blob"],
            "preflight_canonical_sha256": LOCKS["preflight_canonical"],
            "retained_quotient_result_blob_sha1": LOCKS["result_blob"],
            "retained_quotient_result_canonical_sha256": LOCKS["result_canonical"],
            "interface_blob_sha1": LOCKS["interface_blob"],
            "interface_canonical_sha256": LOCKS["interface_canonical"],
            "manifest_blob_sha1": LOCKS["manifest_blob"],
            "manifest_canonical_sha256": LOCKS["manifest_canonical"],
        },
        "kernel": {
            "assignment_labels_1based": ASSIGNMENT_LABELS,
            "assigned_selected_positions_0based": fixed_positions,
            "modulus": check.modulus,
            "active_congruence_row_count": len(check.coefficients),
            "unique_congruence_rows": [list(row) for row in coeff_rows],
            "free_hnf_sha256": check.hnf_sha256,
            "accepted_mod2_classes": parity_accept,
            "total_mod2_classes": 2 ** 11,
            "reconstructed_accepted_mod8_classes": reconstructed_mod8_accept,
            "matches_retained_mod8_quotient": True,
        },
        "panel_contract": {
            "kind": "DETERMINISTIC_LOW_DEGREE_EXACT_RANK_UNRANK_PANEL",
            "strata": PANEL_SPECS,
            "anchors_per_stratum": ANCHOR_COUNT,
            "hpadj_prefixes_per_anchor": PREFIXES_PER_ANCHOR,
            "max_exceptional_prefix_scan_per_anchor": MAX_SCAN_PER_ANCHOR,
            "normal_coordinate_policy": "enumerate the complete x4 block for every selected HPADJ exceptional prefix",
            "selection_is_population_estimator": False,
            "full_population_materialized": False,
            "full178_scaleout_authorized": False,
        },
        "strata": per_stratum,
        "aggregate": {
            "selected_hpadj_exceptional_prefixes": aggregate_prefixes,
            "tested_actual_hpadj_terminals": aggregate_tested,
            "kernel_accepted_terminals": aggregate_accepted,
            "kernel_rejected_terminals": aggregate_rejected,
            "bounded_rejected_fraction_num": aggregate_rejected,
            "bounded_rejected_fraction_den": aggregate_tested,
            "rank_outcome_stream_sha256": rank_stream.hexdigest(),
            "parity_outcome_stream_sha256": residue_stream.hexdigest(),
        },
        "semantics": {
            "claim": "At least one actual retained-HPADJ terminal in this explicitly bounded low-degree panel fails the exact retained mod-8 Picard64 completion necessary condition.",
            "terminal_population_rejection_measured": True,
            "measurement_scope": "BOUNDED_PANEL_ONLY",
            "uniform_terminal_residue_distribution_claimed": False,
            "global_rejected_terminal_fraction_claimed": False,
            "population_wide_pruning_claimed": False,
            "reverse_realization_claimed": False,
            "full178_scaleout_authorized": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
