#!/usr/bin/env python3
import json,pathlib,subprocess,sys
KEY="stages/stage34/runkeys/stage34-02-d2-quartic-maps.json"

def git(*args): return subprocess.run(["git",*args],text=True,capture_output=True)
def emit(ok,reason):
    print(f"authorized={'true' if ok else 'false'}")
    print("reason="+reason.replace("\n"," ").replace("\r"," "))
if len(sys.argv)!=3:
    emit(False,"usage requires BEFORE HEAD"); raise SystemExit(0)
before,head=sys.argv[1],sys.argv[2]
if not before or not head or git("cat-file","-e",f"{before}^{{commit}}").returncode!=0:
    emit(False,"before/head unavailable"); raise SystemExit(0)
chg=git("diff","--name-only",before,head)
if chg.returncode!=0 or KEY not in chg.stdout.splitlines():
    emit(False,"dedicated run-key not changed in actual commit range"); raise SystemExit(0)
try: new=json.loads(pathlib.Path(KEY).read_text())
except Exception as e: emit(False,f"new key parse failure: {e}"); raise SystemExit(0)
oldp=git("show",f"{before}:{KEY}")
old=json.loads(oldp.stdout) if oldp.returncode==0 else {"generation":0,"armed":False}
checks=[
(new.get("schema")=="STAGE34_02_D2_QUARTIC_MAP_RUNKEY_V1","schema"),
(new.get("armed") is True,"armed"),
(isinstance(new.get("generation"),int) and new["generation"]>int(old.get("generation",0)),"generation"),
(new.get("cases")==14,"cases"),(new.get("planned_heavy_jobs")==1,"jobs"),
(new.get("effective_heavy_concurrency")==1,"concurrency"),
(new.get("artifact_max_bytes")==1048576,"artifact"),(new.get("retention_days")==1,"retention")]
bad=[n for ok,n in checks if not ok]
if bad: emit(False,"semantic gate failed: "+",".join(bad)); raise SystemExit(0)
emit(True,f"generation {new['generation']} explicitly armed")
