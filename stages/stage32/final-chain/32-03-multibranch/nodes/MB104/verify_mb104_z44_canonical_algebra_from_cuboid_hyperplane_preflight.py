#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name(
 "MB104-Z44-CANONICAL-ALGEBRA-FROM-CUBOID-HYPERPLANE-PREFLIGHT-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z44_CANONICAL_ALGEBRA_CUBOID_HYPERPLANE_PREFLIGHT_V1"
assert d["exact"]["canonical_index"]==3
assert d["exact"]["canonical_cover_degree"]==3
assert d["exact"]["O_P_descends_to_O_3KY"] is True
assert d["exact"]["formal_generator_on_all_exceptional_thickenings"] is True
assert d["graph_sufficiency"]["resolution_graph_plus_discrepancies_determine_cover_analytic_type"] is False
assert d["conclusion"]["canonical_algebra_materialized"] is False
assert d["conclusion"]["local_symmetric_euler_coefficient_computed"] is False
assert d["disposition"]=="PARK_Z44_AT_CANONICAL_ALGEBRA_MULTIPLICATION_INTERFACE"
assert d["next_leaf"]=="MB104-Z45-FULL-NULL-BOUNDARY-SABATINO-REOPTIMIZATION"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z44 canonical algebra interface wall")
print("index-three cover exists, but the local multiplication/equation is not materialized")
print("next: Z45 exact full-null-boundary Sabatino reoptimization")
