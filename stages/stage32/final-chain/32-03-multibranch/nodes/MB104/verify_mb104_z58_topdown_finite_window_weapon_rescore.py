#!/usr/bin/env python3
import json
from pathlib import Path
d=json.loads(Path(__file__).with_name("MB104-Z58-TOPDOWN-FINITE-WINDOW-WEAPON-RESCORE-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z58_TOPDOWN_FINITE_WINDOW_WEAPON_RESCORE_V1"
f=d["dangerous_frontier"]
assert f["size48_dangerous_packet_excluded"] is True
assert f["remaining_support"]=="000707000f0f"
assert f["remaining_orbit_size"]==768
w={x["id"]:x for x in d["weapons"]}
assert w["Z4P_CONDUCTOR_POSTULATION"]["priority"]==1
assert w["Z12_GENERAL_M_PRIMITIVE_HILBERT"]["priority"]==2
assert w["PICARD_NULL_FORMAL"]["state"]=="EXHAUSTED_INDEPENDENT_CLOSER"
assert w["LOCAL_BMY_SIZE48"]["state"]=="PARK_NOT_CURRENT_DANGEROUS_FRONTIER"
assert d["next_cycle"]["mode"]=="SHALLOW_BROAD"
assert d["next_cycle"]["deep_route_forbidden_without_rescore"] is True
assert not any(d["credit"].values())
print("PASS STAGE32_MB104_Z58_TOPDOWN_FINITE_WINDOW_WEAPON_RESCORE_V1")
print("frontier=000707000f0f only; priority=Z4P then Z12 then Z25; size48 local parked")
