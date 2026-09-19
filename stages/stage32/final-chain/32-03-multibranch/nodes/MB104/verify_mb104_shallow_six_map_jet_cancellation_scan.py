#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-SHALLOW-SIX-MAP-JET-CANCELLATION-SCAN-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_SHALLOW_SIX_MAP_JET_CANCELLATION_SCAN_V1"
assert d["differences"]["order_only_uniform_conductor_bound"] is False
p=d["polars"]
assert p["correct_quadratic_local_scale"] is True
assert p["different_degree"]=="336*l^2+112*l"
assert p["min_ramification_degree"]=="80*l"
assert p["min_polar_degree"]=="336*l^2+192*l"
assert p["leading_coefficient_closer"] is False
assert d["cuboid_syzygies"]["ramification_slack_removed"] is False
assert d["fresh_candidate"]["id"]=="GLOBAL_JACOBIAN_TJURINA_SCHEME"
assert d["fresh_candidate"]["naive_log_cern_closer"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_SHALLOW_SIX_MAP_JET_CANCELLATION_SCAN_V1")
print("order-only closed; polar scale tied; rotate to global Jacobian/Tjurina scheme")
