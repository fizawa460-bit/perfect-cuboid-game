#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-SHALLOW-JACOBIAN-TJURINA-VS-FRESH-WEAPON-SCAN-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_SHALLOW_JACOBIAN_TJURINA_VS_FRESH_WEAPON_SCAN_V1"
assert d["surface"]=={"H2":16,"K2":16,"c2":80,"chi_O":8}
assert d["carrier"]["C2"]=="336*l^2"
assert d["carrier"]["KdotC"]=="112*l"
assert d["tjurina"]["global_lower"]=="4*tau > 1008*l^2+336*l-3*B"
assert d["log_tangent"]["discriminant_exact"]=="304+224*l+1008*l^2-4*tau"
assert d["log_tangent"]["discriminant_after_local_bound"]=="<304-112*l+3*B"
assert d["log_tangent"]["quadratic_cancellation"] is True
assert d["log_tangent"]["branch_excess_linear_bound_known"] is False
assert d["log_tangent"]["semistability_known"] is False
assert d["fresh_secant"]["favorable_finite_l_coefficient_found"] is False
assert d["result"]["deep_route_selected"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_SHALLOW_JACOBIAN_TJURINA_VS_FRESH_WEAPON_SCAN_V1")
print("new exact interface: Delta_log < 304 - 112*l + 3*B")
print("one more shallow gate only: branch-excess / log-stability + unrelated fresh weapon")
