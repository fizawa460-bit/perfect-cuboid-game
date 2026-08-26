#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, re, shutil, subprocess, tempfile, time, urllib.error, urllib.request, zipfile

EXCLUDED={0,15,63,64,173}
BULK_IDS=[i for i in range(256) if i not in EXCLUDED]
HOT_IDS=[i for i in BULK_IDS if i<64]
REGULAR_IDS=[i for i in BULK_IDS if i>=64]
SOURCE_PATTERNS=[
    re.compile(r'^stage32-18p-b14-bulk-packet-(\d+)-g1$'),
    re.compile(r'^stage32-18p-b14-packet-(\d+)-g1$'),
]
REGULAR_JOB=re.compile(r'^(?:regular-packet|synthesize-hot) \((\d+)\)$')
HOT_JOB=re.compile(r'^hot-subshard \((\d+), (\d+)\)$')
REGULAR_ARTIFACT=re.compile(r'^stage32-18t-b14-packet-(\d+)-g[12]$')
RESIDUE_JSON=re.compile(r'^(?:.*/)?residue-runs/residue-(\d+)\.json$')
HOT_SCHEMA='STAGE32_18T_D16_B14_HOT_SUBSHARD_V1'
RESIDUE_SCHEMA='STAGE32_18E_D16_EXACT_SYMMETRY_SHARDED_TRAVERSAL_CERT_V1'
MAGIC=b'S32D16C1'; RECORD_SIZE=141
RETRYABLE_HTTP={429,500,502,503,504}

def api_json(url:str, token:str, attempts:int=7):
    last=None
    for n in range(attempts):
        req=urllib.request.Request(url,headers={
            'Authorization':f'Bearer {token}',
            'Accept':'application/vnd.github+json',
            'X-GitHub-Api-Version':'2022-11-28',
            'User-Agent':'stage32-18t',
        })
        try:
            with urllib.request.urlopen(req,timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code not in RETRYABLE_HTTP: raise
            last=e
        except urllib.error.URLError as e:
            last=e
        if n+1<attempts:
            delay=min(30,2**n)
            print(f'api retry {n+1}/{attempts-1} after {delay}s: {url}',flush=True)
            time.sleep(delay)
    raise last

def list_artifacts(repo:str, run:int, token:str):
    out=[]; page=1
    while True:
        d=api_json(f'https://api.github.com/repos/{repo}/actions/runs/{run}/artifacts?per_page=100&page={page}',token)
        xs=d.get('artifacts',[]); out.extend(xs)
        if len(xs)<100: break
        page+=1
    return out

def list_success_jobs_all_attempts(repo:str, run:int, token:str):
    meta=api_json(f'https://api.github.com/repos/{repo}/actions/runs/{run}',token)
    attempts=int(meta.get('run_attempt') or 1); out=[]
    for attempt in range(1,attempts+1):
        page=1
        while True:
            url=f'https://api.github.com/repos/{repo}/actions/runs/{run}/attempts/{attempt}/jobs?per_page=100&page={page}'
            try:
                d=api_json(url,token)
            except urllib.error.HTTPError as e:
                if e.code==404 and attempt==attempts:
                    d=api_json(f'https://api.github.com/repos/{repo}/actions/runs/{run}/jobs?filter=latest&per_page=100&page={page}',token)
                else: raise
            xs=d.get('jobs',[])
            out.extend(j for j in xs if j.get('status')=='completed' and j.get('conclusion')=='success')
            if len(xs)<100: break
            page+=1
    return out

def source_packet_id(name:str):
    for rx in SOURCE_PATTERNS:
        m=rx.match(name)
        if m: return int(m.group(1))
    return None

def download_zip(repo:str, artifact_id:int, token:str, zpath:pathlib.Path):
    subprocess.run([
        'curl','-L','--fail','--silent','--show-error','--retry','6','--retry-all-errors','--retry-delay','2',
        '-H',f'Authorization: Bearer {token}','-H','X-GitHub-Api-Version: 2022-11-28',
        '-o',str(zpath),f'https://api.github.com/repos/{repo}/actions/artifacts/{artifact_id}/zip',
    ],check=True)

def read_zip_json(zpath:pathlib.Path, suffix:str):
    with zipfile.ZipFile(zpath) as z:
        names=[n for n in z.namelist() if n.endswith(suffix)]
        if len(names)!=1: raise RuntimeError(f'{zpath.name}: expected one {suffix}, got {names}')
        return json.loads(z.read(names[0]))

def extract_zip(zpath:pathlib.Path, dst:pathlib.Path):
    dst.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(zpath) as z: z.extractall(dst)

def source_certificate(repo:str, art:dict, token:str, tmp:pathlib.Path):
    zpath=tmp/f'source-{int(art["id"])}.zip'; download_zip(repo,int(art['id']),token,zpath)
    d=read_zip_json(zpath,'packet-certificate.json'); zpath.unlink(missing_ok=True); return d

def choose_valid_packet_artifact(repo:str, arts:list[dict], pid:int, token:str, tmp:pathlib.Path):
    for art in sorted(arts,key=lambda x:int(x['id']),reverse=True):
        if art.get('expired'): continue
        zpath=tmp/f'packet-{int(art["id"])}.zip'
        try:
            download_zip(repo,int(art['id']),token,zpath); d=read_zip_json(zpath,'packet-certificate.json')
            ok=(int(d.get('packet_id',-1))==pid and d.get('status')=='COMPLETE'
                and d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is True and int(d.get('bound',-1))==14)
            if ok: return art,zpath,d
        except Exception: pass
        zpath.unlink(missing_ok=True)
    return None

def choose_valid_hot_artifact(repo:str, arts:list[dict], pid:int, sid:int, token:str, tmp:pathlib.Path):
    for art in sorted(arts,key=lambda x:int(x['id']),reverse=True):
        if art.get('expired'): continue
        zpath=tmp/f'hot-{int(art["id"])}.zip'
        try:
            download_zip(repo,int(art['id']),token,zpath); d=read_zip_json(zpath,f'hot-packet-{pid}-sub-{sid}.json')
            ok=(d.get('schema')==HOT_SCHEMA and d.get('status')=='COMPLETE' and int(d.get('bound',-1))==14
                and int(d.get('secondary_shard_id',-1))==sid and int(d.get('secondary_shard_count',-1))==4
                and d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is True)
            if ok:
                with zipfile.ZipFile(zpath) as z:
                    bins=[n for n in z.namelist() if n.endswith(f'hot-packet-{pid}-sub-{sid}.bin')]
                    if len(bins)!=1: ok=False
            if ok: return art,zpath,d
        except Exception: pass
        zpath.unlink(missing_ok=True)
    return None

def valid_residue_pair(z:zipfile.ZipFile, jname:str, r:int):
    try:
        d=json.loads(z.read(jname)); bname=jname[:-5]+'.bin'; raw=z.read(bname)
    except Exception:
        return None
    ok=(d.get('schema')==RESIDUE_SCHEMA and d.get('status')=='COMPLETE' and int(d.get('bound',-1))==14
        and (int(d.get('shard_id',-1)),int(d.get('shard_count',-1)),int(d.get('split_coordinate',-1)))==(r,1024,54)
        and d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is True
        and d.get('all_symmetry_branch_rejections_exact_rational_cauchy_schwarz') is True)
    if not ok or raw[:8]!=MAGIC or len(raw[8:])%RECORD_SIZE: return None
    if hashlib.sha256(raw).hexdigest()!=d.get('canonical_dump_sha256'): return None
    if len(raw[8:])//RECORD_SIZE!=int(d.get('canonical_survivors_including_zero',-1)): return None
    return d,bname,raw

def salvage_regular_residues(repo:str, arts:list[dict], pid:int, token:str, tmp:pathlib.Path, dst:pathlib.Path):
    salvaged={}
    for art in sorted(arts,key=lambda x:int(x['id']),reverse=True):
        if art.get('expired'): continue
        zpath=tmp/f'regular-partial-{pid}-{int(art["id"])}.zip'
        try:
            download_zip(repo,int(art['id']),token,zpath)
            with zipfile.ZipFile(zpath) as z:
                for jname in z.namelist():
                    m=RESIDUE_JSON.match(jname)
                    if not m: continue
                    r=int(m.group(1))
                    if r in salvaged: continue
                    got=valid_residue_pair(z,jname,r)
                    if not got: continue
                    d,bname,raw=got
                    rr=dst/'residue-runs'; rr.mkdir(parents=True,exist_ok=True)
                    (rr/f'residue-{r}.json').write_bytes(z.read(jname)); (rr/f'residue-{r}.bin').write_bytes(raw)
                    salvaged[r]={'packet_id':pid,'residue':r,'artifact_id':int(art['id']),'artifact_name':art['name'],
                        'artifact_digest':art.get('digest'),'nodes':int(d.get('nodes',0))}
        except Exception:
            pass
        zpath.unlink(missing_ok=True)
    return salvaged

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True); ap.add_argument('--run-id',type=int,required=True)
    ap.add_argument('--carry-run-id',type=int,action='append',default=[]); ap.add_argument('--carry-dir',type=pathlib.Path)
    ap.add_argument('--output',type=pathlib.Path,required=True); a=ap.parse_args()
    token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token: raise RuntimeError('GH_TOKEN required')
    carry_dir=a.carry_dir or (a.output.parent/'carryover'); carry_dir.mkdir(parents=True,exist_ok=True)

    artifacts=list_artifacts(a.repo,a.run_id,token); complete={}; walls={}; inspected=[]
    with tempfile.TemporaryDirectory() as td:
        tmp=pathlib.Path(td)
        for art in artifacts:
            pid=source_packet_id(art.get('name',''))
            if pid is None or pid not in BULK_IDS or art.get('expired'): continue
            d=source_certificate(a.repo,art,token,tmp)
            if int(d.get('packet_id',-1))!=pid: raise RuntimeError(f'packet id mismatch for artifact {art["name"]}')
            rec={'packet_id':pid,'artifact_id':int(art['id']),'artifact_name':art['name'],'artifact_digest':art.get('digest'),'status':d.get('status')}
            inspected.append(rec)
            if d.get('status')=='COMPLETE' and d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is True: complete[pid]=rec
            else: walls[pid]=rec

        source_complete_ids=sorted(complete); source_missing=sorted(set(BULK_IDS)-set(source_complete_ids))
        carry_packet={}; carry_hot={}; carry_regular_residue={}; carry_audit=[]
        carry_artifacts_by_run={}
        for run in a.carry_run_id:
            jobs=list_success_jobs_all_attempts(a.repo,run,token); run_arts=list_artifacts(a.repo,run,token); carry_artifacts_by_run[run]=run_arts
            by_name={}
            for art in run_arts: by_name.setdefault(art.get('name',''),[]).append(art)
            for j in jobs:
                name=j.get('name',''); m=REGULAR_JOB.match(name)
                if m:
                    pid=int(m.group(1))
                    if pid not in BULK_IDS: continue
                    aname=f'stage32-18t-b14-packet-{pid}-g1'
                    got=choose_valid_packet_artifact(a.repo,by_name.get(aname,[]),pid,token,tmp)
                    if got:
                        art,zpath,d=got; dst=carry_dir/'packets'/str(pid)
                        if dst.exists(): shutil.rmtree(dst)
                        extract_zip(zpath,dst); zpath.unlink(missing_ok=True)
                        carry_packet[pid]={'run_id':run,'job_id':int(j['id']),'job_name':name,'artifact_id':int(art['id']),'artifact_name':art['name'],'artifact_digest':art.get('digest')}
                        carry_audit.append({'kind':'packet','packet_id':pid,**carry_packet[pid]})
                    continue
                m=HOT_JOB.match(name)
                if m:
                    pid,sid=map(int,m.groups())
                    if pid not in HOT_IDS or sid not in range(4): continue
                    aname=f'stage32-18t-b14-hot-packet-{pid}-sub-{sid}-of4-g1'
                    got=choose_valid_hot_artifact(a.repo,by_name.get(aname,[]),pid,sid,token,tmp)
                    if got:
                        art,zpath,d=got; dst=carry_dir/'hot'/str(pid)/str(sid)
                        if dst.exists(): shutil.rmtree(dst)
                        extract_zip(zpath,dst); zpath.unlink(missing_ok=True)
                        carry_hot[(pid,sid)]={'run_id':run,'job_id':int(j['id']),'job_name':name,'artifact_id':int(art['id']),'artifact_name':art['name'],'artifact_digest':art.get('digest')}
                        carry_audit.append({'kind':'hot-subshard','packet_id':pid,'subshard':sid,**carry_hot[(pid,sid)]})

        carry_packet_ids=sorted(set(carry_packet)&set(source_missing))
        remaining=sorted(set(source_missing)-set(carry_packet_ids))
        # Unlike whole-packet carry, exact residue carry does not require the parent job to have succeeded.
        # A cancelled job may have uploaded one or more independently COMPLETE residue certificates.
        for run,run_arts in carry_artifacts_by_run.items():
            by_pid={}
            for art in run_arts:
                m=REGULAR_ARTIFACT.match(art.get('name',''))
                if m: by_pid.setdefault(int(m.group(1)),[]).append(art)
            for pid in remaining:
                if pid not in REGULAR_IDS: continue
                got=salvage_regular_residues(a.repo,by_pid.get(pid,[]),pid,token,tmp,carry_dir/'regular'/str(pid))
                for r,meta in got.items():
                    key=(pid,r)
                    if key not in carry_regular_residue:
                        carry_regular_residue[key]={'run_id':run,**meta}
                        carry_audit.append({'kind':'regular-residue',**carry_regular_residue[key]})

    missing_hot=[i for i in remaining if i<64]; missing_regular=[i for i in remaining if i>=64]
    carry_hot_pairs={(p,s) for (p,s) in carry_hot if p in missing_hot}
    hot_matrix=[{'packet_id':pid,'subshard':s} for pid in missing_hot for s in range(4) if (pid,s) not in carry_hot_pairs]
    hot_compute_ids=sorted({int(row['packet_id']) for row in hot_matrix})
    if len(hot_matrix)>256 or len(missing_regular)>256: raise RuntimeError('matrix exceeds GitHub limit')
    regular_residue_rows=[{'packet_id':p,'residue':r,**carry_regular_residue[(p,r)]} for p,r in sorted(carry_regular_residue) if p in missing_regular]

    out={'schema':'STAGE32_18T_B14_RESUME_UNION_SNAPSHOT_V3','source_run_id':a.run_id,'carry_run_ids':a.carry_run_id,
      'bulk_expected_ids':BULK_IDS,'source_complete_ids':source_complete_ids,'source_missing_bulk_ids':source_missing,
      'carry_complete_packet_ids':carry_packet_ids,
      'carry_complete_hot_subshards':[{'packet_id':p,'subshard':s,**carry_hot[(p,s)]} for p,s in sorted(carry_hot_pairs)],
      'carry_complete_regular_residues':regular_residue_rows,'carry_complete_regular_residue_count':len(regular_residue_rows),
      'source_resource_wall_ids':sorted(walls),'missing_bulk_ids':remaining,'missing_hot_ids':missing_hot,'missing_regular_ids':missing_regular,
      'hot_subshard_count':4,'hot_matrix':hot_matrix,'hot_compute_ids':hot_compute_ids,'hot_packet_matrix':{'packet_id':missing_hot},
      'regular_matrix':{'packet_id':missing_regular},'complete_artifacts':[complete[i] for i in source_complete_ids],
      'carry_packet_artifacts':[carry_packet[i] for i in carry_packet_ids],'carry_audit':carry_audit,'inspected_artifact_count':len(inspected),
      'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING'}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'source_complete':len(source_complete_ids),'carry_complete_packets':len(carry_packet_ids),
        'carry_hot_subshards':len(carry_hot_pairs),'carry_regular_residues':len(regular_residue_rows),
        'missing_hot_packets':len(missing_hot),'missing_hot_jobs':len(hot_matrix),'missing_regular':len(missing_regular),'walls':sorted(walls)},sort_keys=True))
if __name__=='__main__': main()
