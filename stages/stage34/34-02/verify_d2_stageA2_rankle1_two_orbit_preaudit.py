#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,collections

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-rankle1-two-orbit-preaudit-lock.json"
BASE=ROOT/"d2-stageA2-genus2-rankle1-14-closure-certificate.json"
SIGNLOCK=ROOT/"d2-stageA2-sign-involution-remaining30-pair-lock.json"
SIGNCERT=ROOT/"d2-stageA2-sign-involution-remaining30-pair-certificate.json"
OUT=ROOT/"d2-stageA2-rankle1-two-orbit-preaudit-bundle.json"

def sha(p:pathlib.Path)->str:
    return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()

def transform_coeff_desc(c):
    n=len(c)-1; out=[0]*(n+1)
    for i,a in enumerate(c):
        out[n-i]+=int(a)*((-1)**(n-i))
    return out

lock=json.loads(LOCK.read_text()); base=json.loads(BASE.read_text()); sl=json.loads(SIGNLOCK.read_text()); sc=json.loads(SIGNCERT.read_text())
assert lock["schema"]=="STAGE34_02B_D2_STAGEA2_RANKLE1_TWO_ORBIT_PREAUDIT_LOCK_V1"
assert base["remaining_branches"]==30 and base["remaining_by_q"]==lock["baseline"]["authoritative_remaining_by_q"]
assert sl["branch_count"]==30 and sl["pair_count"]==15 and len(sl["pairs"])==15
assert sc["status"]==lock["sign_adapter"]["status_required"] and sc["exact_orbits"]==15

seen=set(); pairmap={}; byq=collections.Counter()
for p in sl["pairs"]:
    L,R=p["left"],p["right"]
    assert L["branch_id"] not in seen and R["branch_id"] not in seen
    seen.update([L["branch_id"],R["branch_id"]])
    assert R["delta"]==[-int(x) for x in L["delta"]]
    assert transform_coeff_desc(L["coefficients_desc_t_degree6"])==list(map(int,R["coefficients_desc_t_degree6"]))
    assert transform_coeff_desc(R["coefficients_desc_t_degree6"])==list(map(int,L["coefficients_desc_t_degree6"]))
    pairmap[L["branch_id"]]=R["branch_id"]; pairmap[R["branch_id"]]=L["branch_id"]
    byq[p["q"]]+=1
assert len(seen)==30 and len(pairmap)==30
assert dict(byq)=={"20/99":4,"48/55":1,"60/11":4,"80/39":2,"84/13":4}

actual_sign_sha=sha(SIGNLOCK)
sign_cert_hash_matches=(sc.get("source_lock_sha256")==actual_sign_sha)
records=[]; candidate=[]
for d in lock["direct_proofs"]:
    cp=ROOT/d["certificate"]; c=json.loads(cp.read_text())
    assert c["status"]==d["required_status"] and c["branch_id"]==d["representative"]
    assert int(c["nondegenerate_full_parent_lift_count"])==0
    assert pairmap[d["representative"]]==d["partner"]
    candidate += [d["representative"],d["partner"]]
    records.append({"representative":d["representative"],"partner":d["partner"],"q":d["q"],"method":d["method"],"certificate":d["certificate"],"certificate_sha256":sha(cp),"status":c["status"],"nondegenerate_full_parent_lift_count":0})
assert len(set(candidate))==4
exp=lock["expected_if_hostile_audit_passes"]
assert set(candidate)==set(exp["candidate_closed_branch_ids"])
remain=dict(base["remaining_by_q"])
for r in records: remain[r["q"]]-=2
assert remain==exp["candidate_remaining_by_q"] and sum(remain.values())==26

payload={
  "schema":"STAGE34_02B_D2_STAGEA2_RANKLE1_TWO_ORBIT_PREAUDIT_BUNDLE_V1",
  "status":"READY_FOR_HOSTILE_AUDIT_TWO_ORBIT_CLOSURE_PREAUDIT",
  "baseline_authoritative_remaining_branches":30,
  "baseline_authoritative_remaining_by_q":base["remaining_by_q"],
  "baseline_certificate":BASE.name,
  "baseline_certificate_sha256":sha(BASE),
  "sign_adapter":{"lock":SIGNLOCK.name,"lock_sha256":actual_sign_sha,"certificate":SIGNCERT.name,"certificate_sha256":sha(SIGNCERT),"certificate_declared_source_hash_matches":sign_cert_hash_matches,"exact_orbits":15,"verified_branch_count":30},
  "direct_proofs":records,
  "candidate_if_hostile_audit_passes":{"direct_closed":2,"sign_transfer_closed":2,"closed_branch_ids":candidate,"remaining_branches":26,"remaining_by_q":remain},
  "authoritative_now":{"remaining_branches":30,"R29_EXT_CHANG_C_closed":False,"all_multiples_closed":False},
  "audit_requirements":["Verify the sign involution theorem and all 15 locked pair transports, including parent square and receiver-degeneracy semantics.","Verify the 6b U*V*B rank-zero Chabauty0 proof certificate and integral-model normalization.","Verify the 03f Q(i) elliptic quotient, fixed free point, 2-saturation/index argument, elliptic Chabauty completeness, exceptional points, and reverse parent pullback.","Only after PASS may MAIN promote the four candidate branches and change 30->26."],
  "credit":"Hostile-audit input only. The projected 26 is not authoritative before a separate audit PASS and explicit MAIN promotion.",
  "firewalls":{"bundle_ready_is_hostile_audit_pass":False,"candidate_remaining_26_is_authoritative":False,"sign_transfer_authoritative_before_audit":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"sign_source_hash_matches":sign_cert_hash_matches,"candidate_closed":4,"candidate_remaining":26,"candidate_remaining_by_q":remain},sort_keys=True))
