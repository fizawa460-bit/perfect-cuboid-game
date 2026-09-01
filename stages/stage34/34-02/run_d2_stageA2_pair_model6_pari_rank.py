#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, re, subprocess

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-pair-model6-pari-rank-lock.json"
OUT=ROOT/"d2-stageA2-pair-model6-pari-rank.json"
RAW=ROOT/"d2-stageA2-pair-model6-pari-rank-stdout.txt"
A4=-3228847023956400
A6=66578607841354020720000
TIMEOUT=300

lock=json.loads(LOCK.read_text())
assert lock["status"]=="SOURCE_LOCKED"
assert int(lock["target"]["model_id"])==6
assert int(lock["target"]["a4"])==A4 and int(lock["target"]["a6"])==A6
assert int(lock["execution"]["process_timeout_seconds"])==TIMEOUT
program=(
 f"E=ellinit([0,0,0,{A4},{A6}]);\n"
 "R=ellrank(E,0);\n"
 "print(\"STAGE34_RESULT=\",R[1],\",\",R[2],\",\",R[3]);\n"
 "quit;\n"
)
cmd=["gp","-q","-f"]
try:
    proc=subprocess.run(cmd,input=program,text=True,capture_output=True,timeout=TIMEOUT)
    raw=proc.stdout+("\nSTDERR:\n"+proc.stderr if proc.stderr else "")
    returncode=proc.returncode
    timeout=False
except subprocess.TimeoutExpired as e:
    def txt(x):
        if x is None:return ""
        if isinstance(x,bytes):return x.decode(errors="replace")
        return str(x)
    raw=txt(e.stdout)+("\nSTDERR:\n"+txt(e.stderr) if e.stderr else "")
    returncode=None
    timeout=True
RAW.write_text(raw)

r1=r2=sha2mod4=None
m=re.search(r"STAGE34_RESULT=(-?\d+),(-?\d+),(-?\d+)",raw)
if not timeout and returncode==0 and m:
    r1,r2,sha2mod4=map(int,m.groups())
    assert 0<=r1<=r2
    if r2==0:
        decision="PROVED_RANK_ZERO"
        credit=True
    elif r1>=1:
        decision="PROVED_RANK_NONZERO"
        credit=True
    else:
        decision="UNRESOLVED_RANK_ZERO_STATUS"
        credit=False
else:
    decision="INCONCLUSIVE_RESOURCE_OR_PARSE_WALL"
    credit=False
exact_rank=r1 if r1 is not None and r1==r2 else None
payload={
  "schema":"STAGE34_02_D2_STAGEA2_PAIR_MODEL6_PARI_RANK_INTERVAL_V1",
  "status":decision,
  "source_lock":"d2-stageA2-pair-model6-pari-rank-lock.json",
  "model_id":6,"a4":A4,"a6":A6,
  "returncode":returncode,"timeout":timeout,"timeout_seconds":TIMEOUT,
  "rank_lower_bound":r1,"rank_upper_bound":r2,"sha2_mod_2sha4_rank":sha2mod4,
  "exact_rank":exact_rank,
  "rank_zero_decided":bool(credit),
  "raw_sha256":hashlib.sha256(raw.encode()).hexdigest(),
  "credit":"Only the zero-versus-nonzero rank decision is credited unless rank_lower_bound == rank_upper_bound; no torsor or parent-branch closure credit.",
  "firewalls":{"analytic_rank_or_BSD_used":False,"non_singleton_interval_is_exact_rank":False,"proved_nonzero_rank_is_Q_point_on_torsor":False,"rank_zero_jacobian_closes_quotient_torsor":False,"probe_closes_parent_branch":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":decision,"model_id":6,"interval":[r1,r2],"exact_rank":exact_rank,"rank_zero_decided":bool(credit)},sort_keys=True))
if not credit:raise SystemExit(2)
