#!/usr/bin/env python3
import json,pathlib,subprocess,sys
KEY="stages/stage34/runkeys/stage34-02-d2-stageA2-rank1-mw-congruence-sieve.json"
def emit(ok,reason):
 print(f"authorized={'true' if ok else 'false'}");print("reason="+reason.replace("\n"," ").replace("\r"," "))
def git(*a):return subprocess.run(["git",*a],text=True,capture_output=True)
if len(sys.argv)!=3:emit(False,"usage requires BEFORE HEAD");raise SystemExit(0)
before,head=sys.argv[1],sys.argv[2]
if not before or not head or git("cat-file","-e",f"{before}^{{commit}}").returncode:emit(False,"before/head unavailable");raise SystemExit(0)
d=git("diff","--name-only",before,head)
if d.returncode or KEY not in d.stdout.splitlines():emit(False,"dedicated run-key not changed");raise SystemExit(0)
try:new=json.loads(pathlib.Path(KEY).read_text())
except Exception as e:emit(False,f"new key parse failure {e}");raise SystemExit(0)
o=git("show",f"{before}:{KEY}")
if o.returncode==0:
 try:old=json.loads(o.stdout)
 except Exception as e:emit(False,f"old key parse failure {e}");raise SystemExit(0)
else:old={"generation":0}
checks=[
(new.get("schema")=="STAGE34_02_D2_STAGEA2_RANK1_MW_CONGRUENCE_SIEVE_RUNKEY_V1","schema"),
(new.get("armed") is True,"armed"),
(isinstance(new.get("generation"),int) and new["generation"]>int(old.get("generation",0)),"generation"),
(new.get("expected_input_branches")==76,"input"),(new.get("expected_closed_branches")==24,"closed"),(new.get("expected_remaining_branches")==52,"remaining"),
(new.get("prime_bound")==211,"prime_bound"),(new.get("max_primes_per_branch")==12,"max_primes"),(new.get("state_cap_per_torsion_translate")==300000,"state_cap"),
(new.get("planned_heavy_jobs")==0,"heavy_jobs"),(new.get("artifact_max_bytes")==1048576,"artifact_cap"),(new.get("retention_days")==1,"retention")]
fail=[n for ok,n in checks if not ok]
if fail:emit(False,"semantic gate failed: "+",".join(fail));raise SystemExit(0)
emit(True,f"generation {new['generation']} explicitly armed")
