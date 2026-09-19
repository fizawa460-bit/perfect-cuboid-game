#!/usr/bin/env python3
import json
from pathlib import Path
p=Path(__file__).with_name("MB104-P6K-FULL-G-CHARACTER-SQUARE-CLASS-COUPLING-CERTIFICATE.json")
d=json.loads(p.read_text())
assert d["schema"]=="STAGE32_MB104_P6K_FULL_G_CHARACTER_SQUARE_CLASS_COUPLING_V1"
f=d["findings"]
assert f["labelled_quadratic_subextensions_same"] is True
assert f["basis_character_square_class_equalities"]==3
assert f["square_class_not_function_equality"] is True
assert f["strictly_stronger_than_p6h"] is False
assert f["new_abel_jacobi_obstruction"] is False
assert d["next_leaf"]=="MB104-P6L-LOW-GENUS-MIYAOKA-BOGOMOLOV-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: P6K square-class coupling is exact and adds no invariant beyond P6H")
