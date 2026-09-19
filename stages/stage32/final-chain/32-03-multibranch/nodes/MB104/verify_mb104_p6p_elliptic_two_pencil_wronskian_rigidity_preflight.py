#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-P6P-ELLIPTIC-TWO-PENCIL-WRONSKIAN-RIGIDITY-PREFLIGHT-CERTIFICATE.json").read_text())
r=d["retained"]; w=d["wronskian"]
assert r["common_line_bundle"] is True
assert r["degree_per_l"]==56
assert r["typewise_ramification_line_bundle_equalities"]==3
assert r["actual_typewise_ramification_divisors_equal"] is False
assert r["actual_full_wronskian_divisor_equal"] is False
assert w["line_bundle_on_elliptic_curve"]=="M^2"
assert w["full_ramification_class_same_for_every_pencil_in_M"] is True
assert w["class_equality_rigidifies_pencil"] is False
assert d["disposition"]=="PARK_P6P_AT_MISSING_ACTUAL_WRONSKIAN_DIVISOR_DATA"
assert d["next_leaf"]=="MB104-P6Q-TWO-PENCIL-NIELSEN-COUPLING-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: P6P Wronskian rigidity preflight wall")
print("same M fixes only the Wronskian line bundle M^2, not the Wronskian section")
print("next: P6Q simultaneous Nielsen coupling preflight")
