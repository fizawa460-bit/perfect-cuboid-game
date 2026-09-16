#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HPADJ09 = ROOT / "stages/stage32-ex5/hpadj-09_ex5"
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"

PREFLIGHT = HPADJ09 / "PREFLIGHT.json"
RESULT = HPADJ09 / "RESULT.json"
PANEL_RESULT = HPADJ09 / "PANEL-RESULT.json"
INTERFACE = ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
PAIRING = RESIDUAL / "pairing_prefix_engine.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"

LOCKS = {
    "preflight_blob": "4fb4b22b0577c19e98aeefa43c073ba062556dff",
    "preflight_canonical": "d41612200ecf621de4d1f44bca128b721c84e73ad50bce7ce1c550f3daf87441",
    "result_blob": "e545ccdbd30e6ecc786df6fbb55ee22a3cbfc4fc",
    "result_canonical": "12fa045883e7400c58ee9b3e8376e3d008471ea7a1701fec5e54021feb11803c",
    "panel_result_blob": "8b01e8e63b402a38b33ec0eab4e669921870bf6c",
    "panel_result_canonical": "7635e28de31e53161ee36b6b0d020a5127de2ddff73ca13ca591740758426115",
    "interface_blob": "8a30e3aa30777460f344eb19836dc725dd442329",
    "interface_canonical": "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6",
    "pairing_blob": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "bundle_blob": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "bundle_canonical": "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c",
    "free_hnf_sha256": "a5d494b72bd4fa8335fe2199df8f938851139308fb77b0253f564d959754072e",
}

ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
NORMAL_COORDINATE_INDEX = 4


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


def load_locked_json(path: Path, blob_sha: str, canonical_sha: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(git_blob(path) == blob_sha, f"{label} blob drift")
    value = json.loads(path.read_text())
    req(value.get("canonical_sha256_without_this_field") == canonical_sha, f"{label} stored canonical drift")
    req(canon(value) == canonical_sha, f"{label} canonical drift")
    return value


def main() -> None:
    # Fail closed before importing load-bearing repository code.
    preflight = load_locked_json(PREFLIGHT, LOCKS["preflight_blob"], LOCKS["preflight_canonical"], "HPADJ09 preflight")
    result = load_locked_json(RESULT, LOCKS["result_blob"], LOCKS["result_canonical"], "HPADJ09 quotient result")
    panel = load_locked_json(PANEL_RESULT, LOCKS["panel_result_blob"], LOCKS["panel_result_canonical"], "HPADJ09 panel result")
    interface = load_locked_json(INTERFACE, LOCKS["interface_blob"], LOCKS["interface_canonical"], "HPADJ interface")
    req(PAIRING.is_file() and git_blob(PAIRING) == LOCKS["pairing_blob"], "pairing engine blob drift")
    req(BUNDLE_SOURCE.is_file() and git_blob(BUNDLE_SOURCE) == LOCKS["bundle_blob"], "retained Picard bundle source blob drift")
    req(preflight.get("route_id") == "HPADJ-09_ex5", "HPADJ09 route drift")
    req(result.get("lattice", {}).get("fixed_image_size") == 2, "retained quotient image-size drift")
    req(panel.get("kernel", {}).get("unique_congruence_row_count") == 1, "bounded panel unique-row count drift")
    req(panel.get("kernel", {}).get("modulus") == 8, "bounded panel modulus drift")
    req(interface.get("terminal_identity_or_exact_rank_unrank_contract", {}).get("rank_unrank_roundtrip_exact") is True, "rank/unrank contract drift")

    sys.path.insert(0, str(RESIDUAL))
    sys.path.insert(0, str(BUNDLE_DIR))
    from pairing_prefix_engine import PrefixMembershipOracle, RetainedBasisPairingTransform
    import picard_base_rows_retained as retained_bundle

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == LOCKS["bundle_canonical"], "Picard bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    req(int(transform.den) == 8, "selected64 denominator drift")
    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    fixed_positions = [labels.index(label) for label in ASSIGNMENT_LABELS]
    req(len(fixed_positions) == 11 and len(set(fixed_positions)) == 11, "fixed assignment identity drift")

    check = PrefixMembershipOracle(transform, fixed_positions).checks[-1]
    req(check.depth == 11, "terminal kernel depth drift")
    req(check.modulus == 8, "terminal kernel modulus drift")
    req(check.hnf_sha256 == LOCKS["free_hnf_sha256"], "terminal kernel HNF drift")
    rows = sorted(set(tuple(int(v) % check.modulus for v in row) for row in check.coefficients))
    req(len(rows) == 1, f"expected one unique terminal congruence row, got {len(rows)}")
    row = rows[0]

    common = check.modulus
    for a in row:
        common = math.gcd(common, int(a))
    req(common > 0 and check.modulus % common == 0, "invalid row/modulus gcd")
    reduced_modulus = check.modulus // common
    reduced_row = tuple((int(a) // common) % reduced_modulus for a in row)

    # fixed_image_size=2 plus one homogeneous row should reduce to one parity equation.
    req(reduced_modulus == 2, f"expected index-2 row to reduce to modulus 2, got {reduced_modulus}")
    req(any(reduced_row), "reduced parity row is zero")
    req(reduced_row[NORMAL_COORDINATE_INDEX] == 1, "x4 is not active in the reduced parity row")

    other_active = [i for i, a in enumerate(reduced_row) if i != NORMAL_COORDINATE_INDEX and a]
    # Over F2, subtraction equals addition, so accepted terminals satisfy
    # x4 == sum(active exceptional coordinates) (mod 2).
    parity_formula = "x4 ≡ " + (" + ".join(f"x{i}" for i in other_active) if other_active else "0") + " (mod 2)"

    out = {
        "schema": "STAGE32EX5_HPADJ10_SYMBOLIC_TERMINAL_KERNEL_V1",
        "status": "EXACT_INDEX2_TERMINAL_KERNEL_REDUCED_TO_PARITY",
        "route_id": "HPADJ-10_ex5",
        "source": {
            "hpadj09_preflight_blob_sha1": LOCKS["preflight_blob"],
            "hpadj09_result_blob_sha1": LOCKS["result_blob"],
            "hpadj09_result_canonical_sha256": LOCKS["result_canonical"],
            "hpadj09_panel_result_blob_sha1": LOCKS["panel_result_blob"],
            "hpadj09_panel_result_canonical_sha256": LOCKS["panel_result_canonical"],
            "interface_blob_sha1": LOCKS["interface_blob"],
            "interface_canonical_sha256": LOCKS["interface_canonical"],
            "pairing_engine_blob_sha1": LOCKS["pairing_blob"],
            "picard_bundle_source_blob_sha1": LOCKS["bundle_blob"],
            "picard_bundle_canonical_sha256": LOCKS["bundle_canonical"],
            "free_hnf_sha256": LOCKS["free_hnf_sha256"],
        },
        "kernel": {
            "assignment_labels_1based": ASSIGNMENT_LABELS,
            "assigned_selected_positions_0based": fixed_positions,
            "original_modulus": check.modulus,
            "active_congruence_row_count": len(check.coefficients),
            "unique_congruence_row": list(row),
            "row_modulus_gcd": common,
            "reduced_modulus": reduced_modulus,
            "reduced_parity_row_x0_through_x10": list(reduced_row),
            "normal_coordinate_index": NORMAL_COORDINATE_INDEX,
            "other_active_coordinate_indices": other_active,
            "accepted_terminal_condition": parity_formula,
        },
        "counting_consequence": {
            "per_exceptional_prefix_exact_counting_available": True,
            "normal_coordinate_range": "x4=0..(19*d-5*e)",
            "normal_block_size": "19*d-5*e+1",
            "for_even_d_and_e_normal_block_size_is_odd": True,
            "accepted_count_per_prefix": "number of x4 in [0,N] with parity required by the exact kernel",
            "rejected_count_per_prefix": "(N+1)-accepted_count_per_prefix",
            "population_wide_count_completed": False,
            "next_exact_unit": "Count HPADJ exceptional prefixes by the reduced parity class on all retained rows, then combine with the exact x4 parity count without enumerating terminals.",
        },
        "semantics": {
            "global_50_percent_claimed": False,
            "population_wide_pruning_claimed": False,
            "full178_scaleout_complete": False,
            "reverse_realization_claimed": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
