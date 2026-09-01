#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, re, subprocess

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-rank1-cover-selection.json"
LOCK=ROOT/"d2-stageA2-selected-rank1-mw-default-lock.json"
OUT=ROOT/"d2-stageA2-selected-rank1-mw-default.json"
RAW=ROOT/"d2-stageA2-selected-rank1-mw-default-stdout.txt"
FULL="The rank and full Mordell-Weil basis have been determined unconditionally."
TIMEOUT=120

def txt(x):
    if x is None:return ""
    if isinstance(x,bytes):return x.decode(errors="replace")
    return str(x)

def parse_o_line(stdout:str):
    lines=[ln.strip().replace(" ","") for ln in stdout.splitlines() if ln.strip().startswith("[[")]
    for ln in reversed(lines):
        m=re.match(r"^\[\[(\d+)\],",ln)
        if m:return int(m.group(1)),ln
    return None,None

lock=json.loads(LOCK.read_text()); src=json.loads(SRC.read_text())
assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION"
assert src["status"]==lock["source_selection_status"]
expected=list(map(int,lock["selected_model_ids"])); assert len(expected)==14
models={int(m["model_id"]):m for m in src["selected_rank1_models"]}
assert sorted(models)==sorted(expected)
assert all(int(models[mid]["rank"])==1 for mid in expected)
records=[]; raw_sections=[]; certified=[]; unresolved=[]
hard_bad=["unable to saturate","saturation failed","not saturated"]
for mid in expected:
    m=models[mid]; a4=int(m["a4"]); a6=int(m["a6"]); curve=f"[0,0,0,{a4},{a6}]\n"
    cmd=["mwrank","-q","-v","1","-o"]
    timed_out=False; returncode=None
    try:
        proc=subprocess.run(cmd,input=curve,text=True,capture_output=True,timeout=TIMEOUT)
        returncode=proc.returncode; out=proc.stdout+("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
    except subprocess.TimeoutExpired as e:
        timed_out=True; out=txt(e.stdout)+("\nSTDERR:\n"+txt(e.stderr) if e.stderr else "")
    rank,oline=parse_o_line(out); low=out.lower()
    good=(not timed_out and returncode==0 and FULL in out and "conditional rank" not in low and not any(s in low for s in hard_bad) and rank==1 and oline is not None)
    status="PASS_UNCONDITIONAL_FULL_MW_BASIS" if good else ("INCONCLUSIVE_TIMEOUT" if timed_out else "INCONCLUSIVE_NO_FULL_BASIS_MARKER_OR_RANK")
    rec={
      "model_id":mid,"a4":a4,"a6":a6,"covered_branches":int(m["covered_branches"]),
      "status":status,"returncode":returncode,"timeout":timed_out,"timeout_seconds":TIMEOUT,
      "parsed_rank":rank,"unconditional_full_basis":bool(good),"mwrank_o_line":oline,
      "raw_sha256":hashlib.sha256(out.encode()).hexdigest()
    }
    records.append(rec); raw_sections.append(f"===== model={mid} a4={a4} a6={a6} =====\n{out}")
    (certified if good else unresolved).append(mid)
    print(f"model={mid} status={status} rank={rank} covered={m['covered_branches']}")
RAW.write_text("\n".join(raw_sections))
payload={
 "schema":"STAGE34_02_D2_STAGEA2_SELECTED_RANK1_MW_DEFAULT_V1",
 "status":"PASS_ALL_14_UNCONDITIONAL_FULL_MW_BASES" if not unresolved else "PARTIAL_UNCONDITIONAL_FULL_MW_BASES_TARGETED_ESCALATION_REQUIRED",
 "source":"d2-stageA2-rank1-cover-selection.json",
 "source_lock":"d2-stageA2-selected-rank1-mw-default-lock.json",
 "software":{"package":"eclib-tools","command":"mwrank -q -v 1 -o","default_quartic_search_bound":10,"required_success_marker":FULL},
 "expected_models":14,"certified_models":certified,"unresolved_models":unresolved,
 "certified_count":len(certified),"unresolved_count":len(unresolved),"models":records,
 "credit":"Only records with unconditional_full_basis=true receive full Mordell-Weil basis credit. Unresolved models are noncredit and must be targeted separately.",
 "firewalls":{"partial_basis_set_is_all14_basis":False,"full_basis_is_quotient_pointset":False,"full_basis_closes_parent_branch":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"certified":certified,"unresolved":unresolved},sort_keys=True))
if unresolved:raise SystemExit(2)
