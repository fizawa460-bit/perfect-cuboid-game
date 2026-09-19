#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-P6R-EQUIGENERIC-ISOLATION-VERSUS-LINEAR-SYSTEM-DIMENSION-CERTIFICATE.json").read_text())
i=d["invariants"]; f=d["formulas"]; c=d["conclusion"]
assert i=={"pg":7,"q":0,"chi_O":8,"P2":336,"K_dot_P":112}
assert f["chi_lP"]=="168*l^2-56*l+8"
assert f["arithmetic_genus"]=="1+168*l^2+56*l"
assert f["delta"]=="168*l^2+56*l"
assert f["optimistic_linear_system_dim"]=="168*l^2-56*l+7"
assert f["expected_difference"]=="7-112*l"
assert c["negative_expected_dimension_for_all_l_ge_1"] is True
assert c["independence_of_delta_conditions_proved"] is False
assert c["emptiness_follows"] is False
assert d["disposition"]=="PARK_P6R_AT_MISSING_SEVERI_REGULARITY_INDEPENDENCE"
assert d["next_leaf"]=="MB104-Z33D-BALANCED16-FOUR-ORBIT-EQUALITY-GATE"
assert all(v is False for v in d["firewalls"].values())
print("PASS: P6R expected-dimension wall")
print("RR minus delta = 7-112*l, but no retained theorem upgrades negative expected dimension to emptiness")
print("next: Z33D four balanced incidence-16 orbits")
