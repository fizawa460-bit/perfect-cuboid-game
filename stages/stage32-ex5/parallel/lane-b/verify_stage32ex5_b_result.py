#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULT = HERE.parent / "results" / "stage32ex5-b-result.json"
TABLE = HERE.parent / "results" / "stage32ex5-b-runtime-points.json"

r = json.loads(RESULT.read_text(encoding="utf-8"))
t = json.loads(TABLE.read_text(encoding="utf-8"))

assert r["schema"] == "STAGE32EX5_B_RESULT_V1"
assert r["lane"] == "stage32ex5-b"
assert r["target"] == "BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE"
assert r["status"] == "PASS"
assert r["authority"] == "SCRATCH_ONLY"
assert all(v is False for v in r["downstream_credit"].values())

nodes = t["nodes"]
assert t["schema"] == "STAGE32EX5_B_STOLL_RUNTIME_POINTS_V1"
assert t["authority"] == "SCRATCH_ONLY"
assert len(nodes) == 48
assert t["row_semantics"].startswith("nodes[k] is runtime exceptional k")
payloads = []
for c in nodes:
    assert len(c) == 7
    first = next(x for x in c if x != "0")
    assert first == "1"
    payloads.append(tuple(c))
assert len(set(payloads)) == 48
assert t["counts"] == {
    "runtime_exceptional": 48,
    "projective_nodes": 48,
    "unique_canonical_nodes": 48,
}
assert t["execution"]["conclusion"] == "success"
assert t["execution"]["checks"] == {
    "node_records": 48,
    "indices_0_through_47": True,
    "unique_normalized_points": True,
    "coordinate_arity_7": True,
    "runtime_error_seen": False,
}

print("STAGE32EX5_B_RESULT_OK")
