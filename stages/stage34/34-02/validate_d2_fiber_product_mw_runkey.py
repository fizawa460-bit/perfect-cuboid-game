#!/usr/bin/env python3
import json, pathlib, subprocess, sys
KEY="stages/stage34/runkeys/stage34-02-d2-fiber-product-mw.json"

def emit(ok,reason):
    print(f"authorized={'true' if ok else 'false'}")
    print("reason="+reason.replace("\n"," ").replace("\r"," "))
def git(*args): return subprocess.run(["git",*args],text=True,capture_output=True)
if len(sys.argv)!=3:
    emit(False,"usage requires BEFORE HEAD"); raise SystemExit(0)
before,head=sys.argv[1],sys.argv[2]
if not before or not head or git("cat-file","-e",f"{before}^{{commit}}").returncode:
    emit(False,"before/head commit unavailable"); raise SystemExit(0)
diff=git("diff","--name-only",before,head)
if diff.returncode or KEY not in diff.stdout.splitlines():
    emit(False,"dedicated run-key not changed in actual commit range"); raise SystemExit(0)
try: new=json.loads(pathlib.Path(KEY).read_text())
except Exception as e:
    emit(False,f"new key parse failure {e}"); raise SystemExit(0)
oldshow=git("show",f"{before}:{KEY}")
if oldshow.returncode==0:
    try: old=json.loads(oldshow.stdout)
    except Exception as e:
        emit(False,f"old key parse failure {e}"); raise SystemExit(0)
else: old={"generation":0,"armed":False}
checks=[
 (new.get("schema")=="STAGE34_02_D2_FIBER_PRODUCT_MW_RUNKEY_V1","schema"),
 (new.get("armed") is True,"armed"),
 (isinstance(new.get("generation"),int) and new["generation"]>int(old.get("generation",0)),"generation"),
 (new.get("prime_panel")==[107,109,113,127],"prime_panel"),
 (new.get("cases")==14,"cases"),
 (new.get("planned_heavy_jobs")==1,"jobs"),
 (new.get("effective_heavy_concurrency")==1,"concurrency"),
 (new.get("artifact_max_bytes")==1048576,"artifact_cap"),
 (new.get("retention_days")==1,"retention"),
]
fail=[n for ok,n in checks if not ok]
if fail: emit(False,"semantic gate failed: "+",".join(fail)); raise SystemExit(0)
emit(True,f"generation {new['generation']} explicitly armed")
