#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

INCIDENCE_EXPECTED = "efdecb5d5cef219fc39d931521cbc1890a4830b5296e3c6ff7e93ccb6fa6b143"
TANGENT_EXPECTED = "beffca388f2795296fd914a6345186dc6e594419f0fffb93896bda2c3896a636"

FIRST = {34, 35, 38, 39, 42, 43}
SECOND = {33, 36, 37, 40, 41, 44}
BLOCKS = [
    ({34, 35}, {33, 36}),
    ({38, 39}, {37, 40}),
    ({42, 43}, {41, 44}),
]
EXPECTED_CZERO_PAIRS = {(34, 33), (35, 36), (38, 37), (39, 40), (42, 41), (43, 44)}
EXPECTED_CNONZERO_PAIRS = {(34, 36), (35, 33), (38, 40), (39, 37), (42, 44), (43, 41)}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_incidence(path: Path) -> dict:
    data = json.loads(path.read_text())
    claimed = data.get("canonical_sha256_without_this_field")
    body = dict(data)
    body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != INCIDENCE_EXPECTED or actual != INCIDENCE_EXPECTED:
        raise ValueError(f"incidence certificate moved: claimed={claimed} actual={actual}")
    return data


def c_is_zero(encoded: list[int]) -> bool:
    if len(encoded) != 4:
        raise ValueError("Q(i) encoding width regression")
    an, ad, bn, bd = (int(x) for x in encoded)
    if ad == 0 or bd == 0:
        raise ValueError("zero denominator in Q(i) encoding")
    return an == 0 and bn == 0


def same_block(first: int, second: int) -> int:
    hits = [j + 1 for j, (fs, ss) in enumerate(BLOCKS) if first in fs and second in ss]
    if len(hits) != 1:
        raise ValueError(f"boundary pair escaped the three C2 blocks: {(first, second)}")
    return hits[0]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--incidence", type=Path, required=True)
    ap.add_argument("--tangent", type=Path, required=True)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    incidence = load_incidence(args.incidence)
    tangent = json.loads(args.tangent.read_text())
    if tangent.get("canonical_sha256") != TANGENT_EXPECTED:
        raise ValueError("retained tangent canonical SHA moved")

    models = tangent.get("exceptional_models", [])
    if len(models) != 48:
        raise ValueError(f"exceptional model count regression: {len(models)}")

    incidence_rows = {int(r["exceptional_label"]): r for r in incidence.get("rows", [])}
    if sorted(incidence_rows) != list(range(93, 141)):
        raise ValueError("incidence exceptional-label range regression")

    rows = []
    zero_pairs: Counter[tuple[int, int]] = Counter()
    nonzero_pairs: Counter[tuple[int, int]] = Counter()
    zero_labels = []
    nonzero_labels = []

    for i, model in enumerate(models, start=1):
        expected_id = f"EXC_{i:03d}"
        if model.get("exceptional_id") != expected_id:
            raise ValueError(f"exceptional model ordering moved at {i}: {model.get('exceptional_id')}")
        point = model.get("node_point_ambient_P6_L_basis")
        if not isinstance(point, list) or len(point) != 7:
            raise ValueError(f"ambient node point shape regression at {expected_id}")
        zero = c_is_zero(point[6])
        label = 92 + i
        ir = incidence_rows[label]
        first = int(ir["first_factor_boundary_label"])
        second = int(ir["second_factor_boundary_label"])
        if first not in FIRST or second not in SECOND:
            raise ValueError(f"marked boundary family regression at label {label}")
        block = same_block(first, second)
        pair = (first, second)
        if zero:
            zero_labels.append(label)
            zero_pairs[pair] += 1
        else:
            nonzero_labels.append(label)
            nonzero_pairs[pair] += 1
        rows.append({
            "exceptional_label": label,
            "exceptional_id": expected_id,
            "c_zero": zero,
            "c2_block": block,
            "first_factor_boundary_label": first,
            "second_factor_boundary_label": second,
        })

    if zero_labels != list(range(117, 141)):
        raise ValueError(f"c=0 exceptional labels moved: {zero_labels}")
    if nonzero_labels != list(range(93, 117)):
        raise ValueError(f"c!=0 exceptional labels moved: {nonzero_labels}")
    if set(zero_pairs) != EXPECTED_CZERO_PAIRS or any(v != 4 for v in zero_pairs.values()):
        raise ValueError(f"c=0 boundary-pair matching moved: {dict(zero_pairs)}")
    if set(nonzero_pairs) != EXPECTED_CNONZERO_PAIRS or any(v != 4 for v in nonzero_pairs.values()):
        raise ValueError(f"c!=0 boundary-pair matching moved: {dict(nonzero_pairs)}")

    result = {
        "schema": "STAGE32_POST1473_X8_MARKED_NODE_CZERO_PARTITION_REPLAY_V1",
        "stage": 32,
        "status": "PASS",
        "source_locks": {
            "incidence_canonical_sha256": INCIDENCE_EXPECTED,
            "tangent_canonical_sha256": TANGENT_EXPECTED,
        },
        "structure": {
            "c2_boundary_graph": "three disjoint K2,2 blocks, each realized edge carrying four exceptional nodes",
            "c_zero_exceptional_labels": [117, 140],
            "c_nonzero_exceptional_labels": [93, 116],
            "c_zero_count": 24,
            "c_nonzero_count": 24,
            "c_zero_pairs": {f"{a}:{b}": zero_pairs[(a, b)] for a, b in sorted(zero_pairs)},
            "c_nonzero_pairs": {f"{a}:{b}": nonzero_pairs[(a, b)] for a, b in sorted(nonzero_pairs)},
            "matching_statement": "Within each C2 K2,2 block, c=0 is one perfect matching and c!=0 is the complementary perfect matching; every matching edge has multiplicity four.",
        },
        "rows": rows,
        "firewall": "exact retained-node marking only; this does not identify a hypothetical O188 carrier defect branch with any node and excludes none of A/B/C by itself",
    }
    result["canonical_sha256_without_this_field"] = csha(result)

    text = json.dumps(result, sort_keys=True, separators=(",", ":"))
    print(text)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
