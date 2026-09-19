#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-P6Q-TWO-PENCIL-NIELSEN-COUPLING-PREFLIGHT-CERTIFICATE.json").read_text())
r=d["retained"]; c=d["conclusion"]
assert d["group"]=="(Z/2)^3"
assert r["same_labelled_G_cover"] is True
assert r["basis_character_square_class_equalities"]==3
assert r["remaining_nontrivial_characters_generated_by_basis"] is True
assert r["individual_branch_value_identification"] is False
assert r["simultaneous_nielsen_presentation_source_locked"] is False
assert c["intrinsic_common_cover_data_stronger_than_P6K"] is False
assert c["new_nielsen_obstruction"] is False
assert d["disposition"]=="PARK_P6Q_AS_KUMMER_REFORMULATION_OF_P6K"
assert d["next_leaf"]=="MB104-P6R-EQUIGENERIC-ISOLATION-VERSUS-LINEAR-SYSTEM-DIMENSION-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: P6Q Nielsen coupling preflight wall")
print("same labelled (Z/2)^3 cover is exactly the retained Kummer square-class package at intrinsic-cover level")
print("next: P6R equigeneric isolation versus linear-system dimension")
