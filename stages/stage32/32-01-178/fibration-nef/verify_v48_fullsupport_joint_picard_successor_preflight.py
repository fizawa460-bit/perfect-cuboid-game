#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PREF=HERE/"V48-FULLSUPPORT-JOINT-PICARD-SUCCESSOR-PREFLIGHT.json"
PREF_BLOB="e5165896e879567a8f18a2d41164ee225d7ac90e"
PREF_CANON="fe6723e39689e72e64510c3f8c68b6215e271bbcd21b9fd793a8f53ce1905d7a"
PANEL=HERE/"V48-EXACT-TSET-HIGHVALUE-PANEL-RETAINED.json"
PANEL_BLOB="19cfa17b049b94dee5f406cb8db32ca94e8cf318"
PANEL_CANON="ec9aa7f7300f7613bd05ef3dbdd56de45db0193f91c1d7a82ed7f3e4c972de60"
RAW=HERE/"local-support-qbc/generation2/row022-b036.json"
RAW_BLOB="e8b9db8f1fbb091bbd9465a4f365e6f160f1300c"
PROBE=HERE/"run_v48_fullsupport_joint_picard_cell_probe.py"
PROBE_BLOB="048b61e9cd93d97afa3e22f47eab98904bde85af"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def main():
    for p,h,n in ((PREF,PREF_BLOB,"preflight"),(PANEL,PANEL_BLOB,"exact-tset panel"),(RAW,RAW_BLOB,"raw full-support receipt"),(PROBE,PROBE_BLOB,"successor probe")):
        req(p.is_file() and blob(p)==h,n+" blob drift")
    pref=json.loads(PREF.read_text()); panel=json.loads(PANEL.read_text()); raw=json.loads(RAW.read_text())
    req(canon(pref)==PREF_CANON==pref["canonical_sha256_without_this_field"],"preflight canonical drift")
    req(canon(panel)==PANEL_CANON==panel["canonical_sha256_without_this_field"],"panel canonical drift")
    req(canon(raw)=="9bbb2336f1a68f4896f937a2f781e27a6e855eb5f288990a7f2fa838cfcd2035"==raw["canonical_sha256_without_this_field"],"raw canonical drift")
    req(pref["source_locks"]["successor_probe_blob_sha1"]==PROBE_BLOB,"probe lock drift")
    req(pref["source_locks"]["exact_tset_panel_blob_sha1"]==PANEL_BLOB,"panel lock drift")
    req(pref["source_locks"]["row022_b036_fullsupport_receipt_blob_sha1"]==RAW_BLOB,"raw lock drift")
    target=pref["panel"]["target"]
    req(target=={"row_index":22,"row_id":"g1-d192","g":1,"d":192,"b":36,"c_values":[83,85,89]},"target drift")
    visited={int(x["c"]):x for x in raw["visited_cells"]}
    pcells={int(x["c"]):x for x in panel["cells"]}
    sh=se=sf=0
    for row in pref["panel"]["cells"]:
        c=int(row["c"]); req(c in visited and c in pcells,f"missing c={c}")
        p=pcells[c]; v=visited[c]
        hull=int(p["v48_hull_survivors"]); exact=int(p["exact_tset_survivors"]); full=int(v["refined"])
        req(int(row["v48_hull_survivors"])==hull,f"hull drift c={c}")
        req(int(row["exact_tset_survivors"])==exact,f"exact drift c={c}")
        req(int(row["current_fullsupport_picard_survivors"])==full,f"fullsupport drift c={c}")
        req(int(row["exact_tset_tightening_vs_v48"])==hull-exact,f"exact tightening drift c={c}")
        req(int(row["current_fullsupport_tightening_vs_v48"])==hull-full,f"fullsupport tightening drift c={c}")
        req(int(row["current_fullsupport_stronger_than_exact_tset_by"])==exact-full,f"dominance drift c={c}")
        req(full<exact<hull,f"panel ordering lost c={c}")
        sh+=hull;se+=exact;sf+=full
    agg=pref["panel"]["aggregate"]
    req(int(agg["v48_hull_survivors"])==sh,"aggregate hull drift")
    req(int(agg["exact_tset_survivors"])==se,"aggregate exact drift")
    req(int(agg["current_fullsupport_picard_survivors"])==sf,"aggregate fullsupport drift")
    req(int(agg["exact_tset_tightening_vs_v48"])==sh-se,"aggregate exact tightening drift")
    req(int(agg["current_fullsupport_tightening_vs_v48"])==sh-sf,"aggregate fullsupport tightening drift")
    req(int(agg["current_fullsupport_stronger_than_exact_tset_by"])==se-sf==5135634930037,"aggregate route decision drift")
    d=pref["route_decision"]
    req(d["deprioritize_exact_tset_only_scaleout"] is True,"route decision drift")
    req(d["successor"]=="JOINT_QBC_MIN_PLUS_EXACT_TSET_PLUS_PICARD_OVER_CURRENT_FULLSUPPORT","successor drift")
    req(pref["scope"]["heavy_execution_armed"] is False and pref["scope"]["new_numeric_tightening_claimed"] is False,"scope overclaim")
    for k,v in pref["firewalls"].items():
        if k=="hostile_audit_required_before_promotion": req(v is True,k)
        else: req(v is False,k)
    text=PROBE.read_text()
    for needle in ("current_fullsupport_picard_survivors","joint_picard_incremental_vs_current_fullsupport","support.qcut_support","fullsupport_qcut_equivalence_regression_cases"):
        req(needle in text,"probe contract missing "+needle)
    print("V48_FULLSUPPORT_JOINT_PICARD_SUCCESSOR_PREFLIGHT=PASS")
    print("PANEL_CURRENT_FULLSUPPORT_BEATS_EXACT_TSET_BY=5135634930037")
    print("NEXT_GATE=JOINT_PICARD_3CELL_REPLAY")
    print("MAIN_CREDIT_CHANGED=false")

if __name__=="__main__": main()
