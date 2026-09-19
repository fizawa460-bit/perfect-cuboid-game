#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-SHALLOW-COMPOSITION-SCAN-A-B-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_SHALLOW_COMPOSITION_SCAN_AB_V1"
A=d["routeA"]; B=d["routeB"]
assert A["piene_lci_finite_normalization_applicable"] is True
assert A["six_polars_generate_local_jacobian"] is True
assert A["common_ramification_bound"]=="80*l"
assert A["shallow_coefficient_closer"] is False
assert B["ramification_order_only_bound"] is False
assert B["counterexample"]["ramification_orders"]==[1,1]
assert B["missing_datum"]=="HIGH_ORDER_JET_CANCELLATION_BETWEEN_PROJECTION_FUNCTIONS"
assert B["jet_cancellation_route_live"] is True
assert d["next"]["duplicate_32_01"] is False
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_SHALLOW_COMPOSITION_SCAN_AB_V1")
print("A: Piene adapter valid but no shallow coefficient closer")
print("B: ramification-only no-go; retain simultaneous jet-cancellation route")
