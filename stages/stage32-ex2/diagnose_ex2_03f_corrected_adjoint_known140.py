#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "stages/stage32/residual-32-01-production"
STAGE33_07 = ROOT / "stages/stage33/33-07"
V6_PATH = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
PARENT = ROOT / "stages/stage32-ex2/EX2-03/remaining-five-conic-restriction-preflight.json"
BLOCKER = ROOT / "stages/stage32-ex2/EX2-03/adjoint-nef-blocker-preflight.json"
TARGETS = [21, 24, 25, 30, 31]

sys.path.insert(0, str(HERE))
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402

EXPECTED_BLOBS = {
    V6_PATH: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    PARENT: "32e19797812f35ad15fc5cad7559be76140480ef",
    BLOCKER: "3c93705c2515346853b58e337add31fa0ad83e93",
    HERE / "hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True).strip()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def retained_degrees(marking: dict) -> list[int]:
    text = marking.get("hperp_text")
    if not isinstance(text, str):
        raise ValueError("retained marking missing hperp_text")
    lines = text.splitlines()
    n, m = map(int, lines[4].split())
    if (n, m) != (63, 140):
        raise ValueError(f"unexpected hperp dimensions {(n, m)}")
    records = [list(map(int, lines[5 + n + r].split())) for r in range(m)]
    if any(len(row) != 65 for row in records):
        raise ValueError("unexpected hperp record width")
    return [row[0] for row in records]


def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        actual = git_blob(path)
        if actual != expected:
            raise ValueError(f"source lock regression {path}: {actual} != {expected}")

    v6 = json.loads(V6_PATH.read_text())
    parent = json.loads(PARENT.read_text())
    blocker = json.loads(BLOCKER.read_text())
    assert parent["remaining_labels_1based"] == TARGETS
    assert blocker["input_geometry"]["labels_1based"] == TARGETS

    bundle = load_retained(STAGE33_07 / "picard_base_rows_retained.py", "ex203f_picard")
    marking = load_retained(STAGE33_07 / "stage32_picard_marking_retained.py", "ex203f_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    coords = adapter.class_coordinates_in_retained_basis
    full = coords * gram * coords.T
    if full.shape != (140, 140) or full != full.T:
        raise ValueError("full intersection replay regression")
    degrees = retained_degrees(marking)
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    if len(degrees) != 140 or len(pairings) != 140:
        raise ValueError("retained vector length regression")

    rows = []
    for target in TARGETS:
        i = target - 1
        others = [z for z in TARGETS if z != target]
        two_p = []
        for e in range(140):
            val = 2 * pairings[e] - 2 * int(full[i, e]) - 2 * degrees[e]
            val -= sum(int(full[z - 1, e]) for z in others)
            two_p.append(int(val))
        neg = [j + 1 for j, x in enumerate(two_p) if x < 0]
        zero = [j + 1 for j, x in enumerate(two_p) if x == 0]
        pos = [j + 1 for j, x in enumerate(two_p) if x > 0]
        # Exact consistency on the five target conics: correction kills the four -2 hits.
        assert two_p[i] == 4
        for z in others:
            assert two_p[z - 1] == 0
        rows.append({
            "target_label_1based": target,
            "definition": "2P_i = 2(V6-C_i-K_S) - sum_{j!=i, j in target5} C_j",
            "twoP_dot_all140": two_p,
            "twoP_dot_all140_sha256": csha(two_p),
            "negative_labels_1based": neg,
            "zero_labels_1based": zero,
            "positive_count": len(pos),
            "negative_count": len(neg),
            "zero_count": len(zero),
            "bounded_known140_nonnegative": len(neg) == 0,
            "target_self_twoP_dot": two_p[i],
            "other_four_target_twoP_dots": {str(z): two_p[z - 1] for z in others},
        })

    out = {
        "schema": "STAGE32EX2_EX2_03F_CORRECTED_ADJOINT_KNOWN140_DIAGNOSTIC_V1",
        "stage": "32EX2",
        "unit": "EX2-03F",
        "status": "EXACT_BOUNDED_KNOWN140_CORRECTED_ADJOINT_SCAN_COMPLETE",
        "source_locks": {
            "v6_blob_sha1": EXPECTED_BLOBS[V6_PATH],
            "v6_canonical_sha256": v6["canonical_sha256_without_this_field"],
            "ex2_03d_blob_sha1": EXPECTED_BLOBS[PARENT],
            "ex2_03d_canonical_sha256": parent["canonical_sha256_without_this_field"],
            "ex2_03e_blocker_blob_sha1": EXPECTED_BLOBS[BLOCKER],
            "ex2_03e_blocker_canonical_sha256": blocker["canonical_sha256_without_this_field"],
            "hperp_adapter_blob_sha1": EXPECTED_BLOBS[HERE / "hperp_integral_adapter.py"],
            "hperp_adapter_canonical_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "all140_retained_coordinates_sha256": adapter.certificate["all140_retained_coordinates_sha256"],
            "full_intersection_sha256": adapter.certificate["full_intersection_sha256"],
        },
        "target_labels_1based": TARGETS,
        "correction_semantics": {
            "purpose": "Cancel the four exact -2 intersections of A_i=V6-C_i-K with the other disjoint target conics using the natural half-sum correction.",
            "integral_scan_representation": "Use 2P_i to avoid fractional arithmetic.",
            "bounded_scope": "retained known-140 irreducible-curve population only",
            "global_nef_inference_allowed": False,
        },
        "rows": rows,
        "decision": {
            "if_any_negative_known140_hit": "The natural correction is still not nef, already witnessed inside the retained known-140 population; do not invoke a nef-based vanishing theorem.",
            "if_no_negative_known140_hit": "This is only bounded nonnegativity. A source-bound cone-generation or equivalent global nef adapter is still required before any vanishing theorem can be invoked.",
            "fallback": "If no global nef/contraction adapter is source-bound, route to EX2-04 explicit section/ideal/syzygy reconstruction outside the known140 monoid.",
        },
        "firewalls": {
            "known140_nonnegative_promoted_to_global_nef": False,
            "corrected_adjoint_promoted_to_nef": False,
            "H1_vanishing_proved": False,
            "restriction_evaluation_computed": False,
            "remaining_five_fixedness_classified": False,
            "fixed_part_fully_classified": False,
            "complete_H0_reconstructed": False,
            "integral_irreducible_genus1_member_constructed": False,
            "population_wide_no_genus1_member_proved": False,
            "stage32_main_credit": False,
            "Q602_excluded": False,
            "O210_excluded": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
