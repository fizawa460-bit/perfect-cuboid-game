#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

P = Path(__file__).with_name("j2-branch-cohomology-route-reduction.json")
data = json.loads(P.read_text())
expected = data.pop("canonical_sha256")
canon = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
actual = hashlib.sha256(canon).hexdigest()
assert actual == expected, (actual, expected)
assert data["route_classification"]["branch_cohomological_map"] == "EQUIVALENT_FOR_CURRENT_MARKED_RECEIVER"
assert data["route_classification"]["candidate_removed"] is True
assert data["loop_guard"]["candidate_count_decreased"] is True
assert data["firewalls"]["stage33_12_closed_exact"] is False
assert data["firewalls"]["stage33_13_released"] is False
print("PASS", actual)
