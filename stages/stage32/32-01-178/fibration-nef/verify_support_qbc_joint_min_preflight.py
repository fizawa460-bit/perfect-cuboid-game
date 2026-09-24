#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "run_hpadj22_support_qbc_local_row_b.py"
SOURCE_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
INF = 10**30


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "cannot load " + str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def min_square_sum_positive(total: int, positive_parts: int) -> int:
    total = int(total)
    k = int(positive_parts)
    if k == 0:
        return 0 if total == 0 else INF
    if not (1 <= k <= 2) or total < k:
        return INF
    q, r = divmod(total, k)
    return (k - r) * q * q + r * (q + 1) * (q + 1)


def joint_q_lower(b: int, c: int, t: int, support: int) -> int:
    """Exact relaxed min qBC at fixed (b,c,t,H-support).

    Variables are the seven retained H coordinates
      (x0,x1,x5,x6,x8,x9,x10).
    Put p=x1+x9. Then the four independent sum groups are
      (x1,x9): p,
      x5: b-p,
      (x0,x6): t-p,
      (x8,x10): c-t+p.
    For each p and exact positive-support allocation, balanced positive
    parts give the exact minimum sum of squares. Canonical ordering is
    deliberately relaxed, so this remains a safe necessary-condition bound.
    """
    b, c, t, support = map(int, (b, c, t, support))
    lo = max(0, t - c)
    hi = min(b, t)
    if lo > hi or not (0 <= support <= 7):
        return INF

    best = INF
    for p in range(lo, hi + 1):
        s_pair_b = p
        s_single = b - p
        s_pair_t = t - p
        s_pair_c = c - t + p

        single_support = int(s_single > 0)
        single_q = s_single * s_single

        for k_bpair in range(3):
            q_bpair = min_square_sum_positive(s_pair_b, k_bpair)
            if q_bpair >= INF:
                continue
            for k_tpair in range(3):
                q_tpair = min_square_sum_positive(s_pair_t, k_tpair)
                if q_tpair >= INF:
                    continue
                k_cpair = support - single_support - k_bpair - k_tpair
                q_cpair = min_square_sum_positive(s_pair_c, k_cpair)
                if q_cpair >= INF:
                    continue
                best = min(best, q_bpair + single_q + q_tpair + q_cpair)
    return best


def bounded_formula_regression(source) -> dict[str, int]:
    states = finite_states = strict_vs_separate = 0
    max_strict_gain = 0
    for b in range(9):
        for c in range(9):
            for t in range(b + c + 1):
                for support in range(8):
                    states += 1
                    old = source.aggregate_q_lower(b, c, t, support)
                    joint = joint_q_lower(b, c, t, support)
                    if joint < INF:
                        finite_states += 1
                        req(joint >= old, f"joint minimum weakened separate bound {(b,c,t,support,old,joint)}")
                        if joint > old:
                            strict_vs_separate += 1
                            max_strict_gain = max(max_strict_gain, joint - old)
    return {
        "states": states,
        "finite_states": finite_states,
        "strict_vs_separate": strict_vs_separate,
        "max_strict_gain": max_strict_gain,
    }


def bounded_literal_regression(source) -> dict[str, int]:
    literal: dict[tuple[int, int, int, int], int] = {}
    for xs in product(range(4), repeat=7):
        x0, x1, x5, x6, x8, x9, x10 = xs
        b = x1 + x5 + x9
        c = x0 + x6 + x8 + x10
        t = x0 + x1 + x6 + x9
        support = sum(int(v > 0) for v in xs)
        q = sum(v * v for v in xs)
        key = (b, c, t, support)
        literal[key] = min(literal.get(key, INF), q)

    strict_vs_separate = 0
    max_strict_gain = 0
    for key, literal_min in literal.items():
        joint = joint_q_lower(*key)
        req(joint == literal_min, f"joint formula != literal enumeration {key}: {joint}!={literal_min}")
        old = source.aggregate_q_lower(*key)
        if joint > old:
            strict_vs_separate += 1
            max_strict_gain = max(max_strict_gain, joint - old)

    return {
        "literal_keys": len(literal),
        "strict_vs_separate": strict_vs_separate,
        "max_strict_gain": max_strict_gain,
    }


def main() -> None:
    req(SOURCE.is_file() and blob(SOURCE) == SOURCE_BLOB, "support-qBC source drift")
    source = load(SOURCE, "stage32_178_support_qbc_joint_min_source")

    formula = bounded_formula_regression(source)
    req(
        formula == {
            "states": 5832,
            "finite_states": 2448,
            "strict_vs_separate": 536,
            "max_strict_gain": 24,
        },
        f"bounded formula regression summary drift {formula}",
    )

    literal = bounded_literal_regression(source)
    req(
        literal == {
            "literal_keys": 1564,
            "strict_vs_separate": 116,
            "max_strict_gain": 2,
        },
        f"bounded literal regression summary drift {literal}",
    )

    # High-mass witness inside the active b=36 / d=192 reconnaissance region.
    witness = (36, 89, 103, 5)
    old = source.aggregate_q_lower(*witness)
    joint = joint_q_lower(*witness)
    req((old, joint) == (3137, 3377), f"high-mass witness drift {(old,joint)}")

    out = {
        "schema": "STAGE32_32_01_178_SUPPORT_QBC_JOINT_BCT_SUPPORT_MIN_PREFLIGHT_V1",
        "status": "STRUCTURAL_STRICT_STRENGTHENING_PASS__ZERO_MAIN_CREDIT",
        "source_lock": {
            "support_qbc_worker_blob_sha1": SOURCE_BLOB,
        },
        "claim": {
            "fixed_data": "(b,c,t,H-support)",
            "exact_relaxed_minimum": "min qBC over seven nonnegative H coordinates satisfying b,c,t and exact positive-support count, with canonical ordering relaxed",
            "decomposition": "p=x1+x9; exact balanced-square minima on pair sums p, t-p, c-t+p plus singleton x5=b-p, minimized over p and support allocations",
            "dominance": "joint_q_lower >= max(support_q_lower,bc_t_q_lower) pointwise",
            "safety": "canonical ordering is relaxed, therefore every actual retained H tuple has qBC >= joint_q_lower",
            "actual_geometric_H_tuple_exactness_claimed": False,
        },
        "bounded_formula_regression": formula,
        "bounded_literal_enumeration": literal,
        "strict_high_mass_witness": {
            "b": 36,
            "c": 89,
            "t": 103,
            "support": 5,
            "old_separate_lower": old,
            "joint_lower": joint,
            "strict_gain": joint - old,
            "implication": "qBC in [3137,3376] previously admitted this t by the separate-max relaxation but is excluded by the simultaneous minimum",
        },
        "next_gate": "intersect the exact-tset candidate with joint_q_lower before bounded V48 weighted replay; compare incremental tightening against the exact-tset-only consumer",
        "firewalls": {
            "main_credit": False,
            "full178_numerical_census_changed": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    print("SUPPORT_QBC_JOINT_MIN_PREFLIGHT=" + json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
