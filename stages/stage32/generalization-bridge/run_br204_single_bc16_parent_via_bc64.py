#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,shutil,subprocess,sys,time
from pathlib import Path
from run_br204_resumable_bc64_hierarchical import PARENT_COUNT,CHILD_COUNT,req,gzip_deterministic,shard_name,validate,locate
def main():
 p=argparse.ArgumentParser()
 for k in ("shard-worker","combiner","group-combiner","worker-blob","out-dir"): p.add_argument("--"+k,required=True)
 p.add_argument("--b",type=int,required=True); p.add_argument("--d",type=int,required=True); p.add_argument("--parent-index",type=int,required=True)
 p.add_argument("--resume-dir",action="append",default=[]); p.add_argument("--child-timeout-seconds",type=int,default=1200); p.add_argument("--soft-seconds",type=int,default=5400)
 a=p.parse_args(); req((a.b,a.d,a.parent_index)==(2,148,0),"repair scope"); req(a.child_timeout_seconds>0 and a.soft_seconds>0,"timeouts")
 out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True); children=out/"children"; children.mkdir(exist_ok=True); parents=out/"parents"; parents.mkdir(exist_ok=True)
 roots=[Path(x) for x in a.resume_dir]; expected=list(range(a.parent_index,CHILD_COUNT,PARENT_COUNT)); req(expected==[0,16,32,48],"partition")
 started=time.monotonic(); recovered=[]; completed=[]; failed=None; stop=None
 def row(q,i): return {"idx":i,"name":q.name,"gzip_bytes":q.stat().st_size,"gzip_sha256":hashlib.sha256(q.read_bytes()).hexdigest()}
 def ck(done=False):
  cr=[]
  for i in expected:
   q=children/shard_name(a.b,a.d,i,CHILD_COUNT)
   if q.is_file(): cr.append(row(q,i))
  pp=parents/shard_name(a.b,a.d,a.parent_index,PARENT_COUNT)
  s={"schema":"STAGE32_BR204_SINGLE_EXPIRED_PARENT_REPAIR_V1","b":a.b,"d":a.d,"parent_index":a.parent_index,"parent_count":PARENT_COUNT,"child_count":CHILD_COUNT,"expected_child64_indices":expected,"worker_blob":a.worker_blob,"recovered_child64_indices":sorted(set(recovered)),"completed_child64_indices":sorted(set(completed)),"missing_child64_indices":sorted(set(expected)-set(completed)),"retained_child64_payloads":cr,"validated_parent_payload":row(pp,a.parent_index) if pp.is_file() else None,"complete":done,"failed_child64":failed,"stop_reason":stop or ("COMPLETE" if done else "IN_PROGRESS"),"elapsed_seconds":round(time.monotonic()-started,3),"credit":{"stage32_main":False,"full178_complete":False,"theorem":False,"effectivity":False,"receiver":False,"endpoint":False,"perfect_cuboid":False,"merge":False}}
  (out/"SINGLE-PARENT-REPAIR-STATUS.json").write_text(json.dumps(s,sort_keys=True,indent=2)+"\n")
 for i in expected:
  old=locate(roots+[children],a.combiner,a.worker_blob,a.b,a.d,i,CHILD_COUNT)
  if old:
   dst=children/shard_name(a.b,a.d,i,CHILD_COUNT)
   if old.resolve()!=dst.resolve(): shutil.copy2(old,dst)
   recovered.append(i); completed.append(i); ck(); continue
  if time.monotonic()-started>=a.soft_seconds: stop="SOFT_DEADLINE"; ck(); break
  plain=out/f"br204-f-b{a.b}-d{a.d}-bc{i}of64.tsv"; gz=children/shard_name(a.b,a.d,i,CHILD_COUNT)
  cmd=[a.shard_worker,"--b",str(a.b),"--d-lo",str(a.d),"--d-hi",str(a.d),"--bc-shard-index",str(i),"--bc-shard-count",str(CHILD_COUNT),"--worker-blob",a.worker_blob,"--out",str(plain)]
  try: cp=subprocess.run(cmd,timeout=a.child_timeout_seconds)
  except subprocess.TimeoutExpired: plain.unlink(missing_ok=True); failed=i; stop="SINGLE_BC64_CHILD_TIMEOUT_REQUIRES_FINER_PARTITION"; ck(); break
  if cp.returncode: plain.unlink(missing_ok=True); failed=i; stop=f"BC64_CHILD_WORKER_FAILURE_{cp.returncode}"; ck(); break
  validate(a.combiner,plain,a.worker_blob,a.b,a.d,i,CHILD_COUNT); gzip_deterministic(plain,gz); plain.unlink(); completed.append(i); ck()
 complete=sorted(set(completed))==expected
 if complete:
  plain=out/f"br204-f-b{a.b}-d{a.d}-bc0of16.tsv"
  cp=subprocess.run([sys.executable,a.group_combiner,"--input-dir",str(children),"--b",str(a.b),"--d",str(a.d),"--parent-index","0","--parent-count",str(PARENT_COUNT),"--child-count",str(CHILD_COUNT),"--worker-blob",a.worker_blob,"--out",str(plain)])
  req(cp.returncode==0,"union"); validate(a.combiner,plain,a.worker_blob,a.b,a.d,0,PARENT_COUNT)
  gz=parents/shard_name(a.b,a.d,0,PARENT_COUNT); gzip_deterministic(plain,gz); plain.unlink(); stop="COMPLETE"; ck(True)
 elif stop is None: stop="PARTIAL_UNKNOWN"; ck()
 print((out/"SINGLE-PARENT-REPAIR-STATUS.json").read_text().strip())
 if not complete: raise SystemExit(75 if stop=="SOFT_DEADLINE" else 76)
if __name__=="__main__": main()
