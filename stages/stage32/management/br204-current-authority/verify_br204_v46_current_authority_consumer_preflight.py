#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
PREFLIGHT=HERE/"BR204-V46-CURRENT-AUTHORITY-CONSUMER-PREFLIGHT.json"
STATE=ROOT/"stages/stage32/MAIN-STATE.json"
HPADJ22=ROOT/"stages/stage32/management/hpadj22-direct-full178/HPADJ22-DIRECT-FULL178-RETAINED.json"
PREFLIGHT_BLOB="281b94981f2de336575b32776d47fd3ea1efe890"
PREFLIGHT_CANON="922a1a331bf871d3fe3837a67b7f168cd5612f50fcf741bfeee1bfa9388168bc"
HPADJ22_BLOB="60ca65208b774cc79c646c46c6780e7028a29845"
HPADJ22_CANON="285def36fd8d05557a73ab324ed56178116d5d51fbf6323a33a5f6ecaf6c8805"
BRIDGE_HEAD="ee755bbfd46f405ca83e4930b354ee63459ad362"
BRIDGE_STATE_BLOB="6f12ff6efff4c435fafe322cdd12d5e8978a8cbb"
BRIDGE_RUNKEY_BLOB="95bfe7aca936ff60d840d10761c20a42fc7480b0"
BRIDGE_CONTRACT_BLOB="796e7fc649ba0482eeae4b602d41278b5f1402fb"
COMMON_MASS=6703403803993209250491
CURRENT_BOUND=138652739800650593494
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock_json(p,b,c,label):
    req(p.is_file(),"missing "+label);req(blob(p)==b,label+" blob drift")
    o=json.loads(p.read_text(encoding="utf-8"))
    req(o.get("canonical_sha256_without_this_field")==c and canon(o)==c,label+" canonical drift")
    return o
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--bridge-root",type=Path);args=ap.parse_args()
    p=lock_json(PREFLIGHT,PREFLIGHT_BLOB,PREFLIGHT_CANON,"BR204 V46 consumer preflight")
    h=lock_json(HPADJ22,HPADJ22_BLOB,HPADJ22_CANON,"HPADJ22 retained aggregate")
    st=json.loads(STATE.read_text(encoding="utf-8"))
    req(canon(st)==st.get("canonical_sha256_without_this_field"),"MAIN state canonical")
    req(st["schema"]=="STAGE32_MAIN_COMPACT_STATE_V46_POSTMERGE_SUCCESSOR","MAIN schema")
    req(st["current_exact_frontier"]["authoritative_remaining_terminals"]==CURRENT_BOUND,"current bound")
    req(h["totals"]["post_mass"]==str(COMMON_MASS),"HPADJ22 post mass")
    req(h["composition"]["same_pre_domain_population"] is True,"HPADJ22 same-population flag")
    req(p["current_authority"]["common_pre_domain_post_mass"]==str(COMMON_MASS),"preflight current envelope")
    req(p["bridge_source"]["envelope"]==str(COMMON_MASS),"preflight BR204 envelope")
    req(p["comparability_preflight"]["equal_envelope_value"] is True,"envelope equality")
    req(p["comparability_preflight"]["mass_equality_alone_proves_identity"] is False,"mass identity overclaim")
    req(p["comparability_preflight"]["additive_subtraction_forbidden"] is True,"additive firewall")
    req(p["comparability_preflight"]["permitted_composition_if_identity_proved"]=="MIN_OF_CERTIFIED_UPPER_BOUNDS__SAME_POPULATION__NO_ADDITIVE_STACKING","composition")
    req(p["comparability_preflight"]["current_bound_for_strict_comparison"]==str(CURRENT_BOUND),"strict comparison bound")
    req(p["disposition"]["current_candidate_upper_bound"] is None and p["disposition"]["main_pruning_credit"] is False,"premature candidate credit")
    req(p["bridge_source"]["result_complete"] is False and p["bridge_source"]["pending_main_handoff"]=="NONE","producer completion/handoff")
    if args.bridge_root is not None:
        root=args.bridge_root
        req((root/".git").exists(),"bridge root is not checkout")
        req(blob(root/"stages/stage32/generalization-bridge/STATE.json")==BRIDGE_STATE_BLOB,"BRIDGE state drift")
        runkey=json.loads((root/"stages/stage32/generalization-bridge/runkeys/br204-full178-heavy.json").read_text())
        req(blob(root/"stages/stage32/generalization-bridge/runkeys/br204-full178-heavy.json")==BRIDGE_RUNKEY_BLOB,"BRIDGE runkey drift")
        req(blob(root/"stages/stage32/generalization-bridge/BR204-HEAVY-EXECUTION-CONTRACT.json")==BRIDGE_CONTRACT_BLOB,"BRIDGE contract drift")
        req(runkey["generation"]==1 and runkey["armed"] is True,"BRIDGE generation1")
        req(runkey["execution"]["envelope"]==str(COMMON_MASS),"BRIDGE runkey envelope")
        contract=json.loads((root/"stages/stage32/generalization-bridge/BR204-HEAVY-EXECUTION-CONTRACT.json").read_text())
        req(contract["objective_semantics"]["same_population_replacement_only"] is True,"BRIDGE same-population contract")
        req(contract["objective_semantics"]["additive_pruning"] is False,"BRIDGE additive contract")
        req(contract["objective_semantics"]["envelope"]==str(COMMON_MASS),"BRIDGE contract envelope")
        req(contract["population"]["rows"]==178 and contract["population"]["b_units"]==97 and contract["population"]["durable_subunits"]==250,"BRIDGE FULL178 shape")
    for k,v in p["firewalls"].items():
        if k=="bridge_work_duplicated_by_main": req(v is False,"bridge duplication")
        elif isinstance(v,bool): req(v is False,"firewall "+k)
    print("PASS: BR204 V46 consumer preflight binds the common envelope but does not confuse equal mass with population identity")
    print("PASS: future BR204 credit requires complete audited FULL178 handoff and strict MIN improvement over current V46 bound")
if __name__=="__main__":main()
