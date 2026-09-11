#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

# Repository-hostile-audit dependency identity boundary for the live N356 replay.
# These are the transitive repository sources that are actually imported/read by
# verify_n356_optimistic_exceptional_transport.py through N355/N345, plus the
# N351/N352 contracts whose necessary inequalities are consumed by N356.
LOCKS = {
    "n220_exact_symbolic_count": (
        ROOT / "stages/stage32/32-01-178/nodes/N220/verify_n220_exact_symbolic_count.py",
        "5855ae0835a828ab56b7a6e93a42f6788b6f676a",
    ),
    "n220_exact_symbolic_count_fast": (
        ROOT / "stages/stage32/32-01-178/nodes/N220/verify_n220_exact_symbolic_count_fast.py",
        "1510533965c475baab577e30e4eb26ad58dc4ac8",
    ),
    "n351_hurwitz_contract": (
        ROOT / "stages/stage32/32-01-178/nodes/N351/GENERAL_FACTOR_HURWITZ_MASS_CAP_CONTRACT.md",
        "377c2c43b3c80644c5913586cee42e9a6ec1138d",
    ),
    "n352_degree_sum_contract": (
        ROOT / "stages/stage32/32-01-178/nodes/N352/DEGREE_SUM_SCALAR_HURWITZ_CONTRACT.md",
        "60295a86297330d83370cf32016c75a8244a2aa4",
    ),
    "n345_geometry_verifier": (
        ROOT / "stages/stage32/32-01-178/nodes/N345/verify_n345_kernel14_integral_self_square.py",
        "61094d69c20dfd1d47c5a94aab435c5976eb6c5b",
    ),
    "hperp_integral_adapter": (
        ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py",
        "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ),
    "pairing_prefix_engine": (
        ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py",
        "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ),
    "full178_manifest": (
        ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json",
        "0a46b34e278688240656b4977e9cb7f589e90e06",
    ),
    "retained_picard_bundle": (
        ROOT / "stages/stage33/33-07/picard_base_rows_retained.py",
        "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    ),
    "retained_picard_marking": (
        ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py",
        "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    ),
    # N355 preflight imports these modules at import time.  They are not used by
    # reconstruct_cell_geometry(), but pinning them closes import-time semantic
    # drift and side effects rather than relying on dead-code assumptions.
    "compressed_terminal_family": (
        ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py",
        "90ff82ed312dcc0cb32cf207935945f550e29170",
    ),
    "n220_filtered_terminal_indexer": (
        ROOT / "stages/stage32/32-01-178/nodes/N230/n220_filtered_terminal_indexer.py",
        "2c04cceb374971dbf83cb684bd8a17a2ee4b50ed",
    ),
    "compressed_terminal_indexer": (
        ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py",
        "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    ),
}


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def validate_n356_dependency_source_locks() -> dict[str, str]:
    observed: dict[str, str] = {}
    for name, (path, expected) in LOCKS.items():
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(
                f"N356 transitive source-lock regression {name}: {path}: {actual}!={expected}"
            )
        observed[name] = actual
    return observed


if __name__ == "__main__":
    observed = validate_n356_dependency_source_locks()
    print(f"PASS_N356_TRANSITIVE_SOURCE_LOCKS count={len(observed)}")
