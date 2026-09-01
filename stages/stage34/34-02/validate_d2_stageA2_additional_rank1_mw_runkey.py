#!/usr/bin/env python3
import json,pathlib,subprocess,sys
KEY="stages/stage34/runkeys/stage34-02-d2-stageA2-additional-rank1-mw.json"
def emit(ok,r):print(f"authorized={'true' if ok else 'false'}");print("reason="+r.replace("\n"," ").replace("\r"," "))
def git(*a):return subprocess.run(["git",*a],text=True,capture_output=True)
if len(sys.argv)!=3:emit(False,"usage requires BEFORE HEAD");raise SystemExit(0)
b,h=sys.argv[1],sys.argv[2]
if not b or not h or git("cat-file","-e",f"{b}^{{commit}}").returncode:emit(False,"before/head unavailable");raise SystemExit(0)
d=git("diff","--name-only",b,h)
if d.returncode or KEY not in d.stdout.splitlines():emit(False,"dedicated run-key not changed");raise SystemExit(0)
try:n=json.loads(pathlib.Path(KEY).read_text())
except Exception as e:emit(False,f"new key parse failure {e}");raise SystemExit(0)
o=git("show",f"{b}:{KEY}")
if o.returncode==0:
 try:old=json.loads(o.stdout)
 except Exception as e:emit(False,f"old key parse failure {e}");raise SystemExit(0)
else:old={"generation":0}
checks=[(n.get("schema")=="STAGE34_02_D2_STAGEA2_ADDITIONAL_RANK1_MW_RUNKEY_V1","schema"),(n.get("armed") is True,"armed"),(isinstance(n.get("generation"),int) and n["generation"]>int(old.get("generation",0)),"generation"),(n.get("selected_model_ids")==[3,4,11,13,14,22,46],"models"),(n.get("expected_covered_branches")==28,"coverage"),(n.get("per_model_timeout_seconds")==120,"timeout"),(n.get("planned_heavy_jobs")==1,"jobs"),(n.get("effective_heavy_concurrency")==1,"concurrency"),(n.get("artifact_max_bytes")==1048576,"artifact"),(n.get("retention_days")==1,"retention")]
f=[x for ok,x in checks if not ok]
if f:emit(False,"semantic gate failed: "+",".join(f));raise SystemExit(0)
emit(True,f"generation {n['generation']} explicitly armed")
