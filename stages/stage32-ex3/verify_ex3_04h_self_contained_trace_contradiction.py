#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ART=ROOT/"stages/stage32-ex3/ex3-04h-self-contained-trace-contradiction.json"
def bsha(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def csha(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
a=json.loads(ART.read_text())
assert a["status"]=="RETAINED_PROVISIONAL_SELF_CONTAINED_TERMINAL_GATE_UNAUDITED"
assert csha(a)==a["canonical_sha256_without_this_field"]
L=a["source_locks"]; P={k:ROOT/v["path"] for k,v in L.items()}
for k,v in L.items(): assert bsha(P[k])==v["blob_sha1"],k
for k in ["typed_cover_tower","relative_H_marking","v6_witness","resolved_double_cover_blowdown_adapter","common_cover_identity","q602_trace_spectrum"]:
    o=json.loads(P[k].read_text()); assert csha(o)==L[k]["canonical_sha256"],k
inc=json.loads(P["physical_C1_node_incidence"].read_text())
assert inc["canonical_sha256"]==L["physical_C1_node_incidence"]["canonical_sha256"]
note=P["modular_graph_source_note"].read_text()
for m in ["arXiv:1009.0388","Section 4","Section 7","u^2=2xy","32 conics","six singularities"]:
    assert m in note
rel=json.loads(P["relative_H_marking"].read_text())
assert [rel["modular_to_stoll"][x] for x in ["u=TTprime","v=RT","uv=RTprime"]]==["g7*g9","g7*g8","g8*g9"]
loc=P["exact_C1_ordering"].read_text()
assert 'add_known("C1", 3' in loc and '[a3, a1 + e1*b2, a2 + e2*b1, b3 + e3*c]' in loc
H=[(1,1,1),(-1,1,-1),(-1,-1,1),(1,-1,-1)]
S=[(e1,e2,e3) for e1 in (1,-1) for e2 in (1,-1) for e3 in (1,-1)]
idx=[17+S.index((-ev,-eu,-ew)) for eu,ev,ew in H]
assert idx==[24,21,18,19]
nodes=defaultdict(set)
for ex in inc["exceptional_models"]:
    j=int(ex["exceptional_id"].split("_")[1])
    for r in ex["physical_crossing_tangent_coordinates"]: nodes[int(r["side_index_1based"])].add(j)
assert all(len(nodes[s])==6 for s in range(1,25))
v6=json.loads(P["v6_witness"].read_text()); pair=v6["witness"]["all140_pairings"]; mult=pair[92:140]
ck=[pair[s-1] for s in idx]; mass=[sum(mult[j-1] for j in nodes[s]) for s in idx]
assert ck==[0,0,14,9] and mass==[41,41,24,34]
gamma=[4*(2*x+y) for x,y in zip(ck,mass)]; A=[186-x for x in gamma]
assert gamma==[164,164,208,208] and A==[22,22,-22,-22]
chars={"trivial":[1,1,1,1],"chi_u":[1,-1,1,-1],"chi_v":[1,1,-1,-1],"chi_uv":[1,-1,-1,1]}
blocks={k:sum(c*x for c,x in zip(r,A))//4 for k,r in chars.items()}
assert blocks=={"trivial":0,"chi_u":0,"chi_v":22,"chi_uv":0}
q=json.loads(P["q602_trace_spectrum"].read_text()); allowed=q["exact_spectrum"]["trace_values"]
assert q["rational_trace"]["gauge_invariant_by_conjugation"] and q["rational_trace"]["trace_mod8"]==4 and 0 not in allowed
assert a["graph_geometry"]["H_character_linear_traces"]==blocks and a["q602_contradiction"]["contradiction"]
d=a["population_domination"]
assert not d["finite_monodromy_sample_used"] and d["does_not_claim_those_enumerations_were_run"]
assert d["all_fixed_O210_cover_configurations_disposed_if_source_chain_is_accepted"]
assert a["verdict"]["retained"] and not a["verdict"]["hostile_audited"]
print("PASS Stage32EX3 EX3-04h retained provisional trace-zero gate")
print(json.dumps({"C1":idx,"Gamma":gamma,"traces":A,"H_blocks":blocks,"terminal_candidate":"O210_COVER_GEOMETRY_EXCLUDED","hostile_audited":False,"stage32_main_credit":False},sort_keys=True))
