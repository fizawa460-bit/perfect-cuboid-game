#!/usr/bin/env python3
import json, pathlib, subprocess, sys
KEY="stages/stage34/runkeys/stage34-02-d2-stageA2-pair-model6-pari.json"

def emit(ok,reason):
    print(f"authorized={'true' if ok else 'false'}")
    print("reason="+reason.replace("\n"," ").replace("\r"," "))

def git(*args):return subprocess.run(["git",*args],text=True,capture_output=True)

if len(sys.argv)!=3:
    emit(False,"usage requires BEFORE HEAD"); raise SystemExit(0)
before,head=sys.argv[1],sys.argv[2]
if not before or not head or git("cat-file","-e",f"{before}^{{commit}}").returncode:
    emit(False,"before/head commit unavailable"); raise SystemExit(0)
diff=git("diff","--name-only",before,head)
if diff.returncode or KEY not in diff.stdout.splitlines():
    emit(False,"dedicated run-key not changed in actual commit range"); raise SystemExit(0)
try:new=json.loads(pathlib.Path(KEY).read_text())
except Exception as e:
    emit(False,f"new key parse failure {e}"); raise SystemExit(0)
oldshow=git("show",f"{before}:{KEY}")
if oldshow.returncode==0:
    try:old=json.loads(oldshow.stdout)
    except Exception as e:
        emit(False,f"old key parse failure {e}"); raise SystemExit(0)
else:old={"generation":0,"armed":False}
checks=[
 (new.get("schema")=="STAGE34_02_D2_STAGEA2_PAIR_MODEL6_PARI_RUNKEY_V1","schema"),
 (new.get("armed") is True,"armed"),
 (isinstance(new.get("generation"),int) and new["generation"]>int(old.get("generation",0)),"generation"),
 (new.get("model_id")==6,"model"),
 (new.get("a4")==-3228847023956400,"a4"),
 (new.get("a6")==66578607841354020720000,"a6"),
 (new.get("pari_effort")==0,"effort"),
 (new.get("process_timeout_seconds")==300,"timeout"),
 (new.get("planned_new_heavy_jobs")==1,"jobs"),
 (new.get("effective_stage34_heavy_concurrency_bound")==2,"concurrency"),
 (new.get("artifact_max_bytes")==1048576,"artifact_cap"),
 (new.get("retention_days")==1,"retention")
]
fail=[name for ok,name in checks if not ok]
if fail:
    emit(False,"semantic gate failed: "+",".join(fail)); raise SystemExit(0)
emit(True,f"generation {new['generation']} explicitly armed")
