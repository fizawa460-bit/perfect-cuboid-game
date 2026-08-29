#!/usr/bin/env python3
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
P = ROOT / "j2-cv-to-discriminant-marking-obstruction.json"
D = json.loads(P.read_text())

assert D["schema"] == "STAGE33_12_J2_CV_TO_DISCRIMINANT_MARKING_OBSTRUCTION_V1"
assert D["two_exact_f2_spaces"]["cv_brauer_dimension"] == 2
assert D["two_exact_f2_spaces"]["semantic_discriminant_dimension"] == 2
assert D["adapter_torsor"]["group"] == "GL(2,F2)"
assert D["adapter_torsor"]["possible_linear_isomorphisms_count"] == 6
assert sorted(map(tuple,D["adapter_torsor"]["j2_possible_nonzero_images"])) == [(0,1),(1,0),(1,1)]
assert D["adapter_torsor"]["picard_lattice_and_galois_action_alone_selects_adapter"] is False
assert D["j2_coordinate_materialized"] is False
assert D["stage33_12_closed_exact"] is False
assert D["stage33_13_released"] is False
for k in ("theorem_credit","receiver_credit","endpoint_credit","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"):
    assert D[k] is False

expected = D.pop("canonical_sha256")
canonical = json.dumps(D,sort_keys=True,separators=(",",":")).encode()
actual = hashlib.sha256(canonical).hexdigest()
assert actual == expected, (actual, expected)
D["canonical_sha256"] = expected
print(expected)
