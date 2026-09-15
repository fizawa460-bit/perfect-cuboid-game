#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESIDUAL = ROOT / "stages/stage32/residual-32-01-production"
BUNDLE_DIR = ROOT / "stages/stage33/33-07"
EX5 = ROOT / "stages/stage32-ex5/hpadj-handoff"
PREFIX = RESIDUAL / "pairing_prefix_engine.py"
BUNDLE_SOURCE = BUNDLE_DIR / "picard_base_rows_retained.py"
INTERFACE = EX5 / "INTERFACE.json"
PRODUCER = EX5 / "hpadj_full178_terminal_picard64_adapter.py"

sys.path.insert(0, str(RESIDUAL))
sys.path.insert(0, str(BUNDLE_DIR))
from pairing_prefix_engine import PrefixMembershipOracle, RetainedBasisPairingTransform, csha, matrix_list
import picard_base_rows_retained as retained_bundle

TERMINAL_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
LOCKS = {
    "pairing_prefix_engine_blob_sha1": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "retained_bundle_source_blob_sha1": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "retained_bundle_canonical_sha256": "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c",
    "interface_blob_sha1": "8a30e3aa30777460f344eb19836dc725dd442329",
    "producer_blob_sha1": "756a859a5949b5054202228d9df005b6c55a20fc",
}


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def req(value: bool, message: str) -> None:
    if not value:
        raise RuntimeError(message)


def main() -> None:
    req(git_blob(PREFIX) == LOCKS["pairing_prefix_engine_blob_sha1"], "pairing-prefix source-lock drift")
    req(git_blob(BUNDLE_SOURCE) == LOCKS["retained_bundle_source_blob_sha1"], "retained-bundle source-lock drift")
    req(git_blob(INTERFACE) == LOCKS["interface_blob_sha1"], "EX5 interface source-lock drift")
    req(git_blob(PRODUCER) == LOCKS["producer_blob_sha1"], "EX5 producer source-lock drift")

    interface = json.loads(INTERFACE.read_text())
    req(interface["picard_completion"]["inverse_denominator"] == 8, "interface denominator drift")
    req(interface["picard_completion"]["terminal_fixed_selected_pairing_labels"] == TERMINAL_LABELS, "terminal pairing order drift")

    bundle = retained_bundle.load()
    req(bundle["canonical_sha256"] == LOCKS["retained_bundle_canonical_sha256"], "retained bundle canonical drift")
    transform = RetainedBasisPairingTransform.from_bundle(bundle)
    req(transform.den == 8, "pairing-transform denominator drift")

    selected_labels = list(transform.certificate["selected_known_indices_1based"])
    assignment_order = [selected_labels.index(label) for label in TERMINAL_LABELS]
    oracle = PrefixMembershipOracle(transform, assignment_order)
    check = oracle.checks[-1]

    forward_projection = Matrix([[int(transform.selected[i, j]) for j in range(64)] for i in assignment_order])
    snf = smith_normal_form(forward_projection, domain=ZZ)
    diag = []
    for i in range(min(snf.rows, snf.cols)):
        value = int(snf[i, i])
        if value:
            diag.append(abs(value))
    rank = len(diag)
    surjective = rank == len(TERMINAL_LABELS) and all(v == 1 for v in diag)
    oracle_unrestricted = check.modulus == 1 and len(check.coefficients) == 0 and check.quotient_index == 1
    req(surjective == oracle_unrestricted, "SNF/HNF extendability disagreement")

    coeff_rows = [list(row) for row in check.coefficients]
    result = {
        "schema": "STAGE32_BRIDGE_BR103_C3_PICARD64_FIXED_PAIRING_PROJECTION_REPLAY_V1",
        "status": "EXACT_REPLAY_PASS_NO_CREDIT",
        "candidate_id": "BR-C3-PICARD64-FIXED-PAIRING-PROJECTION",
        "source_locks": LOCKS,
        "terminal_pairing_labels": TERMINAL_LABELS,
        "selected_coordinate_indices_0based": assignment_order,
        "inverse_denominator": transform.den,
        "depth11_hnf": {
            "modulus": int(check.modulus),
            "active_congruence_rows": len(coeff_rows),
            "quotient_index": int(check.quotient_index),
            "hnf_sha256": check.hnf_sha256,
            "congruence_rows_sha256": csha(coeff_rows),
            "congruence_rows": coeff_rows if len(coeff_rows) <= 16 else coeff_rows[:16],
            "congruence_rows_truncated": len(coeff_rows) > 16,
        },
        "forward_projection_snf": {
            "shape": [forward_projection.rows, forward_projection.cols],
            "rank": rank,
            "nonzero_invariant_factors": diag,
            "projection_surjective_Z": surjective,
            "projection_matrix_sha256": csha(matrix_list(forward_projection)),
            "smith_matrix_sha256": csha(matrix_list(snf)),
        },
        "exact_conclusion": (
            "NO_INTRINSIC_FIXED_PAIRING_CONGRUENCE: every integer terminal x11 extends to an integral primitive retained Picard64 class at raw lattice level"
            if surjective
            else "NONTRIVIAL_INTRINSIC_FIXED_PAIRING_CONGRUENCE: terminal x11 must satisfy the retained HNF congruence rows"
        ),
        "firewall": {
            "geometric_effectivity_inferred": False,
            "current_main_residual_population_identity_inferred": False,
            "main_pruning_credit": False,
            "merge_authorized": False,
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
