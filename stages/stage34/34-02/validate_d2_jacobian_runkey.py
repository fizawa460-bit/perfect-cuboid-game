#!/usr/bin/env python3
import json
import pathlib
import subprocess
import sys

KEY="stages/stage34/runkeys/stage34-02-d2-jacobian-mw.json"
EXPECTED=["20/21","80/39","24/7","84/13","48/55","20/99","60/11"]


def emit(ok,reason):
    print(f"authorized={'true' if ok else 'false'}")
    print("reason="+reason.replace("\n"," ").replace("\r"," "))

def git(*args):
    return subprocess.run(["git",*args],text=True,capture_output=True)

if len(sys.argv)!=3:
    emit(False,"usage requires BEFORE HEAD"); raise SystemExit(0)
before,head=sys.argv[1],sys.argv[2]
if not before or not head:
    emit(False,"missing before/head"); raise SystemExit(0)
if git("cat-file","-e",f"{before}^{{commit}}").returncode!=0:
    emit(False,"before commit unavailable"); raise SystemExit(0)
changed=git("diff","--name-only",before,head)
if changed.returncode!=0 or KEY not in changed.stdout.splitlines():
    emit(False,"dedicated run-key not changed in actual commit range"); raise SystemExit(0)
try:
    new=json.loads(pathlib.Path(KEY).read_text())
except Exception as exc:
    emit(False,f"new key parse failure: {exc}"); raise SystemExit(0)
oldshow=git("show",f"{before}:{KEY}")
if oldshow.returncode==0:
    try: old=json.loads(oldshow.stdout)
    except Exception as exc:
        emit(False,f"old key parse failure: {exc}"); raise SystemExit(0)
else:
    old={"generation":0,"armed":False}
checks=[
    (new.get("schema")=="STAGE34_02_D2_JACOBIAN_MW_RUNKEY_V1","schema"),
    (new.get("armed") is True,"armed"),
    (isinstance(new.get("generation"),int) and new["generation"]>int(old.get("generation",0)),"generation"),
    (new.get("fibers")==EXPECTED,"fibers"),
    (new.get("planned_heavy_jobs")==1,"job_count"),
    (new.get("effective_heavy_concurrency")==1,"concurrency"),
    (new.get("artifact_max_bytes")==1048576,"artifact_cap"),
    (new.get("retention_days")==1,"retention")
]
failed=[n for ok,n in checks if not ok]
if failed:
    emit(False,"semantic gate failed: "+",".join(failed)); raise SystemExit(0)
emit(True,f"generation {new['generation']} explicitly armed")
