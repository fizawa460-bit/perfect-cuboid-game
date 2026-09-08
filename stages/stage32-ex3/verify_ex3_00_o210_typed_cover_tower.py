#!/usr/bin/env python3
"""Replay EX3-00 source locks and the typed O210/q'=4 cover tower."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "stages/stage32-ex3/ex3-00-o210-typed-cover-tower.json"


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical_without_field(obj: dict, field: str) -> str:
    reduced = dict(obj)
    reduced.pop(field, None)
    return hashlib.sha256(
        json.dumps(reduced, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


art = json.loads(ART.read_text(encoding="utf-8"))
assert art["schema"] == "STAGE32EX3_EX3_00_O210_TYPED_COVER_TOWER_V1"
assert art["status"] == "RETAINED_PROVISIONAL_EXACT_SOURCE_LOCK_UNAUDITED"
assert art["fixed_target"]["row_id"] == "g1-d186"
assert art["fixed_target"]["picard_class"] == "V6"
assert art["fixed_target"]["O"] == 210
assert art["fixed_target"]["qprime"] == 4

# Exact retained source locks.
for name, lock in art["source_locks"].items():
    path = ROOT / lock["path"]
    data = path.read_bytes()
    assert git_blob_sha1(data) == lock["blob_sha1"], f"blob drift: {name}"
    if "canonical_sha256" in lock:
        obj = json.loads(data.decode("utf-8"))
        assert canonical_without_field(obj, "canonical_sha256_without_this_field") == lock["canonical_sha256"], f"canonical drift: {name}"

# Group and quotient tower.
assert art["groups"]["G8"]["order"] == 8
assert art["groups"]["H4"]["order"] == 4
assert art["groups"]["H4"]["isomorphic_to"] == "(Z/2)^2"
assert art["groups"]["H4"]["normal_in_G8"] is True
assert art["groups"]["H4"]["index_in_G8"] == 2
assert art["groups"]["H4"]["acts_freely_on_X8"] is True
assert art["objects"]["Z"]["genus"] == 5
assert art["objects"]["C0"]["genus"] == 2
assert art["objects"]["X4"]["genus"] == 0
assert art["objects"]["N"]["genus"] == 1
assert art["objects"]["Y"]["genus"] == 106
assert art["objects"]["D"]["genus"] == 421

maps = {m["map"]: m for m in art["tower_maps"]}
expected = {
    "Z->C0": (4, 0),
    "C0->X4": (2, 6),
    "P->X": (4, 0),
    "Y->N": (2, 210),
    "D->Y": (4, 0),
    "N->X4:first_factor": (105, None),
    "N->X4:second_factor": (81, None),
    "Y->C0:first_factor": (105, 0),
    "Y->C0:second_factor": (81, 48),
    "D->Z:first_factor": (105, 0),
    "D->Z:second_factor": (81, 192),
}
for name, (degree, ramification) in expected.items():
    assert maps[name]["degree"] == degree, name
    if ramification is not None:
        assert maps[name]["ramification_total"] == ramification, name

# Degree transport and extremal Riemann--Hurwitz checks.
deg = art["degree_adapter"]
assert deg["generic_degree_identity"] == "8*n_i = 2*qprime*m_i"
assert deg["m_pair_N_to_X4"] == [105, 81]
assert deg["qprime_1_integrality"] is False
assert deg["qprime_2_integrality"] is False
assert deg["forced_qprime"] == 4
assert deg["n_pair_D_to_X8"] == [105, 81]
assert deg["D_to_N_generic_degree"] == 8

cr = art["contact_and_ramification"]
assert cr["exceptional_total_mass"] == 266
assert cr["O_odd_contact_count"] == 210
assert cr["extremal_histogram"] == {"multiplicity_1_count": 210, "multiplicity_2_count": 28}
assert 210 * 1 + 28 * 2 == 266
assert 2 * 106 - 2 == 210
assert 2 * 421 - 2 == 4 * (2 * 106 - 2) == 840
assert 105 * (2 * 5 - 2) + 0 == 840
assert 81 * (2 * 5 - 2) + 192 == 840
assert 105 * (2 * 2 - 2) + 0 == 210
assert 81 * (2 * 2 - 2) + 48 == 210
assert cr["pre_descent_192_is_not_descended_48"] is True

# Source-text semantic anchors: fail if the retained statements disappear.
bidegree = (ROOT / art["source_locks"]["bidegree_note"]["path"]).read_text(encoding="utf-8")
assert "`m_z=105`, `m_w=81`" in bidegree
assert "`q'=1`: both projected degrees are nonintegral" in bidegree
assert "`q'=2`: both projected degrees are nonintegral" in bidegree
assert "`q'=4`: `(n_z,n_w)=(105,81)`" in bidegree
assert "ramification remainder `4*210-8*105=0`" in bidegree
assert "`210 x m1 + 28 x m2`" in bidegree
assert "source ramification remainder `4*210-8*81=192`" in bidegree
assert "after the V4 etale descent this is ramification degree 48" in bidegree

common = json.loads((ROOT / art["source_locks"]["common_cover_identity"]["path"]).read_text(encoding="utf-8"))
cc = common["carrier_consequence"]
assert cc["same_quadratic_extension"] is True
assert "normalization of N x_{z,X4} C0" in cc["first_factor"]
assert "normalization of N x_{w,X4} C0" in cc["second_factor"]
assert common["relation_to_previous_pic2_reduction"]["do_not_use_for_exclusion"]

v4 = json.loads((ROOT / art["source_locks"]["v4_character_rank"]["path"]).read_text(encoding="utf-8"))
assert v4["deck_group_model"]["group"] == "G=GammaPrime4/Gamma8 ~= F2^2"
assert v4["carrier_pullback_reduction"]["cases"][-1] == {"rank": 2, "qprime": 4}

quot = json.loads((ROOT / art["source_locks"]["x8_v4_cusp_quotient"]["path"]).read_text(encoding="utf-8"))
qg = quot["quotient_geometry"]
assert qg["X8_to_C0_degree"] == 4 and qg["X8_to_C0_etale"] is True
assert qg["genus_X8"] == 5 and qg["genus_C0"] == 2
assert qg["C0_to_X4_degree"] == 2 and qg["C0_to_X4_total_fixed_points"] == 6

beauville = (ROOT / art["source_locks"]["beauville_odd_branch_wall"]["path"]).read_text(encoding="utf-8")
assert "`Y -> N` ramified at exactly the `O` odd-contact points" in beauville
assert "`2*g(Y)-2 = O`" in beauville

ext = (ROOT / art["source_locks"]["product_cover_extremal_wall"]["path"]).read_text(encoding="utf-8")
assert "`q'=|H| in {1,2,4}`" in ext
assert "full V4 monodromy" in ext

rosati = (ROOT / art["source_locks"]["bolza_correspondence_note"]["path"]).read_text(encoding="utf-8")
assert "`deg(f1)=105`, `deg(R_f1)=0`" in rosati
assert "`deg(f2)=81`, `deg(R_f2)=48`" in rosati
assert "`T^dagger T <= 105*81 = 8505`" in rosati

assert art["common_cover_identity"]["obstruction_status"].startswith("compatibility identity")
assert art["correspondence_interface"]["Q602_marked_adapter_obtained"] is False
assert art["verdict"]["EX3_00_source_lock_complete"] is True
assert art["verdict"]["typed_cover_tower_complete"] is True
assert art["verdict"]["credit_ceiling"] == "PROVISIONAL_NECESSARY_CONDITION_ONLY_UNAUDITED"
assert art["verdict"]["next_leaf"] == "EX3-01_EXTREMAL_FIRST_PROJECTION_DEGREE105_ETALE_COVER"
assert all(value is False for value in art["firewalls"].values())
assert canonical_without_field(art, "canonical_sha256_without_this_field") == art["canonical_sha256_without_this_field"]

print("PASS Stage32EX3 EX3-00 typed O210 cover tower")
print("tower: N(g=1) <-2- Y(g=106) <-4 etale- D(g=421)")
print("projections D->X8: 105/R0 and 81/R192; descended Y->C0: 105/R0 and 81/R48")
print("credit: provisional necessary-condition only; no O210/Q602 exclusion")
