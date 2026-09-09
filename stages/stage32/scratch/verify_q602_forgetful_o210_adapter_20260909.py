#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
ART=ROOT/"stages/stage32/scratch/q602-forgetful-o210-adapter-20260909.json"
ACTIVE=ROOT/"stages/stage32/proof/ACTIVE-FRONTIER.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"

CORE_KEYS=["claim_id","kind","statement","scope_key","scope","proves","does_not_prove","requires","bridges","source_locks","replay_verifier"]

def csha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def bsha(data:bytes):
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

def canon(path:Path):
    obj=json.loads(path.read_text())
    stored=obj["canonical_sha256_without_this_field"]
    stripped=dict(obj); stripped.pop("canonical_sha256_without_this_field",None)
    assert csha(stripped)==stored
    return stored

a=json.loads(ART.read_text())
stored=a["canonical_sha256_without_this_field"]
stripped=dict(a); stripped.pop("canonical_sha256_without_this_field",None)
assert csha(stripped)==stored=="63d56bba4505271957376fc169ecc473c1c26bf11e285197fa6c2bc2a2514a36"
assert a["status"]=="SCRATCH_EXACT_UNAUDITED_TYPED_POPULATION_ADAPTER_CANDIDATE"
assert a["base_head"]=="2ad52c41d166d39d7458b6ab228432ba50ed93ce"

for name,lock in a["source_locks"].items():
    p=ROOT/lock["path"]; data=p.read_bytes()
    assert bsha(data)==lock["blob_sha1"], name
    assert canon(p)==lock["canonical_sha256"], name

active=json.loads(ACTIVE.read_text())
by={c["claim_id"]:c for c in active["claims"]}
o1=by["S32.O210.EXCLUSION.V1"]
surv=by["S32.Q602.SURVIVORS_73_97_235.V1"]
q1=by["S32.Q602.EXCLUSION.V1"]

assert o1["scope"]=={"row_id":"g1-d186","picard_class":"V6","O":210,"qprime":4,"target":"population_wide_exclusion"}
assert o1["authority_status"]=="DECLARED_GOAL"
assert surv["authority_status"]=="AUDITED"
assert surv["scope"]["row_id"]=="g1-d186" and surv["scope"]["O"]==210 and surv["scope"]["Q"]==602
assert surv["scope"]["surviving_residues"]==[73,97,235]
assert q1["authority_status"]=="DECLARED_GOAL"
assert q1["scope"]=={"row_id":"g1-d186","O":210,"Q":602,"input_survivors":[73,97,235],"target":"all_residues_excluded"}

state=json.loads(STATE.read_text())
assert state["current_exact_frontier"]["o210_excluded"] is False
assert state["current_exact_frontier"]["q602_excluded"] is False
assert state["firewalls"]["O212_plus_advance_allowed"] is False

qsrc=json.loads((ROOT/a["source_locks"]["q602_survivor_artifact"]["path"]).read_text())
assert qsrc["fixed_target"]=={"O":210,"Q":602,"qprime":4,"row_id":"g1-d186","surviving_residues_decimal":[73,97,235]}
assert qsrc["firewalls"]["O210_excluded"] is False and qsrc["firewalls"]["Q602_excluded"] is False

oart=json.loads((ROOT/a["source_locks"]["o210_v3_artifact"]["path"]).read_text())
assert oart["target"]["row_id"]=="g1-d186"
assert oart["target"]["picard_class"]=="V6"
assert oart["target"]["O"]==210 and oart["target"]["qprime"]==4 and oart["target"]["Q"]==602
assert oart["target"]["surviving_marked_residues"]==[73,97,235]
assert oart["derivation"]["q602_survivors_are_obstruction_evidence_not_population_filter"] is True
assert oart["claim_binding"]["claim_id"]=="S32.O210.EXCLUSION.V3"
assert oart["claim_binding"]["claim_core_sha256"]=="7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824"

m=a["forgetful_map"]
assert m["population_relation"]=="Q602_ADMISSIBLE_POPULATION_MAPS_INTO_O210_POPULATION"
assert m["empty_codomain_implies_empty_domain"] is True
for key in ["changes_row","changes_picard_class","changes_O","changes_qprime","changes_carrier_cover_object"]:
    assert m[key] is False
assert set(m["forgets_only"])=={"Q602 residue label","retained marked W-line/arithmetic decoration"}

ad=a["proposed_adapter_claim"]
assert ad["claim_id"]=="S32.ADAPTER.O210_TO_Q602_FORGETFUL.V1"
assert ad["kind"]=="adapter_contract"
assert ad["bridges"]=={"from_scope_key":"S32.O210.COVER","to_scope_key":"S32.Q602.ARITHMETIC"}
assert ad["requires"]==["S32.MAIN.CURRENT_TARGET_CONTEXT.V1","S32.O210.EXCLUSION.V3","S32.Q602.SURVIVORS_73_97_235.V1"]
assert ad["claim_core_sha256"]=="53bfa1c6c7eca1852be511b71a7cf04249f5ebf796df65c8b42b5cb572ddb3d9"
assert csha({k:ad[k] for k in CORE_KEYS if k in ad})==ad["claim_core_sha256"]

q2=a["proposed_q602_claim"]
assert q2["claim_id"]=="S32.Q602.EXCLUSION.V2"
assert q2["scope"]==q1["scope"]
assert q2["requires"]==["S32.Q602.SURVIVORS_73_97_235.V1","S32.O210.EXCLUSION.V3","S32.ADAPTER.O210_TO_Q602_FORGETFUL.V1"]
assert q2["claim_core_sha256"]=="dce0347fd3bb25eeec70d266bab91f5a8b2124077b7caad5eb360cb26cbeb67f"
assert csha({k:q2[k] for k in CORE_KEYS if k in q2})==q2["claim_core_sha256"]
assert a["versioning"]["existing_q602_v1_core_must_not_be_mutated"] is True
assert a["promotion_gate"]["requires_o210_main_consumption_first"] is True
assert a["promotion_gate"]["requires_hostile_audit_of_forgetful_adapter"] is True
assert a["promotion_gate"]["requires_hostile_audit_of_q602_v2"] is True

for key in ["Q602_excluded","O212_plus_advance_allowed","FULL178_complete","stage32_closed","endpoint_credit","perfect_cuboid_claim","main_state_modified","active_frontier_modified"]:
    assert a["firewalls"][key] is False

print("PASS Stage32 scratch Q602->O210 forgetful population adapter")
print(json.dumps({
    "adapter_claim_id":ad["claim_id"],
    "adapter_core":ad["claim_core_sha256"],
    "q602_claim_id":q2["claim_id"],
    "q602_core":q2["claim_core_sha256"],
    "o210_current_main_consumed":False,
    "q602_promoted":False,
    "stage32_closed":False
},sort_keys=True))
