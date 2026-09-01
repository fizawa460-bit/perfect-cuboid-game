#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,re,subprocess
ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-additional-rank1-selection.json";LOCK=ROOT/"d2-stageA2-additional-rank1-mw-default-lock.json";OUT=ROOT/"d2-stageA2-additional-rank1-mw-default.json";RAW=ROOT/"d2-stageA2-additional-rank1-mw-default-stdout.txt"
FULL="The rank and full Mordell-Weil basis have been determined unconditionally.";TIMEOUT=120

def txt(x):return "" if x is None else (x.decode(errors="replace") if isinstance(x,bytes) else str(x))
def parse_o(stdout):
 for ln in reversed([z.strip().replace(" ","") for z in stdout.splitlines() if z.strip().startswith("[[")]):
  m=re.match(r"^\[\[(\d+)\],",ln)
  if m:return int(m.group(1)),ln
 return None,None
lock=json.loads(LOCK.read_text());src=json.loads(SRC.read_text())
assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION" and src["status"]==lock["source_selection_status"]
expected=list(map(int,lock["selected_model_ids"]));models={int(x["model_id"]):x for x in src["selected_models"]};assert sorted(models)==sorted(expected)
records=[];cert=[];unres=[];raw=[]
for mid in expected:
 m=models[mid];curve=f"[0,0,0,{int(m['a4'])},{int(m['a6'])}]\n";timed=False;rc=None
 try:
  p=subprocess.run(["mwrank","-q","-v","1","-o"],input=curve,text=True,capture_output=True,timeout=TIMEOUT);rc=p.returncode;out=p.stdout+("\nSTDERR:\n"+p.stderr if p.stderr else "")
 except subprocess.TimeoutExpired as e:timed=True;out=txt(e.stdout)+("\nSTDERR:\n"+txt(e.stderr) if e.stderr else "")
 rank,oline=parse_o(out);low=out.lower();bad=any(s in low for s in ["conditional rank","unable to saturate","saturation failed","not saturated"])
 good=(not timed and rc==0 and FULL in out and not bad and rank==1 and oline is not None)
 st="PASS_UNCONDITIONAL_FULL_MW_BASIS" if good else ("INCONCLUSIVE_TIMEOUT" if timed else "INCONCLUSIVE_NO_FULL_BASIS_MARKER_OR_RANK")
 records.append({"model_id":mid,"a4":int(m["a4"]),"a6":int(m["a6"]),"covered_branches":int(m["covered_branches"]),"status":st,"returncode":rc,"timeout":timed,"parsed_rank":rank,"unconditional_full_basis":good,"mwrank_o_line":oline,"raw_sha256":hashlib.sha256(out.encode()).hexdigest()})
 raw.append(f"===== model={mid} =====\n{out}");(cert if good else unres).append(mid);print(f"model={mid} status={st} rank={rank} covered={m['covered_branches']}")
RAW.write_text("\n".join(raw))
payload={"schema":"STAGE34_02_D2_STAGEA2_ADDITIONAL_RANK1_MW_DEFAULT_V1","status":"PASS_ALL_7_ADDITIONAL_UNCONDITIONAL_FULL_MW_BASES" if not unres else "PARTIAL_ADDITIONAL_FULL_MW_BASES_TARGETED_ESCALATION_REQUIRED","source":"d2-stageA2-additional-rank1-selection.json","source_lock":"d2-stageA2-additional-rank1-mw-default-lock.json","expected_models":7,"certified_models":cert,"unresolved_models":unres,"certified_count":len(cert),"unresolved_count":len(unres),"models":records,"credit":"Only unconditional_full_basis=true records receive full MW basis credit. No parent closure follows.","firewalls":{"partial_is_all7":False,"full_basis_closes_parent_branch":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n");print(json.dumps({"status":payload["status"],"certified":cert,"unresolved":unres},sort_keys=True))
if unres:raise SystemExit(2)
