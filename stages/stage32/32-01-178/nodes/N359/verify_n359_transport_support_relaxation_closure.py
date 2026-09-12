#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

LOCKS = {
    ROOT / "stages/stage32/32-01-178/nodes/N356/OPTIMISTIC_EXCEPTIONAL_TRANSPORT_CAP_CONTRACT.md": "d2353cab9c175a680067c7ad4c24759b6dd15df3",
    ROOT / "stages/stage32/32-01-178/nodes/N357-engine/verify_n357_transport_support_capacity.py": "479c783cb42d0952cc310708106787147b499240",
    ROOT / "stages/stage32/32-01-178/nodes/N358/JOINT_TRANSPORT_SUPPORT_SATURATION_CONTRACT.md": "a9a6836dc201feefd37bebb2f6c0ef42e8faaee4",
    ROOT / "stages/stage32/32-01-178/nodes/N358/RESULT.json": "e42c2b6cc6128c4666372b0c3f3c172afc006d7f",
    ROOT / "stages/stage32/32-01-178/nodes/N358/HOSTILE-AUDIT-PASS.json": "7b36e0159987ef65485d36fa2d672c8ee3a1ff33",
    ROOT / "stages/stage32/32-01-178/nodes/N358/STATE.json": "6091b0da0acc3fb4b3b2143327f7d57f5323668e",
    ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json": "0a46b34e278688240656b4977e9cb7f589e90e06",
}

EXPECTED_N358_REVIEW = 5184322011
EXPECTED_N358_REMAINING_STRATA = 17_128
EXPECTED_N358_REMAINING_TERMINALS = 47_589_703_313_957_134_966_240
EXPECTED_N358_RESULT_CANONICAL = "383921ed9387693a8cfa300a9629f629f3a20ed4272979508441c7b13af5a287"
HMAX = 96
RAW_BRUTE_HMAX = 16
AGGREGATE_BRUTE_HMAX = 9


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def s0(h: int) -> int:
    return min(16, 2 * h)


def sa(h: int, a: int) -> int:
    d = 2 * h
    return min(13, d - a, d - 2 * a + 4, h + 5)


def s3(h: int, b: int, c: int) -> int:
    d = 2 * h
    return min(9, d - b - c, d - 2 * b, d - 2 * c + 1)


def capacities(h: int, a: int, b: int, c: int) -> tuple[int, int, int]:
    B = h - b
    C = h - c
    return 2 * h, 2 * h - a, min(B + C, 2 * B)


def j0_formula(h: int, r: int) -> int:
    return min(r, s0(h))


def ja_formula(h: int, a: int, r: int) -> int:
    return min(r, sa(h, a))


def j3_formula(h: int, b: int, c: int, r: int) -> int:
    B = h - b
    R3 = capacities(h, 0, b, c)[2]
    loss = int(b >= c and B >= 5 and r == R3)
    return min(r, s3(h, b, c) - loss)


def joint_formula(h: int, a: int, b: int, c: int, R: int) -> int:
    R0, RA, R3 = capacities(h, a, b, c)
    S = s0(h) + sa(h, a) + s3(h, b, c)
    loss = int(b >= c and h - b >= 5 and R == R0 + RA + R3)
    return min(R, S - loss)


def comp0_raw(h: int, r: int) -> int:
    best = -1
    for p in range(h + 1):
        for q in range(h - p + 1):
            for x in range(h - p + 1):
                y = r - p - q - x
                if y < 0 or x + y > h or q + y > h:
                    continue
                best = max(best, min(4, p) + min(4, q) + min(4, x) + min(4, y))
    return best


def compa_raw(h: int, a: int, r: int) -> int:
    B = h - a
    best = -1
    for z in range(B + 1):
        for x in range(B - z + 1):
            for y in range(B - z + 1):
                w = r - z - x - y
                if w < 0 or w > h - x or w > h - y:
                    continue
                best = max(best, int(z > 0) + min(4, x) + min(4, y) + min(4, w))
    return best


def comp3_raw(h: int, b: int, c: int, r: int) -> int:
    B = h - b
    C = h - c
    best = -1
    for z in range(B + 1):
        cap = min(B - z, C)
        for x in range(cap + 1):
            y = r - z - x
            if 0 <= y <= cap:
                best = max(best, int(z > 0) + min(4, x) + min(4, y))
    return best


def max_convolution(left: list[int], right: list[int]) -> list[int]:
    out = [-1] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a < 0:
            continue
        for j, b in enumerate(right):
            if b >= 0:
                out[i + j] = max(out[i + j], a + b)
    return out


def verify_raw_components() -> int:
    cases = 0
    for h in range(RAW_BRUTE_HMAX + 1):
        for r in range(2 * h + 1):
            assert comp0_raw(h, r) == j0_formula(h, r)
            cases += 1
        for a in range(h + 1):
            RA = 2 * h - a
            for r in range(RA + 1):
                assert compa_raw(h, a, r) == ja_formula(h, a, r)
                cases += 1
        for b in range(h + 1):
            for c in range(h + 1):
                R3 = capacities(h, 0, b, c)[2]
                for r in range(R3 + 1):
                    assert comp3_raw(h, b, c, r) == j3_formula(h, b, c, r)
                    cases += 1
    return cases


def verify_raw_aggregate() -> int:
    cases = 0
    for h in range(AGGREGATE_BRUTE_HMAX + 1):
        arr0 = [comp0_raw(h, r) for r in range(2 * h + 1)]
        for a in range(h + 1):
            RA = 2 * h - a
            arra = [compa_raw(h, a, r) for r in range(RA + 1)]
            left = max_convolution(arr0, arra)
            for b in range(h + 1):
                for c in range(h + 1):
                    R3 = capacities(h, a, b, c)[2]
                    arr3 = [comp3_raw(h, b, c, r) for r in range(R3 + 1)]
                    exact = max_convolution(left, arr3)
                    for R, got in enumerate(exact):
                        assert got == joint_formula(h, a, b, c, R), (h, a, b, c, R, got)
                        cases += 1
    return cases


def verify_full_domain_symbolics() -> tuple[int, int]:
    a_cases = 0
    bc_cases = 0
    for h in range(HMAX + 1):
        t = h // 2
        sat0 = 2 * min(4, t) + 2 * min(4, h - t)
        assert sat0 == s0(h)

        for a in range(h + 1):
            B = h - a
            satA = max(
                int(z > 0) + 2 * min(4, B - z) + min(4, a + z)
                for z in range(B + 1)
            )
            assert satA == sa(h, a), (h, a, satA, sa(h, a))
            assert sa(h, a) <= 2 * h - a
            a_cases += 1

        for b in range(h + 1):
            for c in range(h + 1):
                B = h - b
                C = h - c
                R3 = min(B + C, 2 * B)
                S3 = s3(h, b, c)
                if B <= C:
                    sat3 = 2 * min(4, B)
                    anomaly = B >= 5
                    assert sat3 == S3 - int(anomaly)
                    if anomaly:
                        assert R3 == 2 * B
                        assert S3 == 9
                        assert 1 + 2 * min(4, B - 1) == 9
                else:
                    sat3 = int(B - C > 0) + 2 * min(4, C)
                    anomaly = False
                    assert sat3 == S3

                d = 2 * h
                Cmax = min(3 * d, 3 * d + c - b)
                # M=a+b+c cancels a from this identity.
                assert 4 * h + b + c + R3 == Cmax

                # The only endpoint support loss is exactly the N358 scope.
                assert anomaly == (b >= c and h - b >= 5)
                bc_cases += 1
    return a_cases, bc_cases


def main() -> None:
    for path, expected in LOCKS.items():
        actual = git_blob_sha1(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual} != {expected}")

    receipt = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N358/HOSTILE-AUDIT-PASS.json").read_text())
    result = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N358/RESULT.json").read_text())
    state = json.loads((ROOT / "stages/stage32/32-01-178/nodes/N358/STATE.json").read_text())
    if receipt.get("status") != "PASS" or receipt.get("review_id") != EXPECTED_N358_REVIEW:
        raise ValueError("N358 hostile-audit authority regression")
    counts = receipt.get("consumed_counts", {})
    if counts.get("remaining_strata") != EXPECTED_N358_REMAINING_STRATA or counts.get("remaining_terminals") != EXPECTED_N358_REMAINING_TERMINALS:
        raise ValueError("N358 retained frontier regression")
    if result.get("canonical_sha256_without_this_field") != EXPECTED_N358_RESULT_CANONICAL:
        raise ValueError("N358 RESULT canonical regression")
    if state.get("status") != "AUDITED_NECESSARY_CUT_CONSUMED_BY_MAIN" or state.get("credit", {}).get("n358_main_pruning_credit") is not True:
        raise ValueError("N358 MAIN consumption regression")

    manifest = json.loads((ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json").read_text())
    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 population regression")
    hs = []
    for row_id in rows:
        d = int(row_id.split("-d", 1)[1])
        if d % 2:
            raise ValueError("FULL178 even-degree regression")
        hs.append(d // 2)
    if min(hs) != 4 or max(hs) != HMAX:
        raise ValueError("FULL178 half-degree domain regression")

    raw_component_cases = verify_raw_components()
    raw_aggregate_cases = verify_raw_aggregate()
    full_a_cases, full_bc_cases = verify_full_domain_symbolics()

    print(json.dumps({
        "verdict": "PASS_N359_OPTIMISTIC_TRANSPORT_SUPPORT_RELAXATION_CLOSURE_AUDIT_CANDIDATE",
        "n358_main_pruning_credit": True,
        "n359_main_pruning_credit": False,
        "source_remaining_strata": EXPECTED_N358_REMAINING_STRATA,
        "source_remaining_terminals": EXPECTED_N358_REMAINING_TERMINALS,
        "additional_rejected_exceptional_prefixes": 0,
        "additional_rejected_terminals": 0,
        "candidate_remaining_strata": EXPECTED_N358_REMAINING_STRATA,
        "candidate_remaining_terminals": EXPECTED_N358_REMAINING_TERMINALS,
        "raw_component_cases": raw_component_cases,
        "raw_aggregate_cases": raw_aggregate_cases,
        "full_domain_a_cases": full_a_cases,
        "full_domain_bc_cases": full_bc_cases,
        "hmax": HMAX,
        "n358_is_exact_joint_projection_of_n356_n357_relaxation": True,
        "transport_support_relaxation_route_exhausted_if_audited": True,
        "full178_complete": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
