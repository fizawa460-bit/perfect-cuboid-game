#!/usr/bin/env python3
import json,pathlib,subprocess,sys
KEY="stages/stage34/runkeys/stage34-02-d2-conjugate-exception.json"
def emit(ok,r): print(f"authorized={'true' if ok else 'false'}"); print("reason="+r.replace("\n"," "))
def git(*a): return subprocess.run(["git",*a],text=True,capture_output=True)
if len(sys.argv)!=3: emit(False,"usage requires BEFORE HEAD"); raise SystemExit(0)
before,head=sys.argv[1],sys.argv[2]
if not before or not head or git("cat-file","-e",f"{before}^{{commit}}").returncode: emit(False,"before/head unavailable"); raise SystemExit(0)
d=git("diff","--name-only",before,head)
if d.returncode or KEY not in d.stdout.splitlines(): emit(False,"dedicated run-key not changed in actual commit range"); raise SystemExit(0)
try:new=json.loads(pathlib.Path(KEY).read_text())
except Exception as e: emit(False,f"new key parse failure {e}"); raise SystemExit(0)
o=git("show",f"{before}:{KEY}")
old=json.loads(o.stdout) if o.returncode==0 else {"generation":0,"armed":False}
checks=[(new.get("schema")=="STAGE34_02_D2_CONJUGATE_EXCEPTION_RUNKEY_V1","schema"),(new.get("armed") is True,"armed"),(isinstance(new.get("generation"),int) and new["generation"]>int(old.get("generation",0)),"generation"),(new.get("cases")==14,"cases"),(new.get("planned_heavy_jobs")==1,"jobs"),(new.get("effective_heavy_concurrency")==1,"concurrency"),(new.get("artifact_max_bytes")==1048576,"artifact"),(new.get("retention_days")==1,"retention")]
f=[n for ok,n in checks if not ok]
if f: emit(False,"semantic gate failed: "+",".join(f)); raise SystemExit(0)
emit(True,f"generation {new['generation']} explicitly armed")
