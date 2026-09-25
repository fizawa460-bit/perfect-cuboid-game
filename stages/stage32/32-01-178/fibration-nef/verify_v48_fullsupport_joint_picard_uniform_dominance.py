#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUPPORT = HERE / "run_hpadj22_support_qbc_local_row_b.py"
SUPPORT_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
JOINT = HERE / "verify_support_qbc_joint_min_preflight.py"
JOINT_BLOB = "490db30dc7e4bfc42da0e6dd9947a644dea14275"
PROBE = HERE / "run_v48_fullsupport_joint_picard_cell_probe.py"
PROBE_BLOB = "048b61e9cd93d97afa3e22f47eab98904bde85af"
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

def nearest_hull_distance(y: int, lo: int, hi: int, parity: int) -> int:
    if y < lo:
        return lo - y
    if y > hi:
        return y - hi
    return (y - parity) & 1

def nearest_set_distance(y: int, vals: tuple[int, ...]) -> int:
    req(bool(vals), "distance to empty t-set")
    return min(abs(int(y) - int(t)) for t in vals)

def tsets(support, joint, *, b: int, c: int, s: int, qbc: int):
    parity = int(c) & 1
    domain = tuple(range(parity, int(b) + int(c) + 1, 2))
    separate = tuple(t for t in domain if support.aggregate_q_lower(b, c, t, s) <= qbc)
    joined = tuple(t for t in domain if joint.joint_q_lower(b, c, t, s) <= qbc)
    return separate, joined

def qcut(*, d: int, g: int, b: int, c: int, z: int, a_parity: int) -> int:
    p0 = (int(b) + int(c)) & 1
    p1 = int(a_parity) & 1
    rhs120 = (15 * int(d) * int(d)) // 2 + 120 * int(d) + 240 - 240 * int(g)
    return (rhs120 - 10 * int(z) * int(z) - 60 * p0 - 12 * p1) // 60

def bounded_regression(support, joint) -> dict[str, int]:
    threshold_states = strict_tset_states = empty_joint_states = 0
    qcut_states = qcut_empty_joint_states = strict_qcut_states = 0
    max_qcut_drop = 0

    for b in range(9):
        for c in range(9):
            parity = c & 1
            for s in range(8):
                domain = tuple(range(parity, b + c + 1, 2))
                separate_floor = {t: support.aggregate_q_lower(b, c, t, s) for t in domain}
                joint_floor = {t: joint.joint_q_lower(b, c, t, s) for t in domain}
                req(all(joint_floor[t] >= separate_floor[t] for t in domain),
                    f"joint floor weakened separate floor {(b,c,s)}")
                thresholds = sorted({
                    q for q in (*separate_floor.values(), *joint_floor.values()) if q < INF
                })
                for qbc in thresholds:
                    separate = tuple(t for t in domain if separate_floor[t] <= qbc)
                    joined = tuple(t for t in domain if joint_floor[t] <= qbc)
                    if not separate:
                        continue
                    threshold_states += 1
                    req(set(joined).issubset(separate), f"joint t-set escaped separate {(b,c,s,qbc)}")
                    strict_tset_states += int(len(joined) < len(separate))
                    empty_joint_states += int(not joined)
                    lo, hi = separate[0], separate[-1]
                    for d in (16, 24, 32):
                        for g in (0, 1):
                            for x4 in range(d // 2 + 1):
                                y = d // 2 - 2 * x4
                                zh = nearest_hull_distance(y, lo, hi, parity)
                                for ap in (0, 1):
                                    old = qcut(d=d, g=g, b=b, c=c, z=zh, a_parity=ap)
                                    if not joined:
                                        qcut_empty_joint_states += 1
                                        continue
                                    zj = nearest_set_distance(y, joined)
                                    new = qcut(d=d, g=g, b=b, c=c, z=zj, a_parity=ap)
                                    req(zj >= zh, f"joint set became closer than hull {(b,c,s,qbc,d,g,x4,ap)}")
                                    req(new <= old, f"joint Picard qcut weakened current fullsupport {(b,c,s,qbc,d,g,x4,ap,new,old)}")
                                    qcut_states += 1
                                    if new < old:
                                        strict_qcut_states += 1
                                        max_qcut_drop = max(max_qcut_drop, old - new)

    return {
        "threshold_states": threshold_states,
        "strict_tset_states": strict_tset_states,
        "empty_joint_states": empty_joint_states,
        "qcut_states_with_nonempty_joint_set": qcut_states,
        "qcut_states_with_empty_joint_set": qcut_empty_joint_states,
        "strict_qcut_states": strict_qcut_states,
        "max_qcut_drop": max_qcut_drop,
    }

def main() -> None:
    req(blob(SUPPORT) == SUPPORT_BLOB, "support worker blob drift")
    req(blob(JOINT) == JOINT_BLOB, "joint-min verifier blob drift")
    req(blob(PROBE) == PROBE_BLOB, "successor probe blob drift")
    support = load(SUPPORT, "uniform_dom_support")
    joint = load(JOINT, "uniform_dom_joint")

    # Universal mathematical implication used by the successor:
    # joint_q_lower is the exact minimum with (b,c,t,support) fixed over a
    # feasible set contained in each separate relaxation. Hence
    # joint_q_lower >= aggregate_q_lower = max(separate minima).
    # Therefore for fixed qBC:
    #   T_joint(qBC) subset T_separate(qBC) subset hull(T_separate).
    # Distance from y=d/2-2*x4 to T_joint is >= distance to the hull.
    # The retained Picard qA cutoff is monotone decreasing in that squared
    # distance, so qcut_joint <= qcut_current_fullsupport pointwise.
    # All downstream weights and eligible-e multiplicities are nonnegative.
    # Thus replacing the current hull by T_joint cannot increase any cell,
    # coordinate, or 384-coordinate summed upper bound.

    got = bounded_regression(support, joint)
    expected = {
        "threshold_states": 1120,
        "strict_tset_states": 524,
        "empty_joint_states": 238,
        "qcut_states_with_nonempty_joint_set": 137592,
        "qcut_states_with_empty_joint_set": 37128,
        "strict_qcut_states": 17742,
        "max_qcut_drop": 61,
    }
    req(got == expected, f"bounded dominance regression drift {got}")

    # Independent small strict qcut witness.
    separate, joined = tsets(support, joint, b=0, c=3, s=3, qbc=5)
    req(separate == (1, 3) and joined == (1,), f"small strict witness tsets drift {(separate,joined)}")
    zh = nearest_hull_distance(8, separate[0], separate[-1], 1)
    zj = nearest_set_distance(8, joined)
    old = qcut(d=16, g=0, b=0, c=3, z=zh, a_parity=0)
    new = qcut(d=16, g=0, b=0, c=3, z=zj, a_parity=0)
    req((zh, zj, old, new) == (5, 7, 62, 58), f"small strict qcut witness drift {(zh,zj,old,new)}")

    # High-mass structural witness already identified in the retained active
    # reconnaissance region. This is NOT a claim that qBC=3137 has retained
    # positive histogram mass; it only demonstrates a large exact floor gap.
    separate, joined = tsets(support, joint, b=36, c=89, s=5, qbc=3137)
    req(103 in separate and joined == (), f"high-mass structural threshold witness drift {(separate,joined)}")
    req(support.aggregate_q_lower(36, 89, 103, 5) == 3137, "old high-mass floor drift")
    req(joint.joint_q_lower(36, 89, 103, 5) == 3377, "joint high-mass floor drift")

    print("V48_FULLSUPPORT_JOINT_PICARD_UNIFORM_DOMINANCE=PASS")
    print("BOUNDED_REGRESSION=" + json.dumps(got, sort_keys=True))
    print("SMALL_STRICT_QCUT_WITNESS=old62_new58")
    print("HIGH_MASS_STRUCTURAL_WITNESS=3137_to_3377")
    print("RETAINED_MASS_STRICTNESS_CLAIMED=false")
    print("MAIN_CREDIT_CHANGED=false")

if __name__ == "__main__":
    main()
