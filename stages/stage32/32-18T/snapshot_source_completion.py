#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, pathlib, re, subprocess, tempfile, urllib.request, zipfile

EXCLUDED={0,15,63,64,173}
BULK_IDS=[i for i in range(256) if i not in EXCLUDED]
HOT_IDS=[i for i in BULK_IDS if i<64]
REGULAR_IDS=[i for i in BULK_IDS if i>=64]
PATTERNS=[
    re.compile(r'^stage32-18p-b14-bulk-packet-(\d+)-g1$'),
    re.compile(r'^stage32-18p-b14-packet-(\d+)-g1$'),
]

def api_json(url:str,token:str):
    req=urllib.request.Request(url,headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'stage32-18t'})
    with urllib.request.urlopen(req) as r: return json.load(r)

def list_artifacts(repo:str,run:int,token:str):
    out=[]; page=1
    while True:
        d=api_json(f'https://api.github.com/repos/{repo}/actions/runs/{run}/artifacts?per_page=100&page={page}',token)
        xs=d.get('artifacts',[]); out.extend(xs)
        if len(xs)<100: break
        page+=1
    return out

def artifact_packet_id(name:str):
    for rx in PATTERNS:
        m=rx.match(name)
        if m: return int(m.group(1))
    return None

def read_certificate(repo:str,a:dict,token:str,tmp:pathlib.Path):
    zpath=tmp/f'{int(a["id"])}.zip'
    subprocess.run(['curl','-L','--fail','--silent','--show-error','-H',f'Authorization: Bearer {token}','-H','X-GitHub-Api-Version: 2022-11-28','-o',str(zpath),f'https://api.github.com/repos/{repo}/actions/artifacts/{int(a["id"])}/zip'],check=True)
    with zipfile.ZipFile(zpath) as z:
        names=[n for n in z.namelist() if n.endswith('packet-certificate.json')]
        if len(names)!=1: raise RuntimeError(f'artifact {a["name"]}: expected one packet certificate, got {names}')
        d=json.loads(z.read(names[0]))
    zpath.unlink(missing_ok=True)
    return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True); ap.add_argument('--run-id',type=int,required=True); ap.add_argument('--output',type=pathlib.Path,required=True)
    a=ap.parse_args(); token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token: raise RuntimeError('GH_TOKEN required')
    artifacts=list_artifacts(a.repo,a.run_id,token)
    complete={}; walls={}; inspected=[]
    with tempfile.TemporaryDirectory() as td:
        tmp=pathlib.Path(td)
        for art in artifacts:
            pid=artifact_packet_id(art.get('name',''))
            if pid is None or pid not in BULK_IDS or art.get('expired'): continue
            d=read_certificate(a.repo,art,token,tmp)
            if int(d.get('packet_id',-1))!=pid: raise RuntimeError(f'packet id mismatch for artifact {art["name"]}')
            inspected.append({'packet_id':pid,'artifact_id':int(art['id']),'artifact_name':art['name'],'artifact_digest':art.get('digest'),'status':d.get('status')})
            if d.get('status')=='COMPLETE' and d.get('TRAVERSAL_COMPLETENESS_CERTIFICATE') is True:
                complete[pid]=inspected[-1]
            else:
                walls[pid]=inspected[-1]
    complete_ids=sorted(complete)
    missing=sorted(set(BULK_IDS)-set(complete_ids))
    missing_hot=[i for i in missing if i<64]
    missing_regular=[i for i in missing if i>=64]
    hot_matrix=[{'packet_id':pid,'subshard':s} for pid in missing_hot for s in range(4)]
    if len(hot_matrix)>256 or len(missing_regular)>256: raise RuntimeError('matrix exceeds GitHub limit')
    out={
      'schema':'STAGE32_18T_B14_SOURCE_COMPLETION_SNAPSHOT_V1','source_run_id':a.run_id,
      'bulk_expected_ids':BULK_IDS,'source_complete_ids':complete_ids,'source_resource_wall_ids':sorted(walls),
      'missing_bulk_ids':missing,'missing_hot_ids':missing_hot,'missing_regular_ids':missing_regular,
      'hot_subshard_count':4,'hot_matrix':hot_matrix,'regular_matrix':{'packet_id':missing_regular},
      'complete_artifacts':[complete[i] for i in complete_ids],'inspected_artifact_count':len(inspected),
      'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING'
    }
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'source_complete':len(complete_ids),'missing_hot':len(missing_hot),'missing_regular':len(missing_regular),'hot_jobs':len(hot_matrix),'walls':sorted(walls)},sort_keys=True))
if __name__=='__main__': main()
