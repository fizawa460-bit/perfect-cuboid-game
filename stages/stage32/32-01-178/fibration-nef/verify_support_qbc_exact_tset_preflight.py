#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
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


def exact_relaxed_tset(source, *, b: int, c: int, support: int, qbc: int) -> tuple[int, ...]:
    """Exact t-set for the retained support/qBC lower-bound relaxation.

    This is not claimed to be the exact set of geometric H tuples.  It is
    exactly the parity-restricted set satisfying the already-proved retained
    aggregate_q_lower <= qBC necessary condition.  Every actual H tuple must
    lie in this set, so using distance to this set is safe.
    """
    parity = int(c) & 1
    return tuple(
        t
        for t in range(parity, int(b) + int(c) + 1, 2)
        if source.aggregate_q_lower(int(b), int(c), t, int(support)) <= int(qbc)
    )


def exact_distance(y: int, values: tuple[int, ...]) -> int:
    req(bool(values), "distance requested from empty exact relaxed t-set")
    return min(abs(int(y) - t) for t in values)


def hull_distance(y: int, values: tuple[int, ...], parity: int) -> int:
    req(bool(values), "distance requested from empty hull")
    lo, hi = values[0], values[-1]
    if y < lo:
        return lo - y
    if y > hi:
        return y - hi
    return (int(y) - int(parity)) & 1


def bounded_regression(source) -> dict[str, int]:
    """Independent finite regression of exact-set dominance over the old hull."""
    states = 0
    distance_cases = 0
    strict_distance_cases = 0

    for b in range(13):
        for c in range(13):
            parity = c & 1
            m = b + c
            for support in range(8):
                activation_thresholds = sorted({
                    source.aggregate_q_lower(b, c, t, support)
                    for t in range(parity, m + 1, 2)
                    if source.aggregate_q_lower(b, c, t, support) < INF
                })
                for qbc in activation_thresholds:
                    values = exact_relaxed_tset(
                        source, b=b, c=c, support=support, qbc=qbc
                    )
                    req(bool(values), f"activation threshold produced empty set {(b,c,support,qbc)}")
                    lo, hi = source.support_t_interval(
                        b=b, c=c, support=support, qbc=qbc
                    )
                    req(
                        (lo, hi) == (values[0], values[-1]),
                        f"retained hull endpoints drift {(b,c,support,qbc,lo,hi,values)}",
                    )
                    states += 1
                    for y in range(-2, m + 3):
                        exact = exact_distance(y, values)
                        hull = hull_distance(y, values, parity)
                        req(
                            exact >= hull,
                            f"exact t-set weakened hull distance {(b,c,support,qbc,y,exact,hull)}",
                        )
                        distance_cases += 1
                        strict_distance_cases += int(exact > hull)

    return {
        "threshold_states": states,
        "distance_cases": distance_cases,
        "strict_distance_cases": strict_distance_cases,
    }


def main() -> None:
    req(SOURCE.is_file() and blob(SOURCE) == SOURCE_BLOB, "support-qBC source drift")
    source = load(SOURCE, "stage32_178_support_qbc_exact_tset_source")

    regression = bounded_regression(source)
    req(regression == {
        "threshold_states": 3633,
        "distance_cases": 70927,
        "strict_distance_cases": 3010,
    }, f"bounded regression summary drift {regression}")

    # Relevant high-mass witness.  With total H support one and b+c=36,
    # qBC=36^2 permits only all mass on one side of the t/complement split.
    witness = exact_relaxed_tset(source, b=36, c=0, support=1, qbc=1296)
    req(witness == (0, 36), f"strict witness t-set drift {witness}")

    d = 192
    x4 = 39
    y = d // 2 - 2 * x4
    req(y == 18, "strict witness center drift")
    exact_z = exact_distance(y, witness)
    hull_z = hull_distance(y, witness, 0)
    req((exact_z, hull_z) == (18, 0), "strict witness distance drift")

    # Same Picard terms and rhs as the retained qcut_support formula.
    g = 1
    b = 36
    c = 0
    a_parity = 0
    rhs120 = (15 * d * d) // 2 + 120 * d + 240 - 240 * g
    p0 = (b + c) & 1
    hull_qcut = (rhs120 - 10 * hull_z * hull_z - 60 * p0 - 12 * a_parity) // 60
    exact_qcut = (rhs120 - 10 * exact_z * exact_z - 60 * p0 - 12 * a_parity) // 60
    req((hull_qcut, exact_qcut) == (4992, 4938), "strict witness qcut drift")

    out = {
        "schema": "STAGE32_32_01_178_SUPPORT_QBC_EXACT_RELAXED_TSET_PREFLIGHT_V1",
        "status": "STRUCTURAL_STRICT_STRENGTHENING_PASS__ZERO_MAIN_CREDIT",
        "source_lock": {
            "support_qbc_worker": str(SOURCE.relative_to(HERE.parent.parent.parent.parent)),
            "support_qbc_worker_blob_sha1": SOURCE_BLOB,
        },
        "claim": {
            "scope": "retained support/qBC lower-bound relaxation only",
            "exact_relaxed_tset": "T={t == c mod 2 : aggregate_q_lower(b,c,t,support) <= qBC}",
            "safety": "every actual retained H tuple satisfies the aggregate_q_lower necessary condition, hence its t lies in T",
            "dominance": "distance(y,T) >= distance(y, parity-hull(T)); replacing hull distance by exact-set distance can only lower the accepted qA/qBC cutoff",
            "actual_H_tuple_exactness_claimed": False,
        },
        "bounded_regression": regression,
        "strict_witness": {
            "b": 36,
            "c": 0,
            "support": 1,
            "qbc": 1296,
            "exact_relaxed_tset": list(witness),
            "d": d,
            "g": g,
            "x4": x4,
            "center_y": y,
            "hull_distance": hull_z,
            "exact_set_distance": exact_z,
            "hull_qcut": hull_qcut,
            "exact_set_qcut": exact_qcut,
            "qcut_tightening": hull_qcut - exact_qcut,
        },
        "next_gate": "implement a source-locked same-population V48 exact-set consumer and measure bounded incremental tightening before any production scaleout",
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
    print("SUPPORT_QBC_EXACT_RELAXED_TSET_PREFLIGHT=" + json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
