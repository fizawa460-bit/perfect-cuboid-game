#!/usr/bin/env python3
"""Run the direct free d2_11 verifier with the exact periodic-resolution H1 coordinate order.

`derive_absolute_h1_picu_exact.py` stores the 12 periodic-resolution H1 coordinates
under historical JSON field names `cc_value_free_coordinates` then
`ct_value_free_coordinates`. From its cob(0)=[Gb-I | Ga-I] construction,
the first six coordinates are the ct-generator value and the second six are
the cc-generator value. This adapter corrects that convention, runs the direct
chain-level verifier, and enforces the audited closure condition that all five
free-side d2_11 images vanish.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
path = ROOT / "audit_materialize_free_d2_11.py"
src = path.read_text(encoding="utf-8")
old = '''    a6 = [int(x) for x in rep["cc_value_free_coordinates"]]\n    b6 = [int(x) for x in rep["ct_value_free_coordinates"]]\n    if len(a6) != 6 or len(b6) != 6:\n        raise SystemExit("bad free H1 representative width")\n    # Verify the two involution relations and the commuting-square relation.\n    if any(add(a6, free6_act(a6, "cc"))):\n        raise SystemExit("free H1 cc involution cocycle relation failed")\n    if any(add(b6, free6_act(b6, "ct"))):\n        raise SystemExit("free H1 ct involution cocycle relation failed")\n    cct6_a = add(free6_act(a6, "ct"), b6)\n    cct6_b = add(free6_act(b6, "cc"), a6)\n    if cct6_a != cct6_b:\n        raise SystemExit("free H1 commuting cocycle relation failed")\n    p = {\n        "id": [0] * 64,\n        "cc": [0] * 58 + a6,\n        "ct": [0] * 58 + b6,\n        "cct": [0] * 58 + cct6_a,\n    }\n'''
new = '''    # Historical field names follow the tensor-resolution block order.\n    # cob(0)=[Gb-I | Ga-I], so first six = ct value, second six = cc value.\n    ct6 = [int(x) for x in rep["cc_value_free_coordinates"]]\n    cc6 = [int(x) for x in rep["ct_value_free_coordinates"]]\n    if len(cc6) != 6 or len(ct6) != 6:\n        raise SystemExit("bad free H1 representative width")\n    if any(add(cc6, free6_act(cc6, "cc"))):\n        raise SystemExit("free H1 cc involution cocycle relation failed")\n    if any(add(ct6, free6_act(ct6, "ct"))):\n        raise SystemExit("free H1 ct involution cocycle relation failed")\n    cct6_a = add(free6_act(cc6, "ct"), ct6)\n    cct6_b = add(free6_act(ct6, "cc"), cc6)\n    if cct6_a != cct6_b:\n        raise SystemExit("free H1 commuting cocycle relation failed")\n    p = {\n        "id": [0] * 64,\n        "cc": [0] * 58 + cc6,\n        "ct": [0] * 58 + ct6,\n        "cct": [0] * 58 + cct6_a,\n    }\n'''
if src.count(old) != 1:
    raise SystemExit("could not locate V1 periodic-coordinate block")
fixed = src.replace(old, new, 1)
ns = {"__name__": "__main__", "__file__": str(path)}
exec(compile(fixed, str(path) + "[periodic-order-v2]", "exec"), ns)
cert = json.loads((ROOT / "audit-free-d2-11-direct.json").read_text())
if not cert["free_d2_11_restriction_zero"] or cert["free_d2_11_image_rank_f2"] != 0:
    raise SystemExit("hostile-audit closure gate failed: free d2_11 is nonzero")
if cert["torsion_d2_11_image_rank_f2"] != 2 or cert["combined_direct_d2_11_image_rank_f2"] != 2:
    raise SystemExit("hostile-audit closure gate failed: direct rank regression")
print("HOSTILE_AUDIT_FREE_D2_11_GATE=PASS")
