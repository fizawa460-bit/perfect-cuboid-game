#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "j2-2isogeny-cohomological-gate.json"
cert = json.loads(CERT.read_text(encoding="utf-8"))
claimed = cert.pop("canonical_sha256")
actual = hashlib.sha256(
    json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
assert actual == claimed == "7373416b8c0aa9ca232ba4c0a7ede76cd8400e9d0a79d84ac60d31d408f05a41"
assert cert["exact_gate"]["br_2torsion_implies_order2_sha_class"] is True
assert cert["exact_gate"]["order2_sha_class_automatically_has_named_2isogeny_squareclass"] is False
assert cert["exact_gate"]["shared_branch_support_Dplus_proves_isogeny_kernel_membership"] is False
assert cert["exact_gate"]["shared_branch_support_Dplus_proves_d_equals_Dplus"] is False
assert cert["exact_gate"]["candidate_C_Dplus_retained_conditionally"] is True
assert cert["candidate_count_before"] == 3
assert cert["candidate_count_after"] == 3
assert cert["j2_2isogeny_squareclass_selected"] is False
assert cert["j2_torsor_equation_materialized"] is False
assert cert["j2_marked_brauer_coordinate_selected"] is False
assert cert["stage33_12_closed_exact"] is False
assert cert["stage33_13_released"] is False
print("PASS", claimed)
