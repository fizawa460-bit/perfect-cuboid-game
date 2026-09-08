#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04d-joint-map-birationality.json"
TOWER = ROOT / "stages/stage32-ex3/ex3-00-o210-typed-cover-tower.json"

art = json.loads(ART.read_text(encoding="utf-8"))
tower = json.loads(TOWER.read_text(encoding="utf-8"))

assert art["status"] == "SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED"
assert tower["groups"]["H4"]["order"] == 4
assert tower["objects"]["P"]["model"] == "Z x Z"
assert tower["objects"]["X"]["model"] == "P/H4_diag"
assert tower["objects"]["C0"]["model"] == "Z/H4"

maps={x["map"]:x for x in tower["tower_maps"]}
d1=maps["Y->C0:first_factor"]["degree"]
d2=maps["Y->C0:second_factor"]["degree"]
assert (d1,d2)==(105,81)

# If delta is the generic degree of j:Y->Gamma, each coordinate map factors
# through j, hence delta divides both coordinate degrees.
coord_divisors=[d for d in range(1,math.gcd(d1,d2)+1) if d1%d==0 and d2%d==0]
assert coord_divisors == [1,3]

# X=(ZxZ)/H_diag -> (Z/H)x(Z/H) is the quotient by
# (H x H)/H_diag, of order |H|^2/|H|=4. For an irreducible curve in a
# finite regular cover, the generic degree of its restriction to the image is
# the order of its stabilizer subgroup, hence divides 4.
H=4
ambient_degree=(H*H)//H
assert ambient_degree==4
ambient_divisors=[d for d in range(1,ambient_degree+1) if ambient_degree%d==0]
assert ambient_divisors == [1,2,4]

possible=sorted(set(coord_divisors).intersection(ambient_divisors))
assert possible == [1]
assert art["joint_map"]["forced_generic_degree"] == 1
assert art["diagnostic_verdict"]["degree3_joint_factor_eliminated"] is True
assert art["diagnostic_verdict"]["joint_map_birational"] is True
assert art["diagnostic_verdict"]["O210_excluded"] is False
assert all(v is False for v in art["firewalls"].values())

print("PASS EX3-04d scratch joint-map birationality")
print("delta | gcd(105,81)=3 and delta | 4, hence delta=1")
print("Y is the normalization of a primitive (105,81) correspondence Gamma in C0 x C0")
