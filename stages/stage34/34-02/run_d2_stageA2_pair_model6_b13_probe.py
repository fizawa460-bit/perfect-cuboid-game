#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, re, subprocess, sys

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-pair-model6-b13-lock.json"
OUT=ROOT/"d2-stageA2-pair-model6-b13-probe.json"
RAW=ROOT/"d2-stageA2-pair-model6-b13-probe-stdout.txt"
FULL="The rank and full Mordell-Weil basis have been determined unconditionally."
CURVE_A4=-3228847023956400
CURVE_A6=66578607841354020720000
QUARTIC=[2181025,3806880,-4362050,-3806880,2181025]
BOUND=13
TIMEOUT=600


def invariants(c):
    a,b,c2,d,e=c
    I=12*a*e-3*b*d+c2*c2
    J=72*a*c2*e+9*b*c2*d-27*a*d*d-27*b*b*e-2*c2**3
    return I,J


def parse_rank(stdout:str)->tuple[int,str]:
    lines=[ln.strip().replace(" ","") for ln in stdout.splitlines() if ln.strip().startswith("[[")]
    for ln in reversed(lines):
        m=re.match(r"^\[\[(\d+)\],",ln)
        if m:return int(m.group(1)),ln
    raise RuntimeError("could not parse mwrank rank line")


def text_or_empty(x)->str:
    if x is None:return ""
    if isinstance(x,bytes):return x.decode(errors="replace")
    return str(x)

lock=json.loads(LOCK.read_text())
assert lock["status"]=="SOURCE_LOCKED_NONCREDIT_UNTIL_UNCONDITIONAL_MARKER"
t=lock["target"]
assert int(t["model_id_in_sorted_48_model_list"])==6
assert int(t["a4"])==CURVE_A4 and int(t["a6"])==CURVE_A6
assert list(map(int,t["binary_quartic_example"]))==QUARTIC
I,J=invariants(QUARTIC)
assert I==int(t["binary_quartic_I"]) and J==int(t["binary_quartic_J"])
assert -27*I==CURVE_A4 and -27*J==CURVE_A6
assert int(lock["probe"]["quartic_search_bound"])==BOUND
assert int(lock["probe"]["process_timeout_seconds"])==TIMEOUT
curve=f"[0,0,0,{CURVE_A4},{CURVE_A6}]\n"
cmd=["mwrank","-q","-v","1","-o","-b",str(BOUND)]
status="INCONCLUSIVE"
rank=None
oline=None
returncode=None
try:
    proc=subprocess.run(cmd,input=curve,text=True,capture_output=True,timeout=TIMEOUT)
    returncode=proc.returncode
    raw=proc.stdout+("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
except subprocess.TimeoutExpired as e:
    raw=text_or_empty(e.stdout)+("\nSTDERR:\n"+text_or_empty(e.stderr) if e.stderr else "")
    status="INCONCLUSIVE_RESOURCE_WALL_TIMEOUT"
    RAW.write_text(raw)
    payload={
      "schema":"STAGE34_02_D2_STAGEA2_PAIR_MODEL6_B13_PROBE_V1",
      "status":status,"model_id":6,"a4":CURVE_A4,"a6":CURVE_A6,
      "bound":BOUND,"timeout_seconds":TIMEOUT,"rank":None,
      "raw_sha256":hashlib.sha256(raw.encode()).hexdigest(),
      "credit":False,
      "firewalls":{"timeout_is_rank_credit":False,"probe_closes_parent_branch":False,"R29_EXT_CHANG_C_closed":False}
    }
    OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":status,"model_id":6,"bound":BOUND},sort_keys=True))
    raise SystemExit(2)

RAW.write_text(raw)
low=raw.lower()
hard_bad=["unable to saturate","saturation failed","not saturated"]
if returncode==0 and FULL in raw and "conditional rank" not in low and not any(x in low for x in hard_bad):
    rank,oline=parse_rank(raw)
    status="PASS_UNCONDITIONAL_FULL_MORDELL_WEIL_BASIS"
    credit=True
else:
    status="INCONCLUSIVE_NO_UNCONDITIONAL_FULL_BASIS_MARKER"
    credit=False
payload={
  "schema":"STAGE34_02_D2_STAGEA2_PAIR_MODEL6_B13_PROBE_V1",
  "status":status,
  "source_lock":"d2-stageA2-pair-model6-b13-lock.json",
  "model_id":6,"a4":CURVE_A4,"a6":CURVE_A6,
  "binary_quartic_example":QUARTIC,"I":I,"J":J,
  "bound":BOUND,"timeout_seconds":TIMEOUT,"returncode":returncode,
  "rank":rank,"mwrank_o_line":oline,
  "unconditional_full_basis":bool(credit),
  "raw_sha256":hashlib.sha256(raw.encode()).hexdigest(),
  "credit":bool(credit),
  "firewalls":{"conditional_rank_is_rank_credit":False,"rank_zero_jacobian_closes_quotient_torsor":False,"positive_rank_is_Q_point":False,"probe_closes_parent_branch":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":status,"model_id":6,"bound":BOUND,"rank":rank,"credit":credit},sort_keys=True))
if not credit:raise SystemExit(3)
