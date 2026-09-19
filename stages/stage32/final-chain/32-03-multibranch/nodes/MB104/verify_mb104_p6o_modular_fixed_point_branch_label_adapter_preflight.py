#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-P6O-MODULAR-FIXED-POINT-BRANCH-LABEL-ADAPTER-PREFLIGHT-CERTIFICATE.json").read_text())
f=d["findings"]
assert f["three_X2_diagonal_cusp_types_identified"] is True
assert f["three_stabilizer_types_identified"] is True
assert f["factorwise_X4_branch_value_node_table_found"] is False
assert f["exact_stage32_node_to_ordered_factor_branch_pair_adapter_found"] is False
assert f["new_modular_cusp_computation_required"] is True
assert d["disposition"]=="PARK_P6O_AT_MISSING_FACTORWISE_X4_CUSP_LABEL_TABLE"
assert d["next_leaf"]=="MB104-P6P-ELLIPTIC-TWO-PENCIL-WRONSKIAN-RIGIDITY-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: P6O modular branch-label adapter preflight wall")
print("published source identifies three X(2) cusp types, not the factorwise X(4) node-label table")
print("next: P6P elliptic two-pencil Wronskian rigidity preflight")
