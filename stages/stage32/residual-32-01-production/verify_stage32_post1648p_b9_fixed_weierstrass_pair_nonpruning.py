#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648p-b9-fixed-weierstrass-pair-nonpruning.json"
O_PATH = HERE / "post1648o-b9-zero-translation-conjugacy-nonpruning.json"
N_PATH = HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json"
D_PATH = HERE / "post1648d-deraux-affine-sixpoint-orbit-absolute-line-obstruction.json"

EXPECTED_CERT = "07984fe43fa6f80e7b79fa61ddbd2f87a05b16f9d9ea502361e6963f39229e71"
EXPECTED_O = "6ad188aaf14aa9998ac27efc5737e79666b300cdccf2312d9c2b250f8e8a02ef"
EXPECTED_N = "060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba"
EXPECTED_D = "598f3557d84423702be97a6fc942cf3254e68c57b3ccb1950f4d29c3fb3a69f0"
EXPECTED_O_BLOB = "3636be221c73fa2ec023ee0a6238f2e857089562"
EXPECTED_N_BLOB = "0ee05f679c7706113feed2c217e08a95b3bd6f06"
EXPECTED_D_BLOB = "1ab58cba29ed94e0eaf7e646a8e6ed6a536dde41"

def canonical(obj):
    body = dict(obj); body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()

def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def xor(a,b): return [x ^ y for x,y in zip(a,b)]

def main():
    cert = json.loads(CERT.read_text()); o = json.loads(O_PATH.read_text()); n = json.loads(N_PATH.read_text()); d = json.loads(D_PATH.read_text())
    assert canonical(cert) == EXPECTED_CERT == cert["canonical_sha256_without_this_field"]
    assert canonical(o) == EXPECTED_O == o["canonical_sha256_without_this_field"] and blob(O_PATH) == EXPECTED_O_BLOB
    assert canonical(n) == EXPECTED_N == n["canonical_sha256_without_this_field"] and blob(N_PATH) == EXPECTED_N_BLOB
    assert canonical(d) == EXPECTED_D == d["canonical_sha256_without_this_field"] and blob(D_PATH) == EXPECTED_D_BLOB

    src_pts = d["source_affine_J2_model"]["weierstrass_point_coordinates_f2"]
    assert n["source_marking"]["mu1_x_map"] == "x->i*x"
    assert src_pts["0"] == [1,1,1,0] and src_pts["infinity"] == [0,0,0,0]
    assert xor(src_pts["0"], src_pts["infinity"]) == d["source_affine_J2_model"]["W_nonzero_coordinates_f2"]["Z3_delta_0inf"]

    target_orbit = {tuple(v) for v in d["target_deraux_affine_J2_model"]["sixpoint_orbit_f2"]}
    lines = d["target_deraux_affine_J2_model"]["W_nonzero_coordinates_f2"]
    orecs = o["finite_mod2_translation_audit"]["candidates"]
    byline = {"L1": [], "L2": [], "L3": []}; fixed_pairs = {}
    for r in orecs:
        pair = r["translation_conjugator_solutions_f2"]
        assert len(pair) == 2 and all(tuple(v) in target_orbit for v in pair)
        line = r["fixed_W_line"]
        assert xor(pair[0], pair[1]) == lines[line]
        byline[line].append(r["retained_linear_word"])
        fixed_pairs.setdefault(line, pair)
        assert fixed_pairs[line] == pair

    assert {k:len(v) for k,v in byline.items()} == {"L1":2,"L2":2,"L3":2}
    assert {tuple(v) for pair in fixed_pairs.values() for v in pair} == target_orbit
    assert len(fixed_pairs) == 3

    audit = cert["target_fixed_pair_audit"]
    assert audit["every_fixed_point_lies_in_deraux_sixpoint_orbit"] is True
    assert audit["distinct_fixed_pairs"] == 3
    assert audit["the_three_fixed_pairs_partition_the_deraux_sixpoint_orbit"] is True
    assert audit["candidate_count_by_delta0inf_line"] == {"L1":2,"L2":2,"L3":2}
    assert audit["possible_delta0inf_residues_decimal"] == [73,97,235]
    dec = cert["decision"]
    assert dec["B9_fixed_weierstrass_pair_breaks_affine_conjugacy_ambiguity"] is False
    assert dec["absolute_delta0inf_retained_W_line_identified"] is False
    assert dec["survivors_current_credit"] == [73,97,235]
    assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False
    print("POST1648P_B9_FIXED_WEIERSTRASS_PAIR_NONPRUNING_COMPLETE")
    print("fixed_pairs_partition_deraux_sixpoint_orbit=true")
    print("candidate_count_by_line=L1:2,L2:2,L3:2")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")

if __name__ == "__main__": main()
