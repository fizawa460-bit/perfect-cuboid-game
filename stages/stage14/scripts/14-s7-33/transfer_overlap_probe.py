#!/usr/bin/env python3
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
spec = spec_from_file_location("s733probe", HERE.with_name("shared_common_core_orientation_probe.py"))
assert spec is not None and spec.loader is not None
m = module_from_spec(spec)
spec.loader.exec_module(m)


def pq(st):
    return st["a"] * st["x"] * st["x"], st["b"] * st["y"] * st["y"]


def main():
    groups = m.ch.make_groups(600)
    checked = fail = 0
    max_st_v = max_st_cv = max_fail_overlap = 1
    nontriv_st_v = nontriv_st_cv = fail_with_overlap = 0
    first_failure = None
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                z = m.packet_probe(a, b)
                ST = z["S"] * z["T"]
                gv = gcd(ST, z["v"])
                gcv = gcd(ST, z["C"] * z["v"])
                max_st_v = max(max_st_v, gv)
                max_st_cv = max(max_st_cv, gcv)
                nontriv_st_v += int(gv > 1)
                nontriv_st_cv += int(gcv > 1)
                if z["odd_ST"] and not z["canonical_ok"]:
                    fail += 1
                    max_fail_overlap = max(max_fail_overlap, gcv)
                    fail_with_overlap += int(gcv > 1)
                    if first_failure is None:
                        first_failure = (pq(a), pq(b), z["C"], z["v"], z["S"], z["T"], gv, gcv)
                checked += 1
    assert first_failure is not None
    print("Stage14-s7-33 transfer overlap probe: PASS")
    print(f"finite physical pairs checked: {checked}")
    print(f"strong canonical split failures: {fail}")
    print(f"first exact physical counterexample: {first_failure}")
    print(f"max gcd(S*T,v_res): {max_st_v}; nontrivial packets: {nontriv_st_v}")
    print(f"max gcd(S*T,C*v_res): {max_st_cv}; nontrivial packets: {nontriv_st_cv}")
    print(f"canonical failures with nontrivial gcd(S*T,C*v_res): {fail_with_overlap}/{fail}")
    print(f"max transfer overlap on failures: {max_fail_overlap}")


if __name__ == "__main__":
    main()
