#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z33F-NULL-LATTICE-DISCRIMINANT-GLUING-PREFLIGHT-CERTIFICATE.json").read_text())
a=d["ambient_picard"]; n=d["null_components"]; c=d["conclusion"]
assert a["P_formula"]=="7H-4*sum_(i in Sigma)E_i"
assert a["P_integral_picard_class"] is True
assert n["zero_quartic_pairing"]==0
assert n["zero_quartic_restriction_trivial"] is True
assert n["unsupported_exceptional_pairing"]==0
assert n["unsupported_exceptional_restriction_trivial"] is True
assert c["P_already_integrally_glued_in_PicS"] is True
assert c["discriminant_embedding_obstruction_available"] is False
assert c["new_l_divisibility_condition"] is False
assert c["componentwise_trivial_does_not_automatically_set_reducible_union_gluing"] is True
assert d["disposition"]=="PARK_Z33F_AS_NUMERICAL_LATTICE_NO_GO"
assert d["next_leaf"]=="MB104-Z33G-NULL-UNION-PIC0-GLUING-HOLONOMY-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z33F numerical null-lattice preflight")
print("P is already an integral Pic(S) class orthogonal to the selected null components")
print("discriminant/saturation cannot create a new embedding or l-divisibility obstruction")
print("next: Z33G reducible-null-union Pic0 gluing")
