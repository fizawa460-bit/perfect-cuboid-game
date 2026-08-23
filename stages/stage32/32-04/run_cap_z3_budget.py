#!/usr/bin/env python3
"""Run the audited Stage32-02 Z3 shard with exact dual-certificate caps added."""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import sys
from typing import Any

from cap_certificate import verify_certificate


def load_predecessor() -> Any:
    path = pathlib.Path(__file__).resolve().parents[1] / "32-02" / "run_exact_z3_budget.py"
    spec = importlib.util.spec_from_file_location("stage32_02_z3_budget", path)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load Stage32-02 predecessor backend")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    cap_args, remaining = parser.parse_known_args()
    predecessor = load_predecessor()
    certificate = json.loads(cap_args.cap_certificate.read_text(encoding="utf-8"))
    original_add = predecessor.add_exact_constraints
    original_verify = predecessor.verify_model
    verified_core_hash: str | None = None

    def ensure_verified(core: dict[str, Any]) -> None:
        nonlocal verified_core_hash
        core_hash = core["canonical_sha256_without_this_field"]
        if verified_core_hash == core_hash:
            return
        verify_certificate(core, certificate)
        verified_core_hash = core_hash

    def capped_add(
        solver: Any,
        core: dict[str, Any],
        variables: list[Any],
        degree: int,
        *rest: Any,
    ) -> Any:
        ensure_verified(core)
        pairings, quadratic = original_add(
            solver, core, variables, degree, *rest
        )
        solver.add(*(value <= degree // 2 for value in pairings[:92]))
        solver.add(*(value <= degree // 4 for value in pairings[92:]))
        return pairings, quadratic

    def capped_verify(
        core: dict[str, Any], vector: list[int], degree: int, *rest: Any
    ) -> Any:
        ensure_verified(core)
        result = original_verify(core, vector, degree, *rest)
        pairings = [
            sum(int(row[j]) * int(vector[j]) for j in range(64))
            for row in core["raw_cross_pairings_with_basis"]
        ]
        assert all(value <= degree // 2 for value in pairings[:92])
        assert all(value <= degree // 4 for value in pairings[92:])
        result["intersection_caps_verified"] = True
        return result

    predecessor.add_exact_constraints = capped_add
    predecessor.verify_model = capped_verify
    sys.argv = [sys.argv[0], *remaining]
    predecessor.main()


if __name__ == "__main__":
    main()
