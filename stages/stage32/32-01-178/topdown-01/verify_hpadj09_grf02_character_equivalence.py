#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE = HERE / "HPADJ09-EQUIVALENCE-NOTE.json"
GRF02 = ROOT / "stages/stage32/management/global-residual-feasibility/GRF-02-PROJECTED-KERNEL.json"
INTERFACE = ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json"
PAIRING = ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"

NOTE_BLOB = "9825be2067c1dbd2ea4583e715cfedd991456c82"
NOTE_CANON = "0cabdf02524c1d5e976df863454c790fb7b89c7d585a9e9ba9f36757d13eafd7"
GRF02_BLOB = "7c1cda07749fbfb90245995d1def2ae96fb5604b"
GRF02_CANON = "2e08a25e2de891bfabd0bf96ba06d928d733711b2c27449c9818b856665d4d6f"
INTERFACE_BLOB = "8a30e3aa30777460f344eb19836dc725dd442329"
INTERFACE_CANON = "cc6010f71e46cb21e7bf2fcf12dfe961cb09570454e43dddc0e9cf7fa04542e6"
PAIRING_BLOB = "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"
BUNDLE_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
BUNDLE_CANON = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
B_SHA = "7b4d0601585f011e168bf5c4b15086950b0e3e3e16c90826b7413cdbe183c233"
FIXED_SHA = "e8f4a9004177fc2a2023775431505d4ef39b7b808bd41cb517787c235ab170fe"
FREE_SHA = "ad27fa86fbc98d55a97af5fd9d247fb880af9dac58d6429ca029d6b8ca4c288b"
HPADJ09_UNIQUE_ROWS_SHA256 = "fa255af25e535fa5e60670d2ad6eb5e40a5e4f28476d8ec2afcab4fbb6b787e3"
HPADJ09_PANEL_REF = "fd14ff7e53dcd6f0c5ba9b38c45a27d30885f019"
HPADJ09_PANEL_PATH = "stages/stage32-ex5/hpadj-09_ex5/PANEL-RESULT.json"
HPADJ09_PANEL_BLOB = "8b01e8e63b402a38b33ec0eab4e669921870bf6c"
HPADJ09_PANEL_CANON = "7635e28de31e53161ee36b6b0d020a5127de2ddff73ca13ca591740758426115"
HPADJ09_FREE_HNF_SHA256 = "a5d494b72bd4fa8335fe2199df8f938851139308fb77b0253f564d959754072e"
ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_MOD8_ROW = [4, 0, 0, 0, 4, 0, 0, 0, 4, 0, 4]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob_bytes(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def git_blob(path: Path) -> str:
    return git_blob_bytes(path.read_bytes())


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def matrix_list(m) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def matrix_sha(m) -> str:
    return hashlib.sha256(
        json.dumps(matrix_list(m), sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def historical_bytes(ref: str, path: str) -> bytes:
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "show", f"{ref}:{path}"])
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            f"FAIL: historical HPADJ09 source unavailable {ref}:{path}; fetch the exact commit before --historical-replay"
        ) from exc


def load_historical_panel() -> dict:
    raw = historical_bytes(HPADJ09_PANEL_REF, HPADJ09_PANEL_PATH)
    req(git_blob_bytes(raw) == HPADJ09_PANEL_BLOB, "HPADJ09 PANEL-RESULT blob drift")
    panel = json.loads(raw)
    req(panel.get("canonical_sha256_without_this_field") == HPADJ09_PANEL_CANON,
        "HPADJ09 PANEL-RESULT stored canonical drift")
    req(canon(panel) == HPADJ09_PANEL_CANON, "HPADJ09 PANEL-RESULT canonical drift")
    return panel


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--historical-replay",
        action="store_true",
        help="also replay the exact historical HPADJ09 PANEL-RESULT Git object",
    )
    ns = ap.parse_args()

    # Fail closed on every load-bearing current source before importing executable
    # repository modules used to derive the HPADJ09 row.
    req(git_blob(NOTE) == NOTE_BLOB, "equivalence note blob drift")
    note = json.loads(NOTE.read_text())
    req(note.get("canonical_sha256_without_this_field") == NOTE_CANON, "note stored canonical drift")
    req(canon(note) == NOTE_CANON, "note canonical drift")

    req(git_blob(GRF02) == GRF02_BLOB, "GRF02 blob drift")
    grf = json.loads(GRF02.read_text())
    req(grf.get("canonical_sha256_without_this_field") == GRF02_CANON, "GRF02 stored canonical drift")
    req(canon(grf) == GRF02_CANON, "GRF02 canonical drift")

    req(git_blob(INTERFACE) == INTERFACE_BLOB, "HPADJ interface blob drift")
    interface = json.loads(INTERFACE.read_text())
    req(interface.get("canonical_sha256_without_this_field") == INTERFACE_CANON,
        "HPADJ interface stored canonical drift")
    req(canon(interface) == INTERFACE_CANON, "HPADJ interface canonical drift")
    req(git_blob(PAIRING) == PAIRING_BLOB, "pairing-prefix engine blob drift")
    req(git_blob(BUNDLE_SOURCE) == BUNDLE_BLOB, "retained Picard64 bundle source blob drift")
    deps = interface.get("dependency_source_locks", {})
    req(deps.get("pairing_prefix_engine_blob_sha1") == PAIRING_BLOB, "interface pairing lock drift")
    req(deps.get("picard_bundle_source_blob_sha1") == BUNDLE_BLOB, "interface bundle lock drift")
    req(deps.get("picard_bundle_canonical_sha256") == BUNDLE_CANON, "interface bundle canonical drift")

    # Derive the HPADJ09 terminal congruence row from the retained oracle itself.
    # This is intentionally not a hard-coded-hash-only comparison.
    sys.path.insert(0, str(RESIDUAL))
    sys.path.insert(0, str(BUNDLE_DIR))
    from pairing_prefix_engine import PrefixMembershipOracle, RetainedBasisPairingTransform
    import picard_base_rows_retained as retained_bundle

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == BUNDLE_CANON, "Picard64 bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    req(int(transform.den) == 8, "selected64 denominator drift")
    labels = [int(v) for v in transform.certificate["selected_known_indices_1based"]]
    req(len(labels) == 64 and len(set(labels)) == 64, "selected64 label identity drift")
    fixed_positions = [labels.index(label) for label in ASSIGNMENT_LABELS]
    free_positions = [i for i in range(64) if i not in fixed_positions]
    req(len(fixed_positions) == 11 and len(free_positions) == 53, "fixed/free partition drift")

    B = transform.inverse_integer
    fixed = B.extract(list(range(64)), fixed_positions)
    free = B.extract(list(range(64)), free_positions)
    req(matrix_sha(B) == B_SHA, "inverse integer matrix identity drift")
    req(matrix_sha(fixed) == FIXED_SHA, "fixed matrix identity drift")
    req(matrix_sha(free) == FREE_SHA, "free matrix identity drift")

    oracle = PrefixMembershipOracle(transform, fixed_positions)
    check = oracle.checks[-1]
    req(int(check.depth) == 11, "HPADJ09 terminal-kernel depth drift")
    req(int(check.modulus) == 8, "HPADJ09 terminal-kernel modulus drift")
    req(check.hnf_sha256 == HPADJ09_FREE_HNF_SHA256, "HPADJ09 free-HNF identity drift")
    coeff_rows = sorted(
        set(tuple(int(v) % int(check.modulus) for v in row) for row in check.coefficients)
    )
    req(len(coeff_rows) == 1, "HPADJ09 unique terminal congruence row-count drift")
    derived_hpadj09_row = list(coeff_rows[0])
    req(derived_hpadj09_row == EXPECTED_MOD8_ROW, "HPADJ09 derived mod8 row drift")
    derived_rows_sha = hashlib.sha256(
        json.dumps([derived_hpadj09_row], sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    req(derived_rows_sha == HPADJ09_UNIQUE_ROWS_SHA256, "HPADJ09 derived unique-row hash drift")

    rows = grf["exact_completion_kernel"]["primitive_equation_rows"]
    req(len(rows) == 1 and int(rows[0]["modulus"]) == 2, "GRF02 primitive row contract drift")
    grf02_row = [int(x) for x in rows[0]["coefficients"]]
    req(grf02_row == note["character_identity"]["grf02_mod2_row"], "GRF02 row/note mismatch")
    reconstructed = [4 * x for x in grf02_row]
    req(reconstructed == derived_hpadj09_row, "GRF02 row does not reconstruct derived HPADJ09 row")
    req(derived_hpadj09_row == note["character_identity"]["hpadj09_reconstructed_mod8_row"],
        "derived HPADJ09 row/note mismatch")
    req(derived_rows_sha == note["character_identity"]["hpadj09_retained_unique_congruence_rows_sha256"],
        "derived HPADJ09 row hash/note mismatch")

    for s in range(8):
        req(
            ((4 * s) % 8 == 0) == (s % 2 == 0),
            f"scalar congruence equivalence failed at residue {s}",
        )

    total = 8 ** 11
    accepted = total // 2
    req(total == note["character_identity"]["total_mod8_classes"], "mod8 domain cardinality drift")
    req(accepted == note["character_identity"]["accepted_mod8_classes"], "accepted cardinality drift")
    req(grf["fixed_selected64"]["fixed_coefficient_matrix_sha256"] == FIXED_SHA,
        "GRF02 fixed matrix identity drift")
    req(grf["fixed_selected64"]["free_coefficient_matrix_sha256"] == FREE_SHA,
        "GRF02 free matrix identity drift")
    req(grf["fixed_selected64"]["inverse_integer_matrix_sha256"] == B_SHA,
        "GRF02 inverse matrix identity drift")

    panel_replayed = False
    if ns.historical_replay:
        panel = load_historical_panel()
        kernel = panel["kernel"]
        req(panel.get("route_id") == "HPADJ-09_ex5", "HPADJ09 panel route drift")
        req(kernel["assignment_labels_1based"] == ASSIGNMENT_LABELS,
            "HPADJ09 panel assignment-label order drift")
        req(kernel["assigned_selected_positions_0based"] == fixed_positions,
            "HPADJ09 panel fixed-position order drift")
        req(int(kernel["modulus"]) == 8, "HPADJ09 panel modulus drift")
        req(int(kernel["unique_congruence_row_count"]) == 1,
            "HPADJ09 panel unique-row count drift")
        req(kernel["unique_congruence_rows_sha256"] == derived_rows_sha,
            "HPADJ09 panel unique-row hash does not match direct row derivation")
        req(kernel["free_hnf_sha256"] == check.hnf_sha256,
            "HPADJ09 panel free-HNF does not match direct oracle derivation")
        req(kernel["exact_oracle_matches_retained_free_hnf"] is True,
            "HPADJ09 panel exact-oracle/free-HNF contract drift")
        req(int(kernel["retained_fixed_image_size"]) == 2,
            "HPADJ09 panel fixed-image size drift")
        req(int(kernel["retained_accepted_mod8_classes"]) == accepted,
            "HPADJ09 panel accepted-class count drift")
        req(panel["aggregate"]["kernel_accepted_terminals"] == 17120,
            "HPADJ09 panel accepted terminal count drift")
        req(panel["aggregate"]["kernel_rejected_terminals"] == 17120,
            "HPADJ09 panel rejected terminal count drift")
        req(note["sources"]["hpadj09"]["panel_result_blob_sha1"] == HPADJ09_PANEL_BLOB,
            "equivalence note HPADJ09 panel blob lock drift")
        req(note["sources"]["hpadj09"]["panel_result_canonical_sha256"] == HPADJ09_PANEL_CANON,
            "equivalence note HPADJ09 panel canonical lock drift")
        panel_replayed = True

    print(json.dumps({
        "status": "PASS_EXACT_HPADJ09_GRF02_CHARACTER_EQUIVALENCE",
        "historical_panel_replayed": panel_replayed,
        "panel_blob_sha1": HPADJ09_PANEL_BLOB,
        "panel_canonical_sha256": HPADJ09_PANEL_CANON,
        "grf02_mod2_row": grf02_row,
        "derived_hpadj09_mod8_row": derived_hpadj09_row,
        "unique_rows_sha256": derived_rows_sha,
        "accepted_mod8_classes": accepted,
        "total_mod8_classes": total,
        "double_stack_forbidden": True,
        "main_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
