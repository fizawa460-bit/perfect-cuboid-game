#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import pathlib

from flint import fmpz_mat
from sympy import Matrix

HERE = pathlib.Path(__file__).resolve().parent
TARGET = HERE / "run_signature_cell_affine_coset.py"
spec = importlib.util.spec_from_file_location("stage32_08_coset_base", TARGET)
base = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(base)

ORIGINAL_HNF = base.hnf_affine_full_row
base.ALGORITHM_ID = "D8_SIGNATURE_CELL_PICARD_BASIS_SEQUENTIAL_MOD8_HNF_COSET_GRAM_LLL_FP140_V1"


def canonicalize_column_lattice(L: Matrix) -> Matrix:
    raw = fmpz_mat(base.matrix_list(L.T))
    hnf_f = raw.hnf()
    hnf = Matrix(
        [[int(hnf_f[i, j]) for j in range(hnf_f.ncols())] for i in range(hnf_f.nrows())]
    )
    out = hnf.T
    assert out.shape == L.shape
    assert out.rank() == L.cols
    assert abs(int(out.det())) == abs(int(L.det()))
    return out


def sequential_mod8_preimage(C: Matrix, rhs: Matrix):
    """Exact affine preimage of C*x=rhs (mod 8), refined one row at a time."""
    assert C.cols == 64 and rhs.shape == (C.rows, 1)
    x0 = Matrix.zeros(64, 1)
    L = Matrix.eye(64)
    active = 0
    redundant = 0
    row_certificates = []

    for row_index in range(C.rows):
        c = C[row_index : row_index + 1, :]
        a = c * L
        a_mod = [int(a[0, j]) % base.DEN for j in range(64)]
        target = (int(rhs[row_index]) - int((c * x0)[0])) % base.DEN
        if not any(a_mod):
            if target:
                return None, None, {
                    "image_feasible": False,
                    "sequential_mod8": True,
                    "failed_row_index": row_index,
                    "active_row_count": active,
                    "redundant_row_count": redundant,
                }
            redundant += 1
            continue

        one = Matrix([a_mod + [-base.DEN]])
        point_u, kernel_u, cert = ORIGINAL_HNF(one, Matrix([target]))
        if not cert["image_feasible"]:
            return None, None, {
                "image_feasible": False,
                "sequential_mod8": True,
                "failed_row_index": row_index,
                "active_row_count": active,
                "redundant_row_count": redundant,
            }
        t0 = point_u[:64, :]
        K = kernel_u[:64, :]
        assert K.shape == (64, 64) and K.rank() == 64
        x0 = x0 + L * t0
        L = L * K
        # Row-wise congruences only depend on residues mod 8.  HNF reduction
        # changes the basis by a unimodular column transform and keeps the same
        # lattice while preventing coefficient growth over many refinements.
        L = canonicalize_column_lattice(L)
        active += 1
        row_certificates.append({
            "row_index": row_index,
            "one_row_image_basis_sha256": cert["image_basis_sha256"],
            "lattice_index_after_row": abs(int(L.det())),
        })
        prefix = C[: row_index + 1, :]
        prefix_rhs = rhs[: row_index + 1, :]
        assert all(int(v) % base.DEN == 0 for v in prefix * x0 - prefix_rhs)
        assert all(int(v) % base.DEN == 0 for v in prefix * L)

    assert all(int(v) % base.DEN == 0 for v in C * x0 - rhs)
    assert all(int(v) % base.DEN == 0 for v in C * L)
    cert = {
        "image_feasible": True,
        "sequential_mod8": True,
        "input_row_count": C.rows,
        "active_row_count": active,
        "redundant_row_count": redundant,
        "final_lattice_index": abs(int(L.det())),
        "final_lattice_sha256": base.matrix_sha256(L),
        "final_point_sha256": base.canonical_sha256([int(v) for v in x0]),
        "row_certificate_sha256": base.canonical_sha256(row_certificates),
    }
    return x0, L, cert


def hnf_dispatch(A: Matrix, b: Matrix):
    m, n = A.shape
    # Detect the only large augmented congruence map created by the base
    # implementation: [C | -8 I_m], with C having exactly 64 Picard columns.
    if n == 64 + m and m > 1:
        right = A[:, 64:]
        if right == -base.DEN * Matrix.eye(m):
            C = A[:, :64]
            x0, L, seq_cert = sequential_mod8_preimage(C, b)
            if x0 is None or L is None:
                return Matrix.zeros(n, 1), Matrix.zeros(n, 64), seq_cert
            z0_num = C * x0 - b
            zL_num = C * L
            assert all(int(v) % base.DEN == 0 for v in z0_num)
            assert all(int(v) % base.DEN == 0 for v in zL_num)
            z0 = Matrix([int(v) // base.DEN for v in z0_num])
            zL = Matrix([[int(zL_num[i, j]) // base.DEN for j in range(64)] for i in range(m)])
            point = x0.col_join(z0)
            kernel = L.col_join(zL)
            assert A * point == b
            assert A * kernel == Matrix.zeros(m, 64)
            return point, kernel, seq_cert
    return ORIGINAL_HNF(A, b)


base.hnf_affine_full_row = hnf_dispatch

if __name__ == "__main__":
    base.main()
