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
RELAXED = HERE / "verify_support_qbc_joint_min_preflight.py"
RELAXED_BLOB = "490db30dc7e4bfc42da0e6dd9947a644dea14275"
INF = 10**30


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(p: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, p)
    req(spec is not None and spec.loader is not None, "cannot load " + str(p))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def min_pair_positive(total: int, k: int) -> int:
    total, k = int(total), int(k)
    if k == 0:
        return 0 if total == 0 else INF
    if k == 1:
        return total * total if total >= 1 else INF
    if k == 2:
        if total < 2:
            return INF
        q, r = divmod(total, 2)
        return (2 - r) * q * q + r * (q + 1) * (q + 1)
    return INF


def min_pair_positive_with_first_lower(total: int, k: int, first_lower: int) -> int:
    """Exact min x^2+y^2 with x+y=total, x>=first_lower and exactly k positives."""
    total, k, first_lower = map(int, (total, k, first_lower))
    if k == 0:
        return 0 if total == 0 and first_lower <= 0 else INF
    if k == 1:
        if total < 1:
            return INF
        best = INF
        if total >= first_lower:
            best = min(best, total * total)  # (total,0)
        if first_lower <= 0:
            best = min(best, total * total)  # (0,total)
        return best
    if k == 2:
        if total < 2:
            return INF
        lo = max(1, first_lower)
        hi = total - 1
        if lo > hi:
            return INF
        candidates = {lo, hi}
        for x in (total // 2, (total + 1) // 2):
            candidates.add(max(lo, min(hi, x)))
        return min(x * x + (total - x) * (total - x) for x in candidates)
    return INF


def canonical_joint_q_lower(b: int, c: int, t: int, support: int) -> int:
    """Exact qBC minimum under fixed (b,c,t,H-support) and terminal canonicalization.

    H coordinates are (x0,x1,x5,x6,x8,x9,x10), with
      b=x1+x5+x9,
      c=x0+x6+x8+x10,
      t=x0+x1+x6+x9,
      x0<=x1,
      x0=x1 => (x5,x6)<=lex(x8,x9),
      x1+x8+x9+x10 == 0 mod 2.

    The parity rule is equivalent to t==c mod 2.  After fixing x0,x1,x9,
    x5 and x6 are forced and only x8+x10 remains.  The equality branch
    turns the lex condition into one lower bound on x8, so the remaining
    two-variable quadratic minimum is exact.
    """
    b, c, t, support = map(int, (b, c, t, support))
    if not (0 <= support <= 7) or ((t - c) & 1):
        return INF

    best = INF
    for x0 in range(min(c, t) + 1):
        for x1 in range(x0, min(b, t - x0) + 1):
            rem = t - x0 - x1  # x6+x9
            for x9 in range(max(0, rem - c), min(b - x1, rem) + 1):
                x5 = b - x1 - x9
                x6 = rem - x9
                pair_total = c - t + x1 + x9  # x8+x10
                if min(x5, x6, pair_total) < 0:
                    continue

                base_support = sum(int(v > 0) for v in (x0, x1, x5, x6, x9))
                pair_support = support - base_support
                if not (0 <= pair_support <= 2):
                    continue

                if x0 < x1:
                    pair_q = min_pair_positive(pair_total, pair_support)
                else:
                    # (x5,x6)<=lex(x8,x9):
                    # x8>x5, or x8=x5 with x6<=x9.
                    first_lower = x5 + int(x6 > x9)
                    pair_q = min_pair_positive_with_first_lower(
                        pair_total, pair_support, first_lower
                    )
                if pair_q >= INF:
                    continue

                q = (
                    x0*x0 + x1*x1 + x5*x5 + x6*x6 + x9*x9 + pair_q
                )
                best = min(best, q)
    return best


def bounded_formula_regression(relaxed) -> dict[str, int]:
    out = {
        "states": 0,
        "relaxed_joint_finite": 0,
        "canonical_finite": 0,
        "canonical_infeasible_relaxed_finite": 0,
        "strict_finite": 0,
        "equal_finite": 0,
        "max_strict_gain": 0,
        "weakening": 0,
    }
    for b in range(9):
        for c in range(9):
            for t in range(b + c + 1):
                if ((t - c) & 1):
                    continue
                for support in range(8):
                    out["states"] += 1
                    old = relaxed.joint_q_lower(b, c, t, support)
                    new = canonical_joint_q_lower(b, c, t, support)
                    if old < INF:
                        out["relaxed_joint_finite"] += 1
                    if new < INF:
                        out["canonical_finite"] += 1
                    if old < INF and new >= INF:
                        out["canonical_infeasible_relaxed_finite"] += 1
                    if old < INF and new < INF:
                        if new < old:
                            out["weakening"] += 1
                        elif new > old:
                            out["strict_finite"] += 1
                            out["max_strict_gain"] = max(
                                out["max_strict_gain"], new - old
                            )
                        else:
                            out["equal_finite"] += 1
    return out


def bounded_literal_regression(relaxed) -> dict[str, int]:
    literal: dict[tuple[int,int,int,int], int] = {}
    for xs in product(range(4), repeat=7):
        x0,x1,x5,x6,x8,x9,x10 = xs
        if x0 > x1:
            continue
        if x0 == x1 and (x5,x6) > (x8,x9):
            continue
        if (x1+x8+x9+x10) & 1:
            continue
        b = x1+x5+x9
        c = x0+x6+x8+x10
        t = x0+x1+x6+x9
        support = sum(int(v > 0) for v in xs)
        q = sum(v*v for v in xs)
        key = (b,c,t,support)
        literal[key] = min(literal.get(key, INF), q)

    mismatches = strict = max_gain = 0
    for key, exact in literal.items():
        got = canonical_joint_q_lower(*key)
        mismatches += int(got != exact)
        old = relaxed.joint_q_lower(*key)
        if got > old:
            strict += 1
            max_gain = max(max_gain, got-old)
    return {
        "literal_keys": len(literal),
        "formula_mismatches": mismatches,
        "strict_vs_relaxed_joint": strict,
        "max_strict_gain": max_gain,
    }


def active_panel_structural_scan(relaxed) -> dict[str, object]:
    rows = []
    crossing = []
    for c in (83,85,89):
        stats = {
            "c": c,
            "states": 0,
            "relaxed_joint_finite": 0,
            "canonical_finite": 0,
            "canonical_infeasible_relaxed_finite": 0,
            "strict_finite": 0,
            "max_strict_gain": 0,
            "strict_with_relaxed_floor_at_most_4992": 0,
            "crosses_qbc_cap_4992": 0,
        }
        b = 36
        for t in range(b+c+1):
            if ((t-c)&1):
                continue
            for support in range(8):
                stats["states"] += 1
                old = relaxed.joint_q_lower(b,c,t,support)
                new = canonical_joint_q_lower(b,c,t,support)
                if old < INF:
                    stats["relaxed_joint_finite"] += 1
                if new < INF:
                    stats["canonical_finite"] += 1
                if old < INF and new >= INF:
                    stats["canonical_infeasible_relaxed_finite"] += 1
                if old < INF and new < INF and new > old:
                    stats["strict_finite"] += 1
                    stats["max_strict_gain"] = max(stats["max_strict_gain"], new-old)
                    if old <= 4992:
                        stats["strict_with_relaxed_floor_at_most_4992"] += 1
                if old <= 4992 and new > 4992:
                    stats["crosses_qbc_cap_4992"] += 1
                    crossing.append({
                        "c": c, "t": t, "support": support,
                        "relaxed_joint_floor": old,
                        "canonical_joint_floor": None if new >= INF else new,
                        "canonical_infeasible": new >= INF,
                        "gain_if_finite": None if new >= INF else new-old,
                    })
        rows.append(stats)
    return {"rows": rows, "qbc_cap_crossing_states": crossing}


def main() -> None:
    req(SOURCE.is_file() and blob(SOURCE) == SOURCE_BLOB, "support worker blob drift")
    req(RELAXED.is_file() and blob(RELAXED) == RELAXED_BLOB, "relaxed joint verifier blob drift")
    source = load(SOURCE, "canonical_joint_source")
    relaxed = load(RELAXED, "canonical_joint_relaxed")

    formula = bounded_formula_regression(relaxed)
    req(formula == {
        "states": 2952,
        "relaxed_joint_finite": 1268,
        "canonical_finite": 1128,
        "canonical_infeasible_relaxed_finite": 140,
        "strict_finite": 137,
        "equal_finite": 991,
        "max_strict_gain": 24,
        "weakening": 0,
    }, f"bounded formula regression drift {formula}")

    literal = bounded_literal_regression(relaxed)
    req(literal == {
        "literal_keys": 670,
        "formula_mismatches": 0,
        "strict_vs_relaxed_joint": 65,
        "max_strict_gain": 4,
    }, f"bounded literal regression drift {literal}")

    witness = (36,89,103,5)
    separate = source.aggregate_q_lower(*witness)
    old = relaxed.joint_q_lower(*witness)
    new = canonical_joint_q_lower(*witness)
    req((separate,old,new) == (3137,3377,3617),
        f"active witness drift {(separate,old,new)}")

    panel = active_panel_structural_scan(relaxed)
    req(panel["rows"] == [
        {"c":83,"states":480,"relaxed_joint_finite":294,"canonical_finite":293,
         "canonical_infeasible_relaxed_finite":1,"strict_finite":188,
         "max_strict_gain":1800,"strict_with_relaxed_floor_at_most_4992":184,
         "crosses_qbc_cap_4992":3},
        {"c":85,"states":488,"relaxed_joint_finite":299,"canonical_finite":298,
         "canonical_infeasible_relaxed_finite":1,"strict_finite":192,
         "max_strict_gain":1656,"strict_with_relaxed_floor_at_most_4992":186,
         "crosses_qbc_cap_4992":2},
        {"c":89,"states":504,"relaxed_joint_finite":309,"canonical_finite":308,
         "canonical_infeasible_relaxed_finite":1,"strict_finite":198,
         "max_strict_gain":1368,"strict_with_relaxed_floor_at_most_4992":189,
         "crosses_qbc_cap_4992":4},
    ], f"active panel summary drift {panel['rows']}")
    req(len(panel["qbc_cap_crossing_states"]) == 9,
        "active panel qBC-cap crossing count drift")

    out = {
        "schema": "STAGE32_32_01_178_SUPPORT_QBC_CANONICAL_JOINT_MIN_PREFLIGHT_V1",
        "status": "EXACT_CANONICAL_H_MIN_STRICTLY_DOMINATES_RELAXED_JOINT__ZERO_MAIN_CREDIT",
        "source_locks": {
            "support_qbc_worker_blob_sha1": SOURCE_BLOB,
            "relaxed_joint_min_verifier_blob_sha1": RELAXED_BLOB,
        },
        "claim": {
            "fixed_data": "(b,c,t,H-support)",
            "exact_minimum": "minimum qBC over the seven retained H coordinates with the terminal x0<=x1 / equality-lex canonicalization and retained parity enforced",
            "dominance": "canonical_joint_q_lower >= relaxed joint_q_lower >= aggregate_q_lower pointwise",
            "safety": "every retained H tuple satisfies the canonical constraints, so every retained tuple has qBC >= canonical_joint_q_lower",
            "actual_weighted_v48_gain_claimed": False,
        },
        "bounded_formula_regression": formula,
        "bounded_literal_enumeration": literal,
        "active_structural_witness": {
            "b":36,"c":89,"t":103,"support":5,
            "separate_floor":separate,
            "relaxed_joint_floor":old,
            "canonical_joint_floor":new,
            "canonical_gain_vs_relaxed":new-old,
            "canonical_gain_vs_separate":new-separate,
        },
        "active_three_cell_structural_scan": panel,
        "next_gate": "use canonical_joint_q_lower in the same full-support+Picard successor counter; numerical V48 tightening still requires the authorized weighted retained-histogram replay",
        "firewalls": {
            "main_credit": False,
            "full178_numerical_census_changed": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
    }
    print("SUPPORT_QBC_CANONICAL_JOINT_MIN_PREFLIGHT=" + json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
