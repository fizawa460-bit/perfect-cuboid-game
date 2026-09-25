#!/usr/bin/env python3
"""Exact forced-zero rank collapse for the best AFFINE14 54D fiber.

AFFINE14's closest remaining fiber is

  base4=(0,6,2,6), A=6, AB=8, C=0, p100=6.

With all exceptional pairings nonnegative:
  * A-p100 = 0 forces the other 11 entries of quarter A to zero;
  * C = 0 forces all 12 entries of quarter C to zero;
  * D = e-AB-C = 0 forces all 12 entries of quarter D to zero.

Those are genuine linear equalities, not heuristic pruning.  This probe adds
the implied zero rows, extracts an independent exact fixed-map basis, and
computes the saturated residual lattice dimension before any enumeration.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from flint import fmpz_mat
from sympy import Matrix

ROOT = Path(__file__).resolve().parents[3]
ENGINE = ROOT / "stages/stage32-ex5/effectivity-affine/eff_affine01_fp58_engine.py"
ENGINE_BLOB = "e7857e9213ca9107edada1424012a7a1c902a625"

BASE4 = (0, 6, 2, 6)
A_MASS = 6
AB_MASS = 8
C_MASS = 0
P100 = 6
P100_INDEX = 99


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "module spec")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def independent_rows(rows: list[Matrix], targets: list[int]) -> tuple[Matrix, Matrix, list[int]]:
    full = Matrix.vstack(*rows)
    req(full.rows == len(targets), "target count")
    # Pivot columns of full.T select an exact independent subset of rows.
    pivots = list(full.T.rref()[1])
    selected = full[pivots, :]
    target = Matrix([targets[i] for i in pivots])
    req(selected.rank() == len(pivots), "independent row extraction")
    return selected, target, pivots


def main() -> None:
    req(ENGINE.is_file() and blob(ENGINE) == ENGINE_BLOB, "FP58 engine drift")
    eng = load(ENGINE, "stage32ex5_eff_affine15_engine")
    F6, _A6, _I6, _RK58, _R58, _L, _d, _c, _u, P, gram = eng.build()

    Arow = sum((P.row(i) for i in range(92, 104)), Matrix.zeros(1, 64))
    ABrow = sum((P.row(i) for i in range(92, 116)), Matrix.zeros(1, 64))
    Crow = sum((P.row(i) for i in range(116, 128)), Matrix.zeros(1, 64))
    P100row = P.row(P100_INDEX)

    D_MASS = eng.E - AB_MASS - C_MASS
    B_MASS = AB_MASS - A_MASS
    req((B_MASS, D_MASS) == (2, 0), "target mass decomposition")
    req(A_MASS - P100 == 0, "A remainder is not zero")

    base_rows = [F6.row(i) for i in range(6)] + [Arow, ABrow, Crow, P100row]
    base_targets = [eng.D, eng.E, *BASE4, A_MASS, AB_MASS, C_MASS, P100]
    req(Matrix.vstack(*base_rows).rank() == 10, "AFFINE14 fixed10 rank drift")

    groups = {
        "A_rest_zero": [i for i in range(92, 104) if i != P100_INDEX],
        "B_zero": list(range(104, 116)),
        "C_zero": list(range(116, 128)),
        "D_zero": list(range(128, 140)),
    }
    active = {
        "A_rest_zero": A_MASS - P100 == 0,
        "B_zero": B_MASS == 0,
        "C_zero": C_MASS == 0,
        "D_zero": D_MASS == 0,
    }
    req(active == {
        "A_rest_zero": True,
        "B_zero": False,
        "C_zero": True,
        "D_zero": True,
    }, "forced-zero pattern drift")

    added_rows = []
    added_targets = []
    forced_indices = []
    for name, indices in groups.items():
        if not active[name]:
            continue
        for i in indices:
            added_rows.append(P.row(i))
            added_targets.append(0)
            forced_indices.append(i)

    F, target, pivots = independent_rows(base_rows + added_rows, base_targets + added_targets)
    rank = F.rows
    req(rank == F.rank(), "fixed-map rank")
    kernel_dim = 64 - rank

    hf, tf = fmpz_mat(
        [[int(F[i, j]) for j in range(64)] for i in range(rank)]
    ).transpose().hnf(transform=True)
    H = Matrix([[int(hf[i, j]) for j in range(hf.ncols())] for i in range(hf.nrows())])
    T = Matrix([[int(tf[i, j]) for j in range(tf.ncols())] for i in range(tf.nrows())])
    req(abs(int(tf.det())) == 1, "HNF transform")
    req(H == T * F.T, "HNF replay")

    AT = T.T[:, :rank]
    K = T.T[:, rank:]
    I = F * AT
    req(K.shape == (64, kernel_dim), "collapsed kernel shape")
    req(F * K == Matrix.zeros(rank, kernel_dim), "collapsed kernel equality")
    req(K.rank() == kernel_dim, "collapsed kernel rank")

    icoord = I.inv() * target
    req(all(getattr(v, "q", 1) == 1 for v in icoord), "collapsed target HNF image")
    bp = AT * icoord
    req(all(getattr(v, "q", 1) == 1 for v in bp), "collapsed integral base point")
    req(F * bp == target, "collapsed base replay")

    R = -(K.T * gram * K)
    req(R.shape == (kernel_dim, kernel_dim) and R == R.T, "collapsed Gram")
    L, D = R.LDLdecomposition(hermitian=False)
    req(R == L * D * L.T and all(D[i, i] > 0 for i in range(D.rows)),
        "collapsed negative form not positive definite")

    pair = P * bp
    req(int(pair[P100_INDEX]) == P100, "p100 base replay")
    for i in forced_indices:
        req(int(pair[i]) == 0, f"forced pairing {i} base replay")

    # Also report all 16 zero-pattern dimensions.  The rank depends only on
    # which groups are forced to zero, not on their positive masses.
    pattern_rows = []
    names = list(groups)
    for mask in range(16):
        rows = list(base_rows)
        for bit, name in enumerate(names):
            if mask & (1 << bit):
                rows.extend(P.row(i) for i in groups[name])
        pattern_rank = Matrix.vstack(*rows).rank()
        pattern_rows.append({
            "mask": mask,
            "forced_groups": [name for bit, name in enumerate(names) if mask & (1 << bit)],
            "fixed_rank": int(pattern_rank),
            "kernel_dimension": 64 - int(pattern_rank),
        })

    out = {
        "schema": "STAGE32EX5_EFF_AFFINE15_FORCED_ZERO_COLLAPSE_V1",
        "status": "PASS_EXACT_FORCED_ZERO_COLLAPSE",
        "source_affine14_fiber": {
            "base4": list(BASE4),
            "A": A_MASS,
            "AB": AB_MASS,
            "B": B_MASS,
            "C": C_MASS,
            "D": D_MASS,
            "p100": P100,
        },
        "forced_zero_semantics": {
            "A_rest_indices_0based": groups["A_rest_zero"],
            "C_indices_0based": groups["C_zero"],
            "D_indices_0based": groups["D_zero"],
            "forced_zero_pairing_count": len(forced_indices),
            "reason": "nonnegative integer pairings with zero group mass",
        },
        "collapsed_lattice": {
            "candidate_row_count_before_independence": len(base_rows) + len(added_rows),
            "independent_fixed_rank": rank,
            "kernel_dimension": kernel_dim,
            "hnf_image_index": abs(int(I.det())),
            "target_hnf_integral": True,
            "restricted_negative_form_positive_definite": True,
            "selected_independent_row_indices": pivots,
        },
        "all_zero_patterns": pattern_rows,
        "interpretation": {
            "what_is_proved": (
                "The selected AFFINE14 fiber lives in a saturated exact lattice of the "
                "reported collapsed dimension after converting zero exceptional masses "
                "into their logically forced coordinate equalities."
            ),
            "next_exact_unit": (
                "Run one bounded exact Fincke-Pohst benchmark on this collapsed lattice; "
                "if it completes cheaply, then consider the other structurally similar "
                "remaining hierarchy fibers."
            ),
            "what_is_not_proved": (
                "No bad-shell UNSAT or effectivity statement follows from dimension "
                "collapse alone."
            ),
        },
        "credit": {
            "effectivity": False,
            "main": False,
            "receiver": False,
            "theorem": False,
            "endpoint": False,
            "merge": False,
        },
    }
    print("EFF_AFFINE15_ZERO_COLLAPSE=" + json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
