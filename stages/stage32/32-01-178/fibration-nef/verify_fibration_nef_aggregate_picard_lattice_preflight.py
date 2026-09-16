#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from pathlib import Path

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
RES = ROOT / "stages" / "stage32" / "residual-32-01-production"
RECOVERABILITY = HERE / "verify_fibration_nef_recoverability.py"
TD02_BRIDGE = HERE / "verify_fibration_nef_td02_aggregate_bridge.py"
PAIRING_ENGINE = RES / "pairing_prefix_engine.py"
SOURCE_BASE = "df3b29d20ef0f7da1e34fa92beada6418ad3a4ea"
LOCKS = {
    "recoverability": (RECOVERABILITY, "fbd8dad2194378a6bf77d12cc2c65ac03782f112"),
    "td02_aggregate_bridge": (TD02_BRIDGE, "ec0ed8d32e454115843740bad927b7f56bc3106c"),
}
ASSIGNMENT = (95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96)
AGGREGATE_ORDER = ("a", "b", "c", "t", "x4")
OBSERVABLE_ORDER = AGGREGATE_ORDER + ("e", "d", "r0", "r1", "r2", "r3", "r4")
L = Matrix([
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
])


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def lattice_certificate(rows: list[Matrix], names: tuple[str, ...]) -> dict:
    A = Matrix.vstack(*rows)
    req(A.rows == len(names) and A.cols == 64, "observable matrix shape regression")
    req(int(A.rank()) == A.rows, f"observable rows lost rank for {names}")
    H = hermite_normal_form(A)
    req(H.shape == (A.rows, A.rows), f"HNF shape regression for {names}")
    det = abs(int(H.det()))
    req(det != 0, f"HNF determinant vanished for {names}")
    inv = H.inv()
    modulus = 1
    for value in inv:
        modulus = math.lcm(modulus, int(sympy.denom(value)))
    inv_int_q = inv * modulus
    req(all(sympy.denom(v) == 1 for v in inv_int_q), "denominator clearing failed")
    inv_int = Matrix([
        [int(inv_int_q[i, j]) for j in range(inv_int_q.cols)]
        for i in range(inv_int_q.rows)
    ])
    congruence_rows = []
    if modulus != 1:
        for i in range(inv_int.rows):
            coeff = [int(inv_int[i, j]) % modulus for j in range(inv_int.cols)]
            if any(coeff):
                congruence_rows.append(coeff)
    cert = {
        "observable_order": list(names),
        "rank": int(A.rank()),
        "image_lattice_index_in_Zm": det,
        "membership_modulus": modulus,
        "active_congruence_rows": len(congruence_rows),
        "membership_coefficients_mod_q": congruence_rows,
        "observable_matrix_sha256": csha(matrix_list(A)),
        "column_hnf_sha256": csha(matrix_list(H)),
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    return cert


def main() -> None:
    # Lock executable dependencies before importing them.
    for name, (path, expected) in LOCKS.items():
        req(path.is_file(), f"missing source lock {name}")
        req(git_blob(path) == expected, f"source drift {name}")
    subprocess.run(
        ["git", "diff", "--quiet", SOURCE_BASE, "--", str(PAIRING_ENGINE.relative_to(ROOT))],
        cwd=ROOT,
        check=True,
    )

    vf = load_module(RECOVERABILITY, "stage32_178_fibration_recoverability_lattice")
    vf.lock_sources()
    sys.path.insert(0, str(RES))
    from hperp_integral_adapter import (  # noqa: E402
        HperpIntegralPairingAdapter,
        RETAINED_BASIS_KNOWN_LABELS_1BASED,
        _parse_hperp,
    )

    marking = vf.load_retained(vf.ST33 / "stage32_picard_marking_retained.py", "nef_lattice_marking")
    bundle = vf.load_retained(vf.ST33 / "picard_base_rows_retained.py", "nef_lattice_bundle")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    req(coords.shape == (140, 64) and gram.shape == (64, 64), "Picard64 shape regression")

    # H=K in this retained degree-16 model, reconstructed exactly as in the
    # recoverability preflight.
    _, degree, _, _, _ = _parse_hperp(marking["hperp_text"])
    degrees = [int(degree[i, 0]) for i in range(140)]
    retained_idx = [x - 1 for x in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    Hq = Matrix([[degrees[i] for i in retained_idx]]) * gram.inv()
    req(all(sympy.denom(v) == 1 for v in Hq), "H class is not integral")
    Hclass = Matrix([[int(v) for v in Hq]])
    req(int((Hclass * gram * Hclass.T)[0, 0]) == 16, "H square regression")

    def pairing_row(class_row: Matrix) -> Matrix:
        row = class_row * gram
        req(row.shape == (1, 64), "pairing row shape regression")
        req(all(sympy.denom(v) == 1 for v in row), "nonintegral pairing row")
        return Matrix([[int(v) for v in row]])

    assignment_pairings = [pairing_row(coords.row(lab - 1)) for lab in ASSIGNMENT]
    aggregate_rows = []
    for i in range(L.rows):
        row = Matrix([[0] * 64])
        for j in range(L.cols):
            if L[i, j]:
                row += int(L[i, j]) * assignment_pairings[j]
        aggregate_rows.append(row)

    # First isolate the TD02 aggregate image itself.  A unit 5x5 minor of L
    # already predicts index one; the Picard image calculation below checks
    # the actual retained lattice rather than only the formal Z^11 map.
    unit_minor = None
    import itertools
    for cols in itertools.combinations(range(L.cols), L.rows):
        det = int(L[:, list(cols)].det())
        if abs(det) == 1:
            unit_minor = {"columns_zero_based": list(cols), "determinant": det}
            break
    req(unit_minor is not None, "TD02 aggregate map is not visibly saturated")

    Etotal = Matrix([[0] * 64])
    for lab in range(93, 141):
        Etotal += coords.row(lab - 1)
    e_row = pairing_row(Etotal)
    d_row = pairing_row(Hclass)

    block_labels, _ = vf.recover_unordered_fibration_blocks()
    observed = {lab for lab in ASSIGNMENT if lab >= 93}
    residual_supports = [sorted(set(labels) - observed) for labels in block_labels[:5]]
    expected_supports = [
        [100],
        [104, 105, 106, 107, 108],
        [109, 110, 111, 112, 113, 114, 115, 116],
        [117, 118, 119, 120, 121, 122, 123, 124],
        [125, 126, 127, 128, 129, 130, 131, 132],
    ]
    req(residual_supports == expected_supports, "residual support regression")
    residual_rows = []
    for support in residual_supports:
        class_row = Matrix([[0] * 64])
        for lab in support:
            class_row += coords.row(lab - 1)
        residual_rows.append(pairing_row(class_row))

    rows = aggregate_rows + [e_row, d_row] + residual_rows
    profiles = []
    for depth in range(5, len(rows) + 1):
        profiles.append(lattice_certificate(rows[:depth], OBSERVABLE_ORDER[:depth]))

    out = {
        "schema": "STAGE32_32_01_178_FIBRATION_NEF_AGGREGATE_PICARD_LATTICE_PREFLIGHT_V1",
        "purpose": "measure exact Picard64 image-lattice congruences on the TD02 aggregate plus five residual fibration-block observables; no FULL178 census is run",
        "source_base_exact_head": SOURCE_BASE,
        "td02_aggregate_order": list(AGGREGATE_ORDER),
        "td02_aggregate_map_rank": int(L.rank()),
        "td02_aggregate_unit_minor_certificate": unit_minor,
        "formal_Z11_to_Z5_aggregate_image_saturated": True,
        "observable_order": list(OBSERVABLE_ORDER),
        "residual_supports_exceptional_labels_1based": residual_supports,
        "prefix_image_lattice_profiles": profiles,
        "full_observable_image_lattice": profiles[-1],
        "safe_rejection_rule": "a candidate observable vector is impossible if any listed HNF membership congruence is nonzero modulo membership_modulus",
        "rule_is_exact_for_linear_picard_lattice_extendability": True,
        "nonlinear_nef_or_Hperp_penalty_sufficiency_claimed": False,
        "production_execution_armed": False,
        "bounded_violation_census_run": False,
        "full178_census_run": False,
        "main_credit_changed": False,
        "theorem_credit_changed": False,
        "endpoint_credit_changed": False,
        "td02_additive_credit_claimed": False,
        "merge": False,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
