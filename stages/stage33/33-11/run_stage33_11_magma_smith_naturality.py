#!/usr/bin/env python3
"""Run the Stage33-11 direct naturality proof with an exact Magma Smith backend.

Only the implementation of the 64x64 integer Picard Smith decomposition is
replaced. Any other Smith decomposition used by legacy source-side quotient
code is delegated unchanged to SymPy. The proof script itself still verifies
D = U*G*V, the discriminant invariant factors, every transported action, the
V4 cohomology regressions, and the final H-equivariant Hom spaces. The Picard
Smith calculation is made from the same pinned Testa--Stoll source already
source-locked by Stage33-09/33-07.
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

import sympy as sp
import sympy.matrices.normalforms as normalforms

HERE = Path(__file__).resolve().parent
LEGACY = HERE.parent / "33-07"
TARGET = HERE / "certify_stage33_11_direct_smith_naturality.py"

sys.path.insert(0, str(LEGACY))
import stoll_cuboid_source as stoll  # noqa: E402

PINNED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
_called = False
original = normalforms.smith_normal_decomp


def magma_smith_normal_decomp(M: sp.Matrix, domain=None):
    global _called
    if M.rows != 64 or M.cols != 64:
        return original(M, domain=domain)
    if _called:
        raise SystemExit("Stage33-11 64x64 Picard Magma Smith backend unexpectedly called twice")
    _called = True

    _, core, blob, source_attempt = stoll.load_pinned_source()
    if blob != PINNED_BLOB:
        raise SystemExit(f"pinned Testa--Stoll source lock moved: {blob}")

    code = core + r'''
D33, U33, V33 := SmithForm(pmPic);
printf "STAGE33_11_SMITH_DIAG=%o\n", [Integers()!D33[j,j] : j in [1..64]];
for r in [1..64] do
  printf "STAGE33_11_SMITH_U_ROW_%o=%o\n", r, Eltseq(U33[r]);
  printf "STAGE33_11_SMITH_V_ROW_%o=%o\n", r, Eltseq(V33[r]);
end for;
printf "STAGE33_11_MAGMA_SMITH_DONE\n";
'''
    stdout, magma_attempt = stoll.run_magma(
        code,
        240,
        "Stage33-11 pinned Picard Smith",
        "perfect-cuboid-stage33-11/1.1",
    )
    if "STAGE33_11_MAGMA_SMITH_DONE" not in stdout:
        print(stdout)
        raise SystemExit("Stage33-11 Magma Smith phase did not reach done marker")

    diag = [int(x) for x in stoll._grab_magma_literal(stdout, "STAGE33_11_SMITH_DIAG")]
    if len(diag) != 64:
        raise SystemExit("Stage33-11 Magma Smith diagonal width regression")

    def rows(prefix: str) -> list[list[int]]:
        out = []
        for r in range(1, 65):
            row = [int(x) for x in stoll._grab_magma_literal(stdout, f"{prefix}_{r}")]
            if len(row) != 64:
                raise SystemExit(f"{prefix}_{r}: width regression")
            out.append(row)
        return out

    U = sp.Matrix(rows("STAGE33_11_SMITH_U_ROW"))
    V = sp.Matrix(rows("STAGE33_11_SMITH_V_ROW"))
    D = sp.diag(*diag)
    if D != U * M * V:
        raise SystemExit("Stage33-11 Magma Smith identity D=U*G*V failed locally")
    mods = [abs(x) for x in diag if abs(x) > 1]
    if mods != [2] * 4 + [4] * 6 + [8] * 4:
        raise SystemExit(f"Stage33-11 Magma Smith invariant-factor regression: {mods}")

    print(
        "STAGE33_11_MAGMA_SMITH=PASS "
        f"source_attempt={source_attempt} magma_attempt={magma_attempt} "
        f"nontrivial_factors={len(mods)} max_factor={max(mods)}"
    )
    return D, U, V


normalforms.smith_normal_decomp = magma_smith_normal_decomp
try:
    runpy.run_path(str(TARGET), run_name="__main__")
finally:
    normalforms.smith_normal_decomp = original

if not _called:
    raise SystemExit("Stage33-11 direct proof never requested its 64x64 Picard Smith decomposition")
