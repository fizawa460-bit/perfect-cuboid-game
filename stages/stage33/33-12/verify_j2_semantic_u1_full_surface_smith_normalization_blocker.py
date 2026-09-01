#!/usr/bin/env python3
"""Independent network-free replay of the semantic-u1 Smith blocker."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-semantic-u1-full-surface-smith-normalization-blocker.json"
PRODUCER = HERE / "certify_j2_semantic_u1_full_surface_smith_normalization_blocker.py"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


spec = importlib.util.spec_from_file_location("semantic_u1_blocker_producer", PRODUCER)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.dont_write_bytecode = True
spec.loader.exec_module(module)

stored = json.loads(CERT.read_text(encoding="utf-8"))
body = dict(stored)
claimed = body.pop("canonical_sha256")
assert claimed == csha(body)
assert stored == module.build()

resolved = stored["exact_resolved_normalization"]
missing = stored["exact_missing_numeric_data"]
assert resolved["semantic_label"] == "u1"
assert resolved["semantic_coordinate_f2"] == [1, 0]
assert resolved["semantic_support_BigK_indices_1based"] == [2, 4, 9, 10, 47, 49]
assert resolved["arbitrary_factor_two_choice_remaining"] is False
assert resolved["arbitrary_14D_adapter_remaining"] is False
assert missing["required_rows_already_retained_1based"] == [47, 49]
assert missing["required_rows_missing_1based"] == [2, 4, 9, 10]
assert missing["proper_Br2_14D_coordinate_materialized"] is False
assert missing["first_75D_matrix_column_materialized"] is False
firewall = stored["promotion_firewall"]
assert firewall["finite_v4_kummer_columns_materialized"] == 0
assert not any(value for key, value in firewall.items()
               if key != "finite_v4_kummer_columns_materialized")

print(json.dumps({
    "success": True,
    "certificate_sha256": claimed,
    "normalization_formula_exact": True,
    "missing_BigK_rows": missing["required_rows_missing_1based"],
    "matrix_columns_materialized": 0,
}, sort_keys=True))
