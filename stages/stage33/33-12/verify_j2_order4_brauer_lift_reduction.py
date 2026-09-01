\
#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-order4-brauer-lift-reduction.json"
ORIENTATION = HERE / "j2-cv-d2-semantic-orientation.json"
SEMANTIC = HERE / "j2-semantic-kc-picard-basis.json"
U1 = HERE / "j2-semantic-u1-full-surface-smith-source.json"

def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

obj = json.loads(CERT.read_text())
body = dict(obj); claimed = body.pop("canonical_sha256")
assert claimed == "a524121930e1c712bd8d8220415ef1836b11cd6eb11f2bb44f70dc844f6d85b0" == csha(body)
ori = json.loads(ORIENTATION.read_text())
sem = json.loads(SEMANTIC.read_text())
u1 = json.loads(U1.read_text())
for src, key in [
    (ori, "semantic_orientation_sha256"),
    (sem, "semantic_picard_basis_sha256"),
    (u1, "semantic_u1_full_surface_smith_source_sha256"),
]:
    b = dict(src); got = b.pop("canonical_sha256")
    assert got == obj["source_locks"][key] == csha(b)
frac = ori["anti_isometry_check"]["generator_image_semantic_fractional_coordinates"]
coeff4 = [int(Fraction(x) * 4) for x in frac]
assert coeff4 == obj["semantic_order4_generator"]["fourfold_integer_coefficients"]
ind = sem["upstream_source_lock"]["indlistK_1based"]
terms = [[ind[i], coeff4[i]] for i in range(20) if coeff4[i] % 4]
assert terms == obj["semantic_order4_generator"]["BigK_terms_row_and_coefficient_mod4"]
doubled = [ind[i] for i,c in enumerate(coeff4) if c & 1]
assert doubled == [2,4,9,10,47,49] == u1["semantic_u1_pullback"]["BigK_support_1based"]
extra = [r for r,_ in terms if r not in doubled]
assert extra == [20,35,39,67]
assert obj["promotion_firewall"]["proper_Br2_14D_coordinate_materialized"] is False
print(json.dumps({"success": True, "canonical_sha256": claimed, "additional_rows": extra}, sort_keys=True))
