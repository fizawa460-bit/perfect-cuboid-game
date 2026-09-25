#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
ART=HERE/"V48-FULLSUPPORT-CANONICAL-JOINT-PICARD-SUCCESSOR-PREFLIGHT.json"
ART_BLOB="fb2e208ec374d15e4a1bfc9fa859ac7d36773185"
ART_CANON="d3d4d1970cdf579c4492e3d393ccc1c6c943e2adc49c2f847cfc6f836ed645da"
CANON_MIN=HERE/"verify_support_qbc_canonical_joint_min_retained.py"
CANON_MIN_BLOB="f3754b0e014c9d1885f388a90e3883382bc86907"
PROBE=HERE/"run_v48_fullsupport_canonical_joint_picard_cell_probe.py"
PROBE_BLOB="7d20a7d898bf25f017d742f0f1b7bcaeeab2dc54"
OLD_PREF=HERE/"V48-FULLSUPPORT-JOINT-PICARD-SUCCESSOR-PREFLIGHT.json"
OLD_PREF_BLOB="e5165896e879567a8f18a2d41164ee225d7ac90e"
OLD_PREF_CANON="fe6723e39689e72e64510c3f8c68b6215e271bbcd21b9fd793a8f53ce1905d7a"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    for p,h,n in ((ART,ART_BLOB,"successor v2"),(CANON_MIN,CANON_MIN_BLOB,"canonical min retained verifier"),(PROBE,PROBE_BLOB,"canonical successor probe"),(OLD_PREF,OLD_PREF_BLOB,"relaxed successor preflight")):
        req(p.is_file() and blob(p)==h,n+" blob drift")
    art=json.loads(ART.read_text()); old=json.loads(OLD_PREF.read_text())
    req(canon(art)==ART_CANON==art["canonical_sha256_without_this_field"],"successor v2 canonical drift")
    req(canon(old)==OLD_PREF_CANON==old["canonical_sha256_without_this_field"],"relaxed successor canonical drift")
    req(art["status"]=="CANONICAL_JOINT_SUCCESSOR_PREPARED__ZERO_MAIN_CREDIT__EXECUTION_PENDING","status drift")
    sl=art["source_locks"]
    req(sl["canonical_joint_min_retained_verifier_blob_sha1"]==CANON_MIN_BLOB,"canonical min retained verifier lock drift")
    req(sl["canonical_successor_probe_blob_sha1"]==PROBE_BLOB,"canonical successor probe lock drift")
    req(sl["relaxed_successor_preflight_blob_sha1"]==OLD_PREF_BLOB,"relaxed preflight lock drift")
    req(sl["relaxed_successor_preflight_canonical_sha256"]==OLD_PREF_CANON,"relaxed preflight canonical lock drift")
    d=art["dominance"]
    req("T_canonical(qBC) subset T_relaxed_joint(qBC)"==d["canonical_tset_inclusion"],"set inclusion drift")
    req("canonical-joint-Picard survivors <= relaxed-joint-Picard survivors <= current-fullsupport-Picard survivors" in d["picard_consequence"],"Picard dominance drift")
    e=art["structural_evidence"]
    req((e["bounded_formula_states"],e["bounded_literal_keys"],e["literal_formula_mismatches"])==(2952,670,0),"bounded evidence drift")
    req((e["strict_finite_vs_relaxed"],e["canonical_infeasible_relaxed_finite"])==(137,140),"strict structural evidence drift")
    req((e["active_panel_strict_states_with_relaxed_floor_at_most_4992"],e["active_panel_qbc_cap_crossings"])==(559,9),"active panel evidence drift")
    req(e["active_witness"]=={"b":36,"c":89,"t":103,"support":5,"separate_floor":3137,"relaxed_joint_floor":3377,"canonical_joint_floor":3617},"active witness drift")
    rd=art["route_decision"]
    req(rd["relaxed_joint_picard_route_superseded_for_future_execution"] is True,"supersession drift")
    req(rd["successor"]=="CANONICAL_JOINT_QBC_MIN_PLUS_PICARD_OVER_CURRENT_FULLSUPPORT","successor id drift")
    scope=art["scope"]
    req(scope=={"heavy_execution_armed":False,"production_scaleout_authorized":False,"new_numeric_tightening_claimed":False,"main_consumption_performed":False},"scope overclaim")
    for k,v in art["firewalls"].items():
        if k=="hostile_audit_required_before_promotion": req(v is True,k)
        else: req(v is False,k)
    text=PROBE.read_text()
    for needle in ("canonical_joint_picard_incremental_vs_current_fullsupport","cell_canonical_joint_picard_survivors","canonical_joint_min_exact_for_retained_H_terminal_constraints","cc <= pc <= fc"):
        req(needle in text,"canonical probe contract missing "+needle)
    subprocess.run([sys.executable,str(CANON_MIN)],check=True)
    print("V48_FULLSUPPORT_CANONICAL_JOINT_PICARD_SUCCESSOR_PREFLIGHT=PASS")
    print("RELAXED_ROUTE_SUPERSEDED_FOR_FUTURE_EXECUTION=true")
    print("NEW_NUMERIC_TIGHTENING_CLAIMED=false")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
