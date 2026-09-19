#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

SUPPORTS={
 "0000770000ff":([0,1,2,3,4,5,6,7,24,25,26,28,29,30],48,4),
 "00007b0000ff":([0,1,2,3,4,5,6,7,24,25,27,28,29,30],48,4),
 "000707000f0f":([0,1,2,3,8,9,10,11,24,25,26,32,33,34],768,2),
}
SHELLS=[]
for e in [4,8,12,16,20]:
    for pa in range(20):
        r2=2*pa-2-e
        if 64*r2 <= -3*e*e:
            SHELLS.append((e,pa,r2,-16*r2-3*e*e//4))

def csha(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

ap=argparse.ArgumentParser()
ap.add_argument("--certificate",required=True)
args=ap.parse_args()
d=json.loads(Path(args.certificate).read_text())
assert d["schema"]=="STAGE32_MB104_Z40_P_NULL_PICARD64_FINITE_ENUMERATION_V1"
claimed=d["canonical_sha256_without_this_field"]
body=dict(d); body.pop("canonical_sha256_without_this_field")
assert claimed==csha(body)

src=d["source_locks"]
assert src["stoll_commit"]=="51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
assert src["stoll_cuboids_blob"]=="0422b69847f2afb97cb7b3ed02ebef91279f61b1"
assert src["stage33_stoll_helper_blob"]=="010db3767b8f932c71ac5722b50ccb64a8c79f9d"
assert src["stage33_picard_marking_blob"]=="5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"

ex=d["execution"]
assert ex["support_request_count"]==3
assert ex["shell_count_per_support"]==17
assert ex["total_shell_count"]==51
assert ex["rank_before_P_null_reduction"]==63
assert ex["rank_after_P_null_reduction"]==62
assert ex["max_reduced_norm"]==116
assert ex["raw_artifact_persisted"] is False

assert [x["mask"] for x in d["supports"]]==list(SUPPORTS)
common_map=None
unknown_total=known_total=0
for r in d["supports"]:
    compact,orbit,nullq_count=SUPPORTS[r["mask"]]
    assert r["compact_indices_0based"]==compact
    assert r["orbit_size"]==orbit
    mp=r["compact_to_stoll_pts_1based"]
    assert sorted(mp)==list(range(1,49))
    if common_map is None: common_map=mp
    else: assert mp==common_map
    assert r["support_stoll_pts_1based"]==[mp[i] for i in compact]
    assert len(set(r["support_stoll_pts_1based"]))==14
    assert len(r["known_null_quartic_indices_1based"])==nullq_count
    assert r["reference_null_quartic_index_1based"] in r["known_null_quartic_indices_1based"]
    assert r["kernel_rank"]==62
    got=[]
    for sh in r["shells"]:
        tup=(sh["degree"],sh["arithmetic_genus"],sh["R2"],sh["reduced_norm"])
        got.append(tup)
        assert sh["raw_close_vector_count"]>=sh["unique_class_count"]>=sh["kept_after_known_or_nonnegative_filter"]
        assert sh["kept_after_known_or_nonnegative_filter"]==len(sh["known_kept"])+len(sh["unknown_nonnegative_kept"])
        for rec in sh["known_kept"]:
            assert rec["known_indices_1based"]
            assert all(1<=j<=140 for j in rec["known_indices_1based"])
            assert len(rec["picard_basis_coordinates"])==64
        for rec in sh["unknown_nonnegative_kept"]:
            assert rec["known_indices_1based"]==[]
            assert len(rec["picard_basis_coordinates"])==64
        known_total+=len(sh["known_kept"])
        unknown_total+=len(sh["unknown_nonnegative_kept"])
    assert got==SHELLS

s=d["summary"]
assert s["known_kept_class_occurrences"]==known_total
assert s["unknown_nonnegative_class_occurrences"]==unknown_total
assert s["numerical_null_locus_complete_candidate"]==(unknown_total==0)
assert s["geometric_effectivity_of_unknowns_proved"] is False
assert all(v is False for v in d["credit_firewall"].values())
print(json.dumps({
 "success":True,
 "canonical":claimed,
 "known_kept_class_occurrences":known_total,
 "unknown_nonnegative_class_occurrences":unknown_total,
 "numerical_null_locus_complete_candidate":unknown_total==0,
},sort_keys=True))
