#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-sign-involution-remaining30-pair-lock.json"
OUT=ROOT/"d2-stageA2-sign-involution-remaining30-pair-certificate.json"

def transform_coeff_desc(c):
    n=len(c)-1
    out=[0]*(n+1)
    for i,a in enumerate(c):
        j=n-i
        out[j]+=int(a)*((-1)**(n-i))
    return out

def transform_quadratic(c):
    a,b,c0=map(int,c)
    return [c0,-b,a]

d=json.loads(LOCK.read_text())
assert d["schema"]=="STAGE34_02B_D2_STAGEA2_SIGN_INVOLUTION_REMAINING30_PAIR_LOCK_V1"
assert d["branch_count"]==30 and d["pair_count"]==15 and len(d["pairs"])==15
seen=set(); byq={}; transfer_rank_upper_one=[]
for pair in d["pairs"]:
    q=pair["q"]; aa,bb=map(int,q.split("/"))
    forms={
        "U":[1,0,-1],
        "V":[0,2,0],
        "A":[aa,2*bb,-aa],
        "B":[bb,2*aa,-bb],
    }
    for coeff in forms.values():
        assert transform_quadratic(coeff)==[-x for x in coeff]
    L,R=pair["left"],pair["right"]
    assert L["branch_id"] not in seen and R["branch_id"] not in seen
    seen.update([L["branch_id"],R["branch_id"]])
    assert R["delta"]==[-int(x) for x in L["delta"]]
    assert int(R["squareclass"])==-int(L["squareclass"])
    assert transform_coeff_desc(L["coefficients_desc_t_degree6"])==list(map(int,R["coefficients_desc_t_degree6"]))
    assert transform_coeff_desc(R["coefficients_desc_t_degree6"])==list(map(int,L["coefficients_desc_t_degree6"]))
    assert pair["triple"] in {"U*V*A","U*V*B","U*A*B","V*A*B"}
    byq[q]=byq.get(q,0)+1
    lb=L["rank_bounds"]; rb=R["rank_bounds"]
    if (lb is not None and lb[1] <= 1) or (rb is not None and rb[1] <= 1):
        transfer_rank_upper_one.append([L["branch_id"],R["branch_id"]])
assert len(seen)==30
assert byq=={"20/99":4,"48/55":1,"60/11":4,"80/39":2,"84/13":4}
assert sorted(transfer_rank_upper_one)==sorted([
    ["6b3bcb70c4fda8e6f1e0","bb08690eaf9880e595ea"],
    ["03f88290bf80ef2e6c98","231e60279b7c5627c085"],
])
payload={
    "schema":"STAGE34_02B_D2_STAGEA2_SIGN_INVOLUTION_REMAINING30_PAIR_CERTIFICATE_V1",
    "status":"PASS_EXACT_30_BRANCHES_TO_15_SIGN_ORBITS_PREAUDIT",
    "source_lock":LOCK.name,
    "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
    "input_branches":30,
    "exact_orbits":15,
    "orbit_count_by_q":byq,
    "projective_involution":"T(X:Z)=(-Z:X)",
    "generic_form_identities_verified":True,
    "delta_sign_pairing_verified":True,
    "selected_triple_binary_sextic_isomorphisms_verified":True,
    "parent_four_square_truth_preserved":True,
    "receiver_zero_nondegeneracy_preserved":True,
    "rank_and_complete_Qpoint_results_transfer_across_each_orbit":True,
    "rank_upper_le_1_transfer_pairs":transfer_rank_upper_one,
    "immediate_consequence":"The current 30 individual branches require at most 15 representative arithmetic closures. In particular the q=60/11 resolved-rank-bound branch 03f88290bf80ef2e6c98 transfers its rank upper bound <=1 to previously external-response-unresolved partner 231e60279b7c5627c085 after audit promotion of this adapter.",
    "credit":"Pre-audit exact orbit compression and semantic transfer adapter only; zero branches are closed solely by this certificate and no downstream authoritative credit is released before hostile audit.",
    "firewalls":{"orbit_compression_is_branch_closure":False,"authoritative_transfer_credit_before_audit":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"input_branches":30,"exact_orbits":15,"by_q":byq,"rank_upper_le_1_transfer_pairs":transfer_rank_upper_one},sort_keys=True))
