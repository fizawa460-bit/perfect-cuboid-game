#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z33D-BALANCED16-FOUR-ORBIT-EXCEPTIONAL-LANDING-CERTIFICATE.json").read_text())
rows=d["balanced_orbits"]
assert [(r["orbit_size"],r["zero_quartics_through_each_supported_node"]) for r in rows]==[(48,2),(48,2),(768,1),(768,1)]
assert rows[0]["ambient_type"]==rows[1]["ambient_type"]=="I16-O3"
assert rows[2]["ambient_type"]==rows[3]["ambient_type"]=="I16-O24"
z=d["z33a"]; c=d["conclusion"]
assert z["diagonal_lambda_locus_infinite"] is True
assert c["zero_quartic_forbidden_landing_set_per_node_finite"] is True
assert c["local_allowed_landing_locus_remains_infinite"] is True
assert c["any_balanced16_orbit_excluded"] is False
assert c["local_landing_only_route_closes"] is False
assert d["disposition"]=="PARK_Z33D_AS_LOCAL_LANDING_ONLY_NO_GO"
assert d["next_leaf"]=="MB104-Z33E-NULL-LOCUS-CONTRACTION-GLOBAL-COUPLING-PREFLIGHT"
assert all(v is False for v in d["firewalls"].values())
print("PASS: Z33D balanced16 exceptional-landing gate")
print("zero quartics remove only finitely many exceptional landing points at each node")
print("Z33A leaves an infinite diagonal lambda-locus, so no balanced16 orbit is excluded locally")
print("next: Z33E null-locus contraction global coupling")
