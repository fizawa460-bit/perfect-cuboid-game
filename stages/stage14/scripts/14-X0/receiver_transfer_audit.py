#!/usr/bin/env python3
"""Finite regression and fiber audit for Stage14-X0.

The enumeration is diagnostic, not an asymptotic proof.  It verifies that the
4cg and s7-21 coordinate packets are simultaneous exact functions of the same
physical pair, and measures several deliberately coarsened projection fibers.
"""

from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve()
S7_PATH = HERE.parents[1] / "14-s7-21" / "dual_crt_short_vector_audit.py"
spec = spec_from_file_location("stage14_s7_21", S7_PATH)
assert spec is not None and spec.loader is not None
s7 = module_from_spec(spec)
spec.loader.exec_module(s7)


def oddpart(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def packet(a: dict[str, int], b: dict[str, int]) -> dict[str, object]:
    (R, S, T, J), (alpha, beta, gamma, delta) = s7.four_cells(a, b)

    n_beta = alpha**2 * b["r"]**4 * a["z"]**2 + delta**2 * a["s"]**4 * b["z"]**2
    n_gamma = delta**2 * b["s"]**4 * a["z"]**2 + alpha**2 * a["r"]**4 * b["z"]**2
    n_S = R**2 * b["x"]**4 * a["omega"]**2 + J**2 * a["y"]**4 * b["omega"]**2
    n_T = J**2 * b["y"]**4 * a["omega"]**2 + R**2 * a["x"]**4 * b["omega"]**2
    assert n_beta % beta**2 == n_gamma % gamma**2 == 0
    assert n_S % S**2 == n_T % T**2 == 0
    qk = n_beta // beta**2
    qxi = n_S // S**2
    assert qk == n_gamma // gamma**2
    assert qxi == n_T // T**2

    hk_plus = delta**2 * a["s"]**2 * b["s"]**2 + alpha**2 * a["r"]**2 * b["r"]**2
    hxi_plus = J**2 * a["y"]**2 * b["y"]**2 + R**2 * a["x"]**2 * b["x"]**2
    Ck = oddpart(hk_plus // oddpart(S * T))
    Cxi = oddpart(hxi_plus // oddpart(beta * gamma))
    assert Ck == Cxi
    C = Ck
    assert qk % C == qxi % C == 0

    d = gcd(a["z"], b["z"])
    zratio = (a["z"] // d, b["z"] // d)
    assert zratio[1] * b["g"] * a["x"] * a["y"] == zratio[0] * a["g"] * b["x"] * b["y"]

    return {
        "physical": (a["P"], a["Q"], b["P"], b["Q"]),
        "labels": (a["xi"], a["k"]),
        "cells": (R, S, T, J, alpha, beta, gamma, delta),
        "common": (a["xi"], a["k"], C, qk // C, qxi // C),
        "crt": (a["xi"], a["k"], zratio),
        "joint": (a["xi"], a["k"], C, qk // C, qxi // C, zratio),
    }


def histogram(groups: dict[object, list[object]]) -> dict[int, int]:
    return dict(sorted(Counter(len(v) for v in groups.values()).items()))


def main() -> None:
    repo = HERE.parents[4]
    source_tokens = {
        "stages/stage14/14-4cg/result.md": "CoupledCommonCoreGaussianResidualIncidence",
        "stages/stage14/14-s7-21/result.md": "BalancedDualCRTShortVectorEnergy",
        "stages/stage14/14-t58/result.md": "SharedUCanonicalPrimeDeltaToroidalSecondMoment",
    }
    for rel, token in source_tokens.items():
        assert token in (repo / rel).read_text()

    result = (repo / "stages/stage14/14-X0/result.md").read_text()
    for token in (
        "CCGRI_BDCSVE_JOINT_EXACT_REFINEMENT_PROVED=true",
        "CCGRI_IMPLIES_BDCSVE_ESTIMATE=false",
        "S_TO_FIXED_U_EXACT_VARIABLE_TRANSFER_PROVED=false",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
    ):
        assert token in result

    summary = json.loads(
        (repo / "stages/stage14/data/14-X0/receiver_transfer_summary.json").read_text()
    )
    assert summary["current_exponent"] == "7/8"
    assert summary["new_power_saving_proved"] is False

    limit = 300
    state_groups: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for Q in range(2, limit + 1):
        for P in range(1, Q):
            if gcd(P, Q) == 1:
                st = s7.make_state(P, Q)
                state_groups[(st["xi"], st["k"])].append(st)

    packets: list[dict[str, object]] = []
    for states in state_groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                s7.audit_pair(a, b)
                packets.append(packet(a, b))

    assert packets
    projections: dict[str, dict[object, list[object]]] = {}
    for name in ("common", "crt", "joint"):
        groups: dict[object, list[object]] = defaultdict(list)
        for row in packets:
            groups[row[name]].append(row["physical"])
        projections[name] = groups

    common_max = max(map(len, projections["common"].values()))
    crt_max = max(map(len, projections["crt"].values()))
    joint_max = max(map(len, projections["joint"].values()))
    common_witness = next((k, v) for k, v in projections["common"].items() if len(v) == common_max)
    crt_witness = next((k, v) for k, v in projections["crt"].items() if len(v) == crt_max)

    print("Stage14-X0 receiver transfer audit: PASS")
    print(f"finite cutoff Q<={limit}")
    print(f"dual-cross physical pairs={len(packets)}")
    print(f"common projection fiber histogram={histogram(projections['common'])}")
    print(f"CRT projection fiber histogram={histogram(projections['crt'])}")
    print(f"joint projection fiber histogram={histogram(projections['joint'])}")
    print(f"common max fiber={common_max}; witness={common_witness}")
    print(f"CRT max fiber={crt_max}; witness={crt_witness}")
    print(f"joint max fiber={joint_max}")
    assert summary["finite_audit"]["dual_cross_pairs"] == len(packets)
    assert summary["finite_audit"]["common_projection_max_fiber"] == common_max
    assert summary["finite_audit"]["crt_projection_max_fiber"] == crt_max
    assert summary["finite_audit"]["joint_projection_max_fiber"] == joint_max
    print("exact same-pair joint refinement=verified")
    print("projection fiber B^o(1) uniformly in B=not proved")


if __name__ == "__main__":
    main()
