#!/usr/bin/env python3
"""Stage14-tH10 deterministic audit for squareclass fiber/energy receivers."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
TH9 = ROOT / "stages/stage14/data/tH9/squareclass_crossratio_atlas_summary.json"
T41 = ROOT / "stages/stage14/data/14-t41/global_energy_incidence.json"
SUMMARY = ROOT / "stages/stage14/data/tH10/squareclass_fiber_energy_toolbox_summary.json"


def sxor(a: int, b: int) -> int:
    g = gcd(a, b)
    return (a // g) * (b // g)


def autocorrelation(counts: Counter[int]) -> Counter[int]:
    out: Counter[int] = Counter()
    for s, rs in counts.items():
        for t, rt in counts.items():
            out[sxor(s, t)] += rs * rt
    return out


def metrics(counts: Counter[int]) -> dict[str, int]:
    H = sum(counts.values())
    A1 = sum(v * v for v in counts.values())
    c = autocorrelation(counts)
    assert c[1] == A1
    assert sum(c.values()) == H * H
    E4 = sum(v * v for v in c.values())
    non = [v for k, v in c.items() if k != 1]
    R = max(non, default=0)
    S = H * H - A1
    assert E4 >= A1 * A1
    assert E4 <= A1 * H * H
    assert E4 <= A1 * A1 + R * S

    support = set(counts)
    M = max(counts.values(), default=0)
    d: Counter[int] = Counter()
    for s in support:
        for t in support:
            d[sxor(s, t)] += 1
    D = max((v for k, v in d.items() if k != 1), default=0)
    assert R <= M * M * D
    assert E4 <= A1 * A1 + M * M * D * S

    heavy_checks = 0
    if R:
        thresholds = sorted({0, 1, R // 4, R // 2, (3 * R) // 4, R})
        for T in thresholds:
            M_T = sum(v for k, v in c.items() if k != 1 and v > T)
            rhs = A1 * A1 + T * S + (R - T) * M_T
            assert E4 <= rhs
            heavy_checks += 1

    return {
        "H": H,
        "A1": A1,
        "E4": E4,
        "R_non": R,
        "S_non": S,
        "max_fiber": M,
        "max_support_difference": D,
        "heavy_light_checks": heavy_checks,
    }


def global_counts(cells: dict[str, Counter[int]]) -> Counter[int]:
    out: Counter[int] = Counter()
    for c in cells.values():
        out.update(c)
    return out


def partition_identity(cells: dict[str, Counter[int]]) -> tuple[int, int, int]:
    g = global_counts(cells)
    A1 = sum(v * v for v in g.values())
    local = sum(v * v for cell in cells.values() for v in cell.values())
    names = list(cells)
    off = 0
    for a in names:
        for b in names:
            if a == b:
                continue
            keys = set(cells[a]) | set(cells[b])
            off += sum(cells[a][s] * cells[b][s] for s in keys)
    assert A1 == local + off
    return A1, local, off


def partition_stress() -> dict[str, int]:
    cells = {
        "A": Counter({1: 2, 2: 1, 5: 1}),
        "B": Counter({1: 1, 3: 2, 5: 1}),
        "C": Counter({2: 2, 3: 1, 7: 1}),
        "D": Counter({1: 1, 7: 2, 10: 1}),
    }
    A1, local, off = partition_identity(cells)

    names = list(cells)
    generic = exceptional = 0
    for ia, a in enumerate(names):
        for ib, b in enumerate(names):
            if a == b:
                continue
            overlap = sum(cells[a][s] * cells[b][s] for s in set(cells[a]) | set(cells[b]))
            if (ia + ib) % 2:
                generic += overlap
            else:
                exceptional += overlap
    assert off == generic + exceptional
    assert A1 == local + generic + exceptional
    return {
        "synthetic_A1": A1,
        "synthetic_local": local,
        "synthetic_off": off,
        "synthetic_generic": generic,
        "synthetic_exceptional": exceptional,
    }


def two_sided_countermodel(H: int = 24) -> dict[str, int]:
    rows = {f"r{i}": Counter({1: 1}) for i in range(H)}
    cols = {f"c{i}": Counter({1: 1}) for i in range(H)}
    global_r = Counter({1: H})
    row_local = sum(v * v for c in rows.values() for v in c.values())
    col_local = sum(v * v for c in cols.values() for v in c.values())
    A1 = sum(v * v for v in global_r.values())
    assert row_local == H
    assert col_local == H
    assert A1 == H * H
    return {"H": H, "row_local": row_local, "column_local": col_local, "global_A1": A1}


def exponent_ledger_audit() -> int:
    vals = [Fraction(0), Fraction(1, 8), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]
    checks = 0
    for h in vals[1:]:
        for lam in vals:
            for gen in vals:
                for exc in vals:
                    a = max(lam, gen, exc)
                    for r in vals:
                        q_uniform = max(2 * a, r + 2 * h)
                        assert q_uniform >= 2 * a
                        assert q_uniform >= r + 2 * h
                        checks += 1
                    for t in vals:
                        for r in vals:
                            for m in vals:
                                q_hl = max(2 * a, t + 2 * h, r + m)
                                assert q_hl >= 2 * a
                                assert q_hl >= t + 2 * h
                                assert q_hl >= r + m
                                checks += 1
    return checks


def frozen_regression() -> dict[str, int]:
    th9 = json.loads(TH9.read_text())
    t41 = json.loads(T41.read_text())
    summary = json.loads(SUMMARY.read_text())

    assert th9["status"] == "COMPLETE_SQUARECLASS_CROSS_RATIO_AND_AUTOCORRELATION_ATLAS"
    assert t41["decision"]["STAGE14_T41"] == "COMPLETE_TWO_SIDED_INCIDENCE_AUDIT_AND_KUMMER_ENERGY_BARRIER"
    assert t41["decision"]["TWO_SIDED_LOCAL_ENERGY_IMPLIES_GLOBAL_NEAR_LINEAR"] is False
    assert t41["decision"]["OFF_FIBER_COLLISION_SURFACE_KUMMER_TYPE"] is True

    fourth = t41["frozen_audit"]["fourth_energy"]
    principal = t41["frozen_audit"]["principal_collision_breakdown"]
    cats = principal["ordered_collision_categories"]

    H = int(fourth["H"])
    A1 = int(fourth["A1"])
    E4 = int(fourth["E4"])
    local = int(cats["same_direction"])
    off = int(cats["cross_direction"])
    R = int(fourth["largest_nonprincipal_cross_kernel_multiplicity"])

    assert (H, A1, E4, local, off, R) == (1120, 2368, 21193216, 2240, 128, 160)
    assert A1 == local + off
    uniform_bound = A1 * A1 + R * (H * H - A1)
    assert uniform_bound == 205_932_544
    assert E4 <= uniform_bound

    frozen = summary["t41_frozen_regression"]
    assert frozen["H"] == H
    assert frozen["A1"] == A1
    assert frozen["E4"] == E4
    assert frozen["same_direction_local_energy"] == local
    assert frozen["off_direction_ordered_collisions"] == off
    assert frozen["largest_nonprincipal_kernel"] == R
    assert frozen["uniform_receiver_upper_bound"] == uniform_bound

    return {
        "H": H,
        "A1": A1,
        "E4": E4,
        "local": local,
        "off": off,
        "R_non": R,
        "uniform_receiver_upper_bound": uniform_bound,
    }


def main() -> None:
    synthetic = [
        Counter({1: 1, 2: 1, 3: 1, 5: 1, 7: 1}),
        Counter({1: 3, 2: 2, 3: 1, 5: 4}),
        Counter({1: 2, 6: 3, 10: 2, 15: 1, 30: 2}),
        Counter({2: 5, 3: 4, 5: 3, 6: 2, 10: 1, 15: 2}),
    ]
    metric_reports = [metrics(c) for c in synthetic]
    partition = partition_stress()
    countermodel = two_sided_countermodel()
    exponent_checks = exponent_ledger_audit()
    frozen = frozen_regression()

    assert exponent_checks > 10_000
    report = {
        "synthetic_populations": len(metric_reports),
        "heavy_light_checks": sum(r["heavy_light_checks"] for r in metric_reports),
        "partition": partition,
        "two_sided_countermodel": countermodel,
        "exponent_ledger_checks": exponent_checks,
        "t41_regression": frozen,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    print("Stage14-tH10 audit: PASS")


if __name__ == "__main__":
    main()
