#!/usr/bin/env python3
import json,pathlib,subprocess,sys
KEY="stages/stage34/runkeys/stage34-02-d2-stageA2-two-adic-full-branch.json"
def emit(ok,r):
 print(f"authorized={'true' if ok else 'false'}"); print("reason="+r.replace("\n"," ").replace("\r"," "))
def git(*a):return subprocess.run(["git",*a],text=True,capture_output=True)
if len(sys.argv)!=3:emit(False,"usage requires BEFORE HEAD");raise SystemExit(0)
before,head=sys.argv[1],sys.argv[2]
if not before or not head or git("cat-file","-e",f"{before}^{{commit}}").returncode:emit(False,"before/head unavailable");raise SystemExit(0)
d=git("diff","--name-only",before,head)
if d.returncode or KEY not in d.stdout.splitlines():emit(False,"dedicated run-key not changed");raise SystemExit(0)
try:new=json.loads(pathlib.Path(KEY).read_text())
except Exception as e:emit(False,f"parse failure {e}");raise SystemExit(0)
o=git("show",f"{before}:{KEY}"); old=json.loads(o.stdout) if o.returncode==0 else {"generation":0}
checks=[new.get("schema")=="STAGE34_02_D2_STAGEA2_TWO_ADIC_FULL_BRANCH_RUNKEY_V1",new.get("armed") is True,isinstance(new.get("generation"),int) and new["generation"]>old.get("generation",0),new.get("input_branches")==92,new.get("modulus")==32,new.get("expected_survivors")==64,new.get("planned_heavy_jobs")==1,new.get("effective_heavy_concurrency")==1,new.get("artifact_max_bytes")==1048576,new.get("retention_days")==1]
if not all(checks):emit(False,"semantic gate failed");raise SystemExit(0)
emit(True,f"generation {new['generation']} explicitly armed")
